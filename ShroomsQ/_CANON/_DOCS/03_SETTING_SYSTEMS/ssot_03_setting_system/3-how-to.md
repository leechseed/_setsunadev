---
title: "The setting system: how-to"
type: how-to
for: "A writer building or editing a place record in the setting system."
does: "Gives numbered steps for the recurring setting-system tasks."
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/03_SETTING_SYSTEMS/📐 ssot_03_setting_system.md
source_version: 1.11.1
---

**Who it's for:** a writer building or editing a place · **What it does:** steps for the setting system's tasks · **Type:** how-to

# The setting system: how-to

Field definitions are in the [reference](2-reference.md).

## Start a new place slice

1. Write the slice header: `place_id`, names and aliases, scale class, parent and child places.
2. Add `job`, `dramatic role` and `adjacent` (neighbors listed by travel cost).
3. Tag each fact with a `canon_tier`: core, semi or fringe.
4. Stop. A header alone is a complete slice for a mere location.
5. Fill a layer only when a scene's pressure needs it.

## Fill a layer when a scene needs it

1. Name the scene and the pressure it needs.
2. Pick the layer that carries that pressure.
3. Cold start? Fill in this order: S1, S2, S6, S4, S8, S7.
4. Mark each detail explicit, implicit or gap. Leave gaps as gaps.
5. Close the layer on one character it touches. A layer that traces to nothing is scenery.

## Run the derivation check

1. Give every settlement or fortress a reason: water, food, resource, route or choke point.
2. Trace every S6 resource or trade good to an S1 feature or an S4 rule.
3. Give every invented rule a cost and a limit.
4. If the place rests on one premise, write one line per filled layer on what the premise changes.

## Bind a place to the story (S12)

1. Confirm the place embodies a throughline Domain.
2. Create an S12 record keyed by `storyform_id`.
3. Add `contradiction`, `salient surplus` and the `touchstone` set.
4. Add `link` if a ruler or protagonist is tied to the place.
5. Put in only what a scene has narrated.
6. Know that P12 `domain_ref` reads this Domain for each plot unit set at the place.

## Pin a scene with the SCENE CARD

1. Write the ladder address and the setting with its state.
2. List the active strata and one or two function modes.
3. Add up to three sensorium details, the `governing detail` first.
4. Write the commandments, the value turn and the collision row.
5. Write the exit state. It feeds the next card.
6. If the scene crosses a seam, fill `crossing` and note which rules change.
7. Fill the theme record: `rail_tested` (R1 to R4), `side_argued` and `gauge` (name and step), beside `citation` and `transcript`.
8. Name `focal`: one character id.
9. Answer `fantasy`, `sexy` and `aesthetic` in one breath each.

## Pin a run of scenes with the SEQUENCE CARD

1. Write the address and the sequence question.
2. List the scene-slots.
3. Write one rolled-up value turn for the whole run.
4. Read Coyne's five commandments across all slots, one line each.
5. Write threads and the exit state.
6. Give a slot its own SCENE CARD only if its pressure earns one.

## Build a FACTION / NATION CARD

1. Write the founding sentence, binding principle and one secret.
2. Decide: does the story center this faction? If not, stop at the stub.
3. For a full card, add government, economy tier and border/seam rating.
4. Add `goal` and a `clock` of 4 to 8 ticks.
5. Add `quotable wound`, `claimed vs rewarded`, the folk tier, `fault line` and `drift`.

## Run the Polder test on an enclosed place

1. Name the ring (S1) and what it is made of.
2. Name the keepers (S4) and their right.
3. Name the flood (S11) and record it as a threat clock.
4. Name the inside law (S4).

## Read the setting flags

1. Open the place record after any state diff.
2. Check each flag's trigger against the named fields.
3. Act on each active flag as its signal says. For example, add the cause for RUIN_INERT, or cut the entry.
4. Hand off two flags. UNDERSIDE_SURFACING gives the plot card P7 `reveal_content` and `reveal_type`. LEDGER_DUE gives the fabula event `scheduled:` the future state's 08 time code.
5. Add a story-specific flag to the instance file if the story needs one.

## Handle a contradiction in canon

1. Decide where it sits: main storyline or background mechanics.
2. A main-storyline contradiction is fatal. Fix it.
3. Log a background contradiction. Keep fringe material and never delete it.
4. Give the continuity record to one custodian.
