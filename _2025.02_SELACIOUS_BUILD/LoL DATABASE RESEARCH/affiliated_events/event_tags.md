## 📘 Table of Contents

- [1. Event_Tag_ID](#1_event_tag_id)
- [2. Tag_Label](#2_tag_label)
- [3. Tag_Type](#3_tag_type)
- [4. Tag_Description](#4_tag_description)
- [5. Common_Associated_Champions](#5_common_associated_champions)
- [6. Common_Associated_Regions](#6_common_associated_regions)
- [7. Example_Events](#7_example_events)
- [8. Cross_Tag_Interactions](#8_cross_tag_interactions)
- [9. Usage_Notes](#9_usage_notes)

---
# **Narrative Asset Schema: Event_Tags**

---

## 1. Event_Tag_ID

- **Definition**: Unique identifier (slug or numeric) for the tag entry.
- **Examples**: `ruination`, `ascension`, `civil_war`, `cosmic_cataclysm`

---

## 2. Tag_Label

- **Definition**: Readable label used for classification.
- **Examples**:
  - War
  - Betrayal
  - Ascension
  - Ruination
  - Civil Conflict
  - Void Incursion
  - Magic Unleashed
  - Rebellion
  - Divine Judgment
  - Technological Disaster

---

## 3. Tag_Type

- **Definition**: Broad category of the tag for sorting and filtering.
- **Values**:
  - Narrative Theme
  - Magical Mechanic
  - Political Structure
  - Mythic Pattern
  - World-State Shift
  - Symbolic Motif
  - Factional / Regional

---

## 4. Tag_Description

- **Definition**: Short explanation of what the tag captures in narrative or symbolic terms.
- **Examples**:
  - **Ruination** → Massive soul-corrupting magical event tied to the fall of Viego.
  - **Ascension** → Transformation into a godlike being through ancient Shuriman rituals.

---

## 5. Common_Associated_Champions

- **Definition**: Champions frequently linked to this event type.
- Structure:
  - Champion_ID
  - Relevance: (Primary / Secondary / Opposed)

---

## 6. Common_Associated_Regions

- **Definition**: Regions or cultures tied to this kind of event.
- Examples:
  - **Ascension** → Shurima
  - **Void Incursion** → Ixtal, Freljord
  - **Technological Disaster** → Zaun

---

## 7. Example_Events

- **Definition**: Notable events where this tag applies.
- Structure:
  - Event_Name
  - Event_ID
  - Year / Era (if known)

---

## 8. Cross_Tag_Interactions

- **Definition**: Tags that frequently overlap or combine.
- Examples:
  - **Betrayal + War**
  - **Void Incursion + Cosmic Horror**
  - **Rebellion + Civil Conflict**

---

## 9. Usage_Notes

- **Definition**: Clarification of edge cases, deprecated terms, or lore-wide applications.
