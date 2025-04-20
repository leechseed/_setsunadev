```
cultural_influence {
  cultural_influence_id integer pk increments unique
  cultural_label varchar
  influence_type varchar
  aesthetic_signals text
  mythological_parallels text
  region_association varchar
  champion_examples text
  layer_type varchar
  combined_with text
  notes text
}
```

## 📘 Table of Contents

- [1. Cultural_Influence_ID](#1_cultural_influence_id)
- [2. Cultural_Label](#2_cultural_label)
- [3. Influence_Type](#3_influence_type)
- [4. Aesthetic_Signals](#4_aesthetic_signals)
- [5. Mythological_Parallels](#5_mythological_parallels)
- [6. Region_Association](#6_region_association)
- [7. Champion_Examples](#7_champion_examples)
- [8. Layer_Type](#8_layer_type)
- [9. Combined_With](#9_combined_with)
- [10. Notes](#10_notes)

---

# **Narrative Asset Schema: Cultural_Influence**

---

## 1. Cultural_Influence_ID

- Unique identifier for the cultural influence (e.g. `greco_roman`, `feudal_japan`)

## 2. Cultural_Label

- Clear name of the real-world culture or blend.
- Examples:
  - Feudal Japan
  - Ancient Egypt
  - Norse Mythology
  - Gothic Europe
  - Slavic Paganism
  - Afro-futurism

## 3. Influence_Type

- What aspect of the champion or region it affects:
  - Visual Design
  - Narrative Motif
  - Combat Style
  - Philosophical Theme
  - Religious Structure
  - Social Hierarchy

## 4. Aesthetic_Signals

- Common visual cues taken from the source culture:
  - Robes, armor styles, animal symbols, weapons, color palettes, architecture

## 5. Mythological_Parallels

- Gods, stories, rituals, or concepts echoed in the champion or region.

## 6. Region_Association

- The in-world region most aligned with the influence.
  - Examples:
    - Targon ↔ Greco-Roman
    - Ionia ↔ East Asian
    - Shurima ↔ Ancient Mesopotamian + Egyptian

## 7. Champion_Examples

- List of champions inspired by this culture.
  - Structure:
    - Champion_ID
    - Notes on which part is influenced (e.g. "Dress from Han Dynasty", "Concept similar to Odin")

## 8. Layer_Type

- How directly the culture is expressed:
  - Literal Adaptation
  - Loose Inspiration
  - Symbolic Parallel
  - Aesthetic Remix

## 9. Combined_With

- Any other cultures it’s fused with in design (optional):
  - E.g. “Noxus = Roman Empire + Dark Ages Europe”

## 10. Notes

- Clarifications, dev quotes, or artistic reinterpretation notes.
