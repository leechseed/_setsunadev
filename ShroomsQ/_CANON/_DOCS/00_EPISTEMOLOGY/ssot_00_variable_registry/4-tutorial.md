---
title: "Variable registry: tutorial"
type: "tutorial"
for: "A designer new to the registry, learning by tracing one variable end to end"
does: "Traces T2.WOUND.wound_score from its entry through a formula to a flag"
owner: "Chief"
state: "draft"
reviewed: "2026-10-05"
source: "ShroomsQ/_CANON/_SSOT/00_EPISTEMOLOGY/📐 ssot_00_variable_registry.md"
source_version: "1.2.1"
---

**Who it's for:** a designer new to the registry · **What it does:** traces one variable through its entry, formulas and flags · **Type:** tutorial

# Variable registry: trace the WOUND score

You will read one variable and follow it into every formula and flag it feeds. The facts come from the source entries.

## Step 1. Decode the path

Take `T2.WOUND.wound_score`. `T2` is the tier 2 domain. `WOUND` is the layer code for L5, Accumulated Damage. `wound_score` is the name, in snake_case.

## Step 2. Read the entry

Open the entry. It says: type int, scale class SC-12, display range 0–12, default 0. Source is authored, assigned from character history and not purchased. Tier min is 2. Tag is Dynamic.

## Step 3. Find the constraint

The Constraint row says even values only: 0, 2, 4, 6, 8, 10, 12. Remember it. The formulas depend on it.

## Step 4. Follow Feeds into the formulas

The Feeds row lists six consumers. Three are derived statistics.

- `DRV.basic_damage_resistance`: `(T2.WILL × 3) - ((T2.WOUND × 5) / 2)`.
- `DRV.stress_threshold`: `(T2.WILL × 3) - (T2.WOUND × 5)`.
- `DRV.collapse_risk`: `((T2.WOUND × 5) + (T3.SHADOW.shadow_density × 5)) / 2`.

Check why even matters. WOUND times 5, divided by 2, is exact only when WOUND is even.

## Step 5. Follow Feeds into the flags

Three are flags.

- `FLG.shadow_denial` fires when WOUND is above 6 and two other conditions hold.
- `FLG.optionlock_progression` fires when WOUND is above 8 and two other conditions hold.
- `FLG.kinship_collapse` fires when WOUND is above 8 and two other conditions hold.

## Step 6. Try a value

Set WOUND to 10, with WILL 14. Stress Threshold is 42 - 50, so -8. Both flags with an 8 threshold now pass their WOUND test, since 10 is above 8.

## Step 7. Check the alias

`T2.WOUND.severity` is a read alias of `wound_score`: one number, two names. It uses the same scale and the even-only rule.

## What you did

You decoded a path, read its entry, and followed it to three formulas and three flags. Next, trace `T3.SHADOW.projection_tendency`, which has a multiples-of-3 constraint. The [how-to](3-how-to.md) holds the registry tasks. The [reference](2-reference.md) holds every entry.

Related pages: [concept](1-concept.md) · [reference](2-reference.md) · [how-to](3-how-to.md)
