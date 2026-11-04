# Agent roster

49 specialist agents: 22 adapted from the ECC repo (MIT, github.com/affaan-m/ECC) on 10/12, plus the BOLO 140 intake agents, the five Bench seats and the five Science Department seats (sci-*) (each file names its source and license at the bottom). Seats: haiku = PS (fetch/extract), sonnet = MS (write/review), opus = planning and architecture only. The CDR decides when to call each one.

| Name | Model | Job in plain words | Access |
|---|---|---|---|
| architect | opus | Proposes a design with trade-offs for a new tool or restructure | read-only |
| doc-updater | haiku | Refreshes READMEs and code maps from the actual scripts | writes |
| harness-optimizer | sonnet | Reviews hooks, skills and agent config for reliability and cost; proposes | read-only |
| loop-operator | sonnet | Watches a long run from its logs, spots stalls, recommends pause or resume | read-only (Bash read-only) |
| opensource-sanitizer | sonnet | Independent pre-release audit: secrets, personal data, binaries, history | read-only (Bash read-only) |
| order-parser | haiku | Turns a garbled dictation line into a clean order (proword, BOLO, verb, object, confidence); never acts | read-only |
| python-reviewer | sonnet | Reviews Python for security, error handling, Windows pitfalls, style | read-only (Bash read-only) |
| root-cause | sonnet | Traces a bug to its root cause with an evidence chain before any fix is proposed | read-only (Bash read-only) |
| security-reviewer | sonnet | Finds leaked secrets, private data in public files, injection risks | read-only (Bash read-only) |
| skill-builder | sonnet | Drafts or trims one skill or agent file to the Anthropic skill patterns; names test prompts | writes (one named file) |
| skill-optimizer | sonnet | Reads one transcript and one skill, finds where the skill misfired or dragged, proposes the smallest edit | read-only |
| collect-lead | sonnet | Depth-2 lead for one collect run: launches up to three PS on the batch briefs, checks the extracts parse, writes the register | writes (the register) + Agent (budget 3 PS) |
| bench-operator | sonnet | Gives one advisory opinion on a question from the view of cost, time and what breaks in running the Command; Bench seat, "convene the bench" | read-only |
| bench-storyteller | sonnet | Gives one advisory opinion from the view of the Outliers, the fabula and what the story needs; Bench seat, "convene the bench" | read-only |
| bench-money | sonnet | Gives one advisory opinion from the view of BoldVenture, ORANGE and what pays; Bench seat, "convene the bench" | read-only |
| bench-engineer | sonnet | Gives one advisory opinion from the view of the box, the scripts and what is buildable; Bench seat, "convene the bench" | read-only |
| bench-skeptic | sonnet | Gives one advisory opinion by naming what is wrong with the idea (pre-mortem); Bench seat, "convene the bench" | read-only |
| sci-literature | sonnet | Finds papers through OpenAlex; returns sources with DOI and a one-line finding each; Science Department seat | read-only (Bash: paper_search.py; WebFetch) |
| sci-physics | sonnet | Answers orbital, habitat, Moon and energy questions with the number, the formula and the assumptions; Science Department seat | read-only |
| sci-plausibility | sonnet | Flags the impossible or unexplained in a scene (line, problem, two ways to keep it); advises, never gates; Science Department seat | read-only |
| sci-biomed | sonnet | Checks biology and medicine for the eras in bounded-claims wording; Science Department seat | read-only |
| sci-forecast | sonnet | Forecasts technology for eras 3 and 4 in a favorable / adverse / wild-card / second-order frame; Science Department seat | read-only |
| editing-structure | sonnet | Script editor: act shape, turning points, setups and payoffs, pacing; report only | writes (one report) |
| editing-character | sonnet | Script editor: want vs need, arcs, choices, consistency; report only | writes (one report) |
| editing-dialogue | sonnet | Script editor: voice, subtext, on-the-nose and exposition lines, rhythm; report only | writes (one report) |
| editing-line | sonnet | Script editor: action-line economy, scene headings, formatting, readability; report only | writes (one report) |
| editing-continuity | sonnet | Script editor: timeline, who-knows-what, names, props, world rules; report only | writes (one report) |
| editing-theme-tone | sonnet | Script editor: theme, tone breaks, genre promise, motifs; report only | writes (one report) |
| reading-cold | sonnet | Script editor: first-time reader's coverage with no canon; report only | writes (one report) |
| editing-production | sonnet | Script editor: locations, cast, hard scenes, slice candidates, cheapest beats; report only | writes (one report) |
| planning-project | sonnet | The project manager: phases, owners, gates, decision points, risks and an ETA per step for one project; `kickoff` step 1 | writes (plan.json + plan.md) |
| mapping-sources | haiku | Maps every place one project's material lives (rows, loose ends, gaps), one seat per disjoint folder set; `kickoff` step 2 | writes (sources.SEAT.json) |
| tagging-fabula | haiku | Proposes an era + fabula event tag per story file (story or discourse, kernel or satellite); a script applies; `kickoff` step 3 | writes (tags.BATCH.json) |
| drafting-call-sheet | sonnet | Preps a meeting with Chief: 6–8 calls, one rec each, evidence, dissent and the book behind the rec; `kickoff` step 4 | writes (calls.json + calls.md) |

**The kickoff stack (ruled 11/4, Chief: "build the whole stack"):** the four agents above are fired by the `kickoff` skill whenever a project starts. Every method step in their files cites a library book (BVX / MIL / TEC id + section) or is marked `[organic]`, and every output claim carries `file:line` or is marked `UNSOURCED`. Briefs and the common sourcing rule: `_tools/bolostatus/work/oxo-start/briefs/`.

## The Command rules

Every agent opens with the same block (BOLO 139). It says the agent is a specialist on the CDR's call: it works only on the inputs it is given and writes only the files its brief names. It reports in plain words, with file:line or URL for every claim, in under 250 words unless the brief says otherwise. It never grades another agent's work, never launches agents (no agent has the Agent tool, except collect-lead, which launches up to three PS its brief budgets under depth 2, SOP §1.17), and never scans the machine unless the brief names it. Private detail (health, sexual, provider) stays out of public files. Only collect-lead (its register), doc-updater, refactor-cleaner, opensource-forker and opensource-packager can write or edit; every other agent returns its result as a report for the CDR to file. What each agent lost in adaptation is in `_PRIVATE/ecc/roster-notes.md`.

**Shelved 10/18** (Chief: "take all recs", BOLO 155 M5; never fired; files kept in `_tools/armory/shelf/agents/`, one move from coming back): `a11y-architect`, `chief-of-staff`, `claim-checker`, `code-explorer`, `cto`, `marketing-agent`, `mle-reviewer`, `network-troubleshooter`, `opensource-forker`, `opensource-packager`, `performance-optimizer`, `planner`, `pytorch-build-resolver`, `refactor-cleaner`, `seo-specialist`, `silent-failure-hunter`. Merged: `code-explorer` and `planner` are modes of `architect`; `silent-failure-hunter` and `performance-optimizer` are modes of `python-reviewer`.

**M11 ruled 10/18** (Chief: "do all recs", BOLO 155): five more shelved (no skill or script calls them): `conversation-analyzer` (the session note's Lessons line does the job), `prose-taste` (the one reviewer is a script, `prose_lint.py`; a checker agent breaks the doctrine), `drill-maker` · `teach-coach` · `syllabus-builder` (the teach-back runs in the spoken line). Kept with a named launcher: `architect` (the CDR on a "design X" or "plan X" tooling ask; first test: "plan the per-layer probe step for BOLO 121") and `loop-operator` (the 30-minute reload report deploys it when the log stalls or errors repeat).
