# Deck Assembler

This repository is a Magic: The Gathering deck-building harness for an agent, not an application and not a coding project. The user pitches an idea; you search, propose, and stop at each gate until they pick.

## Before you do anything

1. Read [preferences/profile.md](preferences/profile.md) and treat it as fact.
2. Read [preferences/formats.md](preferences/formats.md) for legality and bracket rules.
3. Follow [procedure/workflow.md](procedure/workflow.md) and the `build-mtg-deck` skill. Do not skip a gate unless the user already decided that stage.

## Non-negotiables

- Use `python3 scripts/scryfall.py` to search and to confirm a card exists and is legal **before** you recommend it. Do not invent cards, printings, or legalities from memory.
- Default formats: Commander EDH and 60-card Pauper. Not Pauper Commander. Not cEDH.
- Default EDH target is high Bracket 3 / low Bracket 4 (competitive). Offer full Bracket 4 when asked for tuned/high. Never propose Bracket 5 / cEDH packages.
- Synergy first, then staples that serve the plan. No stax/prison/chaos packages unless explicitly requested.
- Write session files under `decks/<date>-<slug>/` using the templates in `templates/`.
- After a full list, run `validate`, then `python3 scripts/to_cockatrice.py` so `deck.cod` exists. **`deck.cod` is the official artifact.**
- When the user asks to **create** or **design the structure** of a deck, that session includes `list.txt` and `deck.cod`. Skip `printings/` images unless they ask for images. This is not the import command below.
- Card printings live in [preferences/printings.json](preferences/printings.json). If the user picks art in Cockatrice, import that `.cod` so the registry learns `setShortName` / `collectorNumber` / `uuid` and later `.cod` files reuse those prints.
- When the user asks to **generate a deck structure** and points at a `.cod`, run `python3 scripts/create_from_cod.py path/to/deck.cod`. Do not do this during the normal gates.
- Print sheets (`.docx`) stay at or under 100 MB. Recompress the images enough to fit. Keep the card size and page layout.
