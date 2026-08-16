---
original_path: "/mnt/user-data/outputs/BVX-CR-merged-template.md"
source_conversation: "Advanced literature review of Mating in Captivity"
created: 2026-06-06
trunk: BLACK
kind: generated-file
---

# BVX-CR TEMPLATE v1
## Blended Knowledge Entry Generator — One-Sheet (Tier 1) over Canonical Review (Tier 2)

---

> **What this is.** A generator for turning any book or source into a *single file with two tiers*: a terse, human-facing **one-sheet** on top (BVX-LEARN register) and a deep, machine-readable **canonical review** below, the two cross-linked so a reader drops from any one-sheet line into the full treatment. It merges two prior formats — BVX-LEARN v2 (fast, decision-oriented) and the Canonical Review (deep, learning-oriented) — into the depth/density axis a single artifact can span.
>
> **Invocation.** Feed Claude a source and say: **"BVX-CR this."**

---

## WHY TWO TIERS

| | Tier 1 — One-Sheet | Tier 2 — Canonical Review |
|---|---|---|
| **Reader** | Human, fast | Human (deep) + AI/downstream layers |
| **Job** | Recall + "what do I do now" | Understand + teach + verify |
| **Voice** | Terse, imperative, declarative (BVX) | Instructional substrate |
| **Length** | One screen | As long as fidelity requires |
| **Unit** | Invariant / heuristic / concept | Module (advance organizer → retrieval → transfer) |
| **Contains** | The decision layer | The "in-depth" layer — cases, mechanisms, drills |

They are not redundant. Tier 1 is the index and the fast read; Tier 2 is the source of truth Tier 1 points into.

---

## THE LINKING CONTRACT (non-negotiable)

1. Each Tier-2 module gets an explicit, stable anchor immediately above its header: `<a id="m7"></a>`. Use plain HTML anchors (portable across VS Code, GitHub, Obsidian) — **not** Obsidian block-refs or callouts.
2. Every Tier-1 **invariant, heuristic row, and concept** ends with a deep-link to the module that develops it: `[→ M7](#m7)`.
3. Anchors are `m0…mN`, matching the chapter/module numbering of Tier 2.
4. The file opens with a two-line orientation: Tier 1 is the fast read; `[jump](#tier-2)` to the deep tier.

---

## VOICE RULES

- **Tier 1 — BVX register.** Short declarative sentences. Imperative in the heuristics. No hedging, no contractions. **Bold claim. Then the one-line why.** Compression is the point: if a concept needs more than four sentences here, it belongs only in Tier 2.
- **Tier 2 — instructional register.** Full prose, worked examples, retrieval. May be long.
- **Borrow structure, not ideology.** BVX one-sheets in the wild may carry a manipulative or instrumental frame inherited from their source. Adopt the *format* (invariants / heuristics / kill list / self-check) without importing a stance the source does not actually hold. Describe what the author argues.

---

## FIDELITY RULES (read before generating)

1. **Verify Tier 1 against the source, not against a sibling one-sheet.** When a book sits in a collection, terms bleed across files. Check every vocabulary item: does the author actually use it? (Worked example: the *Mating in Captivity* one-sheet had inherited "Hot/Cold Processing" and "Contextual Rapport" from the *Shogun Method* sheet — Rake's terms, not Perel's. Both were cut.)
2. **Flag every correction** in a `fidelity_note` (frontmatter) and inline where the reader would otherwise trust the wrong term.
3. **Tier 2 carries the locked Fidelity / Substitution Checklist** — every claim recoverable from the document alone; source prose never reproduced (short attributed phrases only).
4. **Distinguish the author's own coinages from borrowed field terms** in the glossary (mark *(Author)* vs. the source of a borrowed concept).

---

## PRODUCTION SEQUENCE (how Claude builds one)

1. **Read the source** (full text where available — do not synthesize from a summary).
2. **Build Tier 2 first** (the deep review): modules on the source's own architecture, real cases as worked examples, retrieval + transfer per module, glossary, dependency map, locked checklist. Insert `<a id="mN"></a>` anchors.
3. **Distill Tier 1 from Tier 2** (not the reverse): the thesis, 3–8 invariants, a 6–10-row heuristics table, 3–8 concepts, kill list, 6–10-item self-check — each linked to its module. Correct against source.
4. **Assemble** one file: frontmatter → Tier 1 → divider → Tier-2 banner (`<a id="tier-2">`) → Tier 2.
5. **Verify** anchors resolve and headers are clean.

---

## PROMPT SHORTCUTS

- **"BVX-CR this"** → full two-tier file from the source in context
- **"BVX-CR this, Tier 1 only"** → regenerate/refresh the one-sheet against existing Tier 2
- **"BVX-CR this, heavy on heuristics"** → expand the Tier-1 table and the modules it links to
- **"Re-fidelity Tier 1"** → audit the one-sheet's vocabulary against the source and flag bleed-in

---

## SKELETON

```markdown
---
id: [CATALOG.ID]
type: blended-entry
format: "BVX-CR v1 — Tier 1 (one-sheet) over Tier 2 (canonical review)"
title: [Title]
author: [Author]
year: [Year]
domain: [DOMAIN]
source_text: "[full citation] — verified against source"
audience: { tier_1: human-fast-read, tier_2: deep-reference-and-ai }
fidelity_note: "[corrections made vs source / sibling-file bleed removed]"
status: [draft|complete]
tags: [bvx-cr, ...]
---

# [ID] — [Title] — [Author] ([Year])
### Blended Entry | BVX-CR v1

> Two tiers, one file. Tier 1 = fast read. Tier 2 ([jump](#tier-2)) = deep reference. Each Tier-1 line links to its module [M#].

---
# TIER 1 — ONE-SHEET (human-facing)

## CORE THESIS
[one sentence] [→ M0](#m0)

## INVARIANTS
1. **[Claim].** [one-line why] [→ M#](#m#)
...

## HEURISTICS
| Situation | Do This | Not This |
|---|---|---|
| [trigger] [→M#](#m#) | [do] | [common mistake] |
...

## CORE CONCEPTS
**1. [Name].** [≤4 sentences] [→ M#](#m#)
...

## KEY VOCABULARY
| Term | Definition |  (mark *(Author)* vs borrowed)
*[note any terms removed as misattributions]*

## NOTABLE QUOTES
> "[short, attributed]"

## WHAT DOESN'T WORK
[comma-separated kill list]

## QUICK SELF-CHECK
- [ ] [binary behavior, priority-ordered]
*If any box is unchecked, that is the next priority — in the order listed.*

`BVX-CR v1 | Tier 1 ends | deep reference follows ↓`

---
---
<a id="tier-2"></a>
# TIER 2 — CANONICAL REVIEW (deep reference · AI-facing)

> [role-of-tier note]

[How to Use · Enduring Understandings · Objectives · Dependency Map · Glossary]

<a id="m0"></a>
## M0 — [Intro]
[advance organizer → objective → builds-on → core concepts → explanation → case → visual → RETRIEVAL → ANSWER → TRANSFER]

<a id="m1"></a>
## M1 — [Ch.1 ...]
...

# Cumulative Review Sets (Interleaved + Spaced)
# Fidelity / Substitution Checklist (locked)
```

---

`BVX-CR TEMPLATE v1 | merges BVX-LEARN v2 + Canonical Review | tool-agnostic plain markdown`
