# Stage 3 — Deck

- **Name:** Sphinx Control
- **Format:** commander
- **Commander / shell:** Yennett, Cryptic Sovereign
- **Mechanic:** A (odd Sphinx tribal) + C (odd-cost Esper control), leaner curve
- **Bracket (EDH) or role (Pauper):** Bracket 3
- **Game Changers (EDH):** none
- **Expensive cards to flag:** Urza's Incubator (~$20), Spellseeker (~$18), Raffine's Tower (~$13), Raise the Palisade (~$12), Swan Song (~$10)

## Game plan

Keep the top card odd, attack Yennett, free-cast a Sphinx or an odd answer. Early turns now have real plays: Judge's Familiar, Baleful Strix, Fatal Push, Warden of Evos Isle (other flyers cost {1} less), Empyrean Eagle. Unesh and Dream Trawler are even — cast them from hand. Win in the air; Raise the Palisade as the one-sided clear; Magister Sphinx as the life-total punch.

Even-from-hand speed: Counterspell, Supreme Verdict, Smuggler's Copter, Baleful Strix. Do not leave those on top for Yennett.

## Categories

Counts match `deck.cod` / `list.txt` (100 cards, 36 lands).

- **Commander:** Yennett, Cryptic Sovereign (1)
- **Ramp / mana:** Sol Ring, Wayfarer's Bauble, Arcane Signet, Talisman of Dominance, Talisman of Progress, Talisman of Hierarchy, Thought Vessel, Fellwar Stone (8)
- **Card advantage:** Brainstorm, Preordain, Opt, Consider, Read the Bones, Brainsurge, Phyrexian Arena, Kindred Discovery, Vanquisher's Banner, Trinket Mage, Spellseeker, Smuggler's Copter (12)
- **Interaction:** Swords to Plowshares, Path to Exile, Pongify, Rapid Hybridization, Fatal Push, Swan Song, An Offer You Can't Refuse, Counterspell, Void Rend, Anguished Unmaking, Generous Gift, Stroke of Midnight, Toxic Deluge, Cleansing Nova, Time Wipe, Supreme Verdict, Absorb, Dovin's Veto, Raise the Palisade (19)
- **Engine / synergy:** 13 Sphinxes in the 99 (Raffine, Prognostic, Dazzling, Defiler of Dreams, Glyph Keeper, Isperia the Inscrutable, Sphinx of the Revelation, Windreader, Magister, Enigma Sphinx, Unesh, Dream Trawler, Serum Sovereign); Warden of Evos Isle, Empyrean Eagle, Brazen Borrower, Baleful Strix, Judge's Familiar; Herald's Horn, Urza's Incubator, Reflections of Littjara; Aqueous Form, Whispersilk Cloak, Lightning Greaves (24)
- **Win conditions:** flying damage, Magister Sphinx, Raise the Palisade
- **Lands:** 36 (4 Island, 3 Plains, 3 Swamp, Path of Ancestry, Mystic Sanctuary, Esper duals/triome, Command Tower, Reliquary Tower, Fabled Passage)
- **Sideboard (Pauper):** n/a

1+8+12+19+24+36 = 100.

**Cuts vs previous list:** Approach of the Second Sun, Kindred Dominance, Sphinx of Uthuun, Sphinx of the Final Word, Inspired Sphinx, Enigma Thief, Isperia, Supreme Judge, Gilded Lotus, Worn Powerstone, Temple of Deceit.

## Official artifact

[`deck.cod`](deck.cod) — Cockatrice XML. Regenerated with `python scripts/to_cockatrice.py decks/2026-09-15-sphinx/`. Preferred prints from `preferences/printings.json` are applied. Copy this file into Cockatrice to play the new list.

## Import

Working copy (`list.txt`):

```
Commander
1 Yennett, Cryptic Sovereign

Deck
1 Raffine, Scheming Seer
1 Prognostic Sphinx
1 Dazzling Sphinx
1 Defiler of Dreams
1 Glyph Keeper
1 Isperia the Inscrutable
1 Sphinx of the Revelation
1 Windreader Sphinx
1 Magister Sphinx
1 Enigma Sphinx
1 Unesh, Criosphinx Sovereign
1 Dream Trawler
1 Serum Sovereign
1 Warden of Evos Isle
1 Empyrean Eagle
1 Brazen Borrower
1 Baleful Strix
1 Judge's Familiar
1 Herald's Horn
1 Urza's Incubator
1 Kindred Discovery
1 Reflections of Littjara
1 Raise the Palisade
1 Vanquisher's Banner
1 Brainstorm
1 Preordain
1 Opt
1 Consider
1 Sol Ring
1 Wayfarer's Bauble
1 Arcane Signet
1 Talisman of Dominance
1 Talisman of Progress
1 Talisman of Hierarchy
1 Thought Vessel
1 Fellwar Stone
1 Smuggler's Copter
1 Swords to Plowshares
1 Path to Exile
1 Pongify
1 Rapid Hybridization
1 Fatal Push
1 Swan Song
1 An Offer You Can't Refuse
1 Counterspell
1 Void Rend
1 Anguished Unmaking
1 Generous Gift
1 Stroke of Midnight
1 Toxic Deluge
1 Cleansing Nova
1 Time Wipe
1 Supreme Verdict
1 Absorb
1 Dovin's Veto
1 Aqueous Form
1 Whispersilk Cloak
1 Lightning Greaves
1 Read the Bones
1 Brainsurge
1 Phyrexian Arena
1 Trinket Mage
1 Spellseeker
1 Command Tower
1 Path of Ancestry
1 Exotic Orchard
1 Arcane Sanctum
1 Raffine's Tower
1 Reliquary Tower
1 Prairie Stream
1 Sunken Hollow
1 Skycloud Expanse
1 Darkwater Catacombs
1 Glacial Fortress
1 Isolated Chapel
1 Drowned Catacomb
1 Temple of Enlightenment
1 Temple of Silence
1 Adarkar Wastes
1 Caves of Koilos
1 Underground River
1 Hallowed Fountain
1 Godless Shrine
1 Watery Grave
1 Deserted Beach
1 Shipwreck Marsh
1 Shattered Sanctum
1 Mystic Sanctuary
1 Fabled Passage
1 Island
1 Island
1 Island
1 Island
1 Plains
1 Plains
1 Plains
1 Swamp
1 Swamp
1 Swamp
```

## Validate

`list.txt` and `deck.cod`:

```
format=commander cards=100 identity=WUB commander=Yennett, Cryptic Sovereign
OK
```
