# Planning: the spec, the plan, the slice

Used by `planner`. Three shapes, in order: spec, plan, slice. Stop after each one and wait for Chief's word; "go" is the order, not the build-out (SOP §1.23).

## 1. The spec shape

Write the spec before any build. List assumptions first ("ASSUMPTIONS I AM MAKING: 1... Correct me now or I proceed") and never fill an ambiguous requirement silently.

```markdown
# Spec: [name]
## Objective        (what, why, who it is for, what done looks like)
## Commands         (full runnable commands with flags)
## Structure        (which folders and files are touched)
## Boundaries       (Always: ... / Ask first: ... / Never: ...)
## Success criteria (specific, checkable conditions)
## Open questions   (each with a rec)
```

- Turn a vague ask into a checkable condition: "make it faster" becomes "the run finishes in under N seconds on this input", and ask whether N is right.
- The Command has no test suite, so "Commands" holds the compile, `--help` or smoke command that proves the work.
- Skip tech stack and test strategy sections; they do not fit `_tools/`.
- Save the spec to the file the brief names, summarize it, list the open questions, then stop. Do not start the plan in the same turn.

## 2. The plan shape

- Map what depends on what, then build foundations first.
- Slice vertically: each task delivers one working path (input, logic, output), not "all the parsing, then all the output".
- Phases, each with a verification and a checkpoint:

```markdown
# Plan: [name]
## Overview
### Phase 1: [smallest slice with value]
- [ ] Task: [what] / Acceptance: [true when done] / Verify: [command and expected result] / Files: [paths]
#### Checkpoint: [what works end to end; Chief reviews before phase 2]
### Phase 2: ...
## Risks (risk, impact, mitigation)
## Open questions
```

- Put the riskiest task early so it fails early.
- Checkpoint after every two or three tasks.
- Size tasks by files touched: 1 file small, 3 to 5 medium. Eight or more files, or a task title with "and" in it, gets split.
- Do not overwrite a plan file that still has unchecked tasks for different work; stop and ask.

## 3. The incremental rule

One working slice at a time. Implement the smallest complete piece, run its verification, then move to the next. Never leave a script broken between slices.

- **Simplest first.** Do the obvious version before any abstraction. Three similar lines beat a premature helper.
- **Scope discipline.** Touch only what the task requires. Do not tidy adjacent code, fix unrelated imports or add features that "seem useful". Write "NOTICED BUT NOT TOUCHING: ..." and let Chief decide.
- **One thing per slice.** Do not mix a refactor, a feature and a config change.
- **Safe defaults and easy undo.** New behavior is off or conservative by default; each slice reverts alone. Do not delete and replace in the same step.
- Over about 100 lines written without running anything is the red flag. Run the check, then continue.

<!-- source: addyosmani/agent-skills skills/spec-driven-development, planning-and-task-breakdown, incremental-implementation (MIT, github.com/addyosmani/agent-skills), adopted 2026-10-13 under BOLO 140; gated-turn rules reduced to "stop after each shape"; /build and commit steps, tracker and test-framework sections cut -->
