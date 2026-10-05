---
title: "The worldbuilding system: how-to"
type: how-to
for: "A writer or script author adding to and checking a world's catalog"
does: "Gives numbered steps for each task the worldbuilding system defines"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/05_WORLDBUILDING_SYSTEMS/📐 ssot_05_worldbuilding_system.md
source_version: 1.1.1
---

**Who it's for:** a writer who knows what the catalog is · **What it does:** step-by-step recipes for worldbuilding tasks · **Type:** how-to

# The worldbuilding system: how-to

Look up fields in the [reference](2-reference.md). Read the [concept](1-concept.md) for the why.

## Decide which system owns a world fact

1. Ask: is the fact about one place? If yes, it goes to 03 Setting.
2. If not, ask: is it about one person? If yes, it goes to 02 Character.
3. If not, ask: is it a change over time? If yes, the change goes to 08 Tracking.
4. If the thing itself is an event or its telling, it goes to 04 Plot.
5. If it is the story's argument, it goes to 06 Theme.
6. Otherwise it is a shared thing. Make a catalog entry.

## Add a catalog stub

1. Pick the type code from the types table. Check the type is one of the open eight, or that a story needs it now.
2. Mint the id as `WB-<TYPE>-<nnnn>`. Search the repo for the highest number first. Never reuse an id.
3. Create the file at `catalog/<type code>/<id>.md` with YAML front matter.
4. Fill only `id`, `type`, `name` and `one_line`.
5. Set `status: stub`.
6. Write `—` for any field not yet narrated.
7. Do not hand-edit `catalog/_INDEX.md`. The compiler generates it.

## Mark an inference

1. Write the word `inferred` in the field you guessed from canon.
2. Write `—` where the story has not narrated the field.
3. Set `status: provisional` for an entry not yet narrated. Use plain words, never a glyph.

## Promote a stub to filled

1. Add a source to `sources`.
2. Add a state id to `state`, in the form `<kind>:<slug>`.
3. Add one era to `era`, using the 08 time code.
4. Set `status: filled`.
5. Fill other fields only when a scene, place or person needs them.

## Link an entry to the other systems

1. Set `places` to the 03 place ids where the thing is found.
2. Set `groups` to the GRP ids that keep it.
3. Set `origin` to the fabula event that brought it into being.
4. Set `state` to the 08 subject id. Never copy state into the entry.
5. Set `tropes` to the trope ids. Never restate the trope.

## Retire an entry

1. Keep the entry's file.
2. Set `status: retired`.
3. Add a pointer to the doc that took it. For example, Tremor Cult points to the 01 registry's `tremor_cult` story.
4. Never reuse its id.

## Check the world with the coherence tests

1. Run the script tests: CT1, CT3, CT4, CT5, CT6, CT9, CT13.
2. Have a person read the reader tests: CT2, CT7, CT8, CT10, CT11, CT12, CT14, CT15, CT16.
3. Read each result as pass, fail, or "stub, not yet checkable".
4. Treat a stub as not failing.
5. Drop any test you cannot turn into a checkable statement.

## Log a retcon

1. Check the new entry against existing entries (CT10): can both hold?
2. If you change a narrated entry, log the change as a retcon with its cost.
3. Record the change as an 08 record, not a rewrite of the catalog entry.

## Read the world view

1. Open the compiled page.
2. Filter by era, place, group or type.
3. Read the gap list for infrastructures I1 to I10 with no entry. Treat a gap as a gap, not a failure.
4. To change a fact, follow the row's link to the owning file and edit there. The view has no input fields.

## Keep the world thin

1. Before adding a detail, ask whether a scene needs it.
2. If not, leave the entry a stub.
3. Do not add a date without a good reason.
4. Do not build out a catalog type before the story that visits it.
