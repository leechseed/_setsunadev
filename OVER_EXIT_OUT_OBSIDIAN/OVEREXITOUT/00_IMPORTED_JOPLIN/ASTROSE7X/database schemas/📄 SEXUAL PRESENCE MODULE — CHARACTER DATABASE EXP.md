---
title: 📄 SEXUAL PRESENCE MODULE — CHARACTER DATABASE EXPANSION
updated: 2025-05-19 12:23:53Z
created: 2025-05-19 12:23:41Z
latitude: 30.43825590
longitude: -84.28073290
altitude: 0.0000
---


# 📄 SEXUAL PRESENCE MODULE — CHARACTER DATABASE EXPANSION  
**Date:** "2025-05-19"  
**Prepared by:** Narrative Systems Division  
**Project:** GUTS99 / Narrative Chemistry Engine  
**Module:** `sexual_presence`  
**Version:** 1.0.0  

---

## 🔧 PURPOSE  
This module defines the **sexual aura, aesthetic signaling, and fetish logic** of a character in both **simulationist** (GURPS-compatible) and **narrative** contexts. It integrates kink theory, visual trope modeling, and modular world logic to support seduction, reputation, social dynamics, and aesthetic-coding systems across narrative systems.

---

## 🧠 OBJECTIVE  
To model characters not just by raw attractiveness, but by:
- **Erotic power projection**
- **Symbolic archetyping**
- **Aesthetic presentation**
- **Fetish and kink signaling**
- **Interactional chemistry and social response**

This enables deeper compatibility for:
- Procedural seduction events
- Faction-based sexual norms and taboos
- Narrative pacing around intimacy and taboo
- Character arcs involving repression, exhibitionism, shame, or divine sexuality

---

## 🗃️ TABLE SCHEMA – `sexual_presence`

```sql
CREATE TABLE sexual_presence (
    character_id INTEGER PRIMARY KEY,

    -- Core Sexual Aura
    charisma_score INTEGER,
    sexual_energy_type TEXT,
    presentation_mode TEXT,
    erotic_archetype TEXT,
    performance_confidence TEXT,
    arousal_reaction TEXT,
    trauma_or_origin_note TEXT,

    -- Fetishized Physical Signals
    fetishized_features TEXT,
    aesthetic_coding TEXT,
    gaze_style TEXT,
    vocal_cues TEXT,
    touch_behavior TEXT,
    scent_profile TEXT,

    -- Kink Logic
    personal_kink TEXT,
    dominant_fetishes TEXT,
    submissive_fetishes TEXT,
    kink_expression_style TEXT,
    kink_triggers TEXT,

    -- World Affiliation Logic
    attraction_faction_tags TEXT,
    rejection_faction_tags TEXT,

    FOREIGN KEY (character_id) REFERENCES characters(character_id)
);
````

---

## 🔑 FIELD DESCRIPTIONS

### 1. **Core Sexual Aura**

| Field                    | Description                                                        |
| ------------------------ | ------------------------------------------------------------------ |
| `charisma_score`         | Mechanical Charisma value from GURPS.                              |
| `sexual_energy_type`     | Dominant erotic projection: e.g., dominant, submissive, chaotic.   |
| `presentation_mode`      | How character behaves in sexually coded ways: teasing, stoic, etc. |
| `erotic_archetype`       | Narrative sexual identity (e.g., femme fatale, discipline daddy).  |
| `performance_confidence` | Inner confidence or performativity during sexual expression.       |
| `arousal_reaction`       | Common initial reactions from others (e.g., enthralled, repulsed). |
| `trauma_or_origin_note`  | Psychological or narrative backstory for sexual behavior.          |

### 2. **Fetishized Physical Signals**

| Field                 | Description                                                            |
| --------------------- | ---------------------------------------------------------------------- |
| `fetishized_features` | Specific physical traits often fetishized (e.g., thighs, ribs).        |
| `aesthetic_coding`    | Visual code or fashion style (e.g., nun, dollcore, latex domme).       |
| `gaze_style`          | Sexualized eye behavior (e.g., locked-on, dead stare).                 |
| `vocal_cues`          | Erotic voice signals (e.g., husky, baby talk).                         |
| `touch_behavior`      | Physical contact style (e.g., commanding, clumsy, featherlight).       |
| `scent_profile`       | Erotic olfactory signal (e.g., sugary musk, iron blood, holy incense). |

### 3. **Kink Logic**

| Field                   | Description                                                              |
| ----------------------- | ------------------------------------------------------------------------ |
| `personal_kink`         | Deepest narrative kink (e.g., humiliation, praise, forced feminization). |
| `dominant_fetishes`     | Tags relevant when acting as top (e.g., degradation, spanking).          |
| `submissive_fetishes`   | Tags relevant when acting as bottom (e.g., obedience, restraint).        |
| `kink_expression_style` | Describes role: repressed, exhibitionist, ritualized, etc.               |
| `kink_triggers`         | Specific arousal cues (e.g., mirror gazing, latex, uniforms).            |

### 4. **Factional / World Reactions**

| Field                     | Description                                                                           |
| ------------------------- | ------------------------------------------------------------------------------------- |
| `attraction_faction_tags` | Factions/races/social classes that are erotically drawn to this character’s presence. |
| `rejection_faction_tags`  | Groups that are repelled, offended, or disturbed by their sexual nature.              |

---

## 🧬 DESIGN PHILOSOPHY

* **GURPS-Compatible**: Tied into Charisma, Appearance, Reputation, and Reaction mechanics.
* **Narrative-Centric**: Enables symbolic, archetypal, or taboo-inflected storytelling.
* **Modular**: Every field is string-tag and JSON-ready for fast integration.
* **World-Linked**: Integrates into faction-based reputational logic for systemic simulation.
* **Kink-Informed**: Leverages real fetish structures for emergent storytelling and consent modeling.

---

## 🛠️ NEXT STEPS

* [ ] Create `fetish_taxonomy` lookup table with canonical fetish tags and domains.
* [ ] Define `aesthetic_coding` registry with linked visuals, tags, and cultural associations.
* [ ] Integrate this schema with `scene_engine` to influence intimacy encounters and NPC behavior.
* [ ] Link to `chemistry_matrix` for pairwise compatibility and attraction simulation.
* [ ] Build automated `sexual_presence_template.md` frontmatter generator for YAML character notes.

---

## 🧾 SAMPLE YAML OUTPUT

```yaml
sexual_presence:
  charisma_score: 2
  sexual_energy_type: "chaotic"
  presentation_mode: "teasing"
  erotic_archetype: "bratty sub"
  performance_confidence: "playful"
  arousal_reaction: "entrancing"
  trauma_or_origin_note: "learned to seduce handlers in covert training camps"

  fetishized_features: "thigh gap, licking lips, messy eyeliner"
  aesthetic_coding: "cyberbimbo"
  gaze_style: "locked-on"
  vocal_cues: "mocking lilt"
  touch_behavior: "lingering"
  scent_profile: "burnt sugar + copper"

  personal_kink: "being watched"
  dominant_fetishes: "degradation, spitting"
  submissive_fetishes: "humiliation, voice control"
  kink_expression_style: "exhibitionist"
  kink_triggers: "mirrors, cameras, red lighting"

  attraction_faction_tags: "Kheprax-Voidwrights, Chimora-Dreamcloaks"
  rejection_faction_tags: "Sephara-Oracles"
```

---

## ✅ STATUS: APPROVED FOR INTEGRATION

This schema is ready to merge into the `character_meta` module and link with `faction_attraction`, `scene_engine`, and `visual_design_pipeline`.

For questions, contact: `leechseed@guts99.internal`

```
```
