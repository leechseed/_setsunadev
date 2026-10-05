---
title: "The worldbuilding system: tutorial"
type: tutorial
for: "A writer new to the catalog who learns by filing one DCUS entry"
does: "Teaches the catalog by walking the DCUS proof's Feed entry from stub to filled"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/05_WORLDBUILDING_SYSTEMS/📐 ssot_05_worldbuilding_system.md
source_version: 1.1.1
---

**Who it's for:** a writer new to the catalog · **What it does:** walks one DCUS entry from route to checked · **Type:** tutorial

# The worldbuilding system: tutorial

You will file the Feed from DCUS, the way the proof did. Keep the [reference](2-reference.md) open.

## Step 1: route the fact

1. Take the fact: DCUS runs a system that watches and scores everyone.
2. Ask if it is about one place. It is not; it is a shared tool.
3. Ask if it is about one person, a change over time, an event, or the story's argument. It is none of these.
4. Conclude it is a shared thing. It belongs in the catalog.

## Step 2: pick the type and mint the id

1. Look at the types table. The Feed is a technique or device, so the type is TEC.
2. The proof's id for it is `WB-TEC-0001`.
3. Check the repo for the highest TEC number before you mint one for real.
4. Create `catalog/TEC/WB-TEC-0001.md`.

## Step 3: write the stub

1. Set `id` to `WB-TEC-0001` and `type` to `TEC`.
2. Set `name` to `The Feed (DCUS)`.
3. Write a one-sentence `one_line`.
4. Set `status: stub`.
5. Stop. A stub is a complete entry.

## Step 4: link it

1. Set `era` to `M2 to M4`. The proof ends every DCUS era at M4, because canon casts DCUS for Movements 2 to 4.
2. Set `origin` to `backstory_dcus_rebrand`. The proof marks it `inferred`, so write that word.
3. Set `state` to a `tech:` id, in the form `<kind>:<slug>`.
4. Set `places` to the DCUS place id.

## Step 5: promote it

1. Add a source to `sources`.
2. Check that the entry has a source, a state id and one era.
3. Set `status: filled`.

## Step 6: run the lens

1. Run the script tests. CT1 and CT13 pass on the filled set, as they did on 9/29.
2. Read CT3: the Feed is not an institution, so the test does not bite here.
3. Notice that the entry is not asked for a ruin or a legitimacy statement.
4. Open the world view. Find the Feed's row. Click through to the entry's file to edit.

You have filed one entry end to end. Next, use the [how-to](3-how-to.md) to retire or link other entries.
