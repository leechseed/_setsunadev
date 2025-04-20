## 📘 Table of Contents

- [1. Media_Appearance_ID](#1_media_appearance_id)
- [2. Title](#2_title)
- [3. Media_Type](#3_media_type)
- [4. Champion_or_Event_ID](#4_champion_or_event_id)
- [5. Role_in_Media](#5_role_in_media)
- [6. Canon_Status](#6_canon_status)
- [7. Timeline_Position](#7_timeline_position)
- [8. Narrative_Impact](#8_narrative_impact)
- [9. Notable_Scenes_or_Quotes](#9_notable_scenes_or_quotes)
- [10. Notes](#10_notes)

---
# **Narrative Asset Schema: Media_Appearance**

---

## 1. Media_Appearance_ID

- **Definition**: Unique identifier (slug or numeric) for the media appearance entry.
- **Examples**: `arcane_s1_vi`, `ruination_cinematic_viego`, `lor_card_darius`

---

## 2. Title

- **Definition**: Official title of the media where the champion or event appears.
- **Examples**:
  - Arcane
  - Ruination
  - Kin of the Stag
  - Before Glory
  - Awakening (Cinematic)
  - Legends of Runeterra

---

## 3. Media_Type

- **Definition**: Type of content.
- **Values**:
  - Animated Series
  - Cinematic
  - Short Story
  - Comic
  - Novel
  - Digital Card Game
  - Dev Blog / Concept Artbook

---

## 4. Champion_or_Event_ID

- **Definition**: The associated champion or event.
- Structure:
  - Champion_ID or Event_ID (reusable for both contexts)

---

## 5. Role_in_Media

- **Definition**: Narrative role or focus level.
- Values:
  - Main Character
  - Supporting Role
  - Antagonist
  - Minor / Cameo
  - Visual Only / Background
  - Flashback / Referenced

---

## 6. Canon_Status

- **Definition**: Whether this media is recognized in official lore.
- Values:
  - Core Canon
  - Semi-Canon
  - Alternate Universe
  - Stylized / Promotional Only

---

## 7. Timeline_Position

- **Definition**: When this media takes place in the narrative timeline (if applicable).
- Examples:
  - Pre-Ruination
  - Arcane Conflict Era
  - Post-Ruination
  - Unknown / AU

---

## 8. Narrative_Impact

- **Definition**: Whether this appearance expands, redefines, or reinforces lore.
- Values:
  - Expands Lore
  - Retells Existing Lore
  - Contradicts Core Canon
  - Adds Flavor Only
  - Unknown

---

## 9. Notable_Scenes_or_Quotes

- **Definition**: Memorable lore beats, quotes, or turning points involving the champion or event.
- Examples:
  - Vi & Powder fight (Arcane)
  - Viego’s corruption spread (Ruination cinematic)

---

## 10. Notes

- **Definition**: Commentary on performance, retcons, dev confirmations, or community interpretation.
