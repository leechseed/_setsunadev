---
title: "The genre system: how-to"
type: how-to
for: A writer who fills genre cards, contracts and load scores
does: Gives the steps for the genre system's recurring tasks
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/01_NARRATIVE_FRAMEWORKS/📐 ssot_01_genre_system.md
source_version: 1.0.1
---

**Who it's for:** a writer filling genre instruments · **What it does:** steps for cards, contracts and the load metric · **Type:** how-to

# The genre system: how-to

Terms are defined in the [reference](2-reference.md).

## Build a GENRE CARD

1. Start from Truby's fourteen genres. Use the other vocabularies as aliases.
2. Fill G1: the industry, marketing and critical labels as three fields.
3. Fill G2: the family and its polar opposite.
4. Fill G3: basic elements, criteria steps and obligatory scenes.
5. Count the required ingredients. Keep exactly three.
6. Fill G4 through G11: core binary, resolution mode, delivery modes, verisimilitude, world build, calls forth, audience ICM and market notes.
7. Add named hybrids under transcending.
8. Add an `expiry_note` if a rival vocabulary has absorbed the conventions.

## Apply the completeness rule

1. List the genre's required ingredients on the card.
2. Count them before filing.
3. If you count fewer than three, mark the card a shelf label and keep working.
4. If you count more than three, split the card.

## Write a GENRE CONTRACT for a work

1. Name the primary genre.
2. Set the mix: the overriding genre plus supporting genres, with percentages.
3. Check that the overriding genre clears its criteria in full.
4. Check that each supporting genre has substantially met its own criteria.
5. Set the delivery mode and resolution mode from the card's G5.
6. Write the register: the sensorium promise.
7. List the obligations owed.
8. Bind the contract to `storyform_id`.

## Record a mid-work mode shift

1. Find the unit where the mode changes, for example an intrusion contract turning into portal-quest.
2. Add an entry to `contract_state`.
3. Write `from_unit`, the changed field and the new value.
4. Read units before `from_unit` with the first value and later units with the new one.

## Discharge an obligation

1. Pick an obligation from the contract's obligations owed.
2. Fire it on the plot card's P10 GENRE OBLIGATION line for one unit.
3. If you withhold it, mark the breach as design.

## Score genre load for a movement

1. List the units whose P10 line is filled.
2. Score each from 0 to 3. Leave the other units blank.
3. Sum the scores and divide by the number of scored units.
4. Count the share of units scoring 2 or 3.
5. Compare both numbers to the contract's mix percentages.
6. Flag any supporting genre that never reaches 2.

## Feed G12 from the storyform

1. Look up the work's `storyform_id`.
2. Write the story point and `storyform_id` in G12.
3. Check that G12 is filled. An empty G12 leaves a shelf label.

## Key a trope to a layer

1. Open the trope register for the genre domain.
2. Find the layer that needs a known pattern in the LAYERS.md pull list.
3. Pull the trope and read its one-line definition in the register.

> **OPEN:** the source gives no steps for entering a new OXO line before phase 2. Chief strikes or keeps each parked line.
