---
title: "Module registry: tutorial"
type: "tutorial"
for: "A designer new to the registry, learning by tracing the Coping module"
does: "Walks the Coping module from planned entry to narrowed entry"
owner: "Chief"
state: "draft"
reviewed: "2026-10-05"
source: "ShroomsQ/_CANON/_SSOT/00_EPISTEMOLOGY/📐 ssot_00_module_registry.md"
source_version: "1.2.0"
---

**Who it's for:** a designer new to the registry · **What it does:** traces one module through the 2026-10-04 audit · **Type:** tutorial

# Module registry: trace the Coping module

You will follow the Coping module through the audit and see why it narrowed. The facts come from the source entry.

## Step 1. Find the entry

Open the Registry Overview. Find `COPING`, Coping Mechanism Catalog. Its attachment is L4 WILL. Its status reads planned (narrowed). Its variables read 2 (was 4).

## Step 2. Read the declaration

The entry is version 0.1.0, attached to WILL, with no dependencies. Its description says it covers how the character manages stress before decompensation.

## Step 3. Read what changed

The 2026-10-04 note says the strategy itself now lives at L4 `coping_strategy`, in slice 2.1.0. So the two strategy enums left the module. Two scores remain.

## Step 4. Read the two variables

- `effectiveness`, SC-12: 0 means coping consistently fails. 12 means it reliably restores function.
- `cost_to_others`, SC-12: 0 means self-contained. 12 means maximum collateral damage.

The module now reads `T2.WILL.coping_strategy` from the core.

## Step 5. Compute the derived stat

The formula is `sustainability_internal = (effectiveness × 5) - (cost_to_others × 5 / 2)`.

Try effectiveness 8 and cost_to_others 4. You get 40 - 10 = 30. The constraint holds because 4 is even. An odd cost breaks the division.

## Step 6. Read the flag

`MOD.COPING.FLG.coping_failure` fires when effectiveness is below 4 and WOUND is above 6. With effectiveness 8, it does not fire.

## Step 7. Check the audit verdict

The audit table says: L4 `coping_strategy` holds the strategy. The verdict is still planned, narrowed to the two scores. None of the modules dropped.

## What you did

You read an entry, saw why the audit narrowed it, and computed its stat. Next, trace DECOMP, which depends on COPING. The [how-to](3-how-to.md) holds the registry tasks. The [reference](2-reference.md) holds every entry.

Related pages: [concept](1-concept.md) · [reference](2-reference.md) · [how-to](3-how-to.md)
