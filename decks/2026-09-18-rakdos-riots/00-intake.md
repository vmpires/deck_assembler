# Stage 0 — Intake

- **Idea:** Upgrade the existing **Rakdos, Lord of Riots** Cockatrice list. Goal: **quicker and more fatal** — same commander. Not a blank commander search.
- **Format:** commander
- **Bracket / power target:** Current list is already **Bracket 4** (six Game Changers). Pitch is **more competitive**, so stay at **Bracket 4 (Optimized)** — faster goldfish, more GCs allowed. Never cEDH / Bracket 5. No stax, prison, Blood Moon, or chaos.
- **Colors / identity:** Rakdos (**B/R**) — **Rakdos, Lord of Riots**
- **Refusal / keep:** No cEDH packages, no MLD, no extra-turn chains. Keep the commander’s identity: opponents lose life → dump huge creatures.

## Source

- Import: `/home/fetchly/.var/app/io.github.Cockatrice.cockatrice/data/Cockatrice/Cockatrice/decks/Rakdos, Lord of Riots.cod`
- Session copies: `baseline-from-import.cod`, `baseline-from-import.txt`
- Validate: `format=commander cards=100 identity=BR` **OK**

## Current read (from list)

| Axis | What the deck is doing today |
| --- | --- |
| **Commander engine** | Opponent must lose life this turn to cast Rakdos; then creature spells cost `{1}` less per life lost. Flying/trample 6/6 body. |
| **Enable (life loss)** | Mix of **slow tap pingers** (Spear Spewer, Thermo-Alchemist, Lobber Crew, Nettle Drone, Unruly Catapult, Creeping Bloodsucker) and **fast burn** (Lightning Bolt, Flame Rift, Boltwave, Vexing Devil, Grab the Prize). |
| **Dump targets** | Strong: **Blightsteel Colossus**, **Ulamog**, **Kozilek**, **Void Winnower**, **Sire of Seven Deaths**, **It That Betrays**. Weak/slow: **Desolation Twin**, **Dread Cacodemon**, **Artisan of Kozilek**, **Pathrazer of Ulamog**, **Conduit of Ruin**. |
| **Finishers besides combat** | **Purphoros**, **Terror of the Peaks**, **Impact Tremors**, **Chandra's Ignition**, **Bloodletter of Aclazotz**, **Torment of Hailfire**. |
| **Haste / protection** | Only **Lightning Greaves**, **Swiftfoot Boots**, **Arena of Glory**, **Malakir Rebirth**. Dumped fatties often sit a turn. |
| **Mana** | Fast artifacts/rituals are good (**Sol Ring**, **Chrome Mox**, **Lotus Petal**, **Dark Ritual**, **Seething Song**, **Jeska's Will**). Lands include slow ping slots (**Shivan Gorge**, **Leechridden Swamp**, **Sunscorched Desert**) and taplands (**Jagged Barrens**, **Bojuka Bog**). |
| **Game Changers (6)** | **Chrome Mox**, **Demonic Tutor**, **Vampiric Tutor**, **Gamble**, **Jeska's Will**, **Orcish Bowmasters**. |

## Friction vs “quicker / more fatal”

1. **Enablers occupy the board and don’t kill.** Tap-to-ping creatures cost a turn and 1 damage. One-mana burn or upkeep Vortex effects enable Rakdos without clogging the dump turn.
2. **No haste density.** Blightsteel without haste is a “please remove this” sticker, not a kill.
3. **No cheat outlet if Rakdos is unavailable.** The 8–15 drops are dead cards when you can’t ping.
4. **Casual Eldrazi** and **slow enchantments** (**Bontu's Monument**, **Theater of Horrors**, **Sarkhan's Unsealing**, **Sanctum of Stone Fangs**) do not close Bracket 4 games.

## Gate status

| Stage | Status |
| --- | --- |
| Commanders | **Skipped** — commander locked: **Rakdos, Lord of Riots** |
| Mechanics | **Plan A** — Instant Enable, Haste Dump |
| Full list | **Done** — `list.txt`, `03-deck.md`, `deck.cod` |
