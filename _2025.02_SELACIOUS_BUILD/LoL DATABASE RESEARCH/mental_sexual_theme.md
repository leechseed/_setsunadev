```
mental_sexual_theme {
  mental_sexual_theme_id integer pk increments unique
  label varchar
  erotic_psychological_drive text
  core_tension text
  cognitive_patterns text
  narrative_symptoms text
  fantasy_form text
  shame_eroticism_curve varchar
  repression_level varchar
  object_of_fixation text
  psychic_myth text
  symbolic_language_cues text
  associated_archetypes text
  media_evidence text
  edge_case_flags text
  codex_notes text
}
```

## 📘 Table of Contents

- [1. Mental_Sexual_Theme_ID](#1_mental_sexual_theme_id)
- [2. Label](#2_label)
- [3. Erotic_Psychological_Drive](#3_erotic_psychological_drive)
- [4. Core_Tension](#4_core_tension)
- [5. Cognitive_Patterns](#5_cognitive_patterns)
- [6. Narrative_Symptoms](#6_narrative_symptoms)
- [7. Fantasy_Form](#7_fantasy_form)
- [8. Shame_Eroticism_Curve](#8_shame_eroticism_curve)
- [9. Repression_Level](#9_repression_level)
- [10. Object_of_Fixation](#10_object_of_fixation)
- [11. Psychic_Myth](#11_psychic_myth)
- [12. Symbolic_Language_Cues](#12_symbolic_language_cues)
- [13. Associated_Archetypes](#13_associated_archetypes)
- [14. Media_Evidence](#14_media_evidence)
- [15. Edge_Case_Flags](#15_edge_case_flags)
- [16. Codex_Notes](#16_codex_notes)

---

# **Narrative Asset Schema: Mental_Sexual_Theme**

---

## 1. Mental_Sexual_Theme_ID

- **Definition**: Unique identifier for the internal sexual psychology theme.
- **Examples**: `obsessive_loyalty`, `unreachable_love`, `divine_shame`, `masochist_saint`

---

## 2. Label

- **Definition**: Short evocative name that captures the core psychological erotic structure.
- **Examples**:
  - Obsessive Loyalty
  - Sacred Shame
  - Lust-As-Violence
  - Forbidden Nurture
  - Erotic Nullification
  - Worship-Addicted
  - Love-Hungry Tyrant
  - Masochist Saint
  - Control-As-Love
  - Chaste Fixation

---

## 3. Erotic_Psychological_Drive

- **Definition**: The character’s deepest sexualized compulsion, fear, or longing.
- **Examples**:
  - Need to be punished to feel love
  - Fear of losing control in intimacy
  - Obsession with being possessed or dominated
  - Worship of a forbidden figure or concept
  - Erotic awe toward purity or shame

---

## 4. Core_Tension

- **Definition**: The central contradiction or psychic wound that defines their erotic identity.
- Examples:
  - Desire vs. Control
  - Guilt vs. Pleasure
  - Abandonment vs. Obsession
  - Power vs. Exposure
  - Carnality vs. Innocence

---

## 5. Cognitive_Patterns

- **Definition**: Mental behaviors, fantasies, or triggers that show up in speech or behavior.
- Examples:
  - Self-effacement in front of dominant figures
  - Flirtation with annihilation or martyrdom
  - Projection of erotic thoughts onto enemies or victims
  - Constant mental tally of one’s worth to others
  - Internal monologues about being unclean, unworthy, or holy

---

## 6. Narrative_Symptoms

- **Definition**: Plot behaviors that reflect internal sexual distortion or desire.
- Values:
  - Jealousy
  - Ritualistic Behavior
  - Suicidal Affection
  - Self-Sabotage
  - Romantic Stalking
  - Seductive Violence
  - Erotic Projection
  - Apathy toward all but the Beloved
  - Bondage to an Ideal

---

## 7. Fantasy_Form

- **Definition**: The internal mental fantasy that structures their sexual worldview.
- Examples:
  - “If I serve them perfectly, they’ll love me.”
  - “If I’m destroyed, I’ll be clean.”
  - “I must never be touched.”
  - “I am a temple, not a person.”
  - “If I conquer them, they will become mine.”

---

## 8. Shame_Eroticism_Curve

- **Definition**: How shame or guilt interacts with arousal internally.
- Values:
  - Shame Amplifies Desire
  - Shame Represses Desire
  - Shame Replaces Desire
  - Shame Is Absent
  - Shame Is Weaponized (projected onto others)

---

## 9. Repression_Level

- **Definition**: How conscious or unconscious the mental sexual theme is.
- Values:
  - Fully Repressed (e.g., manifesting as aggression or denial)
  - Semi-Conscious (rationalized or displaced)
  - Fully Aware but Unspoken
  - Actively Performed / Embraced
  - Fragmented (dissociative, unstable)

---

## 10. Object_of_Fixation

- **Definition**: The external concept, figure, or entity onto which erotic cognition is mapped.
- Examples:
  - One specific person
  - A symbolic ideal (e.g., purity, ruin, fire, God)
  - A phantom from their past
  - A power structure (e.g., military command)
  - No external object (pure internal hunger)

---

## 11. Psychic_Myth

- **Definition**: Mythological or symbolic narrative that governs their erotic psychology.
- Examples:
  - Narcissus (Self-love)
  - Orpheus (Loving the dead)
  - Psyche (Faith in the unknown lover)
  - The Martyr (Love equals pain)
  - The Siren (They must be desired but never touched)

---

## 12. Symbolic_Language_Cues

- **Definition**: Phrases, metaphors, or symbols they use in VO/lore that reveal their internal sexual dynamic.
- Examples:
  - “I am yours, even in ruin.”
  - “Let me bleed for your will.”
  - “Touch me and see the storm.”
  - “They worshipped me once… they’ll worship again.”

---

## 13. Associated_Archetypes

- **Definition**: Links to their Sexual_Archetype and Visual_Sexual_Theme, showing how the mental aspect connects.
- Structure:
  - Sexual_Archetype_Label
  - Visual_Sexual_Theme_Label
  - Harmony or Dissonance (e.g., “Externally Dominant, Internally Submissive”)

---

## 14. Media_Evidence

- **Definition**: Voice lines, short stories, cinematics, or skinlines that portray this mental sexual theme.
- Structure:
  - Media_Title
  - Medium_Type (VO, Short Story, Skinline)
  - Notes on tone or content

---

## 15. Edge_Case_Flags

- **Definition**: Ambiguities, contradictions, or contested interpretations in fan or dev canon.
- Examples:
  - Subtextual only
  - Soft-retconned over time
  - Tone shift in recent patches
  - Conflicting portrayals across skins

---

## 16. Codex_Notes

- **Definition**: Optional commentary for analysis, dev intent, queer/feminist/psychoanalytic framing, or ongoing fan interpretation.
