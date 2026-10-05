---
title: "The plot system (syuzhet): how-to"
type: how-to
for: "A writer or maintainer carding a plot unit or applying a plot-system rule."
does: "Gives numbered steps for the recurring plot-system tasks."
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/04_PLOT_SYSTEMS/📐 ssot_04_plot_system.md
source_version: 1.4.0
---

**Who it's for:** a writer carding plot units · **What it does:** steps for plot-system tasks · **Type:** how-to

# The plot system (syuzhet): how-to

Field meanings are in the [reference](2-reference.md).

## Fill a PLOT CARD for a unit

1. Write the `address` shared with the scene card. Use the canonical time code, `M2 · Q1 · S03`.
2. Find the fabula event the unit tells. Copy its `event_id` into P2 and its `transition`.
3. Set P2 `driver_type` to action or decision. Add `opposition_goal`.
4. Read P3 `value` and `polarity_in` from the state-before half of the transition.
5. Write P4 as one line: the Gap, the commandment chain or the step. Read the `cause` or `enable` edge.
6. Read P5 `polarity_out` from the state-after half. Set `irony_flag` if the audience read differs.
7. Seat P6 from the trope graph's walk.
8. Fill P7 if something is learned. Set `reveal_type` and `reveal_quality`. Where 03's UNDERSIDE_SURFACING fires, take `reveal_content` and `reveal_type` from the surfaced fact.
9. Name the P8 collision row, the P10 obligation and the P11 time fields. Write `order_told` as an 08 time code.
10. Add P12 `story_point` and `storyform_id` if the unit serves the argument. At a LOAD_BEARING place, add `domain_ref`, the S12 Domain the place embodies.
11. Fill the theme record: `rail_tested` (R1 to R4), `side_argued` and `gauge` (name and step). Add the `citation` and `transcript` lines.
12. Write `fantasy:`, `sexy:` and `aesthetic:`, one line each.

## Test that a unit is plot

1. Name the value at entry and its polarity.
2. Name the value at exit.
3. If the polarity did not turn, the unit is not plot. Rework it or cut it.
4. At scene level, check all five commandments: inciting incident, complication, crisis, climax, resolution.
5. At beat level, check only the small value shift.

## Score stakes and escalation (P9)

1. Find the previous unit in the sequence.
2. If this is the first unit, set `stakes_delta: baseline` and stop.
3. Otherwise read the `cause` and `enable` chain back to the prior event.
4. Check that risk or cost trends up.
5. If the unit carries a resurrection beat, allow a repeated peak.

## Classify a reordering (P11)

1. Compare the unit's `order_told` with the fabula's `order_happened`.
2. If they match, set `anachrony.type: none`.
3. If the telling goes earlier, choose analepsis: external, internal or mixed.
4. If the telling goes later, choose prolepsis.
5. Set `duration_mode`: scene, summary, ellipsis, pause or stretch.
6. Set `frequency_mode` for the telling, not the event.
7. Name the `gap_effect`: curiosity, suspense, surprise or none.

## Set the genre obligation (P10)

1. Read the story-level genre. For OXO it is cultcore.
2. Find the unit's movement.
3. Read the scene-level obligation for that movement. For OXO: M1 Opening, M2 to M3 Institutionalized, M4 to M5 Reversal, M6 War / attrition.
4. For a new story, state its own per-movement values in its instance file.

## Declare a story's told-unit-to-act map

1. Write the map once in the story's instance file.
2. List each movement and the act it belongs to. Any count is allowed.
3. Do not borrow another story's map.
4. Let P6 and the trope graph read the seat from it.

## Stack several heroes under one manuscript (P6)

1. Give each hero's seat its own P6 line, keyed to that hero's throughline.
2. Share one `address` only where a scene intercuts them.

## Apply the hook test and the cascade recipe (P7)

1. For each logged fabula event, name one present consequence and one live hook. If you cannot, cut the event.
2. For a cascade, choose one rule that binds an institution.
3. Show a near-miss.
4. Break the rule through a personal-scale event.
5. Check that each step is an existing `cause` or `enable` edge.

## Convert an old address

1. Take the legacy form, e.g. `q1.s3`.
2. Make the q-number the sequence segment: `Q1`.
3. Zero-pad the s-number as the scene segment: `S03`.
4. Write `M2 · Q1 · S03`.
