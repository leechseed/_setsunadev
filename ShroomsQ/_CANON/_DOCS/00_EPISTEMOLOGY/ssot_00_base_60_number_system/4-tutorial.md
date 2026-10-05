---
title: "Base 60 number system: tutorial"
type: "tutorial"
for: "A designer new to base 60, learning by recomputing one character"
does: "Walks Victoria Midnight's derived statistics from display values to internal results"
owner: "Chief"
state: "draft"
reviewed: "2026-10-05"
source: "ShroomsQ/_CANON/_SSOT/00_EPISTEMOLOGY/📐 ssot_00_base_60_number_system.md"
source_version: "1.0.2"
---

**Who it's for:** a designer new to base 60 · **What it does:** recomputes Victoria Midnight's numbers step by step · **Type:** tutorial

# Base 60: recompute Victoria Midnight

You will turn display values into internal values, then compute three derived statistics. The numbers come from the source's Victoria table.

## Step 1. Know the two steps

SC-20 variables have step 3. SC-12 variables have step 5. Internal equals display times step.

## Step 2. Convert her inputs

- WILL is 14 on SC-20. Internal: 14 × 3 = 42.
- WOUND is 10 on SC-12. Internal: 10 × 5 = 50.
- DRIVE is 12 on SC-20. Internal: 12 × 3 = 36.
- SOCIAL is 10 on SC-20. Internal: 10 × 3 = 30.

Check yourself: WOUND must be even, and 10 is.

## Step 3. Compute Stress Threshold

The formula is `WILL_i - WOUND_i`. You get 42 - 50 = -8.

The result is negative. Her wound outweighs her will in internal space. The source calls this diagnostic, not an error.

## Step 4. Compute Basic Damage Resistance

The formula is `WILL_i - (WOUND_i / 2)`. Divide first: 50 / 2 = 25. Then 42 - 25 = 17.

The division is exact because WOUND is even. An odd WOUND would break it.

## Step 5. Compute Narrative Momentum

The formula is `DRIVE_i + (resistance_i / 2)`. Her resistance_index is 8 on SC-12, so internal 40. Then 36 + 20 = 56.

## Step 6. Check your answers

Stress Threshold -8. Basic Damage Resistance 17. Narrative Momentum 56. They match the source table.

## What you did

You converted each value to internal space and computed there. Next, try Collapse Risk: `(WOUND_i + shadow_i) / 2`, with shadow_density 8, internal 40. The source answer is 45. The [how-to](3-how-to.md) holds the task steps and the [reference](2-reference.md) holds every formula.

Related pages: [concept](1-concept.md) · [reference](2-reference.md) · [how-to](3-how-to.md)
