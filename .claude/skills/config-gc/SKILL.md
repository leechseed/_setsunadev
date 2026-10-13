---
name: config-gc
description: Config cleanup audit. Fires ONLY when Chief names it, on "config GC" or "clean the config". Never run it on its own, never scan the box unasked. Audits the repo's .claude config, then asks Chief about each deletion one at a time. Never deletes on its own.
---

# Config GC

Configs only grow. This skill finds dead weight and proposes cleanup. **Chief must name it. Do not offer it, do not start it from another task.** Scope is the repo's `.claude/` folder and the memory folder Chief points to. Not the home folder, logs, caches, processes or network (no-probing rule).

## Rules

- One item, one question: "Remove X? Evidence: Y. [y/n/skip]". No "yes to all". Chief may stop at any point.
- Never delete on your own. Soft-delete only: rename a skill folder to `<name>.disabled`, or move a file to `.claude/_gc_trash/<date>/`. Hard delete only when Chief says so in words.
- Do not edit `settings.local.json`, hooks, or CLAUDE.md without Chief confirming that exact edit. Copy the file to `.bak` first and write the removed text into the log.
- Age is a hint, not a verdict. A skill unused for 60 days may be seasonal.
- Memory: never fix by truncation. If two entries conflict, read both and keep the newer truth, with Chief's okay.

## Steps

1. Ask which channels (skills, memory index, hooks, permissions) unless he named them.
2. Scan read-only with Grep, Read, Bash `ls`/`wc`:
   - Skills: empty or broken SKILL.md, overlapping triggers.
   - Memory: index lines pointing to missing files, files missing from the index, contradictions, passed dates.
   - Hooks: scripts in `_tools/hooks/` that no hook in `settings.local.json` references (grep each name).
   - Permissions: duplicate entries, or ones a wildcard already covers.
3. Rank by confidence (broken or orphaned first). Cap at 20 candidates. Show a numbered table: path, signal, size.
4. Ask each one by one. Soft-delete the yeses.
5. Append a line per action to `.claude/gc_log.md`: time, item, where it went, how to undo.
6. Report what moved and a suggested next review date.

## Dropped from the original

- Scanning `~/.claude` as a whole (projects, file-history, shell-snapshots, caches, scheduled jobs, `~/.claude.json` MCP list): this is machine probing.
- The jq edit one-liners for settings files, and the cache-size sweep.
- Related-skill links to skills we do not have.

<!-- adapted from ECC skills/config-gc (MIT, github.com/affaan-m/ECC), 2026-10-12 -->
