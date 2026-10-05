---
title: "Variable registry: how-to"
type: "how-to"
for: "A designer adding, renaming or reading a character variable"
does: "Gives the steps for each registry task"
owner: "Chief"
state: "draft"
reviewed: "2026-10-05"
source: "ShroomsQ/_CANON/_SSOT/00_EPISTEMOLOGY/📐 ssot_00_variable_registry.md"
source_version: "1.3.1"
---

**Who it's for:** a designer working with character variables · **What it does:** gives the steps for each registry task · **Type:** how-to

# Variable registry: how-to

Entries live in the [reference](2-reference.md).

## Add a variable to the registry

1. Check that no variable already has the name. No two share a canonical name in any namespace.
2. Build the path `[DOMAIN].[LAYER_CODE].[variable_name]`, with a name in snake_case of 30 characters or fewer.
3. Fill every Registry Format field. The fields are path, display name, type, scale class, display range, constraint, default, source, tag, feeds, tier min, behavior.
4. Take the scale class from the Base 60 SSOT for a numeric variable.
5. Set the tag: Static, Dynamic or Derived. No variable ships without one.
6. Write one behavior sentence in LoL-ability style.

## Add a slice field

1. Add one table row with Canonical Path, Type, Scale Class, Tag, Source, Consumer, Values and sub-fields.
2. Put it in the section for its layer, in layer order.
3. Copy the tag from the slice table "Field tags · every field".
4. Leave the behavior in the slice layer paragraph. Do not copy it.

## Choose the right namespace

1. For a primary or secondary attribute, use `T1` or `T2`.
2. For a deep layer variable, use `T3`. For an extended sub-table, use `T3X`.
3. For a computed value, use `DRV`. For a boolean trigger, use `FLG`.
4. For a state-only value, use `STT`. For a record field, use `META`.
5. For a module variable, use `MOD.[MODULE_CODE].[variable_name]`.
6. For a setting layer field, use `SET`. For a plot layer field, use `PLT`. Setting (03) and Plot (04) own those fields.
7. For a relationship record, use `REL`. The 02 state architecture owns those fields.

## Point to another system's field

1. Find the owning doc in the Ownership Rule table.
2. Add one pointer row for that system. Do not copy the field. Narrative (01), Character state (02), Style (07) and Operations (09) have rows too.
3. If the owner is none of the listed systems, check the Ownership Rule before adding anything.

## Rename a variable and keep the old name readable

1. Rename the canonical path.
2. Add an alias row with the old name, marked as a read alias.
3. Note the rename and its BOLO in the version history.
4. The source's example: `narrative_invariant` became `touchstone`, with one alias row kept.
5. For a coined name from the schema pass, cite THE SCHEMA PASS table in the vertical slice. Do not copy its rows.

## Add a derived statistic

1. Write the formula in internal (0-60) space.
2. List input constraints, such as WOUND even.
3. Name the output space and whether it may go negative or exceed 60.
4. Set source `computed` and tag Derived.
5. Add the stat to each input variable's Feeds field.

## Add a status flag

1. Write the trigger as a boolean expression over registered variables.
2. Use the four states: ACTIVE, PENDING, FIRED_PRE_STORY, INACTIVE. Store the fabula `event_id` on a flag in PENDING or FIRED_PRE_STORY.
3. Set source `computed` and tag Derived.
4. Add the flag to each input variable's Feeds field.

## Look up a variable's constraint

1. Open the variable's entry.
2. Read the Constraint row. Four variables carry one: WOUND (even), shadow_density (even), projection_tendency (multiples of 3), resistance_index (even).

## Retire a variable

1. Ask Chief to rule the retirement.
2. Keep the entry. Mark it retired with the date and BOLO.
3. Name any replacement variable.
4. Keep an alias row for the old name.
5. Remove the variable from every Feeds line that lists it.
6. Leave the data in the character records.
7. Add a version-history row.

Related pages: [concept](1-concept.md) · [reference](2-reference.md) · [tutorial](4-tutorial.md)
