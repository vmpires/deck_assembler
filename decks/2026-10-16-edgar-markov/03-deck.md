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

Counts match `list.txt` / `deck.cod` (100 cards, 36 lands).

- **Commander:** Edgar Markov (1)
- **Ramp / mana:** Sol Ring, Arcane Signet, Talisman of Hierarchy, Talisman of Conviction, Talisman of Indulgence, Fellwar Stone, Jeska's Will (7)
- **Card advantage:** Night's Whisper, Demonic Tutor, Champion of Dusk, Twilight Prophet, Welcoming Vampire, Dusk Legion Zealot, Vanquisher's Banner, Skullclamp (8)
- **Interaction:** Swords to Plowshares, Path to Exile, Anguished Unmaking, Terminate, Fracture, Generous Gift, Toxic Deluge, Damn, Kindred Dominance (9)
- **Engine / synergy:** remaining Vampires (including lords, **Mavren Fein**, **Drana**, **Roaming Throne**, **Cover of Darkness**, **Herald's Horn**, **Urza's Incubator**, **Legion's Landing**, **Metallic Mimic**, **Shared Animosity**, **Mirror Entity**) (33)
- **Protection / combat:** Teferi's Protection, Akroma's Will, Boros Charm, Lightning Greaves, Swiftfoot Boots, Rising of the Day (6)
- **Win conditions:** go-wide combat (Shared Animosity / anthems / Edgar attack), Sanctum Seeker drain, Malakir Bloodwitch ETB
- **Lands:** 36 (3 Plains, 4 Swamp, 2 Mountain, shocks, checks, pains, fast lands, tribal lands, **Cavern of Souls**, **Three Tree City**, **Bloodstained Mire**)
- **Sideboard (Pauper):** n/a

## Official artifact

[`deck.cod`](deck.cod) — Cockatrice XML from `python3 scripts/to_cockatrice.py decks/2026-10-16-edgar-markov/`. Preferred prints from `preferences/printings.json` applied to **Herald's Horn**, **Urza's Incubator**, **Swords to Plowshares**, **Toxic Deluge**, **Plains**, **Swamp**.

## Validate

`list.txt`:

```
format=commander cards=100 identity=WBR commander=Edgar Markov
WARN  expensive: Edgar Markov ($44.22); Charismatic Conqueror ($24.39); Bloodletter of Aclazotz ($35.08); Urza's Incubator ($20.59); Cover of Darkness ($22.08); Roaming Throne ($49.89); Jeska's Will ($40.03); Demonic Tutor ($66.93); Teferi's Protection ($44.02); Cavern of Souls ($50.45); Three Tree City ($28.55)
OK
```

`deck.cod`: same **OK** output.
