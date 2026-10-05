---
title: "The spine house inventory: how-to"
type: how-to
for: A builder who keys house files to the spine or cleans the inventory
does: Gives the steps for the inventory's recurring tasks
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/01_NARRATIVE_FRAMEWORKS/📐 ssot_01_spine_house_inventory.md
source_version: 1.0.2
---

**Who it's for:** a builder keying house files to the spine · **What it does:** steps for finding, keying and deduping holdings · **Type:** how-to

# The spine house inventory: how-to

Terms are defined in the [reference](2-reference.md).

## Find what the house holds at a spine level

1. Open the reference and go to the level's section, L0 to L7.
2. Read the Path and Holds columns.
3. Read the Also column for files that serve other levels too.
4. For L5, open `02_CHARACTER_SYSTEMS/` and the files the L5 list names.

## Key a house file to a level

1. Decide the file's home level, the one it serves most.
2. List the file's path and what it holds.
3. Fill the Also column with every other level it serves.
4. Order the row by level.
5. If two levels tie, Chief decides. Until he does, give the file the lower level number as its home.
6. List the other tied level in the Also column.

## Key a library source to the spine

1. Take the source's `feeds:` assignment.
2. Key it to a tree address (`SPINE.Lx`), not a ladder address.
3. Check the narratology shelf first. Stage 2 keys that shelf before the rest.

## Check a shelf's distill status

1. Look in `01_NARRATIVE_FRAMEWORKS/_narratology_shelf/` for finished distills.
2. Open `📐 ssot_01_narratology_shelf.md` for the index and `UID_index.md` for the UID key.
3. Do not trust the 0.6% figure. The addendum corrects it with 109 promoted distills.

## Clear a dedupe candidate

1. Confirm the two files are byte-identical. The variable registries in 00 and 05 are the open case.
2. Pick the copy to keep.
3. Remove the other.
4. Leave the Victoria authoritative and handoff pairs alone. They are duplicates by design, since the handoff is a bundle.

## Find a reserved empty folder

1. Check `_AUTHORITATIVE/OVEREXITOUT/{plot,theme,world}/`.
2. Treat them as reserved and empty.
3. Reconcile any new domain with the numbering ruling: plot is `04_PLOT_SYSTEMS/`, style guides are `06_`.
