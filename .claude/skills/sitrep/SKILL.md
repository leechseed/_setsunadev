---
name: sitrep
description: Deliver the sit rep (the board + the SITREP page) in the formation ruled 2026-09-12 (BOLO 54) — a zero-token prep script, three independent specialists at gear 1, a script reviewer at the fan-in, the main line writing only Block VI and the header. Fires on "sit rep", "the board", "where did we leave off", "what are we working on", or the countersign.
---

# The sit rep — the formation

**The rule (BOLO 54):** orchestrator decomposes, specialists run independently on disjoint inputs, sync only at named handoffs, one reviewer at the fan-in. The main line never reads the five files. Coordination is the serial part; there is none mid-run.

Canonical protocol: SOP.md §1 (the command) · §2 (the blocks) · §3 (the flush). This skill is the procedure.

## H0 · Prep (zero tokens)

```
python _tools/sitrep/prep.py
```

Prints a 20-line digest and writes `_tools/sitrep/work/<date>/`: the previous board split per block (`prev/`), STATE sliced to Blocked + Live, the git log since the last board, `meta.json` (box probe · tree · rack · sizes), Blocks III and VII carried forward (`frag/`), and three briefs. Read the digest only. Do not open STATE, BOLO, SOP, PROJECTS or the cache notes.

## H1 · Fan out (one message, three agents, gear 1)

Launch all three in the same message, `run_in_background: false` is not needed; wait for all. Each prompt is the brief file's contents verbatim (Read it, paste it). No agent reads another's input or output.

| Role | Model | Reads | Writes |
|---|---|---|---|
| **RACK** | haiku | `_CACHE/*.session.md` + `prev/0.json` | `frag/0.json` (Block 0) |
| **INDEX** | sonnet | `state.blocked.md` · `state.live.md` · `git.log` + `prev/{I,II,V}.json` | `frag/I.json` · `frag/II.json` · `frag/V.json` |
| **WATCH** | haiku | `BOLO.md` + `prev/IV.json` | `frag/IV.json` (Block IV + pmcs) |

Model rule is the gearbox's (SOP §1): extraction on haiku, write-ups on sonnet, Fable on the main line only. A gear shift never adds a fourth specialist to the sit rep; it is not a bigger job.

## H2 · Fan in (the reviewer is a script)

```
python _tools/sitrep/assemble.py <date>
```

Runs the reviewer's checklist (eight blocks in order · text + trunk on every item · trunk values legal · every `[[key]]` in glossary.json · every BOLO number in Block IV real and placed once · Block V rows = the Blocked table · plain + strand complete · no stale fragment) and prints the digest: per-block counts against the previous board, first line of each, findings. Blocking findings (a missing fragment, an unknown glossary key) stop the write; fix the one fragment, rerun. Advisory findings go into the reply's one-line caveat, not into a re-run.

Then the main line does the only judgment work in the run, off the digest alone:

1. Write `work/<date>/frag/VI.json` — the leverage line (`line` · `why` · `plain` · `strand`), same shape as `prev/VI.json`.
2. Write `work/<date>/meta.patch.json` — `when` · `trigger` · `countersign` · `main_effort` · `stats` (blocked count · main-effort idle days · agents in flight · anything measured) · `build.calls`/`rounds`. Anything not in the patch keeps prep's value.
3. If prep flagged III (PROJECTS.md moved), edit `frag/III.json` by hand; otherwise leave it.

## H3 · Build, flush, publish

```
python _tools/sitrep/assemble.py <date> --build --flush
```

Writes `boards/<date>.json`, builds `SITREP.html` + the fragment (path printed), then moves every cache note except today's into `_LOG/` (the flush, SOP §3; an empty rack is the proof). Publish the fragment with the Artifact tool to the standing URL:

```
https://claude.ai/code/artifact/aebe5f9c-9f2c-4cb8-abbf-714a0a6ea28a
```

Pass it as `url`; never `read` the artifact first (a read dumps the page into context). The chat reply carries the link, Block 0 in three bullets, the leverage line, and one caveat line if the reviewer left advisory findings. No preamble, no questions, no re-derivation of what the specialists wrote.

## Cost shape (why this order)

- Before: the main line read ~211 KB (about 55k tokens) and wrote the whole 27 KB board on Fable, then carried all of it in context for the rest of the session.
- Now: the main line reads two digests (~3 KB) and writes ~1 KB. The 211 KB is read once, by two haiku and one sonnet context that end when they return. Sync points: four (H0–H3), none of them agent-to-agent.
- If a fragment is wrong, rerun that one specialist with the finding pasted under its brief. Never launch a "checker" agent; the checklist is the checker.
