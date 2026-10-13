# Agent roster

31 specialist agents: 22 adapted from the ECC repo (MIT, github.com/affaan-m/ECC) on 10/12, plus the BOLO 140 intake agents (each file names its source and license at the bottom). Seats: haiku = PS (fetch/extract), sonnet = MS (write/review), opus = planning and architecture only. The CDR decides when to call each one.

| Name | Model | Job in plain words | Access |
|---|---|---|---|
| a11y-architect | sonnet | Audits our HTML pages against WCAG 2.2 AA and specifies fixes | read-only |
| architect | opus | Proposes a design with trade-offs for a new tool or restructure | read-only |
| chief-of-staff | sonnet | Sorts pasted messages into four tiers and drafts replies; never sends | read-only |
| code-explorer | sonnet | Traces how an existing script works end to end | read-only |
| conversation-analyzer | haiku | Finds behaviors Chief had to correct in a transcript | read-only |
| doc-updater | haiku | Refreshes READMEs and code maps from the actual scripts | writes |
| drill-maker | haiku | Writes five recall questions from locked parts, each with its answer as a tip | read-only |
| harness-optimizer | sonnet | Reviews hooks, skills and agent config for reliability and cost; proposes | read-only |
| loop-operator | sonnet | Watches a long run from its logs, spots stalls, recommends pause or resume | read-only (Bash read-only) |
| marketing-agent | sonnet | Plans campaigns and writes or reviews marketing copy | read-only (web) |
| mle-reviewer | sonnet | Reviews data/model scripts for leakage, reproducibility, weak evaluation | read-only (Bash read-only) |
| network-troubleshooter | sonnet | Diagnoses connectivity and DNS symptoms, read-only, only when the box is named | read-only (Bash) |
| opensource-forker | haiku | Copies a project to staging, strips secrets and private references | writes |
| opensource-packager | haiku | Writes README, CLAUDE.md, setup script, LICENSE for a sanitized project | writes |
| opensource-sanitizer | sonnet | Independent pre-release audit: secrets, personal data, binaries, history | read-only (Bash read-only) |
| order-parser | haiku | Turns a garbled dictation line into a clean order (proword, BOLO, verb, object, confidence); never acts | read-only |
| performance-optimizer | sonnet | Finds why a script is slow or heavy and recommends measured fixes | read-only (Bash for timing) |
| planner | opus | Turns a request into a phased plan with files, risks and verification | read-only |
| prose-taste | sonnet | Flags slop words, filler openers, fake precision and unsourced claims in a draft, with the fix; never rewrites | read-only |
| python-reviewer | sonnet | Reviews Python for security, error handling, Windows pitfalls, style | read-only (Bash read-only) |
| pytorch-build-resolver | sonnet | Diagnoses PyTorch/CUDA errors and proposes the smallest fix | read-only (Bash) |
| refactor-cleaner | sonnet | Removes dead code and duplicates from named scripts, with checks | writes |
| root-cause | sonnet | Traces a bug to its root cause with an evidence chain before any fix is proposed | read-only (Bash read-only) |
| security-reviewer | sonnet | Finds leaked secrets, private data in public files, injection risks | read-only (Bash read-only) |
| seo-specialist | sonnet | Audits public pages for technical and on-page SEO | read-only (web) |
| silent-failure-hunter | sonnet | Finds swallowed errors and runs that look green but skipped work | read-only (Bash read-only) |
| syllabus-builder | sonnet | Maps a topic into a bare tree of one-line parts in teaching order | read-only |
| teach-coach | sonnet | Teaches one tiny part at a time as a spoken sentence plus one tip | read-only |
| skill-builder | sonnet | Drafts or trims one skill or agent file to the Anthropic skill patterns; names test prompts | writes (one named file) |
| claim-checker | sonnet | Lists a draft's factual claims, finds primary sources and scores each (supported, weak, unsupported, contradicted) | read-only (web) |
| skill-optimizer | sonnet | Reads one transcript and one skill, finds where the skill misfired or dragged, proposes the smallest edit | read-only |

## The Command rules

Every agent opens with the same block (BOLO 139). It says the agent is a specialist on the CDR's call: it works only on the inputs it is given and writes only the files its brief names. It reports in plain words, with file:line or URL for every claim, in under 250 words unless the brief says otherwise. It never grades another agent's work, never launches agents (no agent has the Agent tool), and never scans the machine unless the brief names it. Private detail (health, sexual, provider) stays out of public files. Only doc-updater, refactor-cleaner, opensource-forker and opensource-packager can write or edit; every other agent returns its result as a report for the CDR to file. What each agent lost in adaptation is in `_PRIVATE/ecc/roster-notes.md`.
