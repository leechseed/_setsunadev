---
title: "The tracking system: how-to"
type: how-to
for: "A writer or tool builder recording story state, cables and tempo in the tracking system"
does: "Gives numbered steps for each task the tracking system defines"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/08_TRACKING_SYSTEMS/📐 ssot_08_tracking_system.md
source_version: 1.2.0
---

**Who it's for:** a writer or tool builder who knows what the grid is · **What it does:** step-by-step recipes for tracking tasks · **Type:** how-to

# The tracking system: how-to

Look up shapes in the [reference](2-reference.md). Read the [concept](1-concept.md) for the why.

## Write a time code

1. Write the movement as `M<n>` with no padding, for example `M2`.
2. Add the sequence as `Q<n>`, for example `Q1`.
3. Add the scene as `S<nn>`, zero-padded to 2 digits, for example `S04`.
4. Write ` | ` after the scene.
5. Write the bar zero-padded to 3 digits, then the beat and tick unpadded: `012.3.2`.
6. Join them: `M2 · Q1 · S04 | 012.3.2`.

## Convert a ladder address or an old date to a time code

1. Copy the movement, sequence and scene numbers: `M2.q3.s12` becomes `M2 · Q3 · S12`.
2. Drop the IP and form prefix. The track or record that holds the code names the story.
3. Write the bar half only when the fact sits inside a scene: the bar, then the beat in that bar.
4. Replace free text and movement tags such as `m1a` with the time code.
5. Leave the `backstory` tag alone. It dates events before M1.
6. Write no SC class on the code. An address is not a scale.

## Sort two time codes

1. Compare the movement numbers as numbers. `M2` sorts before `M12`.
2. If equal, compare sequence, then scene, then bar, then beat, then tick.
3. For world-clock order, ignore the told order and sort by the `Mn` dating instead.

## Date an event before the story begins

1. Use the movement tag `backstory` in place of an `Mn`.
2. Write the event id as `backstory_<slug>`.

## Record a checkpoint

1. Build the full state at the fabula event, in the shape the character state doc defines.
2. Address it with a time code.
3. Leave the checkpoint shape unchanged. This system does not alter it.

## Record a story point

1. Name a `story_point_id` slug.
2. Set `subject.kind` to character, trait, trope, place, relationship, theme, gauge, group, belief, custom, tech, wardrobe, architecture or world. Then set `subject.id`.
3. Write the `field` path and the new `value`.
4. Write `at` as a time code.
5. Add `origin_event` if the point reads from a dated fabula event.
6. Leave `ramp` false for a step. Set `ramp: true` for a continuous slope, as with tension, attraction or dread.
7. Check the 02 field-tag table. Change only a field tagged Dynamic.

## Record an iterative story point

1. Confirm the point's `frequency_mode` reads `iterative`.
2. Set `repeat_count` to how many times the change recurred.
3. Set `span` to the time-code range the repeats cover.

## Track a trope or a theme motif

1. For a trope, make a track of `kind: trope`. Use the trope's `id` as `subject.id`.
2. For a theme motif, write a story point whose `field` is `motif.<id>`.
3. Take the ids from the trope register and the theme doc. This system gives only the address.

## Track a gauge, a catalog thing or the story world

1. For a gauge, make a track of `kind: gauge` under a character or world track. Set each value to one of four steps.
2. For a catalog thing, set `kind` to group, belief, custom, tech, wardrobe or architecture. Write `subject.id` as `<kind>:<slug>`.
3. For a world-level change such as a rebrand, set `kind: world` and write `subject.id` as `world:<slug>`.

## Log a hook or a Touchstone breach

1. For a hook, write a `hook_id`, its P6 `type` and the `container` that closes on it.
2. Set `payoff_at` to the payoff's time code. Leave it unset while the hook is open.
3. For a breach, write `breach_at` as a time code and the `touchstone_id` as a TS id.
4. List every downstream time code that trusted the breached unit in `invalidated_units`.

## Link a setup to its payoff with a cable

1. Name a `cable_id` slug and set `type: setup_payoff`.
2. Write the setup's `track` and `at`.
3. Write the payoff's `track` and `at`.
4. Set `edge: enable`.
5. Set `orphan: none` when both ends are logged.
6. Set `orphan` to `setup_no_payoff` or `payoff_no_setup` when one end is missing.
7. Set `orphan: provisional` when both ends exist narratively but a time code is still unset.
8. Replace `provisional` with `none` once you supply the real time code.

## Set a tempo point

1. Write `at` as a time code.
2. Set `story_bpm` to beats per unit of world time.
3. Set `audience_bpm` to beats per 1,000 words for prose, or per minute for screen.
4. Set `ramp: true` for a slope to the next point, or false for a step.

## Change a scene's meter

1. Write a `meter_marker` with `at` set to a time code.
2. Set `beats_per_bar`, for example 4, 3 or 7.
3. Know the marker holds until the next one. The default is 4/4.

## Plan and measure proportion

1. Set `span` to `act` or `third`.
2. Set `planned_share`. The default plan is 25/50/25.
3. The tool fills `measured_share` from P1 percentage addresses.
4. Read the drift between plan and draft.

## Score reversibility on stakes

1. Open the P9 `stakes_delta` field.
2. Add `reversibility`, a number from 1 to 10.
3. Run the "trend up" test on the numbers.

## Add a reader entry

1. Name a `reader_entry_id` slug and the `character_id`.
2. Write `belief`, what the reader believes about the character.
3. Set `trust` from 0 to 10.
4. Set `shifted_at` to the time code of the scene where it shifted.
5. Set `disclosure` to `concealed` while the story still hides the truth.
6. At the reveal scene, write a new entry with `disclosure: revealed` and a lower `trust`.
7. Optionally run a cable from the planting scene to the overturning scene.
