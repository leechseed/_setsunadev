# The library sweep (BOLO 18 stage 2) — the standing procedure

Ruled 2026-09-16 ("run the full pass"). One sweep keys every item in the Zotero library to every story-spine shelf at once. Scripts do everything but the reading; Payload Specialists (PS, haiku) read tables of contents in batches; Mission Specialists (MS, sonnet) write distills; RANGE (a script) sits at every fan-in.

## The shelves (the keys)

| Key | Holds | Model |
|---|---|---|
| `L0` | root theory of story | the spine doc |
| `L4` | plot | `04_PLOT_SYSTEMS/` |
| `L5` | character | `02_CHARACTER_SYSTEMS/` |
| `L6` | theme | spine L6 |
| `L7` | genre · medium · audience · market | spine L7 |
| `SETTING` | world and place, incl. RPG sourcebooks and campaign settings | `03_SETTING_SYSTEMS/` |
| `TEXTURE` | the telling: narration · POV · voice · prose · dialogue · cinematography | the texture layer |
| `CRAFT-PROCESS` | the writer's process, off the spine | — |
| `OFF` | not a story book | — |

Authority order for a key: Papi's own Zotero tags (`00_` … `09_`, never overwritten) → a PS TOC pass → title rules → subject default (off-spine subjects go `OFF` unless a rule hits).

## The sweep, in order

| Step | Command | Tokens |
|---|---|---|
| 1 · inventory the live DB | `python _tools/zotero/inventory.py` | 0 |
| 2 · subject for every item | `python _tools/zotero/classify_live.py` | 0 |
| 3 · key by tags + rules | `python _tools/zotero/fullpass.py key` | 0 |
| 4 · bundle the unkeyed | `FULLPASS_BATCH_DIR=<scratch> python _tools/zotero/fullpass.py batch` | 0 |
| 5 · PS per batch | one PS per `batchNN.md` → `_meta/spinekeys-batchNN.json` (keys + a repaired title for boilerplate-titled items) | ~40k per batch |
| 6 · fan-in | `python _tools/zotero/fullpass.py merge` → `SPINE-KEYS.md` (one shelf per key, whole library) | 0 |
| 7 · the gap | `python _tools/zotero/gap_scan.py` → `GAP-BY-SHELF.md` (the z-lib favourites ranked per shelf, the acquisition queue) | 0 |
| 8 · distill waves | per shelf: pdftotext → one MS per book on `TEMPLATE.distill.v4.md` → `check_distill.py` → the `_INDEX.md` Distilled register | ~120–190k per book |
| 9 · the model | the SSOT doc for the shelf is written FROM the shelf, never before it is keyed | one MS |

**The drop folder (9/16):** `C:/Users/U01_LEECHSEED/Desktop/_PDF_DROP/` — acquisitions land there as bare PDFs, no Zotero filing needed; `inventory.py` scans it (`src: drop`, title/author/year guessed from the filename, `bvx: NEW` until cataloged) and the sweep keys them like any row. **Regeneration is safe (9/16 fix):** `inventory.py` carries `spine · spine_src · subject · junk_title · rot` and PS-repaired titles across runs, matched by zkey; before the fix a rerun silently dropped every PS TOC key. Rot notes live in `_meta/rot.json`, keyed by BVX id. **The bulk is held:** drop rows with no catalog match get `spine_src: drop-unkeyed` and are never bundled for a PS pass until an intake is ordered (title rules over-key RPG character sheets). Acquisitions get a row in `catalog.json` with `drop_file`, and a manual spine key in `fullpass.py` `MANUAL` (`spine_src: manual`, never overwritten). Report: `_meta/DROP-INTAKE.md`.

Rules of the road: PDFs never enter the repo (public); only paths. A distill needs two to five Mermaid mind models (v4 §C). A book the sweep finds mis-catalogued gets a `rot` note in `inventory-live.json` and the distill lands on the correct BVX id. Re-run steps 1–3 before any library work; they are idempotent.

## Files

`inventory-live.json` · `INVENTORY-LIVE.md` · `CLASSIFY-LIVE.md` · `SPINE-KEYS.md` · `GAP-BY-SHELF.md` · `spinekeys-*.json` all live in `_0.1_BVX_LEARN/_meta/`. Distills live in `_0.1_BVX_LEARN/KNOWLEDGE_AREAS/BVX.####.md`.
