# Stage 2 — Mechanics

- **Pick:** **Ghyrson Starn, Kelermorph** (locked)
- **Format:** commander
- **Bracket / role target:** High Bracket 3 / low Bracket 4. At most **3 Game Changers**. No mass land destruction, no extra-turn chains, no two-card infinites unless you ask.
- **Idea reminder:** Izzet (`{1}{U}{R}`). Ward {2}. Another source you control deals exactly 1 damage, and Ghyrson deals 2 more to that same permanent or player. About $27. He does not trigger off his own 2 damage.

## Rules that bind every plan

All exemplars below were confirmed with `python3 scripts/scryfall.py`.

The 1 and the 2 are separate. A shock for 2, a bolt for 3, and **Guttersnipe** (2 damage to each opponent) do not trigger Ghyrson. **End the Festivities** deals 1 to each opponent and to each creature and planeswalker they control. Each of those is its own trigger, so Ghyrson deals 2 to each of them as well.

A source you control that deals exactly 1 to you is the same ability. **Talisman of Creativity**, **Shivan Reef**, and **City of Brass** would ping you for 1 and Ghyrson would deal 2 more to you. They stay out. **Ancient Tomb** deals 2, so Ghyrson does not trigger off it. It is still a Game Changer (about $125) and stays off the default list.

**Curiosity** on Ghyrson, or on a pinger that does not deal damage when you draw, is one card per hit. **Curiosity** on **Niv-Mizzet, Parun** is a two-card infinite: the draw deals 1, Curiosity draws, and it repeats. That pair stays out unless you ask for combo.

## Plans

Three distinct 99s.

### A. Every spell deals 1

- **How it wins:** Creatures that deal exactly 1 when you cast a spell, then Ghyrson adds 2 to each of those opponents. **Firebrand Archer**, **Kessig Flamebreather**, and **Coruscation Mage** deal 1 to each opponent when you cast a noncreature spell. **Electrostatic Field** does it for an instant or sorcery. **Thermo-Alchemist** taps for 1 to each opponent and untaps when you cast an instant or sorcery, so one spell lets you tap him again. **Vivi Ornitier** deals 1 to each opponent when you cast a noncreature spell, puts a +1/+1 counter on himself, and once each turn adds mana equal to his power. One of those creatures plus Ghyrson is 3 damage to each opponent per spell. Two of them is 6. **End the Festivities** is the one-mana spell that also hits their boards. **Grapeshot** is legal in Commander. Each copy deals 1, and Ghyrson adds 2 to that same target, so each copy is 3. **Archmage Emeritus** draws a card whenever you cast or copy an instant or sorcery.
- **A normal turn:** Ghyrson and one trigger creature are on the board. Cast a cheap instant or cantrip. The trigger creature deals 1 to each opponent, Ghyrson deals 2 to each, and Emeritus draws. Tap Thermo-Alchemist before or after the spell so he fires twice. A later turn with several spells casts Grapeshot at one player.
- **Support categories:** Cheap instants and sorceries, the cast-trigger creatures, one storm finisher, counterspells, a way to replay Ghyrson. **Birgi, God of Storytelling** (about $25) adds {R} whenever you cast a spell and keeps that mana through the turn. **Young Pyromancer** and **Third Path Iconoclast** make a creature token when you cast the spell. Those tokens do not deal the 1 by themselves. They matter if the deck also has an enter trigger from plan B.
- **Exemplars:** **Firebrand Archer**, **Kessig Flamebreather**, **Thermo-Alchemist**, **Electrostatic Field**, **End the Festivities**, **Grapeshot**, **Archmage Emeritus**
- **Bracket (EDH):** High Bracket 3. Flamebreather is about $3. Electrostatic Field is about $2. Archer, Thermo-Alchemist, and Grapeshot are under $1. A dedicated storm pile slides to low Bracket 4. **Vivi Ornitier** is about $33 and is the expensive version of the same trigger.
- **Profile fit:** Spellslinger, which is a default taste. The spells are the engine and the damage. Grapeshot is a finisher after a normal turn of spells, not an infinite combo.
- **Risk:** The trigger creatures have to be on the battlefield. Ghyrson has ward {2}. The Archer and Thermo-Alchemist do not. A removal spell on the trigger creature leaves you casting cantrips for cards and no damage. Guttersnipe looks like it belongs and deals 2, so it adds nothing for Ghyrson.

### B. Something enters, everyone takes 1

- **How it wins:** The 1 damage comes from a permanent entering, not from the spell you cast. **Impact Tremors** deals 1 to each opponent whenever a creature you control enters. **Agate Instigator** and **Molten Gatekeeper** do the same from the creature. **Reckless Fireweaver** does it when an artifact enters. **Weftstalker Ardent** does it when another creature or artifact enters. Ghyrson adds 2 to each opponent on every one of those. **Young Pyromancer** makes a 1/1 whenever you cast an instant or sorcery. **Third Path Iconoclast** makes a 1/1 Soldier artifact, so it triggers both the creature enters and the artifact enters. **Murmuring Mystic** makes a 1/1 Bird. **Loyal Apprentice** makes a hasty Thopter at the beginning of combat if you control your commander. One token with Tremors and Instigator on the board is 6 damage to each opponent before combat. **Goblin Bombardment** sacrifices a creature to deal 1 to any target, and Ghyrson adds 2, so the token can enter for damage and then be sacrificed for 3 more.
- **A normal turn:** Cast a token maker, then cast instants and sorceries. Each token enters, Tremors and Instigator fire, Ghyrson doubles each of those into 3. Attack with the tokens only if the board is empty. The damage does not need them to connect.
- **Support categories:** Token makers, the enter-damage enchantments and creatures, sacrifice for Bombardment, cheap spells to trigger the makers, interaction. The cast-trigger creatures from plan A are optional. This plan still works if the only damage is the enter trigger.
- **Exemplars:** **Impact Tremors**, **Agate Instigator**, **Molten Gatekeeper**, **Reckless Fireweaver**, **Young Pyromancer**, **Third Path Iconoclast**, **Goblin Bombardment**
- **Bracket (EDH):** High Bracket 3. Pyromancer is about $0.30. Iconoclast is about $0.40. Gatekeeper is about $0.20. Bombardment is about $3. Scryfall listed no price for Impact Tremors or Agate Instigator. A wide token turn with two enter triggers is a lot of damage for this bracket, and it is still one turn of spells rather than a loop.
- **Profile fit:** Tokens and a burn payoff that uses them. The bodies are there to enter. Combat is optional.
- **Risk:** The enter trigger cares about creatures and artifacts entering. A spell that deals 1 and makes no permanent does nothing for this plan. Board wipes remove the makers and the tokens. Bombardment plus a creature that returns itself every time it dies is a loop. That loop stays out.

### C. Point the 1, kill the creature

- **How it wins:** The 1 damage chooses a target, and Ghyrson deals 2 to that same target. Three damage kills a small creature or chips a player. **Walking Ballista** removes a +1/+1 counter to deal 1 to any target. **Goblin Bombardment** sacrifices a creature to do the same. **Electrickery** deals 1 to a creature you don't control, or 1 to each of those creatures if overloaded. **Blazing Volley** deals 1 to each creature your opponents control. **End the Festivities** hits their players and their boards. **Basilisk Collar** gives the equipped creature deathtouch and lifelink. On Ghyrson, the 2 damage he deals has deathtouch, so it destroys any creature it hits, and lifelink gains you 2 life per hit. The original 1 does not have deathtouch unless that source does.
- **A normal turn:** Ghyrson, Collar equipped. Remove a Ballista counter or cast Electrickery at a creature. That source deals 1, Ghyrson deals 2 with deathtouch, and the creature dies. Point the same activations at a player's life total when the board is clear. Volley and Festivities are the turns their board is wide.
- **Support categories:** Repeatable 1-damage abilities, the one-mana sweepers, Collar, countermagic, card draw. Token makers are useful only as Bombardment fodder. Cast-trigger creatures from plan A still work, and their "each opponent" damage does not need Collar.
- **Exemplars:** **Walking Ballista**, **Goblin Bombardment**, **Basilisk Collar**, **Electrickery**, **Blazing Volley**, **End the Festivities**
- **Bracket (EDH):** High Bracket 3. Ballista is about $10. Collar and Bombardment are about $3. Electrickery and Volley are under $1. This is the most interactive of the three and the slowest at killing three players, because many of the pings are aimed at one creature.
- **Profile fit:** Control and spellslinger. The 1 damage is removal that also moves life totals. Collar is one equipment, not an equipment deck.
- **Risk:** Collar has to be on Ghyrson. His 2 damage is the part with deathtouch. A 1-damage spell aimed at an x/4 still needs Ghyrson's 2, or the deathtouch on that 2, to finish the creature. Ballista spends counters. An empty Ballista does not ping.

## Cross-plan notes (preview — not the 99)

Shared shell: Ghyrson, cheap instants, countermagic, a way to protect him, lands that do not deal 1 to you.

| Almost always | Game Changers (pick ≤3) | Stay out unless asked |
| --- | --- | --- |
| Ghyrson, at least one source of exactly 1 damage, interaction | **Rhystic Study** (about $68). **Fierce Guardianship** (about $67). **Force of Will** (about $59). **Cyclonic Rift** (about $39). **Jeska's Will** (about $41). **The One Ring** (about $112). **Mystical Tutor** (about $17). **Gamble** (about $18). | **Guttersnipe**. Bolts and shocks that deal 2 or 3. **Talisman of Creativity**, **Shivan Reef**, **City of Brass**. **Curiosity** on **Niv-Mizzet, Parun**. Enter-the-battlefield loops. Extra-turn chains. Stax. **Underworld Breach**. |

## Pick

**A. Every spell deals 1**, with a large defensive suite so the deck can survive until the pingers are online. Plans B and C stay out. Game Changers are **Fierce Guardianship** and **Cyclonic Rift**. **Force of Will** was replaced with **Force of Negation**, which is not a Game Changer. See `list.txt`, `03-deck.md`, and `deck.cod`.

## Stop (cleared)

Stage 3 is written.
