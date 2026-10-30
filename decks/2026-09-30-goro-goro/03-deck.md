# Stage 3 — Deck

- **Name:** Goro-Goro and Satoru
- **Format:** commander
- **Commander / shell:** Goro-Goro and Satoru
- **Mechanic:** Enter-and-attack: ninjutsu, sneak, and haste make a 5/5 Dragon Spirit each time a new creature connects
- **Bracket (EDH) or role (Pauper):** Bracket 3
- **Game Changers (EDH):** Notion Thief (1)
- **Expensive cards to flag:** Scalding Tarn ($35.58)

## Game plan

A creature that entered this turn has to connect. That makes one 5/5 flying Dragon Spirit. Ninjutsu and sneak enter already attacking. Haste creatures, `Rising of the Day`, and the combat-token engines (`Loyal Apprentice`, `Lagomos, Hand of Hatred`, `Daring Piracy`, `Urabrask's Forge`) do the same job. `Reinforced Ronin` bounces itself every end step, so it can enter and connect again next turn. `Raphael, the Nightwatcher` and `Great Train Heist` are how one turn makes more than one dragon. The dragons are the win.

This pass only fixes mana and two slots that were not joining that plan. `Flooded Strand` had no Plains to find. The {1}-to-activate filters and the tapped tri-land are gone. `Feed the Swarm` is the enchantment answer. `Artful Dodge` makes one creature unblockable, twice, which is the ninjutsu setup `Faerie Seer` was not providing.

## Categories

Counts match `list.txt` / `deck.cod` (100 cards).

- **Commander:** Goro-Goro and Satoru (1)
- **Ramp / mana:** Sol Ring, Arcane Signet, Fellwar Stone, Talisman of Creativity, Talisman of Dominance, Cursed Mirror (6)
- **Card advantage:** Bident of Thassa, Reconnaissance Mission, Phyrexian Arena, Chart a Course, Donatello's Technique (5)
- **Interaction:** Aetherize, An Offer You Can't Refuse, Arcane Denial, Bedevil, Chaos Warp, Counterspell, Crux of Fate, Perplexing Test, Reverse the Polarity, Feed the Swarm, Artful Dodge (11)
- **Engine / synergy:** 33 creatures in the 99 (ninjas, haste creatures, Satoru Umezawa, Satoru, the Infiltrator, Raphael, the token-makers); Rising of the Day, Daring Piracy, Urabrask's Forge, Neurok Stealthsuit, Swiftfoot Boots, Great Train Heist, Kaito, Dancing Shadow (40)
- **Win conditions:** Dragon Spirit tokens, Raphael's double strike, Great Train Heist, Crux of Fate once the dragons are the board you want to keep
- **Lands:** 37 mana sources — 35 lands plus Hydroelectric Specimen and Sundering Eruption
- **Sideboard (Pauper):** n/a

1+6+5+11+40+37 = 100.

## This pass

| Cut | Add |
| --- | --- |
| Flooded Strand | Blood Crypt |
| Darkwater Catacombs | Darkslick Shores |
| Ferrous Lake | Clearwater Pathway |
| Shadowblood Ridge | Blackcleave Cliffs |
| Crumbling Necropolis | Blightstep Pathway |
| Coastal Piracy | Feed the Swarm |
| Faerie Seer | Artful Dodge |

Still in the list from the review: Bident of Thassa, Perplexing Test, Alora, Merry Thief, Harried Dronesmith, Curiosity Crafter, Elturel Survivors, Urabrask the Hidden, Notion Thief, Scalding Tarn.

## Official artifact

[`deck.cod`](deck.cod) — Cockatrice XML. Written with `python3 scripts/to_cockatrice.py decks/2026-09-30-goro-goro/`. Preferred prints from `preferences/printings.json` are applied.

## Validate

`python3 scripts/scryfall.py validate decks/2026-09-30-goro-goro/list.txt --format commander --commander "Goro-Goro and Satoru"`

```
format=commander cards=100 identity=UBR commander=Goro-Goro and Satoru
WARN  expensive: Scalding Tarn ($35.58)
OK
```

`deck.cod` validate: same **OK** output.
