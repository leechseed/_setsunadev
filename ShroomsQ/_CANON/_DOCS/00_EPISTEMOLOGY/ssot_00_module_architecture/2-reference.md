---
title: Module architecture: reference
type: reference
for: A designer looking up a module block, rule or lifecycle stage
does: Lists every component and part of the module architecture doc
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/00_EPISTEMOLOGY/📐 ssot_00_module_architecture.md
source_version: 1.0.1
---

**Who it's for:** a designer looking up a module rule · **What it does:** lists every block, rule and stage in the module architecture doc · **Type:** reference

# Module architecture: reference

Source: `ShroomsQ/_CANON/_SSOT/00_EPISTEMOLOGY/📐 ssot_00_module_architecture.md`, version 1.0.1, status canonical, trunk BLACK, tier foundation, last updated 2026-10-04. Dependencies: `ssot_00_variable_registry`, `ssot_00_base_60_number_system`, `ssot_02_character_systems_vertical_slice`. Why it exists: see the [concept](1-concept.md). Registry of modules: [ssot_00_module_registry](../ssot_00_module_registry/2-reference.md).

## The Core Principle

The 12 layers do not change. Modules attach beneath them. The layers are tracks and modules are effects and instruments loaded onto them. Examples: Walking Style on L2 VITAL; Music Interests on L8 IMPRINT; Combat Archetype on L2 VITAL plus L4 WILL. Every module declares its layer, and the declaration is validated against the layer's domain.

## What a Module Is

A self-contained extension that adds variables, sub-scales or analytical frameworks to one or more layers.

A module has:
- a module ID and display name;
- one or more attachment points (layer codes);
- a variable set;
- read dependencies;
- write targets (its own new variables);
- an optional derived stat;
- an optional flag;
- a tier requirement (minimum character tier).

A module does not add layers, modify core variables, override core derived stats or flags, or require other modules.

### Field Modules and Doc Modules

- **Field module:** a Layer-Locked Module. Variables attach beneath a layer under `MOD.<ID>`. This doc and the Module Registry govern it.
- **Doc module:** a sibling document in `02_CHARACTER_SYSTEMS`, stamped `module_of: ssot_02_character_systems_vertical_slice`. It holds one method (the Step 1 gate, an ingest template, the Dramatica integration or the state architecture). It adds no layer variables.
- The slice governs doc modules. The registry never lists one.

## Module Anatomy

Three shapes. Each is written in a MODULE block with ATTACHMENT, TIER_MIN, VARIABLES, READS, WRITES, DERIVED and FLAGS.

### Minimal Module (Data Only)

Descriptive variables, no computation, no flags. Example `walking_style`: attaches to L2.VITAL, TIER_MIN 3. Variables `MOD.WALK.gait_type` (enum: measured, urgent, languid, predatory, bouncing, shuffling), `MOD.WALK.pace_default` (enum: slow, moderate, brisk, variable), `MOD.WALK.signature_tell` (str, freeform). Reads `T1.VITAL.base_value` and `T3.SHADOW.regression_pattern`.

### Standard Module (Data + Computation)

Variables plus one derived value. Example `combat_archetype`: attaches to L2.VITAL and L4.WILL, TIER_MIN 3. Variables `archetype` (enum: striker, grappler, tactician, berserker, guardian, ghost), `philosophy` (str), `win_condition` (str), `lethality` and `survivability` (int, SC-12). Reads `T1.VITAL.base_value`, `T2.WILL.base_value`, `T3.SHADOW.regression_pattern`. Derived: `MOD.COMBAT.threat_index = (MOD.COMBAT.lethality_i + MOD.COMBAT.survivability_i) / 2`.

### Full Module (Data + Computation + Flag)

Variables, a derived value and a flag. Example `sexuality_profile`: attaches to L9.EROS, TIER_MIN 3. Variables `orientation_coding`, `power_dynamic`, `display_confidence` (SC-12), `repression_index` (SC-12, even only), `erotic_autonomy` (SC-12). Reads `T3.EROS.shame_index`, `T3.EROS.erotic_blueprint_type`, `T3.SHADOW.shadow_density`. Derived: `MOD.SEX.sexual_legibility`. Flag: `MOD.SEX.FLG.erotic_suppression` fires when `repression_index > 8 AND T3.EROS.shame_index > 6`.

## The Attachment Protocol

Four steps.

### Step 1: Declare Attachment Point(s)

The author names the layer the module belongs to. The test: does the content fall within that layer's domain? A module that spans two layers declares both.

### Step 2: Validate Against Layer Domain

Each layer has one domain, from the Vertical Slice SSOT.

| Layer | Domain | Valid content |
|---|---|---|
| L1 CORE | Cognitive/psychological mass | Intelligence sub-types, learning styles, ideological framework analysis |
| L2 VITAL | Physical/energetic presence | Walking style, body language, physical training history, combat physicality |
| L3 SOCIAL | Relational interface | Social strategy, communication style, public persona management |
| L4 WILL | Psychological resistance | Coping mechanisms, resilience sub-types, coercion response patterns |
| L5 WOUND | Accumulated damage | Trauma sub-typing, wound trigger catalogs, recovery tracking |
| L6 DRIVE | Motivation fuel | Ambition sub-types, motivational source analysis |
| L7 ORIGIN | Birth context | Cultural background detail, geographic origin, class sub-analysis |
| L8 IMPRINT | Emotional conditioning | Music interests, aesthetic preferences, taste formation, cultural conditioning |
| L9 EROS | Psycho-sexual conditioning | Sexuality profile, kink/fetish alignment, intimacy sub-typing |
| L10 SHADOW | Repressed content | Defense mechanism catalog, projection pattern sub-analysis |
| L11 DESTINY | Growth vector | Spiritual framework, philosophical alignment, belief system analysis |
| L12 FUNCTION | Narrative mechanics | Sub-storyform analysis, extra Dramatica element breakdowns |

### Step 3: Register Variables

Variables use the namespace `MOD.[MODULE_CODE].[variable_name]`. A module code is a unique 3-8 character uppercase identifier registered in the Layer-Locked Module Registry. Every variable uses a Base 60 scale class (if numeric), declares a type from the standard set, declares its source (`authored`, `derived`, `computed`) and lists its core read dependencies.

### Step 4: Declare Access Pattern

- **READS:** core variables needed, by canonical path.
- **WRITES:** always "own variables only".
- **DERIVED:** computed values with formulas.
- **FLAGS:** boolean triggers with conditions.

Module derived stats and flags use `MOD.[CODE].derived_name` and `MOD.[CODE].FLG.flag_name`. They stay out of the core tables and show in the module's panel.

## Data Access Rules

### What Modules CAN Read

Any core layer variable (T1, T2, T3); any derived statistic (DRV); any flag state (FLG); any Character Astrology variable (AST); any other module's variables (MOD), declared as a dependency.

### What Modules CANNOT Read

State diff fields from other characters; relationship records (REL), since synastry belongs to the relationship system; raw Dramatica ingest template fields (modules read structured L12 data).

### What Modules CAN Write

Their own `MOD.[CODE].*` variables, and their own derived stats and flags.

### What Modules CANNOT Write

Core layer variables (T1, T2, T3); core derived statistics (DRV); core flags (FLG); character metadata (META); Character Astrology variables (AST); any other module's variables.

### Cross-Module Dependencies

If Module A reads Module B, Module A declares `DEPENDS_ON: [MODULE_CODE]`. The system checks Module B is installed before Module A activates. Circular dependencies are prohibited.

## Module API Contract

The interface any tool, plugin or extension implements.

### Module Declaration Block

YAML `MODULE_DECLARATION` with fields: `module_id`, `display_name`, `version` (semver), `author`, `attachment_points` (layer codes), `tier_min` (1, 2 or 3), `depends_on` (module ids or empty), `description` (one sentence).

### Variable Declaration Block

YAML `VARIABLES`, one item per variable, fields: `path` (`MOD.[CODE].[name]`), `display_name`, `type` (int, float, str, enum, array_str, array_enum, bool), `scale_class` (SC-N or N/A), `display_range`, `constraint` (divisibility or none), `default`, `source` (authored, derived, computed), `behavior` (one sentence).

### Read Dependencies Block

YAML `READS`: a list of core variable paths, such as `T1.VITAL.base_value`.

### Computation Block (Optional)

- `DERIVED` items: `path`, `formula_internal` (0-60 space), `output_space` (SC-N or internal), `input_constraints`.
- `FLAGS` items: `path` (`MOD.[CODE].FLG.[flag_name]`), `trigger` (boolean expression), `states` (ACTIVE, PENDING, FIRED_PRE_STORY, INACTIVE).

### Data Exchange Format

On load, a module receives a flat key-value JSON block, for example `"MOD.WALK.gait_type": "predatory"`. On save, module data is written as a sub-table block, for example `MOD_WALK:` with `gait_type: predatory`.

## Module Lifecycle

Five stages.

### Creation

1. The author writes the module declaration and variable declarations.
2. The module is registered in the Layer-Locked Module Registry.
3. Variables are added to the Variable Registry under `MOD.[CODE].*`.

### Activation

1. The user enables the module in the plugin panel.
2. The application loads the declaration and adds fields to the relevant layer panels.
3. Existing characters get defaults or `[UNASSIGNED]`.

### Population

1. The user fills module fields for a character.
2. Module derived stats and flags compute automatically.
3. Module data saves with core data in the structured block.

### Deactivation

1. The user disables the module.
2. Fields hide. Data is not deleted.
3. Re-enabling restores the data.

### Retirement

1. The module is deprecated (version marked `retired`).
2. Data stays in character records for archive.
3. The module leaves the available list.

## Application Architecture Vision

The target application follows a music-workstation paradigm. The source frames it as a vision, not a built tool.

### Workspace Layout

A menu bar with a Browse/Edit mode toggle on top. A Layer Rack (L1-L12 as vertical strips) on the left. A Main Panel in the center. A Bottom Panel below it. A Module Rack at the very bottom, with enabled modules as tabs.

### Key Interactions

- **Layer Rack:** click a strip to load its variables. The strip shows name, tier color and a completion indicator.
- **Main Panel:** shows the layer's core variables and module sub-tables. Editable in Edit mode, read-only in Browse.
- **Bottom Panel:** derived stats and flags update in real time. Module stats show when the module tab is selected.
- **Module Rack:** a tab per enabled module. Clicking one highlights its attachment layers.
- **Mode Toggle:** a hotkey or button switches Browse and Edit. Edit mode shows a persistent indicator.

### Data Flow in the Application

When the user edits `T2.WOUND.wound_score` in Edit mode: the application validates the SC-12 even constraint; recomputes every DRV that uses WOUND; re-evaluates every FLG and `MOD.*.FLG.*` that references WOUND; updates the Bottom Panel; and fires a visual indicator if a flag changes state.

### File System Integration (Phase 4B+)

The local server watches the Obsidian vault's `_AUTHORITATIVE/` folder, loads character records from `.md` structured blocks, and saves edited records back in the canonical folder format. Module data is stored as extra YAML blocks in the character's `.md` file.

## Module Registry Format

Each registry entry carries these fields.

| Field | Meaning |
|---|---|
| `module_id` | Unique code |
| `display_name` | Human readable |
| `version` | Current version |
| `status` | `conceptual`, `planned`, `draft`, `active`, `absorbed`, `retired`. `absorbed` means the core schema now holds the module's fields, so the module is closed. |
| `attachment_points` | Layer code(s) |
| `tier_min` | Minimum tier |
| `variable_count` | Number of variables |
| `has_derived` | Yes or No |
| `has_flags` | Yes or No |
| `depends_on` | Dependencies |
| `description` | One sentence |

The registry is `ShroomsQ/_CANON/_SSOT/00_EPISTEMOLOGY/📐 ssot_00_module_registry.md`. It lists field modules only.

> **OPEN:** the source's `FLAGS` block lists four states (ACTIVE, PENDING, FIRED_PRE_STORY, INACTIVE) but defines none of them here.

Related pages: [concept](1-concept.md) · [how-to](3-how-to.md) · [tutorial](4-tutorial.md)
