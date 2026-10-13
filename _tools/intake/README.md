# Intake (BOLO 140)

Chief says "intake" plus GitHub links; the skill is [.claude/skills/intake/SKILL.md](../../.claude/skills/intake/SKILL.md). Nothing is installed; ideas are hand-copied.

How it runs:
1. `repo_scan.py` clones each repo shallow and scans it (license, network calls, auto-trigger skills) into `scan.json`.
2. Specialists read the scan and the README and write `picks.json` (one pick per idea: plain, rec, why, replaces, risk) and `note.md`.
3. `build_report.py` and `build_picker.py` build the glass page where Chief keeps or skips each pick; `digest.py`, `dedupe.py`, `inventory.py`, `enex.py` and `batch.py` support the batch.

Files it writes, per repo, in `_PRIVATE/intake-repos/<owner>__<repo>/`: `scan.json`, `picks.json`, `note.md`.

Idea (cek-005, not built): add `build_report.py --top N`, ranking a large change set by diff size so Chief reads only the top N files; a script is enough, no agent.

Open work: [TODO-next-session.md](TODO-next-session.md).
