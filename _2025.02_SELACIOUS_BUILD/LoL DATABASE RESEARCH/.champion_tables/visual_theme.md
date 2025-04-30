```

visual_theme {
  visual_theme_id integer pk increments unique
  visual_theme_label varchar
  theme_type varchar
  core_elements text
  color_palette text
  silhouette_profile varchar
  cultural_influence text
  region_affiliation_style text
  champion_associations text
  skinline_correspondence text
  symbolic_function text
  visual_trope_alignment text
  visual_mutation_flag varchar
  media_consistency varchar
  animation_style_cues text
  visual_theme_intensity integer
  contrasting_skins text
  codex_notes text
}

```

## 📘 Table of Contents

- [1. Visual_Theme_ID](#1_visual_theme_id)
- [2. Visual_Theme_Label](#2_visual_theme_label)
- [3. Theme_Type](#3_theme_type)
- [4. Core_Elements](#4_core_elements)
- [5. Color_Palette](#5_color_palette)
- [6. Silhouette_Profile](#6_silhouette_profile)
- [7. Cultural_Influence](#7_cultural_influence)
- [8. Region_Affiliation_Style](#8_region_affiliation_style)
- [9. Champion_Associations](#9_champion_associations)
- [10. Skinline_Correspondence](#10_skinline_correspondence)
- [11. Symbolic_Function](#11_symbolic_function)
- [12. Visual_Trope_Alignment](#12_visual_trope_alignment)
- [13. Visual_Mutation_Flag](#13_visual_mutation_flag)
- [14. Media_Consistency](#14_media_consistency)
- [15. Animation_Style_Cues](#15_animation_style_cues)
- [16. Visual_Theme_Intensity](#16_visual_theme_intensity)
- [17. Contrasting_Skins](#17_contrasting_skins)
- [18. Codex_Notes](#18_codex_notes)

---

# **Narrative Asset Schema: Visual_Theme**

---

## 1. Visual_Theme_ID

- **Definition**: Unique identifier (slug or numeric) for the visual theme.
- **Examples**: `gothic_horror`, `knightly_order`, `bioengineered_outlaw`

---

## 2. Visual_Theme_Label

- **Definition**: Canonical name of the visual theme.
- **Examples**: Knight, Ninja, Gothic Horror, Arcane Steampunk, Spirit Beast

---

## 3. Theme_Type

- **Definition**: Broad classification of visual aesthetics.
- **Values**:
  - Cultural Inspiration
  - Mythological Motif
  - Technological/Temporal Era
  - Costume Archetype
  - Biophysical Mutation
  - Metaphysical / Abstract
  - Thematic Hybrid

---

## 4. Core_Elements

- **Definition**: Key design motifs consistently seen across the theme.
- **Examples**:
  - Armor plating, Heraldic sigils, Capes (Knight)
  - Tattoos, Shadow veils, Swords (Ninja)
  - Mechanical limbs, Tubing, Goggles (Steampunk)
  - Animal features, Glowing eyes, Fur/feathers (Spirit Beast)
  - Chains, Broken masks, Pale skin (Gothic Horror)

---

## 5. Color_Palette

- **Definition**: Dominant hues and contrasts.
- **Examples**:
  - Gold/Blue/White (Divine Knight)
  - Red/Black (Blood Magic)
  - Teal/Violet (Voidborn)
  - Copper/Brass/Green (Steampunk)

---

## 6. Silhouette_Profile

- **Definition**: Recognizable shape and posture style.
- **Values**:
  - Bulky / Towering (Juggernauts, Tanks)
  - Agile / Lean (Assassins, Rangers)
  - Cloaked / Shrouded (Mystics, Cultists)
  - Mutated / Asymmetrical (Monsters, Void)
  - Graceful / Regal (Queens, Spirits)

---

## 7. Cultural_Influence

- **Definition**: Real-world cultures or traditions influencing the aesthetic.
- **Examples**:
  - Feudal Japan (Shen, Yasuo)
  - Ancient Egypt (Nasus, Renekton)
  - Western Gothic (Elise, Vex)
  - Slavic Paganism (Lillia, Ornn)
  - Classical Rome (Swain, Leona)

---

## 8. Region_Affiliation_Style

- **Definition**: Regional visual grammar.
- **Examples**:
  - **Demacia**: Ornate plate armor, tabards, lion motifs
  - **Noxus**: Spiked armor, red sashes, warlord decadence
  - **Piltover**: Industrial elegance, gold trim, clean techwear
  - **Zaun**: Rusted implants, green gas, alchemical wear
  - **Shurima**: Sand-gold tones, ceremonial wraps, divine architecture
  - **Ionia**: Flowing robes, asymmetry, nature motifs

---

## 9. Champion_Associations

- **Definition**: Champions whose base design reflects this theme.
- **Structure**:
  - Champion_ID
  - Visual_Theme_Label
  - Notes (e.g., “Hybridized with Gothic”, “Void-corrupted version”)

---

## 10. Skinline_Correspondence

- **Definition**: Skins that maintain or reinterpret this visual theme.
- **Examples**:
  - PROJECT: Echo of cyber-ninja
  - High Noon: Western-gothic demon
  - Spirit Blossom: Ethereal animal spirits in kimono
  - Dark Star: Cosmic horror and obliteration

---

## 11. Symbolic_Function

- **Definition**: Thematic or mythic meaning encoded in the visual language.
- **Examples**:
  - Armor = Duty, Order, Legacy
  - Horns / Claws = Primality, Corruption, Strength
  - Mask = Identity, Deception, Sacredness
  - Wings = Divinity, Ascension, Surveillance

---

## 12. Visual_Trope_Alignment

- **Definition**: Tropes or archetypes expressed through design.
- **Examples**:
  - Dark Messiah
  - Tragic Hero
  - Femme Fatale
  - Death God
  - Arcane Engineer
  - Mad Prophet

---

## 13. Visual_Mutation_Flag

- **Definition**: Whether the theme includes non-human body design.
- **Values**:
  - None
  - Subtle (Eyes, Hair, Skin tone)
  - Partial (Arms, Legs, Tail, Horns)
  - Full (Creature or Post-Human Form)

---

## 14. Media_Consistency

- **Definition**: Fidelity of this visual theme across Riot’s media ecosystem.
- **Values**:
  - Consistent (Lore, Splash Art, Cinematics align)
  - Varied (Different interpretations across media)
  - Retconned / Evolving

---

## 15. Animation_Style_Cues

- **Definition**: In-game or cinematic motion and visual FX design linked to the theme.
- **Examples**:
  - Petal trails (Ionia)
  - Flickering shadows (Noxian assassins)
  - Clockwork gears (Piltover)
  - Corrupted bloom particles (Void)

---

## 16. Visual_Theme_Intensity

- **Definition**: How dominant or core the visual theme is to the champion’s identity.
- **Scale**:
  - 5 = Visually Defining (e.g., Mordekaiser = Gothic Knight)
  - 4 = Primary Aesthetic (e.g., Jhin = Theatrical Killer)
  - 3 = Hybridized
  - 2 = Subtle Influence
  - 1 = Barely Present

---

## 17. Contrasting_Skins

- **Definition**: Skins that deliberately subvert or oppose the base visual theme.
- Structure:
  - Skin_Name
  - Visual_Theme_Contrast_Type: (Humor / Inversion / AU Replacement)

---

## 18. Codex_Notes

- **Definition**: Art team philosophy, dev commentary, inconsistencies, evolution of look, or symbol-theory extrapolation.

---

```

```
