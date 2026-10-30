# Deck Assembler

A Cursor agent harness for building Magic: The Gathering decks. There is no app. Open this folder and talk to the agent. It looks the cards up, stops at each choice, and writes a Cockatrice deck.

## How a deck gets built

1. Pitch the idea. Name the format when you know it: Commander or Pauper. If the format is missing, the agent asks before it searches.
2. A Commander pitch gets 5–8 commanders. A Pauper pitch gets 5–8 archetype shells. There is no Pauper commander. The agent writes the shortlist and stops.
3. You pick. It writes 2–4 game plans and stops.
4. You pick. It writes the full list, checks it, and writes `deck.cod`.

Ask for a different shortlist size when you want one. "About 10 commanders" is a normal request.

Name the choice and that step is skipped. "Ghyrson Starn, spellslinger" starts at the list. "Use all three plans in one deck" is a mechanic pick.

## What you can ask

### Start something

- A new Commander or Pauper deck from a pitch. "I want a token deck" or "Pauper control that grinds."
- Commanders or shells around a theme, with no full list yet. "About 10 commanders with different mechanics."
- Mechanics for a commander you already named. "Let's think of a deck with Ghyrson Starn."
- The full list once the commander and the plan are chosen.

### Shape the plan

- One of the plans it offered.
- Several plans built as a single deck. "All three can be one deck."
- A lean toward something the plan needs. "Plan 1, with defensive spells so I live first."
- Full Bracket 4 when you want the deck tuned or high. The default stays high Bracket 3 / low Bracket 4.
- Stax, prison, mass land destruction, extra-turn chains, or chaos, only when you ask for them.

### Change a finished deck

Point at the session and say what should be different. The agent rewrites the list, checks it again, and updates `deck.cod`.

- Swap a card. "Change Force of Will for something else."
- Cut or add Game Changers.
- Shift the defense, the mana, the interaction, or the win.

### Ask about cards

- Whether a card is legal in the deck you are building.
- What a card actually does, before it goes in the list.
- Cards that do a job the plan needs. "Draw when an enchantment deals combat damage."

The agent confirms the card exists and is legal before it recommends it. A card around $20 or more is called out. Game Changers are counted. The default deck keeps at most three unless you asked for Bracket 4.

### Files beyond the list

A normal deck is the notes, `list.txt`, and `deck.cod`. Ask when you want more.

- Card images for a session. One picture per card, using the printing already saved for that card.
- A print sheet (`.docx`). It stays at or under 100 MB. The card size and the page layout stay as they are.
- A session from a Cockatrice file you already have. Say you want a deck structure and point at the `.cod`. That imports the list, the notes, the images, and the printings. It is separate from pitching a new idea.
- Art you picked in Cockatrice. Hand over that `.cod` and ask the agent to remember the printings. Later decks reuse that set, collector number, and art.

## What you get back

Each deck lives in `decks/YYYY-MM-DD-<slug>/`.

| File | Role |
| --- | --- |
| `00-intake.md` | Idea, format, bracket, refusals |
| `01-commanders.md` | Shortlist, or the commander you already named |
| `02-mechanics.md` | Game plans |
| `03-deck.md` | The built list, Game Changers, expensive cards, the check |
| `list.txt` | Working copy, also a Moxfield / Archidekt paste |
| `deck.cod` | The file you open in Cockatrice |
| `decks/_index.md` | Every session and its status |

Commander lists are 100 cards, singleton, inside the commander's color identity. Pauper lists are 60 cards plus up to 15 in the sideboard, at most 4 copies, and every card is Pauper-legal. Partners are named as `A / B`.

## Taste

The agent treats [preferences/profile.md](preferences/profile.md) as fact and [preferences/formats.md](preferences/formats.md) as the format rules. Tell it to change those when the defaults should change.

Defaults: Commander at high Bracket 3 / low Bracket 4, or 60-card Pauper. Synergy first, then staples that serve the plan. There is no collection inventory and no hard budget.

Welcome: combat, tokens, tribal, spellslinger, control, lands and big mana, value engines, and combo that supports the plan.

Out unless you ask: stax, prison, mass land destruction, extra-turn chains, chaos, and cEDH. Graveyard strategies and politics only when the pitch is about them.

## Branches

Local `master` is the library. It holds every session. It has no upstream.

GitHub `master` is the `publish` branch. That tip keeps the harness and one example, [decks/2026-09-30-goro-goro/](decks/2026-09-30-goro-goro/). Personal sessions stay on local `master`.

Commit deck sessions on local `master`. Push harness updates from `publish`. Merging GitHub `master` into local `master` removes session folders that the public commit deleted, so the two branches stay diverged.
