---
title: "SSOT writing guide: reference"
type: reference
for: "A writer or reviewer looking up one SSOT language, frame or YAML rule"
does: "Lists every component of the SSOT writing guide 07.2a"
owner: Chief
state: draft
reviewed: 2026-10-05
source: "ShroomsQ/_CANON/_SSOT/07_STYLE_GUIDES/📐 ssot_07_2a_writing_guide.md"
source_version: "2.2.2"
---

**Who it's for:** a writer or reviewer looking up one rule · **What it does:** lists every component of 07.2a · **Type:** reference

# SSOT writing guide: reference

One entry per component of the source, in source order. The guide is a module of [07.2 documents style](../ssot_07_2_documents_style/2-reference.md). See the [concept](1-concept.md) for the why.

## Linguistic Authority Standards

Every SSOT document follows these constraints.

| Rule | What it requires |
|---|---|
| No Hedging | Qualifiers such as "basically," "perhaps," or "maybe" are prohibited. |
| Present Tense | The writer describes methodology as an active, perpetual reality. |
| Technical Precision | The first instance of a technical term is **bold** and defined at once. Bold belongs to the writer. A reader marking a document uses `==highlight==`, never bold. |
| Active Voice | Subjects perform specified actions without ambiguity. |
| Contractions allowed | RULED 2026-10-04 (BOLO 92 merge call 1). The older ban is struck. |

Connects to: [07.2b markdown marking](../ssot_07_2b_markdown_marking/2-reference.md) for the reader's mark. It also connects to 07.2 rule 3.2 for the reasoning on contractions.

## Structural Requirements

Every SSOT document keeps one frame (RULED 2026-10-04, BOLO 92 merge call 2). The body follows the page's type (07.2 rules 1.1–1.2).

1. **YAML Boundary:** begins on line 1 with `---`.
2. **Document Title:** an H1 prefixed with 📐 and `ssot_`.
3. **Table of Contents:** linked hierarchical navigation.
4. **Purpose Statement:** a single paragraph defining the document's scope.
5. **The body, by type:**
   - A concept page carries Core Methodology and at least two Examples.
   - A reference page carries the facts as tables or entries.
   - A how-to carries numbered steps.
   - A tutorial carries one lesson start to finish.
   - One page, one type.
6. **Version History:** a tabular record of revisions.

Reviewer rule: name the page's type first, then check the body against that type's rule.

## The Flat-Syntax YAML Standard

All metadata uses flow style for lists, to guarantee Obsidian Property rendering.

| Item | Form |
|---|---|
| Lists | `[Value 1, Value 2]` |
| Wikilinks | `"[[Document_Name]]"`, double-quoted |
| Key spacing | `key: value`, with a space after the colon |

**The header fields** (RULED 2026-10-04, BOLO 92 merge call 3): every new or reviewed document adds these.

| Field | Value |
|---|---|
| `reader` | who the page is for |
| `doc_type` | tutorial · how-to · reference · concept |
| `owner` | who decides what the page says |
| `state` | draft · ruled · retired |
| `reviewed` | a date |

`status` and `last_updated` stay until the schema pass.

The dependency template is `♨️_template_ssot_09_operations_standard_structure_template`. It has eight components, in order. They are YAML frontmatter, H1 title, Table of Contents, Purpose, Core Methodology, Implementation, Examples and Version History.

Its YAML keys are `type`, `category`, `version`, `last_updated`, `applies_to`, `status`, `purpose` and `dependencies`.

Chief decides when the five header fields join the template: now, or at the schema pass. The fields are `reader`, `doc_type`, `owner`, `state` and `reviewed`.
