---
rung: procedure · NASA four, ruled 2026-09-15 (BOLO 50)
type: ssot_procedure
category: operations
version: 0.1.0
last_updated: 2026-09-15
applies_to: [BOLD_VENTURE, ULTRASIN, OPERATOR]
status: ruled 2026-09-15 by Papi ("let's go with the NASA four"); the filing table grows a row per document
bolo: 50
purpose: "Names the four rungs every house document sits on, the shall/should rule that decides the rung, the frontmatter tag that records it, and the filing table of record."
dependencies: ["[[DOCTRINE-0-INVARIANTS]]", "[[SOP]]", "[[📐 ssot_05_operations_project_flow]]", "[[📐 ssot_05_operations_development_standard]]", "[[standards.register]]"]
sources: "standards.register.md §1 (how nine bodies tier their documents, 2026-09-11) · NASA NODIS directive tiers (NPD → NPR → NASA-STD / NASA-HDBK) · DoD DSP (MIL-STD · MIL-HDBK · MIL-SPEC) for the spec concept · Papi's ruling 2026-09-15"
---

# 📐 ssot_05_operations_standards_ladder — THE HOUSE LADDER

## Purpose

Every house document sits on one of four rungs. The rung says how binding the document is and what it may contain. **Ruled 2026-09-15: the NASA four**, in the house's own words, with the spec borrowed from DoD as a tag on nodes rather than a fifth rung.

## The four rungs

| Rung | NASA parent | What it answers | Carries "shall"? | House examples |
|---|---|---|---|---|
| **policy** | NPD | What the house does and why. Signed at the top. | yes, at the level of the whole house | DOCTRINE 0 |
| **procedure** | NPR | How the house does it. Mandatory. Who does what. | yes | SOP · the project flow · the development standard · the marking SOP · this ladder |
| **standard** | NASA-STD | The measurable "shall" for a class of product or process. | yes | the WATCH register · the variable registry · the writing guide |
| **handbook** | NASA-HDBK | Guidance. "Should." Forbids nothing. | no | the MCDP one-sheets · the CK3 IA study · the explainers · the DOPE SHEET pattern |

**Spec** is a tag, not a rung: one document saying what one specific product must be (DoD's MIL-SPEC). In the house a spec is a node or a charter: the BOLO 24 charter, every canon node's invariants, a persona sheet.

## The rule that decides the rung

1. **If it forbids nothing, it is a handbook** (DOCTRINE 0, Invariant III: a rule that forbids nothing is decoration). Handbooks say "should".
2. **If it measures a product, it is a standard.** A standard's "shall" is testable against the thing.
3. **If it governs how the house works, it is a procedure.** Its "shall" is testable against the transcript and the record.
4. **If it says what the house is and why, it is policy.** The policy rung stays tiny: DOCTRINE 0 and nothing else until something earns it (Invariant I).

## The tag

Every document carries one frontmatter line, first line after the opening fence:

```
rung: procedure · NASA four, ruled 2026-09-15 (BOLO 50)
```

A document with no frontmatter gets a three-line block holding only the tag. Read-only files are listed in the table below and stamped when they are next opened for a change.

## The filing table · 2026-09-15

| Document | Rung | Status |
|---|---|---|
| `DOCTRINE-0-INVARIANTS.md` | policy | stamped |
| `SOP.md` | procedure | stamped |
| `ShroomsQ/_CANON/_SSOT/05_OPERATIONS/📐 ssot_05_operations_project_flow.md` | procedure | stamped |
| `ShroomsQ/_CANON/_SSOT/05_OPERATIONS/📐 ssot_05_operations_development_standard.md` | procedure | stamped |
| `ShroomsQ/_CANON/_SSOT/05_OPERATIONS/📐 ssot_05_operations_markdown_marking.md` | procedure | stamped |
| `ShroomsQ/_CANON/_SSOT/05_OPERATIONS/📐ssot_variable_registry.md` | standard | stamped |
| `_0.1_BVX_LEARN/_meta/WATCH-REGISTER.md` | standard | stamped |
| `_0.1_BVX_LEARN/_meta/CK3-IA-STUDY.md` | handbook | stamped |
| `_PRIVATE/BOLO-24-charter.md` | spec | stamped |
| `_0.1_BVX_LEARN/KNOWLEDGE_AREAS/🧬 MIL.01 — MCDP 1 Warfighting — USMC (1997).md` | handbook | stamped |
| `_0.1_BVX_LEARN/KNOWLEDGE_AREAS/🧬 MIL.02 — MCDP 1-1 Strategy — USMC (1997).md` | handbook | stamped |
| `_0.1_BVX_LEARN/KNOWLEDGE_AREAS/🧬 MIL.03 — MCDP 1-2 Campaigning — USMC (1997).md` | handbook | stamped |
| `_0.1_BVX_LEARN/KNOWLEDGE_AREAS/🧬 MIL.04 — MCDP 1-3 Tactics — USMC (1997).md` | handbook | stamped |
| `_0.1_BVX_LEARN/KNOWLEDGE_AREAS/🧬 MIL.05 — MCDP 2 Intelligence — USMC (1997).md` | handbook | stamped |
| `_0.1_BVX_LEARN/KNOWLEDGE_AREAS/🧬 MIL.06 — MCDP 3 Expeditionary Operations — USMC (1998).md` | handbook | stamped |
| `_0.1_BVX_LEARN/KNOWLEDGE_AREAS/🧬 MIL.07 — MCDP 4 Logistics — USMC (2023).md` | handbook | stamped |
| `_0.1_BVX_LEARN/KNOWLEDGE_AREAS/🧬 MIL.08 — MCDP 5 Planning — USMC (1997).md` | handbook | stamped |
| `_0.1_BVX_LEARN/KNOWLEDGE_AREAS/🧬 MIL.09 — MCDP 6 Command and Control — USMC (1996).md` | handbook | stamped |
| `_0.1_BVX_LEARN/KNOWLEDGE_AREAS/🧬 MIL.10 — MCDP 7 Learning — USMC (2020).md` | handbook | stamped |
| `_0.1_BVX_LEARN/KNOWLEDGE_AREAS/🧬 MIL.11 — MCDP 8 Information — USMC (2022).md` | handbook | stamped |
| `ShroomsQ/_CANON/_SSOT/05_OPERATIONS/📐 ssot_writing_guide.md` | standard | read-only file, listed here only |
| `ShroomsQ/_CANON/_SSOT/05_OPERATIONS/📐ssot_SSOT_CREATION.md` | procedure | read-only file, listed here only |
| `_CANON_NODES/*.md` (34 files) | spec | listed by folder; tagged one by one as each node is next touched |

## Governance

DOCTRINE 0 governs: this ladder is v0.1, ruled, and promotes to canonical after two filing passes. Phase 4 of BOLO 50 was the first pass. The next document written in the house carries the tag from birth; a document found without one is filed at the next sit rep.

## Version History

| Version | Date | Changes |
|---|---|---|
| 0.1.0 | 2026-09-15 | Ruled: the NASA four (policy · procedure · standard · handbook), spec as a tag. First filing pass: 20 documents stamped, 2 listed. |
