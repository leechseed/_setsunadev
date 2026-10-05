---
title: "Interface catalog: tutorial"
type: tutorial
for: "A writer or the CDR using the catalog for the first time, who has the source page open."
does: "Teaches the lookup by doing one: find IF-02-04-01, read both sides and test whether it is one-sided."
owner: Chief
state: draft
reviewed: 2026-10-05
source: "ShroomsQ/_CANON/_SSOT/00_EPISTEMOLOGY/📐 ssot_00_interface_catalog.md"
source_version: 0.2.0
---

**Who it's for:** a writer or the CDR using the catalog for the first time, who has the source page open · **What it does:** teaches the lookup by doing one: find `IF-02-04-01`, read both sides and test whether it is one-sided · **Type:** tutorial

# Interface catalog: tutorial

In this lesson you look up one interface and read what each side says about it. You learn why one test calls it wired while a closer read finds a gap. Open the source page first: [ShroomsQ/_CANON/_SSOT/00_EPISTEMOLOGY/📐 ssot_00_interface_catalog.md](../../../_SSOT/00_EPISTEMOLOGY/📐%20ssot_00_interface_catalog.md). The lesson uses version 0.2.0. If you meet a term you do not know, check the [reference](2-reference.md).

## Step 1. Read the id

Take the id `IF-02-04-01`.

Split it at the dashes. `IF` marks an interface. `02` and `04` are the two systems: the LEECHSEED character system and Plot. `01` is the row's place in that pair.

You now know where to look: the subsection for the 02 and 04 pair.

## Step 2. Find the pair

Open the source page and go to THE REGISTER. Scroll to the heading "02 Character (LEECHSEED) ↔ 04 Plot".

You see a table with seven columns: `id`, `side`, `kind`, `payload`, `trigger`, `stated in` and `status`. Under it you see a line that starts "Named only".

The table has 18 rows. Their ids run from `IF-02-04-01` to `IF-02-04-18`.

## Step 3. Read the row

Find the first row, `IF-02-04-01`. Read each cell.

- **side:** `02 writes`. The 02 docs say that 02 writes this to 04.
- **kind:** `DATA`. A field, record or structure crosses.
- **payload:** the Lifecycle Protocol (6 Movements) table, with its columns Movement, Systemic State, Dominant Planet and Variable Condition.
- **trigger:** "when plot_systems lays out the macro-arc".
- **stated in:** `ssot_02_character_astrology`, in the section Category 10: Lifecycle Protocol (The 6 Movements).
- **status:** `built`. The source states the interface as working.

The payload ends with an italic note: "Movements are centered on the MC (Victoria Midnight for OVEREXITOUT). Whether 04 actually reads this table is unverified from this side."

The note tells you the extractor could not confirm that 04 reads the table. That is your question for the rest of the lesson.

## Step 4. Read the other side

The row records only what 02's docs say. To hear 04, scan the same table for rows whose `side` starts with `04`.

You find five: `IF-02-04-09` (04 writes), `IF-02-04-10` (04 reads), `IF-02-04-11` (04 reads), `IF-02-04-17` (04 writes) and `IF-02-04-18` (04 gates).

Read each payload. The 04 side states:

- `event_id`, which the character state record receives as `origin_event`;
- the P12 `story_point` and `storyform_id`;
- the throughline-to-character assignments in OXO's movements map;
- a separate character node for Anna Colson (the copy);
- the origin-moment rule for layers L5 and L7 to L10.

None of the five names the Lifecycle Protocol table. The register holds no 04 statement that 04 reads it.

## Step 5. Test the pair against THE WIRING FINDINGS

The catalog runs one test for one-sidedness. Go to THE WIRING FINDINGS. Look for `02→04` in the first list, "Stated as written, never stated as read". Then look in the second list.

You find it in neither.

Here is why. The test works on a pair and a direction, not on one row. For 02 to 04 it asks two questions. Does any built DATA row say 02 writes to 04? Yes: `IF-02-04-01` and others. Does any built DATA row say 04 reads from 02? Yes: `IF-02-04-10` and `IF-02-04-11`. Both are stated, so the pair counts as wired.

## Step 6. Compare with a pair that is listed

The first list holds `00→04`. Open the subsection "00 Base ↔ 04 Plot".

Look down the `side` column. Every row starts with `00`. The 00 docs state every row, and no row starts with `04`. The 04 side is silent, so the test flags the pair.

That is the pattern the test finds. Your row, `IF-02-04-01`, looks different: 04 states other reads from 02, so the pair passes the pair-level test.

## Step 7. Write down what you found

Record your finding in three lines:

1. `IF-02-04-01` is a built DATA row. 02 states it writes the Lifecycle Protocol table to 04.
2. No 04 row names that table. The extractor's note says the same: it is unverified from 02's side.
3. The pair 02 to 04 is not in THE WIRING FINDINGS, because 04 reads other things from 02. The pair test passes while this one row is unmatched.

You have found a row-level gap that the pair-level test cannot see. The catalog's rule fits: "The catalog records the statements; it does not pretend they agree."

## What you did

You split an id, found its pair, read a row, read the other side and ran the one-sided test twice: once on a pair and once on a row. You also saw the limit of the test.

To go on, learn the four tasks in the [how-to](3-how-to.md). To close a gap like the one you found, follow "Add a new interface" or "Close a one-sided wiring" there. For why the catalog keeps both sides, read the [concept](1-concept.md).
