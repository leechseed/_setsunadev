---
type: ssot_methodology
category: operations
version: 1.8.0
last_updated: 2026-02-12
applies_to:
  - OVEREXITOUT
  - ASTRO7EX
  - LAKAD
status: canonical
purpose: "This document establishes the authoritative standard for SSOT creation, including manual 'kickstart' protocols for Obsidian Properties."
dependencies:
  - "[[📐_ssot_05_operations_obsidian_yaml_standard]]"
---

# 📐 SSOT Writing Guide: Marine Corps Doctrinal Standard

## Table of Contents

1. [Purpose](#purpose)
2. [Linguistic Authority Standards](#linguistic-authority-standards)
3. [The SSOT Creation Process: Step-by-Step](#the-ssot-creation-process-step-by-step)
4. [The Manual UI Kickstart Protocol](#the-manual-ui-kickstart-protocol)
5. [File Naming and Metadata](#file-naming-and-metadata)
6. [Version History](#version-history)

---

## Purpose

This document defines the structural and linguistic requirements for **Single Source of Truth (SSOT)** documentation. It ensures all frameworks remain canonical, precise, and functionally integrated into the Obsidian knowledge base.

## Linguistic Authority Standards

- **No Contractions:** "Do not" / "It is" / "Cannot."
- **No Hedging:** Eliminate "basically," "might," or "likely."
- **Present Tense:** All systems are described in their current operational state.
- **Bold Definitions:** **Bold** the first instance of technical terminology.

---

## The SSOT Creation Process: Step-by-Step

### Phase 1: Classification

Determine if the content is a methodology. If it is project-specific content, divert it to `_AUTHORITATIVE/`.

### Phase 2: Content Generation

Draft the core methodology and examples. Ensure the language follows the Marine Corps Doctrinal Standard.

### Phase 3: YAML Initialization

Generate the Obsidian-compliant YAML block.

> **Note:** Use the standardized template to ensure keys like `type`, `category`, and `applies_to` are present.

### Phase 4: The Manual UI Kickstart

If the YAML appears as a code block rather than the Properties UI, execute the **Kickstart Protocol** detailed below.

### Phase 5: Naming and Storage

Save with the `📐 ssot_` prefix in the `_CANON/_SSOT/` directory.

---

## The Manual UI Kickstart Protocol

When pasting YAML from an external source (AI or Clipboard), Obsidian may fail to recognize the metadata. To force the **Properties UI** to trigger:

1.  Ensure the first `---` is at the absolute top of the file (Line 1, Column 1).
2.  If it remains a code block, delete the first `---`.
3.  **Manually type** three dashes `---` at the top.
4.  This action triggers the Obsidian listener and "clicks" the YAML into the Property UI.

---

## File Naming and Metadata

### Naming Convention

- **Format:** `📐 ssot_[category]_[name].md`
- **Rules:** Lowercase, underscores instead of spaces.

### Emoji Taxonomy

- **📐 SSOT:** Methodology/Framework.
- **🎯 Authoritative:** Story/Project content.
- **⚙️ Operations:** Workflow/AI Instructions.

---

## Version History

| Version | Date       | Changes                                                          |
| :------ | :--------- | :--------------------------------------------------------------- |
| 1.0.0   | 2026-02-10 | Initial Marine Corps standard.                                   |
| 1.7.0   | 2026-02-12 | Added metadata troubleshooting.                                  |
| 1.8.0   | 2026-02-12 | Integrated Manual UI Kickstart Protocol for Obsidian compliance. |

---

**Pro-Tip:** If you're using the **Templater** plugin in Obsidian, you can actually set this up to happen automatically, but for now, the "manual dash" trick is the most reliable way to ensure your knowledge base stays clean and indexed. Ready for the next document?
