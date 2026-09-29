---
type: ssot_06_style_guides
category: style_guide
version: 1.0.0
last_updated: 2026-09-29
applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD, BVX-LEARN]
status: "canonical — 1.0 per BOLO 92's bar; both OPEN calls ruled"
purpose: "The index and the rules for how the Command writes: replies, readbacks, and the SSOT documentation conventions. Points to the writing guide (06.2a) and the markdown-marking standard (06.2b); gathers the reply-format rulings that today live only in SOP §7 and in memory."
dependencies: ["[[📐 ssot_06_2a_writing_guide]]", "[[📐 ssot_06_2b_markdown_marking]]", "SOP.md §7"]
trunk: BLACK
sources: ["SOP.md §7", "memory: plain-register", "memory: house-format", "memory: one-value-one-block", "memory: clickable-file-links", "memory: touchstone-name", "memory: the-command"]
---

# 📐 ssot_06_2_documents_style — how the Command writes

## TABLE OF CONTENTS

- [Purpose](#purpose)
- [The index — 06.2a and 06.2b](#the-index--062a-and-062b)
- [The reply format — SOP §7, summarized](#the-reply-format--sop-7-summarized)
- [Naming rulings that govern every document](#naming-rulings-that-govern-every-document)
- [OPEN](#open)
- [Version History](#version-history)

## PURPOSE

> **The split (CDR, 2026-09-29):** 06.2 governs how the Command writes (docs, replies, pages' text); how the *stories* read is [📐 ssot_06_1_prose_style.md](📐%20ssot_06_1_prose_style.md). Neither guide rules for the other.

Two things are called "style" in the Command and they are not the same thing. **Prose style** ([[📐 ssot_06_1_prose_style]], a parallel BOLO 92 build) governs the fiction. **Documents style** — this page — governs everything the Command writes about itself: replies to Chief, readbacks, and the SSOT documentation the writing guide and the markdown-marking standard already cover in full. This page does not restate either of those; it indexes them and it carries the rulings that, before today, lived only in [SOP.md](../../../../SOP.md) §7 and in session memory, un-collected.

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

RULED 2026-09-29 (Chief: "all right" on all recs, BOLO 92): fold BOLO 6's distill into the rule rows when it lands; the 06.1/06.2 split is drawn by the cross-reference lines (done 2026-09-29).

- **The learning-science distill of the reply format is still pending** — SOP §7 itself is marked "v0.1 — the full learning-science distill is BOLO 6." Rec: fold BOLO 6's findings into this table's rule 1–7 rows when BOLO 6 lands, rather than reopening SOP §7 directly.
- **The boundary between 06.2 (documents) and 06.1 (prose)** is drawn by convention here, not by a ruling — no Chief ruling was found naming the split. Rec: once [[📐 ssot_06_1_prose_style]] publishes, add one cross-reference line each way and confirm neither page claims a rule the other already owns.

## VERSION HISTORY

- **1.0.0 · 2026-09-29** — both OPEN calls RULED as recommended: BOLO 6 folds in on landing; the 06.1/06.2 split is set by cross-reference.
- **0.1.0 · 2026-09-29** — bootstrap: indexes 06.2a and 06.2b; SOP §7's twelve rules summarized with citations; five naming rulings gathered from memory for the first time (plain register, Command format, clickable file links, Touchstone naming, the Command naming); two OPEN calls.
