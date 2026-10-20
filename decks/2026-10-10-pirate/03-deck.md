# Stage 3 — Deck

- **Name:** Brass Treasure Crew
- **Format:** commander
- **Commander / shell:** Admiral Beckett Brass
- **Mechanic:** Plan B, Treasure crew, with a Plan C lane package so three Pirates can connect.
- **Bracket (EDH) or role (Pauper):** High Bracket 3 (3 Game Changers, the cap)
- **Game Changers (EDH):** Jeska's Will, Demonic Tutor, Cyclonic Rift
- **Expensive cards to flag:** Demonic Tutor (~$69), Cavern of Souls (~$51), Jeska's Will (~$41), Cyclonic Rift (~$39), Scalding Tarn (~$37), Morphic Pool (~$30), Cover of Darkness (~$22), Urza's Incubator (~$20). Xorn (~$14), Mystic Remora (~$15), and Training Center (~$18) sit just under $20.

## Game plan

Play Pirates, attack, and turn the attack into mana. Malcolm, Keen-Eyed Navigator makes a Treasure for each opponent dealt damage. Captain Lannery Storm makes one when she attacks. Gemcutter Buccaneer makes a tapped Treasure whenever a Pirate enters, and those Treasures equip a Pirate for {1} and give +2/+0. Captain Storm, Cosmium Raider puts a +1/+1 counter on a Pirate whenever an artifact enters. Xorn adds one extra Treasure each time you make any. Professional Face-Breaker makes a Treasure on combat damage and lets you sacrifice one to play the top of your library. Spend that mana on another Pirate, Deadly Dispute, Big Score, or interaction. Herald's Horn and Urza's Incubator (choose Pirate) make the crew cheaper. Thought Vessel keeps the hand open when Kindred Discovery draws.

The lane package is what turns Brass on. Cover of Darkness names Pirate and gives them fear. Storm Fleet Sprinter cannot be blocked. Departed Deckhand and Changeling Outcast get through, and the Deckhand can hand that restriction to another creature. Breeches, Eager Pillager blanks one blocker. Warkite Marauder turns one defender into a 0/1. Kitesail Larcenist turns one artifact or creature each player controls into a Treasure. Dreamcaller Siren taps two nonland permanents if you control another Pirate. Rogue's Passage makes one creature unblockable. Cyclonic Rift bounces their board. Coercive Recruiter steals a creature until end of turn when a Pirate enters, and that creature becomes a Pirate with haste, so it can be the third body. At your end step, if three or more Pirates hit the same player, Brass takes a nonland permanent they control, and the steal stays.

The clock is combat. Corsair Captain and Dire Fleet Neckbreaker pump the crew. Shared Animosity grows with the number of attacking Pirates. Port Razer untaps your creatures and adds a combat when it connects, and it cannot attack a player it has already attacked this turn. Forerunner of the Coalition drains each opponent for 1 whenever another Pirate enters.

Ragavan, Nimble Pilferer is the one-mana upgrade for Reckless Lackey, and it is about $41. Pitiless Plunderer and Timestream Navigator stay out.

## Categories

Counts match `list.txt` / `deck.cod` (100 cards, 35 lands).

- **Commander:** Admiral Beckett Brass (1)
- **Ramp / mana:** Sol Ring, Arcane Signet, Talisman of Dominance, Talisman of Indulgence, Talisman of Creativity, Thought Vessel, Herald's Horn, Urza's Incubator, Dark Ritual, Jeska's Will, Strike It Rich (11)
- **Card advantage:** Demonic Tutor, Coastal Piracy, Reconnaissance Mission, Kindred Discovery, Night's Whisper, Mystic Remora, Big Score, Deadly Dispute (8). Francisco, Fowl Marauder explores. Ramirez DePietro, Pillager exiles a card you may cast later. Professional Face-Breaker impulses. Spectral Sailor draws for {3}{U}.
- **Interaction:** Counterspell, Lookout's Dispersal, Negate, An Offer You Can't Refuse, Drown in the Loch, Go for the Throat, Feed the Swarm, Terminate, Chaos Warp, Bitter Triumph, Toxic Deluge, Cyclonic Rift, Lightning Greaves, Swiftfoot Boots (14). Kitesail Freebooter exiles a noncreature card from a hand. Siren Stormtamer sacrifices itself to counter a spell that targets you or a creature you control.
- **Engine / synergy:** Malcolm, Keen-Eyed Navigator, Captain Lannery Storm, Gemcutter Buccaneer, Captain Storm, Cosmium Raider, Corsair Captain, Professional Face-Breaker, Ramirez DePietro, Pillager, Reckless Lackey, Xorn, Storm Fleet Sprinter, Departed Deckhand, Changeling Outcast, Breeches, Eager Pillager, Kitesail Larcenist, Warkite Marauder, Fathom Fleet Captain, Dreamcaller Siren, Dire Fleet Neckbreaker, Siren Stormtamer, Spectral Sailor, Spyglass Siren, Francisco, Fowl Marauder, Broadside Bombardiers, Forerunner of the Coalition, Kitesail Freebooter, Metallic Mimic, Coercive Recruiter, Dire Fleet Poisoner, Cover of Darkness (29). Metallic Mimic and the tribal lands choose Pirate. Changeling Outcast is every creature type. Professional Face-Breaker and Xorn are not Pirates.
- **Win conditions:** Shared Animosity, Port Razer (2). Combat with the anthem and the Treasures-as-Equipment is the clock. Brass's end step is the steal.
- **Lands:** 35 (4 Island, 3 Swamp, 2 Mountain, Command Tower, Path of Ancestry, Exotic Orchard, Unclaimed Territory, Secluded Courtyard, Cavern of Souls, Rogue's Passage, Watery Grave, Blood Crypt, Steam Vents, Morphic Pool, Luxury Suite, Training Center, Drowned Catacomb, Dragonskull Summit, Sulfur Falls, Shipwreck Marsh, Haunted Ridge, Stormcarved Coast, Clearwater Pathway, Blightstep Pathway, Riverglide Pathway, Polluted Delta, Bloodstained Mire, Scalding Tarn, Creeping Tar Pit)
- **Sideboard (Pauper):** n/a

## Official artifact

[`deck.cod`](deck.cod) — Cockatrice XML from `python3 scripts/to_cockatrice.py decks/2026-10-10-pirate/`.

## Validate

```
format=commander cards=100 identity=UBR commander=Admiral Beckett Brass
WARN  expensive: Urza's Incubator ($20.17); Jeska's Will ($41.15); Demonic Tutor ($69.47); Cyclonic Rift ($39.16); Cover of Darkness ($21.67); Cavern of Souls ($51.06); Morphic Pool ($29.54); Scalding Tarn ($36.86)
OK
```

`deck.cod` validate: same **OK** output.
