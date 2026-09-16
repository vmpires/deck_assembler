# Stage 3 — Deck

- **Name:**
- **Format:** commander | pauper
- **Commander / shell:**
- **Mechanic:**
- **Bracket (EDH) or role (Pauper):**
- **Game Changers (EDH):** none | list them
- **Expensive cards to flag:**

## Game plan

One short paragraph: what the deck does, how it wins, what a normal game looks like.

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

## Import

- **Official:** `deck.cod` in the session folder (Cockatrice). Write it with `python scripts/to_cockatrice.py decks/<session>/`.
- Working copy: `list.txt` (Moxfield / Archidekt / validate). Commander: 100 × `1 Card Name` (commander first). Pauper: 60 main, then `Sideboard`, then up to 15.

```
1 Card Name
```

## Validate

Paste `python scripts/scryfall.py validate ...` output here. Then confirm `deck.cod` exists. All errors must be fixed before calling the deck done.
