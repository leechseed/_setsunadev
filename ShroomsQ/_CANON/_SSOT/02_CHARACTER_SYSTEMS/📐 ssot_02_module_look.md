---
type: ssot_02_character_systems
category: field_module
module_of: ssot_00_module_architecture
version: 1.0.0
tier: standard
last_updated: 2026-10-12
applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD]
status: "v1.0.0 2026-10-12 RULED (Chief: 'All recommendations … Go layers'): tier 2 floor, L2 VITAL attachment, the static/dynamic split, the one-at-a-time accept rule, the new part and hair keys on the shared rail. Overlap with MOD.PHYS and MOD.FASHION is OPEN (call 6). v0.1.0 2026-10-12 draft."
trunk: BLACK
purpose: "Defines LOOK, the field module that holds a character's appearance as six layers of label keys, and the two-way sync between those keys and the private reference-image database."
dependencies: ["ssot_00_module_architecture", "ssot_00_module_registry", "ssot_02_character_state_architecture", "ssot_02_character_astrology_12_layer_mapping"]
rung: standard
---
# 📐 SSOT: Module LOOK (Appearance)

## Table of Contents

1. [Purpose](#purpose)
2. [Module Declaration](#module-declaration)
3. [The Six Layers](#the-six-layers)
4. [Label Keys](#label-keys)
5. [The Sync Contract](#the-sync-contract)
6. [Feeds and the Independence Boundary](#feeds-and-the-independence-boundary)
7. [State Diffs](#state-diffs)
8. [Registry entry (to add on ruling)](#registry-entry-to-add-on-ruling)
9. [OPEN calls for Chief](#open-calls-for-chief)
10. [Version History](#version-history)

---

## Purpose

LOOK is a field module that records how a character appears. It stores every value as a label key from one shared vocabulary. The same keys tag the private reference-image database, so a character and its pictures find each other by key.

Chief, 10/12: "the first layer would be bodies. So all body parts. The second layer would be like style … clothing … reference to the character designer or the character creator" and "I'll need it to be able to sync with the character portion of BoldVenture."

---

## Module Declaration

```yaml
MODULE_DECLARATION:
  module_id: LOOK
  display_name: Appearance
  version: 1.0.0
  author: LEECHSEED
  attachment_points: [VITAL]
  tier_min: 2
  depends_on: []
  description: Holds a character's appearance as six layers of shared label keys that sync both ways with the private reference database.
```

- **Attachment point (RULED 2026-10-12).** LOOK attaches to L2 VITAL alone. L2 covers physical presence, and the Ascendant sets how the body reads in space.
- **Tier requirement (RULED 2026-10-12).** Tier 2 and up. A background character needs no appearance record.
- **Dependencies.** None. LOOK reads core layers L2 and L7 but needs no other module.
- **READS.** `T1.VITAL.base_value` (layer 1 feed) and the L7 ORIGIN heritage fields (layer 2 suggestions).
- **WRITES.** Own variables only: `MOD.LOOK.*`.
- **DERIVED and FLAGS.** None.

---

## The Six Layers

The six layers follow the order of a character creator. Layer 1 comes first and layer 6 last. A layer is a group of variables, not a core layer.

All variables are `authored`, default `[UNASSIGNED]`, scale class N/A. The Static and Dynamic tags are RULED (2026-10-12, "All recommendations"): static holds build, height, skin tone, eye color, face shape and focus; dynamic holds age read, hair, wardrobe, pose, scene and vibe.

### Layer 1: Body

|Path|Type|Allowed values (label keys)|Tag|Why|
|---|---|---|---|---|
|`MOD.LOOK.body.build`|enum|slight, lean, athletic, average, curvy, broad, heavy|Static (rec)|Frame is fixed at the base record.|
|`MOD.LOOK.body.height`|enum|short, average, tall|Static (rec)|Height does not change in a story.|
|`MOD.LOOK.body.skin_tone`|enum|deep, brown, tan, olive, light, fair|Static (rec)|Skin tone is a birth trait.|
|`MOD.LOOK.body.focus`|array_enum|general, shoulders, arms, hands, waist, legs, back|Static (rec)|Focus names the feature the character is known for.|

### Layer 2: Face and hair

|Path|Type|Allowed values (label keys)|Tag|Why|
|---|---|---|---|---|
|`MOD.LOOK.face.shape`|enum|oval, round, square, heart, long|Static (rec)|Bone structure does not change.|
|`MOD.LOOK.face.eye_color`|enum|brown, hazel, green, blue, gray, amber|Static (rec)|Eye color is a birth trait.|
|`MOD.LOOK.face.age_read`|enum|youthful, prime, mature, weathered|Dynamic (rec)|Apparent age shifts with years and hardship.|
|`MOD.LOOK.hair.style`|enum|straight, wavy, curly, coily, braids, bun, ponytail, buzz, bald|Dynamic (rec)|Characters restyle hair over a story.|
|`MOD.LOOK.hair.color`|enum|black, brown, auburn, blond, red, gray, dyed|Dynamic (rec)|Color changes by dye or age.|
|`MOD.LOOK.hair.length`|enum|short, shoulder, long|Dynamic (rec)|Hair grows and gets cut.|

### Layer 3: Wardrobe

|Path|Type|Allowed values (label keys)|Tag|Why|
|---|---|---|---|---|
|`MOD.LOOK.wardrobe.dress`|enum|vocab axis `dress`, SFW keys: clothed, swim|Dynamic (rec)|What a character wears changes scene to scene.|
|`MOD.LOOK.wardrobe.styling`|enum|vocab axis `styling`, SFW keys: gym, casual, streetwear, alt, office, swim, cosplay, none|Dynamic (rec)|Style shifts with era, job, and mood.|

### Layer 4: Pose and framing

|Path|Type|Allowed values (label keys)|Tag|Why|
|---|---|---|---|---|
|`MOD.LOOK.pose.framing`|enum|vocab axis `framing`, SFW keys: full, threeq, waist, face|Dynamic (rec)|Framing belongs to one picture, not the character.|

### Layer 5: Scene

|Path|Type|Allowed values (label keys)|Tag|Why|
|---|---|---|---|---|
|`MOD.LOOK.scene.setting`|enum|vocab axis `setting`: bedroom, bathroom, gym, car, beach, outdoors, public, home, backdrop, street|Dynamic (rec)|A scene is one place at one time.|
|`MOD.LOOK.scene.register`|enum|vocab axis `register`: studio, editorial, mirror, selfie, candid, render, ai, illustration|Dynamic (rec)|Register is the photo style of one picture.|

### Layer 6: Vibe

|Path|Type|Allowed values (label keys)|Tag|Why|
|---|---|---|---|---|
|`MOD.LOOK.vibe.mood`|enum|vocab axis `mood`, SFW keys: playful, soft, fierce, candid, dominant, sultry, bratty|Dynamic (rec)|Mood moves with events.|

**Variable count: 16** (4 + 6 + 2 + 1 + 2 + 1).

**Lane is a filter, not a layer.** A query carries `lane: straight` and `gender: male` as filters on the reference database. LOOK stores neither as a variable. Acts and kinks stay off the character stack entirely.

---

## Label Keys

**The rule.** Every LOOK value is a key from the shared vocabulary. LOOK never stores free text. A key means one thing in the character, in the taxonomy engine, and in the reference database.

**Where the keys come from.** The six axes `register`, `dress`, `setting`, `styling`, `mood`, and `framing` come verbatim from `_PRIVATE/taxonomy_engine/vocab.json`. The body, face, and hair keys above are new plain descriptors. Chief rules them in, then they join the vocabulary.

**SFW keys listed in this public doc:**

- **register:** studio, editorial, mirror, selfie, candid, render, ai, illustration
- **dress:** clothed, swim
- **setting:** bedroom, bathroom, gym, car, beach, outdoors, public, home, backdrop, street
- **styling:** gym, casual, streetwear, alt, office, swim, cosplay, none
- **mood:** playful, soft, fierce, candid, dominant, sultry, bratty
- **framing:** full, threeq, waist, face
- **body, face, hair:** the keys in the tables above

**The private rest.** The vocabulary holds more keys than this doc lists. Every explicit label exists only in the private reference database under `_PRIVATE/`, which git ignores. This doc refers to those labels by key and never writes them out. The repo is public.

---

## The Sync Contract

The sync runs both ways between a character's LOOK fields and the private reference database. The author holds the only write access to a character.

### (a) Character to references

1. The tool reads the character's `MOD.LOOK.*` values, one key per variable.
2. The tool builds a query. Each assigned variable is a layer key. `[UNASSIGNED]` variables are skipped. The lane filter adds `straight` and `male`.
3. The tool searches the private database for images tagged with those keys.
4. The tool ranks matches by label source: human first, then board, then automatic. A human label always outranks the other two.
5. The tool returns matching images with the layers each one matched. A partial match shows which layers missed.
6. The tool writes nothing to the character.

### (b) References to character

1. The author picks one or more reference images.
2. The tool reads each picked image's labels, by the same precedence: human, then board, then automatic.
3. The tool proposes a value for each layer. When picked images disagree on a layer, it shows every candidate with a count.
4. The author accepts or rejects each proposed value, one layer at a time.
5. The tool writes only accepted values into `MOD.LOOK.*`.
6. **Nothing writes to a character without the author's accept.** No batch accept, no silent fill, no automatic overwrite.

---

## Feeds and the Independence Boundary

### L2 VITAL feeds layer 1

L2 VITAL holds body capital. The Ascendant sets how the body reads in space (L2 section, Character Astrology mapping). The tool shows the VITAL value and the Ascendant read beside the layer 1 fields. Rec: high VITAL suggests `athletic` or `lean`. These are suggestions. The author rules each field.

### L7 ORIGIN heritage feeds layer 2 defaults

The heritage roll (`_tools/leechseed/heritage.py`, W1-B) outputs a group mix and a roots table per character. The tool reads that mix and suggests defaults for `body.skin_tone`, `face.shape`, `face.eye_color`, and `hair.*`. A suggestion shows as a candidate only. The roll cannot fill a field. The author accepts each one, as in sync step (b).

### Independence boundary

LOOK reads core layers L2 and L7 and writes only `MOD.LOOK.*`. LOOK never writes into any core layer. A change to LOOK never changes VITAL, ORIGIN, a derived stat, or a flag. The core system runs the same with LOOK disabled, per the module deactivation rule.

---

## State Diffs

Static fields stay in the base record. Dynamic fields enter a state diff under `MODIFIED_VALUES`, in the `MOD.LOOK` namespace. A diff lists only the values that changed.

```yaml
origin_event: m2c_new_term_begins
state_diffs:
  MODIFIED_VALUES:
    MOD.LOOK.hair.style: braids       # was straight
    MOD.LOOK.hair.color: dyed         # was black
    MOD.LOOK.wardrobe.styling: alt    # was casual
```

Overlay resolution follows the state architecture. The base record supplies every omitted value. The latest diff at or before the narrative moment wins.

---

## Registry entry (added 2026-10-12)

The Registry Overview table and the Active Modules section carry this entry since the ruling (registry 1.3.0).

|Module ID|Display Name|Attachment|Tier|Status|Variables|Derived|Flags|
|---|---|---|---|---|---|---|---|
|`LOOK`|Appearance|L2 VITAL|2|**active** (1.0.0)|16|No|No|

```yaml
MODULE_DECLARATION:
  module_id: LOOK
  display_name: Appearance
  version: 1.0.0
  author: LEECHSEED
  attachment_points: [VITAL]
  tier_min: 2
  depends_on: []
  description: Holds a character's appearance as six layers of shared label keys that sync both ways with the private reference database.
```

Full variable declarations live in [📐 ssot_02_module_look.md](📐%20ssot_02_module_look.md).

---

## Calls

RULED 2026-10-12 (Chief: "All recommendations, and the fable switch is done. Go layers."), recs taken as written:

1. **Tier floor.** LOOK starts at Tier 2. Tip: Tier 2 skips extras who never appear on a page.
2. **Attachment point.** LOOK attaches to L2 VITAL alone. Tip: one point keeps the module simple; L3 can join later if wardrobe needs it.
3. **Static or dynamic.** Static: build, height, skin tone, eye color, face shape, focus. Dynamic: age read, hair, wardrobe, pose, scene, vibe. Tip: static fields never clutter a state diff.
4. **Accept rule.** The author accepts every proposed value one at a time; there is no accept-all. Tip: one-at-a-time keeps a reference from silently rewriting a character.
5. **New body, face, and hair keys.** The new descriptors joined the shared vocabulary the same day, as two rail axes: `part` (the body focus, keyed to the part names the reference boards use) and `hair` (color). Provisional until Chief reads the lists. Tip: the reference database tags images by them from the next automatic pass on.

OPEN:

6. **Overlap with MOD.PHYS and MOD.FASHION.** PHYS's `body_type` and `age_presentation` now have homes in LOOK layers 1 and 2, and FASHION's `body_display` sits inside LOOK's wardrobe `dress`. Rec: PHYS stays planned for what LOOK does not hold (`physicality_source`, `distinguishing_marks`, `beauty_read`, `physical_confidence`); FASHION stays planned for the social-signal fields and drops `body_display` to LOOK. Tip: a field lives in one module, so the registry's audit table records where each moved.

---

## Version History

|Version|Date|Changes|
|---|---|---|
|1.0.0|2026-10-12|RULED, Chief ("All recommendations … Go layers"): calls 1 to 5 taken as recommended. `attachment_points` written `[VITAL]` to match the registry. The `part` and `hair` axes joined the shared vocabulary (private rail file) the same day. Registry 1.3.0 carries the entry. Call 6 (PHYS and FASHION overlap) opened.|
|0.1.0|2026-10-12|Draft. Six layers in character-creator order, 16 variables, two-way sync contract, feeds from L2 VITAL and L7 ORIGIN, state-diff example. Awaiting Chief's ruling on five OPEN calls.|
