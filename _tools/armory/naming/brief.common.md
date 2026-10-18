# Naming the general-purpose families (BOLO 155 M2, round 2 · 10/18)

Chief, 10/17: "generic is a cop out ... i want names processes". The Armory ledger shows these jobs ran again and again as `general-purpose`. Each gets a role file in `.claude/agents/`, superpowers style (ruled 10/17: "we use superpowers").

## The pattern to copy

Read `.claude/agents/drafting-rack-block.md`: that is the house shape. Match it:

- **Frontmatter:** `name` = the file name (verb-first, hyphens). `description` = WHEN to use it only (the trigger: which skill or script launches it, which brief names it), one or two sentences, under 300 characters, no workflow. If the description holds `: ` (colon then space), wrap the whole value in single quotes. `tools` = the fewest that do the job. `model` = the model the family already runs on (given below).
- **Body:** the Command rules paragraph, copied verbatim from the pattern file. One paragraph: who you are (the old role name, "formerly a general-purpose run; named 10/18 under the superpowers framework, BOLO 155 M2") and the job. "How you work": 3 to 6 numbered steps taken from the real brief writer you are given; never invent steps the brief writer does not ask for. "Report": the files written are the report; the reply is three lines at most and ends with one status line: `DONE` · `DONE_WITH_CONCERNS: <what>` · `NEEDS_CONTEXT: <what file or fact>` · `BLOCKED: <why>`.
- **Plain register** (SOP §7): one idea per sentence, 20 words max, actor and verb in every sentence.
- **Doctrine:** the agent never grades another agent, never launches agents (unless the brief writer says it leads PS seats), never scans the machine. Private detail stays out of public files.

## Prove it

Run `python _tools/done/verify.py` from the repo root (Bash). It must print PASS for your file. Write ONLY your one file. Reply in three lines: the path, what the brief writer launches it from (file:line), and anything the launcher must change to pass the agent's name and a `JOB: <name>` first line. End with a status line.
