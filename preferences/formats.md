# Format rules

Never memorize ban lists. Use Scryfall (`legalities` on a card, or `banned:commander` / `banned:pauper` in search).

## Commander (EDH)

- 100 cards total, including the commander.
- Singleton except basic lands and cards that explicitly allow copies.
- Every card's color identity must be a subset of the commander's.
- Commander must be a legal commander (`is:commander` on Scryfall, usually legendary creature or equivalent).
- Bracket is social, not legality. Game Changers are listed by Wizards; look up the current list rather than trusting memory. Call out any Game Changer in the list.
- Official overview: https://magic.wizards.com/en/formats/commander

Default target: high Bracket 3 / low Bracket 4 (competitive). Full Bracket 4 on request. Bracket 5 out of scope.

## Pauper (60-card)

- 60-card main deck, up to 15-card sideboard.
- Maximum 4 copies of a card, except basic lands.
- Every card must be Pauper-legal (Scryfall `legalities.pauper == legal`). That means a common printing and not banned.
- Not PDH. Uncommon commanders and 99-card pauper lists are out of scope unless the user explicitly asks later.

## Import blocks

- **Official artifact:** Cockatrice `deck.cod` in the session folder (`python3 scripts/to_cockatrice.py`).
- Working copy: `list.txt` — Commander Moxfield / Archidekt style (`1 Card Name` per line, commander called out). Pauper: maindeck then `Sideboard` then 15 cards.
