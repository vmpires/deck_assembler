# Stage 1 — Commanders / shells

- **Idea:** Spider tribal with reach creatures and toughness greater than power
- **Format:** commander
- **Bracket / role target:** Bracket 3 (Upgraded)
- **Colors / identity (if known):** Green-centered; black and white optional
- **Scryfall queries used:**
  - `is:commander t:spider f:commander` (51; most are Marvel Spider-Heroes)
  - `t:spider f:commander unique:cards -t:hero` (93 in-universe spiders)
  - `t:spider f:commander unique:cards -t:hero id<=g` (70)
  - `t:spider f:commander unique:cards -t:hero id<=bg` (83)
  - `t:spider f:commander unique:cards -t:hero id<=wbg` (85)
  - `t:spider tou>pow f:commander unique:cards -t:hero` (61)
  - `kw:reach tou>pow f:commander unique:cards id<=wbg` (155)
  - `is:commander o:spider -t:spider f:commander`
  - `is:commander o:"assigns combat damage" f:commander`

Skipped on profile: **Thantis, the Warweaver** (all creatures attack if able — politics/chaos). **Shelob, Dread Weaver** (exile-and-steal reanimator, not spider tribal).

## Options

Rank 5–8. For Pauper, these are archetype shells, not commanders.

### 1. Shelob, Child of Ungoliant

- **Identity / colors:** BG
- **Why it fits the pitch:** Spider lord: other Spiders get deathtouch and ward {2}. Reachers with low power become lethal blockers *and* attackers. Spider combat kills become Food copies of the dead creature.
- **Likely plans:** Spider tribal combat, deathtouch board, incremental copy-value. 83 non-Hero spiders in identity.
- **Bracket (EDH) or role (Pauper):** Bracket 3
- **Risk:** Six mana; the Food copies lose creature types, so they do not grow the spider count. Table will kill Shelob on sight.
- **Skip if:** you want toughness-as-damage more than “spiders are lethal.”

### 2. Felothar the Steadfast

- **Identity / colors:** WBG
- **Why it fits the pitch:** Your creatures deal damage equal to toughness, and defenders can attack. 1/2 reach spiders and high-toughness walls actually hit. Abzan adds white walls without helping opponents (unlike Doran). Felothar is a 0/5.
- **Likely plans:** Toughness combat, spiders + reach walls, sac-a-fatty-to-draw. 85 non-Hero spiders plus 155 reach `tou>pow` bodies.
- **Bracket (EDH) or role (Pauper):** Bracket 3
- **Risk:** The commander is the whole combat math. Without Felothar, the team is mostly blockers. Three-color mana.
- **Skip if:** you want a spider in the command zone, not a treefolk-shaped warrior.

### 3. Ishkanah, Grafwidow

- **Identity / colors:** BG
- **Why it fits the pitch:** A 3/5 reach spider. Delirium ETB makes three 1/2 reach Spiders (toughness > power). Activated drain scales with spider count.
- **Likely plans:** Typal tokens, light delirium (not a graveyard deck), drain finish.
- **Bracket (EDH) or role (Pauper):** Bracket 3
- **Risk:** Five mana and a one-shot token burst unless you recast her. Drain is {6}{B}. Delirium is extra setup.
- **Skip if:** you want a continuous engine more than a burst-and-drain spider.

### 4. Arasta of the Endless Web

- **Identity / colors:** G
- **Why it fits the pitch:** She *is* the pitch on one card: 3/5 reach spider that makes 1/2 reach Spiders whenever an opponent casts an instant or sorcery. Mono-green, cheap, 70 non-Hero spiders.
- **Likely plans:** Token factory, spider typal, overrun/anthem finish (Wall Crawl, Arachnogenesis, Twin-Silk Spider). Punishes interaction.
- **Bracket (EDH) or role (Pauper):** Bracket 3
- **Risk:** The tokens do not win combat without lords or overrun. No black removal or deathtouch lord, no white toughness-as-damage. Creature-heavy tables feed her less. Enchantment-creature dies to both creature and enchantment removal.
- **Skip if:** you want a built-in win condition in the command zone (Shelob’s deathtouch, Felothar’s toughness math, Ishkanah’s drain).

### 5. Blex, Vexing Pest

- **Identity / colors:** BG
- **Why it fits the pitch:** Lord for Spiders (and pests, insects, snakes, bats). Adventure half is card selection. Cheap commander.
- **Likely plans:** Creepy-crawly typal, anthem combat. Spiders as the main creature type.
- **Bracket (EDH) or role (Pauper):** Bracket 3
- **Risk:** Not a spider himself. No token engine and no toughness payoff. The 99 has to do all the work.
- **Skip if:** the commander should be a spider or a toughness switch.

### 6. Doran, the Siege Tower

- **Identity / colors:** WBG
- **Why it fits the pitch:** Classic “toughness is power.” Same Abzan spider + wall team as Felothar. Doran is a 0/5 (~$9).
- **Likely plans:** Toughness combat, reachers and walls.
- **Bracket (EDH) or role (Pauper):** Bracket 3
- **Risk:** *Every* creature assigns damage with toughness, including opponents. Strictly worse at that job than Felothar for this table.
- **Skip if:** Felothar is available — take Felothar.

### 7. The Swarmweaver

- **Identity / colors:** BG
- **Why it fits the pitch:** Delirium: Insects and Spiders get +1/+1 and deathtouch. Makes two Insect tokens on ETB.
- **Likely plans:** Insect/spider mix, light delirium, deathtouch combat.
- **Bracket (EDH) or role (Pauper):** Bracket 3
- **Risk:** Wants insects as much as spiders. Delirium is setup. Weaker Shelob.
- **Skip if:** you want spiders only, not a bug pile.

### 8. Cosmic Spider-Man

- **Identity / colors:** WUBRG
- **Why it fits the pitch:** Five-color Spider lord: other Spiders gain flying, first strike, trample, lifelink, and haste. Lets you run every spider.
- **Likely plans:** Marvel Spider-Hero aggro, 5c goodstuff with a spider sticker.
- **Bracket (EDH) or role (Pauper):** Bracket 3 (mana base is the tax)
- **Risk:** Universes Beyond. The 99 will look like Spider-Man, not webs and 1/2 reachers. Five colors.
- **Skip if:** the pitch is in-universe spiders, which it is.

## Stop

Waiting for a pick. Do not write mechanics or a list yet.

**Recommendation:** Shelob if the 99 should be Spiders; Felothar if the 99 should be high-toughness reachers that actually hit. Arasta if you want the cleanest token engine and are fine putting the win in the 99.
