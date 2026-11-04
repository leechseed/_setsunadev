---
id: jebb_midnight
entity: Jebb Midnight
entity_id: jebb_midnight
title: Jebb Midnight
type: character
kind: character
ip: OVEREXITOUT
series: The Outliers
trunk: BLACK
role: pre-story bond (Tori's older brother, her navigator); the ghost of her L5 WOUND
resolve: n/a (dies pre-story, M1B)
status: "STUB 2026-11-04 (BOLO 176, Chief: go). Every fact below cites canon. The one lineage section is marked STUB, research-grade. No LEECHSEED record yet; this card exists so Tori's L5 relational_refs can point at a character_id."
blocking: none
created: 2026-11-04
aliases: [Jebb, "jebb-midnight"]
links:
  - "[[victoria-midnight]]"
  - "[[oxo-storyform]]"
  - "[[ssot_04_fabula]]"
  - "[[anna-colson-conway]]"
feeds:
  - "Tori's L5 relational_refs (kind ghost) and L8 secure_base_object (brother_deceased), in the vertical slice"
  - "ssot_04_fabula: m1b_crash_jebb_death, m1b_system_removes_jebb, m3_underground_search"
sources: 7 canon files (see Sources)
last_consolidated: 2026-11-04
---

# Jebb Midnight

> **"Love embedded inside procedure — the exact type of data the system cannot process and therefore erases."** — AUTH §Core Bond, on his pace notes

---

## Structure

| Field | Value | Source |
|---|---|---|
| Full name | Jebb Midnight | AUTH §Identity ("Primary Bond: Jebb Midnight (older brother)") |
| `character_id` | `jebb_midnight` | this card (minted 11/4 for Tori's `relational_refs`) |
| Relation to Tori | older brother, her primary bond | AUTH §Core Bond · [[victoria-midnight]] §Structure, §Relationships |
| Role in the rally car | navigator to her driver; he called the pace notes | slice L8 prose ("He functioned as navigator to her driver") · [[victoria-midnight-L9-eros]] §3 |
| Risk profile | more reckless than Victoria | AUTH §Core Bond |
| System belief | believes in the system more than she does | AUTH §Core Bond · [[victoria-midnight]] §Relationships |
| His dream for her | that she succeeds "the right way" and does not ruin her life chasing dreams like he did | AUTH §Core Bond |
| His pace notes | Type B, technical + human noise: inside jokes, emotional shorthand, personal rhythm indicators | AUTH §Pace Notes |
| Story position | pre-story; the OS-level pre-story bond, not the RS pair | [[oxo-storyform]] §6 (rs_pair: "Jebb remains the OS-level pre-story bond") |
| Death | M1B, Delta Coast Racing | AUTH §Brother Death Event · ssot_04_fabula `m1b_crash_jebb_death` |

## How he dies: two events

- **Believed cause:** `m1b_crash_jebb_death`. Tori overrides the pace notes because she calculates she knows better, and Jebb dies. It is a kernel event, the source of her WOUND and of KINSHIP_COLLAPSE. Actant role: object. (ssot_04_fabula, `confidence: direct_quote`.)
- **True cause:** `m1b_system_removes_jebb` (F8, ruled 2026-10-11). The system (DCUS) removes him as a punitive removal, and Tori reads it as her own crash. It stays untold until the P7 reveal. (ssot_04_fabula, `confidence: inferred`, series bible note OB35.)
- **Purpose of the removal:** "Sever stabilizing attachment and increase asset compliance probability" (AUTH §Brother Death Event, Mode: punitive removal).
- **After:** the data of his death is deleted. In M3, Tori works the transgressive underground for it (ssot_04_fabula `m3_underground_search`; [[victoria-midnight]] §Where she appears).

## What he is to Tori's record

| Tori field | Value | Source |
|---|---|---|
| L5 `relational_refs` | {kind: ghost, character_id: jebb_midnight} | vertical slice, VM fill pass 11/4 |
| L8 `secure_base_object` | brother_deceased | vertical slice L8 |
| Flag KINSHIP_COLLAPSE | FIRED_PRE_STORY at `m1b_crash_jebb_death` | vertical slice §Active Flags |
| L7 `life_script.source` | his dream for her | vertical slice, VM fill pass 11/4 · AUTH §Core Bond |
| L9 `template_origin` | the pace notes, `parallel_presence` | vertical slice L9 · [[victoria-midnight-L9-eros]] §3 |
| Trope register | the SIGNATURE WOUND: a sibling dies in a vehicle disaster | `ShroomsQ/_CANON/_SSOT/01_NARRATIVE_FRAMEWORKS/📐 ssot_01_trope_register.md` |

## Relationships

| Entity | Relation | Source |
|---|---|---|
| [[victoria-midnight]] | younger sister; he was her navigator and secure base | AUTH · slice L8 |
| the Administration / the system | removed him (true cause, untold) | ssot_04_fabula `m1b_system_removes_jebb` |
| [[anna-colson-conway]] | none documented; Anna's node proposes none exists | [[anna-colson-conway]] §Relationships |

## Draft and unruled uses (⧗, not canon)

- The M2 row 9 scene card has the Sync cadence play "Jebb's pace notes, technical layer only" (`_CANON_NODES/oxo-scene-card-M2-row9.md`, draft ⧗).
- The telling profile lists "the narratee as the dead brother" as one menu option. The rec is no explicit narratee (`_CANON_NODES/oxo-telling-profile.md` T10).

## Not documented

Age, appearance, voice and his own LEECHSEED layers are not documented. The dreams "he chased" are not named. Nothing records how far apart the siblings are in age. Nothing is invented here.

## Lineage (STUB, research-grade, not canon)

The 10/29 OXO full script (BOLO 169, `_PRIVATE/BOLO-169/OXO-full-script.txt`) has **no older brother**. In it, Tori is "Ariel"; her family runs a rally team (~L3609), and the grief at the script's centre is for Cain, a friend and mentor (~L2390). The brother-navigator is therefore a later canon development, and the script cannot fill his gaps. BOLO 175's early scripts carry no Jebb material.

## Sources

AUTH = `ShroomsQ/_CANON/_AUTHORITATIVE/OVEREXITOUT/characters/🎯 auth overexitout victoria midnight.md` §Identity, §Movement 1 Origin Commitments, §Core Bond · [`victoria-midnight.md`](victoria-midnight.md) · [`victoria-midnight-L9-eros.md`](victoria-midnight-L9-eros.md) §3 · [`oxo-storyform.md`](oxo-storyform.md) §6 · `ShroomsQ/_CANON/_SSOT/04_PLOT_SYSTEMS/📐 ssot_04_fabula.md` (three events) · `ShroomsQ/_CANON/_SSOT/02_CHARACTER_SYSTEMS/📐 ssot_02_character_systems_vertical_slice.md` (L5, L8, flags) · [`anna-colson-conway.md`](anna-colson-conway.md) §Relationships

**Naming note:** [[victoria-midnight]] links `[[jebb-midnight]]`. This card is filed as `jebb-midnight.md` (renamed 11/4) so the link resolves.
