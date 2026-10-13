# Retire: removing old code safely

Used by `refactor-cleaner`. Code costs upkeep (bugs, drift, mental load); code that no longer earns its keep goes. Never remove first and ask later.

## The decision

1. Does it still do something nothing else does? If yes, keep it.
2. Who or what uses it? Grep the repo, including strings, skills, hooks and `.claude/settings.local.json`. Count the callers.
3. Does a replacement exist? If not, build it first. Do not retire without one.
4. What does moving each caller cost? Cheap and mechanical: do it. Costly: weigh it against keeping the thing.
5. What does keeping it cost (confusion, a second copy of the same job)?

Default to advisory (note it, leave a pointer, migrate at leisure). Go compulsory (remove by a date) only when Chief rules it.

## The steps

1. Build or confirm the replacement and write down how to switch.
2. Mark the old one retired with a one-line pointer to the replacement.
3. Move callers one at a time. After each, compile and run the smoke command. If you own the old thing, you move the callers; do not just announce it.
4. Remove only when a grep shows zero remaining callers. Delete the code, its notes and its config together.
5. Data files are never deleted; report them to the CDR.

Zombie code (no owner, still depended on) gets an owner or a retirement plan, not limbo. Do not add features to a retired thing.

## Red flags

A retirement with no replacement · removing before the zero-callers grep · a swap and a delete in the same step (separate them so each can be undone) · dropping a data field in place instead of adding the new one first, backfilling, then removing the old one in a later step.

<!-- source: addyosmani/agent-skills skills/deprecation-and-migration (MIT, github.com/addyosmani/agent-skills), adopted 2026-10-13 under BOLO 140; traffic-routing, feature-flag and production database sections cut, schema rule kept as one line -->
