# Severity rubric (our words)

Used by python-reviewer and security-reviewer. Rank every finding with one of four words, then give the reason. Idea from the Pragmatic Quality review in OneRedOak/claude-code-workflows (MIT, Patrick Ellis); text is ours. Source: https://raw.githubusercontent.com/OneRedOak/claude-code-workflows/main/code-review/pragmatic-code-review-subagent.md

- **blocker.** Must be fixed before the script runs again: a leak of secrets or private data, data loss, a crash on the main path, or a design that breaks what depends on it.
- **high.** Strong recommendation: a real bug or hole that bites under normal use (swallowed errors, wrong Windows path or encoding, unsafe input handling).
- **medium.** Worth fixing soon: correctness or upkeep risk that needs unusual conditions, or clear mess that will cost time later.
- **low.** Optional polish (naming, style, small tidy-ups). Prefix with "Nit:". Never blocks.

Rule of thumb: if the change leaves the code healthier overall, do not block on imperfection. Report only what you can point to with file:line.
