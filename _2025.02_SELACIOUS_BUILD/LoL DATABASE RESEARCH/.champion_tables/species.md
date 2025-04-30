```
species {
  species_id integer pk increments unique
  species_name varchar
  classification_type varchar
  origin_source varchar
  typical_lifespan varchar
  known_abilities_or_traits text
  representative_champions text
  inter_species_hybrids varchar
  cultural_representation varchar
  weaknesses_or_limits varchar
  status_in_world varchar
  evolution_or_transformation_paths text
  canon_conflicts text
  species_crest_or_visual_iconography text
  skinline_alterations text
  cultural_aesthetic_and_inspirations text
  lore_sources text
  codex_notes text
}
```

## 📘 Table of Contents

- [1. Species_ID](#1_species_id)
- [2. Species_Name](#2_species_name)
- [3. Classification_Type](#3_classification_type)
- [4. Origin_Source](#4_origin_source)
- [5. Typical_Lifespan](#5_typical_lifespan)
- [6. Known_Abilities_or_Traits](#6_known_abilities_or_traits)
- [7. Representative_Champions](#7_representative_champions)
- [8. Inter-Species_Hybrids](#8_interspecies_hybrids)
- [9. Cultural_Representation](#9_cultural_representation)
- [10. Weaknesses_or_Limits](#10_weaknesses_or_limits)
- [11. Status_in_World](#11_status_in_world)
- [12. Evolution_or_Transformation_Paths](#12_evolution_or_transformation_paths)
- [13. Canon_Conflicts](#13_canon_conflicts)
- [14. Species_Crest_or_Visual_Iconography](#14_species_crest_or_visual_iconography)
- [15. Skinline_Alterations](#15_skinline_alterations)
- [16. Cultural_Aesthetic_and_Inspirations](#16_cultural_aesthetic_and_inspirations)
- [17. Lore_Sources](#17_lore_sources)
- [18. Codex_Notes](#18_codex_notes)

---

# **Narrative Asset Schema: Species**

---

## 1. Species_ID

- **Definition**: Unique identifier (slug or numeric) for each species.
- **Examples**: `human`, `vastaya`, `yordle`, `ascended`, `voidborn`

---

## 2. Species_Name

- **Definition**: Canonical species/race name.
- **Examples**: Human, Vastaya, Yordle, Darkin, Celestial, Spirit

---

## 3. Classification_Type

- **Definition**: Broad metaphysical or biological classification.
- **Values**:
  - Mortal
  - Magical Hybrid
  - Divine Entity
  - Construct / Artificial
  - Undead
  - Elemental
  - Cosmic / Celestial
  - Voidborn
  - Unknown

---

## 4. Origin_Source

- **Definition**: Narrative origin or mythos.
- **Examples**:
  - Evolutionary (Humans)
  - Magical Interbreeding (Vastaya)
  - Ascension Ritual (Ascended, Darkin)
  - Born from the Void (Voidborn)
  - Made by Celestials (Constructs like Galio)
  - Natural Manifestation (Elementals)

---

## 5. Typical_Lifespan

- **Definition**: Normal life expectancy or temporal state.
- **Values**:
  - Mortal (Normal Lifespan)
  - Extended (Centuries)
  - Immortal
  - Reincarnating
  - Unknown

---

## 6. Known_Abilities_or_Traits

- **Definition**: Inherent powers or physical/magical attributes typical of the species.
- **Examples**:
  - Magic Affinity
  - Shape-shifting
  - Enhanced Senses
  - Spiritual Possession
  - Cosmic Awareness
  - Immortality
  - Regeneration
  - Void Mutation

---

## 7. Representative_Champions

- **Definition**: Champions of this species.
- **Structure**:
  - Champion_ID
  - Name
  - Notes (e.g., “Half-Vastaya”, “Darkin Host”)

---

## 8. Inter-Species_Hybrids

- **Definition**: Whether the species can interbreed or fuse with others.
- **Values**:
  - Yes (Common or Rare)
  - No
  - Conditional (e.g., through ritual)
- **Notes**: Supports flags for mixed heritage (e.g., Kayn as human/Darkin host)

---

## 9. Cultural_Representation

- **Definition**: Societies or civilizations composed of this species.
- **Examples**:
  - Vastaya Tribes (Vastaya)
  - Shuriman Empire (Ascended)
  - Bandle City (Yordles)
  - Icathia / Void Cults (Voidborn)
  - Targonian Pantheon (Celestials)

---

## 10. Weaknesses_or_Limits

- **Definition**: Canonical vulnerabilities or existential limitations.
- **Examples**:
  - Can be corrupted (Ascended → Darkin)
  - Bound to magical laws (Yordles in spirit form)
  - Must inhabit host (Darkin)
  - Vulnerable to silver (Spirits / Superstitious types)

---

## 11. Status_in_World

- **Definition**: Narrative treatment or perception in Runeterra.
- **Values**:
  - Dominant / Widespread
  - Feared
  - Marginalized
  - Mythic / Forgotten
  - Extinct
  - Invasive / Threatening

---

## 12. Evolution_or_Transformation_Paths

- **Definition**: Known ways species evolve, ascend, fall, or transform.
- **Examples**:
  - Human → Ascended → Darkin
  - Vastaya → Ferality (if unbalanced)
  - Celestial → Host Manifestation
  - Voidborn → Assimilation Forms
  - Dead → Undead (Isles)

---

## 13. Canon_Conflicts

- **Definition**: Major lore-based species conflicts.
- **Examples**:
  - Voidborn vs. Shuriman Ascended
  - Yordles vs. Mortal Understanding
  - Humans vs. Darkin
  - Spirits vs. Shadow Magic

---

## 14. Species_Crest_or_Visual_Iconography

- **Definition**: Common visual markers, motifs, or symbols associated.
- **Examples**:
  - Yordles: Whimsical, soft features, glowing eyes
  - Darkin: Blood weapons, red-black themes
  - Celestials: Gold, blue, sun/moon symbology

---

## 15. Skinline_Alterations

- **Definition**: Notable alternate universes that redefine species.
- **Examples**:
  - Star Guardian Yordles (Celestial reinterpretation)
  - PROJECT Warwick (from Beast to Cybernetic)
  - High Noon Aatrox (Demon, not Darkin)

---

## 16. Cultural_Aesthetic_and_Inspirations

- **Definition**: Real-world mythological or literary sources inspiring the species.
- **Examples**:
  - Vastaya: East Asian mythology + animism
  - Darkin: Fallen angels + vampiric warlords
  - Yordles: Celtic fae + Western tricksters
  - Celestials: Greco-Roman gods + cosmic horror
  - Voidborn: Lovecraftian entities

---

## 17. Lore_Sources

- **Definition**: Canon stories or texts where the species is explored.
- **Structure**:
  - Title
  - Medium (Short Story, Comic, Cinematic)
  - URL / Reference

---

## 18. Codex_Notes

- **Definition**: Editorial commentary, dev insights, known contradictions.

---
