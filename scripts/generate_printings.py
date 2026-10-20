#!/usr/bin/env python3
"""Download each card's exact printing image from Scryfall for a deck session.

Resolves every unique card in a deck to its exact printing using
preferences/printings.json first; cards missing from that registry fall back
to Scryfall's default printing, which is then written back into the
registry so later runs (and to_cockatrice.py) reuse it.

Images are saved into decks/<slug>/printings/ with a zero-padded sequence
number prefix, e.g. "01 - Sol Ring.png", so a gap in the numbering makes an
incomplete folder obvious at a glance.

An image already downloaded under any decks/*/printings/ folder is copied
into the destination with this deck's sequence number. Scryfall is only
called for cards that have no local image yet.
"""

from __future__ import annotations

import argparse
import re
import shutil
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter
from pathlib import Path
from typing import Any

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from deckio import (
    REPO_ROOT,
    load_deck,
    load_printings,
    merge_printings,
    resolve_input,
    save_printings,
)
from scryfall import MIN_INTERVAL, Scryfall, ScryfallError, norm_name

INVALID_CHARS_RE = re.compile(r'[\\/:*?"<>|]')
PRINTING_FILE_RE = re.compile(
    r"^(?P<index>\d+)(?P<face>[a-h])? - (?P<name>.+?)"
    r"(?: \((?P<label>front|back)\))?\.(?P<ext>png|jpe?g)$",
    re.IGNORECASE,
)
IMAGE_TIMEOUT = 30
FACE_LETTERS = "abcdefgh"
USER_AGENT = "deck-assembler/0.1"
DEFAULT_OUT_DIRNAME = "printings"
DECKS_ROOT = REPO_ROOT / "decks"


def sanitize_filename(name: str) -> str:
    cleaned = INVALID_CHARS_RE.sub("", name)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned or "card"


class CachedPrinting:
    """Newest local image(s) for one card name, gathered from other decks."""

    def __init__(self) -> None:
        self.single: Path | None = None
        self.single_mtime = -1.0
        self.faces: dict[str, tuple[Path, float]] = {}

    def consider(self, path: Path, face: str, mtime: float) -> None:
        if face:
            previous = self.faces.get(face)
            if previous is None or mtime >= previous[1]:
                self.faces[face] = (path, mtime)
            return
        if mtime >= self.single_mtime:
            self.single = path
            self.single_mtime = mtime


def parse_printing_filename(filename: str) -> tuple[int, str, str] | None:
    match = PRINTING_FILE_RE.match(filename)
    if not match:
        return None
    face = (match.group("face") or "").lower()
    return int(match.group("index")), face, match.group("name")


def image_filename(index: int, width: int, suffix: str, safe_name: str, ext: str) -> str:
    filename = f"{index:0{width}d}{suffix} - {safe_name}"
    if suffix == "a":
        filename += " (front)"
    elif suffix == "b":
        filename += " (back)"
    if ext and not ext.startswith("."):
        ext = f".{ext}"
    return filename + (ext or ".png")


def _complete_files(
    single: Path | None, faces: dict[str, Path]
) -> list[tuple[str, Path]] | None:
    """A normal card is one file. A double-faced card is reused only with both faces."""
    if "a" in faces and "b" in faces:
        return [(face, faces[face]) for face in sorted(faces)]
    if single is not None:
        return [("", single)]
    return None


def reusable_files(entry: CachedPrinting | None) -> list[tuple[str, Path]] | None:
    if entry is None:
        return None
    faces = {face: path for face, (path, _mtime) in entry.faces.items()}
    return _complete_files(entry.single, faces)


def files_already_in_place(
    dest_dir: Path, index: int, card_name: str
) -> list[tuple[str, Path]] | None:
    """Return this deck's numbered files when they are already complete."""
    if not dest_dir.is_dir():
        return None
    key = norm_name(card_name)
    single: Path | None = None
    faces: dict[str, Path] = {}
    for path in dest_dir.iterdir():
        if not path.is_file():
            continue
        parsed = parse_printing_filename(path.name)
        if parsed is None:
            continue
        file_index, face, name = parsed
        if file_index != index or norm_name(name) != key:
            continue
        if face:
            faces[face] = path
        else:
            single = path
    if faces and not ("a" in faces and "b" in faces):
        return None
    return _complete_files(single, faces)


def index_local_printings(decks_root: Path, dest_dir: Path) -> dict[str, CachedPrinting]:
    """Index images under decks/*/printings/, skipping the destination folder."""
    indexed: dict[str, CachedPrinting] = {}
    if not decks_root.is_dir():
        return indexed
    dest_resolved = dest_dir.resolve()
    for folder in decks_root.iterdir():
        printings = folder / DEFAULT_OUT_DIRNAME
        if not printings.is_dir() or printings.resolve() == dest_resolved:
            continue
        for path in printings.iterdir():
            if not path.is_file():
                continue
            parsed = parse_printing_filename(path.name)
            if parsed is None:
                continue
            _index, face, name = parsed
            key = norm_name(name)
            try:
                mtime = path.stat().st_mtime
            except OSError:
                continue
            indexed.setdefault(key, CachedPrinting()).consider(path, face, mtime)
    return indexed


def ordered_unique_names(
    main: Counter[str], side: Counter[str], commanders: list[str]
) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for name in commanders:
        if name in main and name not in seen:
            ordered.append(name)
            seen.add(name)
    for name in main:
        if name not in seen:
            ordered.append(name)
            seen.add(name)
    for name in side:
        if name not in seen:
            ordered.append(name)
            seen.add(name)
    return ordered


def registry_lookup(
    registry: dict[str, dict[str, str]], name: str
) -> dict[str, str] | None:
    if name in registry:
        return registry[name]
    target = norm_name(name)
    for key, spec in registry.items():
        if norm_name(key) == target:
            return spec
    return None


def pick_image_url(uris: dict[str, Any] | None) -> str | None:
    if not uris:
        return None
    return uris.get("png") or uris.get("large") or uris.get("normal") or uris.get("small")


def image_targets(card: dict[str, Any]) -> list[tuple[str, str]]:
    """Return (suffix, url) pairs; suffix is '' unless a card has separate per-face art."""
    top_url = pick_image_url(card.get("image_uris"))
    if top_url:
        return [("", top_url)]
    faces = card.get("card_faces") or []
    targets: list[tuple[str, str]] = []
    for i, face in enumerate(faces):
        url = pick_image_url(face.get("image_uris"))
        if url:
            suffix = FACE_LETTERS[i] if len(faces) > 1 else ""
            targets.append((suffix, url))
    return targets


def url_extension(url: str) -> str:
    path = urllib.parse.urlsplit(url).path
    ext = Path(path).suffix
    return ext if ext else ".jpg"


def resolve_printing(
    api: Scryfall, registry: dict[str, dict[str, str]], name: str
) -> tuple[dict[str, Any] | None, dict[str, str] | None, str | None]:
    """Return (card_json, learned_spec_or_None, error_or_None)."""
    spec = registry_lookup(registry, name)
    if spec and spec.get("setShortName") and spec.get("collectorNumber"):
        try:
            card = api.by_set_number(spec["setShortName"], spec["collectorNumber"])
            return card, None, None
        except ScryfallError:
            pass  # registry entry stale/broken; fall through to default printing

    try:
        card = api.named(name, fuzzy=False)
    except ScryfallError as exc:
        if exc.status != 404:
            return None, None, str(exc)
        try:
            card = api.named(name, fuzzy=True)
        except ScryfallError as exc2:
            return None, None, str(exc2)

    learned = {
        "setShortName": str(card.get("set") or "").upper(),
        "collectorNumber": str(card.get("collector_number") or ""),
        "uuid": str(card.get("id") or ""),
    }
    learned = {k: v for k, v in learned.items() if v}
    return card, (learned or None), None


def download_image(url: str, dest: Path) -> None:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    with urllib.request.urlopen(req, timeout=IMAGE_TIMEOUT) as resp:
        dest.write_bytes(resp.read())


def process_deck(api: Scryfall, path: Path, *, out_dir: Path | None = None) -> int:
    source = resolve_input(path)
    folder = source.parent
    main, side, commanders, file_printings, _deckname = load_deck(source)
    if not main and not side:
        raise ValueError(f"empty deck: {source}")

    registry = merge_printings(load_printings(), file_printings)
    names = ordered_unique_names(main, side, commanders)
    total = len(names)
    width = max(2, len(str(total)))
    dest_dir = out_dir or (folder / DEFAULT_OUT_DIRNAME)
    dest_dir.mkdir(parents=True, exist_ok=True)
    cache = index_local_printings(DECKS_ROOT, dest_dir)

    learned_updates: dict[str, dict[str, str]] = {}
    errors: list[str] = []
    ok_count = 0
    present_count = 0
    reused_count = 0
    fetched_count = 0

    for index, name in enumerate(names, start=1):
        safe_name = sanitize_filename(name)
        existing = files_already_in_place(dest_dir, index, name)
        if existing:
            present_count += 1
            ok_count += 1
            print(f"{index:0{width}d} already present  {name}")
            continue

        cached = reusable_files(cache.get(norm_name(name)))
        if cached:
            copied = True
            for suffix, src in cached:
                dest_path = dest_dir / image_filename(index, width, suffix, safe_name, src.suffix)
                try:
                    shutil.copy2(src, dest_path)
                except OSError as exc:
                    copied = False
                    errors.append(f"{name}: could not copy local printing ({exc})")
                    print(f"ERROR {name}: could not copy local printing ({exc})")
                    break
            if not copied:
                continue
            reused_count += 1
            ok_count += 1
            source = cached[0][1].parent.parent.name
            print(f"{index:0{width}d} reused           {name}  (from {source})")
            continue

        card, learned, error = resolve_printing(api, registry, name)
        if error:
            errors.append(f"{name}: {error}")
            print(f"ERROR {name}: {error}")
            continue

        if learned:
            registry[name] = learned
            learned_updates[name] = learned

        targets = image_targets(card) if card else []
        if not targets:
            errors.append(f"{name}: no image available")
            print(f"ERROR {name}: no image available")
            continue

        saved_all = True
        for suffix, url in targets:
            dest_path = dest_dir / image_filename(
                index, width, suffix, safe_name, url_extension(url)
            )
            time.sleep(MIN_INTERVAL)
            try:
                download_image(url, dest_path)
            except (urllib.error.URLError, OSError) as exc:
                saved_all = False
                errors.append(f"{name}: image download failed ({exc})")
                print(f"ERROR {name}: image download failed ({exc})")

        if not saved_all:
            continue

        fetched_count += 1
        ok_count += 1
        status = "fetched (default printing, registered)" if learned else "OK"
        print(f"{index:0{width}d} {status:<38} {name}")

    if learned_updates:
        save_printings(registry)
        print(
            f"\nRegistered {len(learned_updates)} new printing(s) in preferences/printings.json"
        )

    print(
        f"\n{ok_count}/{total} card(s) in {dest_dir} "
        f"({reused_count} reused, {present_count} already present, {fetched_count} fetched)"
    )
    if errors:
        print(f"{len(errors)} error(s):")
        for err in errors:
            print(f"  - {err}")
        return 1
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="generate_printings.py",
        description="Download each card's exact printing image into decks/<slug>/printings/.",
    )
    parser.add_argument(
        "path",
        type=Path,
        help="session folder, list.txt, or deck.cod",
    )
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help=f"output directory (default: <session>/{DEFAULT_OUT_DIRNAME})",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    api = Scryfall()
    try:
        return process_deck(api, args.path, out_dir=args.out)
    except (OSError, ValueError, FileNotFoundError) as exc:
        print(exc, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
