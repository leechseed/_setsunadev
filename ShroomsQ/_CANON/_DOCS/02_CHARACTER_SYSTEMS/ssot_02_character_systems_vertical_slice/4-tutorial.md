---
title: "Character system (12-layer vertical slice): tutorial"
type: tutorial
for: "A newcomer who has never computed a character's statistics and flags"
does: "Walks one learner through Victoria Midnight's slice from layer values to statistics, flags and the data block"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/02_CHARACTER_SYSTEMS/📐 ssot_02_character_systems_vertical_slice.md
source_version: 3.3.3
---

**Who it's for:** a newcomer who has never computed a slice · **What it does:** one guided pass through Victoria Midnight's statistics and flags · **Type:** tutorial

# Character system (12-layer vertical slice): tutorial

You will take Victoria Midnight's locked layer values and compute her seven statistics. You will test her five flags and spot one open item. Every number comes from the source. Lookups are in the [reference](2-reference.md).

## Step 1. Write down her layer values

Copy these into a scratch list.

| Value | Number |
|---|---|
| CORE | 13 |
| VITAL | 14 |
| SOCIAL | 10 |
| WILL | 14 |
| WOUND | 8 |
| DRIVE | 12 |
| `shadow_density` | 7 |
| `projection_tendency` | 6 |
| `resistance_index` | 8 |
| `shame_index` | 2 |
| `armor_index` | 8 |

Check: WILL is CORE plus 1. DRIVE is VITAL minus 2. Say why in your own words. The source says she is slightly more stubborn than intelligent, and meaning-driven characters burn below their physical ceiling.

## Step 2. Compute the seven statistics

Do each one yourself before you read the answer. Round fractions down.

1. Basic Damage Resistance is `WILL - (WOUND / 2)`.
2. Social Legibility is `SOCIAL - (projection_tendency / 3)`.
3. Narrative Momentum is `DRIVE + (resistance_index / 2)`.
4. Stress Threshold is `WILL - WOUND`.
5. Collapse Risk is `(WOUND + shadow_density) / 2`.
6. Truth Exposure Index is `SOCIAL + max(0, 10 - shame_index)`.
7. Expressive Range is `12 - armor_index`.

Answers from the source: 10, 8, 16, 6, 8, 18 and 4.

Check your fifth. 8 plus 7 is 15, and half of 15 rounds down to 7. The source's table writes `(8 + 7) / 2` and shows 8. Your 7 may differ from the source by one.

> **OPEN:** the source rule says all fractions round down, but Collapse Risk for Victoria reads 8 where 15 / 2 rounds down to 7. The source does not explain the difference.

## Step 3. Read the one that matters

Truth Exposure Index is 18. Above 15, the character cannot manage their own signal visibility. The source says this is why the Ban acts on her. She carries low shame and average social masking, so the system reads her completely.

Say it back in one sentence: why does a low `shame_index` raise her exposure?

## Step 4. Test her flags

Each flag has a trigger. Test each against her values.

1. SHADOW_DENIAL: `WOUND > 6`? Yes, 8. `projection_tendency >= 5`? Yes, 6. `conditional_patterns` contains "merit_earns_freedom"? Yes. The flag is ACTIVE.
2. TRUTH_VULNERABILITY: `SOCIAL < 12`? Yes, 10. `mc_problem_element` is Equity? Yes. `shadow_density > 6`? Yes, 7. ACTIVE.
3. OPTIONLOCK_PROGRESSION: `WOUND > 7`? Yes. `resistance_index > 7`? Yes, 8. `limit_type` is Optionlock? Yes. ACTIVE.
4. EARNED_JUDGEMENT: archetype Protagonist, outcome Failure, `WILL > 10`. All true. The flag waits for the climax, so it is PENDING.
5. KINSHIP_COLLAPSE: `attachment_style_score > 5`? Yes, 6. Secure base deceased? Yes. `WOUND > 7`? Yes. The crash already fired it, so it is FIRED_PRE_STORY.

Check: three ACTIVE, one PENDING, one FIRED_PRE_STORY.

## Step 5. Find the gaps

Open the source's instance. Count the fields marked `⏸ VM fill pass (phase 2)`. Notice the pattern. Her core numbers are filled. The newer fields are blank, and the record says why: no one has documented them, and the system invents nothing.

Two newer fields do carry values: `wound_kind` is error_committed, and `civic_standing` is the Ban plus her Sync-era standing.

## Step 6. Spot an open item

Look at the `DERIVED` section of her structured data block. It lists `expressive_range: 2`. You computed 4 in Step 2.

The version history explains the cause. Version 3.3.2 changed the formula to `12 - armor_index`, so her value moved from 2 to 4. Her canon nodes still say 2 and update in the VM fill pass.

> **OPEN:** the block in the source still reads 2 while the derived table reads 4.

## What you learned

You computed seven statistics from layer values, tested five flags against their triggers and found the open items. The statistics and flags are never entered. They come out of the layers. To build a slice for a new character, follow the [how-to](3-how-to.md).
