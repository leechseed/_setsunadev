---
title: ✅ **Atomic Astrology Database — Daily Build Checklist**
updated: 2025-12-03 18:30:00Z
created: 2025-12-03 18:29:55Z
latitude: 30.43825590
longitude: -84.28073290
altitude: 0.0000
---


# ✅ **Atomic Astrology Database — Daily Build Checklist**

---

## **📅 Day 1–2: Core Meta (Domains, Subsystems, Atomic Variables)**

* [ ] **Install DB stack**

  * [ ] PostgreSQL installed and running
  * [ ] DBBeaver connected to the Postgres instance

* [ ] **Create schema tables**

  * [ ] `domains`
  * [ ] `subsystems`
  * [ ] `atomic_variable_def`

* [ ] **Seed base meta**

  * [ ] Insert all `domains` (IDENTITY, EMOTIONAL, etc.)
  * [ ] Insert `subsystems` (SUN → IDENTITY, MOON → EMOTIONAL, etc.)
  * [ ] Import CSV of atomic variables (`SUN_IDENTITY_AXIS`, etc.)

* [ ] **Sanity check**

  * [ ] Run `SELECT * FROM domains;`
  * [ ] Verify subsystem-to-domain mapping query
  * [ ] Confirm Sun atomic vars show correctly with names/descriptions

---

## **📅 Day 3–4: Overlay Meta (Models & Dimensions)**

* [ ] **Create model tables**

  * [ ] `overlay_model`
  * [ ] `overlay_model_dimension`
  * [ ] `atomic_variable_overlay`

* [ ] **Seed overlay models**

  * [ ] BIG_FIVE (trait)
  * [ ] ENNEAGRAM (typology)
  * [ ] ATTACHMENT (typology)
  * [ ] Add optional: SHADOW, IFS, LOVE_LANG, etc.

* [ ] **Seed model dimensions**

  * [ ] BIG_FIVE → O, C, E, A, N (0–100)
  * [ ] ENNEAGRAM → TYPE, WING
  * [ ] ATTACHMENT → STYLE (enum Secure, Anxious, Avoidant, Disorganized)

* [ ] **Wire atomic variables**

  * [ ] SUN_IDENTITY_AXIS → BIG_FIVE + ENNEAGRAM
  * [ ] SUN_EGO_STYLE → BIG_FIVE
  * [ ] MOON_NEED_CORE → ATTACHMENT
  * [ ] Verify mapping with query output

---

## **📅 Day 5: Instance Skeleton**

* [ ] **Create instance tables**

  * [ ] `characters`
  * [ ] `charts`
  * [ ] `overlay_model_profile`
  * [ ] `overlay_model_dimension_value`
  * [ ] `atomic_value`

* [ ] **Insert test character**

  * [ ] 1 record in `characters` (e.g., Test Character)
  * [ ] 1 natal chart in `charts`
  * [ ] Create linked profiles for BIG_FIVE, ENNEAGRAM, ATTACHMENT
  * [ ] Insert example scores (e.g., O=80, C=60, etc.)
  * [ ] Insert 3–5 atomic variable values manually (proof of flow)

---

## **📅 Day 6: Query & Debug**

* [ ] Run **Core Queries**

  * [ ] List atomic variables for subsystem
  * [ ] Check overlay model mapping per variable
  * [ ] Retrieve overlay scores per character + chart
  * [ ] Dump all atomic values per chart

* [ ] **Debug issues**

  * [ ] Verify foreign keys + constraints
  * [ ] Confirm joins return expected results
  * [ ] Fix naming or schema errors via migration scripts

* [ ] **Validation checks**

  * [ ] # of `atomic_variable_def` = expected
  * [ ] # of `atomic_value` per chart matches definition count
  * [ ] # of overlay dimensions matches model specification

---

## **📅 Day 7: Admin + Refinement**

* [ ] **Admin script setup**

  * [ ] Script to add new atomic variable defs
  * [ ] Script to wire overlays automatically
  * [ ] Script to dump subsystem/variable summaries

* [ ] **Schema stability**

  * [ ] Lock `domains`, `subsystems`, and `atomic_variable_def` for 1 week
  * [ ] Add `display_name` columns instead of renaming codes
  * [ ] Keep changelog of migrations

* [ ] **Expansion readiness**

  * [ ] Add remaining planets, houses, aspects
  * [ ] Add extra overlay models (Maslow, SDT, Shadow, etc.)
  * [ ] Validate new model integrations

---

## **🧠 Ongoing Maintenance Checklist**

* [ ] Weekly schema regression test via core queries
* [ ] Monthly migration log review
* [ ] Backup and version meta CSVs
* [ ] Add new overlay model dimensions only via controlled migration
* [ ] Run coverage reports (atomic vs overlay completeness)

---

Would you like me to generate a **CLI-friendly version** (e.g., shell checklist with timestamps and progress logging) to actually *run this* each day as part of a dev workflow?
