```
region_of_origin {
  region_id integer pk increments unique
  region_name varchar
  government_type varchar
  dominant_political_ideology varchar
  geographic_features varchar
  magical_orientation varchar
  founding_myth_or_legend text
  key_figures text
  core_factions varchar
  cultural_aesthetic varchar
  religion_or_spirituality varchar
  known_conflicts varchar
  champions_associated text
  related_events varchar
  interregional_relationships text
  narrative_themes varchar
  subregions_or_cities text
  visual_iconography text
  associated_skinlines varchar
  codex_notes text
}
```

## 📘 Table of Contents

- [1. Region_ID](#1_region_id)
- [2. Region_Name](#2_region_name)
- [3. Government_Type](#3_government_type)
- [4. Dominant_Political_Ideology](#4_dominant_political_ideology)
- [5. Geographic_Features](#5_geographic_features)
- [6. Magical_Orientation](#6_magical_orientation)
- [7. Founding_Myth_or_Legend](#7_founding_myth_or_legend)
- [8. Key_Figures](#8_key_figures)
- [9. Core_Factions](#9_core_factions)
- [10. Cultural_Aesthetic](#10_cultural_aesthetic)
- [11. Religion_or_Spirituality](#11_religion_or_spirituality)
- [12. Known_Conflicts](#12_known_conflicts)
- [13. Champions_Associated](#13_champions_associated)
- [14. Related_Events](#14_related_events)
- [15. Interregional_Relationships](#15_interregional_relationships)
- [16. Narrative_Themes](#16_narrative_themes)
- [17. Subregions_or_Cities](#17_subregions_or_cities)
- [18. Visual_Iconography](#18_visual_iconography)
- [19. Associated_Skinlines](#19_associated_skinlines)
- [20. Codex_Notes](#20_codex_notes)

---

# **Narrative Asset Schema: Region_of_Origin**

---

## 1. Region_ID

- **Definition**: Unique identifier (slug or numeric) for each region.
- **Example**: `demacia`, `noxus`, `ionia`

---

## 2. Region_Name

- **Definition**: Canonical name of the region.
- **Examples**: Demacia, Noxus, Shurima

---

## 3. Government_Type

- **Definition**: Form of governance or power structure.
- **Values**:
  - Monarchy
  - Magocracy
  - Military Junta
  - Tribal Confederation
  - Theocracy
  - Anarchy
  - Council Rule
  - Colonial Power
  - Technocracy

---

## 4. Dominant_Political_Ideology

- **Definition**: Core philosophy or political framework.
- **Examples**:
  - Honor & Order (Demacia)
  - Expansionist Imperialism (Noxus)
  - Balance & Harmony (Ionia)
  - Technological Innovation (Piltover)
  - Survival of the Fittest (Void)

---

## 5. Geographic_Features

- **Definition**: Primary biome/environmental traits.
- **Examples**:
  - Mountainous Highlands
  - Frozen Tundra
  - Desert Wastes
  - Jungles & Forests
  - Coastal / Island Chains
  - Urban Megacity
  - Floating Celestial Realms

---

## 6. Magical_Orientation

- **Definition**: Relationship to or use of magic.
- **Values**:
  - Magic-Rejecting
  - Magic-Infused
  - Technomagic Hybrid
  - Forbidden/Corrupted Magic
  - Natural/Spiritual Magic

---

## 7. Founding_Myth_or_Legend

- **Definition**: Origin story or foundational legend of the region.
- **Format**: Text summary or linked reference to lore database.

---

## 8. Key_Figures

- **Definition**: Influential historical or mythic people tied to the region.
- **Structure**:
  - Name
  - Role/Title
  - Status (Alive / Dead / Deified / Unknown)

---

## 9. Core_Factions

- **Definition**: Major in-universe organizations based in the region.
- **Examples**:
  - Dauntless Vanguard (Demacia)
  - Black Rose (Noxus)
  - Kinkou Order (Ionia)
  - Chem-Barons (Zaun)
  - Ascended Host (Shurima)

---

## 10. Cultural_Aesthetic

- **Definition**: Thematic or visual design influence of the region.
- **Examples**:
  - Feudal European
  - Roman Imperial
  - High Fantasy Nature
  - Cyber-Victorian
  - Mesoamerican
  - Apocalyptic / Gothic Horror

---

## 11. Religion_or_Spirituality

- **Definition**: Dominant beliefs or mythos systems.
- **Examples**:
  - Solari / Lunari (Targon)
  - Spirit Worship (Ionia)
  - Ascension Cult (Shurima)
  - Void Cultism (Icathia)
  - No Official Religion (Piltover)

---

## 12. Known_Conflicts

- **Definition**: Historical or ongoing major wars or political upheavals.
- **Examples**:
  - Freljord Civil War
  - Demacia vs Noxus
  - Piltover-Zaun Tensions
  - Void Incursions

---

## 13. Champions_Associated

- **Definition**: List of champions originally from or narratively tied to the region.
- **Structure**:
  - Champion_ID
  - Name
  - Role in Region (e.g. General, Rebel, Exile)

---

## 14. Related_Events

- **Definition**: Major lore events, stories, or arcs occurring in the region.
- **Examples**:
  - The Ruination
  - Arcane Conflict
  - Icathian Cataclysm
  - Shuriman Ascension

---

## 15. Interregional_Relationships

- **Definition**: Political and narrative connections to other regions.
- **Structure**:
  - Target Region
  - Relationship Type: (Allied / Enemy / Colonized / Rival / Neutral / Trade Partner)

---

## 16. Narrative_Themes

- **Definition**: Key motifs or philosophical themes represented.
- **Examples**:
  - Honor vs Pragmatism
  - Isolation vs Unity
  - Legacy vs Revolution
  - Nature vs Industry
  - Order vs Chaos

---

## 17. Subregions_or_Cities

- **Definition**: Important named locations within the region.
- **Examples**:
  - **Demacia**: High Silvermere, Uwendale
  - **Noxus**: Immortal Bastion, Basilich
  - **Piltover**: The Academy, Entresol
  - **Zaun**: The Sump, The Entresol
  - **Shurima**: Nashramae, Nerimazeth

---

## 18. Visual_Iconography

- **Definition**: Key symbols, crests, and color schemes.
- **Structure**:
  - Flag / Sigil Description
  - Common Colors
  - Iconic Motifs (e.g. swords, gears, suns, feathers)

---

## 19. Associated_Skinlines

- **Definition**: Skins whose narrative is _tied_ to the regional identity or AU representations.
- **Examples**:
  - High Noon (Wild West version of the Freljord/Southwest)
  - Battle Academia (Piltover-as-Academy)
  - PROJECT (Zaun / Piltover Cyberpunk)

---

## 20. Codex_Notes

- **Definition**: External links or references to extended lore, including short stories, comics, cinematic scripts, or developer notes.

---
