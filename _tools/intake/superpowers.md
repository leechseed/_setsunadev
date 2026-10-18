# Superpowers: framework read (10/17)

Sources: [repo](https://github.com/obra/superpowers) and `https://raw.githubusercontent.com/obra/superpowers/main/skills/<name>/SKILL.md`, cited as [sdd](https://raw.githubusercontent.com/obra/superpowers/main/skills/subagent-driven-development/SKILL.md), [ws](https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-skills/SKILL.md), [wp](https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-plans/SKILL.md), [bs](https://raw.githubusercontent.com/obra/superpowers/main/skills/brainstorming/SKILL.md), [ep](https://raw.githubusercontent.com/obra/superpowers/main/skills/executing-plans/SKILL.md), [dpa](https://raw.githubusercontent.com/obra/superpowers/main/skills/dispatching-parallel-agents/SKILL.md). Our figures come from DVA's assessment.

## What it is

- A development method for coding agents, built from composable skills ([repo](https://github.com/obra/superpowers)).
- MIT licensed, with plugin manifests for Claude Code and other harnesses ([repo](https://github.com/obra/superpowers)).
- Skills trigger by context and are called "mandatory workflows" ([repo](https://github.com/obra/superpowers)).
- The chain: brainstorming, worktrees, writing-plans, subagent-driven or inline execution, review, finish ([repo](https://github.com/obra/superpowers)).
- It holds 15 skills, including writing-skills and dispatching-parallel-agents ([repo](https://github.com/obra/superpowers)).

## Conventions

| Convention | Superpowers | The Command now | Verdict |
|---|---|---|---|
| Layout | One folder per skill, `SKILL.md` required, extras past ~100 lines ([ws](https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-skills/SKILL.md)) | Same | Adopt |
| Description | "Use when...", triggers only, never the workflow, under 500 characters ([ws](https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-skills/SKILL.md)) | Ours carry workflow and proword | Adapt: keep proword, cut workflow |
| Trigger | Automatic by context ([repo](https://github.com/obra/superpowers)) | Prowords only | Skip |
| Names | Letters, numbers, hyphens; verb-first ([ws](https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-skills/SKILL.md)) | Short nouns | Adapt for new files only |
| Testing a skill | Run pressure scenarios without the skill first ([ws](https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-skills/SKILL.md)) | skill-builder names test prompts | Adopt |
| Brief | Brief file path, one line of fit, report-file path ([sdd](https://raw.githubusercontent.com/obra/superpowers/main/skills/subagent-driven-development/SKILL.md)) | SOP 1.24: paths | Adopt, add report file |
| Return | Full report to a file; reply is status plus one line ([sdd](https://raw.githubusercontent.com/obra/superpowers/main/skills/subagent-driven-development/SKILL.md)) | Free-form | Adopt |
| Status codes | DONE, DONE_WITH_CONCERNS, NEEDS_CONTEXT, BLOCKED ([sdd](https://raw.githubusercontent.com/obra/superpowers/main/skills/subagent-driven-development/SKILL.md)) | None | Adopt |
| Model | Always set explicitly; cheapest for mechanical work ([sdd](https://raw.githubusercontent.com/obra/superpowers/main/skills/subagent-driven-development/SKILL.md)) | Floats | Adopt in frontmatter |
| Ledger | Each ruling: decision, why, cost if wrong ([sdd](https://raw.githubusercontent.com/obra/superpowers/main/skills/subagent-driven-development/SKILL.md)) | STATE, cache notes | Adapt |
| Parallel | One agent per independent domain ([dpa](https://raw.githubusercontent.com/obra/superpowers/main/skills/dispatching-parallel-agents/SKILL.md)) | Disjoint inputs | Adopt (ours already) |
| Plans | Global Constraints, Interfaces per task, proportion check ([wp](https://raw.githubusercontent.com/obra/superpowers/main/skills/writing-plans/SKILL.md)) | DOPE SHEET | Adapt: add Interfaces |
| Worktrees, TDD | Isolated branch, test first ([ep](https://raw.githubusercontent.com/obra/superpowers/main/skills/executing-plans/SKILL.md)) | Autocommit; mostly scripts | Skip |

## Conflicts with doctrine

1. **Reviewer per task.** A task reviewer follows every task ([sdd](https://raw.githubusercontent.com/obra/superpowers/main/skills/subagent-driven-development/SKILL.md)). We allow one script reviewer at the fan-in. Adapt: turn its checklist into a RANGE script check.
2. **Whole-branch reviewer on the top model** ([ep](https://raw.githubusercontent.com/obra/superpowers/main/skills/executing-plans/SKILL.md)). Adapt: RANGE runs at the fan-in; the CDR rules.
3. **Builder-check subagent** reads the design ([bs](https://raw.githubusercontent.com/obra/superpowers/main/skills/brainstorming/SKILL.md)). That is a checker agent. Adapt: the CDR reads it as the builder, which the skill allows without a subagent tool.
4. **Five-round fix loop** ([sdd](https://raw.githubusercontent.com/obra/superpowers/main/skills/subagent-driven-development/SKILL.md)). Adapt: one script pass, one fix.
5. **"You MUST use this" auto-trigger** ([bs](https://raw.githubusercontent.com/obra/superpowers/main/skills/brainstorming/SKILL.md)). Adapt: prowords only.
6. **No parallel implementers** ([sdd](https://raw.githubusercontent.com/obra/superpowers/main/skills/subagent-driven-development/SKILL.md)). Adapt: keep ours; disjoint inputs allow parallel.
7. **Workers never spawn subagents** ([sdd](https://raw.githubusercontent.com/obra/superpowers/main/skills/subagent-driven-development/SKILL.md)). Our `collect-lead` does. Adapt: keep it; it only launches briefed PS seats.

## Naming plan

DVA found 947 of 953 deployments were `general-purpose`. Only RACK, WATCH, INDEX and NOTE carried labels. The first four rows are DVA's rack; the rest come from agent files that never fired.

| Family | Name | Trigger | Model | Borrows from |
|---|---|---|---|---|
| RACK (43 runs) | agent `drafting-rack-block` | sit rep | haiku | sdd brief and report file |
| WATCH (36) | agent `drafting-watch-block` | sit rep | haiku | sdd |
| INDEX (34) | agent `drafting-index-blocks` | sit rep | sonnet | sdd |
| NOTE (20) | agent `drafting-session-note` | "Oscar Mike" | haiku | sdd |
| Link harvest | agent `extracting-link-batch` | "collect the locus" | haiku | dpa |
| Scan batches | agents `transcribing-scan`, `filing-scan` | "scan <kind>" | sonnet, haiku | dpa |
| Skill authoring | skill `writing-command-skills` | "build a skill for X" | sonnet | ws |
| Bench seats | skill `convening-bench` over the five `bench-*` agents | "convene the bench" | sonnet | dpa |
| Debugging | skill `tracing-root-cause` over `root-cause` | "why did X break" | sonnet | systematic-debugging |
| Done check | skill `verifying-before-done`, a script | any build close | none | verification-before-completion |

That names ten families. Existing files keep their names.

## First three moves

1. **Put `JOB: <name>` on line one of every brief, plus a report-file and status-code contract.** DVA's M1. Effort S.
2. **Write the four ritual agents** with the model in frontmatter. Switch sit rep and Oscar Mike to launch them by name. DVA's M2. Effort M.
3. **Write `verifying-before-done` as a script check** and trim skill descriptions to triggers. Effort M.
