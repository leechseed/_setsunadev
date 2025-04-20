## 📘 Table of Contents

- [1. Notes_ID](#1_notes_id)
- [2. Associated_Asset](#2_associated_asset)
- [3. Note_Type](#3_note_type)
- [4. Note_Text](#4_note_text)
- [5. Source_Citation](#5_source_citation)
- [6. Status](#6_status)
- [7. Last_Updated](#7_last_updated)

---
# **Narrative Asset Schema: Notes**

---

## 1. Notes_ID

- **Definition**: Unique identifier (slug or numeric) for the note entry.
- **Examples**: `viego_retcon_warning`, `zilean_temporal_inconsistency`

---

## 2. Associated_Asset

- **Definition**: The schema or object this note is attached to.
- Examples:
  - Champion_ID: `viego`
  - Event_ID: `ruination`
  - Timeline_Position_ID: `post_ruination`
  - Field: `Narrative_Status`

---

## 3. Note_Type

- **Definition**: The purpose or category of the note.
- **Values**:
  - Retcon Tracker
  - Lore Inconsistency
  - Ambiguity Warning
  - Developer Commentary
  - Fan Interpretation Reference
  - Design Intent
  - Unresolved Narrative Hook

---

## 4. Note_Text

- **Definition**: The content of the note itself. Plain text, 1–4 sentence ideal length.
- **Examples**:
  - _Viego’s arc appears inconsistent with past depictions of Isolde’s agency in pre-2021 lore._
  - _Zilean’s presence across multiple events implies nonlinear continuity that has not been officially mapped._
  - _Character design hints at Void origin, though not confirmed narratively._
  - _Lore suggests betrayal, but champion VO contradicts emotional tone._

---

## 5. Source_Citation

- **Definition**: Optional field for referencing a patch note, developer blog, story, or interview.
- Examples:
  - Riot Dev Blog (April 2021)
  - _Ruination_ Novel, Chapter 6
  - Champion VO, Line 43

---

## 6. Status

- **Definition**: Whether the note is still relevant or outdated.
- Values:
  - Active
  - Resolved
  - Deprecated

---

## 7. Last_Updated

- **Definition**: Timestamp for when the note was last added or modified.
- Format: `YYYY-MM-DD`
