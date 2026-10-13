---
name: safety-guard
description: Freeze mode for long detached runs. Fires on "freeze" or "safety guard". While the pull waves or other detached scripts run, no edits to the named running scripts and no killing their processes without Chief's word.
---

# Safety Guard: Freeze

A detached run reads its scripts while it works. An edit mid-run can break it. Killing it loses the wave. This skill is a promise the main session keeps, not a hook.

## On "freeze"

1. Ask Chief (or read from his order) which scripts and processes are running. Write them back as a short bulleted list: the **frozen list**. Example: `pull_queue.py`, the wave launcher, its worker process.
2. Say "Frozen: <list>. Say unfreeze to lift it."

## While frozen

- No Edit, Write, rename, move or delete on any file in the frozen list. Reading is fine.
- No kill, stop, restart or relaunch of their processes (`taskkill`, `Stop-Process`, `kill`, a second launch of the same script).
- Need a change to a frozen file? Write the patch to a new file beside it or in the reply, and ask Chief. Apply it only after he says so.
- Agents and subagents spawned in this session get the same list in their brief.
- Do not look up what is running by scanning the machine. Use only what Chief names or what the run's own status file shows.

## On "unfreeze"

Say "Lifted: <list>" and drop the list. If the session compacts or closes while frozen, put the list in the cache note so it carries.

## Dropped from the original

- Careful mode (the watched-command list) and Guard mode (Careful plus Freeze): not requested.
- The directory-lock form (`freeze src/...`) and its PreToolUse hooks on Bash/Write/Edit.
- The block log at `~/.claude/safety-guard.log`, Codex and ECC 2.0 notes.

<!-- adapted from ECC skills/safety-guard (MIT, github.com/affaan-m/ECC), 2026-10-12 -->
