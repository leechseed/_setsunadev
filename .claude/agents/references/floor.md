# The floor: rules that never lower the bar

Used by `python-reviewer`. The floor is what a diff may never do to get to green. A reviewer checks the diff against it and reports each hit as a blocker. `_tools/review/touchstone_check.py` checks Touchstone ids in the SSOT only, so it is not the home for these; this file is the list.

## The rules

1. **No new suppressions.** A diff adds no `# noqa`, `# type: ignore`, `# pragma: no cover` or `# nosec`, and no blanket `except:` or `except Exception: pass` that turns a failure into silence.
2. **No skipped checks.** No smoke command, lint step or review step removed from a script, skill or hook to make it pass; no `--no-verify`; no early `sys.exit(0)` ahead of a check.
3. **No secrets.** No key, token, password or private-detail text in a tracked file. Private detail stays in `_PRIVATE/`.
4. **The checker is never weakened.** A diff to a checker (`touchstone_check.py`, `lint.py`, `sop_audit.py`, `prose_lint.py`, a threshold, an allowlist or an EXAMPLES entry) that loosens it is a blocker unless Chief ruled it. Tightening is fine and stays silent; loosening is loud.
5. **No unfinished stand-ins.** No stub that raises "not implemented", and no TODO sitting where the code should be (SOP 7.25).

## How to check

`git diff -- '*.py' '*.md'` and grep the added lines (those starting with `+`) for the patterns above. Report file:line and the rule number. Do not run installers.

<!-- source: addyosmani/agent-skills skills/constraint-driven-development, the Floor and guard sections (MIT, github.com/addyosmani/agent-skills), adopted 2026-10-13 under BOLO 140; CONSTRAINTS.md file, tool installs (tsc, biome, gitleaks, semgrep and the rest) and lifecycle wiring cut -->
