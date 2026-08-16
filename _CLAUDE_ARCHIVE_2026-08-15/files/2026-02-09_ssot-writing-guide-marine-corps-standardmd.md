---
original_path: "/mnt/user-data/outputs/ssot_writing_guide_marine_corps_standard.md"
source_conversation: "MAIN SONNET"
created: 2026-02-09
trunk: BLACK
kind: generated-file
---

---
type: ssot_operations
category: operations
version: 1.0.0
last_updated: 2026-02-10
applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD]
status: canonical
purpose: Defines how to create and maintain SSOT documents using Marine Corps doctrinal publication standards
---

# SSOT Writing Guide: Marine Corps Doctrine Standard

## Table of Contents
1. [Purpose](#purpose)
2. [What is an SSOT](#what-is-an-ssot)
3. [SSOT vs Authoritative](#ssot-vs-authoritative)
4. [Marine Corps Doctrinal Standards](#marine-corps-doctrinal-standards)
5. [Mandatory Components](#mandatory-components)
6. [Template Location](#template-location)
7. [Writing Rules](#writing-rules)
8. [Language Requirements](#language-requirements)
9. [Structural Requirements](#structural-requirements)
10. [Versioning](#versioning)
11. [For AI Assistants](#for-ai-assistants)
12. [Version History](#version-history)

---

## Purpose

This document establishes the authoritative standard for creating Single Source of Truth (SSOT) documentation within the LEECHSEED narrative development system. It applies Marine Corps doctrinal publication principles to ensure clarity, authority, and consistency across all methodology documentation.

---

## What is an SSOT

**Single Source of Truth** is methodology that applies across all narrative projects.

An SSOT defines how a system works. It is not the application of that system to a specific story.

**Examples of SSOT:**
- How character astrology works (applies to OVEREXITOUT, ASTRO7EX, LAKAD)
- How to ascertain truth (epistemology framework)
- Dramatica integration rules
- Plot structure methodology

**Not SSOT:**
- Victoria Midnight's character sheet (Authoritative - story-specific)
- OVEREXITOUT plot outline (Authoritative - story-specific)
- Scene drafts (Workshop material)

---

## SSOT vs Authoritative

| SSOT | Authoritative |
|------|--------------|
| Methodology | Application |
| Applies to ALL stories | Story-specific |
| How the system works | Using the system on specific content |
| Abstract and general | Concrete and specific |
| Example: "Narrative Astrology 15 Categories Framework" | Example: "Victoria Midnight Astrology Profile" |
| Location: `_CANON/_SSOT/` | Location: `_CANON/_AUTHORITATIVE/[STORY]/` |

---

## Marine Corps Doctrinal Standards

SSOT documents follow MCDP (Marine Corps Doctrinal Publication) writing standards for clarity, authority, and utility.

### Core Principles from MCDP-1 Warfighting

**Authoritative Foundation**
> "This publication provides the authoritative basis for how we fight and how we prepare to fight."

SSOTs provide the authoritative basis for how narrative systems work. They are not suggestions. They are doctrine.

**Philosophy Over Procedure**
> "This book contains no specific techniques or procedures for conduct. Rather, it provides broad guidance in the form of concepts and values."

SSOTs define concepts and principles. Authoritative documents apply those principles to specific content.

**Requires Judgment**
> "It requires judgment in application."

SSOTs establish frameworks. Users exercise judgment when applying frameworks to specific situations.

**Continuous Evolution**
> "Doctrine must continue to evolve based on growing experience, advancements in theory, and the changing face of war itself."

SSOTs are versioned. They evolve. They improve. They are never final.

---

## Mandatory Components

Every SSOT must contain these sections in this order:

1. **Frontmatter** (YAML format - exact structure required)
2. **Title** (Clear, descriptive)
3. **Table of Contents** (mandatory, non-negotiable)
4. **Purpose** (Single paragraph stating what this SSOT defines)
5. **Core Concepts** (The methodology itself)
6. **Implementation** (How to use the methodology)
7. **Examples** (Minimum two concrete examples)
8. **References** (Dependencies and sources)
9. **Version History** (Table format)

Missing any section renders the SSOT incomplete and non-canonical.

---

## Template Location

**Do not write SSOT documents from scratch.**

Always copy from: `_CANON/_TEMPLATES/ssot/ssot_template.md`

This ensures:
- Consistent structure
- No missing mandatory sections
- Proper frontmatter format
- AI parsability
- Human readability

---

## Writing Rules

### Rule 1: Write for Both Humans and AIs

Documents must be parsable by:
- Human readers (clarity, flow)
- AI assistants (structure, explicit definitions)
- Future maintainers (no implicit context)

### Rule 2: One Concept Per SSOT

Do not combine unrelated methodologies in a single document.

**Wrong:** "Character Systems and Plot Systems Combined Guide"
**Right:** Two separate documents

### Rule 3: Link Dependencies Explicitly

If SSOT A requires understanding SSOT B, declare it in frontmatter:

```yaml
dependencies:
  - narrative_astrology_15_categories
  - planetary_dignities
```

### Rule 4: Use Examples Liberally

Every concept requires at least two examples.

Examples must be:
- Concrete (specific scenarios)
- Clear (no ambiguity)
- Diverse (show range of application)

### Rule 5: No Story-Specific Content

If you reference specific characters, plots, or story elements, the document is Authoritative, not SSOT.

**Keep methodology abstract and general.**

---

## Language Requirements

### Declarative Authority

Use declarative statements. This is doctrine, not suggestion.

**Use:**
- "The system works this way."
- "Apply this framework."
- "This defines..."

**Avoid:**
- "The system might work this way."
- "You could try..."
- "This possibly defines..."

### Active Voice

Use active voice. Be direct.

**Use:**
- "Define the character's Mars placement."
- "Apply the 15-category framework."

**Avoid:**
- "The character's Mars placement should be defined."
- "The 15-category framework can be applied."

### Present Tense

Write in present tense. SSOT describes current methodology.

**Use:**
- "The framework consists of..."
- "This method produces..."

**Avoid:**
- "The framework will consist of..."
- "This method would produce..."

### Economy of Language

Remove all unnecessary words.

**Eliminate:**
- Hedging: "perhaps", "maybe", "possibly", "might", "could"
- Qualifiers: "very", "really", "quite", "somewhat"
- Redundancy: "completely finished", "end result", "future plans"
- Conversational filler: "basically", "actually", "just", "simply"

### Precision

Use precise terms. Define them on first use.

**Example:**
> The **Dramatica-Astrology Interface (DAI)** maps Dramatica's 64 story elements to astrological chart positions. DAI operates by...

**Bold key terms on first use only.**

---

## Structural Requirements

### Hierarchical Levels

Use exactly four heading levels:

```markdown
# Document Title (H1 - Once only)
## Major Section (H2)
### Subsection (H3)
#### Sub-subsection (H4 - use sparingly)
```

Do not use H5 or H6. Restructure if needed.

### Lists

**Numbered lists** for sequences and procedures:
1. First action
2. Second action
3. Third action

**Bulleted lists** for concepts and options:
- Concept one
- Concept two
- Concept three

### Paragraph Length

Maximum 5 sentences per paragraph.

One idea per paragraph.

No walls of text.

### Tables

Use tables for:
- Comparisons
- Definitions
- Version history
- Quick reference

Tables must have clear headers.

### Code Blocks

Use fenced code blocks for:
- Example frontmatter
- Data structures
- Command examples

Label the language:
````markdown
```yaml
example: content
```
````

---

## Versioning

Format: `MAJOR.MINOR.PATCH`

**MAJOR**: Fundamental methodology change (breaks existing implementations)
- Example: Complete restructure of framework
- Old implementations no longer work
- Requires updating all dependent Authoritative docs

**MINOR**: New features or sections added (backward compatible)
- Example: Added new character technique
- Old implementations still work
- New capabilities available

**PATCH**: Clarifications, corrections, formatting
- Example: Fixed typo in example
- No methodology change
- Pure cleanup

### Version History Table

Every SSOT ends with:

```markdown
## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-02-10 | Initial creation |
| 1.1.0 | 2026-02-15 | Added Mars aspect variations |
| 1.1.1 | 2026-02-16 | Clarified terminology in examples |
```

---

## For AI Assistants

When creating or updating an SSOT:

### Step 1: Read This Guide
Always read this guide before creating any SSOT document.

### Step 2: Use the Template
Always copy from `_CANON/_TEMPLATES/ssot/ssot_template.md`

### Step 3: Check for Existing SSOTs
Search `_CANON/_SSOT/` before creating new documents. Avoid duplication.

### Step 4: Verify SSOT vs Authoritative
Ask the user: "Is this methodology (SSOT) or story-specific application (Authoritative)?"

### Step 5: Follow Marine Corps Standards
Apply all language and structural requirements from this guide.

### Step 6: Include All Mandatory Sections
No section may be skipped or omitted.

### Step 7: Submit for Review
User reviews all AI-generated SSOTs for:
- Template compliance
- Complete sections
- Proper categorization
- Marine Corps doctrine standards

### Trust But Verify

Templates and standards prevent hallucination. Structure is non-negotiable.

**If you are uncertain about any requirement, ask the user.**

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-02-10 | Initial SSOT writing guide created with Marine Corps doctrine standards |
