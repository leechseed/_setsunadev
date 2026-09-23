---
name: dope-sheet
description: Build BOLO N's standing status page (DOPE SHEET N, ruled 9/11) in the formation (BOLO 51 phase 2.4) — a script gathers every mention, a Mission Specialist (MS, sonnet) drafts Situation · Execution · Admin · Log, the CDR writes Mission · Command & Signal · the order and the calls, a script reviews, build, publish. Fires on "DOPE SHEET N", "the dope on N", "status report on N", "build the sheet for N".
---

# DOPE SHEET N — the standing page

**Steps (BOLO 64, provisional 9/23):** RECON = `prep.py N` gathers every mention · ORDER = `brief.SHEET.md` · EXECUTE = SHEET drafts, the main line writes M · C · the order · CONSOLIDATE = `check.py --promote`, `build.py`, publish, the three URL records.

Canonical: SOP.md §1 (DOPE SHEET / FRAGO rows) · §2 (the layout). If `_tools/bolostatus/boards/N.json` already exists, this is not a build: show the page link from `_tools/pages/pages.json`, or run the `frago` skill for an update.

## H0 · Prep (zero tokens)

```
python _tools/bolostatus/prep.py N
```

Writes `_tools/bolostatus/work/N/sources.md` (the BOLO row, the rows it names, STATE mentions, note mentions, related sheets' status lines), `schema.json` (the newest sheet, trimmed, as the shape), and `brief.SHEET.md`.

## H1 · One specialist

Launch **SHEET** (sonnet) with the brief verbatim. It writes `boards/N.draft.json`: the header, the mantra, paragraphs S · E · A · L. It leaves M and C as empty shapes and the order and calls empty. It reads nothing outside the work dir.

## H2 · The main line's judgment

Edit `boards/N.draft.json` directly (small JSON edits, not a rewrite):

- **M** — `task` ("<verb> …,"), `intent` ("in order to …"), `spoken` (Chief's words), `endstate` (3–4 lines).
- **frago** — `mission` (task + intent in one sentence), `order` (the one next action, bold), `default` ("Silence: …"), `calls` (each `q` · `options` · `default` · `s`).
- **C** — who decides · the gate · signal.

Then:

```
python _tools/bolostatus/check.py N --promote
```

Blocking findings (paragraph order, missing header keys, unknown glossary keys) stop it; fix and rerun. Advisory ones ride in the reply. Add `boloN` to `_tools/sitrep/glossary.json` if the check says it is missing (the standing order).

## H3 · Build and publish

```
python _tools/bolostatus/build.py N
```

Publish the printed fragment with the Artifact tool (new page: favicon + one-line description; the title is `DOPE SHEET N`). Then record the URL in three places: the BOLO row's status cell (`**DOPE SHEET N:** <url>`), `_tools/pages/pages.json` (`"N": "<url>"`), and the glossary `boloN` entry's `w`. The reply carries the link and the order line.
