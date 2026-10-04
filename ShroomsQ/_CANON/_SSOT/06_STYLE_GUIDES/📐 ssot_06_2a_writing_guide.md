---
type: ssot_05_operations
category: operations
version: 2.2.0
last_updated: 2026-10-04
reader: "anyone writing or reviewing an SSOT document"
doc_type: reference
owner: "Chief (HOTLINE ACTUAL); Claude keeps it"
state: ruled
reviewed: 2026-10-04
applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD]
status: canonical
purpose: "Defines mandatory linguistic and structural standards for SSOT documentation using Marine Corps doctrinal precision."
dependencies: ["[[📐_ssot_05_operations_standard_structure_template]]"]
moved: "2026-09-29 from 05_OPERATIONS/📐 ssot_writing_guide.md to 06_STYLE_GUIDES/📐 ssot_06_2a_writing_guide.md (BOLO 92)"
---

# 📐 ssot_05_operations_writing_guide

## Table of Contents

1. [Purpose](#purpose)
2. [Linguistic Authority Standards](#linguistic-authority-standards)
3. [Structural Requirements](#structural-requirements)
4. [The Flat-Syntax YAML Standard](#the-flat-syntax-yaml-standard)
5. [Version History](#version-history)

---

## Purpose

This document establishes the authoritative standard for Single Source of Truth (SSOT) documentation. It ensures all frameworks remain canonical, precise, and functionally optimized for the Obsidian Properties UI through rigid linguistic and structural constraints.

---

## Linguistic Authority Standards

To maintain doctrinal authority, all SSOT documentation must adhere to the following constraints:

- **No Hedging**: Qualifiers such as "basically," "perhaps," or "maybe" are prohibited.
- **Present Tense**: Methodology is described as an active, perpetual reality.
- **Technical Precision**: The first instance of a technical term must be **Bolded** and defined immediately. Bold belongs to the writer; a reader marking a document uses `==highlight==`, never bold. See [[📐 ssot_05_operations_markdown_marking]].
- **Active Voice**: Subjects must perform specified actions without ambiguity.
- **Contractions allowed** (RULED 2026-10-04, BOLO 92 merge call 1): the older ban is struck; text reads clean out loud ([06.2 core](📐%20ssot_06_2_documents_style.md) rule 3.2).

---

## Structural Requirements

Every SSOT document keeps one frame (RULED 2026-10-04, BOLO 92 merge call 2; the body follows the page's type, [06.2 core](📐%20ssot_06_2_documents_style.md) rules 1.1–1.2):

1.  **YAML Boundary**: Must begin on Line 1 with `---`.
2.  **Document Title**: H1 prefixed with 📐 and `ssot_`.
3.  **Table of Contents**: Linked hierarchical navigation.
4.  **Purpose Statement**: Single paragraph defining document scope.
5.  **The body, by type**: a **concept** page carries Core Methodology and at least two Examples; a **reference** page carries the facts as tables or entries; a **how-to** carries numbered steps; a **tutorial** carries one lesson start to finish. One page, one type.
6.  **Version History**: Tabular record of revisions.

---

## The Flat-Syntax YAML Standard

To guarantee Obsidian Property rendering, all metadata must use **Flow Style** for lists:

- **Lists**: `[Value 1, Value 2]`
- **Wikilinks**: `"[[Document_Name]]"` (must be double-quoted).
- **Key Spacing**: `key: value` (mandatory space after colon).
- **The header fields** (RULED 2026-10-04, BOLO 92 merge call 3; 06.2 core rules 2.1–2.3): every new or reviewed document adds `reader`, `doc_type` (tutorial · how-to · reference · concept), `owner`, `state` (draft · ruled · retired), and `reviewed` (a date). `status` and `last_updated` stay until the schema pass.

---

## Version History

| Version | Date       | Changes                                                   |
| :------ | :--------- | :-------------------------------------------------------- |
| 1.0.0   | 2026-02-10 | Initial Marine Corps standard.                            |
| 2.1.0   | 2026-02-12 | Integrated Flat-Syntax and triple-dash boundary mandates. |
| 2.1.1   | 2026-09-29 | Moved to 06_STYLE_GUIDES/📐 ssot_06_2a_writing_guide.md (BOLO 92); no content change. |
| 2.2.0   | 2026-10-04 | BOLO 92 merge calls ruled: contractions allowed · frame kept, body by type · header fields added · the pasted-in Goon Room protocol split out to 05_OPERATIONS. |
