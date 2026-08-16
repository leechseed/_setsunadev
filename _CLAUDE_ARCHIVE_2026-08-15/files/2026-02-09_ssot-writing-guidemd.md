---
original_path: "/mnt/user-data/outputs/📐📐_ssot_writing_guide.md"
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
purpose: Defines how to create and maintain SSOT documents using Marine Corps Chesty Puller standard
---

# 📐📐 SSOT Writing Guide: Chesty Puller Standard

## Table of Contents
1. [Mission](#mission)
2. [What is an SSOT](#what-is-an-ssot)
3. [SSOT vs Authoritative](#ssot-vs-authoritative)
4. [File Naming Standard](#file-naming-standard)
5. [Mandatory Components](#mandatory-components)
6. [Chesty Puller Language Standard](#chesty-puller-language-standard)
7. [Structural Requirements](#structural-requirements)
8. [Versioning](#versioning)
9. [For AI Assistants](#for-ai-assistants)
10. [Version History](#version-history)

---

## Mission

This document is doctrine.

It defines how you write SSOT documents.

Follow it or don't write SSOTs.

---

## What is an SSOT

**Single Source of Truth** = Methodology that applies to all stories.

An SSOT defines how systems work. Not how you used them once.

**SSOT:**
- Character astrology framework
- Truth verification methods
- Plot structure rules

**Not SSOT:**
- Victoria Midnight's character sheet
- OVEREXITOUT plot outline
- Your scene drafts

If it mentions a specific character or story, it's not SSOT.

---

## SSOT vs Authoritative

| SSOT | Authoritative |
|------|--------------|
| Methodology | Application |
| All stories | One story |
| How it works | How you used it |
| Abstract | Concrete |
| `_CANON/_SSOT/` | `_CANON/_AUTHORITATIVE/[STORY]/` |

---

## File Naming Standard

### Format

`[emoji]_[category]_[name].md`

### Emoji Standards

**📐** SSOT Documents (precision/measurement)
**🎯** Authoritative Documents (specific target)
**⚙️** Operations Documents (mechanism)
**📋** Templates (forms)
**❌** Deprecated (do not use)

### Mission-Critical Files

Use double emoji for foundational doctrine:

```
📐📐_ssot_writing_guide.md
⚙️⚙️_ops_mission_control.md
🎯🎯_auth_leechseed_core.md
```

### Rules

- Lowercase only
- Underscores for spaces
- No version numbers in filename
- Descriptive but brief

### Examples

```
📐_ssot_character_astrology.md
📐_ssot_truth_verification.md
🎯_auth_victoria_midnight.md
🎯_auth_plot_act_one.md
⚙️_ops_goon_room_workflow.md
📋_template_ssot_standard.md
❌_deprecated_old_system.md
```

---

## Mandatory Components

Every SSOT contains these sections. No exceptions.

1. **Frontmatter** (YAML - exact format)
2. **Title** (Clear, direct)
3. **Table of Contents** (mandatory)
4. **Mission** (What this defines)
5. **Core Concepts** (The methodology)
6. **Implementation** (How to use it)
7. **Examples** (Two minimum)
8. **References** (Dependencies)
9. **Version History** (Table format)

Skip a section, your SSOT is incomplete.

---

## Chesty Puller Language Standard

> "We're surrounded. That simplifies the problem."
> —Chesty Puller

Write like this. Direct. Clear. Deadly.

### Rule 1: State Facts

No hedging. No maybe. No perhaps.

**Right:**
- "This is how it works."
- "Apply the framework."
- "Execute now."

**Wrong:**
- "This might work."
- "You could try..."
- "Perhaps consider..."

If you're unsure, don't write.

### Rule 2: Active Voice

Passive voice is for cowards.

**Right:**
- "Define the character's Mars placement."
- "Execute the framework."
- "Apply pressure."

**Wrong:**
- "The placement should be defined."
- "The framework can be applied."
- "Pressure should be applied."

Own your actions.

### Rule 3: Kill Weak Words

Remove without mercy:

**KILL:**
- perhaps, maybe, possibly, might, could, potentially
- very, really, quite, somewhat, rather
- try to, attempt to, seek to
- basically, actually, just, simply, essentially

**Before:**
> "You might want to try applying the framework."

**After:**
> "Apply the framework."

### Rule 4: Present Tense

Write what IS. Not what might be.

**Right:**
- "The framework consists of 15 categories."
- "This method produces results."

**Wrong:**
- "The framework will consist of..."
- "This method would produce..."

### Rule 5: Short Sentences

Maximum 25 words per sentence.

Exceed this, you lose your reader.

**Wrong:**
> "The system combines traditional astrology with Dramatica's structure to create character profiles that reflect psychological complexity."

**Right:**
> "The system combines astrology with Dramatica structure. This creates deep character profiles. Profiles reflect psychological complexity."

### Rule 6: Precision

Define every technical term once. Bold it. Move on.

**First use:**
> The **Dramatica-Astrology Interface (DAI)** maps story elements to chart positions.

Never bold it again.

### Rule 7: No Retreat

Don't soften your statements.

**Weak:**
> "This approach tends to work better in most cases."

**Strong:**
> "This approach works."

State the truth. If exceptions exist, list them.

### The Puller Test

Ask: **"Could Chesty read this under fire?"**

- Yes → Ship it
- No → Rewrite

### Examples: Weak vs Strong

**Weak:**
> "When creating a character, you might want to consider starting with the Sun sign, as this could provide a foundation for understanding core identity."

**Strong:**
> "Start with the Sun sign. This defines core identity."

**Weak:**
> "Practitioners should generally attempt to apply the framework systematically, though flexibility may be appropriate."

**Strong:**
> "Apply the framework systematically. Exercise judgment when required."

**Weak:**
> "It has been observed that house systems tend to enhance depth."

**Strong:**
> "House systems enhance depth."

### The Five Laws

1. **State facts. No hedging.**
2. **Active voice. Always.**
3. **Kill every useless word.**
4. **Short sentences. Clear meaning.**
5. **If Chesty couldn't read it under fire, burn it.**

---

## Structural Requirements

### Hierarchy

Four levels maximum:

```markdown
# Document Title (H1 - once)
## Major Section (H2)
### Subsection (H3)
#### Detail (H4 - rare)
```

No H5 or H6. Restructure if needed.

### Lists

**Numbered** for sequences:
1. First
2. Second
3. Third

**Bulleted** for concepts:
- Concept one
- Concept two
- Concept three

### Paragraphs

Maximum 5 sentences.

One idea per paragraph.

No walls of text.

### Tables

Use for:
- Comparisons
- Definitions
- Version history

Must have headers.

### Code Blocks

Label the language:

````markdown
```yaml
example: content
```
````

---

## Versioning

Format: `MAJOR.MINOR.PATCH`

**MAJOR** - Breaks everything (2.0.0)
**MINOR** - Adds features (1.1.0)
**PATCH** - Fixes only (1.0.1)

### Version Table

End every SSOT with:

```markdown
## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-02-10 | Initial |
```

---

## For AI Assistants

### Orders

1. **Read this guide first**
2. **Use the template** at `_CANON/_TEMPLATES/ssot/📋_template_ssot.md`
3. **Check for duplicates** before creating new SSOTs
4. **Apply Puller Standard** to all writing
5. **Include all mandatory sections**
6. **Submit for review**

### Trust But Verify

User reviews your output for:
- Template compliance
- Complete sections
- Puller Standard adherence
- Proper file naming

If uncertain, ask.

Do not guess.

Do not hallucinate.

---

## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-02-10 | Initial doctrine with Chesty Puller standard and file naming |
