#!/usr/bin/env python3
"""Thin Scryfall CLI for the deck assembler harness. Stdlib only."""

from __future__ import annotations

import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
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

from deckio import load_deck

API = "https://api.scryfall.com"
USER_AGENT = "deck-assembler/0.1"
ACCEPT = "application/json"
MIN_INTERVAL = 0.5
COLLECTION_BATCH = 75
PRICE_WARN_USD = 20.0

UNLIMITED_RE = re.compile(r"A deck can have any number of cards named", re.I)


class ScryfallError(Exception):
    def __init__(self, message: str, status: int | None = None):
        super().__init__(message)
        self.status = status


class Scryfall:
    def __init__(self) -> None:
        self._last = 0.0

    def _wait(self) -> None:
        gap = MIN_INTERVAL - (time.monotonic() - self._last)
        if gap > 0:
            time.sleep(gap)

    def request(
        self,
        url: str,
        *,
        method: str = "GET",
        body: dict[str, Any] | None = None,
        retry_on_429: bool = True,
    ) -> dict[str, Any]:
        self._wait()
        data = None if body is None else json.dumps(body).encode("utf-8")
        req = urllib.request.Request(url, data=data, method=method)
        req.add_header("User-Agent", USER_AGENT)
        req.add_header("Accept", ACCEPT)
        if data is not None:
            req.add_header("Content-Type", "application/json")
        try:
            with urllib.request.urlopen(req) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            self._last = time.monotonic()
            raw = exc.read().decode("utf-8", errors="replace")
            details = _scryfall_error_text(raw, exc.code, exc.reason)
            if exc.code == 429 and retry_on_429:
                wait_s = _retry_after(exc, default=31.0)
                print(f"Scryfall 429; waiting {wait_s:.0f}s then retrying once", file=sys.stderr)
                time.sleep(wait_s)
                return self.request(url, method=method, body=body, retry_on_429=False)
            raise ScryfallError(details, status=exc.code) from exc
        except urllib.error.URLError as exc:
            self._last = time.monotonic()
            raise ScryfallError(f"network error: {exc.reason}") from exc
        self._last = time.monotonic()
        return payload

    def search(self, query: str, *, max_cards: int, order: str | None) -> list[dict[str, Any]]:
        params = {"q": query, "unique": "cards"}
        if order:
            params["order"] = order
        url = f"{API}/cards/search?{urllib.parse.urlencode(params)}"
        cards: list[dict[str, Any]] = []
        while url and len(cards) < max_cards:
            payload = self.request(url)
            if payload.get("object") == "error":
                raise ScryfallError(payload.get("details") or "search failed")
            cards.extend(payload.get("data") or [])
            url = payload.get("next_page") if payload.get("has_more") else None
        return cards[:max_cards]

    def named(self, name: str, *, fuzzy: bool = False) -> dict[str, Any]:
        key = "fuzzy" if fuzzy else "exact"
        url = f"{API}/cards/named?{urllib.parse.urlencode({key: name})}"
        return self.request(url)

    def by_set_number(self, code: str, number: str) -> dict[str, Any]:
        set_code = urllib.parse.quote(code.strip().lower())
        collector_number = urllib.parse.quote(number.strip())
        url = f"{API}/cards/{set_code}/{collector_number}"
        return self.request(url)

    def collection(self, names: list[str]) -> tuple[list[dict[str, Any]], list[str]]:
        found: list[dict[str, Any]] = []
        missing: list[str] = []
        unique = list(dict.fromkeys(names))
        for i in range(0, len(unique), COLLECTION_BATCH):
            batch = unique[i : i + COLLECTION_BATCH]
            payload = self.request(
                f"{API}/cards/collection",
                method="POST",
                body={"identifiers": [{"name": n} for n in batch]},
            )
            found.extend(payload.get("data") or [])
            for item in payload.get("not_found") or []:
                missing.append(item.get("name") or "")
        missing = [m for m in missing if m]
        # Collection identifiers accept either face of a split card, not the
        # combined "Left // Right" name Scryfall itself returns.
        split_missing = [name for name in missing if " // " in name]
        if split_missing:
            faces = [name.split(" // ", 1)[0] for name in split_missing]
            face_payload = self.request(
                f"{API}/cards/collection",
                method="POST",
                body={"identifiers": [{"name": face} for face in faces]},
            )
            found.extend(face_payload.get("data") or [])
            still_missing = {
                item.get("name") or ""
                for item in (face_payload.get("not_found") or [])
            }
            resolved = {
                name
                for name, face in zip(split_missing, faces)
                if face not in still_missing
            }
            missing = [name for name in missing if name not in resolved]
        return found, missing


def _scryfall_error_text(raw: str, code: int, reason: str) -> str:
    try:
        payload = json.loads(raw)
    except json.JSONDecodeError:
        return f"HTTP {code} {reason}: {raw.strip() or 'no body'}"
    details = payload.get("details") or payload.get("code") or raw
    return f"HTTP {code}: {details}"


def _retry_after(exc: urllib.error.HTTPError, default: float) -> float:
    raw = exc.headers.get("Retry-After") if exc.headers else None
    if not raw:
        return default
    try:
        return min(max(float(raw), 1.0), 35.0)
    except ValueError:
        return default


def oracle_text(card: dict[str, Any]) -> str:
    if card.get("oracle_text"):
        return str(card["oracle_text"])
    faces = card.get("card_faces") or []
    parts = [str(face.get("oracle_text") or "") for face in faces]
    return " // ".join(p for p in parts if p)


def type_line(card: dict[str, Any]) -> str:
    if card.get("type_line"):
        return str(card["type_line"])
    faces = card.get("card_faces") or []
    return " // ".join(str(face.get("type_line") or "") for face in faces)


def mana_cost(card: dict[str, Any]) -> str:
    if card.get("mana_cost"):
        return str(card["mana_cost"])
    faces = card.get("card_faces") or []
    return faces[0].get("mana_cost") or "" if faces else ""


def identity_str(card: dict[str, Any]) -> str:
    ident = card.get("color_identity") or []
    return "".join(ident) or "C"


def snippet(text: str, limit: int = 220) -> str:
    folded = " / ".join(line.strip() for line in text.splitlines() if line.strip())
    if len(folded) <= limit:
        return folded
    return folded[: limit - 1] + "…"


def format_card(card: dict[str, Any], *, full_oracle: bool = False) -> str:
    legal = card.get("legalities") or {}
    oracle = oracle_text(card)
    oracle_out = oracle if full_oracle else snippet(oracle)
    lines = [
        card.get("name") or "?",
        f"  type: {type_line(card)}",
        f"  mana: {mana_cost(card) or '—'}",
        f"  identity: {identity_str(card)}",
        f"  legal: commander={legal.get('commander', '?')} pauper={legal.get('pauper', '?')}",
    ]
    usd = (card.get("prices") or {}).get("usd")
    if usd:
        lines.append(f"  usd: {usd}")
    if oracle_out:
        lines.append(f"  oracle: {oracle_out}")
    return "\n".join(lines)


def norm_name(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", name.lower())


def card_lookup(cards: list[dict[str, Any]]) -> dict[str, dict[str, Any]]:
    lookup: dict[str, dict[str, Any]] = {}
    for card in cards:
        names = [card.get("name") or ""]
        for face in card.get("card_faces") or []:
            names.append(face.get("name") or "")
        for name in names:
            key = norm_name(name)
            if key:
                lookup[key] = card
    return lookup


def get_card(lookup: dict[str, dict[str, Any]], name: str) -> dict[str, Any] | None:
    return lookup.get(norm_name(name))


def parse_commander_flag(raw: str | None) -> list[str]:
    if not raw:
        return []
    # "and" is part of card names (Goro-Goro and Satoru). Partners use " / " or " & ".
    parts = re.split(r"\s*(?://|/|&)\s*", raw.strip(), maxsplit=1)
    return [p for p in (part.strip() for part in parts) if p]


def is_basic(card: dict[str, Any]) -> bool:
    return "Basic" in type_line(card)


def allows_unlimited(card: dict[str, Any]) -> bool:
    return bool(UNLIMITED_RE.search(oracle_text(card)))


def usd_price(card: dict[str, Any]) -> float | None:
    raw = (card.get("prices") or {}).get("usd")
    if raw is None:
        return None
    try:
        return float(raw)
    except (TypeError, ValueError):
        return None


def cmd_search(api: Scryfall, args: argparse.Namespace) -> int:
    try:
        cards = api.search(args.query, max_cards=args.max, order=args.order)
    except ScryfallError as exc:
        if exc.status == 404:
            print("No cards found.")
            return 1
        print(exc, file=sys.stderr)
        return 1
    if not cards:
        print("No cards found.")
        return 1
    print(f"{len(cards)} card(s) for: {args.query}")
    print()
    print("\n\n".join(format_card(c) for c in cards))
    return 0


def cmd_card(api: Scryfall, args: argparse.Namespace) -> int:
    try:
        card = api.named(args.name, fuzzy=False)
    except ScryfallError as exc:
        if exc.status != 404:
            print(exc, file=sys.stderr)
            return 1
        try:
            card = api.named(args.name, fuzzy=True)
        except ScryfallError as exc2:
            print(exc2, file=sys.stderr)
            return 1
        print(f"(fuzzy match for {args.name!r})", file=sys.stderr)
    print(format_card(card, full_oracle=True))
    return 0


def cmd_validate(api: Scryfall, args: argparse.Namespace) -> int:
    try:
        main, side, file_commanders, _printings, _deckname = load_deck(args.list_file)
    except OSError as exc:
        print(f"cannot read {args.list_file}: {exc}", file=sys.stderr)
        return 1
    except (ValueError, ET.ParseError) as exc:
        print(f"cannot parse {args.list_file}: {exc}", file=sys.stderr)
        return 1
    flag_commanders = parse_commander_flag(args.commander)
    errors: list[str] = []
    warnings: list[str] = []

    if args.format == "commander":
        commanders = flag_commanders or file_commanders
        if not commanders:
            errors.append("no commander: pass --commander NAME or a Commander section")
        if side:
            warnings.append(f"sideboard present ({sum(side.values())} cards); Commander lists are 100 cards, no sideboard")
        names = list(main)
        extra = [
            n
            for n in commanders
            if not any(norm_name(n) == norm_name(m) for m in main)
        ]
        if extra:
            errors.append("commander not in list: " + ", ".join(extra))
        names.extend(extra)
        try:
            cards, missing = api.collection(names) if names else ([], [])
        except ScryfallError as exc:
            print(exc, file=sys.stderr)
            return 1
        lookup = card_lookup(cards)
        _note_missing(missing, errors)
        total = sum(main.values())
        if total != 100:
            errors.append(f"size {total}, expected 100 including commander")
        commander_cards = [c for n in commanders if (c := get_card(lookup, n))]
        identity: set[str] = set()
        for card in commander_cards:
            identity.update(card.get("color_identity") or [])
        if commander_cards:
            ident_label = "".join(c for c in "WUBRG" if c in identity) or "C"
            for name, count in sorted(main.items()):
                card = get_card(lookup, name)
                if card is None:
                    continue
                if count > 1 and not is_basic(card) and not allows_unlimited(card):
                    errors.append(f"duplicate x{count}: {name}")
                card_id = set(card.get("color_identity") or [])
                if not card_id.issubset(identity):
                    extra_colors = "".join(c for c in "WUBRG" if c in (card_id - identity))
                    errors.append(f"identity {identity_str(card)} not in {ident_label}: {name} (+{extra_colors})")
                legal = (card.get("legalities") or {}).get("commander")
                if legal != "legal":
                    errors.append(f"commander-illegal ({legal}): {name}")
            _price_warnings(lookup, main, warnings)
            print(f"format=commander cards={total} identity={ident_label} commander={', '.join(commanders)}")
        else:
            print(f"format=commander cards={total}")
    else:
        if flag_commanders:
            warnings.append("--commander ignored for pauper")
        try:
            cards, missing = api.collection(list(main) + list(side)) if (main or side) else ([], [])
        except ScryfallError as exc:
            print(exc, file=sys.stderr)
            return 1
        lookup = card_lookup(cards)
        _note_missing(missing, errors)
        main_total = sum(main.values())
        side_total = sum(side.values())
        if main_total != 60:
            errors.append(f"main size {main_total}, expected 60")
        if side_total > 15:
            errors.append(f"sideboard size {side_total}, expected at most 15")
        combined = main + side
        for name, count in sorted(combined.items()):
            card = get_card(lookup, name)
            if card is None:
                continue
            if count > 4 and not is_basic(card) and not allows_unlimited(card):
                errors.append(f"over 4 copies ({count}): {name}")
            legal = (card.get("legalities") or {}).get("pauper")
            if legal != "legal":
                errors.append(f"pauper-illegal ({legal}): {name}")
        _price_warnings(lookup, combined, warnings)
        print(f"format=pauper main={main_total} side={side_total}")

    for warning in warnings:
        print(f"WARN  {warning}")
    if errors:
        for err in errors:
            print(f"ERROR {err}")
        print(f"FAIL ({len(errors)} error(s))")
        return 1
    print("OK")
    return 0


def _note_missing(missing: list[str], errors: list[str]) -> None:
    for name in missing:
        errors.append(f"missing name: {name}")


def _price_warnings(lookup: dict[str, dict[str, Any]], counts: Counter[str], warnings: list[str]) -> None:
    flagged: list[str] = []
    for name in counts:
        card = get_card(lookup, name)
        if card is None:
            continue
        price = usd_price(card)
        if price is not None and price >= PRICE_WARN_USD:
            flagged.append(f"{name} (${price:.2f})")
    if flagged:
        warnings.append("expensive: " + "; ".join(flagged))


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="scryfall.py",
        description="Search, show, and validate cards via Scryfall.",
    )
    sub = parser.add_subparsers(dest="cmd", required=True)

    search_p = sub.add_parser("search", help="fulltext search")
    search_p.add_argument("query", help='Scryfall query, e.g. is:commander o:token')
    search_p.add_argument("--max", type=int, default=15, help="max cards to print (default 15)")
    search_p.add_argument("--order", default=None, help="Scryfall order, e.g. edhrec or name")
    search_p.set_defaults(func=cmd_search)

    card_p = sub.add_parser("card", help="lookup one card by name")
    card_p.add_argument("name")
    card_p.set_defaults(func=cmd_card)

    val_p = sub.add_parser("validate", help="check a decklist file")
    val_p.add_argument("list_file", type=Path)
    val_p.add_argument("--format", choices=("commander", "pauper"), required=True)
    val_p.add_argument("--commander", default=None, help='Commander name, or "A / B" for partners')
    val_p.set_defaults(func=cmd_validate)
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    return args.func(Scryfall(), args)


if __name__ == "__main__":
    sys.exit(main())
