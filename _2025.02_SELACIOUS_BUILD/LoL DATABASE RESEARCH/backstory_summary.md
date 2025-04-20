```
backstory_summary {
  backstory_id integer pk increments unique
  champion_id integer > champion.champion_id
  backstory_text text
  origin_event varchar
  core_wound varchar
  narrative_trajectory varchar
  primary_motivation varchar
  emotional_tone varchar
  thematic_keywords text
  lore_timeline_position varchar
  canon_references text
  alternate_backstory_flag varchar
  narrative_integration_score integer
  codex_notes text
}
```

## 📘 Table of Contents

- [1. Summary_ID](#1_summary_id)
- [2. Champion_ID](#2_champion_id)
- [3. Summary_Text](#3_summary_text)
- [4. Origin_Event](#4_origin_event)
- [5. Core_Wound](#5_core_wound)
- [6. Narrative_Trajectory](#6_narrative_trajectory)
- [7. Primary_Motivation](#7_primary_motivation)
- [8. Emotional_Tone](#8_emotional_tone)
- [9. Thematic_Keywords](#9_thematic_keywords)
- [10. Lore_Timeline_Position](#10_lore_timeline_position)
- [11. Canon_References](#11_canon_references)
- [12. Alternate_Backstory_Flag](#12_alternate_backstory_flag)
- [13. Narrative_Integration_Score](#13_narrative_integration_score)
- [14. Codex_Notes](#14_codex_notes)

---

# **Narrative Asset Schema: Backstory_Summary**

---

## 1. Summary_ID

- **Definition**: Unique identifier for the backstory entry.
- **Examples**: `viego_backstory_01`, `ekko_core_lore`

---

## 2. Champion_ID

- **Definition**: Reference to the champion the backstory is associated with.
- **Example**: `viego`, `ekko`, `lissandra`

---

## 3. Summary_Text

- **Definition**: Condensed prose summary (1–3 sentences) of the champion's canonical backstory.
- **Constraints**: 1,000 character max preferred; lore-accurate, emotionally charged, mythically resonant.

---

## 4. Origin_Event

- **Definition**: The initial condition or inciting trauma in the character’s lore.
- **Examples**:
  - Death of a loved one
  - War-time betrayal
  - Magical experimentation
  - Divine encounter
  - Childhood exile

---

## 5. Core_Wound

- **Definition**: The emotional, psychological, or moral rupture that defines the character’s internal conflict.
- **Examples**:
  - Abandonment
  - Guilt
  - Obsession
  - Injustice
  - Loss of identity

---

## 6. Narrative_Trajectory

- **Definition**: How the champion's story has evolved over time.
- **Values**:
  - Linear Progression
  - Fall from Grace
  - Redemption Arc
  - Revenge Spiral
  - Stasis / Cyclical
  - Unknown / Fragmented

---

## 7. Primary_Motivation

- **Definition**: What drives the champion at present in the lore.
- **Examples**:
  - Avenge loved one
  - Protect homeland
  - Unlock forbidden knowledge
  - Prove self-worth
  - Restore balance
  - Achieve power

---

## 8. Emotional_Tone

- **Definition**: Dominant emotional or mythic tone of the backstory.
- **Values**:
  - Tragic
  - Heroic
  - Bittersweet
  - Ominous
  - Cathartic
  - Ambiguous
  - Comedic (rare)

---

## 9. Thematic_Keywords

- **Definition**: Tags that summarize key themes in the backstory.
- **Examples**:
  - Sacrifice
  - Madness
  - Betrayal
  - Hope
  - Legacy
  - Identity
  - Transformation

---

## 10. Lore_Timeline_Position

- **Definition**: Relative placement of the backstory within Runeterra’s historical timeline.
- **Values**:
  - Ancient Era
  - Rune Wars Era
  - Shuriman Empire
  - Modern Runeterra
  - Void Incursion Epoch
  - Timeless / Unknown

---

## 11. Canon_References

- **Definition**: Source materials used to build the backstory.
- **Structure**:
  - Title
  - Media Type (Short Story, Comic, Cinematic, Biography)
  - URL or Citation

---

## 12. Alternate_Backstory_Flag

- **Definition**: Indicates if the champion has a conflicting or alternate version in canon or AU.
- **Values**:
  - No
  - Yes – Alternate Universe (e.g., PROJECT, Star Guardian)
  - Yes – Lore Revision
  - Yes – Fragmented Canon

---

## 13. Narrative_Integration_Score

- **Definition**: How tightly the backstory integrates with other champions and events.
- **Scale**:
  - 5 = Deeply Integrated (e.g., Viego, Ryze)
  - 4 = Regionally Tied (e.g., Kayn, Rakan)
  - 3 = Factional Context
  - 2 = Isolated Arc
  - 1 = Vague / Ambiguous

---

## 14. Codex_Notes

- **Definition**: Internal commentary, inconsistencies, rewrites, or developer insights about the summary's evolution.

---
