## 📘 Table of Contents

- [1. Sex_Gender_ID](#1_sex_gender_id)
- [2. Label](#2_label)
- [3. Classification_Tier](#3_classification_tier)
- [4. Canonical_Usage](#4_canonical_usage)
- [5. Gender_Presentation](#5_gender_presentation)
- [6. Biological_Status](#6_biological_status)
- [7. Cultural_Role_in_Lore](#7_cultural_role_in_lore)
- [8. Pronoun_Usage](#8_pronoun_usage)
- [9. Representative_Champions](#9_representative_champions)
- [10. Aesthetic_Association](#10_aesthetic_association)
- [11. Voice_Profile](#11_voice_profile)
- [12. Symbolic_Alignment](#12_symbolic_alignment)
- [13. Edge_Case_Flags](#13_edge_case_flags)
- [14. Codex_Notes](#14_codex_notes)

---
# **Narrative Asset Schema: Sex_Gender**

---

## 1. Sex_Gender_ID

- Unique identifier (slug or string) for the gender category.
- Examples: `male`, `female`, `nonbiological`, `femboy`

---

## 2. Label

- Display name used across systems and documentation.
- Values:
  - Male
  - Female
  - Femboy
  - Non-Biological Entity

---

## 3. Classification_Tier

- Indicates the structural basis of the gender category.
- Values:
  - Biological (linked to reproductive systems or species sex dimorphism)
  - Aesthetic / Performed (defined by visual, behavioral, or cultural coding)
  - Ontological / Synthetic (used for constructs, spirits, or Voidborn)

---

## 4. Canonical_Usage

- Does Riot use this label or aesthetic directly in lore, design, or community-recognized identity?
- Values:
  - Canonical
  - Semi-Canonical (design-coded but not explicitly labeled)
  - Community Constructed / Implicit

---

## 5. Gender_Presentation

- How the character is framed visually and narratively.
- Values:
  - Masculine
  - Feminine
  - Androgynous
  - Femboy (feminine presentation on male-coded frame)
  - Inhuman / Non-Gendered

---

## 6. Biological_Status

- Whether the character is biological, synthetic, or metaphysical.
- Values:
  - Organic
  - Non-Biological
  - Post-Biological / Unknown
  - Dual-Aspect (e.g., Kindred)

---

## 7. Cultural_Role_in_Lore

- How gender identity intersects with social or factional identity.
- Examples:
  - Demacian gender norms (military, patriarchal)
  - Ionian fluidity in spiritual beings
  - Zaunite disregard for fixed identity
  - Targonian ascension erasing mortal form

---

## 8. Pronoun_Usage

- Pronouns used in official media or accepted fandom canon.
- Examples:
  - He/Him
  - She/Her
  - They/Them
  - N/A (Void entities or constructs)
  - Mixed / Contextual (e.g., Kindred = They)

---

## 9. Representative_Champions

- Champions falling under this category.
- Structure:
  - Champion_ID
  - Label
  - Notes (e.g., “Visually coded as femboy in Spirit Blossom skin”)

---

## 10. Aesthetic_Association

- What kind of themes, shapes, and designs are visually linked to this gender identity.
- Examples:
  - **Femboy**: Soft features, exposed legs, thigh highs, coquettish posture, elegance mixed with power
  - **Non-Biological**: Glowing cores, metal limbs, voice modulation
  - **Male**: Broad silhouettes, utilitarian armor, exposed torsos
  - **Female**: Accentuated curves, ornate headdresses, elegant weapons

---

## 11. Voice_Profile

- Voice design and casting.
- Values:
  - Male Voice Actor
  - Female Voice Actor
  - Gender-Ambiguous Vocal Tone
  - Digitized / Synthetic Voice
  - Silent

---

## 12. Symbolic_Alignment

- What mythic or archetypal symbolism the gender represents.
- Examples:
  - Femboy = Trickster, Siren, Youthful Innocence, Subversion of Power
  - Non-Biological = Tabula Rasa, Programmed Will, Artificial Emotion
  - Female = The Nurturer, The Avenger, The Oracle
  - Male = The Warrior, The Tyrant, The Fallen Hero

---

## 13. Edge_Case_Flags

- Use this field to handle ambiguous or dual-aspect characters.
- Examples:
  - Kindred = Dual-Aspect (Lamb & Wolf)
  - Blitzcrank = Non-Gendered but coded masculine
  - Neeko = Female, with shape-shifting that includes male mimicry

---

## 14. Codex_Notes

- Commentary on fandom classification, Riot dev statements, regional design philosophies, or cultural interpretations.

- **Male**: Garen, Darius, Yasuo, Tryndamere
- **Female**: Leona, Morgana, Vi, Ahri
- **Femboy**: Sett (Star Guardian), Aphelios (general design), Viego (Ruined aesthetic)
- **Non-Biological**: Blitzcrank, Orianna, Vel’Koz, Xerath, Bard
- **Edge Case / Dual-Aspect**: Kindred (Lamb = feminine-coded, Wolf = masculine-coded)
