# Stage 3 — Deck

- **Name:** Every spell deals 1
- **Format:** commander
- **Commander / shell:** Ghyrson Starn, Kelermorph
- **Mechanic:** **A. Every spell deals 1**, with a defensive suite
- **Bracket (EDH) or role (Pauper):** High Bracket 3 / low Bracket 4 (2 Game Changers)
- **Game Changers (EDH):** Fierce Guardianship, Cyclonic Rift
- **Expensive cards to flag:** Deflecting Swat (~$76), Fierce Guardianship (~$67), Mana Drain (~$55), Force of Negation (~$46), Cyclonic Rift (~$39), Misty Rainforest (~$35), Scalding Tarn (~$33), Vivi Ornitier (~$33), Arid Mesa (~$31), Prismatic Vista (~$30), Otawara, Soaring City (~$28), Ghyrson Starn, Kelermorph (~$27), Birgi, God of Storytelling (~$25), Polluted Delta (~$21). **Mana Drain**, **Deflecting Swat**, and **Force of Negation** are not Game Changers. **Force of Will** came out. **Rhystic Study** and **Jeska's Will** stayed out.

## Game plan

Hold the early turns with counters, bounce, and two combat resets. **Force of Negation** is the free counter on an opponent's turn: exile a blue card instead of paying, counter a noncreature spell, and exile that spell. **Aetherize** and **Aetherspouts** send attacking creatures back. **Slip Out the Back** and **Shore Up** protect Ghyrson. **Swiftfoot Boots** gives him hexproof. **Blasphemous Act** clears a large board. **End the Festivities**, **Electrickery**, and **Blazing Volley** deal exactly 1, so they clear small creatures and Ghyrson deals 2 more to each of those same targets. **Third Path Iconoclast** makes a Soldier whenever you cast a noncreature spell, and those Soldiers block.

Once a trigger creature is on the board, cheap spells are the damage. **Firebrand Archer**, **Kessig Flamebreather**, and **Coruscation Mage** deal 1 to each opponent when you cast a noncreature spell. **Electrostatic Field** does it for an instant or sorcery. **Vivi Ornitier** does it, grows, and can add mana equal to his power once each turn. **Thermo-Alchemist** and **Gelectrode** tap for 1 and untap when you cast an instant or sorcery. **Harmonic Prodigy** makes a triggered ability of a Shaman or another Wizard trigger an additional time, so those 1-damage triggers happen twice and Ghyrson answers each one. **Archmage Emeritus** draws whenever you cast or copy an instant or sorcery. **Curiosity** is on a pinger that does not deal damage off the draw. It is not on **Niv-Mizzet, Parun**.

**Grapeshot** closes. Each copy deals 1, and Ghyrson deals 2 to that same target. **Pyretic Ritual** and **Desperate Ritual** are spells, so they trigger the pingers, and they pay for the copies. **Mana Drain** counters a spell and adds that much colorless on your next main phase, which is another turn of pings.

**Talisman of Creativity**, **Shivan Reef**, and **City of Brass** are not in the deck. Each deals exactly 1 to you, and Ghyrson would deal 2 more to you. **Fiery Islet** costs 1 life. That is not damage. **Guttersnipe** deals 2 and is not in the deck.

## Categories

Counts match `list.txt` / `deck.cod` (100 cards, no card images).

- **Commander:** Ghyrson Starn, Kelermorph (1)
- **Trigger creatures:** 8 (Archer, Flamebreather, Coruscation Mage, Electrostatic Field, Thermo-Alchemist, Vivi, Gelectrode, Harmonic Prodigy)
- **Spells that deal exactly 1:** 4 (End the Festivities, Electrickery, Blazing Volley, Grapeshot)
- **Cheap spells:** 10 cantrips and two rituals
- **Draw:** 7 (Archmage Emeritus, Mystic Remora, Curiosity, Expressive Iteration, Dig Through Time, Treasure Cruise, Big Score)
- **Mana and blockers:** 11, including Birgi, Storm-Kiln Artist, Third Path Iconoclast, and Swiftfoot Boots
- **Defense:** 23 (counters, bounce, Aetherize, Aetherspouts, Blasphemous Act, the two protection instants)
- **Lands:** 36 (8 Island, 5 Mountain, plus duals and fetches)
- **Sideboard (Pauper):** n/a

## Import

- **Official:** [`deck.cod`](deck.cod) (Cockatrice). Written with `python3 scripts/to_cockatrice.py decks/2026-10-29-ghyrson/`.
- Working copy: [`list.txt`](list.txt). Commander / Deck sections, role headers as comments, no images.

Preferred prints from `preferences/printings.json` are applied by that export.

## Validate

`list.txt` and `deck.cod`:

```
format=commander cards=100 identity=UR commander=Ghyrson Starn, Kelermorph
WARN  expensive: Ghyrson Starn, Kelermorph ($27.28); Vivi Ornitier ($32.64); Birgi, God of Storytelling ($24.88); Cyclonic Rift ($39.05); Deflecting Swat ($76.05); Fierce Guardianship ($67.32); Force of Negation ($45.74); Mana Drain ($54.90); Arid Mesa ($30.99); Misty Rainforest ($35.33); Otawara, Soaring City ($27.82); Polluted Delta ($20.95); Prismatic Vista ($29.95); Scalding Tarn ($33.29)
OK
```
