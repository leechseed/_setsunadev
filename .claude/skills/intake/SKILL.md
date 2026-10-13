---
name: intake
description: The repo intake (BOLO 140). Fires on "intake" followed by one or more GitHub links, or "run the intake on these repos". A script scans each repo, specialists judge what it could add to the Command, and Chief keeps or skips each pick on a glass page. Never installs anything on its own.
---

# The repo intake — BOLO 140

**Why (Chief 10/12):** "I have a whole bunch of GitHub repos ... adding them to our process ... tools so you have to think less." Every repo goes through the same four steps, so each one costs the same small, known amount and nothing gets installed blind.

**Steps (BOLO 64):** RECON = the scan script · ORDER = one brief per repo · EXECUTE = specialists, one repo each · CONSOLIDATE = the picker glass and Chief's picks.

## 1 · Scan (zero tokens)

```
python _tools/intake/repo_scan.py <url> [<url> ...]
```

Writes `_PRIVATE/intake-repos/<owner>__<repo>/scan.json` (stars, license, last push, file tree, counts of agents / skills / commands / hooks / MCP configs / installers) and `README.md`. Read the one-line summaries only.

**Gates before any specialist runs:**
- No license, or a license that bars reuse: **stop**, report it.
- Archived, or no push in 12+ months: flag it as stale.
- Mostly Node/JS with installers: anything taken is hand-copied text, never the installer.

## 2 · Judge (one specialist per repo, in parallel)

Launch one MS (sonnet) per repo in one message. Each brief, verbatim plus the repo path:

> Read `_PRIVATE/intake-repos/<owner>__<repo>/scan.json` and `README.md`, then fetch and read in full any file you recommend (raw.githubusercontent.com). Compare against what the Command already has: `.claude/agents/README.md`, the skill list in `.claude/skills/`, the hooks in `.claude/settings.local.json`, and `_tools/` (names only). Write `_PRIVATE/intake-repos/<owner>__<repo>/picks.json`: a list of `{id, kind (agent|skill|command|hook|script|idea), plain (one plain sentence: what it does for us), rec (yes|maybe|no), why (one line), replaces (our seat, skill or tool it would replace, or "none"), source (path or URL), risk (hooks, installers, network calls, telemetry, license: one line or "none")}`. Rules: our formation (no checker agents, a script reviews), least tools, no auto-triggers, no machine scanning unasked, no Node installers, private detail stays private. Reply in under 120 words.

**RANGE (script):** every `picks.json` parses, every row has the fields, every `yes` names a `source`.

## 3 · Pick (the glass)

Build the picker from all `picks.json` files with the roster-picker template (`_PRIVATE/ecc/roster_picker.tpl.html`, Keep / Skip, "replaces or joins as", Take all recs), publish with `capabilities: {db: {}}`, add it to `_tools/pages/pages.json` as `intake-<date>`, and open it. Chief picks.

## 4 · Adopt

Read the picks back (`ArtifactData list picks`). For each kept item, adapt it the BOLO 139 way: read in full, strip hooks / installers / auto-triggers / outside calls, add the Command rules block to agents, least tools, write it into `.claude/agents/`, `.claude/skills/` or `_tools/`. Rebuild the Roster (`python _tools/roster/build.py`) when agents changed. Log the adoption on BOLO 140, the source repo and license in a comment line at the bottom of each adopted file.

**Never:** run a repo's installer or plugin, add its hooks, or wire an MCP server without Chief naming it.

The scanner may consult `_tools/intake/known_skills.json` (name, url, license for 2,687 skills from sickn33/agentic-awesome-skills `skills_index.json`; a lookup list, not an install list).
