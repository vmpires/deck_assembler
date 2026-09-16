---
name: build-mtg-deck
description: >-
  Builds Magic: The Gathering decks in this harness using the user's taste profile
  and a gated procedure (commander shortlist, then mechanics, then a validated
  list). Use when the user pitches a deck idea, asks for commanders, mechanics,
  EDH/Commander or Pauper lists, or works under decks/, preferences/, or templates/.
---

# Build an MTG deck

Read [preferences/profile.md](../../../preferences/profile.md) and [preferences/formats.md](../../../preferences/formats.md). Follow [procedure/workflow.md](../../../procedure/workflow.md).

## Gates

1. Pitch → Scryfall search → write `01-commanders.md` → **stop**.
2. User picks → write `02-mechanics.md` → **stop**.
3. User picks → write `list.txt` + `03-deck.md` → `validate` → `to_cockatrice.py` → `deck.cod` (official).

Skip a gate only if the user already named that choice. Never dump a 99-card list in the same turn as the first shortlist.

Session path: `decks/YYYY-MM-DD-<slug>/`. Copy structure from [templates/](../../../templates/).

## Scryfall (required)

Confirm cards with the repo script, not memory:

```bash
python scripts/scryfall.py search "QUERY" --max 8
python scripts/scryfall.py card "Exact Name"
python scripts/scryfall.py validate decks/<session>/list.txt --format commander --commander "Name"
python scripts/scryfall.py validate decks/<session>/list.txt --format pauper
python scripts/to_cockatrice.py decks/<session>/
python scripts/scryfall.py validate decks/<session>/deck.cod --format commander --commander "Name"
```

Write real Scryfall syntax:

- Commanders: `is:commander o:token id:gw`
- Oracle: `o:"create a token"`
- Pauper: `f:pauper t:instant c:u cmc<=2`
- Banned check: `banned:commander`, `banned:pauper`

EDHREC/web is a staples *hint* only after Scryfall says the card exists and is legal. It must not override synergy-first.

## Ranking

Against the profile: synergy with the pitch, combat/tokens/tribal/spellslinger/control/lands/value/combo as fits, no stax/chaos, graveyard/politics only if the pitch is about them.

Default EDH Bracket 3 (≤3 Game Changers, no MLD, no extra-turn chains). Bracket 4 only on request. Never cEDH.

## Shortlist shape

Each commander or Pauper shell: why it fits, color identity (or colors), likely plans, bracket/role, one risk. 5–8 options.

Each mechanic: win condition, normal turn, support categories, 3–6 exemplar cards (validated), bracket/role.

## Final list

- Commander: 100 cards including commander; singleton; color identity.
- Pauper: 60 + up to 15; ≤4 copies; all `f:pauper`.
- Working copy: `list.txt`. **Official artifact: `deck.cod`** (Cockatrice XML) via `python scripts/to_cockatrice.py decks/<session>/`.
- Preferred printings: [preferences/printings.json](../../../preferences/printings.json). Importing a `.cod` with `setShortName` / `collectorNumber` / `uuid` updates that registry; later exports must keep those prints.
- Call out Game Changers and expensive cards.
- Paste validate output into `03-deck.md`. A deck is not done until `deck.cod` exists and validate is clean.
