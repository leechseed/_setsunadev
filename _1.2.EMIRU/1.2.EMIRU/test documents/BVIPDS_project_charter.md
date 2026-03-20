---

## type: ssot_05_operations category: project_charter version: 1.0.0 last_updated: 2026-03-19 applies_to: [BOLD_VENTURE, BVIPDS, OVEREXITOUT, ASTRO7EX, LAKAD] status: draft purpose: "Formally authorizes the existence of the Bold Venture IP Development System (BVIPDS) project, assigns the project manager, and establishes the authority to apply organizational resources to project activities. This document is the single authorizing artifact for all BVIPDS development work." dependencies: [ssot_00_system_architecture_map] companion_documents: [bvipds_assumption_log] pmbok_process: "4.1 Develop Project Charter" pmbok_inputs: [business_documents, agreements, enterprise_environmental_factors, organizational_process_assets] pmbok_tools_and_techniques: [expert_judgment, data_gathering] pmbok_outputs: [project_charter, assumption_log]
---
# BVIPDS Project Charter

## Table of Contents

1. [Project Purpose and Justification](https://claude.ai/chat/05ff65c2-e731-4a97-b14c-b114f0113a6d#1-project-purpose-and-justification)
2. [Measurable Objectives and Success Criteria](https://claude.ai/chat/05ff65c2-e731-4a97-b14c-b114f0113a6d#2-measurable-objectives-and-success-criteria)
3. [High-Level Requirements](https://claude.ai/chat/05ff65c2-e731-4a97-b14c-b114f0113a6d#3-high-level-requirements)
4. [High-Level Project Description](https://claude.ai/chat/05ff65c2-e731-4a97-b14c-b114f0113a6d#4-high-level-project-description)
5. [Project Boundaries](https://claude.ai/chat/05ff65c2-e731-4a97-b14c-b114f0113a6d#5-project-boundaries)
6. [Overall Project Risk](https://claude.ai/chat/05ff65c2-e731-4a97-b14c-b114f0113a6d#6-overall-project-risk)
7. [Summary Milestone Schedule](https://claude.ai/chat/05ff65c2-e731-4a97-b14c-b114f0113a6d#7-summary-milestone-schedule)
8. [Pre-Approved Financial Resources](https://claude.ai/chat/05ff65c2-e731-4a97-b14c-b114f0113a6d#8-pre-approved-financial-resources)
9. [Key Stakeholder List](https://claude.ai/chat/05ff65c2-e731-4a97-b14c-b114f0113a6d#9-key-stakeholder-list)
10. [Project Exit Criteria](https://claude.ai/chat/05ff65c2-e731-4a97-b14c-b114f0113a6d#10-project-exit-criteria)
11. [Assigned Project Manager and Authority Level](https://claude.ai/chat/05ff65c2-e731-4a97-b14c-b114f0113a6d#11-assigned-project-manager-and-authority-level)
12. [Authorizing Sponsor](https://claude.ai/chat/05ff65c2-e731-4a97-b14c-b114f0113a6d#12-authorizing-sponsor)
13. [Version History](https://claude.ai/chat/05ff65c2-e731-4a97-b14c-b114f0113a6d#13-version-history)

---

## 1. Project Purpose and Justification

### 1.1 Problem Statement

A solo creative developer building narrative intellectual property at the scale of a Tolkien legendarium faces a structural problem: the volume of canonical data (characters, world systems, plot architecture, thematic frameworks, and their interdependencies) exceeds what unstructured creative process can manage without contradiction, loss, or stalling. No commercially available tool combines rigorous narrative theory (Dramatica, GURPS-derived attribute mathematics, astrological archetype mapping) with a queryable, version-controlled, medium-agnostic data architecture. The developer must build the tool that builds the story.

### 1.2 Project Purpose

The Bold Venture IP Development System (BVIPDS), also known as LEECHSEED, is a methodology and toolset for producing medium-agnostic IP sourcebooks. An IP sourcebook is the canonical, queryable reference artifact that contains the entirety of a fictional universe — every character, every place, every event, every rule, every thematic structure — organized so that any downstream content creator (screenwriter, game designer, comic artist, novelist, showrunner) can pull from it to produce work in their specific medium without contradicting anything else in the universe.

BVIPDS separates methodology from content. The methodology (how to build a sourcebook) is story-agnostic and replicable. The content (the sourcebook for a specific IP) is the output of running that methodology against a specific creative vision. The system is the deliverable. The sourcebooks it produces are the validation artifacts.

### 1.3 Business Justification

The value of BVIPDS is threefold:

First, it eliminates the structural ceiling on IP complexity. Without a system, the solo developer's working memory becomes the bottleneck. With a system, the canonical data lives in structured, queryable documents that do not degrade, forget, or contradict themselves.

Second, it makes the IP legible to outsiders from day one. Every output artifact passes a cold reader test — a person with zero context about Bold Venture can orient themselves using only the sourcebook. This is a prerequisite for collaboration, licensing, adaptation, and any future commercial activity.

Third, it is replicable. The methodology that produces the OVEREXITOUT sourcebook will produce the ASTRO7EX and LAKAD sourcebooks without reinventing process. The investment in the system amortizes across every IP it services.

### 1.4 Strategic Alignment

BVIPDS is the core operational capability of Bold Venture studio. All creative output, all future collaboration, and all potential commercial activity depend on this system functioning. There is no secondary priority that competes with it.

---

## 2. Measurable Objectives and Success Criteria

### 2.1 System Completeness

The BVIPDS is complete when all four engine domains are operational and validated:

|Engine Domain|System Architecture ID|Status at Charter|Success Condition|
|---|---|---|---|
|Character Systems|Engine 2.01|Partially built|All sub-components operational. Victoria Midnight vertical slice passes full diagnostic.|
|Plot Systems|Engine 2.02|Flagged / Not built|Timeline coordinate system, scene-to-state mapping, and character-plot interface (INT-002) defined and operational.|
|World Systems|Engine 2.03 (proposed)|Not yet in architecture|Geography, factions, rules, technology, and culture engines defined and operational.|
|Thematic Framework|Engine 2.04 (proposed)|Not yet in architecture|Philosophical premise, motif tracking, and thematic-to-plot binding defined and operational.|

Each engine is considered operational when it can accept structured input, process it through its internal pipeline, and produce an SSOT-compliant output artifact that passes the cold reader test.

### 2.2 Sourcebook Completeness (OVEREXITOUT Proving Ground)

The OVEREXITOUT sourcebook is the validation artifact. It is complete when:

1. The character roster is populated at the depth required by narrative function (Tier 3 for main cast, Tier 2 for supporting, Tier 1 for background).
2. The world system is documented to the depth required for scene-level creative work.
3. The plot architecture is documented from macrostructure (act/sequence) through microstructure (scene/beat).
4. The thematic framework is documented and its connections to character arcs, plot events, and world elements are traceable.
5. An outside reader with no prior context can navigate the sourcebook, locate any canonical fact, and understand its relationship to the rest of the IP without assistance.

### 2.3 Process Maturity

The development methodology is mature when:

1. Every SSOT domain (00 through 05) has at least one canonical document.
2. The Bold Venture Development Doctrine (BVDP-1) is written and operational.
3. A second IP (ASTRO7EX or LAKAD) can begin development by following the documented methodology without requiring the original developer to explain anything verbally.

---

## 3. High-Level Requirements

### 3.1 Functional Requirements

REQ-001: The system shall produce structured, queryable IP sourcebooks from creative input.

REQ-002: The system shall separate methodology (how to build) from content (what is built). Methodology documents shall be story-agnostic. Content documents shall be IP-specific.

REQ-003: The system shall enforce canonical consistency. No two documents within an IP sourcebook shall contain contradictory information about the same canonical fact.

REQ-004: Each engine shall accept structured input, process it through a defined pipeline, and produce an SSOT-compliant output artifact.

REQ-005: The system shall support three character tiers (Tier 1 flat, Tier 2 standard, Tier 3 deep) with modular expansion via sub-tables rather than expanding the core 12-layer structure.

REQ-006: The system shall support state diffs — narrative overlays that represent how a character, location, or system changes in response to plot events, without modifying the base record.

### 3.2 Documentation Requirements

REQ-007: All canonical documents shall use markdown as the file format.

REQ-008: All canonical documents shall include YAML frontmatter specifying type, version, status, and dependencies.

REQ-009: All documentation shall pass the cold reader test: a person with zero context about Bold Venture can orient themselves using only the document and its linked references.

REQ-010: All documentation shall follow Marine Corps Doctrinal Publication style — declarative, no contractions, no hedging, behavioral consequences explained in plain conversational terms.

REQ-011: All documentation shall pass a 12-year-old test — no academic jargon, no unnecessary abstraction. If a concept cannot be explained in plain language, it is not understood well enough to document.

### 3.3 Architectural Requirements

REQ-012: The Narrative Layer Stack (Layers 0-6, the invariant physics of the story-world) and the SSOT Domain Structure (Domains 00-05, the development infrastructure) shall remain architecturally separate. They are two axes of the system. Conflating them is a known failure mode.

REQ-013: The development methodology shall exist outside and above the creative content it governs, analogous to how a manufacturing process exists outside the product it manufactures.

REQ-014: The three-layer architectural model (Library, Engines, Assembly) established in the System Architecture Map shall govern all component placement and data flow.

REQ-015: All system interfaces identified in the System Architecture Map (currently 11 undefined) shall be formally specified before the components they connect are considered integrated.

---

## 4. High-Level Project Description

BVIPDS development proceeds in four phases, each gated by a defined exit condition. The phases are sequenced to build capability incrementally, with each phase producing artifacts that the next phase consumes.

**Phase 1: Foundation and Character Systems Completion.** Close out Engine 2.01 (Character Systems). Complete the Victoria Midnight Dramatica Ingest. Propagate the mc_problem_element field rename. Confirm Base 60 recalibration. Lock the Narrative Layer Stack as the first formal SSOT outside of character systems. Resolve the four-option decision point that has been blocking forward progress. Write the Bold Venture Development Doctrine (BVDP-1).

**Phase 2: Plot and World Systems.** Define and build Engine 2.02 (Plot Systems) and Engine 2.03 (World Systems). Specify interfaces INT-002 (Character to Plot) and the new world-system interfaces. Begin populating the OVEREXITOUT sourcebook with plot architecture and world data using the new engines.

**Phase 3: Thematic Framework and Integration.** Define and build Engine 2.04 (Thematic Framework). Specify all remaining undefined interfaces. Integrate all four engines so that a change in one domain propagates traceably to affected domains. The sourcebook becomes a unified artifact rather than four separate data collections.

**Phase 4: Validation and Process Maturity.** Complete the OVEREXITOUT sourcebook to the standard defined in Section 2.2. Conduct a cold reader test with the sourcebook. Document all methodology in final SSOT form. Confirm that a second IP could begin development using only the documented methodology. Conduct an After Action Review (AAR) per doctrine Phase 6.

---

## 5. Project Boundaries

### 5.1 In Scope

- The BVIPDS methodology and all supporting SSOT documents (Domains 00-05)
- All four engine domains (Character, Plot, World, Thematic) and their internal pipelines
- The OVEREXITOUT IP sourcebook as the system validation artifact
- The System Architecture Map and all interface specifications
- The Bold Venture Development Doctrine (BVDP-1)
- Library layer formalization (metadata schema, collection standards)
- Tool evaluation and adoption justified by system requirements

### 5.2 Out of Scope

- Medium-specific adaptations (screenplays, game design documents, comic scripts, novel manuscripts). These are downstream consumers of the sourcebook, not part of the system.
- The ASTRO7EX and LAKAD sourcebooks. These are future projects that will use the system once it is validated.
- The Bold Venture Command Console application beyond conceptual specification. A native application may be built in a future charter once the underlying data architecture is stable enough to know what the application must display, query, and compute.
- Commercial activity (licensing, sales, partnership agreements). The system must exist before it can be commercialized.
- Audience-facing content of any kind (marketing, social media, portfolio presentations). These are downstream of the sourcebook.

### 5.3 Boundary Enforcement

Any work item that does not directly serve the completion of the BVIPDS methodology or the OVEREXITOUT sourcebook requires a formal change request documented in the assumption log with justification. The default answer to "should we add this?" is no. Scope creep is the historically documented primary threat to this project.

---

## 6. Overall Project Risk

### 6.1 Risk Register (Qualitative)

|Risk ID|Risk Description|Probability|Impact|Response Strategy|
|---|---|---|---|---|
|R-001|Scope creep. The developer expands system scope before current work is closed. This is the historically documented primary failure mode.|High|High|Boundary enforcement per Section 5.3. Phase gates prevent new work streams from opening until current phase exit criteria are met. The charter itself is the primary control artifact.|
|R-002|Solo-developer bottleneck. The developer is simultaneously sponsor, PM, architect, developer, writer, and QA. No role reaches flow state because they interrupt each other.|High|High|Phase structure isolates roles. Within a phase, the developer operates in one role at a time. AI augmentation handles the 80% middle per Vargas's 5-80-15 model.|
|R-003|Emotional momentum dependency. The developer has identified that stalling is a known failure mode triggered by loss of momentum.|High|Medium|Phase gates are designed to produce visible deliverables at short intervals. Each phase exit is a tangible artifact, not an abstract milestone. The assumption log tracks morale-relevant assumptions.|
|R-004|Premature architecture. The developer builds system components before the system design is complete, resulting in rework. This has occurred previously (22-phase sprint plan rejected as premature).|Medium|High|The System Architecture Map and this charter govern build sequence. No component is built until its inputs, outputs, and interfaces are specified.|
|R-005|Tool-stack instability. Technology choices for the command console and automation pipeline remain unresolved, creating decision paralysis.|Medium|Medium|Tool decisions are explicitly out of scope for this charter beyond evaluation. The system operates on markdown and existing tools until the data architecture is stable enough to dictate application requirements.|
|R-006|Cold reader test failure. Documentation produced by the developer (who has total context) may not be legible to an outsider despite intentions.|Medium|Medium|The cold reader test is a formal validation gate at Phase 4. Earlier phases include spot-checks. Documentation standards (REQ-009 through REQ-011) are designed to mitigate this risk continuously.|
|R-007|Base 60 mathematical foundation requires revision. The character attribute system is built on Base 60 arithmetic. If this foundation proves insufficient for world or plot systems, rework propagates across the entire system.|Low|High|Assumption A-005 in the assumption log tracks this. The OVEREXITOUT proving ground tests the foundation under real load before it is extended to other engines.|

### 6.2 Risk Tolerance

The project tolerates schedule risk (phases take longer than hoped) but does not tolerate scope risk (phases include work not authorized by the charter) or quality risk (documentation fails the cold reader test). Time is flexible. Boundaries are not.

---

## 7. Summary Milestone Schedule

Milestones are gated by deliverables, not calendar dates. The developer's time commitment is 10-20 hours per week with variable intensity. Calendar estimates are therefore unreliable and counterproductive. Progress is measured by artifacts produced, not time elapsed.

|Milestone|Phase|Gate Condition|Key Deliverables|
|---|---|---|---|
|M-001: Character Systems Closed|Phase 1|Engine 2.01 passes full diagnostic with Victoria Midnight. All open items resolved (Dramatica Ingest, field rename, Base 60 recalibration).|Locked Engine 2.01, Victoria Midnight vertical slice (final)|
|M-002: Foundation Documents Locked|Phase 1|Narrative Layer Stack SSOT locked. BVDP-1 (Development Doctrine) written and operational. Four-option decision point resolved.|NLS SSOT, BVDP-1, updated System Architecture Map|
|M-003: Plot and World Engines Specified|Phase 2|Engines 2.02 and 2.03 have defined sub-components, pipelines, and interface specifications.|Engine 2.02 spec, Engine 2.03 spec, INT-002 spec, world-system interface specs|
|M-004: Plot and World Engines Operational|Phase 2|Engines 2.02 and 2.03 accept input and produce SSOT-compliant output. OVEREXITOUT sourcebook contains plot architecture and world data.|Operational engines, initial OVEREXITOUT plot and world data|
|M-005: Thematic Framework Operational|Phase 3|Engine 2.04 defined, built, and integrated with Engines 2.01-2.03. All undefined interfaces specified.|Operational Engine 2.04, complete interface registry|
|M-006: OVEREXITOUT Sourcebook Complete|Phase 4|Sourcebook meets all criteria in Section 2.2. Cold reader test conducted.|Complete OVEREXITOUT sourcebook|
|M-007: Process Maturity Validated|Phase 4|Methodology documented to the standard in Section 2.3. AAR conducted.|Final SSOT set (Domains 00-05), AAR document|

---

## 8. Pre-Approved Financial Resources

### 8.1 Budget Classification

Moderate. The developer is willing to invest in tools justified by direct acceleration of sourcebook production or system development. No pre-set monthly cap, but every expenditure requires justification against a specific requirement or risk mitigation.

### 8.2 Current Baseline (Existing Subscriptions)

|Tool|Purpose|Status|
|---|---|---|
|Claude (Anthropic)|AI-augmented development, expert consultation, document generation|Active|
|Obsidian|Knowledge management, canonical document authoring and navigation|Active|
|GitHub|Version control, canonical workspace (_setsunadev repository, ShroomsQ workspace)|Active|
|Dramatica|Narrative theory engine, storyform generation|Active (perpetual license)|

### 8.3 Discretionary Spend Authorization

New tool adoption is authorized when the following conditions are met:

1. The tool addresses a specific requirement listed in Section 3 or mitigates a specific risk listed in Section 6.
2. No existing tool in the baseline can fulfill the requirement.
3. The cost is documented in the assumption log with the requirement or risk it addresses.

---

## 9. Key Stakeholder List

|Stakeholder|Role|Interest|Influence|
|---|---|---|---|
|Daddy (Project Originator)|Sponsor, Project Manager, Developer, Writer, QA|Total. All aspects of the project.|Total. Sole decision authority.|
|AI Consultant (Claude)|Expert Judgment Provider|System architecture, PMBOK methodology, document generation, scope enforcement|Advisory. Provides consultation per Vargas 5-80-15 model. No decision authority.|
|Future Collaborators / Licensees|Eventual sourcebook consumers|Sourcebook legibility and completeness|None currently. The cold reader test (REQ-009) protects their future interests.|

---

## 10. Project Exit Criteria

The BVIPDS project is complete when all of the following conditions are true:

1. All four engine domains (Character, Plot, World, Thematic) are operational and validated per Section 2.1.
2. The OVEREXITOUT sourcebook meets all completeness criteria per Section 2.2.
3. The development methodology meets all maturity criteria per Section 2.3.
4. The After Action Review (AAR) has been conducted and documented.
5. The assumption log has been reviewed and all critical assumptions have been validated or formally revised.

Upon completion, the project transitions to an operations-and-maintenance state. New IP sourcebooks (ASTRO7EX, LAKAD) are authorized under separate charters using the validated methodology.

---

## 11. Assigned Project Manager and Authority Level

**Project Manager:** Daddy (Project Originator)

**Authority Level:** Full. The project manager has sole authority over scope, schedule, budget, quality, and resource allocation. No external approval is required for any project decision.

**AI Augmentation Model:** The project manager operates under the Vargas 5-80-15 cooperative model:

- 5% — Human provides intent, context, constraints, and creative vision.
- 80% — AI executes drafts, analysis, code, document generation, and structured processing.
- 15% — Human validates, refines, decides, and locks.

The AI consultant (Claude) operates within the 80% execution band and provides expert judgment when requested. The AI consultant does not initiate work, expand scope, or make decisions without explicit direction from the project manager.

---

## 12. Authorizing Sponsor

**Sponsor:** Daddy (Project Originator)

**Authorization:** This charter authorizes the BVIPDS project to proceed through all four phases described in Section 4, subject to the phase gates defined in Section 7 and the boundary enforcement rules defined in Section 5.3.

**Standing Instruction:** No execution begins until the project manager explicitly directs which phase, milestone, or work item to pursue. The default state is hold.

**Date:** 2026-03-19

---

## 13. Version History

|Version|Date|Changes|
|---|---|---|
|1.0.0|2026-03-19|Initial project charter. PMBOK 4.1 compliant. Covers all four input categories (business documents, agreements, enterprise environmental factors, organizational process assets). Defines four-phase development plan, seven milestones, seven risks, fifteen requirements, and formal project boundaries. Companion assumption log established.|