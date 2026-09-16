"""Deck list parsing and Cockatrice .cod (official artifact) I/O. Stdlib only."""

from __future__ import annotations

from io import BytesIO
import json
import re
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

SECTION_RE = re.compile(
    r"^(commander|commanders|deck|main|mainboard|maindeck|main deck|"
    r"sideboard|maybeboard|wishlist|companion)\s*:?\s*$",
    re.I,
)

NAME_LINE_RE = re.compile(r"^\s*-\s*\*\*Name:\*\*\s*(.+?)\s*$")
FORMAT_LINE_RE = re.compile(r"^\s*-\s*\*\*Format:\*\*\s*(.+?)\s*$")
COMMANDER_LINE_RE = re.compile(
    r"^\s*-\s*\*\*Commander / shell:\*\*\s*(.+?)\s*$"
)

REPO_ROOT = Path(__file__).resolve().parent.parent
PRINTINGS_PATH = REPO_ROOT / "preferences" / "printings.json"
PRINT_ATTRS = ("setShortName", "collectorNumber", "uuid")


def clean_name(name: str) -> str:
    name = re.sub(r"\s*\*[A-Z][A-Z0-9]*\*\s*$", "", name)
    name = re.sub(r"\s*\([A-Za-z0-9:_]+\)(?:\s+\d+\S*)?\s*$", "", name)
    name = re.sub(r"\s*\[\d+\]\s*$", "", name)
    return name.strip()


def parse_decklist(text: str) -> tuple[Counter[str], Counter[str], list[str]]:
    main: Counter[str] = Counter()
    side: Counter[str] = Counter()
    commanders: list[str] = []
    section = "main"
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#") or line.startswith("//"):
            continue
        section_match = SECTION_RE.match(line)
        if section_match:
            label = section_match.group(1).lower()
            if label in {"sideboard"}:
                section = "side"
            elif label in {"maybeboard", "wishlist"}:
                section = "maybe"
            elif label in {"commander", "commanders"}:
                section = "commander"
            else:
                section = "main"
            continue
        sb_prefix = line.upper().startswith("SB:")
        if sb_prefix:
            line = line[3:].strip()
        match = re.match(r"^(?:(\d+)\s*x?\s+)(.+)$", line, re.I)
        if match:
            count = int(match.group(1))
            name = clean_name(match.group(2))
        else:
            count = 1
            name = clean_name(line)
        if not name:
            continue
        if section == "maybe":
            continue
        if sb_prefix or section == "side":
            side[name] += count
            continue
        if section == "commander":
            commanders.extend([name] * count)
        main[name] += count
    return main, side, list(dict.fromkeys(commanders))


def _zone_kind(name: str | None) -> str:
    label = (name or "main").strip().lower()
    if label in {"side", "sideboard", "sb"}:
        return "side"
    if label in {"commander", "commanders"}:
        return "commander"
    if label in {"maybe", "maybeboard", "tokens"}:
        return "skip"
    return "main"


def parse_cod(
    text: str,
) -> tuple[Counter[str], Counter[str], list[str], dict[str, dict[str, str]], str]:
    root = ET.parse(BytesIO(text.encode("utf-8"))).getroot()
    tag = root.tag.rsplit("}", 1)[-1]
    if tag != "cockatrice_deck":
        raise ValueError(f"not a cockatrice_deck (got {root.tag})")
    main: Counter[str] = Counter()
    side: Counter[str] = Counter()
    commanders: list[str] = []
    printings: dict[str, dict[str, str]] = {}
    for zone in root.findall("zone"):
        kind = _zone_kind(zone.get("name"))
        if kind == "skip":
            continue
        for card in zone.findall("card"):
            name = (card.get("name") or "").strip()
            if not name:
                continue
            number = int(card.get("number") or "1")
            printing = {
                key: value
                for key in PRINT_ATTRS
                if (value := (card.get(key) or "").strip())
            }
            if printing:
                printings[name] = printing
            if kind == "side":
                side[name] += number
            elif kind == "commander":
                commanders.extend([name] * number)
                main[name] += number
            else:
                main[name] += number
    deckname = (root.findtext("deckname") or "").strip()
    return main, side, list(dict.fromkeys(commanders)), printings, deckname


def load_deck(
    path: Path,
) -> tuple[Counter[str], Counter[str], list[str], dict[str, dict[str, str]], str]:
    text = path.read_text(encoding="utf-8")
    stripped = text.lstrip()
    if path.suffix.lower() == ".cod" or stripped.startswith("<?xml") or stripped.startswith(
        "<cockatrice_deck"
    ):
        return parse_cod(text)
    main, side, commanders = parse_decklist(text)
    return main, side, commanders, {}, ""


def _ordered_main(main: Counter[str], commanders: list[str]) -> list[tuple[str, int]]:
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


def load_printings(path: Path | None = None) -> dict[str, dict[str, str]]:
    target = path or PRINTINGS_PATH
    if not target.is_file():
        return {}
    raw = json.loads(target.read_text(encoding="utf-8"))
    if not isinstance(raw, dict):
        raise ValueError(f"printings file must be an object: {target}")
    out: dict[str, dict[str, str]] = {}
    for name, spec in raw.items():
        if not isinstance(spec, dict):
            continue
        printing = {key: str(spec[key]) for key in PRINT_ATTRS if spec.get(key)}
        if printing:
            out[str(name)] = printing
    return out


def save_printings(printings: dict[str, dict[str, str]], path: Path | None = None) -> None:
    target = path or PRINTINGS_PATH
    target.parent.mkdir(parents=True, exist_ok=True)
    ordered = {
        name: {key: spec[key] for key in PRINT_ATTRS if key in spec}
        for name, spec in sorted(printings.items())
    }
    target.write_text(json.dumps(ordered, indent=2) + "\n", encoding="utf-8")


def merge_printings(
    base: dict[str, dict[str, str]],
    incoming: dict[str, dict[str, str]],
) -> dict[str, dict[str, str]]:
    merged = dict(base)
    merged.update(incoming)
    return merged


def _card_attrs(name: str, count: int, printings: dict[str, dict[str, str]]) -> dict[str, str]:
    attrs = {"number": str(count), "name": name}
    spec = printings.get(name) or {}
    for key in PRINT_ATTRS:
        if spec.get(key):
            attrs[key] = spec[key]
    return attrs


def write_cod(
    path: Path,
    *,
    deckname: str,
    comments: str,
    main: Counter[str],
    side: Counter[str],
    commanders: list[str] | None = None,
    printings: dict[str, dict[str, str]] | None = None,
) -> None:
    chosen = printings or {}
    root = ET.Element("cockatrice_deck", {"version": "1"})
    ET.SubElement(root, "deckname").text = deckname
    ET.SubElement(root, "comments").text = comments
    main_zone = ET.SubElement(root, "zone", {"name": "main"})
    for name, count in _ordered_main(main, commanders or []):
        ET.SubElement(main_zone, "card", _card_attrs(name, count, chosen))
    side_zone = ET.SubElement(root, "zone", {"name": "side"})
    for name, count in side.items():
        ET.SubElement(side_zone, "card", _card_attrs(name, count, chosen))
    tree = ET.ElementTree(root)
    ET.indent(tree, space="    ")
    path.parent.mkdir(parents=True, exist_ok=True)
    tree.write(path, encoding="utf-8", xml_declaration=True)


def session_meta(folder: Path) -> dict[str, str]:
    notes = folder / "03-deck.md"
    meta = {
        "name": folder.name,
        "format": "",
        "commander": "",
    }
    if not notes.is_file():
        return meta
    for line in notes.read_text(encoding="utf-8").splitlines():
        if m := NAME_LINE_RE.match(line):
            meta["name"] = m.group(1).strip()
        elif m := FORMAT_LINE_RE.match(line):
            meta["format"] = m.group(1).split("|")[0].strip()
        elif m := COMMANDER_LINE_RE.match(line):
            meta["commander"] = m.group(1).strip()
    return meta


def resolve_input(raw: Path) -> Path:
    if raw.is_dir():
        for name in ("list.txt", "deck.cod"):
            candidate = raw / name
            if candidate.is_file():
                return candidate
        raise FileNotFoundError(f"no deck.cod or list.txt in {raw}")
    return raw
