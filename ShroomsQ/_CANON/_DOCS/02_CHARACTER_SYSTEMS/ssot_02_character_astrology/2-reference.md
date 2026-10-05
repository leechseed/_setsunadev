---
title: "Character astrology: reference"
type: reference
for: "A writer or builder looking up what a Character Astrology category, planet, angle or rule means"
does: "Lists every component and part of the Character Astrology doc with its fields, rules and connections"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/02_CHARACTER_SYSTEMS/📐 ssot_02_character_astrology.md
source_version: 1.1.1
---

**Who it's for:** a writer or builder looking up a category, planet, angle or rule · **What it does:** lists every component of the Character Astrology doc · **Type:** reference

# Character astrology: reference

Why the system exists: [concept](1-concept.md). Steps: [how-to](3-how-to.md). A worked chart: [tutorial](4-tutorial.md). Source: [ssot_02_character_astrology.md](../../../_SSOT/02_CHARACTER_SYSTEMS/📐%20ssot_02_character_astrology.md), version 1.1.1.

Machine names appear in code font. Each planet or angle lists its function name, then the Dramatica input it derives from.

## What Character Astrology Is

A **notation system**. It takes narrative truths set by Dramatica and encodes them as planets, signs, houses, aspects and dignities. The output is a second representation of the same character data.

- **The Chart:** the character's source code. A structured symbolic dataset derived from locked narrative positions.
- **The Character:** the compiled entity. The behavior that appears when chart variables interact under story conditions.
- **The Story:** the execution environment. External conditions that activate, suppress or transform chart variables.

Rule: every behavior traces to a variable configuration. A behavior that cannot be traced means the chart is incomplete.

## What Character Astrology Is Not

- It does not produce narrative structure. Dramatica owns that.
- It does not assign numbers to character layers. The 12-layer system owns that.
- It does not generate plot events, scenes or timelines. Plot systems own those.
- It is a translation layer, not a destination.
- It is not traditional astrology applied to fiction. Every assignment is justified by a locked Dramatica position.

## The Narrative-First Policy

Governing principle: Dramatica defines the narrative truth, and the chart serves the story.

| # | Rule |
|---|---|
| 1 | No variable is assigned without a Dramatica justification. |
| 2 | When astrology contradicts locked Dramatica data, Dramatica governs. The writer revises the astrological assignment. |
| 3 | Chart generation follows the fixed derivation sequence in the DAI doc. No step is skipped or reordered. |
| 4 | A partial chart is enough for L1-L11: Sun, Moon, Mercury, Venus, Mars, Saturn, Ascendant. Outer planets, progressions and transits come later. |
| 5 | Tier 3 gets a full chart. Tier 2 gets a partial chart (Sun, Moon, one or two defining aspects) from its element signature. Tier 1 gets none. |

Connects to: [DAI doc](../ssot_02_character_astrology_dai/2-reference.md).

## Domain Classification

The 15 categories stay valid. The test: data about who the character IS at canonical definition is character-level. Data about what is HAPPENING to the character at a narrative moment is story-level. The static character record never changes. Progressions and transits make state diffs. Synastry makes relationship records. Movements make story-structure records keyed to the main character.

### Character-Level Categories (Static Chart)

Data enters the Character Astrology Ingest Template and feeds the 12-layer slice.

| # | Category | Domain | Function |
|---|---|---|---|
| 1 | Systemic Core Philosophy | Meta | Governing principles. A design philosophy, not a data category. |
| 2 | Dramatica-Astrology Interface (DAI) | Interface | Translation rules from Dramatica to astrological variables. |
| 3 | Personal Stack (Inner Planets) | Character | Sun, Moon, Mercury, Venus, Mars. |
| 4 | Structural Stack (Outer Planets) | Character | Jupiter, Saturn, Uranus, Neptune, Pluto. |
| 5 | Interface Layer (Angles) | Character | Ascendant, Midheaven, Descendant, IC. |
| 7 | Aspect Logic Gates | Character | Geometric relationships between planets. |
| 8 | House Systems | Character | Environmental directories where planets act. |
| 9 | Planetary Dignities | Character | Efficiency ratings for each variable. |
| 14 | Void Variable (12th House) | Character | The system recursion log. |

The classification table lists category 2 under character-level. The "Character-Level Categories" section below does not give it a subsection. The DAI doc holds its rules.

### Story-Level Categories (State Overlays / Relationship / Plot)

Data does NOT enter the static record.

| # | Category | Domain | Destination |
|---|---|---|---|
| 6 | Network Topology (Unicursal Hexagram) | Relationship | Relationship tracking tables |
| 10 | Lifecycle Protocol (6 Movements) | Story Structure | Plot systems |
| 11 | Synastry Overlays | Relationship | Relationship tables |
| 12 | Progressions (Internal Clock) | State Overlay | Character state diff system |
| 13 | Transits (External Commands) | State Overlay | Character state diff system |
| 15 | Reset Protocol (Systemic Wipe) | Story Structure | Plot systems |

## Character-Level Categories

### Category 1: Systemic Core Philosophy

Characters are deterministic entities defined by variables and logic gates. The chart is the source code from which behavior compiles. This category produces no data. It is the principle all other categories serve.

### Category 3: Personal Stack (The Hardware)

The inner planets are the functional processing units that produce moment-to-moment behavior.

| Planet | Function name | Role | Derived from |
|---|---|---|---|
| Sun | `IDENTITY_AXIS` | The central processor. What the character believes they are. Generates the thematic question. | MC Domain and MC Concern |
| Moon | `INTERNAL_STATE` | Instinctual default and subconscious memory. Logic collapses into it under stress. | MC Problem and MC Response |
| Mercury | `CODE_INTERPRETATION` | The logic gate. Speech, tactical navigation, comprehension. | Unique Ability and Methodology quad |
| Venus | `VALUE_VECTOR` | The priority sensor. What the character tries to acquire. | MC Concern and Purpose quad |
| Mars | `ACTION_PROTOCOL` | The execution command. Aggression, kinetic movement, sexual energy, physical will. | Approach (Do-er/Be-er) and Motivation quad |

### Category 4: Structural Stack (The Limit)

The outer planets are the systemic environment, historical forces and boundary conditions.

| Planet | Function name | Role | Derived from |
|---|---|---|---|
| Jupiter | `REDUNDANCY` | The system's permission for growth. Temporary safety, resource spikes. | MC Unique Ability |
| Saturn | `ENTROPY_LIMITER` | The boundary variable. Rules, antagonist principle, constraint. | MC Critical Flaw and Inhibitor |
| Uranus | `BREACH_PROTOCOL` | Sudden shifts in code. The awakening that disrupts the loop. | MC Solution |
| Neptune | `HAUNT_SIGNAL` | Glitches, illusions, synthetic hauntings. | MC Symptom |
| Pluto | `TERMINATION_CODE` | The ultimate reset. Power dynamics ending in exhaustion. | Story Outcome and Story Judgment |

### Category 5: Interface Layer (The Angles)

The angles define how the character is rendered and recorded in the narrative world.

| Angle | Function name | Role | Derived from |
|---|---|---|---|
| Ascendant | `CHARACTER_UI_SKIN` | First-response style. The visible mask, with its exploit vector. | Approach and MC Critical Flaw |
| Midheaven | `CHARACTER_OUTPUT_LOG` | Public legacy. The output as the world records it. | Story Goal and the character's relation to it |
| Descendant | `CHARACTER_SHADOW_INTERFACE` | What the character lacks and seeks in others. Inverse of the Ascendant. | MC Direction |
| IC | `CHARACTER_ROOT_ORIGIN` | Private origin and hidden trauma foundation. | MC Benchmark and Origin layer data |

### Category 7: Aspect Logic Gates

Aspects are logic gates that define internal friction and flow.

| Aspect | Gate | Effect |
|---|---|---|
| Conjunction | AND | Two variables fuse and run together. Intensity, singular purpose. |
| Square | NOT | Variable A blocks B. Friction forces a state change and drives turning points. |
| Opposition | XOR | A binary choice. The character cannot run both. Either/or dilemmas. |
| Trine | OR | Data flows freely. Natural ability that can lead to stagnation. |
| Sextile | OR | Data flows when the character acts on it. A talent that takes effort, so it does not stagnate. |

Assignment rule: aspects come from tension inside the Dramatica quads.

- Elements in natural tension (e.g. Equity and Inequity as Problem/Solution) give a hard aspect: Square or Opposition.
- Elements that flow give a soft aspect: Trine or Sextile.
- Conjunctions are reserved for two Dramatica functions that fuse in the character.

### Category 8: House Systems (Environmental Context)

Houses are the directories where planetary action operates.

| House group | Houses | Meaning |
|---|---|---|
| Angular | 1, 4, 7, 10 | High-priority execution. Visible, immediate, shifts the narrative. |
| Succedent | 2, 5, 8, 11 | Resource management. Maintenance, assets, value exchange. |
| Cadent | 3, 6, 9, 12 | Background processing. Communication, preparation, belief, ghost-code. |

Assignment rule: the MC Domain sets the emphasis.

| MC Domain | Emphasis |
|---|---|
| Situation | Angular houses (the problem is externally visible). |
| Activity | Angular and succedent (the problem shows in what the character does and burns). |
| Fixed Attitude | Cadent and succedent (the problem lives in background processing and valuation). |
| Psychology | All house types (the problem is in how the character thinks). |

### Category 9: Planetary Dignities (Code Efficiency)

- **Essential Dignity** (Domicile, Exaltation): the variable runs at full efficiency.
- **Essential Debility** (Detriment, Fall): the variable glitches. The planet and sign work against each other.

Assignment rule: compare the Dramatica element on the planet with the sign's natural mode. Alignment gives dignity. Conflict gives debility. Source example: Mars in a cardinal fire sign for a Proaction-driven character is dignified. Mars in a cardinal water sign is debilitated.

Debility is a behavioral texture, not a flaw. A debilitated Mars acts at internal cost. The texture feeds L10 SHADOW and L5 WOUND.

### Category 14: Void Variable (12th House)

The 12th House is the system's garbage collection folder.

- **Variable:** `SYSTEM_RECURSION_LOG`.
- **Function:** stores deleted memories, previous-state data and residue of transformations. A planet here operates in hidden, recursive mode.
- **Hauntology Effect:** when Mercury aspects a 12th House planet, the character feels deja vu and recursive thought loops. The configuration is static. Its expression is story-level.
- **Assignment rule:** the 12th House receives planets whose Dramatica functions are submerged. A MC Problem the character cannot see is a strong candidate.

## Story-Level Categories

Defined for completeness and to prevent scope creep into the static record. None feeds the Character Astrology Ingest Template.

### Category 6: Network Topology (Unicursal Hexagram)

Relationships are inter-process communications mapped onto the hexagram. Data enters relationship tables keyed to pairs of `character_id` values.

| Vertex | Planet | Meaning |
|---|---|---|
| Top | Jupiter | Social status, growth |
| Upper Left | Saturn | Authority, duty, rules |
| Upper Right | Mars | Conflict, kinetic violence |
| Lower Left | Mercury | Logic, negotiation, code |
| Lower Right | Venus | Intimacy, value, desire |
| Bottom | Moon | Subconscious, private trauma |

### Category 10: Lifecycle Protocol (The 6 Movements)

The macro-arc of sequential erosion. Centered on the MC (Victoria Midnight for OVEREXITOUT). Other characters are measured by distance from the MC's position. Belongs to plot systems. It reads chart variables and does not change the chart.

| Movement | Systemic state | Dominant planet | Condition |
|---|---|---|---|
| 1. Delta Coast | Legibility | Mercury | High clarity, clean code |
| 2. Year 1 School | Constraint | Saturn | Integration, systemic binding |
| 3. Year 2 School | Decay | Neptune | Corruption, Moon override |
| 4. Bourne | Awakening | Uranus | Framework perception |
| 5. Fight Club | Resistance | Mars | Insurgency, reboot attempts |
| 6. The Pacific | Collapse | Pluto | Exhaustion, total reset |

### Category 11: Synastry Overlays (Network Mesh)

Collision detection between charts. Data enters relationship tables. A row references two `character_id` values.

- **Aspect Mesh:** direct planet-to-planet contacts between two charts. The raw collision data.
- **Composite Chart:** a virtual third chart from the midpoints of two characters' planets. It represents the relationship as its own entity.

### Category 12: Progressions (Internal Clock)

Secondary Progressions age the character's code over narrative time. They are state diffs, not chart edits. Data enters the character state overlay system, keyed to narrative time coordinates.

- **Progressed Sun Change:** a shift in `IDENTITY_AXIS`. A state diff changes the effective Sun sign for a period.
- **Progressed Lunar Cycle:** a 28-unit arc of emotional maturation or decay. A state diff changes the effective Moon condition.

### Category 13: Transits (External Execution Commands)

Pings from the narrative environment to the static chart. Data enters the state overlay system as diffs. The static chart says which variables are vulnerable. Plot systems say when transits fire.

- **Saturn Return:** a mandatory system audit at major milestones.
- **Mars Transit:** a temporary spike in kinetic conflict.
- **Outer Planet Transits:** trigger the shift between the 6 Movements.

### Category 15: Reset Protocol (Systemic Wipe)

At the end of Movement 6 the system executes a terminal reset. The category defines what survives (stored in the 12th House). It also defines how the character is re-acquired in Movement 1 of the next cycle. It also defines what share of entropy remains as the ghost signal. It belongs entirely to plot systems. It reads the 12th House contents and does not change the chart.

## The Dramatica-Astrology Interface (DAI)

The DAI is the translation layer between Dramatica outputs and chart inputs. It is the API specification for converting narrative positions to astrological configurations. The full rules are in deliverable 2B, [ssot_02_character_astrology_dai.md](../../../_SSOT/02_CHARACTER_SYSTEMS/🔮ssot_02_character_astrology_dai.md).

### Where the rules live

The DAI doc holds the full table: each Dramatica input, the planet or angle it sets, and the derivation rule. This doc does not repeat the table, so the two cannot drift apart.

## Pipeline Position

The chain, in order:

1. Dramatica Ingest Template [LOCKED].
2. Dramatica-Astrology Interface, DAI translation rules (deliverable 2B).
3. Character Astrology Ingest Template [LOCKED] (deliverable 2C). It holds the five personal planets, the five structural planets and the four angles. It also holds aspects, house placements, dignities and 12th House contents.
4. LEECHSEED Vertical Slice, which receives L1-L11 through the astrology-to-layer mapping (deliverable 3A).

The chart consumes Dramatica and is consumed by the 12-layer system. It does not work independently of either.

## Relationship to the LEECHSEED Character System

The two systems are parallel datasets in different notations. Neither contains the other. They share Dramatica upstream and connect through the formal mapping (3A).

| The chart provides | The 12-layer system provides |
|---|---|
| Symbolic vocabulary for psychological complexity | Numeric values for queries, derived statistics, flag triggers |
| Internal contradiction logic (aspects) | A tiered complexity model from background to protagonist |
| Cross-character collision detection (synastry) | Machine-readable structured data blocks |
| A mature notation with a long interpretive literature | Derived statistics: Stress Threshold, Collapse Risk, Truth Exposure Index |

Specific feeds named in the source:

- Sun feeds L1 CORE justification.
- Moon feeds L8 IMPRINT.
- Venus feeds L9 EROS.
- Mars feeds L2 VITAL.
- Saturn feeds L4 WILL and L5 WOUND.
- Shadow-related aspects feed L10 SHADOW.
- Destiny-related configurations (North Node, growth axis) feed L11 DESTINY.

Not chart-fed: the twelve fields added in schema 2.5.0 and the 3.0.0 additions. Authors set them from the authoritative document. Per-field notes are in the schema-pass table of [ssot_02_character_astrology_12_layer_mapping.md](../../../_SSOT/02_CHARACTER_SYSTEMS/🔮ssot_02_character_astrology_12_layer_mapping.md).

A complete Tier 3 character holds two records in the canonical folder. One is a Character Astrology Ingest Template. The other is a LEECHSEED Vertical Slice. Blank form: [astrology ingest template reference](../ssot_02_template_astrology_ingest/2-reference.md).
