---
title: "Character state architecture: tutorial"
type: tutorial
for: A new narrative designer learning state diffs by writing one
does: Walks the Victoria Midnight post-crash state, from the event to the assembled character
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/02_CHARACTER_SYSTEMS/🔮ssot_02_character_state_architecture.md
source_version: 1.3.0
---

**Who it's for:** a new narrative designer · **What it does:** one state diff built from the source's own example · **Type:** tutorial

# Tutorial: write the post-crash state for Victoria Midnight

You will build the `vm_m1b_post_crash` state from the source's example. Every value comes from the source. Field definitions are in the [reference](2-reference.md).

## Step 1: Name the event and the state

The crash kills Jebb and Victoria survives. Write the identity fields.

- `character_id`: `victoria_midnight`
- `state_id`: `vm_m1b_post_crash`
- `origin_event`: `m1b_crash_jebb_death`
- `movement`: `m1b`
- `state_version`: `1.0`
- `base_record_version`: `1.0.0`

## Step 2: Fix the distances

Victoria is the origin of the time grid. Write `mc_distance_temporal` as `0`. The system computes it. Write `mc_distance_narrative` as `0`. You author it.

> **OPEN:** the source gives no `told_at` value for this state. The example `["M2 · Q1 · S04 | 012.3.2"]` shows the shape only. Fill it from the tracking system.

## Step 3: Write the modified values

Write only what changed. Each comment names the old value.

```
state_diffs:
  MODIFIED_VALUES:
    WOUND: 8
    DRIVE: 12
    WILL_EFFECTIVE: 13
    L8_IMPRINT:
      secure_base_object: brother_deceased
      attachment_style_score: 6
    L10_SHADOW:
      shadow_density: 7
      shadow_content:
        - culpability_for_brother
        - distrust_of_own_judgment
```

WOUND went from 4 to 8. DRIVE went from 14 to 12. Base WILL is 14, so the reduction to 13 is `WILL_EFFECTIVE`, a state-only field.

## Step 4: Recompute the derived statistics

Use the modified values. List only what changed.

```
  MODIFIED_DERIVED:
    basic_damage_resistance: 10
    stress_threshold: 5
    collapse_risk: 6
```

The source shows the arithmetic: 13 - (8/2) for damage resistance, 13 - 8 for stress threshold, (8 + 4) / 2 for collapse risk. `stress_threshold` uses `WILL_EFFECTIVE` here.

## Step 5: Re-evaluate the flags

Rule 4 makes this mandatory. Three flags change.

```
  MODIFIED_FLAGS:
    KINSHIP_COLLAPSE: FIRED
    SHADOW_DENIAL: ACTIVE
    TRUTH_VULNERABILITY: ACTIVE
```

## Step 6: Write the note

Add 2-5 sentences. The source's note says the wound is not grief. It is the knowledge that she chose not to listen. WOUND jumps from 4 to 8. SHADOW gains culpability and self-doubt. KINSHIP_COLLAPSE fires. All later behavior runs without a secure attachment base.

## Step 7: Assemble the character

Now read the state back. Load the base. Apply your diff. Every value you wrote replaces the base value. Every value you left out keeps its base value. The result is Victoria immediately after the crash.

## Step 8: Check your work

- You wrote no value that equals the base.
- You deleted no base field.
- You diffed against the base, not against another state.
- You re-evaluated all flags.

## What you learned

You wrote a checkpoint from an event. You saw that a diff holds only changes. You assembled a character from base plus diff. Next, see the [how-to](3-how-to.md) for splitting moments and recording relationships.
