# Build procedure

Gates are mandatory. After stages 1 and 2, stop and wait. Skip a stage only when the user already decided it (named the commander, named the mechanic).

Create a session folder first: `decks/YYYY-MM-DD-<slug>/`.

## Stage 0 — Intake

Capture: idea, format (`commander` or `pauper`), bracket/power if given, colors if given, anything they refuse.

If format is missing, ask. Do not assume.

## Stage 1 — Commanders (or Pauper shells)

Translate the pitch into Scryfall queries. Run `python scripts/scryfall.py search ...`.

Commander: 5–8 commanders ranked against [preferences/profile.md](../preferences/profile.md).

Pauper: there is no commander. Propose 5–8 **archetype shells** (e.g. Affinity, Faeries, Tron-adjacent, control) that match the pitch, each with a few legal exemplar cards from Scryfall.

Write `01-commanders.md` from [templates/01-commanders.md](../templates/01-commanders.md). Then **stop**.

## Stage 2 — Mechanics

After the user picks, propose **2–4 distinct game plans**.

Each plan: how it wins, a normal turn, support categories, a few Scryfall-confirmed exemplars, estimated bracket (EDH) or Pauper role (aggro / midrange / control / combo).

Write `02-mechanics.md` from [templates/02-mechanics.md](../templates/02-mechanics.md). Then **stop**.

## Stage 3 — List

Build the full list. Engine cards first, then staples that serve the plan, then lands / interaction.

Write `list.txt` (working copy for validate / Moxfield paste) and `03-deck.md` from [templates/03-deck.md](../templates/03-deck.md).

Validate, then write the official Cockatrice artifact:

```bash
python scripts/scryfall.py validate decks/<session>/list.txt --format commander --commander "Name"
python scripts/scryfall.py validate decks/<session>/list.txt --format pauper
python scripts/to_cockatrice.py decks/<session>/
python scripts/scryfall.py validate decks/<session>/deck.cod --format commander --commander "Name"
```

`to_cockatrice.py` applies [preferences/printings.json](../preferences/printings.json). Importing a Cockatrice `.cod` that already has print attributes **learns** those prints for later decks.

Fix every error. Flag Game Changers and expensive cards. **`deck.cod` is the official artifact** — do not call the deck done without it. Append `decks/_index.md`.
