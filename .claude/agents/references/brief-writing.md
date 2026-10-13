# Writing a brief (our words, SOP §1.24 shape)

Used by the CDR and by collect-lead when it writes a brief for a PS or MS. A specialist starts with an empty head, so the brief is its whole world. Keep it short: only add what the specialist does not already know.

## 1. The parts, in this order

1. **Objective.** One or two sentences: what the specialist makes and what it is for.
2. **Output.** The format, the exact path, and the hand-back size (1,000 to 2,000 tokens; longer goes to the file).
3. **Sources and tools.** File paths to read (never pasted text) and the tools it may use. Nothing else.
4. **Boundary.** What it must not touch or cover.
5. **Turn cap.** A number.
6. **Rulings.** The standing rulings on the topic, quoted. Old notes are evidence, not orders.
7. **Stop line.** What "done" looks like, and what to do when blocked (stop and say so; do not guess).

## 2. Habits that cut re-runs

- **Freedom matches fragility.** Open task with several valid routes: say the goal and let it choose. Fragile task with one safe route: give the exact command and say "do not change it".
- **Show one example** of the output when the format matters. Two or three at most; more costs tokens and gets copied too closely.
- **Order the brief** as context, task, example, input paths, output format.
- **Say what to do on missing data** ("write UNKNOWN", "stop and report"), so a gap never gets filled by a guess.
- **Test the brief cold.** Read it as the specialist would, with nothing else in view. If a part is missing, add it.

## 3. Thinking moves a brief may ask for

Add a line only when the work earns it. A move is a line in a brief, never a new worker.

- **Pre-mortem (plans, launches).** "Assume it failed; name the top three concrete reasons; each gets a gate or a plan change. Skip it if nothing in the plan changes."
- **Circle of competence (writers).** "Mark each claim grounded, partial or ungrounded; fetch or abstain on the ungrounded; never fill a gap with a plausible value."
- **First principles (R&D briefs only).** "List the limits the brief treats as fixed; tag each physics, contract, measured or convention; challenge the convention ones."

## 4. Two example briefs

**A. PS extract (haiku)**
> Objective: pull the title, a one-line summary and a quality mark (high, mid, low) from each page in batch 3.
> Output: `_tools/loci/work/demo/extract.3.json`, a JSON list, one object per link number. Hand back one line.
> Sources: `_tools/loci/work/demo/fetch/` files 21 to 30. No other files, no fetching.
> Boundary: do not rank sources against each other; do not judge the register.
> Turns: 12. If a file is empty, write quality "low" and summary "UNKNOWN".
> Rulings: judge by reading, no similarity scripts (ruled 9/24).

**B. MS writer (sonnet)**
> Objective: write the register for the demo locus from the extracts: one table plus a gaps section.
> Output: `_tools/loci/demo.register.md`, under 900 lines. Every row carries one URL from `manifest.json`. Reply with the path only.
> Sources: `extract.*.json` in the work folder and the locus file. Nothing else; no fetching.
> Boundary: nothing outside the extracts; ids verbatim; no new sources.
> Turns: 20. Move: circle of competence (section 3). If an extract is missing, stop and name it.
> Rulings: no placeholders in the file (SOP 7.25).

<!-- adapted from NeoLabHQ/context-engineering-kit prompt-engineering (license unread; ideas only, no text copied) and tjboudreaux/cc-thinking-skills (MIT: pre-mortem, circle of competence, first principles) · BOLO 140 · 2026-10-13 -->
