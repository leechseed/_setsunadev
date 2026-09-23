---
id: L2b.FACE
title: "Facial Morphology — the substrate and coordinate system"
type: layer-spec
layer: L2b_MORPHOLOGY
module: face
status: draft
confidence: medium
trunk: BOTH
views: [character-generation, aesthetic-taxonomy]
sources:
  - "gap-face-anatomy.md"  # extraction register; inline citations carried through in §6
created: 2026-09-23
---

# Facial Morphology

One causal substrate, ported from [[L2b-morphology-gluteal.md|the gluteal node]]. One coordinate system, three axes in place of three. One taxonomy, named as outputs. The chain survives the port; two of its four stages don't survive it unchanged.

> **The governing claim, carried over:** shape is skeletal first. Muscle, fat, and skin modulate a frame they cannot redraw. The face keeps that claim and breaks two of the body's assumptions along the way — where it breaks is the finding, not a defect in the port.

---

## 1 · The substrate — four stages, two deviations

```
SKELETON    cranial vault · brow ridge · orbital rim · zygomatic arch · nasal bones · maxilla · mandible
   ↓        Immovable. Sets the ceiling — forensic reconstruction's own claim about the same bones.
MUSCLE      MIMETIC sheet (expression, non-volumetric) · MASTICATORY block (masseter + temporalis, volumetric)
   ↓        Two mechanisms sharing one stage name. The first deviation.
FAT         compartmentalized, bidirectional: deep pads atrophy/descend · superficial pads hypertrophy — same clock
   ↓        modulates every read. The second deviation — the body's fat doesn't run two directions at once.
CONDITION   skin — texture · laxity · hydration · colour · vascularity
            where believability and age both live
```

**SKELETON** is bone: cranial vault (forehead height/slope), brow ridge (the strongest sexually-dimorphic skeletal cue), orbital rims (anchor tissue tightly — one of the lowest-deviation regions under the soft tissue), zygomatic arches (cheekbone width, zygion the landmark for bizygomatic width), nasal bones (nose width/bridge), maxilla (midface projection, philtrum support), mandible (ramus, gonial angle, symphysis). Same functional role as the pelvis in the body model: fixed, sets the silhouette, nothing below it can redraw it.

**MUSCLE — deviation 1.** Mimetic muscles (frontalis, orbicularis oculi, orbicularis oris, zygomaticus, levator labii, depressor anguli oris, mentalis, platysma) drive expression, not resting bulk — fast-twitch, brief-burst, and they lack the muscle spindles that reset resting tone in ordinary skeletal muscle. Resting facial form is shaped less by "tone" than by chronic contraction habit (static expression lines) sitting over whatever the skin/fat/bone beneath is doing — not a volume block the way a trained biceps reads. Masseter and temporalis behave like body muscle: real, trainable volume. Masseter hypertrophy widens the jaw corner; temporalis bulk fills the temple hollow. Both atrophy with age, and that atrophy feeds back into SKELETON — reduced loading correlates with bone-density loss at the ramus and zygomatic arch. The body chain has no such feedback loop; bone there never waits on muscle.

**FAT — deviation 2.** Fat sits in named pads, split superficial/deep by a membranous system, not one distribution layer. Deep pads (periorbital, buccal, deep medial cheek) atrophy and ptose. Superficial pads (submental, jowl, nasolabial, lateral malar) hypertrophy on the same clock. Top deflates while bottom descends and thickens — one aging silhouette produced by two opposite tissue behaviors, not the body model's single gain/loss axis. Carry this as two sub-vectors rather than one level × pattern pair:

```
DEEP         ↓↓ very high atrophy … ↔ stable … ↑ resistant   (periorbital, buccal, deep medial cheek)
SUPERFICIAL  ↑↑ very high hypertrophy … ↔ stable … ↓ resistant  (submental, jowl, nasolabial, lateral malar)
```

**CONDITION** carries the same functional role as the body's: the visible surface — texture, laxity, hydration, colour, vascularity — where believability and age both live.

---

## 2 · The coordinate system

Three axes, three positions each, mirroring `I·F·T`. **27 cells.**

| Axis | 1 | 2 | 3 |
|---|---|---|---|
| **FI — Facial index** (bizygomatic width ÷ nasion–menton height × 100) | low — narrow, long face | medium — canonical proportion | high — wide, short face |
| **G — Gonial angle** (Ar–Go–Me) | narrow — sharp, square jaw read | medium — ~120–130°, typical adult | wide — soft, round jaw read |
| **E — Eye spacing** (rule of fifths: intercanthal distance vs. one eye-width) | close-set — under one eye-width | medium — ≈ one eye-width, canonical | wide-set — over one eye-width |

Notation: **`FI2·G2·E2`** = canonical facial index, typical gonial angle, canonical eye spacing — the mesoprosopic mid-cell. A cell is addressed the same way the body's is: three digits, one per axis, no separator ambiguity.

---

## 3 · Derived features

Not shapes. Consequences of the stages above, read the way the body node's Frame/Tissue/Condition/Line vocabulary reads them.

| Feature | Derivation |
|---|---|
| **Frame** | `FI·G·E` — the 27 cells. Immovable; forensic reconstruction's own working assumption. |
| **Tissue** | MIMETIC habit (non-volumetric) + MASTICATORY volume, then DEEP atrophy × SUPERFICIAL hypertrophy — two sub-chains, not one. |
| **Condition** | Skin texture · laxity · hydration · colour · vascularity. |
| **Line** | The silhouette read — the output of all four stages at a glance. |
| **Archetype** | Frame + Tissue + Condition resolved to one of §4's named reads, or unnamed mid-cell. |

Line and Archetype are reads, not stages: nothing is generated at them.

---

## 4 · The taxonomy — named face reads

Named at recognizable clusters, not all 27 cells. These are **outputs of the cells, not generators of them** — the same discipline the body node enforces on its thirteen types.

| Type | Cell | Read |
|---|---|---|
| **The Pediment** | `FI1·G1·E1` | Long, narrow face; sharp gonial angle; close-set eyes. Vertical, angular, no lateral spill. |
| **The Rotunda** | `FI3·G3·E2` | Wide, short face with a soft, round jaw. The bubble equivalent — full curve, no long axis to interrupt it. |
| **The Voussoir** | `FI2·G1·E2` | Canonical proportion with a sharp jaw. The wedge taper: proportion at the top, angle at the bottom. |
| **The Transom** | `FI3·G1·E3` | Wide, short face with a sharp gonial angle despite the width, and wide-set eyes. Horizontal band read. |
| **The Impost** | `FI1·G3·E2` | Narrow, long face carrying a soft, round jaw — a vertical frame with no angular finish at the base. |
| **The Spandrel** | any cell + DEEP ↓↓ · SUPERFICIAL ↑↑ | The frame reads one way; the fat compartments push a heavier lower read against it — hollow midface, forward jowl and nasolabial fold. The fat-driven type, not the skeleton-driven one; included because the finding is that fat can outvote the frame here in a way it can't on the body. |

**Explicit note on the popular family.** The oval/round/square/heart/diamond taxonomy in circulation is hairdressing/styling convention, not a medical or scientific classification — stated in the sourced material directly, not inferred here. The neoclassical canon it draws on (equal thirds/fifths) failed to validate outside its origin population, in an Arabian Peninsula sample. This system uses the continuous landmark ratios instead — facial index, gonial angle, eye-spacing fraction — because they are measured and reproducible, and their cross-population variance is a stated caveat rather than a fact hidden inside a bucket label.

---

## 5 · The cell-call procedure

```
1  POPULATION   [name]                         → prior FI·G·E · masticatory/mimetic loading fingerprint
2  TELLS        [observation 1] · [observation 2] · [observation 3]
3  CALL         FI·G·E · POPULATION · nearest: [type] · override: [flag]
```

**Line 1** supplies the population prior. **Line 2** narrows the frame with observed tells, one axis each. **Line 3** records the final cell, population name, nearest named type, and override flag (`none · filler · implant · surgical · unknown`).

---

## 6 · Sourced versus derived

**Sourced:** the seven skeletal landmarks and their read (cranial vault, brow ridge, orbital rims, zygomatic arch, nasal bones, maxilla, mandible); the mimetic/masticatory muscle split and the spindle mechanism behind it; masseter/temporalis hypertrophy-to-bone feedback; the named fat compartments and their deep-atrophy/superficial-hypertrophy split (Rohrich & Pessa); the facial index formula and its cross-population caveat; the gonial angle range (~120–130°, 115–130° aesthetically preferred); the rule-of-fifths eye-spacing convention; the failed validation of neoclassical canons outside their origin population; skin-condition drivers (photoaging texture/laxity, sleep's measured ~30% recovery differential, stress/cortisol effects on collagen and circulation). All carried from `gap-face-anatomy.md`'s own inline citations.

**Derived:** the 27-cell `FI·G·E` coordinate system, all six named types, the DEEP/SUPERFICIAL fat-vector notation, the cell-call procedure, and the Frame/Tissue/Condition/Line mapping. `gap-face-anatomy.md` names a landmark spine and a mechanism; it does not systematize either into a scored coordinate system or a taxonomy. This document is an extension of that mechanism, not a report of its findings — the same relationship the gluteal node has to its own source text.

**Unsourced, flagged rather than invented:** the dose-response relationship between substances/lifestyle factors (alcohol, smoking, hydration) and CONDITION. `gap-face-anatomy.md` names these as degrading factors but found no numeric range attached to any of them, and none is stated here.

---

## 7 · Operating notes

This layer feeds a 3D sculpt. The four stages do not fall on one tool the way they might look like they do on paper.

- **Geometry, base mesh — SKELETON.** Cranial vault, brow ridge, zygomatic arch, nasal bones, maxilla, mandible (including gonial angle and symphysis) are blockout: fixed topology decisions made once, at the skeleton pass, before any soft-tissue sculpt layer goes on.
- **Geometry, soft-tissue sculpt — MASTICATORY muscle and FAT.** Masseter/temporalis volume and both fat sub-vectors (DEEP displacement, SUPERFICIAL displacement) are geometry, but on a separate sculpt layer from the base mesh — this is where the model gets fuller or gaunter without changing the underlying frame.
- **Rig, not geometry — MIMETIC muscle.** The expression sheet belongs on blend shapes or a rig, not on static geometry: it is habit and motion, not a volume block, and sculpting it as fixed geometry would misrepresent what the sourced mechanism says it is.
- **Shader/texture, no geometry — CONDITION.** Skin texture, laxity, colour, and vascularity are texture and shader work — diffuse/roughness/subsurface maps — not mesh displacement. Nothing at this stage should move a vertex.
