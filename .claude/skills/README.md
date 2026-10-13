# Skills

A skill is a procedure Claude loads when Chief says its proword. Each lives in `<name>/SKILL.md`; the frontmatter `description` carries every trigger. The Steering column points at the skill's `references/` folder (rulings, history, past slips) where one exists. Lint: `python -X utf8 _tools/skills/lint.py`.

| Skill | Triggers (Chief says) | One line | Steering |
|---|---|---|---|
| [bench](bench/SKILL.md) | "convene the bench", "bench this" | Five-seat advisory Bench opines on one question | none |
| [brainstorm](brainstorm/SKILL.md) | "brainstorm X", "riff on X" | One question at a time until "lock it", then a short brief | none |
| [collect](collect/SKILL.md) | "collect <locus>", "pull every link in ...", "build the register from the harvest" | Link-harvest formation: script fetch, PS extract, MS register, script proof | none |
| [config-gc](config-gc/SKILL.md) | "config GC", "clean the config" | Audits .claude config, asks before each deletion | none |
| [context-budget](context-budget/SKILL.md) | "context budget", "what's eating the context" | Points to /context, audits always-loaded files on request | none |
| [dope-sheet](dope-sheet/SKILL.md) | "DOPE SHEET N", "the dope on N", "build the sheet for N" | Builds BOLO N's standing status page | none |
| [frago](frago/SKILL.md) | "FRAGO N", "update the sheet for N" | Pushes a ~1 KB patch onto DOPE SHEET N | none |
| [intake](intake/SKILL.md) | "intake" plus GitHub links | Scans repos, specialists judge, Chief keeps or skips on a glass page | none |
| [launch](launch/SKILL.md) | "go for launch", "launch sequence" | Brings stations up, opens boards, runs the sit rep | [launch/references/](launch/references/history.md) |
| [oscar-mike](oscar-mike/SKILL.md) | "Oscar Mike" | The close-out: note, STATE, journal, OUT block | none |
| [rtb](rtb/SKILL.md) | "RTB", "clear the cards" | Clears open oscar-mike cards, one disposition each | none |
| [safety-guard](safety-guard/SKILL.md) | "freeze", "safety guard" | No edits to running scripts, no kills, without Chief's word | none |
| [sitrep](sitrep/SKILL.md) | "sit rep", "the board", "where did we leave off" | The board plus the SITREP page | [sitrep/references/](sitrep/references/history.md) |
| [strategic-compact](strategic-compact/SKILL.md) | "compact check", "should we compact" | Judges whether now is a good moment to /compact | none |

To test a skill before shipping it: `python _tools/skills/baseline.py <name>`.
