---

## type: ssot_02_character_systems category: character_astrology version: 1.0.0 last_updated: 2026-03-03 applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD] status: canonical purpose: "Defines the Character Astrology system as a deterministic character rendering engine within the LEECHSEED pipeline. Establishes narrative-first derivation policy, separates 15 framework categories into character-level and story-level domains, and specifies the system's relationship to Dramatica and the 12-Layer Character Database." dependencies: ["ssot_02_character_dramatica_integration", "ssot_03_character_systems_vertical_slice"] supersedes: ["ssot_narrative_astrology_framework", "ssot_narrative_astrology_modular_toolkit"]
---
# 📐 SSOT: Character Astrology

## Table of Contents

1. [Purpose](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#purpose)
2. [What Character Astrology Is](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#what-character-astrology-is)
3. [What Character Astrology Is Not](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#what-character-astrology-is-not)
4. [The Narrative-First Policy](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#the-narrative-first-policy)
5. [Domain Classification: Character-Level vs Story-Level](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#domain-classification)
6. [Character-Level Categories](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#character-level-categories)
7. [Story-Level Categories](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#story-level-categories)
8. [The Dramatica-Astrology Interface (DAI)](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#the-dramatica-astrology-interface)
9. [Pipeline Position](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#pipeline-position)
10. [Relationship to the 12-Layer Character Database](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#relationship-to-the-12-layer-character-database)
11. [Version History](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#version-history)

---

## Purpose

This document defines **Character Astrology** — a deterministic character rendering engine that translates Dramatica storyform outputs into astrological notation, producing a secondary symbolic dataset for each character. Character Astrology sits between Dramatica and the 12-Layer Character Database in the pipeline. It consumes locked Dramatica data and produces astrological variables that feed Layers 7 through 11 of the Vertical Slice.

This SSOT supersedes both prior "Narrative Astrology" documents. The system has been renamed to **Character Astrology** to reflect its function: it operates on characters, not on narratives broadly. It is classified under `02_CHARACTER_SYSTEMS`.

---

## What Character Astrology Is

Character Astrology is a **notation system**. It takes the narrative truths established by Dramatica and encodes them in astrological language — planets, signs, houses, aspects, dignities. The resulting chart is not a horoscope. It is a second representation of the same underlying character data, expressed in a symbolic vocabulary that generates additional depth, internal contradiction, behavioral texture, and cross-character collision logic.

**Core definitions:**

- **The Chart**: A character's source code. A structured symbolic dataset derived from locked narrative positions.
- **The Character**: The compiled entity. The behavioral output that emerges when the chart's variables interact under story conditions.
- **The Story**: The execution environment. The external conditions that activate, suppress, or transform chart variables.

Character Astrology treats characters as **deterministic systems** governed by variables and logic gates rather than arbitrary personality traits. Every behavioral output traces back to a specific variable configuration in the chart. If the behavior cannot be traced, the chart is incomplete — not the character.

---

## What Character Astrology Is Not

Character Astrology does not produce narrative structure. That is Dramatica's domain. Character Astrology does not assign numeric values to character layers. That is the 12-Layer system's domain. Character Astrology does not generate plot events, scene sequences, or story timelines. Those belong to plot_systems.

Character Astrology produces a **symbolic character dataset** — a natal chart with planetary positions, aspects, dignities, and house placements — that other systems consume. It is a translation layer, not a destination.

Character Astrology is also not traditional astrology applied to fictional characters. It borrows astrological vocabulary and structural logic because that vocabulary provides a mature, internally consistent symbolic language for encoding psychological complexity. The framework is deterministic where traditional astrology is interpretive. Every assignment is justified by a locked Dramatica position, not by intuition or aesthetic preference.

---

## The Narrative-First Policy

**Governing principle:** Dramatica defines the narrative truth. Character Astrology encodes that truth in astrological language. The chart serves the story. The story does not serve the chart.

**Operational rules:**

1. No astrological variable is assigned without a Dramatica justification. Every planetary placement, aspect, and dignity traces back to a specific element, throughline variable, or structural role in the locked Dramatica ingest.
    
2. When the astrological vocabulary suggests a character behavior that contradicts the locked Dramatica data, the Dramatica data governs. The astrological assignment is revised, not the storyform.
    
3. Chart generation follows a fixed derivation sequence (defined in the DAI Expansion document, deliverable 2B). The sequence begins with the Dramatica ingest and proceeds outward through planetary assignments. No step in the sequence is skipped or reordered.
    
4. Complete chart generation is not required for the Vertical Slice to proceed. A partial chart with core planets assigned (Sun, Moon, Mercury, Venus, Mars, Saturn, Ascendant) is sufficient for L7-L11 population. Outer planets (Jupiter, Uranus, Neptune, Pluto) and advanced configurations (progressions, transits) are populated as development continues.
    
5. The narrative-first policy applies to all tiers. Tier 3 characters receive full chart generation. Tier 2 characters receive a partial chart (Sun, Moon, and one or two defining aspects) derived from their element signature. Tier 1 characters do not receive Character Astrology treatment.
    

---

## Domain Classification

The original framework defined 15 categories. These categories remain valid. What changes is their classification: some are **character-level** (belonging to the static character record and the Character Astrology Ingest Template) and others are **story-level** (belonging to the state overlay system, relationship tables, or plot_systems).

The classification principle: if the data describes who the character IS at the point of canonical definition, it is character-level. If the data describes what is HAPPENING TO the character at a specific narrative moment, it is story-level.

### Character-Level Categories (Static Chart)

These categories produce data that enters the Character Astrology Ingest Template and feeds the 12-Layer Vertical Slice.

|#|Category|Domain|Function|
|---|---|---|---|
|1|Systemic Core Philosophy|Meta|Governing principles for the entire system. Not a data category — a design philosophy.|
|2|Dramatica-Astrology Interface (DAI)|Interface|Translation rules from Dramatica to astrological variables. Defined in DAI Expansion (2B).|
|3|Personal Stack (Inner Planets)|Character|Sun, Moon, Mercury, Venus, Mars — the character's functional processing units.|
|4|Structural Stack (Outer Planets)|Character|Jupiter, Saturn, Uranus, Neptune, Pluto — systemic environment and historical forces.|
|5|Interface Layer (Angles)|Character|Ascendant, Midheaven, Descendant, IC — how the character renders in the world.|
|7|Aspect Logic Gates|Character|Geometric relationships between planets — the character's internal friction and flow patterns.|
|8|House Systems|Character|Environmental directories where planetary action operates.|
|9|Planetary Dignities|Character|Efficiency ratings for each variable in its assigned environment.|
|14|Void Variable (12th House)|Character|The system recursion log — stored deleted memories, previous-state data, ghost-code foundation.|

### Story-Level Categories (State Overlays / Relationship / Plot)

These categories produce data that does NOT enter the static character record. They belong to downstream systems.

|#|Category|Domain|Destination|
|---|---|---|---|
|6|Network Topology (Unicursal Hexagram)|Relationship|Relationship tracking tables. Defines energy flow patterns between characters.|
|10|Lifecycle Protocol (6 Movements)|Story Structure|Plot_systems. Defines the macro-arc sequence centered on the MC.|
|11|Synastry Overlays|Relationship|Relationship tables. Collision detection between character charts.|
|12|Progressions (Internal Clock)|State Overlay|Character state diff system. Represents code aging over narrative time.|
|13|Transits (External Commands)|State Overlay|Character state diff system. Represents external events activating chart variables.|
|15|Reset Protocol (Systemic Wipe)|Story Structure|Plot_systems. Terminal reset at Movement 6 conclusion.|

**The static character record never changes.** Progressions and transits create state diffs that overlay on the static chart. Synastry creates relationship records that reference two static charts. Movements create story-structure records that reference the MC's chart as the (0,0) coordinate. None of these operations modify the natal chart itself.

---

## Character-Level Categories

### Category 1: Systemic Core Philosophy

Characters operate as deterministic entities defined by variables and logic gates rather than arbitrary personality traits. The astrological chart provides the source code from which character behavior compiles. This is the governing design philosophy, not a data-producing category. It is restated here as the foundational principle that all other categories serve.

### Category 3: Personal Stack (The Hardware)

The inner planets represent the character's functional processing units. These are the variables that produce observable behavior moment to moment.

**SUN** (`IDENTITY_AXIS`): The central processor. Defines what the character believes they are. Generates the thematic question. Derived from the MC Domain and MC Concern intersection in the Dramatica ingest.

**MOON** (`INTERNAL_STATE`): The instinctual default and subconscious memory bank. Under stress, the character's logic collapses into this variable. Derived from the MC Problem and MC Response intersection — the place the character goes when their primary processing fails.

**MERCURY** (`CODE_INTERPRETATION`): The logic gate. Controls speech, tactical navigation, code-breaking, and the ability to comprehend. Derived from the Unique Ability and the Methodology quad — how the character processes and acts on information.

**VENUS** (`VALUE_VECTOR`): The priority sensor. Determines what resources or relationships the character will attempt to acquire. Derived from the MC Concern and the Purpose quad — what the character values and why.

**MARS** (`ACTION_PROTOCOL`): The execution command. Controls aggression, kinetic movement, sexual energy, and physical will. Derived from the Approach (Do-er/Be-er) and the Motivation quad — what drives the character to act and how that action manifests.

### Category 4: Structural Stack (The Limit)

The outer planets represent the systemic environment, historical forces, and boundary conditions that constrain or transform the character.

**JUPITER** (`REDUNDANCY`): The system's permission for growth. Where the character finds temporary safety, resource spikes, or expansion. Derived from the MC Unique Ability — the one capacity that gives the character an edge.

**SATURN** (`ENTROPY_LIMITER`): The boundary variable. Represents the rules, the antagonist principle, and the constraint state. Derived from the MC Critical Flaw and the Inhibitor — the hard-coded limit the character cannot bypass without transformation.

**URANUS** (`BREACH_PROTOCOL`): Sudden shifts in code. The awakening variable that disrupts the loop. Derived from the MC Solution — the thing the character must eventually adopt or accept, which initially appears as disruption.

**NEPTUNE** (`HAUNT_SIGNAL`): The source of glitches, illusions, and synthetic hauntings. Derived from the MC Symptom — the false signal the character chases instead of addressing the actual problem.

**PLUTO** (`TERMINATION_CODE`): The ultimate reset. Intense power dynamics leading to total character exhaustion. Derived from the Story Outcome and Story Judgment intersection — the terminal condition of the narrative argument.

### Category 5: Interface Layer (The Angles)

The Angles define how the character is rendered and recorded in the narrative world.

**ASCENDANT** (`CHARACTER_UI_SKIN`): The immediate aesthetic and first-response style. The visible mask. Derived from Approach (Do-er/Be-er) combined with the MC Critical Flaw — the interface the world sees, including its exploit vector.

**MIDHEAVEN** (`CHARACTER_OUTPUT_LOG`): The public legacy and narrative achievement. The character's output as the world records it. Derived from the Story Goal and the character's relationship to it.

**DESCENDANT** (`CHARACTER_SHADOW_INTERFACE`): What the character lacks and seeks in others. The inverse of the Ascendant. Derived from the MC Direction — what the character moves toward in relationships.

**IC** (`CHARACTER_ROOT_ORIGIN`): The private origin and hidden trauma foundation. Derived from the MC Benchmark and Origin layer data — the buried measurement standard against which the character unconsciously judges all progress.

### Category 7: Aspect Logic Gates

Geometric relationships between planetary variables function as logic gates that define internal friction and flow.

**CONJUNCTION** (AND Gate): Two variables fuse into a single command. Both execute simultaneously. Produces intensity and singularity of purpose.

**SQUARE** (NOT Gate): Friction that forces a state change. Variable A prevents Variable B from executing cleanly. Produces the internal turning points that drive character movement.

**OPPOSITION** (XOR Gate): A binary choice. The character cannot execute both variables simultaneously. Produces the either/or dilemmas that define key decisions.

**TRINE** (OR Gate): A passive talent. Data flows freely between variables without friction. Produces natural ability that can lead to stagnation because there is no internal pressure to grow.

**Aspect assignment rule:** Aspects are not randomly assigned. They are derived from the tension relationships within the Dramatica element quads. When two Dramatica elements in a character's assignment are in natural tension (e.g., Equity and Inequity as Problem/Solution), the corresponding planets receive a hard aspect (Square or Opposition). When two elements flow naturally (e.g., elements within the same quad that do not conflict), the corresponding planets receive a soft aspect (Trine or Sextile). Conjunctions are reserved for cases where two Dramatica functions fuse in the character (e.g., when the MC Problem and the Motivation element point to the same behavioral output).

### Category 8: House Systems (Environmental Context)

Houses are the directories where planetary action operates. They define the life domain in which each variable expresses itself.

**Angular Houses (1, 4, 7, 10)**: High-priority execution. Action here is visible, immediate, and shifts the narrative. Planets in angular houses produce behavior the story cannot ignore.

**Succedent Houses (2, 5, 8, 11)**: Resource management. Action here governs maintenance, assets, value exchange, and the infrastructure that supports or undermines the character's angular-house actions.

**Cadent Houses (3, 6, 9, 12)**: Background processing. Action here governs communication, preparation, belief systems, and hidden ghost-code. Planets in cadent houses produce behavior that operates beneath the surface until triggered.

**House assignment rule:** House placement is derived from the story's environmental context for the character. The MC Domain determines which house system emphasis applies. A Situation-domain MC has planetary emphasis in angular houses (their problem is externally visible and immediate). An Activity-domain MC has emphasis distributed across angular and succedent houses (their problem manifests through what they do and what resources they burn). A Fixed Attitude MC has cadent and succedent emphasis (their problem lives in background processing and internal valuation). A Psychology-domain MC distributes across all house types (their problem is in how they think, which touches every domain).

### Category 9: Planetary Dignities (Code Efficiency)

Dignities determine how efficiently each variable functions in its assigned sign and house.

**Essential Dignity (Domicile / Exaltation)**: The variable runs at full efficiency. The character is in their element for that specific function. The planetary energy and the sign energy reinforce each other.

**Essential Debility (Detriment / Fall)**: The variable glitches. The character struggles to execute that specific function correctly. The planetary energy and the sign energy work against each other.

**Dignity assignment rule:** Dignities are not randomly distributed. They are derived from the relationship between the Dramatica element assigned to that planet and the sign the planet occupies. When the Dramatica element and the sign's natural mode align (e.g., Mars in a cardinal fire sign for a Proaction-driven character), the planet receives dignity. When they conflict (e.g., Mars in a cardinal water sign for the same character), the planet receives debility. Debility is not a flaw — it is a specific behavioral texture. A debilitated Mars does not mean the character cannot act. It means the character acts in a way that is internally costly, emotionally volatile, or structurally inefficient. That texture feeds directly into L10 SHADOW and L5 WOUND in the 12-Layer system.

### Category 14: Void Variable (12th House)

The 12th House functions as the system's garbage collection folder.

**Variable:** `SYSTEM_RECURSION_LOG`

**Function:** Stores deleted memories, previous-state data, and the residue of transformations the character has undergone or will undergo. Any planet placed in the 12th House operates in a hidden, recursive mode — the character experiences its effects but cannot easily articulate or access them consciously.

**The Hauntology Effect:** When the character's Mercury (conscious processing) forms an aspect to a 12th House planet, they experience synthetic haunting — deja vu, recursive thought loops, the sensation that they have been in this situation before. This is a character-level configuration (it exists in the static chart) but its narrative expression is story-level (it activates at specific narrative moments).

**Assignment rule:** The 12th House receives planets whose Dramatica functions are submerged — elements the character carries but cannot access directly. The MC Problem element, if it operates beneath the character's awareness (as it does for most Change characters who do not recognize their Problem until late in the arc), is a strong candidate for 12th House placement or 12th House aspect.

---

## Story-Level Categories

The following categories are defined here for completeness and to establish their boundaries. They do not produce data for the Character Astrology Ingest Template. They are documented to prevent scope creep into the static character record.

### Category 6: Network Topology (Unicursal Hexagram)

Relationships are inter-process communications mapped onto the Unicursal Hexagram for energy flow tracking. This category defines the geometric model for relationship analysis. Data produced by this category enters **relationship tables** keyed to pairs of `character_id` values, not individual character records.

**Vertex mapping remains canonical:**

1. Top (Jupiter): Social status, growth
2. Upper Left (Saturn): Authority, duty, rules
3. Upper Right (Mars): Conflict, kinetic violence
4. Lower Left (Mercury): Logic, negotiation, code
5. Lower Right (Venus): Intimacy, value, desire
6. Bottom (Moon): Subconscious, private trauma

### Category 10: Lifecycle Protocol (The 6 Movements)

The 6 Movements define the macro-arc sequence of sequential erosion through systemic states. In the current implementation, the Movements are **centered on the MC** (Victoria Midnight for OVEREXITOUT). Other characters' arcs are measured by their temporal and narrative distance from the MC's movement position.

|Movement|Systemic State|Dominant Planet|Variable Condition|
|---|---|---|---|
|1. Delta Coast|Legibility|Mercury|High clarity, clean code|
|2. Year 1 School|Constraint|Saturn|Integration, systemic binding|
|3. Year 2 School|Decay|Neptune|Corruption, Moon override|
|4. Bourne|Awakening|Uranus|Framework perception|
|5. Fight Club|Resistance|Mars|Insurgency, reboot attempts|
|6. The Pacific|Collapse|Pluto|Exhaustion, total reset|

This category belongs to **plot_systems**. It references Character Astrology variables (dominant planets per movement) but does not modify the static chart.

### Category 11: Synastry Overlays (Network Mesh)

Synastry defines collision detection between two or more character charts. When Character A's planetary variable forms an aspect to Character B's planetary variable, the interaction produces a specific behavioral dynamic.

**Aspect Mesh:** Direct planet-to-planet contacts between two charts. Produces the raw collision data.

**Composite Chart:** A virtual third chart created by the midpoints of two characters' planetary positions. Represents the relationship itself as a separate entity with its own variable set.

Synastry data enters **relationship tables**, not character records. A relationship table row references two `character_id` values and contains the aspect mesh and composite chart data.

### Category 12: Progressions (Internal Clock)

Secondary Progressions represent the aging of the character's code over narrative time. They are state diffs, not chart modifications.

**Progressed Sun Change:** A fundamental shift in the character's `IDENTITY_AXIS`. Produces a state diff that modifies the effective Sun sign for a given narrative period.

**Progressed Lunar Cycle:** A 28-unit narrative arc tracking emotional maturation or decay. Produces a state diff that modifies the effective Moon condition.

Progression data enters the **character state overlay system** as diffs keyed to narrative time coordinates.

### Category 13: Transits (External Execution Commands)

Transits are pings from the current narrative environment to the character's static chart. They represent external events activating specific chart variables.

**Saturn Return:** A mandatory system audit occurring at major narrative milestones.

**Mars Transit:** A temporary spike in kinetic conflict.

**Outer Planet Transits:** Trigger the shift between the 6 Movements.

Transit data enters the **character state overlay system** as diffs keyed to narrative time coordinates. The static chart defines which variables are vulnerable to which transits. The plot_systems domain defines when those transits fire.

### Category 15: Reset Protocol (Systemic Wipe)

At the conclusion of Movement 6, the system executes a terminal reset. This category defines what survives the wipe (stored in the 12th House / Void Variable), how the character is re-acquired in Movement 1 of the next cycle, and what percentage of entropy remains as the ghost signal enabling future awakening.

This category belongs entirely to **plot_systems**. It references the static chart (specifically the 12th House contents) to determine data persistence, but it does not modify the chart.

---

## The Dramatica-Astrology Interface (DAI)

The DAI is the translation layer between Dramatica outputs and Character Astrology inputs. It is the API specification that governs how narrative positions convert to astrological configurations.

The DAI is summarized here and expanded in full in **deliverable 2B: DAI Expansion**.

### Summary Table

|Dramatica Input|Astrological Output|Derivation Logic|
|---|---|---|
|MC Domain + MC Concern|**Sun Sign**|The domain-concern intersection defines the character's identity axis. The sign that best encodes this intersection is assigned.|
|MC Problem + MC Response|**Moon Sign**|The problem-response pair defines the stress-collapse pattern. The sign that best encodes this instinctual default is assigned.|
|Unique Ability + Methodology Quad|**Mercury Configuration**|How the character processes information and what gives them an edge in doing so.|
|MC Concern + Purpose Quad|**Venus Configuration**|What the character values and what they pursue as meaningful.|
|Approach + Motivation Quad|**Mars Configuration**|How the character acts and what drives them to act.|
|MC Unique Ability|**Jupiter Placement**|Where the character finds expansion, permission, and temporary safety.|
|MC Critical Flaw + Inhibitor|**Saturn Placement**|The hard-coded limit. The wall that cannot be bypassed without transformation.|
|MC Solution|**Uranus Configuration**|The disruption that is actually the answer. Initially experienced as threat.|
|MC Symptom|**Neptune Configuration**|The false signal. The illusion the character chases instead of facing the real problem.|
|Story Outcome + Story Judgment|**Pluto Configuration**|The terminal condition. How the argument ends and what that ending means.|
|Approach + MC Critical Flaw|**Ascendant**|The visible interface, including its exploit vector.|
|Story Goal + Character's OS Role|**Midheaven**|The public output. What the character achieves or fails to achieve in the world's eyes.|
|MC Direction|**Descendant**|What the character seeks in others. The shadow complement.|
|MC Benchmark|**IC**|The hidden measurement standard. The buried origin metric.|

Each row in this table expands to a full derivation rule in the DAI Expansion document.

---

## Pipeline Position

```
┌─────────────────────┐
│   DRAMATICA INGEST   │
│   TEMPLATE [LOCKED]  │
└────────┬────────────┘
         │
         ▼
┌─────────────────────────────────┐
│   DRAMATICA-ASTROLOGY INTERFACE │
│   (DAI Translation Rules)       │
│   [Deliverable 2B]              │
└────────┬────────────────────────┘
         │
         ▼
┌─────────────────────────────────┐
│   CHARACTER ASTROLOGY            │
│   INGEST TEMPLATE [LOCKED]       │
│   [Deliverable 2C]              │
│                                  │
│   Contains:                      │
│   - Sun, Moon, Mercury,          │
│     Venus, Mars (Personal Stack) │
│   - Jupiter, Saturn, Uranus,     │
│     Neptune, Pluto (Structural)  │
│   - Ascendant, MC, Desc, IC     │
│   - Aspects (Logic Gates)        │
│   - House Placements             │
│   - Dignities                    │
│   - 12th House / Void Contents   │
└────────┬────────────────────────┘
         │
         ▼
┌─────────────────────────────────┐
│   12-LAYER VERTICAL SLICE        │
│   (Feeds L7-L11 via             │
│    Astrology-to-Layer Mapping)   │
│   [Deliverable 3A]              │
└─────────────────────────────────┘
```

Character Astrology sits in the middle of the pipeline. It consumes Dramatica. It is consumed by the 12-Layer system. It does not operate independently of either.

---

## Relationship to the 12-Layer Character Database

Character Astrology and the 12-Layer system are **parallel datasets** that describe the same character in different notation systems. They are not hierarchical — neither contains the other. They share a common upstream source (Dramatica) and are connected by a formal mapping (deliverable 3A).

**What Character Astrology provides that the 12-Layer system does not:**

- A symbolic vocabulary for encoding psychological complexity that generates depth beyond numeric values.
- Internal contradiction logic (aspects) that produces behavioral texture not capturable by single-axis numeric scales.
- Cross-character collision detection (synastry) that predicts relationship dynamics from chart comparison alone.
- A mature notation system with centuries of interpretive literature that can be leveraged for character development beyond what the 12-Layer schema defines.

**What the 12-Layer system provides that Character Astrology does not:**

- Numeric values suitable for database queries, derived statistics, and flag trigger computation.
- A tiered complexity model that scales from background characters to deep protagonists.
- Machine-readable structured data blocks suitable for ingestion into hard-coded database infrastructure.
- Derived statistics (Stress Threshold, Collapse Risk, Truth Exposure Index) that produce actionable diagnostic outputs.

**The connection:** Specific astrological variables feed specific layers. Sun sign feeds L1 CORE justification. Moon sign feeds L8 IMPRINT. Venus feeds L9 EROS. Mars feeds L2 VITAL. Saturn feeds L4 WILL and L5 WOUND. Shadow-related aspects feed L10 SHADOW. Destiny-related configurations (North Node, growth axis) feed L11 DESTINY. The complete mapping is defined in deliverable 3A.

The two systems coexist. A complete Tier 3 character has both a Character Astrology Ingest Template and a 12-Layer Vertical Slice in their canonical folder. Both are valid, complete representations. Neither replaces the other.

---

## Version History

|Version|Date|Changes|
|---|---|---|
|1.0.0|2026-03-03|Initial SSOT. Renamed from Narrative Astrology to Character Astrology. Relocated to 02_CHARACTER_SYSTEMS. Separated 15 categories into character-level (9 categories) and story-level (6 categories). Established narrative-first policy. Defined pipeline position and relationship to 12-Layer system. Supersedes both prior Narrative Astrology documents.|