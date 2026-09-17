# Stage 2 — Mechanics

- **Pick:** **Captain N'ghathrod** (locked)
- **Format:** commander
- **Bracket / role target:** **Bracket 3** — keep ≤3 **Game Changers** unless Victor explicitly wants Bracket 4 tuning. Current GCs in the list: **Demonic Tutor**, **Sol Ring** (Wizards Game Changer list). Adding **Mystic Remora** or **Rhystic Study** would be a deliberate third GC slot.
- **Idea reminder:** Faster, more fatal horror-mill — trim slow taplands and pet slots; sharpen interaction and mana; align win conditions.

## Current plan (baseline)

The import plays like a **kitchen-sink Dimir mill** deck with a **horror combat** sub-theme:

1. **Mill opponents** with crabs, enchantments, sorceries, and **Bruvac**.
2. **Attack with horrors** (commander grants menace) to mill again on combat damage.
3. **Occasionally steal** the best creature/artifact an opponent milled this turn (**N'ghathrod** end step).
4. **Side lanes:** graveyard theft (**Extract from Darkness**, **Memory Plunder**), **Jace, Wielder of Mysteries** backup, board wipes (**Toxic Deluge**, **Damnation**).

**Friction today:** mana is slow; many one-shot mill sorceries don’t advance the board; several cards don’t care about Horror type or combat (**Kitsune's Technique**, **Chasm Skulker**, **Patient Rebuilding**); **Jace, Wielder of Mysteries** fights **Psychic Corrosion** and the “mill them” focus.

---

## Plans

Propose **four upgrade directions**. All exemplars confirmed with `python3 scripts/scryfall.py`.

### A. Menace Raiders (combat-first horror)

- **How it wins:** Curve **Horror** creatures with menace (from commander), connect for **large combat mills**, then **steal** a huge milled creature at end step. Backup: **Toxic Deluge** / **Damnation** then rebuild with stolen bodies.
- **A normal turn:** T2 rock or **Ancient Cellarspawn** → T3–4 horror (e.g. **Silent Hallcreeper**, **Appendage Amalgam**, **Umbris**) → attack with menace → mill 4–8+ → steal their best milled threat.
- **Support categories:** Horror density, cost reduction, equipment (**Greaves** / **Boots** stay), selective mill (not full sorcery-mill package), efficient removal, **untapped** duals.
- **Exemplars:** **Ancient Cellarspawn**, **Appendage Amalgam**, **Aboleth Spawn**, **Silent Hallcreeper** (in list), **Umbris, Fear Manifest** (in list), **Drown in the Loch**, **Counterspell**, **Watery Grave**, **Clearwater Pathway**
- **Bracket (EDH):** Bracket 3 — keeps **Demonic Tutor** / **Sol Ring**; avoids extra GC draw engines unless Victor swaps one in.
- **Profile fit:** Strong synergy (combat + tokens/typal horrors). Cuts most “mill 13 for {5}” sorcery speed without **Bruvac** support. No stax.

### B. Bruvac Burst (combo-mill acceleration)

- **How it wins:** **Bruvac the Grandiloquent** doubles mill; chain **cheap multi-mill** triggers and **Psychic Corrosion** / **Fractured Sanity** until libraries are gone. **Jace, Wielder of Mysteries** becomes optional (often cut).
- **A normal turn:** Deploy **Bruvac** with protection (**Greaves**, **Spellskite**) → one **Maddening Cacophony** / **Archive Trap** / **Ashiok, Dream Render** activation → opponent loses half their library; repeat.
- **Support categories:** Tutor finds **Bruvac** or protection (**Demonic Tutor** already there), flash interaction, **Ashiok** to shut off searches and exile graveyards, fewer weak beaters.
- **Exemplars:** **Bruvac the Grandiloquent** (in list), **Archive Trap**, **Ashiok, Dream Render**, **Maddening Cacophony** (in list), **Psychic Corrosion** (in list), **An Offer You Can't Refuse** *(validate before list stage)*, **Talisman of Dominance**
- **Bracket (EDH):** Upper Bracket 3 — same GC count; faster goldfish than A but less combat flavor.
- **Profile fit:** Synergy-first mill; acceptable graveyard hate via Ashiok. **Not** full stax — Ashiok is narrow. Less horror tribal.

### C. Library Theft (N'ghathrod value engine)

- **How it wins:** Force cards into opposing graveyards from the **library**, then **steal** the best creature/artifact every end step (**N'ghathrod**) and **Extract from Darkness** / **Mnemonic Betrayal** bursts. Combat mill is setup, not the only kill.
- **A normal turn:** Mill 6–10 on their turn (crabs + combat) → end step steal **Sol Ring**-tier artifact or their commander → snowball board. **Notion Thief** + wheels trimmed (less **Whispering Madness**).
- **Support categories:** Steady mill engines, theft spells, recursion (**Persist**), removal for what you can’t steal.
- **Exemplars:** **Mnemonic Betrayal**, **Extract from Darkness** (in list), **Notion Thief** (in list), **Ruin Crab** / **Hedron Crab** (in list), **Persist**, **Phyrexian Arena**, **Polluted Delta** (in list)
- **Bracket (EDH):** Bracket 3 — can feel “combo-adjacent” when theft chains; still no hard locks.
- **Profile fit:** Uses graveyard as Victor’s list already does; politics of stealing commanders — acceptable for this upgrade pitch.

### D. Balanced Bracket 3 (recommended default)

- **How it wins:** **Primary:** combat horrors + **Bruvac** as a “boss” mill multiplier, not a full sorcery-mill deck. **Secondary:** **Toxic Deluge** / **Damnation** stabilize; **Jace, Wielder of Mysteries** **cut** unless Victor wants self-mill backup.
- **A normal turn:** Untapped mana → deploy threat or **Bruvac** → hold **Counterspell** / **Drown in the Loch** → attack or crack a one-shot mill spell → steal on end step.
- **Support categories:** ~10–12 horrors, ~8–10 mill pieces (not 20), 8–10 interaction, 10–12 ramp/rocks, 36–38 lands with **tapland count reduced**.
- **Exemplars:** **Ancient Cellarspawn**, **Aboleth Spawn**, **Bruvac the Grandiloquent**, **Psychic Corrosion**, **Drown in the Loch**, **Counterspell**, **Mystic Remora** *(third GC — flag to Victor)*, **Talisman of Dominance**, **Watery Grave**
- **Bracket (EDH):** Bracket 3 if we **hold at 3 Game Changers** (e.g. Tutor + Sol Ring + Remora **or** skip Remora for **Phyrexian Arena**).
- **Profile fit:** Best match to “way better, faster, more fatal” without becoming cEDH or stax.

---

## Cross-plan upgrades (preview — not final 99)

These show up in most plans; full cuts/adds land in Stage 3 after Victor’s pick.

| Faster | More fatal | Likely cuts (examples) |
| --- | --- | --- |
| **Watery Grave**, **Clearwater Pathway**, **Talisman of Dominance**, trim **Dimir Aqueduct** / **Guildgate** / **Ash Barrens** | **Ancient Cellarspawn**, **Drown in the Loch**, **Counterspell**, keep **Toxic Deluge** / **Damnation** | **Kitsune's Technique**, **Chasm Skulker**, **Patient Rebuilding**, **Fleet Swallower**, **In Garruk's Wake**, **Murder**, **Jace, Memory Adept** |
| **Preordain** stays; consider **Phyrexian Arena** or **Mystic Remora** (GC) | **Bruvac** + fewer slow sorceries (**Traumatize**, **Tunnel Vision**, **Mind Funeral**) unless Plan B | **Whispering Madness** (chaos wheel), **Dimir Keyrune** |

**Expensive cards already in list (flag):** Damnation, Demonic Tutor, Bruvac, Cover of Darkness, Morphic Pool (validate output on import).

---

## Victor’s pick (recorded)

- **Plan A — Menace Raiders**
- **No third Game Changer** — keep **Phyrexian Arena**, no Mystic Remora
- **Cut** Jace, Wielder of Mysteries
- **Mind flayers:** keep only strong combat Horrors (**Grazilaxx** kept); cut flavor-only Illithid pieces

## Stop (cleared)

Stage 3 complete — see `list.txt`, `03-deck.md`, `deck.cod`.

---

## Stop (historical)

**Waiting for Victor:** pick **A**, **B**, **C**, or **D** (or a hybrid, e.g. “D but keep Jace”). Optional sub-choices:

1. **Third Game Changer:** **Mystic Remora** vs stay at two GCs and use **Phyrexian Arena**.
2. **Keep or cut** **Jace, Wielder of Mysteries**.
3. **Flavor floor:** minimum horror count / keep **mind flayer** package (**Grazilaxx**, **Illithid Harvester**, etc.)?

Do **not** write `list.txt` / `deck.cod` until this gate clears.
