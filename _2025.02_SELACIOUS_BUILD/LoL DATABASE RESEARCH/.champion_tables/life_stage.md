```
life_stage {
  life_stage_id integer pk increments unique
  life_stage_label varchar
  biological_age_range varchar
  temporal_nature varchar
  physical_appearance_age varchar
  psychological_maturity varchar
  metaphysical_class varchar
  representative_champions text
  narrative_function varchar
  transformational_stages text
  cultural_perception varchar
  known_lifespan varchar
  time_distortion_flags varchar
  aesthetic_representation text
  cross_archetype_interaction text
  lore_sources text
  codex_notes text
}
```

## 📘 Table of Contents

- [1. Life_Stage_ID](#1_life_stage_id)
- [2. Life_Stage_Label](#2_life_stage_label)
- [3. Biological_Age_Range](#3_biological_age_range)
- [4. Temporal_Nature](#4_temporal_nature)
- [5. Physical_Appearance_Age](#5_physical_appearance_age)
- [6. Psychological_Maturity](#6_psychological_maturity)
- [7. Metaphysical_Class](#7_metaphysical_class)
- [8. Representative_Champions](#8_representative_champions)
- [9. Narrative_Function](#9_narrative_function)
- [10. Transformational_Stages](#10_transformational_stages)
- [11. Cultural_Perception](#11_cultural_perception)
- [12. Known_Lifespan](#12_known_lifespan)
- [13. Time_Distortion_Flags](#13_time_distortion_flags)
- [14. Aesthetic_Representation](#14_aesthetic_representation)
- [15. Cross-Archetype_Interaction](#15_crossarchetype_interaction)
- [16. Lore_Sources](#16_lore_sources)
- [17. Codex_Notes](#17_codex_notes)

---

# **Narrative Asset Schema: Life_Stage**

---

## 1. Life_Stage_ID

- **Definition**: Unique identifier (slug or numeric) for the life stage classification.
- **Examples**: `adolescent`, `immortal`, `post_mortal`

---

## 2. Life_Stage_Label

- **Definition**: Canonical label for the life stage.
- **Examples**: Child, Adolescent, Adult, Elder, Immortal

---

## 3. Biological_Age_Range

- **Definition**: Approximate physical age range in human years (if applicable).
- **Structure**:
  - Min_Age
  - Max_Age
  - Notes (if non-human, metaphysical, or unknown)

---

## 4. Temporal_Nature

- **Definition**: Describes the character’s temporal state.
- **Values**:
  - Mortal
  - Extended
  - Immortal
  - Undead
  - Reincarnating
  - Frozen (Time-stasis)
  - Artificial / Constructed
  - Unknown

---

## 5. Physical_Appearance_Age

- **Definition**: Visual/physical age as presented in the game and lore.
- **Values**:
  - Childlike
  - Teen/Youth
  - Prime Adult
  - Aged
  - Ageless

---

## 6. Psychological_Maturity

- **Definition**: Narrative age in terms of wisdom, behavior, and social cognition.
- **Values**:
  - Naïve
  - Curious
  - Rebellious
  - Hardened
  - Enlightened
  - Jaded
  - Childlike but Ancient (e.g., Yordles)

---

## 7. Metaphysical_Class

- **Definition**: Lifespan-affecting metaphysical condition.
- **Values**:
  - Ascended
  - Celestial
  - Undead
  - Void-corrupted
  - Host-bound
  - Spirit-Form
  - Construct (Golem, AI)
  - None

---

## 8. Representative_Champions

- **Definition**: Champions who exemplify this life stage.
- **Structure**:
  - Champion_ID
  - Name
  - Notes (e.g., "Centuries old but looks 20")

---

## 9. Narrative_Function

- **Definition**: Thematic or plot role often filled by this life stage.
- **Values**:
  - Innocent Catalyst
  - Coming-of-Age Protagonist
  - Reluctant Leader
  - Ancient Mentor
  - Undying Tyrant
  - Tragic Immortal
  - Forgotten Relic

---

## 10. Transformational_Stages

- **Definition**: Whether the life stage is transitional in the champion’s arc.
- **Structure**:
  - From → To
  - Trigger (e.g., Ascension, Curse, Death, Betrayal)

---

## 11. Cultural_Perception

- **Definition**: How this life stage is treated in-world by others.
- **Examples**:
  - Revered Elder
  - Feared Undead
  - Marginalized Youth
  - Mythic Immortal
  - Enslaved Construct

---

## 12. Known_Lifespan

- **Definition**: Expected duration of life.
- **Values**:
  - 0–30 years
  - 30–80 years
  - 80–300 years
  - 300+ years
  - Infinite / Unmeasurable
  - Unknown

---

## 13. Time_Distortion_Flags

- **Definition**: Indicates unique time experiences or time manipulation.
- **Values**:
  - Chrono-Affected (e.g., Ekko)
  - Immortality-by-Stasis (e.g., Zilean)
  - Time Loop / Repeating Life
  - Temporally Anchored
  - N/A

---

## 14. Aesthetic_Representation

- **Definition**: Visual and stylistic motifs used to convey the life stage.
- **Examples**:
  - Glowing Eyes, Silver Hair (Ancient)
  - Playful Voice and Small Size (Childlike)
  - Battle Scars and Armor (Aged Warrior)
  - Ethereal Transparency (Undead/Spirit)

---

## 15. Cross-Archetype_Interaction

- **Definition**: Common combinations of life stage with narrative archetypes.
- **Examples**:
  - Adolescent → Rebel / Trickster
  - Elder → Sage / Guardian
  - Immortal → Tyrant / Tragic Hero
  - Artificial → Monster / Catalyst

---

## 16. Lore_Sources

- **Definition**: Canonical sources discussing lifespan or age.
- **Structure**:
  - Title
  - Medium (Short Story, Voice Line, Cinematic)
  - URL / Citation

---

## 17. Codex_Notes

- **Definition**: Notes on narrative ambiguity, retcons, or visual inconsistencies.

---
