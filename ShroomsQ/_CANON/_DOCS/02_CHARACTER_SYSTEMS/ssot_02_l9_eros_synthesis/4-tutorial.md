---
title: "L9 EROS synthesis: tutorial"
type: tutorial
for: "A newcomer who has never traced a schema change back to its sources"
does: "Walks one learner through tracing change 5, the shame split, from source to applied field"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/02_CHARACTER_SYSTEMS/📐 ssot_02_l9_eros_synthesis.md
source_version: 1.1.0
---

**Who it's for:** a newcomer tracing a schema change for the first time · **What it does:** one guided trace of change 5, the shame split · **Type:** tutorial

# L9 EROS synthesis: tutorial

You will follow one change from three sources to a live field and a backfilled instance. The example is change 5, the split of `shame_index`. Lookups are in the [reference](2-reference.md).

## Step 1. Read the problem

Open section 5 of the source. Find change 5.

It says Victoria Midnight's `shame_index: 2` describes immunity to being shamed for being seen. A different mechanism exists: shame about a role, such as bottoming or receiving. One number cannot hold both.

Write one sentence in your own words saying why one scalar fails here.

## Step 2. Find the three sources

Change 5 cites MSX.23, MSX.25 and MSX.34. Open section 2, the register. Read each row.

- MSX.23 names the "Act Like a Man Box". Masculinity shame blocks receptive pleasure.
- MSX.25 says "bottoming makes you a woman". Mockery enforces it, not anatomy.
- MSX.34 says stigma tracks role: the penetrator carries none, the receiver is marked.

Check: each source reaches the same mechanism, and none is a copy of another.

## Step 3. Find the pattern

Open section 3. Find the method that names these three: "Masculinity-policing shame attaches to receptive role, not to desire itself."

Three independent cultures name the same mechanism. That agreement is why the synthesis trusted the change.

## Step 4. Read the rec

Return to change 5. The rec: split into `exposure_shame` and `role_shame`, both 0 to 10, with the same convention as the old field.

It also says the change was applied additively. `shame_index` stays as a read alias for `exposure_shame`. No field was removed.

## Step 5. Check the instance

The synthesis backfilled Victoria's `exposure_shame` with 2, the same value as `shame_index`. The reason is on record: the Administration's main weapon is public Desyncs and legibility, and she is immune to it.

Her `role_shame` stays null, marked ⏸. The record does not document it, so the system invents nothing.

Check: one new field carries a value from the record, and one is honestly blank.

## Step 6. Say it back

Without looking, answer three questions.

1. Which three sources fed change 5?
2. Which field kept the old meaning, and under what name?
3. Why is Victoria's `role_shame` null?

You have traced one change from source to schema to instance. The [how-to](3-how-to.md) shows how to repeat the trace for any L9 field.
