## 📘 Table of Contents

- [1. Timeline_Position_ID](#1_timeline_position_id)
- [2. Era_Label](#2_era_label)
- [3. Temporal_Tier](#3_temporal_tier)
- [4. Canon_Status](#4_canon_status)
- [5. Anchor_Events](#5_anchor_events)
- [6. Temporal_Sequence_Order](#6_temporal_sequence_order)
- [7. Associated_Regions](#7_associated_regions)
- [8. Thematic_Significance](#8_thematic_significance)
- [9. Representative_Champions](#9_representative_champions)
- [10. Temporal_Distortion_Flags](#10_temporal_distortion_flags)
- [11. Media_References](#11_media_references)
- [12. Chronological_Predecessor](#12_chronological_predecessor)
- [13. Chronological_Successor](#13_chronological_successor)
- [14. Codex_Notes](#14_codex_notes)

---
# **Narrative Asset Schema: Timeline_Position**

---

## 1. Timeline_Position_ID

- **Definition**: Unique identifier (slug or numeric) for a specific era, epoch, or timeline marker.
- **Examples**: `ancient_targon_age`, `modern_runeterra`, `ruination_event`, `arcane_conflict`, `star_guardian_timeline`

---

## 2. Era_Label

- **Definition**: Canonical name of the time period or event window.
- **Examples**:
  - Age of Myth
  - Shuriman Empire Era
  - Rune Wars Era
  - Noxian Expansion Period
  - Modern Runeterra
  - Post-Ruination
  - Arcane Era (Zaun Conflict)
  - Alternate Universe

---

## 3. Temporal_Tier

- **Definition**: Level of chronological granularity.
- **Values**:
  - Epoch (thousands of years)
  - Era (centuries to millennia)
  - Historical Period (decades to centuries)
  - Event Block (months to years)
  - Local Incident (days to weeks)
  - Fragmentary / Mythic (nonlinear or symbolic)
  - AU Timeline (non-canon track)

---

## 4. Canon_Status

- **Definition**: Degree to which the timeline is officially acknowledged and synchronized.
- **Values**:
  - Core Canon
  - Semi-Canon (e.g., Legends of Runeterra content)
  - Fragmentary Canon (implied or partial chronology)
  - Alternate Universe
  - Game-Evoked / Event-Driven

---

## 5. Anchor_Events

- **Definition**: Known major events that define this time segment.
- Structure:
  - Event Name
  - Event_ID
  - Description
- **Examples**:
  - The Fall of Shurima
  - The Ascension of Targon Hosts
  - The Death of Isolde
  - The Arcane Conflict
  - The Ruination
  - The Sentinels of Light Campaign

---

## 6. Temporal_Sequence_Order

- **Definition**: Numeric or structured field for sorting timeline segments linearly.
- **Examples**:
  - `001`: Age of Myth
  - `010`: Rise of Shurima
  - `020`: Rune Wars
  - `030`: Modern Runeterra
  - `999`: Alternate Timeline

---

## 7. Associated_Regions

- **Definition**: Runeterran regions primarily affected or active during this period.
- **Examples**:
  - Freljord, Shurima, Piltover & Zaun, Targon

---

## 8. Thematic_Significance

- **Definition**: Narrative motifs dominant in this period.
- **Examples**:
  - Myth-Making & Godhood
  - War & Expansion
  - Magical Collapse
  - Technological Rise
  - Cataclysm & Rebirth
  - Cultural Reformation

---

## 9. Representative_Champions

- **Definition**: Champions whose arcs are rooted in this timeline segment.
- Structure:
  - Champion_ID
  - Role in Period (Origin / Active / Victim / Catalyst)
  - Arc Summary
- **Examples**:
  - Azir → Catalyst of Shuriman Fall
  - Viego → Catalyst of Ruination
  - Ekko → Active Agent in Zaun’s Future
  - Zilean → Nonlinear presence across multiple periods

---

## 10. Temporal_Distortion_Flags

- **Definition**: Indicators of non-linear time (magic, memory, godhood, multiversal logic).
- **Values**:
  - Time Travel (Zilean)
  - Timeline Looping / Branching (Ekko)
  - Eternal Return (Kindred's metaphysics)
  - Alternate Continuity (Arcane, Star Guardian, PROJECT)

---

## 11. Media_References

- **Definition**: Where this timeline period is explored across Riot media.
- Structure:
  - Title
  - Medium (Short Story, Cinematic, Comic, Arcane)
  - Canon Status
- **Examples**:
  - _Ruination_ Novel
  - _Arcane_ Netflix Series
  - _Shadow and Fortune_ Short Story

---

## 12. Chronological_Predecessor

- **Definition**: The timeline segment that precedes this one.
- Example:
  - Rune Wars → Modern Runeterra

---

## 13. Chronological_Successor

- **Definition**: The timeline segment that follows this one.
- Example:
  - Ruination → Post-Ruination Era

---

## 14. Codex_Notes

- **Definition**: Notes on disputed dates, conflicting depictions, developer interviews, or patch retcons.
