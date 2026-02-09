---

## type: ssot_operations category: operations version: 1.0.0 last_updated: 2026-02-10 applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD] status: canonical purpose: Defines standards for creating and maintaining Single Source of Truth documentation within the LEECHSEED narrative development system
---
# 📐📐 SSOT Writing Guide: Marine Corps Doctrinal Standard

## Table of Contents

1. [Purpose](https://claude.ai/chat/73ada3ab-6fe3-49c6-b1b4-74e20ea8d9d6#purpose)
2. [SSOT Defined](https://claude.ai/chat/73ada3ab-6fe3-49c6-b1b4-74e20ea8d9d6#ssot-defined)
3. [SSOT Distinguished from Authoritative Documentation](https://claude.ai/chat/73ada3ab-6fe3-49c6-b1b4-74e20ea8d9d6#ssot-distinguished-from-authoritative-documentation)
4. [File Naming Standard](https://claude.ai/chat/73ada3ab-6fe3-49c6-b1b4-74e20ea8d9d6#file-naming-standard)
5. [Mandatory Structural Components](https://claude.ai/chat/73ada3ab-6fe3-49c6-b1b4-74e20ea8d9d6#mandatory-structural-components)
6. [Language Requirements](https://claude.ai/chat/73ada3ab-6fe3-49c6-b1b4-74e20ea8d9d6#language-requirements)
7. [Structural Requirements](https://claude.ai/chat/73ada3ab-6fe3-49c6-b1b4-74e20ea8d9d6#structural-requirements)
8. [Versioning Protocol](https://claude.ai/chat/73ada3ab-6fe3-49c6-b1b4-74e20ea8d9d6#versioning-protocol)
9. [Implementation Standards for AI Systems](https://claude.ai/chat/73ada3ab-6fe3-49c6-b1b4-74e20ea8d9d6#implementation-standards-for-ai-systems)
10. [Version History](https://claude.ai/chat/73ada3ab-6fe3-49c6-b1b4-74e20ea8d9d6#version-history)



## Purpose

This document establishes the authoritative standard for Single Source of Truth documentation within the LEECHSEED narrative development system. It defines structural requirements, language standards, and implementation protocols that ensure consistency, clarity, and canonical authority across all methodology documentation.

---

## SSOT Defined

**Single Source of Truth (SSOT)** documentation establishes methodology applicable across all narrative projects within the LEECHSEED system. These documents define operational frameworks—including but not limited to character generation systems, plot structure methodologies, and epistemological standards—independent of their application to specific story content.

An SSOT document maintains relevance regardless of which story project employs its principles. The methodology described applies equally to OVEREXITOUT, ASTRO7EX, LAKAD, and all subsequent narrative developments.

**SSOT Documentation Examples:**

- Character astrology framework defining the 15-category system
- Epistemological methodology for truth verification
- Dramatica integration protocols
- Plot structure theory

**Non-SSOT Documentation Examples:**

- Character profiles applying methodology to specific characters
- Story-specific plot outlines
- Scene drafts and narrative content
- Project-specific worldbuilding details

SSOT documentation describes how systems operate. Authoritative documentation describes how those systems have been applied to specific narrative content.

---

## SSOT Distinguished from Authoritative Documentation

|Characteristic|SSOT Documentation|Authoritative Documentation|
|---|---|---|
|Scope|Methodology applicable to all projects|Application to specific project|
|Abstraction|Abstract principles and frameworks|Concrete implementation|
|Location|`_CANON/_SSOT/`|`_CANON/_AUTHORITATIVE/[PROJECT]/`|
|Dependencies|May depend on other SSOT documents|Depends on SSOT methodology|
|Revision Trigger|Methodology evolution|Story development changes|

---

## File Naming Standard

### Structure

All canonical documentation follows the format: `[emoji]_[category]_[descriptive_name].md`

### Emoji Taxonomy

The following emoji designations provide visual classification:

- **📐** SSOT Documentation (methodology and frameworks)
- **🎯** Authoritative Documentation (story-specific application)
- **⚙️** Operations Documentation (workflow and process)
- **📋** Template Documentation (structural forms)
- **❌** Deprecated Documentation (archived, non-canonical)

### Critical Documentation Designation

Foundational documents that define system-level operations receive double emoji designation:

```
📐📐_ssot_writing_guide.md
⚙️⚙️_ops_mission_control_specification.md
🎯🎯_auth_leechseed_universe_foundation.md
```

### Naming Conventions

**Required Standards:**

- All characters lowercase
- Underscores replace spaces
- No version numbers in filename (version controlled through frontmatter)
- Descriptive terminology without abbreviation

**Example Implementation:**

```
📐_ssot_narrative_astrology_framework.md
📐_ssot_epistemology_truth_verification.md
🎯_auth_overexitout_victoria_midnight_profile.md
🎯_auth_overexitout_plot_structure_act_one.md
⚙️_ops_goon_room_workflow_protocol.md
📋_template_ssot_standard_structure.md
❌_deprecated_legacy_character_system.md
```

---

## Mandatory Structural Components

All SSOT documentation contains the following components in the specified order. Omission of any component renders the document non-canonical.

1. **Frontmatter**
    
    - YAML format with required fields
    - Type, category, version, applicability scope, status, and purpose
2. **Document Title**
    
    - Clear identification of subject matter
    - Follows file naming conventions without emoji prefix
3. **Table of Contents**
    
    - Complete section linkage
    - Hierarchical structure representation
    - Non-negotiable requirement
4. **Purpose Statement**
    
    - Single paragraph defining document scope
    - Establishes what the SSOT defines and why it exists
5. **Core Concepts**
    
    - Detailed methodology exposition
    - Framework principles and operational theory
6. **Implementation**
    
    - Application procedures
    - Integration with existing systems
7. **Examples**
    
    - Minimum two concrete implementations
    - Demonstrates range of application
8. **References**
    
    - Dependent SSOT documentation
    - External source material
9. **Version History**
    
    - Tabular format
    - Complete revision record

---

## Language Requirements

### Declarative Authority

SSOT documentation employs declarative sentences that establish operational fact. Statements assert methodology without qualification or hedging.

**Standard Construction:**

- The framework operates through three sequential phases of character development.
- This methodology requires foundational understanding of both Dramatica narrative structure and traditional astrological chart analysis before implementation.
- Application of the 15-category system produces character profiles with psychological depth and thematic coherence.

**Non-Standard Construction:**

- Hedged assertions: "The framework might work through three phases."
- Informal address: "You need to understand Dramatica first."
- Colloquial expression: "This makes your characters deeper."

### Technical Precision

Define all technical terminology with exactness upon first use. Employ subordinate clauses to establish scope, boundaries, and operational limits.

**Example from Marine Corps Doctrine:**

> War is a violent clash of interests between or among organized groups characterized by the use of military force. These groups have traditionally been established nation-states, but they may also include any nonstate group—such as an international coalition or a faction within or outside of an existing state—with its own political interests and the ability to generate organized violence on a scale sufficient to have significant political consequences.

**Applied Standard:**

> Single Source of Truth documentation establishes methodology applicable across all narrative projects within the LEECHSEED development system. These documents define operational frameworks—including but not limited to character generation systems, plot structure methodologies, and epistemological standards—independent of their application to specific story content or character profiles.

### Prohibition of Contractions

All words appear in complete form. Contractions compromise the formal authority of doctrinal text.

**Required Forms:**

- do not
- cannot
- will not
- it is
- they are
- has not
- would not

**Prohibited Forms:**

- do not use contracted forms

### Complex Sentence Structure

Employ complex sentences with subordinate clauses to convey complete operational meaning within coherent units. This structure allows precise qualification and scope definition without fragmenting related concepts.

**Marine Corps Model:**

> The essence of war is a violent struggle between two hostile, independent, and irreconcilable wills, each trying to impose itself on the other.

**Application to SSOT:**

> The function of character astrology methodology within narrative development is the systematic generation of psychological profiles through astrological chart analysis, wherein planetary positions, aspects, and house placements correspond to specific character traits, motivations, and developmental arcs as defined by the Dramatica narrative structure.

### Active Voice with Explicit Subject

Maintain active voice construction with clearly identified subjects performing specified actions. Avoid implied actors or ambiguous references.

**Standard:**

- The practitioner applies the character framework to generate initial personality profiles.
- This methodology requires sequential implementation beginning with solar position analysis.
- Documentation standards mandate comprehensive coverage of all framework components.

**Non-Standard:**

- Imperative without subject: "Apply the character framework."
- Passive construction: "The framework should be used sequentially."
- Informal imperative: "Make sure to cover all components."

### Elimination of Imprecise Terminology

Remove all qualifying language that introduces ambiguity or uncertainty into doctrinal statements.

**Terms to Eliminate:**

- Hedging qualifiers: perhaps, maybe, possibly, might, could, potentially, arguably
- Intensity modifiers: very, really, quite, somewhat, rather, fairly
- Vague action verbs: try to, attempt to, seek to, endeavor to
- Filler terms: basically, actually, just, simply, essentially, literally, obviously

**Revision Process:**

Non-Standard: "The practitioner might want to try applying the framework to potentially improve character depth."

Standard: "Application of the framework increases character psychological depth."

Non-Standard: "The methodology basically provides a way to systematically develop characters."

Standard: "The methodology provides systematic character development protocols."

### Present Tense Construction

SSOT documentation describes current operational reality. Use present tense to establish standing methodology.

**Required:**

- The framework consists of 15 distinct categories.
- This method produces consistent results across narrative projects.
- Implementation requires sequential progression through developmental phases.

**Prohibited:**

- Future tense: "The framework will consist of 15 categories."
- Conditional: "This method would produce consistent results."
- Hypothetical: "Implementation would require sequential progression."

### Term Definition Standards

Define technical terminology upon first use with bold formatting. Provide complete definitional scope including operational boundaries and limitations.

**Format:**

> The **Dramatica-Astrology Interface (DAI)** establishes correspondence between Dramatica's 64 narrative elements and traditional astrological chart positions, creating a systematic method for character generation that integrates narrative function with psychological archetypal patterns.

Bold formatting appears only on initial definition. Subsequent references employ standard text.

---

## Structural Requirements

### Hierarchical Organization

Documentation employs four hierarchical levels maximum:

```markdown
# Document Title (H1 - appears once)
## Major Section (H2)
### Subsection (H3)
#### Detail Level (H4 - minimal use)
```

Documents requiring deeper nesting indicate structural problems requiring reorganization.

### List Construction

**Numbered Lists** indicate sequential procedures or hierarchical priority:

1. First action or primary concept
2. Second action or secondary concept
3. Third action or tertiary concept

**Bulleted Lists** indicate non-sequential concepts or equivalent options:

- First concept or option
- Second concept or option
- Third concept or option

### Paragraph Standards

Maximum paragraph length: five sentences.

Each paragraph addresses one concept or procedural step.

Paragraphs exceeding five sentences require subdivision into multiple paragraphs or restructuring as lists.

### Table Usage

Tables provide comparative analysis, definitional clarity, or version tracking:

- Comparative analysis between concepts
- Term definitions with classifications
- Version history records

All tables require column headers with clear terminology.

### Code Block Formatting

Code blocks display example syntax, data structures, or command sequences. All code blocks specify language for proper rendering:

````markdown
```yaml
type: ssot_methodology
version: 1.0.0
```
````

---

## Versioning Protocol

### Version Number Format

Format: `MAJOR.MINOR.PATCH`

**MAJOR Version** (X.0.0): Fundamental methodology changes that break backward compatibility

- Existing implementations cease to function correctly
- Complete framework restructuring
- All dependent Authoritative documentation requires revision

**MINOR Version** (1.X.0): Feature additions maintaining backward compatibility

- New capabilities added to existing framework
- Existing implementations continue functioning
- Optional adoption of new features

**PATCH Version** (1.0.X): Corrections and clarifications without methodology changes

- Typographical corrections
- Clarified language
- Formatting improvements
- No operational impact

### Version History Table

All SSOT documentation concludes with complete version history:

```markdown
## Version History

| Version | Date | Changes |
|---------|------|---------|
| 1.0.0 | 2026-02-10 | Initial documentation |
| 1.1.0 | 2026-02-15 | Added Mars aspect variation methodology |
| 1.1.1 | 2026-02-16 | Clarified terminology in implementation examples |
| 2.0.0 | 2026-03-01 | Complete framework restructure with house system integration |
```

---

## Implementation Standards for AI Systems

### Operational Protocol

AI systems creating or modifying SSOT documentation execute the following protocol:

1. **Read Current Guide**: Review this document completely before generating content
2. **Template Utilization**: Copy structure from `_CANON/_TEMPLATES/ssot/📋_template_ssot.md`
3. **Duplication Check**: Search existing `_CANON/_SSOT/` directory before creating new documents
4. **Classification Verification**: Confirm document qualifies as SSOT rather than Authoritative content
5. **Standard Application**: Apply all language and structural requirements from this guide
6. **Component Completeness**: Include all mandatory sections without omission
7. **Human Review**: Submit generated content for practitioner review and approval

### Quality Verification

Human practitioners review AI-generated documentation for:

- Template structural compliance
- Complete section inclusion
- Proper SSOT classification
- Language standard adherence
- File naming convention compliance

AI systems operating with uncertainty regarding any requirement query the human practitioner rather than proceeding with assumptions or approximations.

---

## Version History

|Version|Date|Changes|
|---|---|---|
|1.0.0|2026-02-10|Initial SSOT writing guide with Marine Corps doctrinal standards and file naming protocols|