---
title: "The story registry: how-to"
type: how-to
for: A builder who adds, promotes or looks up stories, projects and vignettes
does: Gives the steps for the registry's recurring tasks
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/01_NARRATIVE_FRAMEWORKS/📐 ssot_01_story_registry.md
source_version: 1.0.1
---

**Who it's for:** a builder adding or promoting registry entries · **What it does:** steps for rows, blanks, projects and vignettes · **Type:** how-to

# The story registry: how-to

Terms are defined in the [reference](2-reference.md).

## Add a story

1. Add the row to the registry before any doc names the story in `applies_to`.
2. Add the row before any tracking file starts for it.
3. Fill the fields: `id`, name, aliases, genre, era, where, medium, status, storyform, nodes, data.
4. Write `id` short and lowercase.
5. Set status to the lowest rung that fits. Use provisional (seed) if a digest sourced the story and Chief has not ruled it.

## Fill a blank slot

1. If the slot has no name yet, write `—`.
2. If Chief deferred the slot to a pass, write `⏸ <pass name> (phase 2)`.
3. Do not count either mark as unfinished work.

## Place a story in an era

1. Pick one of the five eras: 1 Skeeter Creek, 2 DCUS, 3 LAKAD, 4 ASTRO7EX, 5 beyond.
2. Write the era number and name in the Era column.
3. If Chief has not placed the story, leave the era parked. LEECHSEED is the example.

## Promote a story up the status ladder

1. Read the current status: named only, reports in, storyform drafted, active.
2. Move one rung when the evidence exists, for example the storyform file.
3. Link the storyform in the Storyform column.
4. Link the tracking file in the data field once it exists.

## Add a project

1. Check that the item is a game, business or tool, not a story.
2. Add a row to the PROJECTS table.
3. Fill kind, status and source.
4. Do not add the project to the story registry.

## Add a vignette

1. Confirm the piece is short, has no full arc, and shows a place, group or custom.
2. Take the intake from Chief's spoken text. Save it near-verbatim as `_CANON_NODES/vignette-<slug>.md`.
3. Add a row to the VIGNETTES table. Give it an ID `VG-<nnnn>`.
4. Tag the worldbuilding catalog entries it shows, as `WB-<TYPE>-<nnnn>`.
5. Set the era. It is required.
6. Add a time code if you have one. It is optional.
7. Leave canon status at lineage until Chief rules it in.

## Check whether a name is a story

1. Look the name up in the registry.
2. If it is not there, treat it as not a story.
3. Remember the exclusions: *The Outliers* is OXO's series title, and BVIPDS / Bold Venture is the methodology and studio.

## Borrow from a story for a project

1. Find the story row.
2. Copy only what the project needs.
3. Keep the project's own row in the PROJECTS table.

## Assign a vignette's next ID

1. Grep the registry and `_CANON_NODES/` for the highest `VG-<nnnn>`.
2. Take that number plus one. Pad it to four digits.
3. Never reuse a number, even for a dropped vignette.
