# Stage 2 — Mechanics

- **Pick:** **Rakdos, Lord of Riots** (locked)
- **Format:** commander
- **Bracket / role target:** **Bracket 4 (Optimized)** — list already has six Game Changers. Stay under cEDH. Cap is not 3 GCs here; name every GC we keep or add.
- **Idea reminder:** Quicker and more fatal — same commander. Damage this turn should let us **cast and kill**, not just put a 10-drop into play.

## Current plan (baseline)

The import is a **kitchen-sink Rakdos dump** list:

1. **Ping** with tap creatures, a few burn spells, and ping lands so an opponent loses life.
2. **Cast Rakdos**, then **discount** Eldrazi / Blightsteel / demons into play.
3. **Hope** Greaves/Boots or a Purphoros trigger makes that dump matter the same turn.
4. **Side lanes:** **Torment of Hailfire** + rituals, singleton **Reanimate**, **Chandra's Ignition**.

**Friction today:** tap-pingers are slow; several Eldrazi don’t kill; haste is thin; no cheat outlet if Rakdos is answered.

---

## Plans

Propose **four upgrade directions**. All exemplars confirmed with `python3 scripts/scryfall.py`.

### A. Instant Enable, Haste Dump (recommended default)

- **How it wins:** Cheap **opponent** damage (often at instant/sorcery speed) → cast Rakdos → drop **Blightsteel Colossus** / **Ulamog** / **Sire of Seven Deaths** **with haste** and attack immediately. Infect or annihilator ends someone that turn.
- **A normal turn:** T1–2 **Tectonic Hazard** / **Chain Lightning** / **Boltwave** / **Flame Rift** → T3 Rakdos + **Mass Hysteria** or **Anger** in the yard → T3–4 free **Blightsteel** swings for 10 poison.
- **Support categories:** 1–2 mana burn that hits players, haste (Anger / Mass Hysteria / Fervor / keep Greaves), 6–8 actual kill creatures (cut the casual Eldrazi), fast mana already in list, premium removal.
- **Exemplars:** **Tectonic Hazard**, **Chain Lightning**, **Price of Progress**, **Roiling Vortex**, **Mass Hysteria**, **Anger**, **Simian Spirit Guide**, **Blightsteel Colossus** (in list)
- **Bracket (EDH):** Bracket 4 — keeps existing GCs; **Ancient Tomb** (GC, ~$131) and **Imperial Seal** (GC, ~$170) are optional speed adds, not required.
- **Profile fit:** Combat-first, synergy with the commander. No stax. Fastest version that still *is* a Rakdos dump deck.

### B. Cheat Parallel (Sneak / Breach)

- **How it wins:** **Sneak Attack**, **Through the Breach**, **Purphoros, Bronze-Blooded**, and **Ilharg, the Raze-Boar** put the fatty in **with haste** even if nobody lost life. Rakdos becomes a second, cheaper dump outlet — not a bottleneck.
- **A normal turn:** T3 **Sneak Attack** → `{R}`: **Blightsteel** attacking. Recur the same creature next turn or follow with **Ulamog**. Commander tax never comes up.
- **Support categories:** Cheat enchantments/creatures, 8–10 dump hits that win on attack (Blightsteel, Ulamog, Void Winnower, It That Betrays), discard/draw to refill hand after sneak, same burn package as A only as backup.
- **Exemplars:** **Sneak Attack**, **Through the Breach**, **Purphoros, Bronze-Blooded**, **Ilharg, the Raze-Boar**, **Quicksilver Amulet**, **Anger**
- **Bracket (EDH):** Bracket 4 — goldfish can be faster than A; more “combo-adjacent,” still not a cEDH storm deck.
- **Profile fit:** High synergy with the *payload*, lower synergy with Rakdos himself. Best if you often fail to ping before you want to dump.

### C. ETB Burn Kill

- **How it wins:** **Purphoros, God of the Forge**, **Terror of the Peaks**, **Warstorm Surge**, **Agate Instigator**, **Impact Tremors** — the dump **deals its power as damage** when it enters. Combat is optional. **Chandra's Ignition** on Rakdos or a Colossus wipes the table. **Bloodletter of Aclazotz** doubles.
- **A normal turn:** Enchantment/creature damage engine → enable Rakdos with the same trigger → drop a 10+ body → 10+ to each opponent (or one player dead). Repeat.
- **Support categories:** ETB/cast-trigger damage, token/enter density (Agate Instigator offspring), keep the best dump creatures, cut pingers that don’t also trigger Purphoros well.
- **Exemplars:** **Purphoros, God of the Forge** (in list), **Terror of the Peaks** (in list), **Warstorm Surge**, **Agate Instigator**, **Impact Tremors** (in list), **Chandra's Ignition** (in list)
- **Bracket (EDH):** Bracket 4 — table-wide damage is more “fatal” in multiplayer than attacking one player with Blightsteel.
- **Profile fit:** Combat/tokens profile. Slightly less infect-kill, more “everyone is at 10 after one dump.”

### D. Ritual X-Drain

- **How it wins:** **Dark Ritual**, **Cabal Ritual**, **Seething Song**, **Jeska's Will**, **Neheb, the Eternal** into **Torment of Hailfire** / **Exsanguinate**. Creatures are backup. Rakdos discount is unused for the primary kill.
- **A normal turn:** T2–3 ritual into **Jeska's Will** → T4 **Torment** for a lethal X, or **Neheb** combat then X-spell.
- **Support categories:** Rituals, wheels/impulse for gas, one or two X drains, cut most Eldrazi.
- **Exemplars:** **Jeska's Will** (in list), **Dark Ritual** (in list), **Seething Song** (in list), **Cabal Ritual**, **Neheb, the Eternal** (in list), **Exsanguinate**, **Torment of Hailfire** (in list)
- **Bracket (EDH):** Bracket 4 — can goldfish very fast; the 99 stops looking like a Rakdos creature deck.
- **Profile fit:** Combo-leaning, still 2-card (mana + X). Weakest commander synergy of the four.

---

## Cross-plan upgrades (preview — not final 99)

These show up in most plans; full cuts/adds land in Stage 3 after the pick.

| Faster | More fatal | Likely cuts (examples) |
| --- | --- | --- |
| **Tectonic Hazard**, **Chain Lightning**, **Simian Spirit Guide**, trim **Jagged Barrens** / **Dragonskull Summit** | **Haste**: **Anger**, **Mass Hysteria** or **Fervor**; keep **Blightsteel** / **Ulamog** / **Sire of Seven Deaths** | **Spear Spewer**, **Thermo-Alchemist**, **Lobber Crew**, **Nettle Drone**, **Unruly Catapult**, **Creeping Bloodsucker**, **Rakdos Cackler** |
| Untapped duals already good; cut ping lands | **Sneak Attack** (if B or hybrid); **Warstorm Surge** / **Agate Instigator** (if C) | **Desolation Twin**, **Dread Cacodemon**, **Artisan of Kozilek**, **Pathrazer of Ulamog**, **Conduit of Ruin** |
| Keep **Sol Ring** / rituals | Keep **Deadly Rollick** / **Deflecting Swat** (not GCs) | **Bontu's Monument**, **Theater of Horrors**, **Sarkhan's Unsealing**, **Sanctum of Stone Fangs**, **Shivan Gorge**, **Leechridden Swamp**, **Sunscorched Desert**, **Cryptolith Fragment** |

**Game Changers already in list:** Chrome Mox, Demonic Tutor, Vampiric Tutor, Gamble, Jeska's Will, Orcish Bowmasters.

**Optional extra GCs (flag, expensive):** Ancient Tomb (~$131), Imperial Seal (~$170), Mana Vault (~$120), Grim Monolith (~$483).

**Expensive non-GCs already in list (flag):** Deflecting Swat, Deadly Rollick, Cavern of Souls, fetches, Blightsteel, tutors as above.

---

## Victor’s pick (recorded)

- **Plan A — Instant Enable, Haste Dump**
- **Ancient Tomb** added (seventh GC) for speed. Did **not** add Imperial Seal / Mana Vault / Grim Monolith.
- Casual Eldrazi **cut** (Artisan, Pathrazer, Desolation Twin, Dread Cacodemon, Conduit of Ruin).
- **Blightsteel** remains the single-player hammer; **Purphoros** / **Terror of the Peaks** / **Impact Tremors** stay as dump amplifiers, not a full Plan C package.

## Stop (cleared)

Stage 3 complete — see `list.txt`, `03-deck.md`, `deck.cod`.
