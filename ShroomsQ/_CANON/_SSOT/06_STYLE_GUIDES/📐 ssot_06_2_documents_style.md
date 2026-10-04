---
type: ssot_06_style_guides
category: style_guide
version: 1.3.0
last_updated: 2026-10-04
reader: "anyone writing for the Command: Claude sessions first, Chief when he checks"
doc_type: reference
owner: "Chief (HOTLINE ACTUAL); Claude keeps it"
state: ruled
reviewed: 2026-10-04
applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD, BVX-LEARN]
status: "canonical core (the documentation SOP, BOLO 95, folded in 2026-10-04); all five merge calls ruled"
purpose: "The index and the rules for how the Command writes: replies, readbacks, and the SSOT documentation conventions. Points to the writing guide (06.2a) and the markdown-marking standard (06.2b); gathers the reply-format rulings that today live only in SOP §7 and in memory."
dependencies: ["_tools/bolostatus/work/95/DOC-SOP.md (the teach-back record)", "[[📐 ssot_06_2a_writing_guide]]", "[[📐 ssot_06_2b_markdown_marking]]", "SOP.md §7"]
trunk: BLACK
sources: ["SOP.md §7", "memory: plain-register", "memory: house-format", "memory: one-value-one-block", "memory: clickable-file-links", "memory: touchstone-name", "memory: the-command"]
---

# 📐 ssot_06_2_documents_style — how the Command writes

## TABLE OF CONTENTS

- [Purpose](#purpose)
- [The documentation rules — the core (BOLO 95)](#the-documentation-rules--the-core-bolo-95)
- [The index — 06.2a and 06.2b](#the-index--062a-and-062b)
- [The reply format — SOP §7, summarized](#the-reply-format--sop-7-summarized)
- [Naming rulings that govern every document](#naming-rulings-that-govern-every-document)
- [OPEN](#open)
- [Version History](#version-history)

## PURPOSE

> **The split (CDR, 2026-09-29):** 06.2 governs how the Command writes (docs, replies, pages' text); how the *stories* read is [📐 ssot_06_1_prose_style.md](📐%20ssot_06_1_prose_style.md). Neither guide rules for the other.

Two things are called "style" in the Command and they are not the same thing. **Prose style** ([[📐 ssot_06_1_prose_style]], a parallel BOLO 92 build) governs the fiction. **Documents style** — this page — governs everything the Command writes about itself: replies to Chief, readbacks, and the SSOT documentation the writing guide and the markdown-marking standard already cover in full. This page does not restate either of those; it indexes them and it carries the rulings that, before today, lived only in [SOP.md](../../../../SOP.md) §7 and in session memory, un-collected.

## THE DOCUMENTATION RULES — THE CORE (BOLO 95)

> **Folded in 2026-10-04 (BOLO 92, Chief: "go ahead with a recommendation").** These rules are the core of 06.2. Chief locked each one by teach-back between 2026-09-30 and 2026-10-03; his readbacks and the sources live in the record, [DOC-SOP.md](../../../../_tools/bolostatus/work/95/DOC-SOP.md). Where 06.2a or 06.2b disagree, this section wins (merge calls ruled 2026-10-04).

**1 · One page, one job**

| # | Rule | Locked |
|---|---|---|
| 1.1 | Every document does one job. A page that tries to do two becomes two pages. The job is either **doing** (the reader skims for a step, then stops) or **understanding** (the reader reads it through). | 2026-09-30 |
| 1.2 | Four types. **Tutorial**: a lesson, learned by doing it start to finish. **How-to**: a recipe for one task the reader already understands. **Reference**: facts the reader looks up and leaves. **Concept**: the why, read front to back. The first three are doing pages; concept is the one understanding page. | 2026-10-03 |
| 1.3 | Writing order: concept, then reference, then how-to, then tutorial. Readers meet them in the opposite order. | 2026-10-03 |

**2 · The page header**

| # | Rule | Locked |
|---|---|---|
| 2.1 | Every page first names **who it's for** (reader and situation), **what it does** (the one job, one line), and **which type** it is. | 2026-10-03 |
| 2.2 | Under those three: **owner** (who decides what it says), **state** (draft · ruled · retired), **reviewed** (the date someone last checked it against the truth). | 2026-10-03 |
| 2.3 | The 2.1 three sit up top, in the one thin strip. The 2.2 three sit one click away: behind a button on a page, in the front matter of a markdown file. | 2026-10-03 |

**3 · The words**

| # | Rule | Locked |
|---|---|---|
| 3.1 | One word for each thing, and only that word. Define it the first time it shows up. | 2026-10-03 |
| 3.2 | One idea per sentence. Every sentence names who does what. Read it out loud; where the reader runs out of breath, the sentence is too long (20 words is the check the scripts run). | 2026-10-03 |
| 3.3 | Docs stay plain. The rich, verbose description goes in one marked section, "The long read," at the bottom of a concept page. Story prose follows [06.1](📐%20ssot_06_1_prose_style.md). | 2026-10-03 |
| 3.4 | Review in separate passes: facts, then words, then out loud. A ruled page is never edited quietly; Chief rules the change and the reviewed date updates. | 2026-10-03 |

**4 · The extra page types**

| # | Rule | Locked |
|---|---|---|
| 4.1 | **Troubleshooting**: starts from what the reader sees. One entry per problem: symptom, then cause, then fix. The heading is the symptom in the reader's words. | 2026-10-03 |
| 4.2 | **Glossary**: one entry per term, alphabetical. Each entry is the term, a one-line plain meaning, and a link to where it is used. An old name points to the current one. | 2026-10-03 |
| 4.3 | **Decision record**: one decision per page, dated, with who ruled it. Three parts: what we decided, why, and what we gave up. Never edited after it is ruled; a new decision gets a new record that points back. | 2026-10-03 |

**Applied so far (2026-10-04):** the SOI (reviewed in three passes, 46 entries rewritten), the sit rep page and the DOPE SHEETs (header, writer briefs, and a long-sentence check in the reviewer script).

## THE INDEX — 06.2a AND 06.2b

| Document | Governs | Status |
|---|---|---|
| [📐 ssot_06_2a_writing_guide.md](📐%20ssot_06_2a_writing_guide.md) | SSOT documentation: the H1–H2 hierarchy, the linguistic-authority standards (no contractions, no hedging, present tense, bolded first-instance terms), the flat-syntax YAML standard. | canonical (moved from 05_OPERATIONS, BOLO 92) |
| [📐 ssot_06_2b_markdown_marking.md](📐%20ssot_06_2b_markdown_marking.md) | The four inline marks (`**bold**` writer-structure, `==highlight==` reader-capture, `_italic_` captions, `[[wikilink]]` promotion) and the harvest tool. | canonical (moved from 05_OPERATIONS, BOLO 92) |
| [_history/📐 ssot_06_legacy_styleguide_2024.md](_history/📐%20ssot_06_legacy_styleguide_2024.md) | The 2024 ancestor of both — kept as the record, not read as doctrine. | history |

## THE REPLY FORMAT — SOP §7, SUMMARIZED

SOP §7 stays the authority for replies (it says so itself, in the line added for this BOLO). This table is a locator, not a replacement — read [SOP.md §7](../../../../SOP.md) for the full text of each rule.

| # | Rule, in one line | Citation |
|---|---|---|
| 1 | Readbacks are bulleted, one order per bullet, bold anchor up front — never a prose wall. | SOP §7 rule 1 (coded 2026-08-21) |
| 2 | One idea per paragraph, three sentences max. | SOP §7 rule 2 (coded 2026-08-21) |
| 3 | Bold is a signpost, not decoration — the bolds alone must tell the story on a scan. | SOP §7 rule 3 (coded 2026-08-21) |
| 4 | Parallel items go in bullets or tables, never buried in prose. | SOP §7 rule 4 (coded 2026-08-21) |
| 5 | Answer-first everywhere (Pyramid Principle). | SOP §7 rule 5 (coded 2026-08-21) |
| 6 | The Spartan dial: trim words, not meaning. | SOP §7 rule 6 (coded 2026-08-21) |
| 7 | The ten-second test: headers plus bolds alone must carry the message. | SOP §7 rule 7 (coded 2026-08-21) |
| 8 | One value, one block: anything Chief must copy-paste gets its own fenced code block, nothing else in it. | SOP §7 rule 8 (coded 2026-09-04; memory: one-value-one-block) |
| 9 | The OUT block: every Oscar Mike reply closes with the fenced sign-off block and nothing after it. | SOP §7 rule 9 (coded 2026-09-06) |
| 10 | The spoken line: a reply longer than a few sentences opens with `<!-- say: … -->` in JUDY's register; a reply without one is silent. | SOP §7 rule 10 (coded 2026-09-17, BOLO 56) |
| 11 | The ETA: every reply that accepts a tasking states when it lands. | SOP §7 rule 11 (RULED 2026-09-20) |
| 12 | Match the flavor: when Chief flirts, the reply answers in kind before the readback; the work itself stays in the plain register. | SOP §7 rule 12 (RULED 2026-09-20) |
| 13 | One part per teaching reply: one small idea, then stop. | SOP §7 rule 13 (RULED 2026-10-04, BOLO 6) |
| 14 | The spoken line is the point: a sentence, never a label; the teach-back says it back. | SOP §7 rule 14 (RULED 2026-10-04, BOLO 6) |
| 15 | The cold re-check: one cold question on the newest locked part at the next session's open. | SOP §7 rule 15 (RULED 2026-10-04, BOLO 6) |
| 16 | A worked example, last step open, for procedures only. | SOP §7 rule 16 (RULED 2026-10-04, BOLO 6) |

## NAMING RULINGS THAT GOVERN EVERY DOCUMENT

These never made it into SOP §7's numbered list because they are not reply-formatting rules — they are naming and register rulings that apply to documents (this one included). Collected here for the first time.

| Rule, in one line | Citation |
|---|---|
| Write in the plain register: name first, number second; define a Command term on first use; every sentence has an actor and a verb. | RULED 2026-09-17, BOLO 67 (memory: plain-register) |
| Readbacks and documents chunk — bold signposts, the ten-second scan test — under the name **the Command format** (was "house format" until 9/16). | Coded 2026-08-21; renamed 2026-09-16 (memory: house-format, the-command) |
| Every file or folder named in a reply is a clickable markdown link with a workspace-relative path, never a backticked path. | Ruled 2026-09-03 (memory: clickable-file-links) |
| The rules a story can never break are cited **Touchstone(s)**, as **TS 1:3** (book:number) — "invariant" is retired in prose; machine fields keep the old name until the schema pass. | RULED 2026-09-24, BOLO 81, call 81-A (memory: touchstone-name) |
| The whole operation is **the Command**, never "the house"; "organic" replaces "in-house"; BLACK and ORANGE stay trunks. | RULED 2026-09-16, BOLO 48 (memory: the-command) |

## OPEN

✅ **The merge calls (2026-10-04, BOLO 92), ALL FIVE RULED as recommended (Chief: "all right").** Folding the core in exposed five places where the older guides disagreed with it. Each *Rec* below is now the rule; 06.2a 2.2.0 carries 1–4.

1. **Contractions.** 06.2a bans them ("do not," never "don't"). The core's 3.2 asks for text that reads clean out loud, and the plain register (BOLO 67) writes like the Claude Code docs, which use them. *Rec:* allow contractions everywhere; strike the 06.2a ban.
2. **The fixed eight-part skeleton.** 06.2a makes every SSOT document carry Core Methodology, Implementation, and at least two Examples. That puts a concept, a how-to, and a reference on one page, against 1.1. *Rec:* keep the frame (YAML, title, contents, purpose, version history); the body follows the page's type (1.2); two examples stay required on concept pages only.
3. **Front-matter fields.** 2.2–2.3 put owner, state, and reviewed in the front matter; today the YAML has `status` and `last_updated` only. *Rec:* add `reader`, `doc_type`, `owner`, `state` (draft · ruled · retired), and `reviewed`; keep `status` and `last_updated` until the schema pass, the way the Touchstone rename kept its machine fields.
4. **A stray document inside 06.2a.** Below its version history, 06.2a carries a second, unrelated file pasted in: the 2026-02 Goon Room protocol. *Rec:* split it out to its own file in `05_OPERATIONS/`, flagged as legacy, and leave 06.2a holding one job.
5. **The SOP's home.** *Rec:* this section is the home of the rules from today; DOC-SOP.md stays as the teach-back record (readbacks and sources) with a pointer here at its head.

**Ruled 2026-09-29:**

RULED 2026-09-29 (Chief: "all right" on all recs, BOLO 92): fold BOLO 6's distill into the rule rows when it lands; the 06.1/06.2 split is drawn by the cross-reference lines (done 2026-09-29).

- **The learning-science distill of the reply format is still pending** — SOP §7 itself is marked "v0.1 — the full learning-science distill is BOLO 6." Rec: fold BOLO 6's findings into this table's rule 1–7 rows when BOLO 6 lands, rather than reopening SOP §7 directly.
- **The boundary between 06.2 (documents) and 06.1 (prose)** is drawn by convention here, not by a ruling — no Chief ruling was found naming the split. Rec: once [[📐 ssot_06_1_prose_style]] publishes, add one cross-reference line each way and confirm neither page claims a rule the other already owns.

## VERSION HISTORY

- **1.3.0 · 2026-10-04** — SOP §7 rules 13–16 added to the locator (BOLO 6, the teaching rules); this is BOLO 6's first fold into 06.2.
- **1.2.0 · 2026-10-04** — all five merge calls RULED as recommended (Chief: "all right"); header fields added to this page's own front matter.
- **1.1.0 · 2026-10-04** — the documentation SOP (BOLO 95) folded in as the core; five merge calls OPEN with recs.
- **1.0.0 · 2026-09-29** — both OPEN calls RULED as recommended: BOLO 6 folds in on landing; the 06.1/06.2 split is set by cross-reference.
- **0.1.0 · 2026-09-29** — bootstrap: indexes 06.2a and 06.2b; SOP §7's twelve rules summarized with citations; five naming rulings gathered from memory for the first time (plain register, Command format, clickable file links, Touchstone naming, the Command naming); two OPEN calls.
