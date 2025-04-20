```
narrative_archetype {
  archetype_id integer pk increments unique
  archetype_name varchar
  structural_function varchar
  moral_alignment varchar
  core_motivation varchar
  character_traits text
  associated_champions text
  transformation_potential text
  shadow_archetype varchar
  classical_correspondence text
  narrative_themes text
  common_symbols text
}
```

## 📘 Table of Contents

- [1. Archetype_ID](#1_archetype_id)
- [2. Archetype_Name](#2_archetype_name)
- [3. Structural_Function](#3_structural_function)
- [4. Moral_Alignment](#4_moral_alignment)
- [5. Core_Motivation](#5_core_motivation)
- [6. Character_Traits](#6_character_traits)
- [7. Associated_Champions](#7_associated_champions)
- [8. Transformation_Potential](#8_transformation_potential)
- [9. Shadow_Archetype](#9_shadow_archetype)
- [10. Classical_Correspondence](#10_classical_correspondence)
- [11. Narrative_Themes](#11_narrative_themes)
- [12. Common_Symbols](#12_common_symbols)

---

# **Narrative Asset Schema: Narrative_Archetype**

---

## 1. Archetype_ID

- **Definition**: Unique identifier (slug or numeric) for the archetype.
- **Examples**: `hero`, `trickster`, `fallen_hero`

---

## 2. Archetype_Name

- **Definition**: Canonical name of the archetype.
- **Examples**: Hero, Antihero, Trickster, Monster

---

## 3. Structural_Function

- **Definition**: Role in narrative structure based on classical or modern theory (e.g. Campbell, Propp, Vogler).
- **Values**:
  - Protagonist
  - Antagonist
  - Deuteragonist
  - Foil
  - Mentor
  - Catalyst
  - Shadow Self
  - Threshold Guardian
  - Tempter / Disruptor
  - Audience Surrogate

---

## 4. Moral_Alignment

- **Definition**: Ethical positioning across narrative functions.
- **Values**:
  - Heroic
  - Ambiguous
  - Villainous
  - Chaotic
  - Redeemable
  - Corrupted
  - Unknowable

---

## 5. Core_Motivation

- **Definition**: Primary goal or drive as defined by narrative need.
- **Examples**:
  - Justice
  - Revenge
  - Chaos
  - Self-Discovery
  - Power
  - Protection
  - Escape
  - Knowledge
  - Restoration

---

## 6. Character_Traits

- **Definition**: Dominant characteristics usually expressed by this archetype.
- **Structure**:
  - Trait (e.g., Noble, Arrogant, Cunning)
  - Trait_Type: (Virtue / Flaw / Dual)

---

## 7. Associated_Champions

- **Definition**: Champions who embody this archetype.
- **Structure**:
  - Champion_ID
  - Name
  - Notes (e.g., “Early Arc”, “Post-Ruination”)

---

## 8. Transformation_Potential

- **Definition**: Common narrative arc or transition paths.
- **Structure**:
  - From → To
  - Example Champion
- **Examples**:
  - Hero → Fallen Hero (e.g., Viego)
  - Villain → Redeemed (e.g., Rengar [partial])
  - Trickster → Mentor (e.g., Ekko [in Arcane])

---

## 9. Shadow_Archetype

- **Definition**: Inverse or corrupted mirror archetype.
- **Examples**:
  - Hero → Tyrant
  - Sage → Manipulator
  - Trickster → Saboteur

---

## 10. Classical_Correspondence

- **Definition**: Link to historical/mythological figures or literary archetypes.
- **Examples**:
  - Hercules → Hero
  - Loki → Trickster
  - Oedipus → Tragic Hero
  - Icarus → Hubristic Challenger
  - Athena → Wise Mentor
  - Dracula → Monster

---

## 11. Narrative_Themes

- **Definition**: Themes typically explored through this archetype.
- **Examples**:
  - Redemption
  - Hubris
  - Power and Corruption
  - Sacrifice
  - Identity
  - Duality
  - Fate vs Free Will

---

## 12. Common_Symbols

- **Definition**: Visual or symbolic motifs attached to the archetype.
- **Examples**:
  - Sword (Hero)
  - Mask (Trickster)
  - Chains (Fallen Hero)
  - Flame (Rebel
