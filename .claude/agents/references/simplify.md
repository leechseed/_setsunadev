# Simplify: guard rules for cleanups

Used by `refactor-cleaner`. Simplify means easier to read with the same behavior. Fewer lines is not the goal.

## The five rules

1. **Preserve behavior exactly.** Same output for every input, same error behavior, same side effects and order. If you are not sure a change preserves behavior, do not make it.
2. **Follow the project's conventions.** Match neighboring scripts (naming, error handling, how they open files). A change that breaks consistency is churn.
3. **Clarity over cleverness.** A nested conditional chain becomes a plain if/elif or a lookup table; a dense one-liner gets a named step.
4. **Keep the balance.** Do not inline a helper that gave a concept its name, merge two simple functions into one complex one, or strip an abstraction that exists on purpose.
5. **Scope to what changed.** Simplify the code the brief names. No drive-by cleanups elsewhere unless the brief widens the scope.

## Chesterton's fence

Before changing or removing anything, answer: what is its job, what calls it, what are its edge cases and error paths, and why might it be written this way (a platform quirk, a Windows path rule, a fix from an old bug)? Check `git log -S name` or blame for the original context. If you cannot answer, read more or leave it and list it for the CDR.

## Signals worth a look

Nesting three or more levels deep (use guard clauses) · functions over 50 lines with several jobs · repeated identical conditions (extract a named predicate) · generic names like `data`, `tmp`, `val` · comments that say what, not why (cut those; keep the why comments) · dead code and unused names (after confirming they are dead) · wrappers that add nothing.

## Process

One simplification at a time. After each, compile (`python -m py_compile`) and run the brief's smoke command. If it fails, revert it and reconsider. Do not batch several untested changes. Keep refactors apart from fixes and features.

## Red flags

A change that needs the smoke command altered to pass (you changed behavior) · "simplified" code that is longer or harder to follow · error handling removed because it "looks cleaner" · simplifying code you do not understand · renaming to personal taste.

<!-- source: addyosmani/agent-skills skills/code-simplification (MIT, github.com/addyosmani/agent-skills), adopted 2026-10-13 under BOLO 140; TypeScript and React sections, test-suite and PR steps cut -->
