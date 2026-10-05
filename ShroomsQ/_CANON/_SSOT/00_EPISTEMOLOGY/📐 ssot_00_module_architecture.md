---
type: ssot_00_foundations
category: module_architecture
version: 1.1.0
tier: foundation
last_updated: 2026-10-05
applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD]
status: canonical
trunk: BLACK
purpose: "Defines the Layer-Locked Module system, the plugin/extension architecture for attaching new capability to the LEECHSEED Character System without expanding the core schema. Establishes the module API contract, attachment protocol, data access rules, and the registry format for all current and planned modules."
dependencies: ["ssot_00_variable_registry", "ssot_00_base_60_number_system", "ssot_02_character_systems_vertical_slice"]
rung: standard
---
# 📐 SSOT: Module Architecture

## Table of Contents

1. [Purpose](#purpose)
2. [The Core Principle](#the-core-principle)
3. [What a Module Is](#what-a-module-is)
4. [Module Anatomy](#module-anatomy)
5. [The Attachment Protocol](#the-attachment-protocol)
6. [Data Access Rules](#data-access-rules)
7. [Module API Contract](#module-api-contract)
8. [Module Lifecycle](#module-lifecycle)
9. [Module Registry Format](#module-registry-format)
10. [Application Architecture Vision](#application-architecture-vision)
11. [Version History](#version-history)

---

## Purpose

The LEECHSEED Character System is a fixed schema. It does not grow. New character dimensions — physical sexuality analysis, walking style taxonomy, music interests, combat archetypes, cultural conditioning profiles — attach as **Layer-Locked Modules** (sub-tables under existing layers) rather than as new layers.

This document defines the architecture that makes that possible. It specifies how a module declares itself, which layer it attaches to, what data it can read and write, what format its variables take, and how it integrates with the core system's derived statistics and flag triggers.

The design philosophy mirrors audio production workstations (Ableton Live, Premiere Pro): a core engine with a standardized plugin interface. Modules are the VSTs/AUs of the character system. They process character data through a defined API without needing to understand the core engine's internals.

---

## The Core Principle

**The 12 layers do not change. Modules attach beneath them.**

The core schema is: L1 CORE, L2 VITAL, L3 SOCIAL, L4 WILL, L5 WOUND, L6 DRIVE, L7 ORIGIN, L8 IMPRINT, L9 EROS, L10 SHADOW, L11 DESTINY, L12 FUNCTION. These 12 layers define the complete character. They are the tracks in the DAW.

Modules are the effects and instruments loaded onto those tracks. A "Walking Style" module attaches to L2 VITAL because walking style is a physical expression. A "Music Interests" module attaches to L8 IMPRINT because music preference is conditioned by formative emotional experience. A "Combat Archetype" module attaches to L2 VITAL + L4 WILL because combat style involves physical capacity and psychological resistance.

The attachment point is not arbitrary. Every module must declare which layer it semantically belongs to, and that declaration is validated against the layer's domain definition.

---

## What a Module Is

A module is a self-contained extension that adds variables, sub-scales, or analytical frameworks to one or more layers of the LEECHSEED Character System. It has:

- A **module ID** and display name
- One or more **attachment points** (layer codes it connects to)
- A **variable set** (the new data fields it introduces)
- **Read dependencies** (which core variables it needs to read)
- **Write targets** (which new variables it creates)
- An optional **derived stat** (a computed value within the module)
- An optional **flag** (a boolean trigger within the module)
- A **tier requirement** (minimum character tier that uses this module)

A module does NOT:

- Add new layers to the core 12
- Modify core layer variables
- Override derived statistics or flag triggers defined in the core system
- Require other modules to function (modules are independent)

### Field Modules and Doc Modules

The word "module" has two meanings in the Command. Each meaning gets its own name.

- A **field module** is a Layer-Locked Module. It is a set of variables that attaches beneath a layer and lives under `MOD.<ID>`. This document and the Module Registry govern field modules.
- A **doc module** is a sibling document in `02_CHARACTER_SYSTEMS`, stamped `module_of: ssot_02_character_systems_vertical_slice`. It holds one method: the Step 1 gate, an ingest template, the Dramatica integration, or the state architecture. It adds no variables to a layer.

The slice governs a doc module. The registry never lists one. Write "field module" or "doc module" whenever the bare word could mean either.

---

## Module Anatomy

### Minimal Module (Data Only)

A module that adds descriptive variables to a layer. No computation. No flags.

```
MODULE: walking_style
  ATTACHMENT: L2.VITAL
  TIER_MIN: 3
  VARIABLES:
    MOD.WALK.gait_type:        enum {measured, urgent, languid, predatory, bouncing, shuffling}
    MOD.WALK.pace_default:     enum {slow, moderate, brisk, variable}
    MOD.WALK.signature_tell:   str  (freeform — "leads with shoulders", "feet never fully leave ground")
  READS: T1.VITAL.base_value, T3.SHADOW.regression_pattern
  WRITES: own variables only
  DERIVED: none
  FLAGS: none
```

### Standard Module (Data + Computation)

A module that adds variables and computes a derived value from them.

```
MODULE: combat_archetype
  ATTACHMENT: L2.VITAL, L4.WILL
  TIER_MIN: 3
  VARIABLES:
    MOD.COMBAT.archetype:       enum {striker, grappler, tactician, berserker, guardian, ghost}
    MOD.COMBAT.philosophy:      str  (freeform — "end it fast", "outlast and punish")
    MOD.COMBAT.win_condition:   str
    MOD.COMBAT.lethality:       int  SC-12 (0-12)
    MOD.COMBAT.survivability:   int  SC-12 (0-12)
  READS: T1.VITAL.base_value, T2.WILL.base_value, T3.SHADOW.regression_pattern
  WRITES: own variables only
  DERIVED:
    MOD.COMBAT.threat_index = (MOD.COMBAT.lethality_i + MOD.COMBAT.survivability_i) / 2
  FLAGS: none
```

### Full Module (Data + Computation + Flag)

A module that adds variables, computes values, and triggers a boolean flag.

```
MODULE: sexuality_profile
  ATTACHMENT: L9.EROS
  TIER_MIN: 3
  VARIABLES:
    MOD.SEX.orientation_coding:     enum {heteronormative, queer_coded, fluid, ambiguous, asexual_coded}
    MOD.SEX.power_dynamic:          enum {dominant, submissive, switch, neutral, contextual}
    MOD.SEX.display_confidence:     int  SC-12 (0-12)
    MOD.SEX.repression_index:       int  SC-12 (0-12, even only)
    MOD.SEX.erotic_autonomy:        int  SC-12 (0-12)
  READS: T3.EROS.shame_index, T3.EROS.erotic_blueprint_type, T3.SHADOW.shadow_density
  WRITES: own variables only
  DERIVED:
    MOD.SEX.sexual_legibility = (MOD.SEX.display_confidence_i - MOD.SEX.repression_index_i / 2)
  FLAGS:
    MOD.SEX.FLG.erotic_suppression: MOD.SEX.repression_index > 8 AND T3.EROS.shame_index > 6
```

---

## The Attachment Protocol

### Step 1: Declare Attachment Point(s)

The module author identifies which layer(s) the module semantically belongs to. The test: "Does this module's content fall within the domain definition of this layer?" If yes, attachment is valid. If the content spans two layers (like combat_archetype spanning VITAL and WILL), the module declares both attachment points.

### Step 2: Validate Against Layer Domain

Each layer has a single domain declaration (from the Vertical Slice SSOT). The module's variables must fall within that domain.

|Layer|Domain|Valid Module Content|
|---|---|---|
|L1 CORE|Cognitive/psychological mass|Intelligence sub-types, learning styles, ideological framework analysis|
|L2 VITAL|Physical/energetic presence|Walking style, body language, physical training history, combat physicality|
|L3 SOCIAL|Relational interface|Social strategy, communication style, public persona management|
|L4 WILL|Psychological resistance|Coping mechanisms, resilience sub-types, coercion response patterns|
|L5 WOUND|Accumulated damage|Trauma sub-typing, wound trigger catalogs, recovery tracking|
|L6 DRIVE|Motivation fuel|Ambition sub-types, motivational source analysis|
|L7 ORIGIN|Birth context|Cultural background detail, geographic origin, class sub-analysis|
|L8 IMPRINT|Emotional conditioning|Music interests, aesthetic preferences, taste formation, cultural conditioning|
|L9 EROS|Psycho-sexual conditioning|Sexuality profile, kink/fetish alignment, intimacy sub-typing|
|L10 SHADOW|Repressed content|Defense mechanism catalog, projection pattern sub-analysis|
|L11 DESTINY|Growth vector|Spiritual framework, philosophical alignment, belief system analysis|
|L12 FUNCTION|Narrative mechanics|Sub-storyform analysis, additional Dramatica element breakdowns|

### Step 3: Register Variables

All module variables follow the `MOD.[MODULE_CODE].[variable_name]` namespace. Module codes are unique 3-8 character uppercase identifiers registered in the Layer-Locked Module Registry.

Every module variable must:

- Use a scale class from the Base 60 SSOT (for numeric variables)
- Declare its type from the standard type set
- Declare its source (`authored`, `derived`, `computed`)
- Declare its tag, `Static` or `Dynamic`, so the state architecture knows whether to record a state diff for it (IF-00-02-27; IF catalog call 4, ruled 2026-10-05)
- List its read dependencies from core variables

### Step 4: Declare Access Pattern

The module specifies:

- **READS**: Which core variables the module needs to read (by canonical path)
- **WRITES**: Always "own variables only" — modules cannot write to core layer variables
- **DERIVED**: Any computed values within the module (with formulas)
- **FLAGS**: Any boolean triggers within the module (with conditions)

Module-defined derived stats and flags are namespaced under the module (`MOD.[CODE].derived_name`, `MOD.[CODE].FLG.flag_name`). They do not enter the core derived stat or flag tables. They are visible in the module's panel within the application UI.

---

## Data Access Rules

### What Modules CAN Read

- Any core layer variable (T1, T2, T3 prefixes)
- Any derived statistic (DRV prefix)
- Any flag state (FLG prefix)
- Any Character Astrology variable (AST prefix)
- Any other module's variables (MOD prefix) — but this creates a dependency and must be declared

### What Modules CANNOT Read

- State diff fields from other characters
- Relationship records (REL prefix) — synastry belongs to the relationship system, not to individual modules
- Raw Dramatica ingest template fields — modules read the L12 structured data, not the source template

### What Modules CAN Write

- Their own namespaced variables (`MOD.[CODE].*`)
- Their own derived stats and flags

### What Modules CANNOT Write

- Core layer variables (T1, T2, T3)
- Core derived statistics (DRV)
- Core flags (FLG)
- Character metadata (META)
- Character Astrology variables (AST)
- Any other module's variables

### Cross-Module Dependencies

If Module A reads Module B's variables, Module A must declare Module B as a dependency. The system validates that Module B is installed before Module A can activate. Circular dependencies are prohibited.

Dependency declarations follow: `DEPENDS_ON: [MODULE_CODE]`

---

## Module API Contract

The formal interface specification for modules. Any tool, plugin, or extension that adds capability to the character system implements this contract.

### Module Declaration Block

Every module declares itself with this header:

```yaml
MODULE_DECLARATION:
  module_id: [unique_code]
  display_name: [human readable name]
  version: [semver]
  author: [name or handle]
  attachment_points: [array of layer codes]
  tier_min: [1, 2, or 3]
  depends_on: [array of module_ids, or empty]
  description: [one sentence]
```

### Variable Declaration Block

Each variable in the module:

```yaml
VARIABLES:
  - path: MOD.[CODE].[name]
    display_name: [human readable]
    type: [int, float, str, enum, array_str, array_enum, bool]
    scale_class: [SC-N or N/A]
    display_range: [range or N/A]
    constraint: [divisibility constraint or none]
    default: [value or none]
    source: [authored, derived, computed]
    tag: [Static or Dynamic]
    behavior: [one sentence]
```

### Read Dependencies Block

```yaml
READS:
  - T1.VITAL.base_value
  - T3.SHADOW.regression_pattern
  # list all core variables the module needs
```

### Computation Block (Optional)

```yaml
DERIVED:
  - path: MOD.[CODE].[derived_name]
    formula_internal: [formula in 0-60 space]
    output_space: [SC-N or internal]
    input_constraints: [any divisibility requirements]

FLAGS:
  - path: MOD.[CODE].FLG.[flag_name]
    trigger: [boolean expression using module + core variables]
    states: [ACTIVE, PENDING, FIRED_PRE_STORY, INACTIVE]
    event_id: [fabula event_id, required in PENDING and FIRED_PRE_STORY]
```

A module flag uses the four core definitions unchanged. ACTIVE means the condition is met now. PENDING means it is met at a defined narrative event. FIRED_PRE_STORY means it was met before story entry. INACTIVE means it is not met. The author of a module links to the vertical slice's "Flag Trigger Conditions" section instead of redefining them.

A flag in PENDING stores the fabula `event_id` of the event that makes it true. A flag in FIRED_PRE_STORY stores the `event_id` of the story-entry marker. The fabula owns both ids (IF-00-04-06; IF catalog call 5, ruled 2026-10-05).

### Data Exchange Format

When the application loads a character record, modules receive their data as a flat key-value block:

```json
{
  "MOD.WALK.gait_type": "predatory",
  "MOD.WALK.pace_default": "brisk",
  "MOD.WALK.signature_tell": "leads with shoulders, slight leftward lean"
}
```

When the application saves, module data is written as a sub-table block within the character's structured data output:

```yaml
MOD_WALK:
  gait_type: predatory
  pace_default: brisk
  signature_tell: "leads with shoulders, slight leftward lean"
```

---

## Module Lifecycle

### Creation

1. Author writes module declaration + variable declarations following the API contract
2. Module is registered in the Layer-Locked Module Registry (next deliverable)
3. Variables are added to the Variable Registry under `MOD.[CODE].*` namespace

### Activation

1. User enables the module in the application (toggle in settings/plugin panel)
2. Application loads the module declaration and adds the variable fields to the relevant layer panel(s)
3. For existing characters, module fields are initialized to defaults or marked `[UNASSIGNED]`

### Population

1. User fills module fields for a character
2. Module derived stats and flags compute automatically
3. Module data saves alongside core data in the structured data block

### Deactivation

1. User disables the module
2. Module fields hide from the UI but data is NOT deleted
3. Re-enabling the module restores the data

### Retirement

1. Module is deprecated (version marked `retired`)
2. Data remains in character records for archival
3. Module no longer appears in the available modules list

---

## Application Architecture Vision

The target application follows the Ableton Live / Premiere Pro paradigm:

### Workspace Layout

```
┌─────────────────────────────────────────────┐
│  MENU BAR / MODE TOGGLE (Browse ⟷ Edit)     │
├──────────┬──────────────────────────────────┤
│          │                                   │
│ LAYER    │   MAIN PANEL                      │
│ RACK     │   (selected layer's variables,    │
│          │    module sub-tables,              │
│ L1-L12   │    or pipeline view)              │
│ listed   │                                   │
│ as       │                                   │
│ vertical │                                   │
│ strips   │                                   │
│          ├──────────────────────────────────┤
│          │   BOTTOM PANEL                    │
│          │   (Derived Stats + Flags +        │
│          │    Module computed values)         │
├──────────┴──────────────────────────────────┤
│  MODULE RACK (enabled modules as tabs)       │
└─────────────────────────────────────────────┘
```

### Key Interactions

- **Layer Rack** (left): Click a layer strip to load its variables in the Main Panel. The strip shows the layer name, tier color, and a completion indicator.
- **Main Panel** (center): Displays the selected layer's core variables plus any attached module sub-tables. In Edit mode, fields are editable. In Browse mode, read-only.
- **Bottom Panel**: Derived statistics and flags update in real time as values change. Module-specific derived stats appear when the relevant module tab is selected.
- **Module Rack** (bottom): Tabs for each enabled module. Clicking a tab highlights the module's attachment layer(s) in the Layer Rack and shows module-specific data in the Main Panel.
- **Mode Toggle**: Hotkey or button switches between Browse (read-only, all fields locked) and Edit (read-write, all fields editable). Edit mode shows a persistent indicator.

### Data Flow in the Application

```
User edits T2.WOUND.wound_score (Edit mode)
  → Application validates against SC-12 even constraint
  → Application recomputes all DRV.* that consume WOUND
  → Application re-evaluates all FLG.* that reference WOUND
  → Application re-evaluates all MOD.*.FLG.* that reference WOUND
  → Bottom Panel updates in real time
  → If any flag state changes, visual indicator fires
```

### File System Integration (Phase 4B+)

The local server component:

- Watches the Obsidian vault's `_AUTHORITATIVE/` folder for changes
- Loads character records from `.md` structured data blocks
- Saves edited records back to `.md` files in the canonical folder format
- Module data is stored as additional YAML blocks within the character's `.md` file

---

## Module Registry Format

Each module entry in the Layer-Locked Module Registry contains:

|Field|Description|
|---|---|
|`module_id`|Unique code|
|`display_name`|Human readable|
|`version`|Current version|
|`status`|`conceptual`, `planned`, `draft`, `active`, `absorbed`, `retired`. `absorbed` means the core schema now holds the module's fields, so the module is closed. A module moves to `planned` when its registry entry holds every field and a variable list. It moves to `draft` when the author writes the module declaration and the variable declarations under `MOD.[CODE].*`. It moves to `active` when the application can enable it and Chief rules it in. Chief rules every move.|
|`attachment_points`|Layer code(s)|
|`tier_min`|Minimum tier|
|`variable_count`|Number of variables|
|`has_derived`|Yes/No|
|`has_flags`|Yes/No|
|`depends_on`|Dependencies|
|`description`|One sentence|

The registry is [📐 ssot_00_module_registry.md](📐%20ssot_00_module_registry.md). It lists field modules only.

---

## Version History

|Version|Date|Changes|
|---|---|---|
|1.0.0|2026-03-08|Initial module architecture. Establishes Layer-Locked Module system, attachment protocol, data access rules, API contract, module lifecycle, application architecture vision, and registry format.|
|1.0.1|2026-10-04|BOLO 100 base batch 1 (B1, B3, B9, B13, B15), RULED Chief "REC.": frontmatter repaired to a multi-line block with `trunk`; table-of-contents links repointed to in-page anchors; dependency names fixed to the real file stems; new subsection separating field modules from doc modules; registry format gains the `conceptual` and `absorbed` statuses; the registry pointer replaces "the next deliverable".|
|1.0.2|2026-10-05|BOLO 102 batch C (Chief: "all recs"): C7, the four flag states defined by link to the slice; C8, the rule for when a module moves from `planned` to `draft` to `active`.|
|1.1.0|2026-10-05|BOLO 102 stage 2 (Chief: "My word"): Variable Declaration Block gains `tag: Static or Dynamic` (call 4); the flag block gains `event_id` for PENDING and FIRED_PRE_STORY (call 5).|
