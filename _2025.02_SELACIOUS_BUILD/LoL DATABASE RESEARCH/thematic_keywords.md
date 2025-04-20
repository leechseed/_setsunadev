```
thematic_keywords {
  thematic_id integer pk increments unique
  thematic_label varchar
  thematic_type varchar
  abstract_definition text
  inworld_interpretation text
  narrative_function varchar
  emotional_resonance varchar
  common_arc_patterns text
  symbolic_motifs text
  associated_champions text
  region_ties text
  faction_ties text
  thematic_opposition text
  crossmedia_representation text
  canon_events_expressing_theme text
  thematic_complexity_score integer
  related_mythic_roles text
  codex_notes text
}

```

## 📘 Table of Contents

- [1. Keyword_ID](#1_keyword_id)
- [2. Keyword_Label](#2_keyword_label)
- [3. Keyword_Type](#3_keyword_type)
- [4. Abstract_Definition](#4_abstract_definition)
- [5. In-World_Interpretation](#5_inworld_interpretation)
- [6. Narrative_Function](#6_narrative_function)
- [7. Emotional_Resonance](#7_emotional_resonance)
- [8. Common_Arc_Patterns](#8_common_arc_patterns)
- [9. Symbolic_Motifs](#9_symbolic_motifs)
- [10. Associated_Champions](#10_associated_champions)
- [11. Region_Ties](#11_region_ties)
- [12. Faction_Ties](#12_faction_ties)
- [13. Thematic_Opposition](#13_thematic_opposition)
- [14. Cross-Media_Representation](#14_crossmedia_representation)
- [15. Canon_Events_Expressing_Theme](#15_canon_events_expressing_theme)
- [16. Thematic_Complexity_Score](#16_thematic_complexity_score)
- [17. Related_Mythic_Roles](#17_related_mythic_roles)
- [18. Codex_Notes](#18_codex_notes)

---

# **Narrative Asset Schema: Thematic_Keywords**

---

## 1. Keyword_ID

- **Definition**: Unique identifier (slug or numeric) for the thematic keyword.
- **Examples**: `vengeance`, `identity_crisis`, `transcendence`

---

## 2. Keyword_Label

- **Definition**: Canonical theme term.
- **Examples**: Vengeance, Redemption, Legacy, Madness, Freedom, Identity

---

## 3. Keyword_Type

- **Definition**: Structural or symbolic classification of the theme.
- **Values**:
  - Core Theme (defines narrative foundation)
  - Supporting Theme (shapes arc texture)
  - Subtextual Theme (present through implication or symbol)
  - Meta-Theme (commentary on storytelling itself)
  - Relational Theme (expressed via interpersonal dynamics)

---

## 4. Abstract_Definition

- **Definition**: Philosophical or literary meaning of the theme in a general context.
- **Examples**:
  - **Vengeance**: The consuming pursuit of retribution, often leading to moral collapse or transformation.
  - **Legacy**: The burden or gift of what one leaves behind — inheritance of name, trauma, or ideology.

---

## 5. In-World_Interpretation

- **Definition**: How the theme manifests uniquely in the world of Runeterra.
- **Examples**:
  - **Redemption**: Often literalized through resurrection, reintegration into an order, or reversal of power.
  - **Freedom**: Opposed by institutional control — Piltover's rule, Demacia's suppression, Noxian doctrine.

---

## 6. Narrative_Function

- **Definition**: Thematic role across character arcs and events.
- **Values**:
  - Arc Driver (e.g. Vengeance → Viego)
  - Arc Resolution (e.g. Redemption → Rengar)
  - Contrapuntal Theme (e.g. Duty vs Freedom → Quinn vs Sylas)
  - Foil Generator (expressed through contrasts)
  - Lore Nexus (theme crosses regions/factions/arcs)

---

## 7. Emotional_Resonance

- **Definition**: Dominant emotional field tied to the theme.
- **Values**:
  - Rage
  - Grief
  - Awe
  - Terror
  - Wonder
  - Isolation
  - Hope
  - Despair
  - Love
  - Paranoia

---

## 8. Common_Arc_Patterns

- **Definition**: Typical character arc structures expressing this theme.
- **Structure**:
  - Theme → Arc Type
  - Example Champion
- **Examples**:
  - **Madness** → Fall into Delusion → Jhin
  - **Sacrifice** → Hero’s Death → Senna
  - **Power** → Corruption → Xerath
  - **Hope** → Renewal Arc → Ekko

---

## 9. Symbolic_Motifs

- **Definition**: Recurring symbols that evoke the theme.
- **Examples**:
  - **Vengeance**: Broken swords, bloodied hands, mirrors
  - **Legacy**: Family crests, fading statues, ancestral ruins
  - **Freedom**: Chains, open skies, wind, birds
  - **Identity**: Masks, names, reflections, twins
  - **Madness**: Fractals, red spirals, broken clocks

---

## 10. Associated_Champions

- **Definition**: Champions whose arcs are primarily or heavily shaped by this theme.
- **Structure**:
  - Champion_ID
  - Role: (Primary / Secondary / Subtextual)
  - Arc Summary

---

## 11. Region_Ties

- **Definition**: Which regions most strongly express this theme in their politics, culture, or history.
- **Structure**:
  - Region_ID
  - Contextualization
- **Examples**:
  - **Vengeance** → Shadow Isles → Ruination
  - **Order** → Demacia → Anti-magic suppression
  - **Freedom** → Zaun → Chem-punk resistance

---

## 12. Faction_Ties

- **Definition**: Organizations or groups centered around this theme.
- **Examples**:
  - **Control** → Mage Seekers, Chem-Barons
  - **Faith** → Solari, Black Rose
  - **Knowledge** → Glorious Evolution, Academies of Piltover

---

## 13. Thematic_Opposition

- **Definition**: Opposing or counterbalancing themes.
- **Structure**:
  - Theme → Opposed Theme
  - Example Conflict Pair
- **Examples**:
  - **Order ↔ Chaos** → Karma vs Jhin
  - **Legacy ↔ Rebellion** → Lucian vs Viego
  - **Power ↔ Sacrifice** → Xerath vs Leona

---

## 14. Cross-Media_Representation

- **Definition**: Appearance and portrayal of this theme across Riot media.
- **Structure**:
  - Media Title
  - Medium (e.g., Arcane, Ruination, Cinematic)
  - Expression (Explicit / Symbolic / Visual)

---

## 15. Canon_Events_Expressing_Theme

- **Definition**: Major story arcs that are vehicles for this theme.
- **Examples**:
  - **Ruination** → Vengeance, Madness, Corruption
  - **Arcane** → Identity, Legacy, Class Conflict
  - **Shuriman Fall** → Hubris, Ascension, Betrayal

---

## 16. Thematic_Complexity_Score

- **Definition**: Depth of thematic layering and narrative centrality.
- **Scale**:
  - 5 = Meta-Structural (defines entire region or event)
  - 4 = Arc-Defining (core driver for major characters)
  - 3 = Interpersonal Theme
  - 2 = Symbolic Accent
  - 1 = Light Flavor Text

---

## 17. Related_Mythic_Roles

- **Definition**: Mythic archetypes that commonly embody the theme.
- **Examples**:
  - **Sacrifice** → The Martyr (Senna, Galio)
  - **Corruption** → The Fallen God (Aatrox, Mordekaiser)
  - **Identity** → The Masked Trickster (Jhin, Kayn)
  - **Legacy** → The Scion of Ruin (Viego)

---

## 18. Codex_Notes

- **Definition**: Metacommentary on usage across patches, retcons, contradictions, or cultural significance.

---

- **Vengeance**
- **Redemption**
- **Sacrifice**
- **Power**
- **Corruption**
- **Legacy**
- **Freedom**
- **Identity**
- **Madness**
- **Duty**
- **Control**
- **Faith**
- **Obsession**
- **Hope**
- **Isolation**
- **Love**
- **Betrayal**
- **Rebirth**
- **Justice**
- **Hubris**

```

## 📘 Table of Contents

- [1. Keyword_ID](#1_keyword_id)
- [2. Keyword_Label](#2_keyword_label)
- [3. Keyword_Type](#3_keyword_type)
- [4. Abstract_Definition](#4_abstract_definition)
- [5. In-World_Interpretation](#5_inworld_interpretation)
- [6. Narrative_Function](#6_narrative_function)
- [7. Emotional_Resonance](#7_emotional_resonance)
- [8. Common_Arc_Patterns](#8_common_arc_patterns)
- [9. Symbolic_Motifs](#9_symbolic_motifs)
- [10. Associated_Champions](#10_associated_champions)
- [11. Region_Ties](#11_region_ties)
- [12. Faction_Ties](#12_faction_ties)
- [13. Thematic_Opposition](#13_thematic_opposition)
- [14. Cross-Media_Representation](#14_crossmedia_representation)
- [15. Canon_Events_Expressing_Theme](#15_canon_events_expressing_theme)
- [16. Thematic_Complexity_Score](#16_thematic_complexity_score)
- [17. Related_Mythic_Roles](#17_related_mythic_roles)
- [18. Codex_Notes](#18_codex_notes)

---

# **Narrative Asset Schema: Thematic_Keywords**

---

## 1. Keyword_ID

- **Definition**: Unique identifier (slug or numeric) for the thematic keyword.
- **Examples**: `vengeance`, `identity_crisis`, `transcendence`

---

## 2. Keyword_Label

- **Definition**: Canonical theme term.
- **Examples**: Vengeance, Redemption, Legacy, Madness, Freedom, Identity

---

## 3. Keyword_Type

- **Definition**: Structural or symbolic classification of the theme.
- **Values**:
  - Core Theme (defines narrative foundation)
  - Supporting Theme (shapes arc texture)
  - Subtextual Theme (present through implication or symbol)
  - Meta-Theme (commentary on storytelling itself)
  - Relational Theme (expressed via interpersonal dynamics)

---

## 4. Abstract_Definition

- **Definition**: Philosophical or literary meaning of the theme in a general context.
- **Examples**:
  - **Vengeance**: The consuming pursuit of retribution, often leading to moral collapse or transformation.
  - **Legacy**: The burden or gift of what one leaves behind — inheritance of name, trauma, or ideology.

---

## 5. In-World_Interpretation

- **Definition**: How the theme manifests uniquely in the world of Runeterra.
- **Examples**:
  - **Redemption**: Often literalized through resurrection, reintegration into an order, or reversal of power.
  - **Freedom**: Opposed by institutional control — Piltover's rule, Demacia's suppression, Noxian doctrine.

---

## 6. Narrative_Function

- **Definition**: Thematic role across character arcs and events.
- **Values**:
  - Arc Driver (e.g. Vengeance → Viego)
  - Arc Resolution (e.g. Redemption → Rengar)
  - Contrapuntal Theme (e.g. Duty vs Freedom → Quinn vs Sylas)
  - Foil Generator (expressed through contrasts)
  - Lore Nexus (theme crosses regions/factions/arcs)

---

## 7. Emotional_Resonance

- **Definition**: Dominant emotional field tied to the theme.
- **Values**:
  - Rage
  - Grief
  - Awe
  - Terror
  - Wonder
  - Isolation
  - Hope
  - Despair
  - Love
  - Paranoia

---

## 8. Common_Arc_Patterns

- **Definition**: Typical character arc structures expressing this theme.
- **Structure**:
  - Theme → Arc Type
  - Example Champion
- **Examples**:
  - **Madness** → Fall into Delusion → Jhin
  - **Sacrifice** → Hero’s Death → Senna
  - **Power** → Corruption → Xerath
  - **Hope** → Renewal Arc → Ekko

---

## 9. Symbolic_Motifs

- **Definition**: Recurring symbols that evoke the theme.
- **Examples**:
  - **Vengeance**: Broken swords, bloodied hands, mirrors
  - **Legacy**: Family crests, fading statues, ancestral ruins
  - **Freedom**: Chains, open skies, wind, birds
  - **Identity**: Masks, names, reflections, twins
  - **Madness**: Fractals, red spirals, broken clocks

---

## 10. Associated_Champions

- **Definition**: Champions whose arcs are primarily or heavily shaped by this theme.
- **Structure**:
  - Champion_ID
  - Role: (Primary / Secondary / Subtextual)
  - Arc Summary

---

## 11. Region_Ties

- **Definition**: Which regions most strongly express this theme in their politics, culture, or history.
- **Structure**:
  - Region_ID
  - Contextualization
- **Examples**:
  - **Vengeance** → Shadow Isles → Ruination
  - **Order** → Demacia → Anti-magic suppression
  - **Freedom** → Zaun → Chem-punk resistance

---

## 12. Faction_Ties

- **Definition**: Organizations or groups centered around this theme.
- **Examples**:
  - **Control** → Mage Seekers, Chem-Barons
  - **Faith** → Solari, Black Rose
  - **Knowledge** → Glorious Evolution, Academies of Piltover

---

## 13. Thematic_Opposition

- **Definition**: Opposing or counterbalancing themes.
- **Structure**:
  - Theme → Opposed Theme
  - Example Conflict Pair
- **Examples**:
  - **Order ↔ Chaos** → Karma vs Jhin
  - **Legacy ↔ Rebellion** → Lucian vs Viego
  - **Power ↔ Sacrifice** → Xerath vs Leona

---

## 14. Cross-Media_Representation

- **Definition**: Appearance and portrayal of this theme across Riot media.
- **Structure**:
  - Media Title
  - Medium (e.g., Arcane, Ruination, Cinematic)
  - Expression (Explicit / Symbolic / Visual)

---

## 15. Canon_Events_Expressing_Theme

- **Definition**: Major story arcs that are vehicles for this theme.
- **Examples**:
  - **Ruination** → Vengeance, Madness, Corruption
  - **Arcane** → Identity, Legacy, Class Conflict
  - **Shuriman Fall** → Hubris, Ascension, Betrayal

---

## 16. Thematic_Complexity_Score

- **Definition**: Depth of thematic layering and narrative centrality.
- **Scale**:
  - 5 = Meta-Structural (defines entire region or event)
  - 4 = Arc-Defining (core driver for major characters)
  - 3 = Interpersonal Theme
  - 2 = Symbolic Accent
  - 1 = Light Flavor Text

---

## 17. Related_Mythic_Roles

- **Definition**: Mythic archetypes that commonly embody the theme.
- **Examples**:
  - **Sacrifice** → The Martyr (Senna, Galio)
  - **Corruption** → The Fallen God (Aatrox, Mordekaiser)
  - **Identity** → The Masked Trickster (Jhin, Kayn)
  - **Legacy** → The Scion of Ruin (Viego)

---

## 18. Codex_Notes

- **Definition**: Metacommentary on usage across patches, retcons, contradictions, or cultural significance.

---

- **Vengeance**
- **Redemption**
- **Sacrifice**
- **Power**
- **Corruption**
- **Legacy**
- **Freedom**
- **Identity**
- **Madness**
- **Duty**
- **Control**
- **Faith**
- **Obsession**
- **Hope**
- **Isolation**
- **Love**
- **Betrayal**
- **Rebirth**
- **Justice**
- **Hubris**
```
