---
name: sitrep
description: 'Use when Chief asks where things stand: "sit rep", "the board", "where did we leave off", "what are we working on", or the countersign.'
---

# The sit rep — the formation

**Steps (BOLO 64, provisional 9/23):** RECON = H0 `prep.py` and the digest · ORDER = the three briefs, pasted verbatim · EXECUTE = H1 fan-out, H2 RANGE the script · CONSOLIDATE = H3 build, flush, publish.

**The rule (BOLO 54):** the orchestrator decomposes. Specialists run independently on disjoint inputs. They sync only at named handoffs, with one reviewer at the fan-in. The main line never reads the five files.

Canonical protocol: SOP.md §1 (the command) · §2 (the blocks) · §3 (the flush). This skill is the procedure.

Alternative Workflow path (BOLO 68, provisional 10/12, untested): [.claude/workflows/sitrep.js](../../workflows/sitrep.js). History, the retired BREVITY step and the cost figures: references/history.md

## H0 · Prep (zero tokens)

```
python _tools/sitrep/prep.py
```

It prints a 20-line digest. It writes `_tools/sitrep/work/<date>/`: the previous board split per block (`prev/`), STATE sliced to Blocked + Live, and the git log since the last board. The log holds named commits plus one FOOTPRINT line per autosave window; an autosave is never an item (BOLO 59). It also writes STATE's Moved sections since the last board (`state.moved.md`), `meta.json` (box probe · tree · rack · sizes), Blocks III and VII carried forward (`frag/`), and three briefs. Read the digest only. Do not open STATE, BOLO, SOP, PROJECTS or the cache notes.

## H0.5 · BREVITY picks — RETIRED 2026-10-04

Chief, 10/4: "eliminate the brevity panel … it's just taking up space now". Skip this step.

## H1 · Fan out (one message, three agents, gear 1)

Launch all three in one message and wait for all. Each prompt is the brief file's contents verbatim: Read it, paste it. No agent reads another's input or output. **Launch each by its agent name (`subagent_type`), never as general-purpose** (BOLO 155 M2, ruled 10/17 under the superpowers framework). Each brief opens with its `JOB:` line and ends with the status contract; each agent's reply ends DONE, DONE_WITH_CONCERNS, NEEDS_CONTEXT or BLOCKED.

| Role | Agent (`subagent_type`) | Model | Reads | Writes |
|---|---|---|---|---|
| **RACK** | `drafting-rack-block` | haiku | `_CACHE/*.session.md` + `prev/0.json` | `frag/0.json` (Block 0) |
| **INDEX** | `drafting-index-blocks` | sonnet | `state.blocked.md` · `state.live.md` · `git.log` · `PROJECTS.md` + `prev/{I,II,III,V}.json` | `frag/I.json` · `frag/II.json` · `frag/V.json` · `frag/III.json` (BOLO 86; if INDEX writes none, the carried III stands) |
| **WATCH** | `drafting-watch-block` | haiku | `BOLO.md` + `prev/IV.json` | `frag/IV.json` (Block IV + pmcs) |

The reruns (H2) launch the same agent names.

The gearbox sets the model (SOP §1): PS (haiku) extract, MS (sonnet) writes, CDR (Fable) stays on the main line. A gear shift never adds a fourth specialist.

## H2 · Fan in (RANGE, the reviewer, is a script)

```
python _tools/sitrep/assemble.py <date>
```

The script runs the reviewer's checklist:
- eight blocks in order
- text + trunk on every item, trunk values legal
- every `[[key]]` in glossary.json
- every BOLO number in Block IV real and placed once
- Block V rows = the Blocked table
- plain + strand complete
- no stale fragment

It prints per-block counts against the previous board, the first line of each, and findings. Blocking findings (a missing fragment, an unknown glossary key) stop the write. Fix the one fragment and rerun. Advisory findings go into the reply's one-line caveat, with one exception.

**The auto-rerun (BOLO 95, ruled 10/4):** the digest may print `RERUN <ROLE>` lines (sentences over 20 words, SOP 3.2). Launch each named role once, in one message, with its `work/<date>/rerun.<ROLE>.md` brief verbatim. Then run `assemble.py` again. A role reruns once per board; the brief file is the marker. What survives goes into the caveat. Block VI is the main line's, so write it plain the first time.

Then the main line does the only judgment work, off the digest alone:

1. Write `work/<date>/frag/VI.json`, the leverage line (`line` · `why` · `plain` · `strand`), in the shape of `prev/VI.json`.
2. Write `work/<date>/meta.patch.json`: `when` · `trigger` · `countersign` · `main_effort` · `stats` · `build.calls`/`rounds`. Write `stats` as a **list of "label: value" strings**, never a dict (a dict blanked the board twice on 10/4; assemble.py now coerces it). Stats cover blocked count, main-effort idle days, agents deployed, anything measured. Anything not in the patch keeps prep's value.
3. Rebuild Block III by default (BOLO 86, provisional 10/12). Prep flags it every run. Edit `frag/III.json` against PROJECTS.md. Block VII's prowords refresh from the register.

## H3 · Build, flush, publish

```
python _tools/sitrep/assemble.py <date> --build --flush
```

It writes `boards/<date>.json` and builds `SITREP.html` plus the fragment (path printed). The flush then moves every cache note except the newest into `_LOG/` (SOP §3; BOLO 86 ruled 10/12: one note stays). Publish the fragment with the Artifact tool to the standing URL:

```
https://claude.ai/code/artifact/aebe5f9c-9f2c-4cb8-abbf-714a0a6ea28a
```

Pass it as `url`. Never `read` the artifact first, because a read dumps the page into context.

The chat reply, ruled 10/6, runs in this order:
- **Left off**: one sentence.
- **Start next: BOLO N**: one row, a five-word why.
- The link.
- Block 0 in three bullets.
- The leverage line.
- One caveat line, only if the reviewer left advisory findings.

No preamble, no questions, no re-derivation of what the specialists wrote. If a fragment is wrong, rerun that one specialist with the finding pasted under its brief. Never launch a checker agent.
