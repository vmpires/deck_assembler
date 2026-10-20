# Stage 1 — Commanders / shells

- **Idea:** Zombie tribal. Lords, a Zombie board, and a commander that pays that board off.
- **Format:** commander
- **Bracket / role target:** high Bracket 3 / low Bracket 4
- **Colors / identity (if known):** open
- **Scryfall queries used:**
  - `is:commander legal:commander (t:zombie OR o:"Zombie creatures" OR o:"other Zombies" OR o:"Zombie spells" OR o:"nontoken Zombie")` ordered by edhrec
  - `is:commander legal:commander (o:"Zombie you control" OR o:"other Zombie" OR o:"Zombies you control" OR o:"Zombie creature" OR o:"Zombie spells" OR o:"with one or more Zombies" OR o:"attack with one or more Zombies")` ordered by edhrec
  - `card` checks: Wilhelt, the Rotcleaver; Varina, Lich Queen; The Scarab God; Zul Ashur, Lich Lord; Temmet, Naktamun's Will; Gisa, the Hellraiser

Left off the shortlist: **Temmet, Naktamun's Will** (same Esper attack-and-draw shape as Varina; the payoff is a temporary anthem). **Zul Ashur, Lich Lord** and **Gisa and Geralf** (cast Zombies from the graveyard; that is a recursion deck). **Gisa, the Hellraiser** (the anthem is real, but the tokens come from committing crimes). **Hashaton, Scarab's Fist** (discard a creature, pay `{2}{U}`, make a 4/4 Zombie copy; that is reanimator tokens). **Sidisi, Brood Tyrant** (self-mill).

## Options

### 1. Wilhelt, the Rotcleaver

- **Identity / colors:** UB
- **Why it fits the pitch:** He is a Zombie. Whenever another Zombie you control dies, if it did not have decayed, you create a 2/2 black Zombie token with decayed. At the beginning of your end step you may sacrifice a Zombie to draw a card. Deaths become bodies, and a body becomes a card.
- **Likely plans:** Zombie lords and a wide board. Trade or sacrifice nontoken Zombies, keep the decayed tokens, and draw every turn. Decayed tokens cannot block, and they die after they attack, so the second wave is expendable.
- **Bracket (EDH) or role (Pauper):** High Bracket 3 / low Bracket 4. Three mana, two colors, and a draw engine in the command zone. About $9.
- **Risk:** Decayed tokens are bad at blocking, so a board of them folds to a real attack. The famous loops (a free Zombie plus a sacrifice outlet) are a different deck. This shortlist is the tribal one.
- **Skip if:** you want the Zombies to stay on the board and attack as a real army.

### 2. Varina, Lich Queen

- **Identity / colors:** WUB
- **Why it fits the pitch:** She is a Zombie. Whenever you attack with one or more Zombies, you draw that many cards, discard that many cards, and gain that much life. `{2}`, exile two cards from your graveyard: create a tapped 2/2 black Zombie token. White adds lords and removal the Dimir lists do not have.
- **Likely plans:** Attack with several Zombies every turn. The loot finds lords and fills the graveyard; the activated ability turns that graveyard into more attackers. Life gain is a cushion while the board grows.
- **Bracket (EDH) or role (Pauper):** High Bracket 3 / low Bracket 4. Three mana. The card flow is as large as the attack, so a developed board keeps the hand full. About $4.
- **Risk:** The draw and the discard are the same number. A wide attack with nothing you want to throw away empties your hand. Three colors want a real mana base. The token ability exiles cards, so this is not a reanimator deck.
- **Skip if:** you want two colors, or you want the graveyard to stay intact for recursion.

### 3. The Scarab God

- **Identity / colors:** UB
- **Why it fits the pitch:** At the beginning of your upkeep, each opponent loses life and you scry, both equal to the number of Zombies you control. `{2}{U}{B}`: exile a creature card from a graveyard and create a token copy of it that is a 4/4 black Zombie. When he dies, he returns to your hand at the beginning of the next end step.
- **Likely plans:** Play Zombies so the upkeep is a clock and a scry. Spend the activated ability on your own Zombie lords and on the best creature in any graveyard, and every copy is another Zombie for the drain. Removal does not stick.
- **Bracket (EDH) or role (Pauper):** High Bracket 3. Five mana, so slower than Wilhelt or Varina. The drain wins if the Zombie count stays high. About $5.
- **Risk:** He is a God, not a Zombie, so Zombie lords do not buff him. The activated ability costs four mana on top of that. The deck can drift into "copy their creatures" and stop being a tribe.
- **Skip if:** you want the commander to be a Zombie in the army, or you want to win by attacking.

## Stop

Locked: **Wilhelt, the Rotcleaver**. Mechanics are in `02-mechanics.md`.
