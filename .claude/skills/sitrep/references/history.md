# Sit rep history

Read this only when you need the record. The procedure lives in ../SKILL.md.

## H0.5 · BREVITY picks — RETIRED 2026-10-04

**Retired (Chief, 10/4: "eliminate the brevity panel … it's just taking up space now"):** the panel is gone from the board; skip this step. The text below is kept as the record.

The board carries the BREVITY panel (BOLO 37, ruled 9/23): Chief's proword picks land in the page's store. Before the fan-out, `ArtifactData` action `list`, collection `picks`, on the standing URL; if any documents come back, save them to `<scratchpad>/picks.json` and run `python _tools/soi/brevity.py apply <scratchpad>/picks.json`, then add the SOI entry and the SOP §5 line the script prints for each ruled slot. The build reads `_tools/soi/benches.json` and the ruled slots show as ruled on the next board. The publish carries `capabilities: {db: {}}` once (omit on later publishes; the declaration persists).

## Alternative path (BOLO 68, provisional 10/12, untested)

[.claude/workflows/sitrep.js](../../../workflows/sitrep.js) runs H0 to H2 as a Workflow script. The skill stays the canonical procedure.

## Measured numbers

- Auto-rerun, measured 10/4: the first pass carried 19 long sentences forward; one rerun took the board to 2.

## Cost shape (why this order)

- Before: the main line read ~211 KB (about 55k tokens) and wrote the whole 27 KB board on Fable, then carried all of it in context for the rest of the session.
- Now: the main line reads two digests (~3 KB) and writes ~1 KB. The 211 KB is read once, by two haiku and one sonnet context that end when they return. Sync points: four (H0–H3), none of them agent-to-agent.
- If a fragment is wrong, rerun that one specialist with the finding pasted under its brief. Never launch a "checker" agent; the checklist is the checker.
