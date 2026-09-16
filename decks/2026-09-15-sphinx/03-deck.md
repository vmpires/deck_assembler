# Stage 3 — Deck

- **Name:** Sphinx Control
- **Format:** commander
- **Commander / shell:** Yennett, Cryptic Sovereign
- **Mechanic:** A (odd Sphinx tribal) + C (odd-cost Esper control)
- **Bracket (EDH) or role (Pauper):** Bracket 3
- **Game Changers (EDH):** none
- **Expensive cards to flag:** Urza's Incubator (~$20), Spellseeker (~$18), Raffine's Tower (~$13), Raise the Palisade (~$12), Swan Song (~$10). Scryfall USD for the list is ~$180.

## Game plan

Keep the top card odd. Attack Yennett (flying, vigilance, menace) and free-cast a 5- or 7-drop Sphinx, a tribal enchantment, or an answer. Unesh, Dream Trawler, and Isperia, Supreme Judge are even — cast them from hand. Interaction is almost all odd (Swords, Void Rend, Toxic Deluge, Cleansing Nova) so it is also a legal Yennett hit. Win in the air, with Kindred Dominance / Raise the Palisade as one-sided board wipes, or by casting Approach of the Second Sun **from hand** (Yennett cannot win with it; that ability requires from-hand).

X spells are not in the list. Do not put even rocks on top; Brainstorm / Opt / Prognostic Sphinx / Mystic Sanctuary (return an odd instant) fix the top.

## Categories

Counts should match `list.txt` (100 cards, 37 lands).

- **Commander:** Yennett, Cryptic Sovereign (1)
- **Ramp / mana:** Sol Ring, Wayfarer's Bauble, Arcane Signet, Talisman of Dominance, Talisman of Progress, Talisman of Hierarchy, Thought Vessel, Fellwar Stone, Worn Powerstone, Gilded Lotus (10)
- **Card advantage:** Brainstorm, Preordain, Opt, Consider, Read the Bones, Brainsurge, Phyrexian Arena, Kindred Discovery, Vanquisher's Banner, Trinket Mage, Spellseeker (11)
- **Interaction:** Swords to Plowshares, Path to Exile, Pongify, Rapid Hybridization, Swan Song, An Offer You Can't Refuse, Void Rend, Anguished Unmaking, Generous Gift, Stroke of Midnight, Toxic Deluge, Cleansing Nova, Time Wipe, Absorb, Dovin's Veto, Kindred Dominance, Raise the Palisade (17)
- **Engine / synergy:** 17 Sphinxes (Raffine, Prognostic, Dazzling, Defiler of Dreams, Glyph Keeper, Isperia the Inscrutable, Sphinx of the Revelation, Windreader, Magister, Enigma Sphinx, Enigma Thief, Inspired, Sphinx of Uthuun, Sphinx of the Final Word, Unesh, Dream Trawler, Isperia, Supreme Judge); Herald's Horn, Urza's Incubator, Reflections of Littjara; Aqueous Form, Whispersilk Cloak, Lightning Greaves (23)
- **Win conditions:** flying damage, Magister Sphinx (set a life total to 10), Approach of the Second Sun from hand (1, counted here; already listed as a card in the 100)
- **Lands:** 37 (4 Island, 3 Plains, 3 Swamp, Path of Ancestry, Mystic Sanctuary, Esper duals/triome, Command Tower, Reliquary Tower, Fabled Passage)
- **Sideboard (Pauper):** n/a

Approach is in the 100 once (win conditions), not double-counted in the numeric total: 1+10+11+17+23+37 = 99, plus Approach = 100.

## Official artifact

[`deck.cod`](deck.cod) — Cockatrice XML. Regenerated with `python scripts/to_cockatrice.py decks/2026-09-15-sphinx/`. This is the file to open in Cockatrice.

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
1 Enigma Thief
1 Inspired Sphinx
1 Sphinx of Uthuun
1 Sphinx of the Final Word
1 Unesh, Criosphinx Sovereign
1 Dream Trawler
1 Isperia, Supreme Judge
1 Herald's Horn
1 Urza's Incubator
1 Kindred Discovery
1 Reflections of Littjara
1 Kindred Dominance
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
1 Worn Powerstone
1 Gilded Lotus
1 Swords to Plowshares
1 Path to Exile
1 Pongify
1 Rapid Hybridization
1 Swan Song
1 An Offer You Can't Refuse
1 Void Rend
1 Anguished Unmaking
1 Generous Gift
1 Stroke of Midnight
1 Toxic Deluge
1 Cleansing Nova
1 Time Wipe
1 Absorb
1 Dovin's Veto
1 Aqueous Form
1 Whispersilk Cloak
1 Lightning Greaves
1 Read the Bones
1 Brainsurge
1 Phyrexian Arena
1 Approach of the Second Sun
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
1 Temple of Deceit
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
