# Stage 2 — Mechanics

- **Pick:** Mayael the Anima
- **Format:** commander
- **Bracket / role target:** high Bracket 3 / low Bracket 4 (3 Game Changers)
- **Idea reminder:** Green ramp, white defense, red haste and removal, power-5 creatures with enter and attack triggers. One late combat combo.

The enter-heavy plan and the attack-only plan were set aside. This file is the balanced plan, with one combo added inside it.

## Plans

### C. Balanced

- **How it wins:** Cast Mayael, ramp to six mana, and activate her. A power-5 creature enters and either does something immediately (draw, fight, destroy, make tokens, deal damage) or attacks and triggers. Craterhoof Behemoth and Moonshaker Cavalry end the game if the board is already wide. Combat damage is the normal kill.
- **A normal turn:** A land or a two-mana ramp spell, then Mayael on turn 3 if she is available. Protect her. Once six mana is open, activate, put a creature onto the battlefield, and attack if it has haste from Fires of Yavimaya, Rhythm of the Wild, Lightning Greaves, Swiftfoot Boots, or its own text. White removal clears a blocker. After combat, Bear Umbra can untap the lands so the six-mana activation is available again.
- **Support categories:** green ramp, power-5 enter triggers, power-5 attack triggers, haste, spot removal, a wrath, protection, card draw when a big creature enters
- **Exemplars:** Inferno Titan (3 damage on enter and on attack), Kogla, the Titan Ape (fights on enter, destroys an artifact or enchantment on attack), Dragonhawk, Fate's Tempest (exiles cards on enter and on attack), Terror of the Peaks (damage when another creature enters), Thorn Mammoth (fights when a creature enters), Avacyn, Angel of Hope (other permanents are indestructible), Etali, Primal Storm (casts from exile on attack), Ilharg, the Raze-Boar (puts a creature from hand onto the battlefield attacking)
- **Bracket (EDH) or role (Pauper):** High Bracket 3. Three Game Changers: Worldly Tutor, Natural Order, Seedborn Muse. Seedborn untaps Mayael on each opponent's turn, so the activation can happen four times a turn cycle. Natural Order sacrifices a green creature and puts a green creature onto the battlefield. Worldly Tutor puts a creature on top; activating Mayael before the next draw looks at that card in the top five.
- **Profile fit:** Combat, ramp, and incremental value from enter and attack triggers. No stax, no chaos, no extra-turn chain, no graveyard deck. Sun Titan returns a permanent with mana value 3 or less (a rock, a dork, Greaves). That is a small retrieve, not a reanimator plan.

Zacama, Primal Calamity untaps lands only if you cast it. Mayael and Natural Order skip that line. The 9/9 body and the damage and destroy abilities still work.

Apex Devastator is not in the list. Cascade happens when you cast it. Mayael does not cast the creature she puts in.

### The one combo — Hellkite Charger and Bear Umbra

Both cards are in the fair deck. Hellkite Charger is a 5/5 flying haste Dragon, so Mayael can put it onto the battlefield and it can attack that turn. Bear Umbra is +2/+2, umbra armor, and it untaps all lands when the enchanted creature attacks. Umbra armor is the white-and-green defense: if the creature would be destroyed, the aura is removed instead and the damage is cleared.

The loop is late. It needs both permanents and lands that can tap for `{5}{R}{R}` by themselves. Bear Umbra untaps lands, not rocks or creatures, so Sol Ring and Selvala do not refill the loop.

1. Bear Umbra is attached to a creature you will attack with. That creature can be Hellkite Charger, or another attacker in the same combat.
2. Declare attackers, including Hellkite Charger and the creature wearing Bear Umbra.
3. Two triggers go on the stack. Put Hellkite's payment trigger on the stack first, then Bear Umbra, so the lands untap first.
4. Bear Umbra resolves. All lands untap.
5. Hellkite's trigger resolves. Pay `{5}{R}{R}`. Attacking creatures untap. After this combat phase there is another combat phase.
6. Attack again. The same two triggers happen. Pay again.

That is infinite combat phases, not extra turns. Blockers tap to block and do not untap between these combats, so later swings usually get through. The table takes combat damage until it is gone.

If the lands cannot make two red, or Bear Umbra is not on an attacker, nothing loops. Hellkite is still a hasty flyer. Bear Umbra still untaps lands for Mayael's activation and still saves a creature once.

## Pick

**C. Balanced**, with Hellkite Charger and Bear Umbra as the only combo.

The Cockatrice edit on 2026-10-11 removed Hellkite Charger and Bear Umbra. That combo is not in the current `deck.cod`. Creatures stuck in hand are handled by Scroll Rack and Valakut Awakening, described in `03-deck.md`.
