---
original_path: "/home/claude/ssot_00_system_architecture_map.md"
source_conversation: "Character database system architecture with Dramatica and astrology integration"
created: 2026-02-25
trunk: BLACK
kind: generated-file
---

---
type: ssot_00_foundations
category: system_architecture
version: 1.0.0
last_updated: 2026-03-09
applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD, BOLD_VENTURE]
status: canonical
purpose: "Names every component across all three layers of the Bold Venture creative operating system (Library, Engines, Assembly), maps every connection between components, marks every undefined interface, and establishes the architectural principles that govern how the system grows."
dependencies: []
---

# 📐 ssot_00_system_architecture_map

## Table of Contents

1. [Purpose](#purpose)
2. [Core Methodology](#core-methodology)
    1. [Architectural Principles](#architectural-principles)
    2. [The Three Layers](#the-three-layers)
    3. [Layer 0 — Foundations](#layer-0-foundations)
    4. [Layer 1 — Library](#layer-1-library)
    5. [Layer 2 — Engines](#layer-2-engines)
    6. [Layer 3 — Assembly](#layer-3-assembly)
    7. [Cross-Layer Connection Map](#cross-layer-connection-map)
    8. [Undefined Interface Registry](#undefined-interface-registry)
    9. [Component Status Dashboard](#component-status-dashboard)
    10. [Build Priority Assessment](#build-priority-assessment)
3. [Implementation](#implementation)
4. [Examples](#examples)
5. [Version History](#version-history)

---

## Purpose

This document is the radar view of the entire Bold Venture creative operating system. It names every component across all layers, maps every connection between components, and marks every interface that has not yet been defined. No component exists in this system without an entry in this map. No connection between components exists without a documented interface. When a new component is proposed, it is added here first. When a connection is discovered, it is registered here. This document is the single point of truth for the question: "What is the system and how does it fit together?"

---

## Core Methodology

### Architectural Principles

**Principle 1: Three Layers, One Direction.** Raw material enters through the Library. Processing happens in the Engines. Output exits through the Assembly. Data flows from Layer 1 through Layer 2 into Layer 3. Layer 0 (Foundations) provides the infrastructure that all three layers stand on.

**Principle 2: MECE at Every Level.** Every component belongs to exactly one layer. Every sub-component belongs to exactly one component. Categories do not overlap. Together they cover the complete system. If a component appears to belong in two places, the architecture has a boundary error that must be resolved.

**Principle 3: Engines Are Pipelines, Not Destinations.** An Engine takes input, processes it through a defined sequence, and produces output. The output is consumed by another Engine or by the Assembly layer. No Engine operates as a standalone artifact. If an Engine has no consumer, it is either incomplete or misclassified.

**Principle 4: The Library Is Story-Agnostic.** Nothing in the Library is tied to a specific IP, project, or narrative. Library items are tagged, typed, and structured for retrieval. They become story-specific only when pulled into the Assembly layer.

**Principle 5: The Assembly Is Configuration, Not Creation.** A project in the Assembly layer does not create new material from scratch. It configures Library materials through Engine pipelines to produce story-specific output. The Assembly is a recipe that references pantry ingredients and kitchen techniques.

**Principle 6: Interfaces Before Internals.** When two components must communicate, define the interface (what data crosses the boundary, in what format, with what validation) before defining the internal logic of either component. The interface specification is the contract. Internal implementation can change without breaking the contract.

### The Three Layers

```
┌─────────────────────────────────────────────────────────────────────┐
│  LAYER 0 — FOUNDATIONS                                              │
│  (Infrastructure that all layers stand on)                          │
│  SSOT Standard · Base 60 · Variable Registry · Module Architecture  │
│  Design System · Development Doctrine · Operations Guides           │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│  LAYER 1 — LIBRARY          LAYER 2 — ENGINES                      │
│  (Story-agnostic             (Processing                            │
│   raw material)               pipelines)                            │
│                                                                     │
│  ┌──────────────┐          ┌──────────────────────┐                 │
│  │ Reference    │─────────▶│ CHARACTER SYSTEMS    │──┐              │
│  │ Characters   │          │ ENGINE               │  │              │
│  ├──────────────┤          ├──────────────────────┤  │              │
│  │ Visual       │          │ PLOT SYSTEMS         │  │              │
│  │ References   │─────────▶│ ENGINE               │──┤              │
│  ├──────────────┤          ├──────────────────────┤  │              │
│  │ Scene        │          │ WORLD SYSTEMS        │  │              │
│  │ References   │─────────▶│ ENGINE               │──┤              │
│  ├──────────────┤          ├──────────────────────┤  │              │
│  │ Framework    │          │ RELATIONSHIP         │  │              │
│  │ Collection   │─────────▶│ ENGINE               │──┤              │
│  ├──────────────┤          ├──────────────────────┤  │              │
│  │ Aesthetic    │          │ DIALOGUE             │  │              │
│  │ DNA / GUTS  │─────────▶│ ENGINE               │──┤              │
│  ├──────────────┤          ├──────────────────────┤  │              │
│  │ Audio/Music  │          │ AESTHETIC             │  │              │
│  │ References   │─────────▶│ ENGINE               │──┤              │
│  └──────────────┘          └──────────────────────┘  │              │
│                                                      │              │
│                              LAYER 3 — ASSEMBLY      │              │
│                              (IP-specific output)    │              │
│                                                      ▼              │
│                            ┌──────────────────────────┐             │
│                            │  OVEREXITOUT             │             │
│                            │  (The Outliers)          │             │
│                            ├──────────────────────────┤             │
│                            │  ASTRO7EX               │             │
│                            ├──────────────────────────┤             │
│                            │  LAKAD                  │             │
│                            ├──────────────────────────┤             │
│                            │  [FUTURE IPs]           │             │
│                            └──────────────────────────┘             │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

### Layer 0 — Foundations

Layer 0 is not a processing layer. It is the infrastructure on which all three operational layers depend. Every Foundation component is consumed by multiple components across Layers 1, 2, and 3.

| ID | Component | Status | Description |
|---|---|---|---|
| F.01 | **SSOT Standard Structure Template** | BUILT | The mandatory structural blueprint for all documentation. Defines YAML frontmatter, eight required sections, doctrinal sweep compliance. Every SSOT in the system conforms to this template. |
| F.02 | **Base 60 Number System** | BUILT | The mathematical foundation. 60 = 2²×3×5, 12 divisors. Defines SC-20 (primary attributes), SC-12 (sub-variables), SC-60 (internal computation). All numeric values in the character systems derive from this lattice. |
| F.03 | **Variable Registry** | BUILT | The canonical namespace for all variables across all systems. Convention: `[DOMAIN].[LAYER_CODE].[variable_name]`. 50+ variables defined with canonical paths, types, scale classes, constraints, defaults, sources, consumers. |
| F.04 | **Module Architecture** | BUILT | The plugin system specification. Layer-Locked Modules attach to specific layers and extend them without modifying core schemas. Three complexity tiers (minimal, standard, full). API contract defined. |
| F.05 | **Module Registry** | BUILT | The catalog of all modules. 14 modules: 1 active (DUALISM), 10 planned, 3 conceptual. Dependency map and build order documented. |
| F.06 | **Process Illustration** | BUILT | Four pipeline flow diagrams (Mermaid format, Obsidian-native). Flow A: Dramatica Extraction. Flow B: DAI Translation. Flow C: Vertical Slice. Flow D: State Diffs. Cross-Flow: Module Attachment. |
| F.07 | **Bold Venture Design System** | BUILT | The mandatory visual standard. Adapted from Astro UXDS v7. Dark navy palette (#101923 base), six-level status system (Off through Critical), Roboto typography, 4px spacing grid, 40 components with `bvx-` prefix. |
| F.08 | **Development Doctrine (BVDP-1)** | PLANNED | The philosophical backbone for how Bold Venture develops everything. USMC maneuver warfare philosophy, McKinsey MECE decomposition, DoD milestone gates, PMBOK measurement, Vargas 5-80% human-AI model. |
| F.09 | **Operational Guides (BVOG-0 through BVOG-5)** | PLANNED | Phase-specific tactical manuals for the six-phase development lifecycle. Intelligence, Framing, Design, Build, Deploy, AAR. |
| F.10 | **Operations Writing Guide** | REFERENCED | Referenced in SSOT dependencies. Standards for written output. Not yet delivered in this session. |
| F.11 | **Operations AI Instruction Protocol** | REFERENCED | Referenced in SSOT dependencies. Standards for AI-directed task delegation. Not yet delivered in this session. |

### Layer 1 — Library

The Library is the story-agnostic raw material warehouse. Nothing here is tied to any specific IP. Every item is tagged, typed, and structured for retrieval by Engines.

| ID | Component | Status | Description | Data Format |
|---|---|---|---|---|
| L1.01 | **Reference Character Collection** | PARTIALLY BUILT | Characters from other media, real people, archetypes collected for study and pattern extraction. The LoL character database (14-dimension schema across 160+ champions) is the most developed sub-collection. | .md files with structured variable stacks |
| L1.02 | **Visual Reference Collection** | NOT BUILT | Images, mood boards, aesthetic fragments, photography references. Organized by aesthetic taxonomy (TO BE DEFINED). | Image files + .md metadata tags |
| L1.03 | **Scene Reference Collection** | NOT BUILT | Scenes from films, books, games collected as structural specimens. Tagged by function (inciting incident, reversal, revelation, climax, etc.) and by emotional register. | .md files with structural tags |
| L1.04 | **Framework Collection** | PARTIALLY BUILT | Theoretical frameworks from narratology, psychology, design theory. Includes existing Obsidian vault content on Dramatica theory, narratology (fabula/syuzhet), screenwriting craft, and the Overlay Models document (7+ categories of psychological/narrative models). | .md SSOT-format documents |
| L1.05 | **Aesthetic DNA Collection (GUTS99)** | EXISTS EXTERNALLY | The grognard entries — aesthetic influences, taste data, cultural reference points that define Bold Venture's creative fingerprint. Currently exists in the external repo. | .md entries with tags |
| L1.06 | **Audio/Music Reference Collection** | NOT BUILT | Musical references, soundscapes, tonal palettes. Tagged by mood, tempo, instrumentation, narrative function. | Audio files + .md metadata |
| L1.07 | **Narratology Theory Collection** | PARTIALLY BUILT | Source theory documents being consolidated from multi-system PKM (Obsidian, Joplin, Logseq). Includes Dramatica theory summaries, movement/state theory, and structural analysis frameworks. | .md SSOT-format documents |

**Library Interface Contract (TO BE DEFINED):**
Every Library item must carry a minimum metadata set that allows Engines to discover and consume it. The metadata schema is:

```
library_item_id: [unique identifier]
library_type: [character | visual | scene | framework | aesthetic | audio | theory]
tags: [array of searchable tags]
source: [where this item came from]
date_collected: [when it entered the library]
ip_agnostic: true  # mandatory — Library items are never IP-specific
consumable_by: [array of Engine IDs that can process this item]
```

This schema is TO BE DEFINED as a formal specification.

### Layer 2 — Engines

Engines are processing pipelines. Each Engine takes structured input, processes it through a defined sequence of steps, and produces structured output that is consumed by another Engine or by the Assembly layer.

#### ENGINE 2.01: CHARACTER SYSTEMS ENGINE — STATUS: OPERATIONAL

The most developed Engine. Produces complete, validated, queryable character records from authoritative source documentation through a three-stage pipeline: Dramatica → Character Astrology → 12-Layer Vertical Slice.

| Sub-Component | ID | Status | SSOT Document |
|---|---|---|---|
| Dramatica Integration Protocol | 2.01.A | BUILT | `ssot_02_character_dramatica_integration` |
| Dramatica Ingest Template | 2.01.B | BUILT | `template_dramatica_ingest` |
| Character Astrology System | 2.01.C | BUILT | `ssot_02_character_astrology` |
| DAI (Dramatica-Astrology Interface) | 2.01.D | BUILT | `ssot_02_character_astrology_dai` |
| Character Astrology Ingest Template | 2.01.E | BUILT | `template_character_astrology_ingest` |
| Astrology-to-12-Layer Mapping | 2.01.F | BUILT | `ssot_02_character_astrology_12layer_mapping` |
| 12-Layer Vertical Slice Protocol | 2.01.G | BUILT | `ssot_03_character_systems_vertical_slice` |
| Character State Architecture | 2.01.H | BUILT | `ssot_02_character_state_architecture` |
| Step 1 Source Verification | 2.01.I | BUILT | `ssot_02_step1_source_verification` |
| Base 60 Number System (char-specific) | 2.01.J | BUILT | `ssot_00_base60_number_system` |
| Variable Registry (char-specific) | 2.01.K | BUILT | `ssot_00_variable_registry` |
| Module Architecture | 2.01.L | BUILT | `ssot_00_module_architecture` |
| Module Registry | 2.01.M | BUILT | `ssot_00_module_registry` |
| Process Illustration | 2.01.N | BUILT | `ssot_00_process_illustration` |

**Engine 2.01 Internal Pipeline:**
```
AUTHORITATIVE DOCUMENT [LOCKED]
       │
       ▼
DRAMATICA STORYFORM ──▶ DRAMATICA INGEST TEMPLATE [LOCKED]
                              │
                    ┌─────────┴─────────┐
                    ▼                   ▼
            DAI TRANSLATION       12-LAYER SYSTEM
            (18 steps)            (L12 direct feed)
                    │                   │
                    ▼                   │
            CHAR ASTROLOGY              │
            INGEST [LOCKED]             │
                    │                   │
                    └─────────┬─────────┘
                              ▼
                    STEP 1 VERIFICATION
                    (3-component gate)
                              │
                              ▼
                    VERTICAL SLICE
                    (7-step protocol)
                              │
                              ▼
                    CHARACTER RECORD [LOCKED]
                              │
                              ▼
                    STATE DIFFS (per narrative moment)
```

**Engine 2.01 Validated Output:**
Victoria Midnight — 11/11 fed layers CONSISTENT, all 6 derived stats validated, all 5 flags validated. Pipeline proven functional.

**Engine 2.01 Pending Items:**
Victoria Midnight Dramatica Ingest completion (~65 fields require storyform extraction). Field rename: `motivation_element` → `mc_problem_element` across all SSOTs. Base 60 recalibration propagation to Vertical Slice point budget tables.

---

#### ENGINE 2.02: PLOT SYSTEMS ENGINE — STATUS: FLAGGED / NOT BUILT

Referenced across multiple character system SSOTs as the downstream consumer of story-level data. Boundaries are documented but no internal specification exists.

| Sub-Component | ID | Status | Notes |
|---|---|---|---|
| 6 Movements / Lifecycle Protocol | 2.02.A | BOUNDARY DEFINED | Character Astrology Category 10. Centered on MC. Planet-to-movement mapping exists. |
| Timeline Coordinate System | 2.02.B | TO BE DEFINED | Replaces freeform `narrative_moment` field in state diffs with structured temporal keys. |
| Victoria-as-(0,0) Coordinate System | 2.02.C | CONCEPT ONLY | All characters measured by temporal + narrative distance from MC. |
| Scene-to-State Mapping | 2.02.D | TO BE DEFINED | Which scenes produce which state diffs. |
| Signpost Sequence Engine | 2.02.E | TO BE DEFINED | Dramatica signposts (4 per throughline) mapped to narrative timeline. |
| Act Structure / Storyweaving | 2.02.F | TO BE DEFINED | How the storyform argument is dramatized across scenes and sequences. |
| Reset Protocol | 2.02.G | BOUNDARY DEFINED | Character Astrology Category 15. Terminal reset at Movement 6 conclusion. |

**Engine 2.02 Consumes From:**
Engine 2.01 (character records, state diff format, MC-relative distance fields, movement tags).
Library Layer (scene references, framework collection).

**Engine 2.02 Produces For:**
Assembly Layer (scene sequences, act structures, plot timelines per IP).

---

#### ENGINE 2.03: RELATIONSHIP ENGINE — STATUS: PARTIALLY DEFINED

Relationship tracking architecture is defined in the Character State Architecture SSOT. The data structures exist but no processing pipeline has been specified.

| Sub-Component | ID | Status | Notes |
|---|---|---|---|
| Relationship Record Format | 2.03.A | DEFINED | character_a, character_b, type, status, synastry_data, state_history. |
| Synastry Computation | 2.03.B | BOUNDARY DEFINED | Character Astrology Category 11. Aspect mesh + composite chart. |
| Network Topology (Unicursal Hexagram) | 2.03.C | BOUNDARY DEFINED | Character Astrology Category 6. Six-vertex energy flow model. |
| Relationship State Tracking | 2.03.D | DEFINED | State history array keyed to narrative moments. |
| Cross-Character Query System | 2.03.E | TO BE DEFINED | "Show all characters where relationship to victoria_midnight has status = severed." |

**Engine 2.03 Consumes From:**
Engine 2.01 (locked character astrology charts for synastry, character IDs for relationship keying).

**Engine 2.03 Produces For:**
Engine 2.02 (relationship dynamics feed scene design).
Assembly Layer (relationship maps per IP).

---

#### ENGINE 2.04: WORLD SYSTEMS ENGINE — STATUS: NOT BUILT

No specification exists. This Engine would process world-building data — geography, institutions, technology, culture, economics, power structures — into structured, queryable world records.

| Sub-Component | ID | Status | Notes |
|---|---|---|---|
| World Record Schema | 2.04.A | TO BE DEFINED | What variables define a world/setting. |
| Institution Modeling | 2.04.B | TO BE DEFINED | "The System" in OVEREXITOUT is an institution. How is it structured as data? |
| Environmental Context Mapping | 2.04.C | TO BE DEFINED | How world data feeds character house placements (Character Astrology dependency). |
| Technology Level Tracking | 2.04.D | TO BE DEFINED | tech_level variable in L7 ORIGIN references world state. |
| Economic System Modeling | 2.04.E | TO BE DEFINED | "Salvage economy" in M1A requires world-level economic data. |

**Engine 2.04 Consumes From:**
Library Layer (framework collection, visual references, scene references).

**Engine 2.04 Produces For:**
Engine 2.01 (environmental context for house assignments, origin data).
Engine 2.02 (setting data for scenes).
Assembly Layer (world bibles per IP).

---

#### ENGINE 2.05: DIALOGUE ENGINE — STATUS: NOT BUILT

No specification exists. This Engine would process character voice data — speech patterns, vocabulary, rhetorical strategies, code-switching behavior — into dialogue generation guidelines or AI-augmented dialogue drafting.

| Sub-Component | ID | Status | Notes |
|---|---|---|---|
| Voice Profile Schema | 2.05.A | TO BE DEFINED | What variables define a character's speech. |
| Code-Switching Rules | 2.05.B | TO BE DEFINED | How speech changes by social context. Feeds from L3 SOCIAL and Character Astrology Ascendant. |
| Dialogue Constraint System | 2.05.C | TO BE DEFINED | Non-negotiables (Section 7 of authoritative docs) constrain what a character will and will not say. |
| VOICE Module (from Module Registry) | 2.05.D | CONCEPTUAL | Module Registry lists VOICE as a planned module. |

**Engine 2.05 Consumes From:**
Engine 2.01 (character records — L1 CORE, L3 SOCIAL, L8 IMPRINT, Ascendant, Mercury sign).
Library Layer (framework collection — linguistic and rhetorical models).

**Engine 2.05 Produces For:**
Assembly Layer (dialogue guidelines, voice sheets per character per IP).

---

#### ENGINE 2.06: AESTHETIC ENGINE — STATUS: NOT BUILT

No specification exists. This Engine would process aesthetic data — visual language, color palettes, architectural references, fashion, material textures — into production-ready aesthetic guidelines. The GUTS99 collection is the primary Library input.

| Sub-Component | ID | Status | Notes |
|---|---|---|---|
| Aesthetic Taxonomy | 2.06.A | TO BE DEFINED | How aesthetic data is categorized and tagged. |
| Character Aesthetic Profile | 2.06.B | TO BE DEFINED | Signature Imagery / Vibe (Section 8 of authoritative docs) formalized as structured data. |
| World Aesthetic Profile | 2.06.C | TO BE DEFINED | Visual language per world/setting/movement. |
| FASHION Module (from Module Registry) | 2.06.D | PLANNED | Module Registry lists FASHION as a planned module. |
| DESIGN Module (from Module Registry) | 2.06.E | CONCEPTUAL | Module Registry lists DESIGN as a conceptual module. |

**Engine 2.06 Consumes From:**
Library Layer (GUTS99, visual references, audio/music references).
Engine 2.01 (character Ascendant, Venus sign, signature imagery from authoritative doc).

**Engine 2.06 Produces For:**
Assembly Layer (aesthetic guides, mood boards, visual development packages per IP).
F.07 Bold Venture Design System (aesthetic decisions may inform application UI themes per IP).

---

### Layer 3 — Assembly

The Assembly layer contains IP-specific projects. Each project pulls from the Library and runs material through Engines to produce the narrative, characters, world, and aesthetic that constitute the IP.

| ID | Project | Status | Primary MC | Active Engines |
|---|---|---|---|---|
| A.01 | **OVEREXITOUT (The Outliers)** | IN DEVELOPMENT | Victoria "Tori" Midnight | 2.01 (Character Systems — validated with Victoria) |
| A.02 | **ASTRO7EX** | REFERENCED | TBD | Has existing Dramatica storyform + 22 PDF reports in external repo |
| A.03 | **LAKAD** | REFERENCED | TBD | No known development artifacts |
| A.04 | **[Future IPs]** | NOT STARTED | — | — |

**Assembly Project Structure (per IP):**

```
_AUTHORITATIVE/[IP]/
├── storyforms/
│   ├── [storyform_id]_storyform.md
│   └── ...
├── characters/
│   ├── [character_id]/
│   │   ├── [character_id]_authoritative.md       [LOCKED]
│   │   ├── [character_id]_dramatica_ingest.md    [LOCKED]
│   │   ├── [character_id]_astrology_ingest.md    [LOCKED/MVC]
│   │   ├── [character_id]_vertical_slice.md      [LOCKED]
│   │   └── states/
│   │       └── [character_id]_state_[moment].md
│   └── ...
├── relationships/
│   └── [relationship_id].md
├── world/
│   └── [TO BE DEFINED by Engine 2.04]
├── plot/
│   └── [TO BE DEFINED by Engine 2.02]
├── dialogue/
│   └── [TO BE DEFINED by Engine 2.05]
└── aesthetic/
    └── [TO BE DEFINED by Engine 2.06]
```

### Cross-Layer Connection Map

Every arrow below represents a data flow that requires a defined interface.

```
LIBRARY                  ENGINES                      ASSEMBLY
───────                  ───────                      ────────

L1.01 Reference  ──────▶ 2.01 Character Systems ────▶ A.01-04 characters/
      Characters         (study patterns,              (IP-specific character
                          inform taxonomy)              records)

L1.02 Visual     ──────▶ 2.06 Aesthetic Engine ─────▶ A.01-04 aesthetic/
      References         (process into guides)

L1.03 Scene      ──────▶ 2.02 Plot Systems ─────────▶ A.01-04 plot/
      References         (structural specimens)

L1.04 Frameworks ──────▶ ALL ENGINES ────────────────▶ (theoretical backing
                         (theoretical foundation)       for all output)

L1.05 GUTS99     ──────▶ 2.06 Aesthetic Engine ─────▶ A.01-04 aesthetic/
                         (aesthetic DNA)

L1.06 Audio      ──────▶ 2.06 Aesthetic Engine ─────▶ A.01-04 aesthetic/
                         (tonal palette)

L1.07 Theory     ──────▶ ALL ENGINES ────────────────▶ (methodology source)

ENGINE-TO-ENGINE:

2.01 Character ────────▶ 2.02 Plot (state diffs, MC coordinate)
2.01 Character ────────▶ 2.03 Relationship (charts for synastry)
2.01 Character ────────▶ 2.05 Dialogue (voice variables from layers)
2.01 Character ────────▶ 2.06 Aesthetic (Ascendant, Venus, imagery)
2.03 Relationship ─────▶ 2.02 Plot (relationship dynamics feed scenes)
2.04 World ────────────▶ 2.01 Character (env context for houses, origin)
2.04 World ────────────▶ 2.02 Plot (setting data for scenes)
```

### Undefined Interface Registry

Every connection in the system that has not yet been formally specified. These are the gaps. Closing them is a prerequisite for the system to operate as an integrated whole rather than a collection of isolated components.

| Interface | Between | Status | Priority | Notes |
|---|---|---|---|---|
| **INT-001** | Library metadata schema ↔ All Engines | TO BE DEFINED | HIGH | How Engines discover and consume Library items. |
| **INT-002** | Engine 2.01 ↔ Engine 2.02 | PARTIALLY DEFINED | HIGH | State diff format is defined. Timeline coordinates, scene-to-state mapping are not. |
| **INT-003** | Engine 2.01 ↔ Engine 2.03 | PARTIALLY DEFINED | MEDIUM | Synastry boundary defined. Computation pipeline is not. |
| **INT-004** | Engine 2.04 ↔ Engine 2.01 | TO BE DEFINED | MEDIUM | World data feeds character house placements and origin variables. No spec exists. |
| **INT-005** | Engine 2.01 ↔ Engine 2.05 | TO BE DEFINED | LOW | Character layer variables feed voice profiles. No spec exists. |
| **INT-006** | Engine 2.01 ↔ Engine 2.06 | TO BE DEFINED | LOW | Character aesthetic data (Ascendant, Venus, imagery) feeds aesthetic profiles. No spec exists. |
| **INT-007** | Engine 2.04 ↔ Engine 2.02 | TO BE DEFINED | MEDIUM | World setting data feeds scene design. No spec exists. |
| **INT-008** | Engine 2.03 ↔ Engine 2.02 | TO BE DEFINED | MEDIUM | Relationship dynamics feed scene/plot design. No spec exists. |
| **INT-009** | All Engines ↔ Assembly Layer | TO BE DEFINED | HIGH | How Engine output lands in the IP-specific folder structure. Currently defined only for Engine 2.01 (canonical folder structure). |
| **INT-010** | Assembly projects ↔ each other | TO BE DEFINED | LOW | Cross-IP references (shared universe elements). Not needed until multiple IPs are in active development. |
| **INT-011** | Library items ↔ Assembly projects | TO BE DEFINED | MEDIUM | How a Library item is "pulled into" a project without being modified. Reference-only or copy-on-use? |

### Component Status Dashboard

| Status | Count | Components |
|---|---|---|
| **BUILT** (SSOT exists, validated) | 14 | F.01–F.07, 2.01.A–2.01.N |
| **DEFINED** (boundary or format specified, no full SSOT) | 5 | 2.03.A, 2.03.B, 2.03.C, 2.03.D, 2.02.A |
| **PLANNED** (named, conceptualized, not specified) | 8 | F.08, F.09, 2.02.B–2.02.G, 2.05.D |
| **REFERENCED** (mentioned in existing SSOTs, not developed) | 4 | F.10, F.11, A.02, A.03 |
| **NOT BUILT** (named in this map for the first time) | 18 | L1.02, L1.03, L1.06, 2.02.B–2.02.F, 2.03.E, 2.04.A–2.04.E, 2.05.A–2.05.C, 2.06.A–2.06.C |
| **EXISTS EXTERNALLY** (lives outside SSOT ecosystem) | 2 | L1.01 (LoL DB), L1.05 (GUTS99) |
| **PARTIALLY BUILT** (some content exists, not SSOT-compliant) | 2 | L1.04, L1.07 |

**Total named components:** 53
**Total with complete SSOTs:** 14
**Total requiring specification before system integration:** 39

### Build Priority Assessment

Based on the current state (Engine 2.01 operational, one IP in development, solo developer + AI), the priority ordering for what to build next:

**Priority 1 — Immediate (enables current work to continue):**

| Component | Rationale |
|---|---|
| F.08 Development Doctrine (BVDP-1) | Governs how everything else gets built. Without it, each component is developed ad hoc. |
| F.09 BVOG-3 (Build and Execute Guide) | The operational guide for the phase the developer is currently in. |
| INT-001 Library metadata schema | Cannot collect material systematically without a tagging standard. |

**Priority 2 — Near-term (enables next IP development phase):**

| Component | Rationale |
|---|---|
| Engine 2.02 Plot Systems (core spec) | Victoria Midnight character record is complete. Next step is plotting her story. Plot Systems is the consumer. |
| INT-002 Character ↔ Plot interface (full spec) | The handoff from character to plot is the next pipeline connection. |
| Engine 2.03 Relationship Engine (pipeline spec) | Multiple characters will require relationship tracking for plot work. |

**Priority 3 — Medium-term (enables production quality):**

| Component | Rationale |
|---|---|
| Engine 2.04 World Systems (core spec) | OVEREXITOUT's "system" needs formal world modeling. |
| Engine 2.05 Dialogue Engine (core spec) | Dialogue is the primary output artifact for screenwriting. |
| Engine 2.06 Aesthetic Engine (core spec) | Visual development is needed for pitching and production. |
| L1.01–L1.07 Library formalization | Systematic collection requires formal structure. |

**Priority 4 — Long-term (enables scaling):**

| Component | Rationale |
|---|---|
| INT-009 Full Engine-to-Assembly interface | Currently only Character Systems has a defined landing zone. |
| INT-010 Cross-IP interface | Needed only when ASTRO7EX or LAKAD enter active development. |
| Application development (BVCC) | The software that operationalizes this entire architecture. Technology choice follows architecture completion. |

---

## Implementation

### Using This Document

1. Before proposing a new component, check whether it already exists in this map. If it does, the work is extending an existing component, not creating a new one.
2. Before building a new connection between components, check the Undefined Interface Registry. If the interface is listed as TO BE DEFINED, define the interface specification before implementing.
3. When a component's status changes (from PLANNED to BUILT, from TO BE DEFINED to DEFINED), update this document's Component Status Dashboard and connection map.
4. When a new Engine is proposed, it must be classified with a 2.XX ID, placed in the Engine layer, and its input sources and output consumers must be identified. If the Engine has no consumer, it is premature.
5. When a new Library collection is proposed, it must carry the Library metadata schema (INT-001) and identify which Engines can consume it.
6. When a new Assembly project is started, it must reference its active Engines and establish its canonical folder structure following the Assembly Project Structure template.

### Adding a New Component

1. Assign an ID following the layer convention (F.XX for Foundations, L1.XX for Library, 2.XX for Engines, A.XX for Assembly).
2. Name the component and write a one-sentence description.
3. Set the initial status (PLANNED, TO BE DEFINED, or BUILT if the SSOT already exists).
4. Identify all input sources and output consumers.
5. For each new connection, add an entry to the Undefined Interface Registry if no interface spec exists.
6. Update the Component Status Dashboard counts.
7. Update the Cross-Layer Connection Map if the component introduces new data flows.

### Reviewing the Architecture

At each major development milestone (new Engine built, new IP started, doctrine revision), review this document against reality. The review asks three questions: Does every built component appear in this map? Does every connection in the map have a defined or at-minimum-documented interface? Are the priority assessments still correct?

---

## Examples

### Example 1: Adding a New Character to OVEREXITOUT

The developer wants to add a Tier 3 character (an Impact Character) to OVEREXITOUT. The System Architecture Map shows the path: write an authoritative document → run it through Engine 2.01 (Character Systems) → the Engine's internal pipeline produces Dramatica Ingest → Character Astrology Ingest → Vertical Slice. The output lands in the Assembly layer at `_AUTHORITATIVE/OVEREXITOUT/characters/[new_character_id]/`. The developer consults the Step 1 Source Verification Protocol (2.01.I) to confirm all upstream documents are locked before proceeding. No new architecture is needed. The existing pipeline handles it.

### Example 2: Starting Plot Development for OVEREXITOUT

The developer wants to begin plotting scenes. The System Architecture Map shows that Engine 2.02 (Plot Systems) is the required processor, but its status is FLAGGED / NOT BUILT. The developer cannot plot systematically without this Engine. The Build Priority Assessment confirms Engine 2.02 is Priority 2. The developer's next action is to specify Engine 2.02's core components, starting with the Timeline Coordinate System (2.02.B) and Scene-to-State Mapping (2.02.D), because those are the interfaces that connect the completed character records to scene design. The interface INT-002 (Character ↔ Plot) must be fully defined as part of this work.

---

## Version History

| Version | Date | Changes |
|---|---|---|
| 1.0.0 | 2026-03-09 | Initial System Architecture Map. Three-layer model (Library, Engines, Assembly) with Layer 0 Foundations. 53 named components across all layers. 11 foundations, 7 library collections, 6 engines with 35 sub-components, 4 assembly projects. 11 undefined interfaces registered. Component status dashboard. Build priority assessment in four tiers. Cross-layer connection map. |
