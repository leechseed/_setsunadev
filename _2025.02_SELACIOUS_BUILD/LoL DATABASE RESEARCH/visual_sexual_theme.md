```
visual_sexual_theme {
  visual_sexual_theme_id integer pk increments unique
  label varchar
  design_focus_areas text
  eroticism_tone varchar
  costume_grammar text
  erotic_symbols text
  gendered_signaling varchar
  power_dynamic varchar
  skinline_amplifiers text
  symbolic_function text
  audience_projection_target varchar
  champion_examples text
  visual_theme_crossover text
  media_presence text
  cultural_influences text
  edge_case_flags text
  codex_notes text
}

```

## 📘 Table of Contents

- [1. Visual_Sexual_Theme_ID](#1_visual_sexual_theme_id)
- [2. Label](#2_label)
- [3. Design_Focus_Areas](#3_design_focus_areas)
- [4. Eroticism_Tone](#4_eroticism_tone)
- [5. Costume_Grammar](#5_costume_grammar)
- [6. Erotic_Symbols](#6_erotic_symbols)
- [7. Gendered_Signaling](#7_gendered_signaling)
- [8. Power_Dynamic](#8_power_dynamic)
- [9. Skinline_Amplifiers](#9_skinline_amplifiers)
- [10. Symbolic_Function](#10_symbolic_function)
- [11. Audience_Projection_Target](#11_audience_projection_target)
- [12. Champion_Examples](#12_champion_examples)
- [13. Visual_Theme_Crossover](#13_visual_theme_crossover)
- [14. Media_Presence](#14_media_presence)
- [15. Cultural_Influences](#15_cultural_influences)
- [16. Edge_Case_Flags](#16_edge_case_flags)
- [17. Codex_Notes](#17_codex_notes)

---

# **Narrative Asset Schema: Visual_Sexual_Theme**

---

## 1. Visual_Sexual_Theme_ID

- **Definition**: Unique identifier (slug or numeric) for this visual-sexual theme entry.
- **Examples**: `bratty_femme`, `divine_dominatrix`, `monster_daddy`, `priestess_of_shame`

---

## 2. Label

- **Definition**: Stylized name of the visual-sexual motif.
- **Examples**:
  - Bratty Femme
  - Cold Dom
  - Divine Virgin
  - Femboy Siren
  - Ritual Object
  - Erotic Construct
  - The Wet Saint
  - Horned Warbeast
  - Cursed Doll

---

## 3. Design_Focus_Areas

- **Definition**: Key physical focal zones used to suggest sexual identity.
- **Examples**:
  - Legs / Thighs
  - Hips / Waist
  - Chest / Shoulders
  - Eyes / Gaze
  - Posture / Pose
  - Voice / Breathing
  - Silhouette Contrast
  - Clothing Removal Logic

---

## 4. Eroticism_Tone

- **Definition**: The emotional temperature or narrative aura of the erotic presentation.
- **Values**:
  - Cold / Remote
  - Seductive / Coaxing
  - Playful / Teasing
  - Brutal / Beastly
  - Sacred / Untouchable
  - Soft / Vulnerable
  - Masochistic / Martyr
  - Repressed / Buried

---

## 5. Costume_Grammar

- **Definition**: Aesthetic language expressed through clothing, skin exposure, and accessories.
- **Examples**:
  - Thigh highs, chokers, silk, harnesses, metal plating, lace, bondage-inspired symmetry, ripped gloves, exposed ribs, religious robes, tattoos, armor gaps, holographic lingerie

---

## 6. Erotic_Symbols

- **Definition**: Visual symbols with sexual or mythic charge.
- **Examples**:
  - Horns, chains, veils, flowers, wounds, blood trails, halos, eyes, masks, rings, roses, mirrors, spit, thorns

---

## 7. Gendered_Signaling

- **Definition**: How the design uses or disrupts binary gender expectations.
- **Values**:
  - Hyper-Feminine
  - Hyper-Masculine
  - Androgynous
  - Gender-Inverse
  - Femboy-Coded
  - Masculine Shell / Feminine Cues
  - Post-Gender / Alien

---

## 8. Power_Dynamic

- **Definition**: Role suggested by the visual sexual motif in social/sexual hierarchies.
- **Values**:
  - Dominant (Commanding / Cruel / Divine)
  - Submissive (Voluntary / Broken / Weaponized)
  - Switch / Ambiguous
  - Independent / Withheld
  - Owned / Displayed
  - Obsessed / Possessive
  - Absent / Numb

---

## 9. Skinline_Amplifiers

- **Definition**: Alternate universe skins that enhance or mutate the base visual-sexual theme.
- Structure:
  - Skinline
  - Modification Notes
- **Examples**:
  - Star Guardian Syndra → Cold Dom + Angelic Fetish Layer
  - K/DA Evelynn → Idol Femme Fatale with Mirror Accessories
  - Debonair Sett → Femboy Power Fantasy with Mafia Swagger

---

## 10. Symbolic_Function

- **Definition**: What the character’s erotic visual design _represents_ mythically or thematically.
- **Examples**:
  - Avatar of Lust
  - Prisoner of Desire
  - Divine Temptation
  - Weapon of Repression
  - Eros-as-Monster
  - Victim of the Gaze
  - Living Taboo

---

## 11. Audience_Projection_Target

- **Definition**: The fantasy this aesthetic is meant to invoke in the viewer.
- **Values**:
  - Domination Fantasy
  - Submission Fantasy
  - Ideal Lover
  - Voyeurism
  - Idolization
  - Forbidden Temptation
  - Mirror / Self-Insertion

---

## 12. Champion_Examples

- **Definition**: Champions that exhibit this theme.
- Structure:
  - Champion_ID
  - Alignment (Primary / Skin-Only / AU-Only / Ambiguous)
  - Visual-Sexual Theme Note

---

## 13. Visual_Theme_Crossover

- **Definition**: Corresponding `Visual_Theme` categories that reinforce the sexual aesthetic.
- Examples:
  - Gothic Horror → Bloodplay, Sacred Whore
  - Cyberpunk → Erotic Augmentation, Digital Siren
  - Celestial / Divine → Virgin Fetish, Ascended Beauty
  - Tribal / Bestial → Primal Lust, Animalistic Heat

---

## 14. Media_Presence

- **Definition**: Whether this visual-sexual theme has appeared in official media.
- Structure:
  - Media Title
  - Type (Cinematic, Comic, Skinline)
  - Explicit or Implied

---

## 15. Cultural_Influences

- **Definition**: Real-world aesthetic or mythological influences.
- Examples:
  - BDSM fashion, Classical Greek statues, Shinto priestess wear, Catholic martyrdom, Japanese ero-guro, Hollywood sirens, Renaissance angels, K-pop idols

---

## 16. Edge_Case_Flags

- **Definition**: Notes on ambiguous, conflicting, or controversial designs.
- Examples:
  - Visual eroticism contradicted by narrative purity
  - Erotic symbolism applied to non-gendered constructs
  - Riot disclaimer for region-specific censorship

---

## 17. Codex_Notes

- **Definition**: Metacommentary, fan discourse, dev commentary, or transmedia implications.
