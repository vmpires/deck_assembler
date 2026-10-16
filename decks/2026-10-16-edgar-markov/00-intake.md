# Stage 0 — Intake

- **Idea:** Build a new **Edgar Markov** Vampire tribal Commander deck from scratch.
- **Format:** commander
- **Bracket / power target:** **Bracket 3 (Upgraded)** — default unless asked to go tuned/high (Bracket 4). Never cEDH.
- **Colors / identity:** Mardu (**B/R/W**) — **Edgar Markov**
- **Refusal / keep:** No stax/prison/MLD/extra-turn chains. No chaos. Aristocrats/graveyard only if that plan is chosen at the mechanics gate (it is not the profile default).

## Commander (confirmed)

```
Edgar Markov
  type: Legendary Creature — Vampire Knight
  mana: {3}{R}{W}{B}
  identity: BRW
  legal: commander=legal
  usd: 44.22
  oracle: Eminence — Whenever you cast another Vampire spell, if Edgar is in the
           command zone or on the battlefield, create a 1/1 black Vampire
           creature token.
           First strike, haste
           Whenever Edgar attacks, put a +1/+1 counter on each Vampire you control.
```

Source: `python3 scripts/scryfall.py card "Edgar Markov"`

## Profile read

Edgar is a strong match: **combat**, **tokens**, and **tribal**. The eminence engine wants a high density of Vampire spells, not Mardu goodstuff. Attack-trigger value and go-wide anthems both serve the commander. Drain/sacrifice is a real Vampire lane but is a **deliberate pick**, not the default.

## Gate status

| Stage | Status |
| --- | --- |
| Commanders | **Skipped** — commander locked: **Edgar Markov** |
| Mechanics | **Picked** — hybrid **A + D** |
| Full list | In progress |
