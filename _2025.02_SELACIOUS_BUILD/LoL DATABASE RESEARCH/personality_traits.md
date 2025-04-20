```

personality_traits {
  ptrait_id integer pk increments unique
  ptrait_name varchar
  ptrait_type varchar
  psychological_dimension varchar
  ptrait_intensity varchar
  expression_mode text
  associated_champions text
  ptrait_archetype_mapping text
  ptrait_duality_relations text
  ptrait_evolution_pathways text
  narrative_function varchar
  real_world_psych_tie text
  expression_quotes text
  ptrait_contextualization text
  ptrait_symbolism text
  ptrait_frequency varchar
  ptrait_impact_score integer
  codex_notes text
}



```

## 📘 Table of Contents

- [1. Trait_ID](#1_trait_id)
- [2. Trait_Name](#2_trait_name)
- [3. Trait_Type](#3_trait_type)
- [4. Psychological_Dimension](#4_psychological_dimension)
- [5. Trait_Intensity](#5_trait_intensity)
- [6. Expression_Mode](#6_expression_mode)
- [7. Associated_Champions](#7_associated_champions)
- [8. Trait_Archetype_Mapping](#8_trait_archetype_mapping)
- [9. Duality_Relations](#9_duality_relations)
- [10. Evolution_Pathways](#10_evolution_pathways)
- [11. Narrative_Function](#11_narrative_function)
- [12. Real_World_Psych_Tie](#12_real_world_psych_tie)
- [13. Expression_Quotes](#13_expression_quotes)
- [14. Trait_Contextualization](#14_trait_contextualization)
- [15. Trait_Symbolism](#15_trait_symbolism)
- [16. Trait_Frequency](#16_trait_frequency)
- [17. Trait_Impact_Score](#17_trait_impact_score)
- [18. Codex_Notes](#18_codex_notes)

---

# **Narrative Asset Schema: Personality_Traits**

---

## 1. Trait_ID

- **Definition**: Unique identifier (slug or numeric) for the personality trait.
- **Examples**: `stoic`, `vengeful`, `manic`, `arrogant`

---

## 2. Trait_Name

- **Definition**: Canonical name of the trait.
- **Examples**: Stoic, Vengeful, Curious, Arrogant

---

## 3. Trait_Type

- **Definition**: Role of the trait in the character's psychological makeup.
- **Values**:
  - Virtue
  - Flaw
  - Dual / Contextual
  - Mask (performative trait, not core)
  - Core (primary defining trait)

---

## 4. Psychological_Dimension

- **Definition**: High-level psychological category for trait grouping.
- **Values**:
  - Emotional Regulation (e.g., Stoic, Impulsive)
  - Cognitive Style (e.g., Cunning, Idealistic)
  - Social Style (e.g., Charming, Withdrawn)
  - Moral Orientation (e.g., Dutiful, Ruthless)
  - Stability Axis (e.g., Manic, Controlled)
  - Identity Structure (e.g., Conflicted, Narcissistic)

---

## 5. Trait_Intensity

- **Definition**: Level of behavioral dominance.
- **Values**:
  - Subtle
  - Moderate
  - Dominant
  - Extreme / Unstable

---

## 6. Expression_Mode

- **Definition**: How the trait is expressed in behavior or narrative.
- **Examples**:
  - Spoken Dialogue (e.g., passive-aggressive, stoic one-liners)
  - Combat Style (e.g., reckless initiator, patient sniper)
  - Moral Decisions (e.g., mercy vs ruthlessness)
  - Relationship Dynamics (e.g., codependent, distant)
  - Visual Cues (e.g., posture, expressions, attire)

---

## 7. Associated_Champions

- **Definition**: Champions strongly defined by this trait.
- **Structure**:
  - Champion_ID
  - Name
  - Role of Trait (Core / Mask / Emerging)

---

## 8. Trait_Archetype_Mapping

- **Definition**: Mapping of the trait to narrative archetypes.
- **Examples**:
  - Stoic → Guardian / Mentor
  - Vengeful → Antihero / Fallen Hero
  - Charming → Trickster
  - Curious → Explorer / Catalyst
  - Zealous → Cultist / Paladin

---

## 9. Duality_Relations

- **Definition**: Natural opposites or conflicted pairings.
- **Structure**:
  - Trait_ID
  - Relationship_Type:
    - Opposed
    - Complementary
    - Masked_By
    - Evolves_Into

---

## 10. Evolution_Pathways

- **Definition**: How the trait can change over a character arc.
- **Structure**:
  - From → To
  - Conditions (e.g., trauma, redemption, betrayal)

---

## 11. Narrative_Function

- **Definition**: What purpose the trait serves in the story.
- **Values**:
  - Tension Generator
  - Relatability Vector
  - Moral Contrast
  - Psychological Depth
  - Catalyst for Change
  - Character Flaw Anchor
  - Comic Relief

---

## 12. Real_World_Psych_Tie

- **Definition**: Correspondence to psychological models.
- **Examples**:
  - Big Five: (e.g., High Neuroticism, Low Agreeableness)
  - MBTI: (e.g., INTJ, ESFP)
  - Enneagram: (e.g., Type 1 Reformer, Type 8 Challenger)
  - Clinical Axis (e.g., Borderline Traits, Narcissism, OCD)

---

## 13. Expression_Quotes

- **Definition**: Canonical quotes or voice lines that reflect the trait.
- **Structure**:
  - Champion_ID
  - Quote
  - Trait_Expressed

---

## 14. Trait_Contextualization

- **Definition**: When/why the trait emerges in canon.
- **Examples**:
  - Garen’s stoicism in battle, but softness around Lux.
  - Jhin’s calm demeanor only breaks when his art fails.
  - Ekko’s curiosity manifests as invention and rebellion.

---

## 15. Trait_Symbolism

- **Definition**: Iconic visuals or motifs tied to the trait.
- **Examples**:
  - Stoic → Stone / Armor / Silence
  - Vengeful → Fire / Chains / Red
  - Curious → Gears / Books / Glowing Eyes
  - Manic → Broken masks / laughter / volatility

---

## 16. Trait_Frequency

- **Definition**: How common the trait is across champions.
- **Values**:
  - Rare
  - Occasional
  - Common
  - Ubiquitous

---

## 17. Trait_Impact_Score

- **Definition**: Narrative weight or influence of this trait in lore arcs.
- **Scale**: 1 (Minor Flavor) to 5 (Arc-Defining)

---

## 18. Codex_Notes

- **Definition**: Notes on usage, contradictions, character dev commentary, or trope subversion.

---
