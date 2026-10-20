#!/usr/bin/env python3
"""Build a session folder from a Cockatrice .cod file.

Run only when the user asks to generate a deck structure. This is not part of
the pitch, commander, or mechanics gates.
"""

from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from datetime import date
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from deckio import (
    REPO_ROOT,
    load_deck,
    load_printings,
    merge_printings,
    save_printings,
    write_cod,
)
from generate_printings import process_deck
from scryfall import Scryfall, parse_commander_flag

DECKS_ROOT = REPO_ROOT / "decks"
INDEX_PATH = DECKS_ROOT / "_index.md"
DATE_RE = re.compile(r"\d{4}-\d{2}-\d{2}")
COMMANDER_COMMENT_RE = re.compile(r"Commander:\s*(.+)", re.I)
BRACKET_RE = re.compile(r"Bracket\s+\d+", re.I)


def slugify(name: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", name.lower()).strip("-")
    return slug or "deck"


def read_cod_header(path: Path) -> tuple[str, str]:
    root = ET.parse(path).getroot()
    tag = root.tag.rsplit("}", 1)[-1]
    if tag != "cockatrice_deck":
        raise ValueError(f"not a cockatrice_deck: {path}")
    fmt = (root.findtext("format") or "").strip().lower()
    comments = (root.findtext("comments") or "").strip()
    return fmt, comments


def commanders_from_comment(comments: str) -> list[str]:
    match = COMMANDER_COMMENT_RE.search(comments)
    if not match:
        return []
    raw = re.split(r"[.\n]", match.group(1).strip(), maxsplit=1)[0].strip()
    return parse_commander_flag(raw)


def infer_format(
    explicit: str | None,
    xml_format: str,
    commanders: list[str],
    main_total: int,
    side_total: int,
) -> str:
    if explicit:
        return explicit
    if xml_format in {"commander", "pauper"}:
        return xml_format
    if commanders:
        return "commander"
    if main_total == 100 and side_total == 0:
        return "commander"
    if main_total == 60:
        return "pauper"
    raise ValueError("cannot infer format; pass --format commander or pauper")


def ordered_main(main: Counter[str], commanders: list[str]) -> list[tuple[str, int]]:
    seen: set[str] = set()
    ordered: list[tuple[str, int]] = []
    for name in commanders:
        if name in main and name not in seen:
            ordered.append((name, main[name]))
            seen.add(name)
    for name, count in main.items():
        if name not in seen:
            ordered.append((name, count))
    return ordered


def render_list(main: Counter[str], side: Counter[str], commanders: list[str]) -> str:
    lines = [f"{count} {name}" for name, count in ordered_main(main, commanders)]
    if side:
        lines.append("Sideboard")
        lines.extend(f"{count} {name}" for name, count in side.items())
    return "\n".join(lines) + "\n"


def official_comments(fmt: str, source: Path, commanders: list[str]) -> str:
    lines = [
        "Official artifact from deck assembler.",
        f"Source: {source.as_posix()}",
        f"Format: {fmt}",
    ]
    if commanders:
        lines.append("Commander: " + ", ".join(commanders))
    return "\n".join(lines)


def write_intake(
    path: Path,
    *,
    source: Path,
    deckname: str,
    fmt: str,
    commanders: list[str],
    bracket: str,
) -> None:
    who = ", ".join(commanders) or deckname
    text = f"""# Stage 0 — Intake

- **Idea:** Imported from a Cockatrice deck. Creative gates were not run.
- **Format:** {fmt}
- **Bracket / power target:** {bracket}
- **Colors / identity:**
- **Refusal / keep:**

## Source

- Import: `{source}`
- Deck name: {deckname}
- Commander / shell: {who}
- Session copies: `baseline-from-import.cod`, `baseline-from-import.txt`

## Gate status

| Stage | Status |
| --- | --- |
| Commanders | Skipped — imported list |
| Mechanics | Skipped — imported list |
| Full list | Imported |
"""
    path.write_text(text, encoding="utf-8")


def write_commanders_stub(
    path: Path, *, fmt: str, commanders: list[str], deckname: str
) -> None:
    who = ", ".join(commanders) or deckname
    text = f"""# Stage 1 — Commanders / shells

- **Idea:** Imported from Cockatrice. No shortlist was proposed.
- **Format:** {fmt}
- **Bracket / role target:**
- **Colors / identity (if known):**
- **Scryfall queries used:** none

## Locked pick

### {who}

Imported from the source `.cod`. The commander or shell is already chosen.

## Stop

Gate skipped. The list already exists.
"""
    path.write_text(text, encoding="utf-8")


def write_mechanics_stub(
    path: Path, *, fmt: str, commanders: list[str], deckname: str
) -> None:
    who = ", ".join(commanders) or deckname
    text = f"""# Stage 2 — Mechanics

- **Pick:** {who}
- **Format:** {fmt}
- **Bracket / role target:**
- **Idea reminder:** Imported list. Mechanics were not proposed.

## Plans

No plans were proposed. The imported list is the deck.

## Stop

Gate skipped.
"""
    path.write_text(text, encoding="utf-8")


def write_deck_notes(
    path: Path,
    *,
    deckname: str,
    fmt: str,
    commanders: list[str],
    bracket: str,
    list_text: str,
    validate_output: str,
) -> None:
    who = ", ".join(commanders)
    text = f"""# Stage 3 — Deck

- **Name:** {deckname}
- **Format:** {fmt}
- **Commander / shell:** {who}
- **Mechanic:**
- **Bracket (EDH) or role (Pauper):** {bracket}
- **Game Changers (EDH):**
- **Expensive cards to flag:**

## Game plan

## Categories

Counts should match `deck.cod` / `list.txt`.

- **Commander:**
- **Ramp / mana:**
- **Card advantage:**
- **Interaction:**
- **Engine / synergy:**
- **Win conditions:**
- **Lands:**
- **Sideboard (Pauper):**

## Official artifact

[`deck.cod`](deck.cod) — Cockatrice XML written by `python3 scripts/create_from_cod.py`. Preferred prints from `preferences/printings.json` and the imported file are applied.

## Import

Working copy (`list.txt`):

```
{list_text.rstrip()}
```

## Validate

```
{validate_output.rstrip()}
```
"""
    path.write_text(text, encoding="utf-8")


def run_validate(deck_path: Path, fmt: str, commanders: list[str]) -> tuple[int, str]:
    cmd = [
        sys.executable,
        str(_SCRIPTS / "scryfall.py"),
        "validate",
        str(deck_path),
        "--format",
        fmt,
    ]
    if fmt == "commander" and commanders:
        cmd.extend(["--commander", " / ".join(commanders)])
    proc = subprocess.run(
        cmd,
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    output = "".join(part for part in (proc.stdout, proc.stderr) if part).strip()
    return proc.returncode, output or "(no validate output)"


def prepend_index(date_s: str, slug: str, fmt: str, who: str, status: str) -> None:
    if not INDEX_PATH.is_file():
        raise FileNotFoundError(INDEX_PATH)
    lines = INDEX_PATH.read_text(encoding="utf-8").splitlines()
    row = f"| {date_s} | {slug} | {fmt} | {who} | {status} |"
    insert_at = None
    for i, line in enumerate(lines):
        if line.startswith("| ---"):
            insert_at = i + 1
            break
    if insert_at is None:
        raise ValueError(f"no table header in {INDEX_PATH}")
    lines.insert(insert_at, row)
    INDEX_PATH.write_text("\n".join(lines) + "\n", encoding="utf-8")


def create_from_cod(
    source: Path,
    *,
    slug: str | None,
    fmt: str | None,
    commander: str | None,
    when: str | None,
    name: str | None,
) -> tuple[Path, int]:
    source = source.expanduser().resolve()
    if not source.is_file():
        raise FileNotFoundError(source)
    if source.suffix.lower() != ".cod":
        raise ValueError(f"expected a .cod file: {source}")

    main, side, zone_commanders, file_printings, file_name = load_deck(source)
    if not main and not side:
        raise ValueError(f"empty deck: {source}")

    xml_format, comments = read_cod_header(source)
    flag_commanders = parse_commander_flag(commander)
    commanders = flag_commanders or zone_commanders or commanders_from_comment(comments)
    deck_format = infer_format(
        fmt,
        xml_format,
        commanders,
        sum(main.values()),
        sum(side.values()),
    )
    deckname = name or file_name or source.stem
    session_slug = slug or slugify(deckname)
    session_date = when or date.today().isoformat()
    if not DATE_RE.fullmatch(session_date):
        raise ValueError("--date must be YYYY-MM-DD")

    folder = DECKS_ROOT / f"{session_date}-{session_slug}"
    if folder.exists():
        raise FileExistsError(f"session already exists: {folder}")
    folder.mkdir(parents=True)

    list_text = render_list(main, side, commanders)
    shutil.copyfile(source, folder / "baseline-from-import.cod")
    (folder / "baseline-from-import.txt").write_text(list_text, encoding="utf-8")
    (folder / "list.txt").write_text(list_text, encoding="utf-8")

    registry = merge_printings(load_printings(), file_printings)
    if file_printings:
        save_printings(registry)

    bracket_match = BRACKET_RE.search(comments)
    bracket = bracket_match.group(0) if bracket_match else ""
    write_intake(
        folder / "00-intake.md",
        source=source,
        deckname=deckname,
        fmt=deck_format,
        commanders=commanders,
        bracket=bracket,
    )
    write_commanders_stub(
        folder / "01-commanders.md",
        fmt=deck_format,
        commanders=commanders,
        deckname=deckname,
    )
    write_mechanics_stub(
        folder / "02-mechanics.md",
        fmt=deck_format,
        commanders=commanders,
        deckname=deckname,
    )
    write_cod(
        folder / "deck.cod",
        deckname=deckname,
        comments=official_comments(deck_format, source, commanders),
        main=main,
        side=side,
        commanders=commanders,
        printings=registry,
    )

    validate_code, validate_output = run_validate(
        folder / "deck.cod", deck_format, commanders
    )
    write_deck_notes(
        folder / "03-deck.md",
        deckname=deckname,
        fmt=deck_format,
        commanders=commanders,
        bracket=bracket,
        list_text=list_text,
        validate_output=validate_output,
    )
    print(validate_output)

    printings_code = process_deck(Scryfall(), folder)
    who = ", ".join(commanders) or deckname
    status = "done" if validate_code == 0 else "imported"
    prepend_index(session_date, session_slug, deck_format, who, status)
    print(folder)
    return folder, 0 if validate_code == 0 and printings_code == 0 else 1


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="create_from_cod.py",
        description="Create a session folder and printings from a Cockatrice .cod file.",
    )
    parser.add_argument("cod", type=Path, help="Cockatrice .cod to import")
    parser.add_argument("--slug", default=None, help="folder slug (default: from the deck name)")
    parser.add_argument("--format", choices=("commander", "pauper"), default=None)
    parser.add_argument("--commander", default=None, help='Commander name, or "A / B" for partners')
    parser.add_argument("--date", default=None, help="session date YYYY-MM-DD (default: today)")
    parser.add_argument("--name", default=None, help="deck title (default: Cockatrice deck name)")
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        _folder, code = create_from_cod(
            args.cod,
            slug=args.slug,
            fmt=args.format,
            commander=args.commander,
            when=args.date,
            name=args.name,
        )
    except (OSError, ValueError, ET.ParseError) as exc:
        print(exc, file=sys.stderr)
        return 1
    return code


if __name__ == "__main__":
    sys.exit(main())
