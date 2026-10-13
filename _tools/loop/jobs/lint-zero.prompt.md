Job: bring the skill lint to zero errors.

Fix ONLY the errors the skill lint reports (lines with "error"; ignore warnings), with the smallest edit possible, in `.claude/skills/**/SKILL.md` or `.claude/agents/*.md`.

Rules:
- Never change what a skill does.
- Never touch the Command rules block.
- Edit no file outside those two locations. Do not commit, delete, or run git commands.
- Do not scan the machine; read only the files the check output names.
- Stop when the lint prints 0 errors (run `python -X utf8 _tools/skills/lint.py` to confirm).
