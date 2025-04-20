## 📘 Table of Contents

- [1. Event_Role_ID](#1_event_role_id)
- [2. Label](#2_label)
- [3. Role_Function](#3_role_function)
- [4. Agency_Level](#4_agency_level)
- [5. Role_Persistence](#5_role_persistence)
- [6. Shared_Role_Flag](#6_shared_role_flag)
- [7. Example_Usage](#7_example_usage)
- [8. Notes](#8_notes)

---
# **Narrative Asset Schema: Event_Role**

---

## 1. Event_Role_ID

- **Definition**: Unique identifier for the role entry (slug or numeric).
- **Examples**: `main_protagonist`, `support_character`, `catalyst_entity`

---

## 2. Label

- **Definition**: Human-readable name of the role.
- Examples:
  - Main Protagonist
  - Main Antagonist
  - Supporting Character
  - Catalyst / Trigger
  - Victim / Collateral
  - Passive Witness
  - Background Mention

---

## 3. Role_Function

- **Definition**: Narrative function this role serves within the event structure.
- Examples:
  - Drives the central conflict (Main Protagonist)
  - Acts as moral or physical opposition (Antagonist)
  - Enables the event’s ignition or transformation (Catalyst)
  - Suffers irreversible consequence to show stakes (Victim)
  - Adds flavor without affecting outcome (Background Mention)

---

## 4. Agency_Level

- **Definition**: Degree of impact or choice the champion exerts during the event.
- Values:
  - High (Direct influence on outcome)
  - Medium (Partial influence or co-dependent)
  - Low (Involuntary or circumstantial involvement)
  - None (Referenced or affected only)

---

## 5. Role_Persistence

- **Definition**: Duration of the character’s presence across the event timeline.
- Values:
  - Full Event
  - Midway Entry
  - Flashback Only
  - Climax Only
  - Off-Screen / Epistolary

---

## 6. Shared_Role_Flag

- **Definition**: Indicates if the narrative role is shared with other champions.
- Values:
  - Yes (multi-character arcs)
  - No (unique role)
  - Partial (overlap in key phases)

---

## 7. Example_Usage

- **Definition**: Real-world application from existing Riot narrative events.
- Examples:
  - Viego as **Main Antagonist** in _The Ruination_
  - Senna as **Catalyst** and **Supporting Hero** in _Sentinels of Light_
  - Riven as **Passive Mention** in _Noxian Civil Discord_

---

## 8. Notes

- **Definition**: Commentary on edge cases, overlaps, or retconned roles.
