# Deck Assembler

A Cursor agent harness for building Magic: The Gathering decks. There is no app, no server, and no UI. Open this folder, pitch an idea, and pick from the shortlists.

## How to use it

1. Open this repository in Cursor.
2. Pitch an idea **and a format**, for example:
   - `Golgari tokens, commander, bracket 3`
   - `pauper spellslinger`
   - `I already want Aesi as commander — lands-matter value`
3. The agent searches Scryfall, writes a commander (or Pauper shell) shortlist, and **stops**.
4. You pick. Then it proposes 2–4 mechanics and **stops**.
5. You pick. Then it builds a validated list and writes **`deck.cod`** (Cockatrice), the official artifact.

Sessions are saved as folders:

`decks/2026-09-15-golgari-tokens/`

Open `deck.cod` in Cockatrice. `list.txt` is the working copy.

## Taste

The agent reads [preferences/profile.md](preferences/profile.md). Edit that file when your tastes change.

Defaults today: competitive Commander (high Bracket 3 / low Bracket 4; full Bracket 4 on request), 60-card Pauper, synergy-first with proven staples, no stax/chaos, no cEDH.

## Scryfall helper

```bash
python3 scripts/scryfall.py search "is:commander o:token" --max 8
python3 scripts/scryfall.py card "Rhys the Redeemed"
python3 scripts/scryfall.py validate decks/example/list.txt --format commander --commander "Rhys the Redeemed"
python3 scripts/to_cockatrice.py decks/example/
python3 scripts/to_cockatrice.py --all
```

`deck.cod` is Cockatrice XML and the official deck file. Printings you pick in Cockatrice are stored in [preferences/printings.json](preferences/printings.json) and reused. Stdlib only. Scryfall calls need network access to `api.scryfall.com`.

## Generate a deck structure

Ask for this by name, and point at a Cockatrice file. It is separate from pitching a new deck.

```bash
python3 scripts/create_from_cod.py path/to/deck.cod
```

That creates `decks/<date>-<slug>/` with the session notes, `list.txt`, official `deck.cod`, and a `printings/` folder. Printings already saved for another deck are copied instead of downloaded again.
