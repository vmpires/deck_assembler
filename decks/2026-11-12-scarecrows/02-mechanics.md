# Stage 2 — Mechanics

- **Pick:** Reaper King
- **Format:** commander
- **Bracket / role target:** high Bracket 3 / low Bracket 4
- **Idea reminder:** Scarecrow typal. The commander lords Scarecrows and destroys a permanent whenever another Scarecrow enters. Five-color. The printed tribe is thin; every plan below uses glue (changelings, type-change, blink, or artifact synergy) so the destroy trigger actually fires.

## Plans

Propose 2–4 distinct game plans. Exemplar cards must already be confirmed with `scripts/scryfall.py`.

### A. Blink ETB control

- **How it wins:** Reaper King is a repeatable removal engine. Blink or bounce a Scarecrow, destroy a permanent, rinse. Once the table is stripped, the +1/+1 anthem and a few bodies close in combat. Not an infinite: `Deadeye Navigator` is `{1}{U}` per blink unless you later add a mana combo (we will not unless you ask).
- **A normal turn:** Land, maybe a rock. Cast a Scarecrow or changeling with the King out (one opponent permanent dies). End step: `Conjurer's Closet` / `Thassa, Deep-Dwelling` / `Soulherder` / `Teleportation Circle` blinks it again (second kill). Or spend `{1}{U}` on Deadeye during their turn to snipe a threat.
- **Support categories:** cheap Scarecrows and changelings as ammo; blink (instant, end-step, soulbond); ETB doublers (`Panharmonicon`; `Elesh Norn, Mother of Machines` if the budget is OK); recursion (`Scarecrone`); 5-color ramp and interaction.
- **Exemplars:** `Panharmonicon`; `Deadeye Navigator`; `Conjurer's Closet`; `Thassa, Deep-Dwelling` (~$25); `Ephemerate`; `Soulherder`; `Teleportation Circle`; `Eldrazi Displacer`; `Scarecrone`.
- **Bracket (EDH) or role (Pauper):** high Bracket 3 / low Bracket 4. The destroy trigger *is* the interaction; keep extra Game Changers to 3 in the 99.
- **Profile fit:** Control + tribal + combat backup. Best use of the commander's unique text. No stax, no chaos. `Thassa` and `Elesh Norn, Mother of Machines` (~$27) are expensive; Mother of Machines is not required.

### B. Type-change overlay

- **How it wins:** Paint every creature a Scarecrow (`Maskwood Nexus`, `Arcane Adaptation`, `Conspiracy`, `Rukarumel, Biologist`). Then play *good* ETB creatures and token-makers; each body (and each token, under Maskwood) is a Reaper King trigger. Combat still happens; the 99 is not skulkin filler.
- **A normal turn:** Type-changer in play. Cast `Spark Double` copying the King (two destroy triggers per Scarecrow) or dump a creature with a real ETB. `Hornet Queen` under Maskwood is four extra kills plus flying deathtouch. `Realmwalker` naming Scarecrow casts the rest off the top.
- **Support categories:** type-changers; premium ETB creatures; token producers that become Scarecrows; changelings as backup ammo; the same blink package as A, but thinner.
- **Exemplars:** `Maskwood Nexus`; `Arcane Adaptation`; `Conspiracy`; `Rukarumel, Biologist`; `Spark Double`; `Hornet Queen`; `Realmwalker`; `Blade of Selves` (myriad token copies ETB as Scarecrows if the equipped creature is one).
- **Bracket (EDH) or role (Pauper):** high Bracket 3 / low Bracket 4. Highest ceiling for the 99 because you are not forced to play mediocre printed scarecrows.
- **Profile fit:** Synergy first (type overlay is the engine). Feels slightly less "scarecrow pile," more "everything is a scarecrow." Tokens only count if Maskwood (or another *all creatures* changer) is out — `Rukarumel` and `Arcane Adaptation` do not hit tokens. `Conspiracy` *replaces* types rather than adding them; name Scarecrow.

### C. Changeling combat

- **How it wins:** Changelings are Scarecrows with no extra cards. Flood cheap shapeshifters, trigger the King as you develop, then `Mirror Entity` or tribal anthems overrun. Closest to a classic tribal aggro/midrange deck.
- **A normal turn:** `Changeling Outcast` or `Universal Automaton` early (unblockable / 1-mana Scarecrow). King comes down, each subsequent changeling pops a permanent. Late: pay X on `Mirror Entity` and swing.
- **Support categories:** dense changeling suite; tribal anthems and cost reduction; evasion; Reaper King as both lord and removal; light blink (you do not need a full soulbond package).
- **Exemplars:** `Mirror Entity`; `Changeling Outcast`; `Universal Automaton`; `Taurean Mauler`; `Unsettled Mariner`; `Realmwalker`; `Metallic Mimic`; `Patchwork Banner`; `Vanquisher's Banner`; `Urza's Incubator` (~$22, name Scarecrow).
- **Bracket (EDH) or role (Pauper):** Bracket 3 combat. Can sit at high 3 with Incubator, Realmwalker, and premium interaction; slower to strip the table than A or B because you are not retriggering the same body.
- **Profile fit:** Tribal + combat, which the profile likes. The printed scarecrows become optional spice, not the core.

### D. Artifact-creature midrange

- **How it wins:** Treat Scarecrows as an artifact-creature deck that happens to have a type lord. Cost-reduce them, recur them with `Scarecrone`, equip `Cranial Plating` or swing with a wide artifact board. Reaper King still kills permanents, but the backup plan does not need blink or Maskwood.
- **A normal turn:** Rocks and Inspectors make the next skulkin cheap. Cast two artifact creatures; King triggers once or twice. `Scarecrone` trades a spare body for a card, then later returns an artifact creature. Plating on the King (or a changeling) ends one player.
- **Support categories:** artifact cost reduction and affinity draw; Scarecrone loops; equipment / combat payoffs; colorless scarecrows as the curve; 5-color interaction still in the deck, just not the spine.
- **Exemplars:** `Scarecrone`; `Foundry Inspector`; `Urza's Incubator`; `Cranial Plating` (legal in Commander); `Thought Monitor`; `Emry, Lurker of the Loch`; `Metallic Mimic`; `Panharmonicon` (still good here).
- **Bracket (EDH) or role (Pauper):** Bracket 3 artifact midrange. Slightly lower floor than A/B if the King is answered, because Foundry Inspector and Thought Monitor do **not** trigger Reaper King unless a type-changer is out.
- **Profile fit:** Combat + artifacts + incremental value. Weakest "scarecrow-ness" of the four; strongest if you would rather play affinity than blink.

## Recommendation

**A** is the plan that makes Reaper King worth the five-color tax. **B** is the better 99 if you want the destroy trigger without playing bad scarecrows — it pairs cleanly with a *light* blink package. **C** if you want to attack. **D** if you want artifacts more than the type.

## Pick

**A. Blink ETB control** — locked. List is in `list.txt` / `deck.cod`.
