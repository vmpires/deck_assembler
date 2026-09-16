#!/usr/bin/env python3
"""Convert any harness deck to Cockatrice .cod — the official artifact."""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))

from deckio import (
    load_deck,
    load_printings,
    merge_printings,
    resolve_input,
    save_printings,
    session_meta,
    write_cod,
)

OFFICIAL_NAME = "deck.cod"


def _comments(meta: dict[str, str], source: Path, commanders: list[str]) -> str:
    lines = [
        "Official artifact from deck assembler.",
        f"Source: {source.as_posix()}",
    ]
    if meta.get("format"):
        lines.append(f"Format: {meta['format']}")
    who = meta.get("commander") or ", ".join(commanders)
    if who:
        lines.append(f"Commander: {who}")
    return "\n".join(lines)


def convert_one(
    source: Path,
    *,
    out: Path | None,
    name: str | None,
) -> Path:
    source = resolve_input(source)
    folder = source.parent
    meta = session_meta(folder)
    main, side, commanders, file_printings, file_name = load_deck(source)
    if not main and not side:
        raise ValueError(f"empty deck: {source}")
    registry = merge_printings(load_printings(), file_printings)
    if file_printings:
        save_printings(registry)
    dest = out or (folder / OFFICIAL_NAME)
    dest_meta = session_meta(dest.parent) if dest.parent != folder else {}
    meta = {**meta, **{k: v for k, v in dest_meta.items() if v}}
    deckname = name or file_name or meta.get("name") or folder.name
    write_cod(
        dest,
        deckname=deckname,
        comments=_comments(meta, source, commanders),
        main=main,
        side=side,
        commanders=commanders,
        printings=registry,
    )
    return dest


def iter_sessions(decks_root: Path) -> list[Path]:
    found: list[Path] = []
    if not decks_root.is_dir():
        return found
    for folder in sorted(decks_root.iterdir()):
        if not folder.is_dir():
            continue
        try:
            found.append(resolve_input(folder))
        except FileNotFoundError:
            continue
    return found


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="to_cockatrice.py",
        description="Write Cockatrice .cod files (official deck artifacts).",
    )
    parser.add_argument(
        "path",
        nargs="?",
        type=Path,
        help="list.txt, deck.cod, or a session folder",
    )
    parser.add_argument(
        "--all",
        action="store_true",
        help="convert every session under decks/",
    )
    parser.add_argument("--name", default=None, help="Cockatrice deck title")
    parser.add_argument(
        "--out",
        type=Path,
        default=None,
        help=f"output path (default: <session>/{OFFICIAL_NAME})",
    )
    parser.add_argument(
        "--decks-root",
        type=Path,
        default=Path("decks"),
        help="root for --all (default: decks/)",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.all == bool(args.path):
        parser.error("pass a PATH or --all")
    try:
        if args.all:
            sessions = iter_sessions(args.decks_root)
            if not sessions:
                print("no decks found", file=sys.stderr)
                return 1
            for source in sessions:
                dest = convert_one(source, out=None, name=args.name)
                print(f"{source} -> {dest}")
            return 0
        dest = convert_one(args.path, out=args.out, name=args.name)
        print(dest)
        return 0
    except (OSError, ValueError, FileNotFoundError) as exc:
        print(exc, file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
