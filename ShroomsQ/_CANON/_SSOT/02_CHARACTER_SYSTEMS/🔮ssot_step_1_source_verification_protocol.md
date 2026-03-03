---

## type: ssot_02_character_systems category: vertical_slice_protocol version: 1.0.0 last_updated: 2026-03-03 applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD] status: canonical purpose: "Replaces the single-sentence Step 1 of the Vertical Slice protocol with a formal source verification gate. Defines exactly what 'canonical documentation exists and is locked' means, specifies the required upstream documents, and establishes the verification checklist that must pass before the Vertical Slice proceeds to Step 2." dependencies: ["ssot_03_character_systems_vertical_slice", "ssot_02_character_dramatica_integration", "ssot_02_character_astrology", "template_dramatica_ingest", "template_character_astrology_ingest"]
---
# 🔮 SSOT: Step 1 — Source Verification Protocol

## Table of Contents

1. [Purpose](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#purpose)
2. [What This Replaces](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#what-this-replaces)
3. [The Source Verification Gate](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#the-source-verification-gate)
4. [Required Documents by Tier](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#required-documents-by-tier)
5. [Verification Sequence](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#verification-sequence)
6. [Pass and Fail Conditions](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#pass-and-fail-conditions)
7. [Canonical Folder Structure](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#canonical-folder-structure)
8. [Version History](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#version-history)

---

## Purpose

The Vertical Slice protocol (ssot_03_character_systems_vertical_slice) defines Step 1 as: "Before assigning any values, confirm that canonical documentation for the character exists and is locked. Do not run a Vertical Slice against a character whose narrative role, Dramatica function, or origin is still in development."

That instruction is correct but insufficient. It does not define what canonical documentation looks like, what format it arrives in, which upstream systems must have completed their work, or how to verify completeness. This document replaces that single sentence with a formal verification gate.

Step 1 is now a checkpoint. The Vertical Slice does not proceed to Step 2 (Tier 1 Assignment) until every item in this protocol passes.

---

## What This Replaces

This document replaces **Step 1** of the Vertical Slice protocol only. Steps 2 through 7 of the Vertical Slice remain unchanged. When the Vertical Slice document is next revised, its Step 1 section should reference this SSOT rather than containing its own abbreviated instruction.

---

## The Source Verification Gate

The gate has three components:

1. **Authoritative Document Verification** — Does the character have a locked canonical document that defines who they are?
2. **Dramatica Ingest Verification** — Does the character have a locked Dramatica Ingest Template that defines their narrative function?
3. **Character Astrology Ingest Verification** — Does the character have a locked (or minimum-viable) Character Astrology Ingest Template that defines their symbolic dataset?

All three components must pass before the Vertical Slice proceeds. The components are checked in order. If Component 1 fails, Components 2 and 3 cannot pass (they depend on the authoritative document). If Component 2 fails, Component 3 cannot pass (Character Astrology consumes Dramatica output).

---

## Required Documents by Tier

### Tier 3 (Deep Characters — Full Verification Required)

|Document|Status Required|Location|
|---|---|---|
|**Authoritative Character Document**|LOCKED|`_AUTHORITATIVE/[IP]/characters/[CHARACTER_ID]/`|
|**Dramatica Ingest Template**|LOCKED|Same folder|
|**Character Astrology Ingest Template**|LOCKED or MINIMUM_VIABLE|Same folder|

All three documents must be present. The Dramatica Ingest must be fully locked. The Character Astrology Ingest may be at minimum-viable completeness (Sections 1-5 and 8-10 populated) — the full chart is not required for the Vertical Slice to proceed, but the core planetary assignments must be in place.

### Tier 2 (Standard Characters — Partial Verification)

|Document|Status Required|Location|
|---|---|---|
|**Authoritative Character Document**|LOCKED|`_AUTHORITATIVE/[IP]/characters/[CHARACTER_ID]/`|
|**Dramatica Element Signature**|DOCUMENTED|May be inline in the authoritative document or in a standalone file|
|**Character Astrology Partial Chart**|OPTIONAL|Sun + Moon + one defining aspect, if completed|

Tier 2 characters do not require a full Dramatica Ingest Template or a full Character Astrology Ingest Template. They require an authoritative document and a documented element signature (2-4 Dramatica elements plus relational role tags). If a partial astrology chart exists, it supplements but does not gate the Vertical Slice.

### Tier 1 (Flat Characters — Minimal Verification)

|Document|Status Required|Location|
|---|---|---|
|**Character Brief**|EXISTS|May be a paragraph in a scene document, a cast list entry, or a standalone note|

Tier 1 characters require only that someone has written down who they are in enough detail to assign L1-L3 values. No Dramatica or Character Astrology documentation is required.

---

## Verification Sequence

### Component 1: Authoritative Document Verification

The authoritative document is the character's canonical bible — the locked document that defines who the character is independent of any downstream system. For Victoria Midnight, this is the "Character Authority Document" containing identity, structural spine, origin commitments, behavior under pressure, relationship to the system, core bonds, non-negotiables, and signature imagery.

**Check 1.1: Document exists.** The file is present in the character's canonical folder.

**Check 1.2: Document is locked.** The document header contains a status field reading LOCKED or CANON LOCKED with a version number.

**Check 1.3: Identity is defined.** The document contains: full name, narrative role, and primary bond(s).

**Check 1.4: Narrative function is defined.** The document contains: Dramatica structural role (MC/IC/OS), resolve (Change/Steadfast), and at minimum the Problem/Solution pair.

**Check 1.5: Origin is defined.** The document contains enough backstory to support L7 ORIGIN variable assignment. At minimum: origin context, family architecture, and the inciting wound or formation event.

**Check 1.6: Behavioral signature is defined.** The document contains documented behavior under pressure — how the character acts when the system pushes back. This is required because L4 WILL, L5 WOUND, and L10 SHADOW assignments depend on knowing how the character responds to stress.

**Check 1.7: Non-negotiables are defined.** The document contains character laws — things this character will not do. These function as invariant constraints on all downstream assignments.

**Component 1 result:** PASS if all checks 1.1-1.7 are satisfied. FAIL if any check is not met.

---

### Component 2: Dramatica Ingest Verification

The Dramatica Ingest Template captures the complete storyform data for this character. It is produced by extracting data from the locked Dramatica storyform using the report manifest and extraction priority defined in ssot_02_character_dramatica_integration.

**Check 2.1: Template exists.** The Dramatica Ingest Template file is present in the character's canonical folder.

**Check 2.2: Template is locked.** The header status field reads `locked`. The storyform_status field reads `locked`.

**Check 2.3: Section 1 (Storyform Dynamics) is complete.** At minimum: story_outcome, story_judgement, story_driver, story_limit are populated.

**Check 2.4: Section 2 (Structural Role) is complete.** All six fields populated: structural_role, dramatica_archetype, resolve, growth, approach, mental_sex.

**Check 2.5: Section 3 (Element Quads) is complete.** All eight element fields populated. Structural meaning statement is written.

**Check 2.6: Applicable throughline sections are complete.** If the character is MC, Section 4 is populated. If IC, Section 5. Section 6 (OS) is always required. Section 7 (RS) is required if the character is an RS principal.

**Check 2.7: Section 9 (Narrative Invariants) contains at least one invariant.** Every Tier 3 character has at least one structural law derived from the storyform.

**Check 2.8: Section 10 (L12 Core Block) is populated and matches the data in preceding sections.** The auto-generated block must be consistent with the template data.

**Check 2.9: Downstream handoff checklist is complete.** All items checked.

**Component 2 result:** PASS if all applicable checks are satisfied. FAIL if any required check is not met.

---

### Component 3: Character Astrology Ingest Verification

The Character Astrology Ingest Template captures the natal chart derived from the Dramatica Ingest via the DAI translation rules. It may be at full or minimum-viable completeness.

**Check 3.1: Template exists.** The Character Astrology Ingest Template file is present in the character's canonical folder.

**Check 3.2: Template references a locked Dramatica Ingest.** The `dramatica_ingest_ref` field points to the locked Dramatica Ingest Template verified in Component 2.

**Check 3.3: Minimum viable chart is populated.** At minimum, the following are assigned with derivation justifications:

- Sun sign (Section 1)
- Moon sign (Section 1)
- Mercury sign (Section 1)
- Venus sign (Section 1)
- Mars sign (Section 1)
- Saturn sign (Section 2)
- Ascendant sign (Section 3)

**Check 3.4: Aspect map contains at least 3 aspects.** Each aspect cites its Dramatica tension source.

**Check 3.5: House placements are assigned for all planets in the minimum viable set.** Seven planets minimum with house assignments and justifications.

**Check 3.6: Chart Summary (Section 8) is written.** The 6-10 sentence prose summary exists.

**Check 3.7: 12-Layer Feed Map (Section 9) is completed.** The table connecting chart elements to layer targets is filled in.

**Check 3.8: Template status is `locked` or `minimum_viable`.** Either status passes the gate. Full chart completion is not required.

**Component 3 result:** PASS if all checks 3.1-3.8 are satisfied. CONDITIONAL PASS if 3.8 status is `minimum_viable` (the Vertical Slice may proceed but the Character Astrology template should be completed to full status during or after the Vertical Slice). FAIL if any check is not met.

---

## Pass and Fail Conditions

### Full Pass (Green Light)

All three components pass. The Vertical Slice proceeds to Step 2 (Tier 1 Assignment) with full upstream documentation in place. The narrative designer has all the information needed to assign values confidently.

### Conditional Pass (Yellow Light)

Components 1 and 2 pass. Component 3 passes at minimum-viable level. The Vertical Slice may proceed, but the following constraints apply:

- L7-L11 assignments that depend on Character Astrology data carry an `[ASTROLOGY_PENDING]` tag until the full chart is completed.
- The Feed Validation Checklist (from ssot_02_character_astrology_12layer_mapping) cannot be run until the full chart is locked.
- The Vertical Slice structured data block is versioned as `draft` until the Character Astrology Ingest Template reaches full status and the Feed Validation Checklist passes.

### Fail (Red Light)

Any component fails. The Vertical Slice does not proceed. The narrative designer must complete the failing upstream document before returning to Step 1.

**Failure diagnostic:**

|Failure Point|Action Required|
|---|---|
|Component 1 fails (no authoritative document)|Write and lock the character's canonical documentation.|
|Component 1 fails (document not locked)|Review and lock the authoritative document. All draft elements must be resolved.|
|Component 1 fails (missing sections)|Complete the missing sections in the authoritative document.|
|Component 2 fails (no Dramatica Ingest)|Complete the Dramatica Ingest Template from the locked storyform.|
|Component 2 fails (template not locked)|Resolve all draft fields and lock the template.|
|Component 2 fails (missing sections)|Extract the missing data from Dramatica reports per the extraction priority.|
|Component 3 fails (no Character Astrology Ingest)|Run the DAI derivation sequence using the locked Dramatica Ingest.|
|Component 3 fails (minimum viable chart incomplete)|Complete at minimum: Sun, Moon, Mercury, Venus, Mars, Saturn, Ascendant + 3 aspects + houses + chart summary + feed map.|

---

## Canonical Folder Structure

When all three components pass, the character's canonical folder contains:

```
_AUTHORITATIVE/[IP]/characters/[CHARACTER_ID]/
├── [CHARACTER_ID]_authoritative.md          [LOCKED]
├── [CHARACTER_ID]_dramatica_ingest.md       [LOCKED]
├── [CHARACTER_ID]_astrology_ingest.md       [LOCKED or MINIMUM_VIABLE]
├── [CHARACTER_ID]_vertical_slice.md         [produced at Step 7]
└── states/
    ├── [CHARACTER_ID]_state_[moment].md     [produced during story development]
    └── ...
```

The `states/` subfolder is created when the first state diff is authored. It does not need to exist at Step 1 — state diffs are a product of story development, not source verification.

Relationship records are stored at the IP level, not inside individual character folders:

```
_AUTHORITATIVE/[IP]/relationships/
├── [RELATIONSHIP_ID].md
└── ...
```

---

## Version History

|Version|Date|Changes|
|---|---|---|
|1.0.0|2026-03-03|Initial Step 1 Source Verification Protocol. Three-component gate with per-tier requirements, 22 verification checks across components, pass/conditional/fail logic, failure diagnostics, and canonical folder structure specification.|