## 📘 Table of Contents

- [1. Sect_Gender_ID](#1_sect_gender_id)
- [2. Label](#2_label)
- [3. Gender_Classification](#3_gender_classification)
- [4. Biological_Status](#4_biological_status)
- [5. Cultural_Function](#5_cultural_function)
- [6. Sexual_Expectations](#6_sexual_expectations)
- [7. Presentation_Style](#7_presentation_style)
- [8. Iconography](#8_iconography)
- [9. Associated_Rites](#9_associated_rites)
- [10. Used_By](#10_used_by)
- [11. Codex_Notes](#11_codex_notes)

---

# **Narrative Asset Schema: sect_genders**

---

## 1. Sect_Gender_ID

- Unique identifier for the gender expression within a sect.
- Format: integer or slug.
- Examples: `male`, `female`, `femboy`, `non_sexed`, `andro_savant`

---

## 2. Label

- Canonical name of the gender role within the sect or ritual context.
- Examples:
  - Male
  - Female
  - Femboy
  - Synthetic Host
  - Drifted Form
  - Non-Sexed Oracle

---

## 3. Gender_Classification

- Traditional or symbolic mapping of the gender.
- Values:
  - Binary (male/female)
  - Soft Androgyne
  - Post-Gender
  - Ritual Gender
  - Tech-Aligned / Robotic

---

## 4. Biological_Status

- The perceived or ritualized biology behind the identity.
- Examples:
  - Born Male
  - Surgically Modified Female
  - Fused Organs
  - Nullified Anatomy
  - Grown in Archive Vat

---

## 5. Cultural_Function

- The social or sexual purpose of this gender in the sect’s structure.
- Examples:
  - Breeding Vessel
  - Moan Archivist
  - Sexless Witness
  - Fluid Distributor
  - Flesh Interface

---

## 6. Sexual_Expectations

- What sexual roles or responsibilities are tied to this gender identity.
- Examples:
  - Receives but never gives
  - Must seduce but never climax
  - Acts as conduit for ritual transformation
  - Facilitates group climax via voice modulation

---

## 7. Presentation_Style

- Expected or glorified ways this gender performs or dresses.
- Examples:
  - Veiled and painted
  - Bound in cords
  - Nude with pearl implants
  - Robotic casing with soft exoskin
  - Animal mask and scent-marked skin

---

## 8. Iconography

- Common visual or symbolic motifs tied to this gender.
- Examples:
  - Feathered codpiece
  - Inked pelvic rings
  - Light-reactive skin patches
  - Cryo-seal genital sigil

---

## 9. Associated_Rites

- Rituals or events that feature this gender prominently.
- Linkable to `rituals` table.
- Examples:
  - First Opening Ceremony
  - Trial of Sealing
  - Breathless Communion
  - Zero-Climax Incantation

---

## 10. Used_By

- Sect(s) or race(s) that use or enforce this gender identity.
- Can be cross-referenced with `sects` or `identity_roles`.

---

## 11. Codex_Notes

- Design commentary, symbolic analysis, or contradictions.
- May include contested interpretations, mythic reversals, or banned derivatives.
