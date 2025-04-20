```
sexual_archetype {
  sexual_archetype_id integer pk increments unique
  archetype_label varchar
  presentation_mode varchar
  erotic_energy_type varchar
  gender_coding varchar
  narrative_function text
  audience_psychotype_target varchar
  aesthetic_signals text
  power_dynamic_affiliation varchar
  alignment_with_lore text
  conflict_or_tension text
  metaphysical_symbolism text
  representative_champions text
  skinline_modifiers text
  audience_reception_profile varchar
  eroticism_vs_lore_sync varchar
  visual_theme_crossover text
  codex_notes text
}
```

## 📘 Table of Contents

- [1. Sexual_Archetype_ID](#1_sexual_archetype_id)
- [2. Archetype_Label](#2_archetype_label)
- [3. Presentation_Mode](#3_presentation_mode)
- [4. Erotic_Energy_Type](#4_erotic_energy_type)
- [5. Gender_Coding](#5_gender_coding)
- [6. Narrative_Function](#6_narrative_function)
- [7. Audience_Psychotype_Target](#7_audience_psychotype_target)
- [8. Aesthetic_Signals](#8_aesthetic_signals)
- [9. Power_Dynamic_Affiliation](#9_power_dynamic_affiliation)
- [10. Alignment_with_Lore](#10_alignment_with_lore)
- [11. Conflict_or_Tension](#11_conflict_or_tension)
- [12. Metaphysical_Symbolism](#12_metaphysical_symbolism)
- [13. Representative_Champions](#13_representative_champions)
- [14. Skinline_Modifiers](#14_skinline_modifiers)
- [15. Audience_Reception_Profile](#15_audience_reception_profile)
- [16. Eroticism_vs_Lore_Sync](#16_eroticism_vs_lore_sync)
- [17. Visual_Theme_Crossover](#17_visual_theme_crossover)
- [18. Codex_Notes](#18_codex_notes)

---

# **Narrative Asset Schema: Sexual_Archetype**

---

## 1. Sexual_Archetype_ID

- Unique identifier (slug or numeric) for the archetype.
- Examples: `innocent_tease`, `femme_fatale`, `divine_seductress`, `brutal_daddy`

---

## 2. Archetype_Label

- Canonical name for the sexual archetype.
- Examples:
  - Innocent Tease
  - Femme Fatale
  - Bratty Sub
  - Divine Seductress
  - Chaste Power Icon
  - Gentle Beast
  - Masochist Weapon
  - Femboy Heartbreaker
  - Forbidden Mother
  - Beast-God of Ruin
  - Incubus of Control

---

## 3. Presentation_Mode

- Primary vector of erotic signaling.
- Values:
  - Visual Design (e.g., exposed skin, suggestive silhouettes)
  - Behavioral Cues (e.g., voice lines, flirting, withdrawal)
  - Symbolic Allegory (e.g., bondage motifs, purity metaphors)
  - Audience Projection (fan interpretation, parasocial desire)

---

## 4. Erotic_Energy_Type

- The emotional flavor or mythic charge of the sexuality expressed.
- Values:
  - Soft / Nurturing
  - Cold / Remote
  - Predatory
  - Submissive
  - Playful / Bratty
  - Dominant
  - Sacred / Intoxicating
  - Chaotic / Unstable
  - Repressed / Fractured

---

## 5. Gender_Coding

- How the sexuality is aligned with or subverts gender expectations.
- Values:
  - Feminine-Aligned
  - Masculine-Aligned
  - Gender-Ambiguous / Femboy
  - Gender-Inverse
  - Androgynous Power Form
  - Post-Gender / Non-Human Desire

---

## 6. Narrative_Function

- Role this archetype plays within the story’s structure or themes.
- Examples:
  - Catalyst of Desire or Betrayal
  - Obstacle to Control
  - Mirror of Repression
  - Avatar of Lust
  - Unreachable Ideal
  - Engine of Chaos
  - Redemptive Temptation
  - Weaponized Sexuality

---

## 7. Audience_Psychotype_Target

- Intended or likely audience projection.
- Values:
  - Domination Fantasy
  - Submission Fantasy
  - Ideal Lover Fantasy
  - Voyeuristic Fantasy
  - Forbidden Fantasy
  - Transformational Fantasy (desire to become them)

---

## 8. Aesthetic_Signals

- Visual and stylistic indicators of the archetype.
- Examples:
  - Thigh-high boots, chokers, lip-licking animations (Femme Fatale)
  - Oversized hoodie, visible thighs, awkward eye contact (Femboy Tease)
  - Wet hair, glowing eyes, slow movement (Divine Seductress)
  - Bandages, scars, cold stares (Masochist Weapon)

---

## 9. Power_Dynamic_Affiliation

- Relationship between the archetype and power structures.
- Values:
  - Submissive (voluntary)
  - Submissive (forced)
  - Dominant (soft)
  - Dominant (cruel)
  - Independent / Untouchable
  - Controlled / Owned
  - Dual / Shifting

---

## 10. Alignment_with_Lore

- How the archetype aligns with the character’s canonical backstory or faction identity.
- Examples:
  - Irelia as Chaste Power Icon despite revealing visual style
  - Evelynn as Canonical Succubus Entity
  - Sett (Star Guardian) as Femboy Dom aesthetic with brute form

---

## 11. Conflict_or_Tension

- Narrative or psychological contradiction within the archetype.
- Examples:
  - Innocent appearance → ruthless behavior
  - Domineering power → deep loneliness
  - Flirtatious persona → complete detachment
  - Weapon of lust → secretly seeks love

---

## 12. Metaphysical_Symbolism

- Archetype’s symbolic or mythic alignment.
- Examples:
  - Aphrodite archetype (Evelynn)
  - Dionysian Temptation (Rakan)
  - Incubus Trickster (Jhin)
  - Kali-as-Blood-Fetish (Elise)
  - Unknowable Divine Virgin (Soraka base skin)

---

## 13. Representative_Champions

- List of champions who embody this archetype.
- Structure:
  - Champion_ID
  - Archetype_Label
  - Notes (e.g., skinline, voice lines, AU reinterpretation)

---

## 14. Skinline_Modifiers

- Whether alternate universes intensify or invert the sexual archetype.
- Examples:
  - Star Guardian Rakan = Playful Flirt
  - Debonair Ezreal = Idealized Dandy / Femboy
  - High Noon Ashe = Cold Killer / Remote Beauty
  - K/DA Evelynn = Modernized Pop Femme Fatale

---

## 15. Audience_Reception_Profile

- How fandom typically responds to the archetype.
- Values:
  - Heavily Simped
  - Cult Classic
  - Meme Object
  - Controversial / Polarizing
  - Queer Reclaimed Symbol
  - Erotically Ignored
  - Beloved but Denied

---

## 16. Eroticism_vs_Lore_Sync

- Does the sexual expression align or contradict the champion’s backstory or role?
- Values:
  - Fully Integrated
  - Visual Only (no narrative sync)
  - Lore-Suppressed (eroticism ignored in story)
  - Symbolic Only

---

## 17. Visual_Theme_Crossover

- Ties into existing `Visual_Theme` schema.
- Examples:
  - Gothic Horror + Blood Fetish (Evelynn)
  - Shuriman Deity + Divine Lover (Nidalee)
  - Mecha Frame + Masochist Servitor (Battlecast Skarner)

---

## 18. Codex_Notes

- Commentary on design intent, artistic intent vs player reception, cultural critiques, or archetype fluidity.

```

```
