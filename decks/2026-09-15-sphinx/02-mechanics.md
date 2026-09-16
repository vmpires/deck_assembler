# Stage 2 — Mechanics

- **Pick:** Yennett, Cryptic Sovereign
- **Format:** commander
- **Bracket / role target:** Bracket 3
- **Idea reminder:** Esper Sphinx-shaped 99; odd mana values so Yennett’s attack trigger actually casts things.

Yennett constraint: prefer **odd MV** (1, 3, 5, 7, 9). Even staples (Counterspell, Sol Ring, Consecrated Sphinx, Unesh) are “cast from hand” cards, not free hits. **X spells are traps on top** — Yennett casts them with X = 0.

Skipped: extra-turn packages, stax, chaos/guessing Sphinxes (Master of Predicaments), graveyard-first (Scholar of the Lost Trove as a theme). Game Changers (Fierce Guardianship, Teferi’s Protection, Force of Will, Necropotence) stay out unless you ask for Bracket 4.

## Plans

Propose 2–4 distinct game plans. Exemplar cards must already be confirmed with `scripts/scryfall.py`.

### A. Odd Sphinx tribal

- **How it wins:** Attack with Yennett, cheat a 5/7-drop Sphinx into play, then win in the air. Magister Sphinx sets a player to 10; the rest beat down.
- **A normal turn:** Scry or Brainstorm so the top card is odd. Yennett attacks (menace + flying). You free-cast Windreader Sphinx / Sphinx of Uthuun / Enigma Sphinx. Other flyers swing.
- **Support categories:** Odd-cost Sphinxes, typal cheapeners, cheap topdeck setup, Esper point removal.
- **Exemplars:** Prognostic Sphinx (attack, scry 3), Windreader Sphinx, Magister Sphinx, Enigma Sphinx (cascade; dies into the top), Herald’s Horn, Brainstorm.
- **Bracket (EDH) or role (Pauper):** Bracket 3
- **Profile fit:** Tribal + combat + value. Synergy first. Sensei’s Divining Top is the right setup card but ~$42 — flag, don’t require.

### B. Flying combat-value

- **How it wins:** Go-wide-enough in the air that Windreader Sphinx and Yennett both trigger, then chip everyone out. Inspired Sphinx makes Thopters if you need bodies.
- **A normal turn:** Several flyers attack. Windreader draws; Yennett hits an odd permanent or a cantrip. Raffine in the 99 connives the team.
- **Support categories:** Odd flyers (not only Sphinxes), anthem/draw-on-attack, unblockable for Yennett, token Sphinx/Thopter payoffs.
- **Exemplars:** Windreader Sphinx, Inspired Sphinx, Dazzling Sphinx, Raffine, Scheming Seer, Aqueous Form, Whispersilk Cloak.
- **Bracket (EDH) or role (Pauper):** Bracket 3
- **Profile fit:** Combat and tokens. Less “Sphinx-shaped” than A unless you keep the flyer slot mostly Sphinxes.

### C. Odd-cost Esper control

- **How it wins:** Answer everything with odd-MV interaction, then Yennett eventually free-casts a haymaker. Damage is a mop-up, not the plan.
- **A normal turn:** Hold up Swords / Void Rend / Swan Song. If the table is quiet, attack Yennett and hope the top is a 5-drop or a 3-mana board wipe-quality spell you actually want.
- **Support categories:** Odd removal and counters, card draw that is odd (Preordain, Read the Bones, Brainsurge), a few Sphinx finishers only.
- **Exemplars:** Swords to Plowshares, Void Rend, Anguished Unmaking, Swan Song, Generous Gift, Preordain. (Sphinx’s Revelation is MV 3 so it *looks* odd, but a free Yennett cast is X = 0 — cast it from hand with mana.)
- **Bracket (EDH) or role (Pauper):** Bracket 3
- **Profile fit:** Control and staples. Weakest Sphinx identity of the four; the 99 can slide into Esper goodstuff.

### D. Top-of-library engine

- **How it wins:** Every combat is a free spell. You do not care as much *what* the Sphinxes are, as long as the top card is always a hit. Win by accumulating free 5-drops and instants until the table can’t keep up.
- **A normal turn:** Activate Top / Opt / Prognostic Sphinx, stack an odd bomb, attack. Repeat.
- **Support categories:** Repeatable top-of-deck (Top, Opt, Consider, Herald’s Horn), odd MV density in the whole 99, protection so Yennett can attack.
- **Exemplars:** Sensei’s Divining Top (~$42), Opt, Preordain, Consider, Brainstorm, Brainsurge, Prognostic Sphinx, Herald’s Horn.
- **Bracket (EDH) or role (Pauper):** Bracket 3 (leans 4 if you add extra tutors / Game Changers)
- **Profile fit:** Value engine + spellslinger. Highest Yennett loyalty, easiest to dilute the Sphinx theme.

## Stop

Waiting for a pick. Do not write the full list yet.

**Recommendation:** **A**, or **A with a D kit** (tribal Sphinxes, but the mana base and cantrips exist to set the top). B if you want more combat. C if you want Esper control and will accept fewer Sphinxes.
