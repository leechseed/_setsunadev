---
name: sitrep
description: Deliver the sit rep (the board + the SITREP page) in the formation ruled 2026-09-12 (BOLO 54) — a zero-token prep script, three independent specialists at gear 1 (one MS · two PS), RANGE the script reviewer at the fan-in, the CDR writing only Block VI and the header. Fires on "sit rep", "the board", "where did we leave off", "what are we working on", or the countersign.
---

# The sit rep — the formation

**Steps (BOLO 64, provisional 9/23):** RECON = H0 `prep.py` and the digest · ORDER = the three briefs, pasted verbatim · EXECUTE = H1 fan-out, H2 RANGE the script · CONSOLIDATE = H3 build, flush, publish.

**The rule (BOLO 54):** orchestrator decomposes, specialists run independently on disjoint inputs, sync only at named handoffs, one reviewer at the fan-in. The main line never reads the five files. Coordination is the serial part; there is none mid-run.

Canonical protocol: SOP.md §1 (the command) · §2 (the blocks) · §3 (the flush). This skill is the procedure.

**Alternative path (BOLO 68, provisional 10/12, untested):** [.claude/workflows/sitrep.js](../../workflows/sitrep.js) runs H0 to H2 as a Workflow script; this skill stays the canonical procedure.

## H0 · Prep (zero tokens)

```
python _tools/sitrep/prep.py
```

Prints a 20-line digest and writes `_tools/sitrep/work/<date>/`: the previous board split per block (`prev/`), STATE sliced to Blocked + Live, the git log since the last board (named commits + one FOOTPRINT line per autosave window; an autosave is never an item, BOLO 59), STATE's Moved sections since the last board (`state.moved.md`, the fold the close-out writes), `meta.json` (box probe · tree · rack · sizes), Blocks III and VII carried forward (`frag/`), and three briefs. Read the digest only. Do not open STATE, BOLO, SOP, PROJECTS or the cache notes.

## H0.5 · BREVITY picks — RETIRED 2026-10-04

**Retired (Chief, 10/4: "eliminate the brevity panel … it's just taking up space now"):** the panel is gone from the board; skip this step. The text below is kept as the record.


The board carries the BREVITY panel (BOLO 37, ruled 9/23): Chief's proword picks land in the page's store. Before the fan-out, `ArtifactData` action `list`, collection `picks`, on the standing URL; if any documents come back, save them to `<scratchpad>/picks.json` and run `python _tools/soi/brevity.py apply <scratchpad>/picks.json`, then add the SOI entry and the SOP §5 line the script prints for each ruled slot. The build reads `_tools/soi/benches.json` and the ruled slots show as ruled on the next board. The publish carries `capabilities: {db: {}}` once (omit on later publishes; the declaration persists).

## H1 · Fan out (one message, three agents, gear 1)

Launch all three in the same message, `run_in_background: false` is not needed; wait for all. Each prompt is the brief file's contents verbatim (Read it, paste it). No agent reads another's input or output.

| Role | Model | Reads | Writes |
|---|---|---|---|
| **RACK** | haiku | `_CACHE/*.session.md` + `prev/0.json` | `frag/0.json` (Block 0) |
| **INDEX** | sonnet | `state.blocked.md` · `state.live.md` · `git.log` · `PROJECTS.md` + `prev/{I,II,III,V}.json` | `frag/I.json` · `frag/II.json` · `frag/V.json` · `frag/III.json` (BOLO 86; if INDEX writes none, the carried III stands) |
| **WATCH** | haiku | `BOLO.md` + `prev/IV.json` | `frag/IV.json` (Block IV + pmcs) |

Model rule is the gearbox's (SOP §1): PS (haiku) extract, MS (sonnet) writes, CDR (Fable) on the main line only. A gear shift never adds a fourth specialist to the sit rep; it is not a bigger job.

## H2 · Fan in (RANGE, the reviewer, is a script)

```
python _tools/sitrep/assemble.py <date>
```

Runs the reviewer's checklist (eight blocks in order · text + trunk on every item · trunk values legal · every `[[key]]` in glossary.json · every BOLO number in Block IV real and placed once · Block V rows = the Blocked table · plain + strand complete · no stale fragment) and prints the digest: per-block counts against the previous board, first line of each, findings. Blocking findings (a missing fragment, an unknown glossary key) stop the write; fix the one fragment, rerun. Advisory findings go into the reply's one-line caveat, not into a re-run, with one exception.

**The auto-rerun (BOLO 95, ruled 10/4):** when the digest prints `RERUN <ROLE>` lines (sentences over 20 words, SOP 3.2), launch each named role once, in one message, with its `work/<date>/rerun.<ROLE>.md` brief verbatim, then rerun `assemble.py`. A role reruns once per board (the brief file is the marker); what survives goes into the caveat. Block VI is the main line's: write it plain the first time. Measured 10/4: the first pass carried 19 long sentences forward; one rerun took the board to 2.

Then the main line does the only judgment work in the run, off the digest alone:

1. Write `work/<date>/frag/VI.json` — the leverage line (`line` · `why` · `plain` · `strand`), same shape as `prev/VI.json`.
2. Write `work/<date>/meta.patch.json` — `when` · `trigger` · `countersign` · `main_effort` · `stats` as a **list of "label: value" strings**, never a dict (a dict blanked the board twice on 10/4; assemble.py now coerces it) (blocked count · main-effort idle days · agents deployed · anything measured) · `build.calls`/`rounds`. Anything not in the patch keeps prep's value.
3. Block III is rebuilt by default now (BOLO 86, provisional 10/12): prep flags it every run; edit `frag/III.json` against PROJECTS.md. Block VII's prowords refresh from the register.

## H3 · Build, flush, publish

```
python _tools/sitrep/assemble.py <date> --build --flush
```

Writes `boards/<date>.json`, builds `SITREP.html` + the fragment (path printed), then moves every cache note except the newest into `_LOG/` (the flush, SOP §3; BOLO 86 ruled 10/12: one note stays). Publish the fragment with the Artifact tool to the standing URL:

```
https://claude.ai/code/artifact/aebe5f9c-9f2c-4cb8-abbf-714a0a6ea28a
```

Pass it as `url`; never `read` the artifact first (a read dumps the page into context). The chat reply opens with **Left off** (one sentence) and **Start next: BOLO N** (one row, a five-word why) — ruled 10/6 — then carries the link, Block 0 in three bullets, the leverage line, and one caveat line if the reviewer left advisory findings. No preamble, no questions, no re-derivation of what the specialists wrote.

## Cost shape (why this order)

- Before: the main line read ~211 KB (about 55k tokens) and wrote the whole 27 KB board on Fable, then carried all of it in context for the rest of the session.
- Now: the main line reads two digests (~3 KB) and writes ~1 KB. The 211 KB is read once, by two haiku and one sonnet context that end when they return. Sync points: four (H0–H3), none of them agent-to-agent.
- If a fragment is wrong, rerun that one specialist with the finding pasted under its brief. Never launch a "checker" agent; the checklist is the checker.
