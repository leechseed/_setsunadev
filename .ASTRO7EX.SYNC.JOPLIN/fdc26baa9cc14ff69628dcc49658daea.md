📘 Development Workflow Atomic Astrology Database — 

# 📘 Atomic Astrology Database — Development Workflow

**Category:** Data Architecture / System Design  
**Focus:** Building the DB as infrastructure (not character-first)

---

## 📑 Table of Contents

1. [Objective](#1-objective)  
2. [Mental Model](#2-mental-model)  
3. [Phase 0 — Stack & Ground Rules](#3-phase-0--stack--ground-rules)  
   - [3.1 DB Engine](#31-db-engine)  
   - [3.2 Tooling](#32-tooling)  
   - [3.3 Conventions](#33-conventions)  
4. [Phase 1 — Core Meta Schema](#4-phase-1--core-meta-schema)  
   - [4.1 Tables to Build First](#41-tables-to-build-first)  
   - [4.2 Minimal DDL Skeleton](#42-minimal-ddl-skeleton)  
5. [Phase 2 — Seed Domains, Subsystems, Atomic Variables](#5-phase-2--seed-domains-subsystems-atomic-variables)  
   - [5.1 Seeding Strategy](#51-seeding-strategy)  
   - [5.2 Sanity Checks](#52-sanity-checks)  
6. [Phase 3 — Add Overlay Models (Meta Only)](#6-phase-3--add-overlay-models-meta-only)  
   - [6.1 Register Models](#61-register-models)  
   - [6.2 Register Dimensions](#62-register-dimensions)  
7. [Phase 4 — Wire Astro Variables to Models](#7-phase-4--wire-astro-variables-to-models)  
8. [Phase 5 — Characters, Charts & Instance Layer](#8-phase-5--characters-charts--instance-layer)  
   - [8.1 Core Instance Tables](#81-core-instance-tables)  
   - [8.2 Overlay & Atomic Instance Tables](#82-overlay--atomic-instance-tables)  
9. [Phase 6 — Dev Workflows & Core Queries](#9-phase-6--dev-workflows--core-queries)  
   - [9.1 Must-Have Queries](#91-must-have-queries)  
10. [Phase 7 — Iteration Strategy](#10-phase-7--iteration-strategy)  
11. [One-Week Implementation Plan](#11-one-week-implementation-plan)

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

## 3. Phase 0 — Stack & Ground Rules

### 3.1 DB Engine

- Recommended:
  - **PostgreSQL** if you want a long-term, flexible, JSON-friendly core.
  - **SQLite** only if you want a quick single-file portable prototype.

- Default assumption: **Postgres**.

---

### 3.2 Tooling

- **DB viewer:** DBBeaver (browse tables, run queries, inspect ERD).
- **Migrations:** pick one and commit to it, e.g.:
  - `Flyway`, `Liquibase`, or
  - ORM-based: `SQLAlchemy + Alembic`, `Prisma`, etc.

Rule:  
- **No manual schema changes in “real” DB.**  
- All schema edits go through migrations.

---

### 3.3 Conventions

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

## 4. Phase 1 — Core Meta Schema

### 4.1 Tables to Build First

Create these **before touching characters**:

1. `domains` – high-level psycho-astro buckets.
2. `subsystems` – Sun/Moon/Asc/Planets/Houses/etc. mapped to domains.
3. `atomic_variable_def` – all the `SUN_*`, `MOON_*`, `ASC_*`, `H*_` variables.
4. `overlay_model` – Big Five, Enneagram, Attachment, etc.
5. `overlay_model_dimension` – each trait/slider inside those models.

---

### 4.2 Minimal DDL Skeleton

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


id: fdc26baa9cc14ff69628dcc49658daea
parent_id: 1bee78f443a94558b4a4b89a9f2e81f9
created_time: 2025-12-03T18:13:39.313Z
updated_time: 2025-12-03T18:23:26.428Z
is_conflict: 0
latitude: 30.43825590
longitude: -84.28073290
altitude: 0.0000
author: 
source_url: 
is_todo: 0
todo_due: 0
todo_completed: 0
source: joplin-desktop
source_application: net.cozic.joplin-desktop
application_data: 
order: 0
user_created_time: 2025-12-03T18:13:39.313Z
user_updated_time: 2025-12-03T18:23:26.428Z
encryption_cipher_text: 
encryption_applied: 0
markup_language: 1
is_shared: 0
share_id: 
conflict_original_id: 
master_key_id: 
user_data: 
deleted_time: 0
type_: 1