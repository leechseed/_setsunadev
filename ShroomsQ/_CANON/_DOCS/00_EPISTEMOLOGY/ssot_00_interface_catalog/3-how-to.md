---
title: "Interface catalog: how-to"
type: how-to
for: "The CDR and the writers, who already know what the catalog is and need to do one of its four tasks."
does: "Gives the steps to look up an interface, add one, close a one-sided wiring and rule a design call."
owner: Chief
state: draft
reviewed: 2026-10-05
source: "ShroomsQ/_CANON/_SSOT/00_EPISTEMOLOGY/📐 ssot_00_interface_catalog.md"
source_version: 0.2.0
---

**Who it's for:** the CDR and the writers, who already know what the catalog is and need to do one of its four tasks · **What it does:** gives the steps to look up an interface, add one, close a one-sided wiring and rule a design call · **Type:** how-to

# Interface catalog: how-to

Source: [ShroomsQ/_CANON/_SSOT/00_EPISTEMOLOGY/📐 ssot_00_interface_catalog.md](../../../_SSOT/00_EPISTEMOLOGY/📐%20ssot_00_interface_catalog.md). The page is generated. Never edit it by hand. Change `_tools/docs/out/ifc_candidates.json` or `_tools/docs/ifc_build.py`, then rebuild. Terms are in the [reference](2-reference.md). For a first pass, try the [tutorial](4-tutorial.md).

## Look up an interface

Use this when you hold an id such as `IF-02-04-01`, or a pair of systems, and want the row.

1. Split the id. `IF-02-04-01` is the interface for systems 02 and 04, row 01. The lower system number comes first.
2. Open the source page and go to THE REGISTER.
3. Find the subsection headed with the two systems, such as "02 Character (LEECHSEED) ↔ 04 Plot". Use "09 Operations → every system" for ids that start `IF-09-ALL`.
4. Find the row whose first cell is the id.
5. Read the row left to right: `side`, `kind`, `payload`, `trigger`, `stated in`, `status`.
6. Read the italic note in parentheses at the end of the payload. It records what the extractor found odd.
7. Read the other side. Scan the same table for rows whose `side` starts with the other system's number. If no row starts with that number, the other side is silent on this pair.
8. Check the "Named only" line under the table. It lists docs that cite each other with nothing crossing.

To find a row by id in the JSON, search `_tools/docs/out/ifc_candidates.json` for `"id": "IF-02-04-01"`. The row there carries three fields the page hides: `evidence`, `to_doc` and `slice`.

## Add a new interface

Use this when you find a place where one system hands another something and the register lacks it.

1. Open `_tools/docs/out/ifc_candidates.json`. It holds the register's truth.
2. Copy a row of the same kind from the file. Paste it at the end of the list.
3. Set `from_sys` and `to_sys` to two-digit system codes, such as `"02"` and `"04"`. Use `"ALL"` as `to_sys` for 09's rows that cover every system. `from_sys` is the stating side.
4. Set `from_doc` and `to_doc` to the two doc stems, such as `ssot_02_character_astrology`.
5. Set `kind` to `DATA`, `CONTROL` or `MENTION`. A MENTION shows only as a "named only" line.
6. Set `direction` to `writes`, `reads`, `gates` or `gated_by`, from the stating doc's side.
7. Fill `payload` with the named thing that crosses. Fill `trigger` with when it fires. Fill `where` with the section of the stating doc.
8. Set `status`. Use `built` if the source states it as working. Use `parked` if the source marks it phase 2. Use `proposed` if you argue the system needs it.
9. Fill `evidence` with the sentence from the stating doc. Fill `note` with anything odd, or leave it empty.
10. Leave `id` out. The build assigns it and writes it back.
11. Run `python _tools/docs/ifc_build.py`.
12. Read the one-line result. It gives the new row count, the interface count and the pair count. Open the page and find your row in its pair.

> **OPEN:** The build numbers each pair's rows by sort order, not by arrival. A new row can renumber the rows after it, which clashes with the page's rule that an id never changes. The source states no fix.

## Close a one-sided wiring

Use this when THE WIRING FINDINGS lists a pair and you own the silent side.

1. Open THE WIRING FINDINGS. Find the pair, written `A→B`. The arrow points the way the data flows.
2. Decide which side is silent. In the first list ("written, never read") B is silent. In the second list ("read, never written") A is silent.
3. Open the pair's subsection in THE REGISTER. Find the stating rows and note their IF ids.
4. Open the silent system's source doc. Go to the section that lists its inputs or outputs: a HANDSHAKE, Boundaries, Feeds or Dependencies section. If none exists, add a short "Interfaces" subsection under the nearest fitting H2.
5. Add one line that names the interface by its IF id. The batch used this form: `Reads from 03 (IF-02-03-04): S8 witness supplies the character id.`
6. Bump the doc's version one minor level. Add one history line in the doc's own history layout.
7. Write the ids you closed into `_tools/docs/work/ifc/done.<system>.json`, a JSON list of IF ids.
8. Run `python _tools/docs/ifc_apply.py`. The script flips each done `proposed` row to `built`, tags a one-sided row with a note, and rebuilds the catalog.

> **OPEN:** `ifc_build.py` builds the findings from register rows only. A new line in a source doc changes no row, so the pair stays listed. Adding the silent side's row (see Add a new interface) removes the pair. The source does not say whether this is the intended close.

## Rule a design call

Use this when Chief decides one of the design calls. Chief rules. The writer records.

1. Read the call in THE DESIGN CALLS. It states a problem and a recommendation, and it names the fields and sections it changes.
2. Find the call's proposed rows in THE REGISTER. Each carries an IF id and an italic note that states the gap.
3. Get Chief's ruling: as recommended, changed, or declined. Quote his words in the heading, as the 0.2.0 heading quotes "My word".
4. Edit the `CALLS` block in `_tools/docs/ifc_build.py`. The page is generated, so the calls live in the script. Change the heading to `RULED <date>` and update any recommendation Chief changed.
5. Run `python _tools/docs/ifc_build.py` to rebuild the page.
6. Fire one fix batch per system. Use `_tools/docs/work/brief.APPLY.md` as the brief. Each writer lands the ruled fields in its source docs, bumps versions and writes `done.<system>.json`.
7. Run `python _tools/docs/ifc_apply.py`. It flips every done `proposed` row to `built` and rebuilds the page.
8. Check the totals line under THE N² GRID. The proposed count falls as fixes land.

A ruled page is never edited quietly (DOC-SOP 3.4). Chief rules the change and the reviewed date updates.
