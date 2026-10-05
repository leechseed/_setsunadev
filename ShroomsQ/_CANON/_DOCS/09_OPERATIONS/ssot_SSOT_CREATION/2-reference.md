---
title: "SSOT creation guide: reference"
type: reference
for: "a writer looking up an SSOT writing rule, process phase, or naming rule"
does: "lists every standard, phase, and naming rule of the SSOT creation guide"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/09_OPERATIONS/📐ssot_SSOT_CREATION.md
source_version: 1.8.2
---

**Who it's for:** a writer looking up an SSOT writing rule, process phase, or naming rule · **What it does:** lists every standard, phase, and naming rule of the SSOT creation guide · **Type:** reference

# SSOT creation guide: reference

The source has type `ssot_methodology`, category operations, status canonical, version 1.8.2, last updated 2026-10-05. It applies to OVEREXITOUT, ASTRO7EX, LAKAD. Its stated purpose: it "establishes the authoritative standard for SSOT creation, including manual 'kickstart' protocols for Obsidian Properties."

## Linguistic Authority Standards

Four rules govern the language:

- **Contractions Allowed:** "Do not" and "don't" both stand. The 07.2 style guide rules this (BOLO 92 merge call 1).
- **No Hedging:** eliminate "basically," "might," or "likely."
- **Present Tense:** all systems are described in their current operational state.
- **Bold Definitions:** **Bold** the first instance of technical terminology.

## The SSOT Creation Process: Step-by-Step

Five phases, run in order. Each phase is one part below.

### Phase 1: Classification

The writer determines whether the content is a methodology. Project-specific content goes to `_AUTHORITATIVE/`.

### Phase 2: Content Generation

The writer drafts the core methodology and examples in the Marine Corps Doctrinal Standard language.

### Phase 3: YAML Initialization

The writer generates the Obsidian-compliant YAML block. The standardized template keeps the keys `type`, `category`, and `applies_to` present.

### Phase 4: The Manual UI Kickstart

If the YAML shows as a code block instead of the Properties UI, the writer runs the Kickstart Protocol. The Kickstart Protocol is the next component.

### Phase 5: Naming and Storage

The writer saves with the `📐 ssot_` prefix in the `_CANON/_SSOT/` directory.

## The Manual UI Kickstart Protocol

The protocol applies when YAML pasted from an external source (AI or clipboard) is not recognized. The four steps:

1. Ensure the first `---` is at the absolute top of the file (Line 1, Column 1).
2. If it remains a code block, delete the first `---`.
3. Manually type three dashes `---` at the top.
4. This triggers the Obsidian listener and "clicks" the YAML into the Property UI.

## File Naming and Metadata

### Naming Convention

- **Format:** `📐 ssot_[category]_[name].md`
- **Rules:** lowercase, underscores instead of spaces.

### Emoji Taxonomy

| Emoji | Meaning |
|---|---|
| 📐 SSOT | Methodology/Framework |
| 🎯 Authoritative | Story/Project content |
| ⚙️ Operations | Workflow/AI Instructions |

The author prefixes story or project content in `_AUTHORITATIVE/` with 🎯. The author names it `🎯 auth_[ip]_[name].md`, in lowercase with underscores. Chief rules whether the existing ingests and reports that carry 📐 there move to 🎯 or keep 📐.

The source also carries a closing "Pro-Tip" (use the Templater plugin to automate the kickstart). It also carries a five-row version history. Row one is 1.0.0 (initial Marine Corps standard). Row two is 1.7.0 (metadata troubleshooting). Row three is 1.8.0 (Manual UI Kickstart). Row four is 1.8.1 (contractions allowed, citing 07.2). Row five is 1.8.2 (the 🎯 prefix and name rule).
