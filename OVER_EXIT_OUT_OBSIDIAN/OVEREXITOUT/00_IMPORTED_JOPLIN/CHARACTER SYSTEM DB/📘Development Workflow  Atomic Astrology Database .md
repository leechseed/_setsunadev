---
title: '📘Development Workflow  Atomic Astrology Database — '
updated: 2025-12-03 18:28:07Z
created: 2025-12-03 18:27:57Z
latitude: 30.43825590
longitude: -84.28073290
altitude: 0.0000
---


# 📘 Atomic Astrology Database — Development Workflow

**Category:** Data Architecture / System Design  
**Focus:** Building the DB as infrastructure (not character-first)

---

## 📑 Table of Contents

1. [Objective](#1-objective)  
2. [Mental Model](#2-mental-model)  
3. [PSTO — Policy / Strategy / Tactics / Operations](#3-psto--policy--strategy--tactics--operations)  
   - [3.1 Policy](#31-policy)  
   - [3.2 Strategy](#32-strategy)  
   - [3.3 Tactics](#33-tactics)  
   - [3.4 Operations](#34-operations)  
4. [Phase 0 — Stack & Ground Rules](#4-phase-0--stack--ground-rules)  
   - [4.1 DB Engine](#41-db-engine)  
   - [4.2 Tooling](#42-tooling)  
   - [4.3 Conventions](#43-conventions)  
5. [Phase 1 — Core Meta Schema](#5-phase-1--core-meta-schema)  
   - [5.1 Tables to Build First](#51-tables-to-build-first)  
   - [5.2 Minimal DDL Skeleton](#52-minimal-ddl-skeleton)  
6. [Phase 2 — Seed Domains, Subsystems, Atomic Variables](#6-phase-2--seed-domains-subsystems-atomic-variables)  
   - [6.1 Seeding Strategy](#61-seeding-strategy)  
   - [6.2 Sanity Checks](#62-sanity-checks)  
7. [Phase 3 — Add Overlay Models (Meta Only)](#7-phase-3--add-overlay-models-meta-only)  
   - [7.1 Register Models](#71-register-models)  
   - [7.2 Register Dimensions](#72-register-dimensions)  
8. [Phase 4 — Wire Astro Variables to Models](#8-phase-4--wire-astro-variables-to-models)  
9. [Phase 5 — Characters, Charts & Instance Layer](#9-phase-5--characters-charts--instance-layer)  
   - [9.1 Core Instance Tables](#91-core-instance-tables)  
   - [9.2 Overlay & Atomic Instance Tables](#92-overlay--atomic-instance-tables)  
10. [Phase 6 — Dev Workflows & Core Queries](#10-phase-6--dev-workflows--core-queries)  
    - [10.1 Must-Have Queries](#101-must-have-queries)  
11. [Phase 7 — Iteration Strategy](#11-phase-7--iteration-strategy)  
12. [One-Week Implementation Plan](#12-one-week-implementation-plan)

---

## 1. Objective

- Build a **universal astrology + psychology database** that:
  - Stores **meta definitions** (domains, subsystems, atomic variables, overlay models).
  - Stores **instance data** (characters, charts, overlay scores, atomic values).
  - Lets you attach external models (Big Five, Enneagram, Attachment, etc.) to astro variables in a clean, scalable way.

This is **infrastructure**, not story. The goal is a stable schema you can slam thousands of characters into later.

---

## 2. Mental Model

- **Meta vs Instance:**
  - **META** = dictionary / grammar:
    - `domains`, `subsystems`, `atomic_variable_def`, `overlay_model`, `overlay_model_dimension`, `atomic_variable_overlay`.
  - **INSTANCE** = actual data:
    - `characters`, `charts`, `overlay_model_profile`, `overlay_model_dimension_value`, `atomic_value`.

- Think in 3 layers:
  1. **Grammar** → table structure + meta rows.
  2. **Dictionary** → all your atomic var definitions + model dimensions.
  3. **Sentences** → concrete character charts and values.

You do **1 & 2 first**. Characters come later.

---

## 3. PSTO — Policy / Strategy / Tactics / Operations

### 3.1 Policy

**High-level rules this system must obey:**

- **P1 — Meta First, Instance Second**  
  The database is built as a **meta engine**, not a character toy. All design decisions prioritize clean separation between:
  - Meta tables (definitions, schemas, wiring).
  - Instance tables (per-character, per-chart data).
- **P2 — Schema Stability Over Vibe**  
  Structural changes must be deliberate and migration-based. No “freelance” edits in the live DB.
- **P3 — Extensibility Over Perfection**  
  It’s better to be able to *add* a new model or variable than to constantly rename or reshape old ones.
- **P4 — One Source of Truth**  
  Every concept (atomic variable, model, dimension) has exactly **one canonical definition** in meta tables.
- **P5 — Readability for Future You**  
  Names and structure must be clear enough that six months from now, you can read the schema without wanting to die.

---

### 3.2 Strategy

**How we’re going to achieve the policy-level goals:**

- **S1 — Two-Layer Architecture**
  - Layer 1: **Meta Schema**  
    `domains`, `subsystems`, `atomic_variable_def`, `overlay_model`, `overlay_model_dimension`, `atomic_variable_overlay`.
  - Layer 2: **Instance Data**  
    `characters`, `charts`, `overlay_model_profile`, `overlay_model_dimension_value`, `atomic_value`.
- **S2 — Phased Build-Out**
  1. Lock core meta schema.
  2. Populate astro variable definitions.
  3. Add overlay models + dimensions.
  4. Wire variables ↔ models.
  5. Only then create characters/charts and start using the system.
- **S3 — Migrations as Gatekeepers**
  - All schema evolution goes through migrations.
  - No silent, manual structural edits; everything is traceable.
- **S4 — Test with Synthetic Characters**
  - Use 1–2 “dummy” characters and charts to validate flows before loading real narrative data.
- **S5 — Query-Driven Validation**
  - Define a small set of **canonical queries** that must always work.  
  - When schema changes, these queries are regression tests.

---

### 3.3 Tactics

**Concrete design choices that make the strategy real:**

- **T1 — Tech Stack**
  - Use **PostgreSQL** as the primary engine.
  - Use **DBBeaver** for visual inspection and ad-hoc queries.
- **T2 — Naming Conventions**
  - Tables in `snake_case_plural`: `atomic_variable_def`, `overlay_model_profile`.
  - Primary keys: `<table>_id`: `character_id`, `model_id`.
  - Code fields in `UPPER_SNAKE`: `SUN_IDENTITY_AXIS`, `BIG_FIVE`.
- **T3 — Hard Separation of Concerns**
  - No instance data sneaks into meta tables.
  - No definitional info (like descriptions of `SUN_IDENTITY_AXIS`) lives in instance tables.
- **T4 — CSV → DB for Bulk Meta**
  - Maintain atomic variable definitions in a **CSV/markdown list** that can be imported into `atomic_variable_def`.
  - Same for model dimensions.
- **T5 — JSON for Complex Values**
  - Where needed, use `value_json` for rich, structured data (e.g., complex scores) but keep basic stuff in `value_text` / `value_numeric`.
- **T6 — Minimal Test Character Set**
  - Start with:
    - 1 character,
    - 1 natal chart,
    - 2–3 overlay models,
    - a small slice of atomic variables (Sun/Moon/Asc).
  - Only expand when the flow from meta → overlay → atomic value is proven.

---

### 3.4 Operations

**Day-to-day behaviors, step-by-step:**

- **O1 — Schema Change Workflow**
  1. Edit migration file (add/alter tables or columns).
  2. Run migration against dev DB.
  3. Run canonical queries to confirm nothing broke.
  4. Apply migration to main DB.
- **O2 — Meta Seeding Workflow**
  1. Update `domains`, `subsystems`, `atomic_variable_def`, `overlay_model`, `overlay_model_dimension` in CSV/markdown.
  2. Import/update via script or DBBeaver.
  3. Run checks:
     - Count of variables per subsystem.
     - Duplicate `var_code` / `model_code` checks.
- **O3 — Wiring Workflow (Atomic ↔ Overlay)**
  1. Decide which models influence a given atomic variable.
  2. Insert rows into `atomic_variable_overlay` with `role` + `weight`.
  3. Run a quick query to verify the mapping.
- **O4 — Character Onboarding Workflow**
  1. Insert `characters` row.
  2. Insert `charts` row linked to that character.
  3. Create `overlay_model_profile` rows for the models you care about.
  4. Insert `overlay_model_dimension_value` rows with scores or labels.
  5. Generate `atomic_value` rows based on your logic (manual or via code).
- **O5 — Validation & Maintenance**
  - Regularly:
    - Run the core queries (Section 10) as a health check.
    - Compare counts:
      - # of `atomic_variable_def` vs. # of `atomic_value` per chart (coverage).
      - # of `overlay_model_dimension` vs. # of `overlay_model_dimension_value` per profile (completeness).
    - Log major schema changes in a simple changelog file.

---

## 4. Phase 0 — Stack & Ground Rules

### 4.1 DB Engine

- Recommended:
  - **PostgreSQL** if you want a long-term, flexible, JSON-friendly core.
  - **SQLite** only if you want a quick single-file portable prototype.

- Default assumption: **Postgres**.

---

### 4.2 Tooling

- **DB viewer:** DBBeaver (browse tables, run queries, inspect ERD).
- **Migrations:** pick one and commit to it, e.g.:
  - `Flyway`, `Liquibase`, or
  - ORM-based: `SQLAlchemy + Alembic`, `Prisma`, etc.

Rule:  
- **No manual schema changes in “real” DB.**  
- All schema edits go through migrations.

---

### 4.3 Conventions

- **Naming:**
  - Tables: `snake_case_plural` → `domains`, `subsystems`, `atomic_variable_def`.
  - PKs: `table_singular_id` → `domain_id`, `subsystem_id`.
  - Codes: `UPPER_SNAKE` → `SUN_IDENTITY_AXIS`, `BIG_FIVE`.

- **IDs:**
  - Start with `SERIAL` / `BIGINT` primary keys.
  - Add `uuid` later if you really need cross-system IDs.

- **Separation:**
  - META tables: definitions only.
  - INSTANCE tables: per character/chart data only.

Lock this in: **do not mix meta and instance in the same table.**

---

## 5. Phase 1 — Core Meta Schema

### 5.1 Tables to Build First

Create these **before touching characters**:

1. `domains` – high-level psycho-astro buckets.  
2. `subsystems` – Sun/Moon/Asc/Planets/Houses/etc. mapped to domains.  
3. `atomic_variable_def` – all the `SUN_*`, `MOON_*`, `ASC_*`, `H*_` variables.  
4. `overlay_model` – Big Five, Enneagram, Attachment, etc.  
5. `overlay_model_dimension` – each trait/slider inside those models.

---

### 5.2 Minimal DDL Skeleton

Barebones start (Postgres-flavored):

```sql
CREATE TABLE domains (
    domain_id        SERIAL PRIMARY KEY,
    domain_code      VARCHAR(64) UNIQUE NOT NULL,
    name             VARCHAR(128) NOT NULL,
    description      TEXT
);

CREATE TABLE subsystems (
    subsystem_id     SERIAL PRIMARY KEY,
    domain_id        INTEGER NOT NULL REFERENCES domains(domain_id),
    subsystem_code   VARCHAR(64) UNIQUE NOT NULL,
    name             VARCHAR(128) NOT NULL,
    description      TEXT
);

CREATE TABLE atomic_variable_def (
    atomic_var_id    SERIAL PRIMARY KEY,
    subsystem_id     INTEGER NOT NULL REFERENCES subsystems(subsystem_id),
    var_code         VARCHAR(128) UNIQUE NOT NULL,
    name             VARCHAR(128) NOT NULL,
    description      TEXT,
    data_type        VARCHAR(32) NOT NULL DEFAULT 'text',
    applies_to_level VARCHAR(32) NOT NULL DEFAULT 'both',
    is_core          BOOLEAN NOT NULL DEFAULT TRUE
);

CREATE TABLE overlay_model (
    model_id         SERIAL PRIMARY KEY,
    domain_id        INTEGER REFERENCES domains(domain_id),
    model_code       VARCHAR(64) UNIQUE NOT NULL,
    name             VARCHAR(128) NOT NULL,
    model_type       VARCHAR(64) NOT NULL,
    description      TEXT
);

CREATE TABLE overlay_model_dimension (
    dimension_id     SERIAL PRIMARY KEY,
    model_id         INTEGER NOT NULL REFERENCES overlay_model(model_id),
    dimension_code   VARCHAR(64) NOT NULL,
    name             VARCHAR(128) NOT NULL,
    data_type        VARCHAR(32) NOT NULL DEFAULT 'numeric',
    min_value        NUMERIC,
    max_value        NUMERIC,
    enum_options     JSONB,
    UNIQUE (model_id, dimension_code)
);
````

This is your **skeleton**. No character data yet.

---

## 6. Phase 2 — Seed Domains, Subsystems, Atomic Variables

### 6.1 Seeding Strategy

1. **Seed `domains`:**

   * Example set:

     * `IDENTITY`, `EMOTIONAL`, `COGNITIVE`, `RELATIONAL`, `ACTION`, `GROWTH`, `SHADOW`, `SOCIAL`, `GLOBAL`.

2. **Seed `subsystems`:**

   * Map each subsystem to a domain:

     * `SUN`, `MOON`, `ASC`, `MERCURY`, `VENUS`, `MARS`, `JUPITER`, `SATURN`, `URANUS`, `NEPTUNE`, `PLUTO`.
     * `HOUSES`, `ASPECTS`, `NODES`, `POINTS`, `CHART_SHAPE`, etc.

3. **Seed `atomic_variable_def`:**

   * Take your long markdown list of atomic vars:

     * `SUN_IDENTITY_AXIS`, `SUN_MOTIVATION_VECTOR`, `MOON_NEED_CORE`, `ASC_SURFACE_IMAGE`, `H1_SELF_ARCHETYPE`, etc.
   * Convert to **CSV** and bulk-import via DBBeaver or scripts:

     * `subsystem_code`, `var_code`, `name`, `description`, `data_type`.

You’re filling the **catalogue**. No scores, no text values yet.

---

### 6.2 Sanity Checks

By the end of this phase you should be able to:

* `SELECT * FROM domains;`
  → see all your domains.

* List all subsystem+domain combos:

  ```sql
  SELECT d.domain_code, s.subsystem_code
  FROM subsystems s
  JOIN domains d ON s.domain_id = d.domain_id;
  ```

* List all atomic variables for Sun:

  ```sql
  SELECT s.subsystem_code, avd.var_code, avd.name
  FROM atomic_variable_def avd
  JOIN subsystems s ON avd.subsystem_id = s.subsystem_id
  WHERE s.subsystem_code = 'SUN'
  ORDER BY avd.var_code;
  ```

If this isn’t clean and readable, fix schema now.

---

## 7. Phase 3 — Add Overlay Models (Meta Only)

Still no characters. Just wiring models.

### 7.1 Register Models

Insert into `overlay_model`:

* `BIG_FIVE` (domain `IDENTITY`, type `trait`).
* `ENNEAGRAM` (domain `IDENTITY`, type `typology`).
* `ATTACHMENT` (domain `EMOTIONAL`, type `typology`).
* Later: `SHADOW`, `IFS`, `SCHEMA`, `STERNBERG`, `LOVE_LANG`, `T_KILMANN`, `KARPMAN`, `MASLOW`, `SDT`, etc.

These rows define **which psychology packs exist** in the system.

---

### 7.2 Register Dimensions

For each model, define dimensions in `overlay_model_dimension`:

* **Big Five:**

  * `O`, `C`, `E`, `A`, `N` (numeric 0–100).
* **Enneagram:**

  * `TYPE`, `WING` (text/enums 1–9).
* **Attachment:**

  * `STYLE` (enum: `Secure`, `Anxious`, `Avoidant`, `Disorganized`).

At this point, still **no character scores**. You’re just defining sliders.

---

## 8. Phase 4 — Wire Astro Variables to Models

Create the junction table:

```sql
CREATE TABLE atomic_variable_overlay (
    atomic_var_id  INTEGER NOT NULL REFERENCES atomic_variable_def(atomic_var_id),
    model_id       INTEGER NOT NULL REFERENCES overlay_model(model_id),
    role           VARCHAR(32) NOT NULL DEFAULT 'PRIMARY',
    weight         NUMERIC NOT NULL DEFAULT 1.0,
    notes          TEXT,
    PRIMARY KEY (atomic_var_id, model_id)
);
```

Then seed rules like:

* `SUN_IDENTITY_AXIS` → `BIG_FIVE` (PRIMARY, 0.7) + `ENNEAGRAM` (SECONDARY, 0.3).
* `SUN_EGO_STYLE` → `BIG_FIVE` only.
* `MOON_NEED_CORE` → `ATTACHMENT` only.
* Etc, for all relevant atomic vars.

This is where you declare:

> “When I compute **this atomic trait**, these **models** are consulted, with these **weights**.”

Still zero characters.

---

## 9. Phase 5 — Characters, Charts & Instance Layer

Once meta is stable, add the **instance layer**.

### 9.1 Core Instance Tables

```sql
CREATE TABLE characters (
    character_id   SERIAL PRIMARY KEY,
    name           VARCHAR(128) NOT NULL,
    status         VARCHAR(32) NOT NULL DEFAULT 'active',
    notes          TEXT
);

CREATE TABLE charts (
    chart_id       SERIAL PRIMARY KEY,
    character_id   INTEGER NOT NULL REFERENCES characters(character_id),
    chart_type     VARCHAR(64) NOT NULL,
    datetime_utc   TIMESTAMPTZ,
    location       VARCHAR(256),
    system         VARCHAR(64),
    notes          TEXT
);
```

Guideline:

* Use **1–2 test characters** at first.
* Don’t treat early characters as canon; they’re just schema testers.

---

### 9.2 Overlay & Atomic Instance Tables

Overlay profiles & values:

```sql
CREATE TABLE overlay_model_profile (
    profile_id     SERIAL PRIMARY KEY,
    character_id   INTEGER NOT NULL REFERENCES characters(character_id),
    chart_id       INTEGER REFERENCES charts(chart_id),
    model_id       INTEGER NOT NULL REFERENCES overlay_model(model_id),
    profile_label  VARCHAR(64) NOT NULL,
    notes          TEXT,
    UNIQUE (character_id, chart_id, model_id, profile_label)
);

CREATE TABLE overlay_model_dimension_value (
    profile_id     INTEGER NOT NULL REFERENCES overlay_model_profile(profile_id),
    dimension_id   INTEGER NOT NULL REFERENCES overlay_model_dimension(dimension_id),
    value_numeric  NUMERIC,
    value_text     VARCHAR(256),
    value_json     JSONB,
    source         VARCHAR(64),
    last_updated   TIMESTAMPTZ DEFAULT NOW(),
    PRIMARY KEY (profile_id, dimension_id)
);
```

Atomic values per chart:

```sql
CREATE TABLE atomic_value (
    chart_id       INTEGER NOT NULL REFERENCES charts(chart_id),
    atomic_var_id  INTEGER NOT NULL REFERENCES atomic_variable_def(atomic_var_id),
    value_text     TEXT,
    value_numeric  NUMERIC,
    value_json     JSONB,
    source         VARCHAR(64),
    last_updated   TIMESTAMPTZ DEFAULT NOW(),
    PRIMARY KEY (chart_id, atomic_var_id)
);
```

This layer is where **Vivian**, etc. actually get:

* Big Five scores,
* Enneagram type,
* Attachment style,
* Atomic variable summaries.

---

## 10. Phase 6 — Dev Workflows & Core Queries

You now need **basic dev workflows** to prove the schema is sane.

### 10.1 Must-Have Queries

**1. List all atomic variables for a subsystem (e.g. Sun):**

```sql
SELECT d.domain_code, s.subsystem_code, avd.var_code, avd.name
FROM atomic_variable_def avd
JOIN subsystems s ON avd.subsystem_id = s.subsystem_id
JOIN domains d ON s.domain_id = d.domain_id
WHERE s.subsystem_code = 'SUN'
ORDER BY avd.var_code;
```

**2. For a given atomic variable, list its overlay models:**

```sql
SELECT avd.var_code, om.model_code, avo.role, avo.weight
FROM atomic_variable_overlay avo
JOIN atomic_variable_def avd ON avo.atomic_var_id = avd.atomic_var_id
JOIN overlay_model om ON avo.model_id = om.model_id
WHERE avd.var_code = 'SUN_IDENTITY_AXIS';
```

**3. For a given character + chart, show overlay scores:**

```sql
SELECT c.name,
       om.model_code,
       omd.dimension_code,
       omdv.value_numeric,
       omdv.value_text
FROM overlay_model_dimension_value omdv
JOIN overlay_model_profile omp ON omdv.profile_id = omp.profile_id
JOIN overlay_model_dimension omd ON omdv.dimension_id = omd.dimension_id
JOIN overlay_model om ON omd.model_id = om.model_id
JOIN characters c ON omp.character_id = c.character_id
WHERE c.character_id = 1
  AND omp.chart_id = 1;
```

**4. Dump all atomic values for a chart:**

```sql
SELECT c.name,
       ch.chart_id,
       s.subsystem_code,
       avd.var_code,
       av.value_text,
       av.value_numeric
FROM atomic_value av
JOIN charts ch ON av.chart_id = ch.chart_id
JOIN characters c ON ch.character_id = c.character_id
JOIN atomic_variable_def avd ON av.atomic_var_id = avd.atomic_var_id
JOIN subsystems s ON avd.subsystem_id = s.subsystem_id
WHERE ch.chart_id = 1
ORDER BY s.subsystem_code, avd.var_code;
```

If these don’t run clean or return sensible data, your design isn’t ready.

---

## 11. Phase 7 — Iteration Strategy

You’re going to keep thinking of better ways to slice things. Don’t wreck the DB every time.

* **Freeze in bursts:**

  * For 1–2 weeks at a time, treat `domains`, `subsystems`, `atomic_variable_def` as **locked**.
  * Make changes via migrations only.

* **Favor adding over renaming:**

  * If you want a prettier label, add a `display_name` column instead of changing codes.

* **Overlay models stay modular:**

  * If a model bloats, add `*_EXTENDED` variant instead of mutating the original.

* **Characters are disposable until meta is stable:**

  * Early characters are test data.
  * Real asset = **meta dictionary & schema**, not first drafts of Vivian.

---

## 12. One-Week Implementation Plan

**Day 1–2: Core Meta**

* Stand up Postgres + DBBeaver.
* Create:

  * `domains`, `subsystems`, `atomic_variable_def`.
* Seed:

  * All `domains`.
  * Core `subsystems` (Sun–Pluto, Houses, Aspects, Nodes).
  * At least Sun/Moon/Asc atomic vars from your existing list.

**Day 3–4: Overlay Meta**

* Create:

  * `overlay_model`, `overlay_model_dimension`, `atomic_variable_overlay`.
* Seed:

  * `BIG_FIVE`, `ENNEAGRAM`, `ATTACHMENT`, plus any others you’re sure about.
* Wire:

  * All `SUN_*` and `MOON_*` variables to relevant models with roles/weights.

**Day 5: Instance Skeleton**

* Create:

  * `characters`, `charts`, `overlay_model_profile`, `overlay_model_dimension_value`, `atomic_value`.
* Add:

  * 1 test character + 1 natal chart.
  * 1 set of overlay scores (e.g., Big Five + Enneagram + Attachment).
  * 3–5 `atomic_value` records generated manually as a proof-of-concept.

**Day 6: Query & Debug**

* Run the **four core queries**.
* Fix:

  * Bad joins, missing FKs, naming screwups.
* Confirm:

  * You can move from character → chart → overlay scores → atomic values smoothly.

**Day 7: Admin + Refinement**

* Build tiny admin flows:

  * SQL scripts / CLI to:

    * Add a new atomic variable definition.
    * Attach overlay models to that variable.
    * List everything for a given subsystem.
* Once this is painless, scale up:

  * Add the full variable universe (all planets/houses/aspects).
  * Add more overlay models.

At that point, the DB is a **real instrument panel**, not a loose pile of ideas.

```
```
