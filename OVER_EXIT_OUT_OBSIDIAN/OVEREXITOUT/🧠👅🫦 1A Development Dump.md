## 1. Characters (The Canonical Identity)
| Field | Type | Note |
| :--- | :--- | :--- |
| character_id | PK | Unique ID |
| status_id | FK | Spec / Locked / Final |
| role_id | FK | Protagonist / Asset / etc. |
| first_name | String | "Doug" |
| last_name | String | "Yamato" |
| primary_alias_id | FK | Links to the "Full Display" nickname |

## 2. Aliases (The Name Library)
| Field | Type | Note |
| :--- | :--- | :--- |
| alias_id | PK | Unique ID |
| character_id | FK | Owner of the name |
| alias_text | String | "Black Nikker Wiskey Drinker" |
| is_canonical | Bool | Used for the "Full Display Name" |
| alias_type | Enum | Legal / Moniker / Codename |

## 3. AliasUsage (The Social Logic)
| Field       | Type | Note                                    |
| :---------- | :--- | :-------------------------------------- |
| usage_id    | PK   | Unique ID                               |
| alias_id    | FK   | Link to Alias table                     |
| speaker_id  | FK   | Who says it (Daughter, Manager, System) |
| context_id  | FK   | Home / Field / Noir / Resistance        |
| valence_id  | FK   | Affectionate / Hostile / Ironic         |
| power_state | Enum | Up / Down / Equal                       |


# 📂 THE CHARACTER ENGINE PILE: PROTO-SSOT MINE

## 1. ATOMIC VARIABLE DICTIONARY (THE HARDWARE)

_These are the primary "sockets" found across the GURPS-Logic and Astrology modules._

|Symbol|System Name|Logic Layer|Function|
|---|---|---|---|
|**P**|Potency|Layer 3/4|Raw output capability / Force projection.|
|**I**|Integrity|Layer 0/3|Structural stability vs. Systemic Decay.|
|**S**|Synchronization|Layer 2|Alignment with Factional Ghost-Code (Montgomery/Bishop).|
|**SUN**|Identity Axis|Layer 0|The ego, will, and core drive; what the character _believes_ they are.|
|**MOON**|Need Core|Layer 3|Emotional triggers, damage, and subconscious instinct.|
|**BAS_**|Base Invariant|Layer 0|Immutable truths (e.g., `BAS_CHR_Astrology`).|
|**VAR_**|Variable State|Layer 4|Evolving states (e.g., `VAR_FAC_InfluenceLevel`).|

Export to Sheets

---

## 2. SYSTEMIC INVARIANT STACK (THE KERNEL)

_The non-negotiable laws of the simulation extracted from Layered Invariants._

- **Layer 0 (Ontology):** Only enacted outcomes exist. Intent has zero weight.
    
- **Layer 1 (Meaning):** Sincerity is ignored. The system rewards inputs/actions only.
    
- **Layer 2 (Force):** Truth does not pause enforcement. Power is outsourced/delegated.
    
- **Layer 3 (Interface):** Dissociation and ritualization as survival coping mechanisms.
    
- **Layer 4 (Expression):** The **Move Set**: `Commit`, `Refuse`, `Reveal`, `Delay`, `Escalate`, `Isolate`, `Transfer Risk`, `Close`.
    
- **Layer 5 (Argument):** Repetition proves the claim (e.g., Systems overpower individuals).
    
- **Layer 6 (Terminal):** Resolution codes: `L6.2 Attrition`, `L6.3 Exhaustion`, `L6.7 Collapse`.
    

---

## 3. DATABASE SCHEMA & ERD MAPPINGS

_Technical table structures found in the deep-dredge (SQL/Postgres logic)._

### Table Class: Meta (The Grammar)

- `domains`: High-level groupings (Identity, Emotional, Cognitive).
    
- `subsystems`: Specific logic modules.
    
- `atomic_variable_def`: Definitions of sockets (e.g., `SUN_EGO_STYLE`).
    
- `overlay_model`: Psychology packs (Big Five, Enneagram, Attachment).
    

### Table Class: Instance (The Sentences)

- `characters`: The unique ID record for an entity.
    
- `charts`: The timestamped "snapshot" (Birth/Booting chart).
    
- `atomic_value`: The final narrative-ready text (e.g., "Anxious Clinger").
    
- `overlay_model_profile`: The specific scores for a character.
    

---

## 4. THE ATTRIBUTE TAXONOMY (THE YAML SCHEMA)

_The 8 dimensions of a character extracted from the Narrative Chemistry Engine._

1. **Physical:** `BAS_CHR_SexualAttributes`, Anatomy.
    
2. **Psychological:** Fear_Wound, Lie_They_Believe (The "Wound").
    
3. **Social:** Alias_ID, Valence (+/-), Faction_Owner.
    
4. **Motivational:** Want vs. Need, True North vs. Yearning.
    
5. **Cognitive:** Behavioral Surface, Mental Profile.
    
6. **Behavioral:** Methodology, Pressure Response.
    
7. **Narrative:** Archetypal Role, Proppian Function.
    
8. **Metafictional:** Ontological Status (Diegetic vs. Meta).
    

---

## 5. TRANSITION LOGIC GATES (THE PHYSICS)

_The "If/Then" mechanics found in the research notes._

- **Booting Sequence:** `Input(Birth_Chart + Faction_ID) -> Init($P, $I, $S)`.
    
- **Awakening Trigger:** `If State = Layer 4 AND $I < 0.5 THEN $S flips to -1.0 (Resistance)`.
    
- **The Attrition Loop:** `Pressure -> Choice -> Cost`. Every choice must reduce I or S.
    
- **Conflict Resolution:** Relies on **Aspect Logic Gates** (Computational Conflict) rather than dialogue.
    

---



- **Systemic Core Philosophy:** The meta-rules governing character rendering.
    
- **The Dramatica-Astrology Interface (DAI):** The bridge (Logic Gate) between story structure and character variables.
    
- **Atomic Variables (Personal):** The "Hardware" stack (Sun, Moon, etc.).
    
- **Atomic Variables (Structural):** The "Limit" stack (Saturn, Pluto, etc.).
    
- **The Interface Layer (Angles):** The specific relationship of the character to the world (ASC,MC).
    
- **Network Topology (Unicursal Hexagram):** The flow of conflict between characters (Group IPC).
    
- **Aspect Logic Gates:** Computational conflict (e.g., Square = XOR, Trine = OR).
    
- **House Systems:** Environmental and situational context.
    
- **Planetary Dignities:** Code efficiency (how well a character functions in a specific environment).
    
- **The Lifecycle Protocol:** The 6-Movement alignment (Outliers sequence).
    
- **Transits:** Real-time systemic pressure on the character.
    
- **Progressions:** The internal evolution of the code over time.
    
- **Synastry Logic:** Direct character-to-character variable interference.
    
- **The Void (12th House):** Data loss, isolation, and systemic erasure.
    
- **Output / Rendering:** The final "compiled" character sheet/manifest.


---

### 🧠 The "Physicality & Goon-Noir" Module

This module serves as the **Hardware Interface** for your characters. It determines how they are "worn," "broken," and "synced" to the world.

#### 1. The "X:1 System" (Erotic Anatomy Library)

You have a standardized library for character design that moves beyond prose into **Parametric Design**.

- **The Rule:** Strict **x:1 selection**. One attribute per category to ensure a "strong sexual identity."
    
- **Core Categories Found:**
    
    - `Stimulus Mode` (Visual magnetism, Kinetic lust, Worship trigger).
        
    - `Silhouette` (Objectification architecture).
        
    - `Chest/Hip/Ass Profile` (Hardware specific metrics).
        
    - `Ruin Trigger` (The specific condition that breaks the Asset's physical/mental sync).
        

#### 2. The `sexual_presence` Database Schema

This is a literal SQL table structure found in your `JUST TABLES` directory. It treats eroticism as **Power Projection**.

- **Fields extracted:** `erotic_archetype`, `arousal_reaction`, `fetishized_features`, `kink_triggers`.
    
- **The "MODS" Case Study:** Shows how the engine handles "Anti-erotic" profiles (Cold bureaucratic tone, libido as spam alerts). This proves your system can handle non-sexual entities using the same schema.
    

#### 3. Ritualized Compliance (The "Goon-Noir" Mechanics)

This is where your **Layer 2 (Force)** and **Layer 3 (Interface)** invariants manifest.

- **The "Denial & Punishment" Framework:** A literal protocol for "Erotic Discipline." It uses triggers like "Accidental Orgasm" or "Skipped Segment" to force "Punishment Sessions."
    
- **System Analog:** This isn't just story; it's a **State Machine**. Failure to follow protocol leads to a **48-hour Forbidden State**.
    
- **Movement 3 Vibe:** Confirmed as "Transgressive Decay" where sexuality and "V-Sync" (Biometric Syncing) are the primary tools of control.
    

---

### 🛠️ The "Physicality" Proto-SSOT (Copy/Paste Pile)



#### **A. The Erotic Hardware Stack (X:1 System)**

|**Category**|**Options (Selected Examples)**|
|---|---|
|**Stimulus Mode**|Visual Magnetism, Kinetic Lust, Worship Trigger, Corruption Drive.|
|**Aesthetic Coding**|Cyberbimbo, Corporate Courtesan, Nun, Dollcore, Latex Domme.|
|**Vocal Cues**|Robotic Flatness, Silk-voiced, Mocking Lilt, Husky.|
|**Scent Profile**|Burnt Sugar + Copper, Cardamom, Sterile Ozone, Holy Incense.|

#### **B. The Control Logic (Logic Gates)**

- **V-Sync Logic:** Students are kept in over-stimulation trances to harvest data.
    
- **The KLK Invariant:** "Power is worn on the body." Less clothing = higher biometric transparency.
    
- **Intimacy as Data-Splicing:** Sex is treated as a "Neural Hack" or "Pleasure Virus" (e.g., _Glitchpriests_).
    
- **The Denial Loop:** `Failure -> Denial Period -> Punishment Protocol -> Re-Sync`.
    

#### **C. SQL Reference: `sexual_presence`**

SQL

```
-- Schema for the Biometric Control Layer
CREATE TABLE sexual_presence (
    character_id INTEGER PRIMARY KEY,
    charisma_score INTEGER, -- GURPS scale
    erotic_archetype TEXT, -- (e.g., Bratty Sub, High Priestess)
    kink_triggers TEXT, -- (e.g., Mirrors, Cameras, Red Lighting)
    sync_rate_modifier FLOAT -- Derived from arousal reaction
);
```

---


---

# 📘 Technical Specification: Simulation & Visual Engine

## 1. The Simulation Kernel (GOON BUILD 0.0)

The core engine is a modular, **tick-based** generator designed for causal consistency and symbolic layering.

- **Tick Engine:** Advances time in configurable units; every tick calculates event queues and domain updates.
    
- **Logic Core (GURPS):** Resolves all agent behaviors using stat blocks, skills, and advantages/disadvantages.
    
- **Forkable Timelines:** Supports branching history and "save-state" re-simulation for alternate narrative outcomes.
    
- **Traceability:** Every event includes a source tick, actor ID, and causal link to ensure narrative integrity.
    

## 2. Character Mechanics & Sheets

Characters are "Compiled Entities" defined by atomic variables and pluggable overlays.

- **Lore Space → Turn Space:** A "compiler" projects high-dimensional data (Big Five, Enneagram, Astrology) into low-dimensional mechanical stats (Prowess, Mojo, Nerves).
    
- **Overlay Models:** Psychological "packs" (OCEAN, Attachment Theory) plug into sockets like `SUN_IDENTITY_AXIS`.
    
- **The Sheet:** Output is structured in **YAML/JSON**, compatible with SQLite and Godot for live simulation.
    

## 3. The KLK Framework (Fashion as Hardware)

You have codified aesthetics into the **Systemic State Theory**.

- **Star-Rating Code:** A literal rank display displayed on uniforms.
    
- **Feed-Linked Clothing:** Uniforms are interfaces; "Clothing = Rank" and "Skin = Biometric Transparency."
    
- **Desync Triggers:** Dress code violations are not social faux pas; they are **Integrity (I) failures** that trigger administrative intervention.
    

## 4. Cinematic Proceduralism (The Fincher Protocol)

The visual layer is governed by rigid, axis-bound movement to simulate "Constraint."

- **Robotic Panning:** Mathematical camera movement restricted to X/Y axes.
    
- **The Palette:** Specific color-coding for systemic states (e.g., **Jaundice Yellow** for the Academy's decay).
    
- **Axis-Bound Framing:** Every shot is a "test of invariants"—does the composition reflect the world's gravity and law?
    

---

## 🏗️ Systemic Invariants (Technical Manifest)

|Component|Logic Gate|Operational Function|
|---|---|---|
|**GURPS_CORE**|`Stat + Skill vs TN`|Behavioral resolution and outcome math.|
|**NCP_SCHEMA**|`Dramatica + JSON`|Machine-readable story structure and revision log.|
|**PSTO_DOCTRINE**|`Policy -> Ops`|Governance layer for decision consistency.|
|**ASCD_SKIN**|`Ascendant = UI`|The visible "skin" or aesthetic layer of the asset.|
|**TICK_ENGINE**|`Queue -> Resolve`|Lifecycle management of agents and civilizations.|

---