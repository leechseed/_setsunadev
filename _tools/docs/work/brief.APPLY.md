# BOLO 102 stage 2 · apply the ten rulings · brief (MS, one per system)

Repo root: C:\Users\U01_LEECHSEED\Desktop\_setsunadev. Write UTF-8, keep each file's line endings.

Chief ruled all ten design calls on 10/5 ("My word"). You land them in YOUR SYSTEM's source docs, then mirror the change on the doc pages. Nothing else.

## Read, in this order

1. `ShroomsQ/_CANON/_SSOT/00_EPISTEMOLOGY/📐 ssot_00_interface_catalog.md`, the section **THE DESIGN CALLS** only (ten rulings, each with the exact fields and sections it names). These are law.
2. `_tools/docs/work/ifc/apply.<your system>.md`: the proposed rows that touch your system (with their IF ids) and the one-sided wirings where your system is the silent side.
3. Your system's source docs (`ShroomsQ/_CANON/_SSOT/<system>/*.md`, top level), as needed.

## Do

**A. The rulings.** For each of the ten calls, apply every change whose rec names a doc or field in YOUR system. The rec says where it lands ("08 gains a section 'The address'", "06 gains `holders:`", "the 05 entry schema gains `gauge:`"). If the rec names your system, you own it; if it names another, leave it. Write the field or rule into the doc's schema table, field list or rules section, in that doc's own layout, with one line of meaning per field. Cite the ruling: `(IF catalog call N, ruled 2026-10-05)`.

**B. The silent side.** For each one-sided wiring in your apply list, add ONE line in the right doc of your system naming the interface: e.g. `Reads from 03 (IF-02-03-04): S8 witness supplies the character id.` Put it where that doc lists its inputs or outputs (a HANDSHAKE, Boundaries, Feeds or Dependencies section; create a short "Interfaces" subsection under the nearest fitting H2 if none exists).

**C. Versions.** Bump each changed source doc one minor level (x.y.z → x.(y+1).0, since the schema grew) and add one history line in the doc's existing history layout: `BOLO 102 stage 2 (Chief: "My word"): <what landed, one line>.` Set last_updated / reviewed to 2026-10-05 where the doc has them.

**D. The pages.** Under `ShroomsQ/_CANON/_DOCS/<system>/<doc>/`: put each new field or rule into `2-reference.md` under the component it belongs to (never add an H2 or H3; the headings must match the source's), add a how-to step where a procedure changed, and set `source_version` on all four pages. Delete any `> **OPEN:**` line the change resolves.

**E. Report the ids.** Write `_tools/docs/work/ifc/done.<your system>.json`: a JSON list of the IF ids you landed (proposed rows now stated in a source, and silent-side lines added). The register flips those rows to `built` from this file.

## Rules

- Only what the rulings and the apply list say. No other rewording.
- DOC-SOP 3.2: 20 words per sentence, every sentence names who acts.
- Standing names: Chief · the Command · the LEECHSEED character system · Touchstones · DCUS. Systems: 05 Worldbuilding · 06 Theme · 07 Style · 08 Tracking · 09 Operations.
- Two files moved under call 9 before you started: `ssot_00_process_illustration_character_pipeline` now lives in 02, `ssot_00_bold_venture_design_system` in 00. The 02 and 00 writers own them.
- Edit only your system's docs and pages. Do not consult other agents. If a ruling cannot land as written (the field already exists under another name, the section is gone), land the closest faithful form and report it.

## Reply

Three lines at most: docs bumped (name → version) · IF ids landed (count) · anything adapted and why.
