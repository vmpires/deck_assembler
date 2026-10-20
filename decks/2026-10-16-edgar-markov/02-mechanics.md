# Stage 2 — Mechanics

- **Pick:** **Edgar Markov** (locked)
- **Format:** commander
- **Bracket / role target:** **Bracket 3** — at most **3 Game Changers**, no MLD, no extra-turn chains, no two-card infinites unless you opt into combo. Stax Game Changers (**Drannith Magistrate**, **Humility**, **Tergrid**, **Braids, Cabal Minion**, **The Tabernacle at Pendrell Vale**) stay out.
- **Idea reminder:** Mardu Vampire tribal that actually uses eminence and combat, not a pile of expensive Mardu staples.

## Plans

Four distinct 99s. All exemplars confirmed with `python3 scripts/scryfall.py card "…"`.

### A. Eminence Swarm (recommended)

- **How it wins:** Cast cheap Vampire spells from turn 1 so **Edgar** (in the command zone) floods the board with 1/1s. Anthems and **Shared Animosity** turn the swarm into a lethal combat step. **Sanctum Seeker** drains while you attack. Cast Edgar himself only when the team is wide enough that his attack trigger ends someone.
- **A normal turn:** T1 **Knight of the Ebon Legion** or **Vicious Conquistador** (token from eminence) → T2 another 2-drop Vampire + swing with two bodies → T3 lord or **Shared Animosity** → T4–5 crash, hold **Akroma's Will** or a wipe.
- **Support categories:** 1–2 CMC Vampires, tribal anthems, cheap card draw that likes small bodies, haste/combat tricks, 8–10 interaction, 35–37 lands, low curve.
- **Exemplars:** **Knight of the Ebon Legion**, **Vicious Conquistador**, **Dusk Legion Zealot**, **Legion Lieutenant**, **Shared Animosity**, **Sanctum Seeker**, **Welcoming Vampire**, **Mirror Entity**, **Skullclamp**
- **Bracket (EDH):** Bracket 3. Fast goldfish, still interactive, not a combo kill.
- **Profile fit:** Best match — combat, tokens, tribal. Synergy first. No stax, no chaos.
- **Risk:** One **Farewell**-class wipe resets you; the plan is obvious.

### B. Attack-Trigger Legion

- **How it wins:** Attack every turn with **nontoken** Vampires so **Mavren Fein**, **Preacher of the Schism**, **Clavileño**, and **Sanctum Seeker** print extra bodies or drain. **Drana, Liberator of Malakir** and Edgar’s attack trigger grow the team. Combat damage, not sacrifice, is the kill.
- **A normal turn:** Deploy a 3-drop attacker → attack to make a lifelink token (**Mavren** / **Preacher** / **Legion's Landing**) → next turn Edgar or **Drana** connects and the board snowballs.
- **Support categories:** Attack-trigger Vampires, “safe attack” pieces, extra combat-adjacent pump, lifelink tokens, targeted removal, slightly higher curve than A.
- **Exemplars:** **Mavren Fein, Dusk Apostle**, **Preacher of the Schism**, **Clavileño, First of the Blessed**, **Drana, Liberator of Malakir**, **Sanctum Seeker**, **Legion's Landing**, **Dolmen Gate**, **Reconnaissance**
- **Bracket (EDH):** Bracket 3 — same GC cap; slower than A, more value from connecting.
- **Profile fit:** Combat and attack-trigger value. Tokens are a byproduct of attacking, not the whole deck.
- **Risk:** Needs to connect; fog / pillowfort tables stall it. **Dolmen Gate** is expensive (~$29).

### C. Aristocrats Drain

- **How it wins:** Eminence tokens are **fodder**. **Blood Artist** / **Cruel Celebrant** ping the table; **Cordial Vampire** / **Indulgent Aristocrat** grow the team; **Elenda** or **Vito** turns a wipe or a lifegain trigger into a kill. Combat is optional.
- **A normal turn:** Make tokens → sack one to **Viscera Seer** or **Bartolomé** → drain + scry/counters → repeat. A board wipe with **Elenda** + **Cruel Celebrant** can finish the table.
- **Support categories:** Free/cheap sacrifice outlets, drain-on-death, recursion, token makers, wipes that you want to resolve.
- **Exemplars:** **Blood Artist**, **Cruel Celebrant**, **Cordial Vampire**, **Elenda, the Dusk Rose**, **Indulgent Aristocrat**, **Vito, Thorn of the Dusk Rose**, **Viscera Seer**, **Bartolomé del Presidio**
- **Bracket (EDH):** Bracket 3 if we skip **Exquisite Blood** / **Sanguine Bond** loops and extra GCs. Those loops would be a combo opt-in, not the default.
- **Profile fit:** **Weaker default.** Graveyard / aristocrats are not profile defaults. Pick this only if you want drain-not-combat.
- **Risk:** Plays like a black sacrifice deck with Vampire clothing; less “Markov attacks.”

### D. Midrange Lords

- **How it wins:** Fewer 1-drops, more **quality** Vampires. **Captivating Vampire**, **Stromkirk Captain**, **Edgar, Charmed Groom**, and **Bloodline Keeper** make a board that survives a small wipe. **Champion of Dusk** and **Twilight Prophet** refill. **Kindred Dominance** is the one-sided reset. Edgar is a 6-mana closer, not a token factory you never cast.
- **A normal turn:** T3–4 lord or **Bloodline Keeper** → make / pump Vampires → **Champion of Dusk** draws a pile → attack with first strike / flying threats, not 1/1s.
- **Support categories:** Lords, expensive draw, tribal finishers, wraths, a denser manabase, fewer Glass-cannon 1-drops.
- **Exemplars:** **Captivating Vampire**, **Stromkirk Captain**, **Edgar, Charmed Groom**, **Bloodline Keeper**, **Champion of Dusk**, **Twilight Prophet**, **Kindred Dominance**, **Vanquisher's Banner**
- **Bracket (EDH):** Bracket 3 — grindiest of the four; still Vampire tribal, not Mardu control.
- **Profile fit:** Tribal and combat, less token-swarm. Better if you dislike dying to the first board wipe.
- **Risk:** Eminence is partly wasted if the curve is too high; slower starts.

---

## Cross-plan notes (preview — not the 99)

| Almost always | Game Changers (pick ≤3) | Stay out unless asked |
| --- | --- | --- |
| Vampire density first; **Herald's Horn** / **Metallic Mimic**; Mardu rocks; **Kindred Dominance** as the tribal wipe | **Jeska's Will**, **Teferi's Protection**, **Demonic Tutor** or **Vampiric Tutor**. **Smothering Tithe** / **Ancient Tomb** / **The One Ring** are legal but expensive and optional. **Sol Ring** is **not** a Game Changer on the current list. | Stax GCs above. **Underworld Breach**, **Ad Nauseam**, **Bolas's Citadel** combo. Chaos wheels. |

**Expensive cards to flag later:** **Edgar Markov** (~$44), **Roaming Throne** (~$53), **Charismatic Conqueror** (~$24), **Dolmen Gate** (~$29), **Jeska's Will** / tutors / **Teferi's Protection** if we use those GC slots.

**Roaming Throne** copies Vampire triggers (eminence does **not** copy — it is not a Vampire you control; Edgar’s *attack* trigger and lords like **Mavren** / **Sanctum Seeker** do). Worth it in B and D; optional in A.

---

## Pick (recorded)

- **Hybrid A + D** — Eminence Swarm with a Midrange Lords spine
- **Game Changers (3):** **Jeska's Will**, **Teferi's Protection**, **Demonic Tutor**
- **Roaming Throne:** include (flag price)
- No aristocrats package (Plan C stays out)

## Stop (cleared)

Stage 3 complete — see `list.txt`, `03-deck.md`, `deck.cod`.

---

## Stop (historical)

Waiting for a pick: **A**, **B**, **C**, or **D** (or a hybrid, e.g. “A with a light drain package”).

Optional sub-choices:

1. **Game Changers:** none / two / three. Suggested three: **Jeska's Will**, **Teferi's Protection**, **Demonic Tutor**.
2. **Roaming Throne:** include (chase, ~$53) or skip.
3. If **C**: allow **Vito** + lifegain as a late kill, or keep drain strictly as combat/death triggers (no two-card infinite).

Do **not** write `list.txt` / `deck.cod` until this gate clears.
