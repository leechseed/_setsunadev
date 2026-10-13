---
name: context-budget
description: Answers "what's eating the context" without scanning the box. Fires on "context budget" or "what's eating the context". Points Chief to the live /context meter, then reads only the repo's always-loaded files if he asks for the audit.
---

# Context Budget

Chief wants to know where the tokens go. Two paths. Default is the first.

## 1. Live check (default)

- Use no tools. Read no files. Run no commands.
- Reply in two lines: "Type `/context` for the live breakdown (`/context all` for every item)." A skill cannot press that command for him.
- Never guess a number from a scan. Never answer "how much is left" with an estimate.

## 2. Repo audit (only if Chief says "audit", "break it down" or similar)

Read-only, repo only. Do not walk the home folder, logs, transcripts, caches or processes (the no-probing rule).

1. Check the byte size of the always-loaded files with Bash `wc -c`: `CLAUDE.md`, the digest the SessionStart hook prints (read the hook's script, do not run it), and the memory index `MEMORY.md`.
2. List `.claude/skills/*/SKILL.md` and read only each `description:` line. Descriptions load eagerly. Bodies load on demand, so report body size separately.
3. Report: file, bytes, rough tokens (bytes / 4, labeled "estimate"). Top 3 heaviest. Up to 3 trims.
4. Known drain: session open measured at about 211 KB. Say which file is the biggest share of it.
5. Close with: "Estimates of static load, not live usage. `/context` is the real number."

## Dropped from the original

- The Codex routing table (we run Claude Code only).
- The Python JSONL transcript counter (it reads the saved transcript; probing).
- Any MCP or CLI launch to count tools.

<!-- adapted from ECC skills/context-budget (MIT, github.com/affaan-m/ECC), 2026-10-12 -->
