---
type: ssot_methodology
category: operations
version: 1.0.2
last_updated: 2026-02-12
applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD]
status: canonical
purpose: "Defines the mandatory structural payload for all SSOT documents to ensure system-wide interoperability and proper Obsidian Property rendering."
dependencies: ["[[📐_ssot_05_operations_writing_guide]]"]
---

# 📐 ssot_05_operations_standard_structure_template

## Table of Contents

1. [Purpose](#purpose)
2. [Structural Components](#structural-components)
3. [The Logic of Order](#the-logic-of-order)
4. [Implementation](#implementation)
5. [Examples](#examples)
6. [Version History](#version-history)

---

## Purpose

This document provides the mandatory structural blueprint for all Single Source of Truth (SSOT) documentation. It ensures that every methodology within the LEECHSEED system is organized identically, starting with a raw triple-dash YAML boundary to guarantee Obsidian Property rendering.

---

## Structural Components

Every SSOT document must contain the following eight components in the specified sequence. Omission of any component, particularly the leading boundary dashes, renders the document non-canonical.

1.  **YAML Frontmatter**: The Obsidian-compliant metadata block, starting and ending with `---`.
2.  **H1 Document Title**: Prefixed with 📐 and the `ssot_` designation.
3.  **Table of Contents**: A hierarchical list of internal document links.
4.  **Purpose Statement**: A single paragraph defining the document scope.
5.  **Core Methodology**: The primary exposition of the system logic and rules.
6.  **Implementation**: Practical, step-by-step instructions for use.
7.  **Examples**: Minimum of two hypothetical scenarios demonstrating the framework.
8.  **Version History**: A tabular record of all document revisions.

---

## The Logic of Order

The sequence of components is designed to mirror the practitioner's cognitive workflow:

- **Metadata First**: Allows the Obsidian database to index the file before the human reads it.
- **Purpose Before Depth**: Ensures the practitioner understands the "Why" before the "How."
- **Examples Last**: Provides a practical anchor for the abstract concepts discussed in the Core Methodology.

---

## Implementation

### Using the Template

1.  **Initialize**: Open a new Markdown file.
2.  **Boundary Setup**: Type `---` on the very first line. This is the mandatory start for the Obsidian Properties UI.
3.  **Metadata Entry**: Populate the flat-syntax YAML fields (e.g., `type: ssot_methodology`).
4.  **Close Boundary**: Type `---` to end the frontmatter.
5.  **Content Drafting**: Follow the H1/H2 structure defined in the [Structural Components](#structural-components) section.

### Verification

A document is "Standard Compliant" only if it passes the **Doctrinal Sweep**:

- [ ] No contractions are present.
- [ ] No hedging language exists.
- [ ] All technical terms are **Bolded** upon first mention.

---

## Examples

### Example 1: Movement Framework SSOT

A document defining the systemic state of "Corruption" (Movement 3) must follow this template to ensure it interfaces correctly with the "Legibility" (Movement 1) SSOT.

### Example 2: Character System SSOT

The **Narrative Astrology Framework** utilizes this template to provide a deterministic rendering engine that can be applied to any story-specific profile.

---

## Version History

| Version | Date       | Changes                                                                    |
| :------ | :--------- | :------------------------------------------------------------------------- |
| 1.0.0   | 2026-02-12 | Initial standardization of the SSOT structural payload.                    |
| 1.0.2   | 2026-02-12 | Refined for absolute YAML boundary compliance and flat-syntax integration. |
