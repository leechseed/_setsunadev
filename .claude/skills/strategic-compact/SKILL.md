---
name: strategic-compact
description: Decides whether now is a good moment to run /compact. Fires on "compact check" or "should we compact". Judges by task phase, makes sure the state is written to a file first, then tells Chief what to type.
---

# Strategic Compact

Compacting at a task boundary keeps what matters. Compacting mid-task loses file names and half-done state. Chief decides; this skill only gives the call.

## Steps

1. Name the phase we are in (research, plan, build, test, debug, between jobs).
2. Look it up:

| Moment | Compact? | Why |
| --- | --- | --- |
| Research done, plan written | Yes | Research is bulky; the plan is the output |
| Plan written, about to build | Yes | Frees room for code |
| Build done, tests next | Maybe | Keep if tests touch the fresh code |
| Debugging done, new job next | Yes | Debug traces pollute the next job |
| Mid-build | No | Variable names and partial state are lost |
| A failed approach just ended | Yes | Drop the dead-end reasoning |
| A detached run is in flight (pull waves) | Only if its state is in a file | Note the running script names first |

3. Before a "yes": make sure anything not yet on disk is written down. A compact keeps CLAUDE.md, files, memory and git. It loses intermediate reasoning, file contents read earlier, and preferences Chief only said aloud. Offer the Oscar Mike note, or a short cache note in `_setsunadev/_CACHE/`, if the work is not yet saved. Do not assume a task list survives; write a file.
4. Reply: one line of verdict, one line of why, then the command to type, with a focus hint: `/compact focus on <next job>`. A skill cannot run `/compact` itself.

For a live number, send him to `/context` (see the context-budget skill). Do not estimate tokens from tool counts.

## Dropped from the original

- The `suggest-compact.js` PreToolUse hook, its settings.json block, and every env variable (COMPACT_*, ECC_CONTEXT_WINDOW_TOKENS).
- The "token-optimizer" and "context-mode" tool recommendations (outside installs).
- Trigger-table and duplicate-instruction sections (we already load skills on demand).

<!-- adapted from ECC skills/strategic-compact (MIT, github.com/affaan-m/ECC), 2026-10-12 -->
