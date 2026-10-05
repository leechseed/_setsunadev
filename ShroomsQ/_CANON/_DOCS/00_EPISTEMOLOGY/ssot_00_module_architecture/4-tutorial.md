---
title: "Module architecture: tutorial"
type: "tutorial"
for: "A designer new to modules, learning by declaring the walking style module"
does: "Walks the source's walking_style example from attachment to data exchange"
owner: "Chief"
state: "draft"
reviewed: "2026-10-05"
source: "ShroomsQ/_CANON/_SSOT/00_EPISTEMOLOGY/📐 ssot_00_module_architecture.md"
source_version: "1.0.1"
---

**Who it's for:** a designer new to modules · **What it does:** builds the walking style module step by step · **Type:** tutorial

# Module architecture: build the walking style module

You will declare one minimal module from the source's own example. By the end you will have the declaration and a data block.

## Step 1. Pick the layer

Walking style is a physical expression. Check the domain table. L2 VITAL covers physical and energetic presence, and its valid content lists walking style. Attach to L2.VITAL.

## Step 2. Name the module

The code is WALK. The source module id is `walking_style`. Variables will live under `MOD.WALK`.

## Step 3. Declare the variables

Add three.

- `MOD.WALK.gait_type`: enum of measured, urgent, languid, predatory, bouncing, shuffling.
- `MOD.WALK.pace_default`: enum of slow, moderate, brisk, variable.
- `MOD.WALK.signature_tell`: str, freeform, for example "leads with shoulders".

No variable is numeric, so no scale class applies.

## Step 4. Declare the access pattern

- **READS:** `T1.VITAL.base_value` and `T3.SHADOW.regression_pattern`.
- **WRITES:** own variables only.
- **DERIVED:** none.
- **FLAGS:** none.
- **TIER_MIN:** 3.

This makes it a minimal module: data only.

## Step 5. Write the data

When the application loads a character, the module receives a flat block:

```json
{
  "MOD.WALK.gait_type": "predatory",
  "MOD.WALK.pace_default": "brisk",
  "MOD.WALK.signature_tell": "leads with shoulders, slight leftward lean"
}
```

When it saves, the block becomes a sub-table:

```yaml
MOD_WALK:
  gait_type: predatory
  pace_default: brisk
  signature_tell: "leads with shoulders, slight leftward lean"
```

## Step 6. Check the rules

Confirm the module wrote only its own variables. Confirm it added no layer. Confirm it needs no other module. All three hold.

## What you did

You attached a module to a layer, declared its variables, set its access pattern and saw its data. Next, read the combat archetype example, which adds a derived value. The [how-to](3-how-to.md) holds the task steps. The [reference](2-reference.md) holds every block.

Related pages: [concept](1-concept.md) · [reference](2-reference.md) · [how-to](3-how-to.md)
