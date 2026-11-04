---
name: kickoff
description: 'Use when Chief starts a project or a new effort: "kick off X", "kickoff X", "new project X", "start the X project", "start a new X", "let''s start on X", or an ORDER HINT that reads kickoff. Pulls the project agents (planning-project, mapping-sources, tagging-fabula, drafting-call-sheet) in order, every method sourced from the library. Not for a single small task, and not for a tooling plan (that goes to architect).'
---

# KICKOFF X — starting a project with the project agents

**Ruled 11/4 (Chief):** "pull agents for this" · "pull methodology from the ivory tower of books that we have; we must make sure there is sourced nature to all this" · "build the whole stack". This skill is how every new project starts.

**Steps (BOLO 64):** RECON = read the project's BOLO row and newest note · ORDER = the readback with the agent plan and an ETA · EXECUTE = the agents below, hub and spoke · CONSOLIDATE = the plan and the call sheet on a page, then wait for Chief's calls.

The CDR (main session) runs this skill. Subagents cannot launch agents, so no agent runs it.

## 0 · Recon (zero tokens where possible)
- Find the project's BOLO row (`grep -n "^| N |" BOLO.md`); open one if none exists (BOLO capture rule).
- Work folder: `_tools/bolostatus/work/<slug>/` (public, generic lines only); private material goes to `_PRIVATE/<slug>/`.
- Write the term list: every name the project has gone by (memory notes on renames, lineage, garbles). The OXO list is the model: OXO · Outliers · DCUS · Delta Coast · Inner Spiral · Red Hills · Skeeter Creek · Red Stick · Ariel · the cast names.
- Write `brief.COMMON.md` in the work folder from `_tools/bolostatus/work/oxo-start/briefs/brief.COMMON.md`: keep the library and sourcing sections, swap in the rulings on this project's topic (writer briefs carry rulings).

## 1 · Plan — `planning-project` (sonnet, 1 seat)
Brief: `JOB: planning-project`, the project, the work folder, the inputs (BOLO row, newest note, the project's key docs). Out: `plan.json` + `plan.md`. Read `plan.md`; the plan's phases drive steps 2–4, and its decision points seed the call sheet.

## 2 · Map — `mapping-sources` (haiku, up to 3 seats on disjoint folders)
Split the repo by folder so no two seats overlap (canon side · `_PRIVATE` and paper · old notes and archives is the proven split). Each seat gets the term list and writes `sources.<seat>.json`. Fan-in: merge the seats into `source-map.md` (the one reviewer is a script: every row has `evidence`, ids parse; no checker agent).

## 3 · Tag — `tagging-fabula` (haiku, story projects only)
Batches from the source map's story rows. Out: `tags.<batch>.json`. A script applies the tags; the agent never edits a story file. Conflicts (one event in two eras) go to the call sheet. Skip this step for non-story projects.

## 4 · Calls — `drafting-call-sheet` (sonnet, 1 seat)
Inputs: `plan.json` decision points, `source-map.md` loose ends, tag conflicts, the standing rulings. Out: `calls.json` + `calls.md`: 6–8 calls, a rec each, evidence and the book behind each rec. Calls a ruling already answers are dropped and the ruling quoted.

## 5 · Consolidate
- Publish the call sheet as cards (Call Sheet format, SP-001) beside the chat; "go" takes every rec.
- Log the agents fired and the files written on the BOLO row; FRAGO the DOPE SHEET if one exists.
- Then stop. "Go" is the order, not the build-out: the next phase waits for Chief's calls.

## Rules that bite
- Gear: at most 3 agents in flight unless Chief raises it; map seats first, plan in parallel.
- Every agent output carries `file:line` evidence and book ids; `UNSOURCED` is marked, never guessed.
- Research is not fabula (ruled 10/18): nothing the agents write lands in canon until Chief promotes it.
- Private detail stays in `_PRIVATE/`.
- ETA on the readback (SOP §7 rule 11). Measured on OXO 11/4: the map seats take about 2–5 minutes each.
