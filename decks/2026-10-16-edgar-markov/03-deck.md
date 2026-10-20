# Stage 3 — Deck

- **Name:** Markov Legion
- **Format:** commander
- **Commander / shell:** Edgar Markov
- **Mechanic:** Hybrid **A + D** — Eminence Swarm + Midrange Lords
- **Bracket (EDH) or role (Pauper):** Bracket 3
- **Game Changers (EDH):** Jeska's Will, Teferi's Protection, Demonic Tutor
- **Expensive cards to flag:** Demonic Tutor (~$67), Cavern of Souls (~$50), Roaming Throne (~$50), Teferi's Protection (~$44), Edgar Markov (~$44), Jeska's Will (~$40), Bloodletter of Aclazotz (~$35), Three Tree City (~$29), Charismatic Conqueror (~$24), Cover of Darkness (~$22), Urza's Incubator (~$21)

## Game plan

Cast cheap **Vampire** spells so **Edgar Markov** (usually still in the command zone) prints 1/1 tokens. **Shared Animosity**, **Legion Lieutenant**, **Stromkirk Captain**, **Captivating Vampire**, and **Metallic Mimic** turn the swarm sideways. **Sanctum Seeker** plus **Bloodletter of Aclazotz** drain while you attack. The midrange spine — **Bloodline Keeper**, **Edgar, Charmed Groom**, **Champion of Dusk**, **Twilight Prophet**, **Olivia Voldaren** — leaves a real board after the first wipe. Cast Edgar himself when the team is wide enough that his attack trigger ends someone.

**Kindred Dominance** is the one-sided reset. **Rising of the Day** and greaves let tokens and Edgar attack immediately. No aristocrats package, no stax, no extra-turn chains, no two-card infinites.

## Categories

Type counts match `list.txt` / `deck.cod` (100 cards, no card images).

- **Commander:** Edgar Markov (1)
- **Creatures:** 32
- **Enchantments:** 4
- **Artifacts:** 12
- **Instants:** 9
- **Sorceries:** 6
- **Lands:** 36 (3 Plains, 4 Swamp, 2 Mountain + duals / tribal lands)
- **Sideboard (Pauper):** n/a

Role notes: ramp is the rocks + **Jeska's Will**; card advantage is **Night's Whisper**, **Demonic Tutor**, **Champion of Dusk**, **Twilight Prophet**, **Welcoming Vampire**, **Dusk Legion Zealot**, **Vanquisher's Banner**, **Skullclamp**; win is go-wide combat plus **Sanctum Seeker** / **Malakir Bloodwitch**.

## Import

- **Official:** [`deck.cod`](deck.cod) (Cockatrice). Written with `python3 scripts/to_cockatrice.py decks/2026-10-16-edgar-markov/`.
- Working copy: [`list.txt`](list.txt) — Commander / Deck sections, type headers as comments, no images.

Preferred prints from `preferences/printings.json` applied to **Herald's Horn**, **Urza's Incubator**, **Swords to Plowshares**, **Toxic Deluge**, **Plains**, **Swamp**.

## Validate

`list.txt` and `deck.cod`:

```
format=commander cards=100 identity=WBR commander=Edgar Markov
WARN  expensive: Edgar Markov ($44.45); Charismatic Conqueror ($26.60); Bloodletter of Aclazotz ($35.06); Roaming Throne ($52.20); Cover of Darkness ($21.91); Urza's Incubator ($20.60); Teferi's Protection ($44.66); Jeska's Will ($39.99); Demonic Tutor ($65.39); Cavern of Souls ($50.45); Three Tree City ($28.89)
OK
```
