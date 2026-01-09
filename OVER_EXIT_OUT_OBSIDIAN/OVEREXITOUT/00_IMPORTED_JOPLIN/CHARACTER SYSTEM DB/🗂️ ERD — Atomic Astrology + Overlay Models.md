---
title: 🗂️ ERD — Atomic Astrology + Overlay Models
updated: 2025-12-03 18:00:01Z
created: 2025-12-03 18:00:00Z
latitude: 30.43825590
longitude: -84.28073290
altitude: 0.0000
---

# 🗂️ ERD — Atomic Astrology + Overlay Models

---

## 📑 Table of Contents

1. [Design Overview](#1-design-overview)
2. [Core Entities — Characters & Charts](#2-core-entities--characters--charts)  
   - [2.1 CHARACTER](#21-character)  
   - [2.2 CHART](#22-chart)
3. [Astro Schema — Domains, Subsystems, Atomic Variables](#3-astro-schema--domains-subsystems-atomic-variables)  
   - [3.1 DOMAIN](#31-domain)  
   - [3.2 SUBSYSTEM](#32-subsystem)  
   - [3.3 ATOMIC_VARIABLE_DEF](#33-atomic_variable_def)  
   - [3.4 ATOMIC_VALUE](#34-atomic_value)
4. [Overlay Models — Types, Dimensions, Profiles](#4-overlay-models--types-dimensions-profiles)  
   - [4.1 OVERLAY_MODEL](#41-overlay_model)  
   - [4.2 OVERLAY_MODEL_DIMENSION](#42-overlay_model_dimension)  
   - [4.3 OVERLAY_MODEL_PROFILE](#43-overlay_model_profile)  
   - [4.4 OVERLAY_MODEL_DIMENSION_VALUE](#44-overlay_model_dimension_value)
5. [Linking Atomic Variables to Overlay Models](#5-linking-atomic-variables-to-overlay-models)  
   - [5.1 ATOMIC_VARIABLE_OVERLAY](#51-atomic_variable_overlay)
6. [ER Diagram (Mermaid)](#6-er-diagram-mermaid)
7. [Usage Pattern](#7-usage-pattern)

---

## 1. Design Overview

Goal: **store astrology-based atomic variables** for a character and then **deepen** them using reusable **overlay models** (Big Five, Enneagram, Attachment, Shadow, etc.).

High level:

- A **CHARACTER** has one or more **CHARTS**.
- Each CHART has a set of **ATOMIC_VALUE** records (e.g. `SUN_IDENTITY_AXIS`, `MOON_NEED_CORE`, etc.), defined in **ATOMIC_VARIABLE_DEF**.
- **DOMAIN** and **SUBSYSTEM** group the atomic variables (Identity, Emotional, Cognitive, etc.).
- **OVERLAY_MODEL** (Big Five, Enneagram, Attachment, etc.) has **dimensions** (traits / sliders).
- For each CHARACTER+MODEL, an **OVERLAY_MODEL_PROFILE** stores **dimension values**.
- **ATOMIC_VARIABLE_OVERLAY** maps which overlay models are attached to which atomic variables (e.g. `SUN_EGO_STYLE` uses Big Five + Enneagram).

---

## 2. Core Entities — Characters & Charts

### 2.1 CHARACTER

**Purpose:** One row per fictional person/entity.

**Fields (example):**

- `character_id` (PK)
- `external_ref` (optional, link to other systems)
- `name`
- `status` (active, archived, etc.)
- `notes`

**Key relationships:**

- `CHARACTER 1 — N CHART`
- `CHARACTER 1 — N OVERLAY_MODEL_PROFILE`

---

### 2.2 CHART

**Purpose:** One row per astrological chart (birth chart, event chart, etc.) tied to a character.

**Fields:**

- `chart_id` (PK)
- `character_id` (FK → CHARACTER)
- `chart_type` (natal, progressed, composite, etc.)
- `datetime_utc`
- `location`
- `system` (e.g. Tropical, Sidereal)
- `notes`

**Key relationships:**

- `CHART 1 — N ATOMIC_VALUE`
- `CHARACTER 1 — N CHART`

---

## 3. Astro Schema — Domains, Subsystems, Atomic Variables

### 3.1 DOMAIN

**Purpose:** High-level grouping by functional area.

Examples: `Identity`, `Emotional`, `Cognitive`, `Relational`, `Action`, `Growth`, `Shadow`, `Social`, `Global`.

**Fields:**

- `domain_id` (PK)
- `domain_code` (e.g. `IDENTITY`, `EMOTIONAL`)
- `name`
- `description`

**Key relationships:**

- `DOMAIN 1 — N SUBSYSTEM`
- `DOMAIN 1 — N OVERLAY_MODEL` (preferred domain for a model)

---

### 3.2 SUBSYSTEM

**Purpose:** Astrological subsystem slice (Sun, Moon, Mercury, Houses, Aspects, etc.).

Examples: `SUN`, `MOON`, `ASC`, `VENUS`, `MARS`, `HOUSES`, `ASPECTS`, `NODES`, etc.

**Fields:**

- `subsystem_id` (PK)
- `domain_id` (FK → DOMAIN)
- `subsystem_code` (e.g. `SUN`, `MOON`, `MERCURY`, `H5`, `ASPECT_GENERAL`)
- `name`
- `description`

**Key relationships:**

- `SUBSYSTEM 1 — N ATOMIC_VARIABLE_DEF`
- `DOMAIN 1 — N SUBSYSTEM`

---

### 3.3 ATOMIC_VARIABLE_DEF

**Purpose:** The definition of each atomic variable (what you listed: `SUN_IDENTITY_AXIS`, `MOON_NEED_CORE`, etc.).

**Fields:**

- `atomic_var_id` (PK)
- `subsystem_id` (FK → SUBSYSTEM)
- `var_code` (e.g. `SUN_IDENTITY_AXIS`, `MOON_NEED_CORE`)
- `name` (human-readable label)
- `description` (what this variable means)
- `data_type` (text, enum, numeric, JSON)
- `applies_to_level` (character, narrative, both)
- `is_core` (boolean, marks important ones)

**Key relationships:**

- `SUBSYSTEM 1 — N ATOMIC_VARIABLE_DEF`
- `ATOMIC_VARIABLE_DEF 1 — N ATOMIC_VALUE`
- `ATOMIC_VARIABLE_DEF 1 — N ATOMIC_VARIABLE_OVERLAY`

---

### 3.4 ATOMIC_VALUE

**Purpose:** Actual value of each atomic variable for a specific chart (i.e., per character-instance).

**Fields:**

- `chart_id` (FK → CHART)
- `atomic_var_id` (FK → ATOMIC_VARIABLE_DEF)
- `value_text` (for categorical / descriptive values)
- `value_numeric` (for scores)
- `value_json` (for structured subdata if needed)
- `source` (manual, AI, rule engine, etc.)
- `last_updated`

**Primary key (recommended):**

- Composite: `(chart_id, atomic_var_id)`

**Key relationships:**

- `CHART 1 — N ATOMIC_VALUE`
- `ATOMIC_VARIABLE_DEF 1 — N ATOMIC_VALUE`

---

## 4. Overlay Models — Types, Dimensions, Profiles

### 4.1 OVERLAY_MODEL

**Purpose:** External psychological / narrative model (Big Five, Enneagram, Attachment, Shadow, etc.).

**Fields:**

- `model_id` (PK)
- `domain_id` (FK → DOMAIN, primary functional domain)
- `model_code` (e.g. `BIG_FIVE`, `ENNEAGRAM`, `ATTACHMENT`, `SHADOW`, `IFS`)
- `name`
- `description`
- `model_type` (trait, typology, arc, etc.)

**Key relationships:**

- `OVERLAY_MODEL 1 — N OVERLAY_MODEL_DIMENSION`
- `OVERLAY_MODEL 1 — N OVERLAY_MODEL_PROFILE`
- `OVERLAY_MODEL 1 — N ATOMIC_VARIABLE_OVERLAY`
- `DOMAIN 1 — N OVERLAY_MODEL`

---

### 4.2 OVERLAY_MODEL_DIMENSION

**Purpose:** A named dimension or component inside a model.

Examples:

- Big Five → `OPENNESS`, `CONSCIENTIOUSNESS`, `EXTRAVERSION`, `AGREEABLENESS`, `NEUROTICISM`
- Attachment → `STYLE`
- Enneagram → `TYPE`, `WING`
- Grit → `GRIT_SCORE`

**Fields:**

- `dimension_id` (PK)
- `model_id` (FK → OVERLAY_MODEL)
- `dimension_code` (e.g. `O`, `C`, `E`, `A`, `N`, `ATTACHMENT_STYLE`)
- `name`
- `data_type` (numeric, enum, text)
- `min_value` / `max_value` (optional for numeric)
- `enum_options` (optional; JSON list for categorical)

**Key relationships:**

- `OVERLAY_MODEL 1 — N OVERLAY_MODEL_DIMENSION`
- `OVERLAY_MODEL_DIMENSION 1 — N OVERLAY_MODEL_DIMENSION_VALUE`

---

### 4.3 OVERLAY_MODEL_PROFILE

**Purpose:** A character’s specific profile for one overlay model.

Examples:

- “Vivian — Big Five”
- “Vivian — Enneagram”
- “Vivian — Attachment”

**Fields:**

- `profile_id` (PK)
- `character_id` (FK → CHARACTER)
- `chart_id` (nullable FK → CHART; optional if profile is chart-specific)
- `model_id` (FK → OVERLAY_MODEL)
- `profile_label` (e.g. `NATAL_DEFAULT`, `ARC_01`)
- `notes`
- `last_updated`

**Uniqueness suggestion:**

- `(character_id, chart_id, model_id, profile_label)` should be unique.

**Key relationships:**

- `CHARACTER 1 — N OVERLAY_MODEL_PROFILE`
- `CHART 1 — N OVERLAY_MODEL_PROFILE` (optional)
- `OVERLAY_MODEL 1 — N OVERLAY_MODEL_PROFILE`
- `OVERLAY_MODEL_PROFILE 1 — N OVERLAY_MODEL_DIMENSION_VALUE`

---

### 4.4 OVERLAY_MODEL_DIMENSION_VALUE

**Purpose:** Actual score/value for a given dimension in a character’s model profile.

**Fields:**

- `profile_id` (FK → OVERLAY_MODEL_PROFILE)
- `dimension_id` (FK → OVERLAY_MODEL_DIMENSION)
- `value_numeric` (for scores, 0–100 etc.)
- `value_text` (for labels like `Anxious-Avoidant`, `Type 3w4`)
- `value_json` (optional complex data)
- `confidence` (optional, 0–1)
- `source` (manual, AI, etc.)
- `last_updated`

**Primary key (recommended):**

- Composite: `(profile_id, dimension_id)`

**Key relationships:**

- `OVERLAY_MODEL_PROFILE 1 — N OVERLAY_MODEL_DIMENSION_VALUE`
- `OVERLAY_MODEL_DIMENSION 1 — N OVERLAY_MODEL_DIMENSION_VALUE`

---

## 5. Linking Atomic Variables to Overlay Models

### 5.1 ATOMIC_VARIABLE_OVERLAY

**Purpose:** Connects **which models** are used to deepen **which atomic variables** (e.g. `SUN_EGO_STYLE` ← Big Five + Enneagram).

**Fields:**

- `atomic_var_id` (FK → ATOMIC_VARIABLE_DEF)
- `model_id` (FK → OVERLAY_MODEL)
- `role` (e.g. `PRIMARY`, `SECONDARY`, `SUPPORTING`)
- `weight` (numeric, e.g. 1.0, 0.5 for influence priority)
- `notes`

**Primary key:**

- Composite: `(atomic_var_id, model_id)`

**Key relationships:**

- `ATOMIC_VARIABLE_DEF 1 — N ATOMIC_VARIABLE_OVERLAY`
- `OVERLAY_MODEL 1 — N ATOMIC_VARIABLE_OVERLAY`

---

## 6. ER Diagram (Mermaid)

```mermaid
erDiagram

    CHARACTER ||--o{ CHART : has
    CHARACTER ||--o{ OVERLAY_MODEL_PROFILE : "has profile"
    CHART ||--o{ ATOMIC_VALUE : "includes"
    CHART ||--o{ OVERLAY_MODEL_PROFILE : "context for"

    DOMAIN ||--o{ SUBSYSTEM : groups
    DOMAIN ||--o{ OVERLAY_MODEL : "primary domain"
    SUBSYSTEM ||--o{ ATOMIC_VARIABLE_DEF : contains
    ATOMIC_VARIABLE_DEF ||--o{ ATOMIC_VALUE : "valued as"

    OVERLAY_MODEL ||--o{ OVERLAY_MODEL_DIMENSION : defines
    OVERLAY_MODEL ||--o{ OVERLAY_MODEL_PROFILE : "used by"
    OVERLAY_MODEL_PROFILE ||--o{ OVERLAY_MODEL_DIMENSION_VALUE : "assigns"

    OVERLAY_MODEL_DIMENSION ||--o{ OVERLAY_MODEL_DIMENSION_VALUE : "dimension of"

    ATOMIC_VARIABLE_DEF ||--o{ ATOMIC_VARIABLE_OVERLAY : "is enriched by"
    OVERLAY_MODEL ||--o{ ATOMIC_VARIABLE_OVERLAY : "enriches"
