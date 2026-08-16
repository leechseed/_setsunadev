---
original_path: "/home/claude/bvipds_assumption_log.md"
source_conversation: "Bold Venture Initiative project charter planning"
created: 2026-03-19
trunk: BLACK
kind: generated-file
---

---
type: ssot_05_operations
category: assumption_log
version: 1.0.0
last_updated: 2026-03-19
applies_to: [BOLD_VENTURE, BVIPDS, OVEREXITOUT]
status: draft
purpose: "Captures every assumption embedded in the BVIPDS Project Charter. Each assumption is a statement believed to be true but not yet validated. Assumptions carry risk — if an assumption proves false, the dependent charter elements must be revised. This is a living document updated throughout the project lifecycle."
dependencies: [bvipds_project_charter]
pmbok_process: "4.1 Develop Project Charter (Output)"
---

# BVIPDS Assumption Log

## Table of Contents

1. [How to Use This Document](#how-to-use-this-document)
2. [Assumption Register](#assumption-register)
3. [Retired Assumptions](#retired-assumptions)
4. [Version History](#version-history)

---

## How to Use This Document

Each assumption has six fields:

- **ID** — Unique identifier (A-XXX).
- **Assumption** — The statement believed to be true.
- **Category** — Which charter input category the assumption originates from (Business, Environmental, Process Asset, or Technical).
- **Charter Impact** — Which charter sections depend on this assumption being true.
- **Risk if False** — What happens to the project if this assumption is wrong.
- **Validation Method** — How and when the assumption will be confirmed or invalidated.
- **Status** — OPEN (not yet tested), VALIDATED (confirmed true), INVALIDATED (confirmed false), or REVISED (original assumption modified based on evidence).

Assumptions are reviewed at every milestone gate (M-001 through M-007). Any assumption that is INVALIDATED triggers a review of the dependent charter sections listed in its Charter Impact field.

---

## Assumption Register

### A-001: The 12-Layer Character Model Is the Correct Granularity

| Field | Content |
|---|---|
| Assumption | The 12-layer character database structure (CORE, VITAL, SOCIAL, WILL, WOUND, DRIVE, ORIGIN, IMPRINT, EROS, SHADOW, DESTINY, FUNCTION) with three tiers (Flat, Standard, Deep) provides the correct level of granularity for sourcebook-grade character data. No layers need to be added, removed, or restructured. |
| Category | Technical |
| Charter Impact | Section 3.1 (REQ-005), Section 2.1 (Engine 2.01 success condition), Section 7 (M-001) |
| Risk if False | The character systems engine requires architectural rework. All character records produced under the current model may require migration. The Victoria Midnight vertical slice loses its validation status. |
| Validation Method | Complete the Victoria Midnight vertical slice through full diagnostic. If the 12 layers can express every canonical fact about Victoria that the OVEREXITOUT narrative requires, the model is validated. Test against at least one additional character of a different archetype (Impact Character or Contagonist) to confirm the model is not protagonist-biased. |
| Status | OPEN |

---

### A-002: OVEREXITOUT Is a Sufficient Proving Ground

| Field | Content |
|---|---|
| Assumption | The OVEREXITOUT IP is complex enough to stress-test all four engine domains (Character, Plot, World, Thematic) such that a system validated against OVEREXITOUT will function for ASTRO7EX and LAKAD without fundamental redesign. |
| Category | Business |
| Charter Impact | Section 1.3 (replicability claim), Section 2.2 (sourcebook completeness), Section 4 (Phase 4 validation), Section 10 (exit criteria) |
| Risk if False | The system is validated against an insufficiently complex test case. When ASTRO7EX or LAKAD enters development, the system encounters requirements that OVEREXITOUT did not surface, requiring rework of methodology and possibly engine architecture. |
| Validation Method | At M-006 (OVEREXITOUT Sourcebook Complete), conduct a gap analysis: compare the documented requirements of ASTRO7EX and LAKAD (even at high level) against the capabilities proven by the OVEREXITOUT sourcebook. Identify any domain, data type, or relationship pattern that OVEREXITOUT did not exercise. |
| Status | OPEN |

---

### A-003: One Person at 10-20 Hours Per Week Can Produce a System of This Scope

| Field | Content |
|---|---|
| Assumption | A solo developer working 10-20 hours per week with AI augmentation (Vargas 5-80-15 model) can complete all four phases of the BVIPDS project within a timeframe that maintains emotional momentum. "Maintaining emotional momentum" means visible progress occurs frequently enough to prevent stalling. |
| Category | Environmental |
| Charter Impact | Section 7 (milestone schedule), Section 6 (R-002, R-003), Section 8 (budget), Section 11 (PM authority) |
| Risk if False | The project stalls. The developer burns out or loses interest before the system reaches critical mass. Phases stretch indefinitely, compounding the emotional momentum risk (R-003). |
| Validation Method | Track elapsed time per milestone. If any single milestone exceeds 12 weeks of active work (roughly 120-240 hours), review whether the scope of that milestone is too large or whether the 10-20 hour estimate is inaccurate. Adjust milestone granularity or time commitment accordingly. |
| Status | OPEN |

---

### A-004: Markdown Is Sufficient as the Canonical Format

| Field | Content |
|---|---|
| Assumption | Plain markdown files with YAML frontmatter, stored in a Git repository, provide sufficient structure for the canonical data architecture. No relational database, graph database, or specialized data store is required at the current stage of development. |
| Category | Technical |
| Charter Impact | Section 3.2 (REQ-007, REQ-008), Section 5.2 (command console out of scope), Section 8 (budget baseline) |
| Risk if False | As the sourcebook grows, cross-referencing between documents becomes unmanageable. Queries that should be simple (e.g., "which characters are present in Scene 47") require manual search across dozens of files. The system requires a database layer earlier than planned, potentially invalidating the tool-stack baseline and triggering unplanned expenditure. |
| Validation Method | At M-004 (Plot and World Engines Operational), assess whether the volume and interconnectedness of canonical data can still be navigated effectively using markdown files and Git. If the developer consistently loses time to manual cross-referencing, the assumption is invalidated and a database layer must be scoped. |
| Status | OPEN |

---

### A-005: The Base 60 Mathematical Foundation Is Stable

| Field | Content |
|---|---|
| Assumption | The Base 60 divisor lattice (SC-12, SC-20, SC-60 scale classes) used in the character attribute system is mathematically sound and does not require revision. The recalibration currently pending is a propagation task, not a design revision. |
| Category | Technical |
| Charter Impact | Section 2.1 (Engine 2.01 success condition), Section 7 (M-001), Section 6 (R-007) |
| Risk if False | The mathematical foundation of the character system is flawed. All derived statistics, point budgets, and scale class constraints require recalculation. Every character record built on the current math is incorrect. |
| Validation Method | Complete the Base 60 recalibration propagation to the Vertical Slice point budget tables. Run the Victoria Midnight diagnostic with the propagated values. If all derived statistics produce narratively meaningful results (no absurd outliers, no degenerate edge cases), the foundation is validated. |
| Status | OPEN |

---

### A-006: Victoria Midnight Is a Representative Test Case

| Field | Content |
|---|---|
| Assumption | Victoria Midnight, as a Tier 3 Protagonist with a Change resolve and Failure/Good outcome, exercises enough of the character system to validate the system for all character types. |
| Category | Technical |
| Charter Impact | Section 2.1 (Engine 2.01 success condition), Section 7 (M-001) |
| Risk if False | The character system works for protagonists with Change resolve but fails for Steadfast characters, Impact Characters, or characters with Success outcomes. The system is protagonist-biased and requires additional validation passes. |
| Validation Method | After Victoria Midnight passes full diagnostic, run at least one additional character through the system who differs on the key Dramatica axes: a Steadfast Impact Character with a Success/Bad outcome. If the system handles both without structural modification, the assumption is validated. |
| Status | OPEN |

---

### A-007: Four Engine Domains Are MECE for Sourcebook Coverage

| Field | Content |
|---|---|
| Assumption | Character Systems, Plot Systems, World Systems, and Thematic Framework together cover every category of canonical data that an IP sourcebook requires. There is no fifth domain that these four do not encompass. |
| Category | Business |
| Charter Impact | Section 2.1 (system completeness), Section 4 (four-phase plan), Section 5.1 (scope) |
| Risk if False | A critical sourcebook domain is missing. The most likely candidates: a Style/Tone domain (how the IP feels, distinct from what it contains), a Rules/Mechanics domain (if the IP includes game-like systems), or a Meta/Production domain (adaptation guidelines for downstream creators). The four-phase plan requires a fifth phase or the existing phases require expansion. |
| Validation Method | At M-003 (Plot and World Engines Specified), conduct a MECE audit: list every type of canonical fact the OVEREXITOUT sourcebook must contain. Assign each to one of the four domains. If any fact type cannot be assigned, a fifth domain must be defined. |
| Status | OPEN |

---

### A-008: Cold Reader Legibility Is Achievable Through Documentation Discipline Alone

| Field | Content |
|---|---|
| Assumption | An outsider with zero context about Bold Venture can orient themselves using only the sourcebook documents (markdown files in a Git repository) without requiring a dedicated user interface, visual navigation layer, or guided onboarding experience. |
| Category | Business |
| Charter Impact | Section 2.2 (cold reader test), Section 3.2 (REQ-009), Section 5.2 (command console out of scope), Section 6 (R-006) |
| Risk if False | The sourcebook is structurally complete but practically illegible. The volume and density of markdown files overwhelm a cold reader. A navigation UI or guided entry point is required to make the sourcebook usable, pulling the command console application back into scope earlier than planned. |
| Validation Method | At M-006 (OVEREXITOUT Sourcebook Complete), conduct the formal cold reader test: provide the complete sourcebook to someone unfamiliar with Bold Venture and ask them to answer a set of canonical questions using only the documents. If they cannot navigate to the answers within a reasonable time, the assumption is invalidated. |
| Status | OPEN |

---

### A-009: Emotional Momentum Is Manageable Through Structured Phase Gates

| Field | Content |
|---|---|
| Assumption | The developer's identified tendency to stall when momentum drops can be managed by designing the project around frequent, visible deliverables at short intervals. External accountability (collaborators, deadlines, public commitments) is not required. |
| Category | Environmental |
| Charter Impact | Section 6 (R-003), Section 7 (milestone schedule), Section 11 (PM authority) |
| Risk if False | Phase gates and visible deliverables are insufficient. The developer stalls despite having a clear next step. The project requires external accountability mechanisms (a collaborator, a public commitment, a deadline tied to an external event) to maintain forward motion. |
| Validation Method | Track the gap between milestone completions. If any gap exceeds 4 weeks of inactivity (not elapsed time, but actual zero-progress periods), the assumption is invalidated and external accountability mechanisms must be explored. |
| Status | OPEN |

---

### A-010: The Narrative Layer Stack and SSOT Domain Structure Are Architecturally Complete

| Field | Content |
|---|---|
| Assumption | The Narrative Layer Stack (Layers 0-6) and the SSOT Domain Structure (Domains 00-05) as currently defined are complete. No additional layers or domains need to be added to support the four-engine system. |
| Category | Process Asset |
| Charter Impact | Section 3.3 (REQ-012, REQ-013), Section 4 (Phase 1 foundation work) |
| Risk if False | A gap in the layer stack or domain structure is discovered during engine development. The gap requires adding a new layer or domain, which propagates changes to all existing SSOTs that reference the current structure. |
| Validation Method | At M-002 (Foundation Documents Locked), review the Narrative Layer Stack and SSOT Domain Structure against the requirements of all four engine domains. If any engine requires a concept that does not fit into the existing layers or domains, the assumption is invalidated and the structures must be extended. |
| Status | OPEN |

---

### A-011: AI Augmentation Remains Available and Cost-Effective

| Field | Content |
|---|---|
| Assumption | The AI consultation model (Claude as expert judgment provider within the Vargas 5-80-15 framework) remains available, capable, and affordable throughout the project lifecycle. API pricing, model capabilities, and access do not change in ways that materially affect the project. |
| Category | Environmental |
| Charter Impact | Section 8 (budget), Section 11 (AI augmentation model), Section 6 (R-002) |
| Risk if False | API pricing increases significantly, model capabilities degrade, or access is restricted. The 5-80-15 model breaks down, shifting more of the 80% execution burden to the developer. The solo-developer bottleneck (R-002) intensifies. |
| Validation Method | Monitor AI tool costs as a line item. If monthly AI expenditure exceeds 20% of total project budget for two consecutive months, review whether the augmentation model is still cost-effective. |
| Status | OPEN |

---

### A-012: The System Architecture Map Is Structurally Sound

| Field | Content |
|---|---|
| Assumption | The 53-component System Architecture Map with its three-layer model (Library, Engines, Assembly) and Layer 0 Foundations accurately represents the architecture of the system. Components are correctly assigned to layers, connections are correctly mapped, and the 11 flagged undefined interfaces represent the complete set of integration gaps. |
| Category | Process Asset |
| Charter Impact | Section 3.3 (REQ-014, REQ-015), Section 4 (all phases), Section 7 (all milestones) |
| Risk if False | The architecture map has misassigned components, missed connections, or failed to identify critical interfaces. Development proceeds against an inaccurate blueprint, resulting in rework when the true architecture is discovered. |
| Validation Method | At each milestone gate, compare the architecture map against the actual state of the system. If new components, connections, or interfaces have been discovered that the map did not predict, update the map and assess whether the discovery invalidates any completed work. |
| Status | OPEN |

---

## Retired Assumptions

*No assumptions have been retired yet. Assumptions move here when they are VALIDATED or INVALIDATED, with a note explaining the outcome and any charter changes that resulted.*

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0.0 | 2026-03-19 | Initial assumption log. 12 assumptions registered across four categories: 2 Business, 2 Environmental, 2 Process Asset, 6 Technical. All statuses OPEN. Companion to BVIPDS Project Charter v1.0.0. |
