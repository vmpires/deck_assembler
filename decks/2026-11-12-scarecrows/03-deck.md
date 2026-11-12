# Stage 3 — Deck

- **Name:** Reaper King blink
- **Format:** commander
- **Commander / shell:** Reaper King
- **Mechanic:** Blink ETB control — every Scarecrow (or changeling) that enters destroys a permanent; blink it and do it again
- **Bracket (EDH) or role (Pauper):** high Bracket 3 / low Bracket 4
- **Game Changers (EDH):** Cyclonic Rift; Demonic Tutor; Fierce Guardianship (3)
- **Expensive cards to flag:** Demonic Tutor ($66.47); Fierce Guardianship ($65.16); Preston, the Vanisher ($62.89); Esper Sentinel ($54.71); Painter's Servant ($48.81); Cavern of Souls ($48.57); Boseiju, Who Endures ($44.74); Urza's Saga ($39.98); Cyclonic Rift ($38.41); Scalding Tarn ($35.84); Misty Rainforest ($35.79); Mana Confluence ($33.91); Verdant Catacombs ($30.05); Otawara, Soaring City ($28.77); Three Tree City ($28.54); Elesh Norn, Mother of Machines ($26.74); Thassa, Deep-Dwelling ($24.85); Delighted Halfling ($20.65); Zagoth Triome ($20.64)

## Game plan

Reaper King is a removal engine, not a lord tribal. A Scarecrow or changeling entering with the King in play destroys a permanent. Blink that body (`Ephemerate`, `Ghostly Flicker`, `Conjurer's Closet`, `Thassa, Deep-Dwelling`, `Soulherder`, `Deadeye Navigator` at `{1}{U}`) and destroy another. `Panharmonicon` and `Elesh Norn, Mother of Machines` double the trigger. `Preston, the Vanisher` turns each blink into an extra 0/1 Scarecrow copy, which is another kill. `Spark Double` copies the King so every ETB fires twice. `Maskwood Nexus` / `Arcane Adaptation` make the blink creatures themselves into Scarecrows. Once the table is stripped, `Mirror Entity` and the King's anthem close in combat. `Deadeye` is a grind, not an infinite — no mana combo in the list.

Normal game: rocks and green land ramp into King as WUBRG. Dump cheap ammo (`Heap Doll`, `Changeling Outcast`, `Universal Automaton`). Protect him (`Lightning Greaves`, `Fierce Guardianship`, `Heroic Intervention`). End steps blink; opponents' turns snipe with Deadeye or Displacer. `Scarecrone` recasts artifact creatures from the yard.

## Categories

Counts should match `deck.cod` / `list.txt`.

- **Commander:** Reaper King (1)
- **Ramp / mana:** Sol Ring, Arcane Signet, Fellwar Stone, Chromatic Lantern, Birds of Paradise, Delighted Halfling, Nature's Lore, Three Visits, Farseek (9)
- **Card advantage:** Esper Sentinel, Mystic Remora, Skullclamp, Guardian Project, Kindred Discovery, Demonic Tutor, Fabricate, Eladamri's Call (8)
- **Interaction:** Swords to Plowshares, Assassin's Trophy, Beast Within, Chaos Warp, Swan Song, An Offer You Can't Refuse, Fierce Guardianship, Cyclonic Rift, Heroic Intervention, Lightning Greaves (10)
- **Engine / synergy:** blink 13 (Ephemerate, Cloudshift, Ghostly Flicker, Eerie Interlude, Conjurer's Closet, Teleportation Circle, Thassa, Deep-Dwelling, Soulherder, Deadeye Navigator, Restoration Angel, Eldrazi Displacer, Yorion, Sky Nomad, Panharmonicon); copy/double 3 (Elesh Norn, Mother of Machines, Preston, the Vanisher, Spark Double); scarecrows 10 (Scarecrone, Wreckage Wickerfolk, Foraging Wickermaw, Heap Doll, Painter's Servant, Scuttlemutt, Wingrattle Scarecrow, The Reaper, King No More, Wild-Field Scarecrow, Dread Tiller); changelings 8 (Changeling Outcast, Universal Automaton, Mirror Entity, Realmwalker, Unsettled Mariner, Masked Vandal, Chomping Changeling, Bloodline Pretender); type-change 2 (Maskwood Nexus, Arcane Adaptation) (36)
- **Win conditions:** repeated Reaper King destroys until nothing is left; Mirror Entity / anthem combat; Preston copies and Spark Double as extra triggers
- **Lands:** 36
- **Sideboard (Pauper):** n/a

1+9+8+10+36+36 = 100.

## Import

- **Official:** `deck.cod` in the session folder (Cockatrice). Write it with `python3 scripts/to_cockatrice.py decks/<session>/`.
- Working copy: `list.txt` (Moxfield / Archidekt / validate). Commander: 100 × `1 Card Name` (commander first). Pauper: 60 main, then `Sideboard`, then up to 15.

## Validate

```
python3 scripts/scryfall.py validate decks/2026-11-12-scarecrows/list.txt --format commander --commander "Reaper King"
format=commander cards=100 identity=WUBRG commander=Reaper King
WARN  expensive: Boseiju, Who Endures ($44.74); Cavern of Souls ($48.57); Cyclonic Rift ($38.41); Delighted Halfling ($20.65); Demonic Tutor ($66.47); Elesh Norn, Mother of Machines ($26.74); Esper Sentinel ($54.71); Fierce Guardianship ($65.16); Mana Confluence ($33.91); Misty Rainforest ($35.79); Otawara, Soaring City ($28.77); Painter's Servant ($48.81); Preston, the Vanisher ($62.89); Scalding Tarn ($35.84); Thassa, Deep-Dwelling ($24.85); Three Tree City ($28.54); Urza's Saga ($39.98); Verdant Catacombs ($30.05); Zagoth Triome ($20.64)
OK

python3 scripts/scryfall.py validate decks/2026-11-12-scarecrows/deck.cod --format commander --commander "Reaper King"
format=commander cards=100 identity=WUBRG commander=Reaper King
WARN  expensive: Boseiju, Who Endures ($44.74); Cavern of Souls ($48.57); Cyclonic Rift ($38.41); Delighted Halfling ($20.65); Demonic Tutor ($66.47); Elesh Norn, Mother of Machines ($26.74); Esper Sentinel ($54.71); Fierce Guardianship ($65.16); Mana Confluence ($33.91); Misty Rainforest ($35.79); Otawara, Soaring City ($28.77); Painter's Servant ($48.81); Preston, the Vanisher ($62.89); Scalding Tarn ($35.84); Thassa, Deep-Dwelling ($24.85); Three Tree City ($28.54); Urza's Saga ($39.98); Verdant Catacombs ($30.05); Zagoth Triome ($20.64)
OK
```

`deck.cod` exists. No errors.
