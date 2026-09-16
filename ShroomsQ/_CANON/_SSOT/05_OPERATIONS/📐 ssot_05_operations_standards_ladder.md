---
rung: procedure · NASA four, ruled 2026-09-15 (BOLO 50)
type: ssot_procedure
category: operations
version: 0.2.0
last_updated: 2026-09-15
applies_to: [BOLD_VENTURE, ULTRASIN, OPERATOR]
status: ruled 2026-09-15 by Papi ("let's go with the NASA four"); the filing table grows a row per document
bolo: 50
purpose: "Names the four rungs every Command document sits on, the shall/should rule that decides the rung, the frontmatter tag that records it, and the filing table of record."
dependencies: ["[[DOCTRINE-0-INVARIANTS]]", "[[SOP]]", "[[📐 ssot_05_operations_project_flow]]", "[[📐 ssot_05_operations_development_standard]]", "[[standards.register]]"]
sources: "standards.register.md §1 (how nine bodies tier their documents, 2026-09-11) · NASA NODIS directive tiers (NPD → NPR → NASA-STD / NASA-HDBK) · DoD DSP (MIL-STD · MIL-HDBK · MIL-SPEC) for the spec concept · Papi's ruling 2026-09-15"
---

# 📐 ssot_05_operations_standards_ladder — THE COMMAND LADDER

## Purpose

Every Command document sits on one of four rungs. The rung says how binding the document is and what it may contain. **Ruled 2026-09-15: the NASA four**, in the Command's own words, with the spec borrowed from DoD as a tag on nodes rather than a fifth rung.

## The four rungs

| Rung | NASA parent | What it answers | Carries "shall"? | Command examples |
|---|---|---|---|---|
| **policy** | NPD | What the Command does and why. Signed at the top. | yes, at the level of the whole Command | DOCTRINE 0 |
| **procedure** | NPR | How the Command does it. Mandatory. Who does what. | yes | SOP · the project flow · the development standard · the marking SOP · this ladder |
| **standard** | NASA-STD | The measurable "shall" for a class of product or process. | yes | the WATCH register · the variable registry · the writing guide |
| **handbook** | NASA-HDBK | Guidance. "Should." Forbids nothing. | no | the MCDP one-sheets · the CK3 IA study · the explainers · the DOPE SHEET pattern |

**Spec** is a tag, not a rung: one document saying what one specific product must be (DoD's MIL-SPEC). In the Command a spec is a node or a charter: the BOLO 24 charter, every canon node's invariants, a persona sheet.

## The rule that decides the rung

1. **If it forbids nothing, it is a handbook** (DOCTRINE 0, Invariant III: a rule that forbids nothing is decoration). Handbooks say "should".
2. **If it measures a product, it is a standard.** A standard's "shall" is testable against the thing.
3. **If it governs how the Command works, it is a procedure.** Its "shall" is testable against the transcript and the record.
4. **If it says what the Command is and why, it is policy.** The policy rung stays tiny: DOCTRINE 0 and nothing else until something earns it (Invariant I).

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
| `_CANON_NODES/dcus-standards-body.md` | spec | stamped at birth, 2026-09-15 (BOLO 50 phase 5) |
| `_CANON_NODES/oxo-trash-land-standards-body.md` | spec | stamped at birth, 2026-09-15 (BOLO 50 phase 5) |
| `_CANON_NODES/astro7ex-standards-body.md` | spec | stamped at birth, 2026-09-15 (BOLO 50 phase 5) |
| `_CANON_NODES/*.md` (34 files) | spec | listed by folder; tagged one by one as each node is next touched |

## The network · flat index (phase 6, 2026-09-15)

This index links all 26 filed Command documents in the BOLO 50 network to the Command level or project they govern, to the other filed documents they depend on, and to their outside parents in the standards register. Read Table 1 document by document, Table 2 body by body, Table 3 level by level; a browsable page comes later, once the count earns it.

### Table 1 · By document

| Document | Rung | Governs | Command parents | Outside parents |
|---|---|---|---|---|
| `DOCTRINE-0-INVARIANTS.md` | policy | the Command | none | none in the register |
| `SOP.md` | procedure | the session | none | none in the register |
| `📐 ssot_05_operations_project_flow.md` | procedure | the project (applies_to: BOLD_VENTURE, ULTRASIN, OPERATOR) | `SOP.md`, `DOCTRINE-0-INVARIANTS.md`, `📐 ssot_05_operations_development_standard.md`, `📐 ssot_05_operations_pm_holdings_inventory.md`, `🧬 MIL.01 — MCDP 1 Warfighting — USMC (1997).md`, `🧬 MIL.03 — MCDP 1-2 Campaigning — USMC (1997).md`, `🧬 MIL.07 — MCDP 4 Logistics — USMC (2023).md`, `🧬 MIL.08 — MCDP 5 Planning — USMC (1997).md`, `🧬 MIL.09 — MCDP 6 Command and Control — USMC (1996).md`, `🧬 MIL.11 — MCDP 8 Information — USMC (2022).md` | PMI standards — PMBOK Guide (8th ed.) + Practice Guides + global standards (register) |
| `📐 ssot_05_operations_development_standard.md` | procedure | the build loop inside a session (applies_to: BOLD_VENTURE, ULTRASIN, OPERATOR) | `SOP.md`, `📐 ssot_05_operations_project_flow.md`, `DOCTRINE-0-INVARIANTS.md`, `standards.register.md` | none in the register |
| `📐 ssot_05_operations_standards_ladder.md` | procedure | the Command, document rung classification (applies_to: BOLD_VENTURE, ULTRASIN, OPERATOR) | `DOCTRINE-0-INVARIANTS.md`, `SOP.md`, `📐 ssot_05_operations_project_flow.md`, `📐 ssot_05_operations_development_standard.md`, `standards.register.md` | NASA NODIS directives (register); DLA Defense Standardization Program (register) |
| `📐 ssot_05_operations_markdown_marking.md` | procedure | BVX-LEARN · OVEREXITOUT · ASTRO7EX · SSOT (applies_to) | `📐 ssot_writing_guide.md`, `📐ssot_SSOT_CREATION.md`, `📐 ssot_template_prompt_for_summarizing_novels_and_books.md` | none in the register |
| `📐ssot_SSOT_CREATION.md` | procedure | unscoped (applies_to blank) | none | none in the register |
| `📐ssot_variable_registry.md` | standard | unscoped (no applies_to given) | none | none in the register |
| `WATCH-REGISTER.md` | standard | WARROOM | none | MIL-STD-1472H — DoD Design Criteria Standard: Human Engineering (register) |
| `📐 ssot_writing_guide.md` | standard | OVEREXITOUT · ASTRO7EX · LAKAD (applies_to) | `📐_ssot_05_operations_standard_structure_template.md` | none in the register |
| `CK3-IA-STUDY.md` | handbook | the MCDP Doctrine Browser (a planned tool, per title-line) | none | none in the register |
| `🧬 MIL.01 — MCDP 1 Warfighting — USMC (1997).md` | handbook | the project (feeds the project flow's methodology) | none | USMC MCDP corpus (outside the register) |
| `🧬 MIL.02 — MCDP 1-1 Strategy — USMC (1997).md` | handbook | the project | none | USMC MCDP corpus (outside the register) |
| `🧬 MIL.03 — MCDP 1-2 Campaigning — USMC (1997).md` | handbook | the project | none | USMC MCDP corpus (outside the register) |
| `🧬 MIL.04 — MCDP 1-3 Tactics — USMC (1997).md` | handbook | the project | none | USMC MCDP corpus (outside the register) |
| `🧬 MIL.05 — MCDP 2 Intelligence — USMC (1997).md` | handbook | the project | none | USMC MCDP corpus (outside the register) |
| `🧬 MIL.06 — MCDP 3 Expeditionary Operations — USMC (1998).md` | handbook | the project | none | USMC MCDP corpus (outside the register) |
| `🧬 MIL.07 — MCDP 4 Logistics — USMC (2023).md` | handbook | the project | none | USMC MCDP corpus (outside the register) |
| `🧬 MIL.08 — MCDP 5 Planning — USMC (1997).md` | handbook | the project | none | USMC MCDP corpus (outside the register) |
| `🧬 MIL.09 — MCDP 6 Command and Control — USMC (1996).md` | handbook | the project | none | USMC MCDP corpus (outside the register) |
| `🧬 MIL.10 — MCDP 7 Learning — USMC (2020).md` | handbook | the project | none | USMC MCDP corpus (outside the register) |
| `🧬 MIL.11 — MCDP 8 Information — USMC (2022).md` | handbook | the project | none | USMC MCDP corpus (outside the register) |
| `BOLO-24-charter.md` | spec | ORANGE | `📐 ssot_05_operations_project_flow.md` (type field: "first live instance of") | none in the register |
| `dcus-standards-body.md` | spec | DCUS | none | none in the register |
| `oxo-trash-land-standards-body.md` | spec | Trash Land | none | none in the register |
| `astro7ex-standards-body.md` | spec | ASTRO7EX | none | none in the register |

### Table 2 · By outside body

| Body / family | What the Command takes from it | Command documents that cite it | Free or paid |
|---|---|---|---|
| NASA | The NPD → NPR → NASA-STD/NASA-HDBK directive tiers, borrowed as the Command's own policy/procedure/standard/handbook ladder | `📐 ssot_05_operations_standards_ladder.md` | Free, public NODIS library (266 current directives); some need internal NASA access |
| DoD (DSP/DLA) | The MIL-STD → MIL-HDBK → MIL-SPEC/MIL-DTL → MIL-PRF tiering, for the spec-as-tag concept; separately, MIL-STD-1472H's human-engineering criteria for the WATCH register's day/night polarity rule | `📐 ssot_05_operations_standards_ladder.md`, `WATCH-REGISTER.md` | Free via ASSIST (116,970 documents indexed) |
| PMI | The PMBOK Guide's project/program/portfolio body of knowledge, folded into the Command's six-phase project-flow methodology | `📐 ssot_05_operations_project_flow.md` | Free overview; full text needs membership/purchase |

### Table 3 · By level and world

| Level or world | Its standards body | Documents on its rungs | Gaps |
|---|---|---|---|
| the Command | HOTLINE ACTUAL | policy: `DOCTRINE-0-INVARIANTS.md`; procedure: `📐 ssot_05_operations_standards_ladder.md`; standard: none; handbook: none; spec: none | standard and handbook empty |
| the session | HOTLINE ACTUAL | policy: none; procedure: `SOP.md`, `📐 ssot_05_operations_development_standard.md`; standard: none; handbook: none; spec: none | policy, standard, handbook, spec empty |
| the project | HOTLINE ACTUAL | policy: none; procedure: `📐 ssot_05_operations_project_flow.md`; standard: none; handbook: all 11 MIL one-sheets (`🧬 MIL.01`–`🧬 MIL.11`); spec: none | standard and spec empty (specs are filed per-instance, e.g. ORANGE, not at the generic project level) |
| BLACK | HOTLINE ACTUAL | none on any rung | all four rungs empty; no filed document governs BLACK directly (the name appears only in the register's Command-area column, as BVX) |
| ORANGE | HOTLINE ACTUAL | policy: none; procedure: none; standard: none; handbook: none; spec: `BOLO-24-charter.md` | policy, procedure, standard, handbook empty |
| OPERATOR | HOTLINE ACTUAL | policy: none; procedure: `📐 ssot_05_operations_project_flow.md`, `📐 ssot_05_operations_development_standard.md`, `📐 ssot_05_operations_standards_ladder.md`; standard: none; handbook: none; spec: none | policy, standard, handbook, spec empty |
| DCUS | The Administration | policy: none; procedure: none; standard: none; handbook: none; spec: `dcus-standards-body.md` | policy, procedure, standard, handbook empty |
| Trash Land | the border itself (no named institution; region name itself UNRULED, per spec node) | policy: none; procedure: none; standard: none; handbook: none; spec: `oxo-trash-land-standards-body.md` | policy, procedure, standard, handbook empty |
| ASTRO7EX | unnamed life-support/certification authority (working title; unkeyed to a place until the moon question is ruled) | policy: none; procedure: none; standard: none; handbook: none; spec: `astro7ex-standards-body.md` | policy, procedure, standard, handbook empty |
| DARKROOM | HOTLINE ACTUAL | none on any rung | all four rungs empty; no filed document governs DARKROOM directly (the name appears only in the register's Command-area column) |
| WARROOM | HOTLINE ACTUAL | policy: none; procedure: none; standard: `WATCH-REGISTER.md`; handbook: none; spec: none | policy, procedure, handbook, spec empty |

**Gaps the index shows**

- `WATCH-REGISTER.md`'s lead cites both MIL-STD-1472H and FAA HF-STD-001B, but only MIL-STD-1472H is a register row; FAA HF-STD-001B does not appear anywhere in the register's sections 1-2.
- Five of the eleven MCDP one-sheets (MIL.02 Strategy, MIL.04 Tactics, MIL.05 Intelligence, MIL.06 Expeditionary Operations, MIL.10 Learning) are filed at the handbook rung but no other filed document's frontmatter names them as a dependency; only MIL.01, MIL.03, MIL.07, MIL.08, MIL.09, and MIL.11 are wired into `📐 ssot_05_operations_project_flow.md`.
- BLACK and DARKROOM have no filed document governing them among the 26; both names surface only in the standards register's Command-area column, never as a governs target in this network.
- 12 of the 26 filed documents carry no outside parent at all: `DOCTRINE-0-INVARIANTS.md`, `SOP.md`, `📐 ssot_05_operations_development_standard.md`, `📐 ssot_05_operations_markdown_marking.md`, `📐ssot_SSOT_CREATION.md`, `📐ssot_variable_registry.md`, `📐 ssot_writing_guide.md`, `CK3-IA-STUDY.md`, `BOLO-24-charter.md`, and the three in-world standards-body nodes (DCUS, Trash Land, ASTRO7EX).
- The Command's own generic handbook rung is empty; the only handbooks in the network sit at the project level (the 11 MIL one-sheets) or govern a still-unbuilt tool (`CK3-IA-STUDY.md`, the MCDP Doctrine Browser).
- Trash Land and ASTRO7EX have no named standards-body entity yet; both spec nodes record the body as a working title rather than a proper name.

## Governance

DOCTRINE 0 governs: this ladder is v0.1, ruled, and promotes to canonical after two filing passes. Phase 4 of BOLO 50 was the first pass. The next document written in the Command carries the tag from birth; a document found without one is filed at the next sit rep.

## Version History

| Version | Date | Changes |
|---|---|---|
| 0.1.0 | 2026-09-15 | Ruled: the NASA four (policy · procedure · standard · handbook), spec as a tag. First filing pass: 20 documents stamped, 2 listed. |
| 0.2.0 | 2026-09-15 | Phase 6, the network: flat index added (by document · by outside body · by level and world · the gaps). 26 documents, 3 outside bodies cited, 11 levels and worlds. The browsable page waits on the count. |
