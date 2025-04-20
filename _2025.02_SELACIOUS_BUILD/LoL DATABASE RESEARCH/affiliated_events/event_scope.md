## 📘 Table of Contents

- [1. Event_Scope_ID](#1_event_scope_id)
- [2. Scope_Label](#2_scope_label)
- [3. Description](#3_description)
- [4. Affected_Regions](#4_affected_regions)
- [5. Temporal_Duration](#5_temporal_duration)
- [6. Escalation_Potential](#6_escalation_potential)
- [7. Example_Events](#7_example_events)
- [8. Notes](#8_notes)

---
# **Narrative Asset Schema: Event_Scope**

---

## 1. Event_Scope_ID

- **Definition**: Unique identifier (slug or numeric) for the event scope classification.
- **Examples**: `personal`, `regional`, `cosmic`

---

## 2. Scope_Label

- **Definition**: Human-readable name for the scope level.
- Values:
  - Personal
  - Localized Conflict
  - Regional
  - Interregional
  - Global / World-Shaping
  - Cosmic / Multiversal

---

## 3. Description

- **Definition**: Summary of what the scope represents in narrative terms.
- Examples:
  - **Personal**: Affects only one character or their immediate circle.
  - **Regional**: Alters the political or environmental status of a single region (e.g., Demacia, Shurima).
  - **Global**: Causes continent-wide war, magic disasters, or factional shifts.
  - **Cosmic**: Involves the Void, Celestials, or metaphysical realities beyond Runeterra.

---

## 4. Affected_Regions

- **Definition**: List of Runeterran regions directly impacted.
- Format: Multi-select field
- Examples:
  - Ionia, Zaun, Shadow Isles

---

## 5. Temporal_Duration

- **Definition**: How long the event lasted in lore time.
- Values:
  - Instantaneous
  - Hours / Days
  - Weeks / Months
  - Years / Decades
  - Timeless / Ongoing

---

## 6. Escalation_Potential

- **Definition**: Whether the scope has potential to grow beyond initial range.
- Values:
  - Contained
  - Expanding
  - Uncontrolled
  - Already Maximal

---

## 7. Example_Events

- **Definition**: Canonical examples of each scope type.
- Examples:
  - **Personal** → Yasuo's exile
  - **Regional** → Freljord Civil War
  - **Global** → The Ruination
  - **Cosmic** → Void incursions, Targonian ascensions

---

## 8. Notes

- **Definition**: Developer intent, classification edge cases, or post-event reevaluations.
