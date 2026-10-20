# Stage 3 — Deck

- **Name:** Menace Raiders
- **Format:** commander
- **Commander / shell:** Captain N'ghathrod
- **Mechanic:** Plan A — Menace Raiders (combat horrors, mill on combat damage)
- **Bracket (EDH) or role (Pauper):** Bracket 3 (upper end; two Game Changers only)
- **Game Changers (EDH):** Demonic Tutor, Sol Ring
- **Expensive cards to flag:** Demonic Tutor (~$67), Bruvac the Grandiloquent (~$46), Morphic Pool (~$30), Damnation (~$21), Cover of Darkness (~$23), Urza's Incubator (~$20), Undercity Sewers (~$15), Umbris, Fear Manifest (~$13), Aboleth Spawn (~$7), Ancient Cellarspawn (~$6)

## Game plan

Curve **Horror** creatures with **menace** (from the commander), connect for **combat damage**, and **mill** opponents for that much. **Bruvac the Grandiloquent** doubles every mill trigger, so a single attacker can end games quickly. At end step, **N'ghathrod** steals the best artifact or creature an opponent milled from their library **this turn** — your board becomes their best threats.

**Phyrexian Arena** and **Kindred Discovery** keep cards flowing; **Herald's Horn** and **Urza's Incubator** (choose Horror) reduce costs. **Maddening Cacophony** and **Court of Cunning** are backup mill, not the main engine. Win by milling opponents out, stealing a finisher, or **Toxic Deluge** / **Damnation** then rebuilding with stolen bodies.

Victor’s defaults: **no third Game Changer** (no Mystic Remora), **cut Jace, Wielder of Mysteries**, flavor **Illithid** pieces cut unless they fight (kept **Grazilaxx** as a Horror that rewards combat damage).

## Categories

Counts match `list.txt` / `deck.cod` (100 cards, 37 lands).

- **Commander:** Captain N'ghathrod (1)
- **Ramp / mana:** Sol Ring, Arcane Signet, Dimir Signet, Talisman of Dominance, Fellwar Stone, Thought Vessel, Mind Stone, Dimir Keyrune (8)
- **Card advantage:** Preordain, Night's Whisper, Deadly Dispute, Phyrexian Arena, Kindred Discovery, Herald's Horn, Grazilaxx, Illithid Scholar, Chasm Skulker, Court of Cunning (10)
- **Interaction:** Counterspell, Negate, An Offer You Can't Refuse, Drown in the Loch, Bitter Triumph, Feed the Swarm, Go for the Throat, Cast Down, Sheoldred's Edict, Toxic Deluge, Damnation, Overcharged Amalgam, Extract from Darkness (13)
- **Engine / synergy:** 27 Horror (and Horror-token) bodies including Ancient Cellarspawn, Umbris, Zellix, Nemesis of Reason, Silent Hallcreeper, Bruvac; Cover of Darkness; Greaves / Boots / Spellskite; Urza's Incubator; Maddening Cacophony; Demonic Tutor (30)
- **Win conditions:** combat mill + N'ghathrod theft, Bruvac multipliers, backup mass mill (11)
- **Lands:** 37 (8 Island, 8 Swamp, duals including Watery Grave, Undercity Sewers, Polluted Delta, Restless Reef, etc.)
- **Sideboard (Pauper):** n/a

## Official artifact

[`deck.cod`](deck.cod) — Cockatrice XML from `python3 scripts/to_cockatrice.py decks/2026-09-17-nghathrod-horror/`.

## Validate

```
format=commander cards=100 identity=UB commander=Captain N'ghathrod
WARN  expensive: Bruvac the Grandiloquent ($46.23); Cover of Darkness ($22.71); Damnation ($20.82); Demonic Tutor ($67.33); Morphic Pool ($29.73)
OK
```

`deck.cod` validate: same **OK** output.
