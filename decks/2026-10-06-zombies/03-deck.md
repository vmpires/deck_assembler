# Stage 3 — Deck

- **Name:** Rotcleaver Horde
- **Format:** commander
- **Commander / shell:** Wilhelt, the Rotcleaver
- **Mechanic:** Plans A and C. Lords and a combat clock, plus token makers that build a horde. A drain package is the second win. Ramp and interaction are both heavy.
- **Bracket (EDH) or role (Pauper):** High Bracket 3 (3 Game Changers, the cap)
- **Game Changers (EDH):** Demonic Tutor, Fierce Guardianship, Cyclonic Rift
- **Expensive cards to flag:** Demonic Tutor (~$69), Fierce Guardianship (~$64), Urborg, Tomb of Yawgmoth (~$55), Cyclonic Rift (~$39), Cabal Coffers (~$29), Morphic Pool (~$27), The Meathook Massacre (~$25), Cover of Darkness (~$22), Damnation (~$21), Polluted Delta (~$21). Crypt Ghast and Undead Warchief sit just under $20.

## Game plan

Cast Wilhelt, then Zombies. Lords (Death Baron, Lord of the Accursed, Diregraf Captain, Undead Warchief, Liliana's Mastery, Graf Harvest, Cover of Darkness) turn the board into a combat clock: deathtouch, menace, flying from Hordewing Skaab, and fear from Cover of Darkness. Diregraf Colossus, Cryptbreaker, Endless Ranks of the Dead, Necroduality, Liliana's Mastery, Cemetery Reaper, and Army of the Damned make Zombies that do not have decayed, so they can attack and block. When a nontoken Zombie dies, Wilhelt replaces it with a decayed token and can draw by sacrificing a Zombie at the end step.

The second win is life loss. The Meathook Massacre drains each opponent whenever a creature you control dies, and its enter ability is a scalable wipe. Diregraf Captain and Plague Belcher drain when a Zombie dies. Gray Merchant of Asphodel drains for black devotion. Crypt Ghast's extort and Geralf's Messenger add smaller drains. A stalled combat still kills the table if Zombies are dying.

Ramp is rocks, Dark Ritual, Wayfarer's Bauble, Solemn Simulacrum, Herald's Horn, Urza's Incubator (choose Zombie), Undead Warchief, Crypt Ghast, and Cabal Coffers with Urborg, Tomb of Yawgmoth. Defense is five counters, single-target removal, Fleshbag Marauder, and four sweepers: Toxic Deluge, Damnation, Cyclonic Rift, and The Meathook Massacre. Lightning Greaves and Swiftfoot Boots keep Wilhelt in play. Death Baron gives deathtouch to Zombies that are allowed to block. Creeping Tar Pit and Restless Reef block as lands. Wilhelt's own tokens have decayed, so they cannot block. The horde tokens can.

Rooftop Storm, Phyrexian Altar, and Pitiless Plunderer are out. With Gravecrawler and a sacrifice outlet those three go infinite. Gravecrawler stays as a one-mana Zombie that comes back while you control a Zombie.

## Categories

Counts match `list.txt` / `deck.cod` (100 cards, 36 lands).

- **Commander:** Wilhelt, the Rotcleaver (1)
- **Ramp / mana:** Sol Ring, Arcane Signet, Dimir Signet, Talisman of Dominance, Fellwar Stone, Mind Stone, Thought Vessel, Dimir Keyrune, Herald's Horn, Urza's Incubator, Wayfarer's Bauble, Solemn Simulacrum, Crypt Ghast, Dark Ritual (14)
- **Card advantage:** Demonic Tutor, Phyrexian Arena, Night's Whisper, Sign in Blood, Kindred Discovery, Undead Augur, Deadly Dispute (7). Cryptbreaker, Hordewing Skaab, and Baleful Strix also draw. Thought Vessel removes the maximum hand size so Kindred Discovery does not discard the extra cards.
- **Interaction:** Counterspell, Fierce Guardianship, Negate, An Offer You Can't Refuse, Drown in the Loch, Go for the Throat, Feed the Swarm, Bitter Triumph, Toxic Deluge, Damnation, Cyclonic Rift, Sheoldred's Edict, Fleshbag Marauder, Lightning Greaves, Swiftfoot Boots, Baleful Strix (16)
- **Engine / synergy:** Death Baron, Lord of the Accursed, Diregraf Captain, Hordewing Skaab, Lost Monarch of Ifnir, Undead Warchief, Cemetery Reaper, Cover of Darkness, Graf Harvest, Diregraf Colossus, Cryptbreaker, Endless Ranks of the Dead, Necroduality, Champion of the Perished, Jadar, Ghoulcaller of Nephalia, Ghoulcaller Gisa, Army of the Damned, Headless Rider, Grave Titan, Liliana's Mastery, Gravecrawler, Relentless Dead, Geralf's Messenger (23)
- **Win conditions:** combat with the lords and the horde. Life drain from The Meathook Massacre, Plague Belcher, and Gray Merchant of Asphodel (3). Diregraf Captain also drains and is already counted as a lord.
- **Lands:** 36 (7 Island, 9 Swamp, Cabal Coffers, Urborg, Tomb of Yawgmoth, fetch and duals including Watery Grave, Undercity Sewers, Polluted Delta, Creeping Tar Pit, Restless Reef)
- **Sideboard (Pauper):** n/a

## Official artifact

[`deck.cod`](deck.cod) — Cockatrice XML from `python3 scripts/to_cockatrice.py decks/2026-10-06-zombies/`.

## Validate

```
format=commander cards=100 identity=UB commander=Wilhelt, the Rotcleaver
WARN  expensive: Fierce Guardianship ($63.92); Damnation ($20.92); Cyclonic Rift ($39.16); Demonic Tutor ($69.13); Cover of Darkness ($21.67); The Meathook Massacre ($24.70); Morphic Pool ($27.17); Polluted Delta ($20.72); Cabal Coffers ($29.21); Urborg, Tomb of Yawgmoth ($55.42)
OK
```

`deck.cod` validate: same **OK** output.
