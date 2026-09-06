---
title: WATCH — the long-session register (working name)
type: design-register
version: 1.0.0
date: 2026-09-06
bolo: 34
status: applied to WARROOM 1.1; filing into the Bold Venture design system SSOT (fifth register beside EMBER · PUNCH · DUST · NOIR) is Papi's open ruling (BOLO 34 Q2)
derived_from: _0.1_BVX_LEARN/_meta/LONG-WATCH-STANDARDS.md (MIL-STD-1472H · MIL-STD-2525D · FAA HF-STD-001B + HF-STD-010A · NASA-STD-3001 Rev F + HIDH · ISO 9241-303 · IHO S-52 · Piepenbrock/Buchner/Mayr · Dobres 2017)
environment: one monitor, off-axis to the operator's left, overhead room light ON, sessions of 4–8 h, viewing distance assumed ~60 cm
trunk: BLACK
---

# WATCH — the long-session register

**One register, two faces, keyed to the room light.** The standards do not prefer dark themes for comfort; they key polarity to ambient light (MIL-STD-1472H 5.2.2.6: light-on-dark only below ~0.1 lx; FAA HF-STD-001B 5.3.2.1.6: positive polarity "when all else is equal"; the bridge clause 5.18.2.2: "separate day and night color palettes may be necessary"). Papi's room is lit. So **DAY is the working face** and NIGHT is for the light switched off. Both faces share one grammar.

## The grammar (Papi's ruling on BOLO 34 Q6: judgment colors, borrow the Navy's yellow)

| Role | Meaning | Source of the meaning |
|---|---|---|
| ink | reading text, 9–11:1 on the ground; never pure white on dark, never pure black on light | MIL-STD-1472H 5.2.2.7 (6:1 min, 10:1 preferred); FAA Exhibit 5.6.2.2.1 (>7:1 continuous reading) |
| link | a glossary term; the CK3 concept link | CK3 study R1; FAA 5.6.6.2.2.14 (never pure blue on dark → aqua at 60–70% luminance on the night face) |
| good | normal, held, in tolerance | MIL-STD-1472H Table XV; NASA Table 10.4-3 |
| warn | caution, pending, **unknown / unruled** | MIL-STD-1472H Table XV yellow = caution; MIL-STD-2525D yellow = unknown (the borrow) |
| bad | critical, failed, what does not work | MIL-STD-1472H Table XV red |
| help | captions, sources, asides | CK3 blue-gray help text |
| accent | selection, focus, the active sheet — the Bold Venture ROSE anchor, one hue, ≥20 ΔE from every status hue | design system v2.0.0; MIL-STD-1472H 5.17.26.2 (two brightness levels, ≥2:1 apart) |
| mark | a reader's `==highlight==` | 📐 ssot_05_operations_markdown_marking |

Hue budget: seven meaningful hues (link · good · warn · bad · help · accent · mark) on grayscale chrome. FAA 5.6.6.2.7.5 allows six recalled meanings per screen; mark is not a meaning, it is a location. MIL-STD-2525 affiliation colors are **not used**: WARROOM has nothing to classify as friend or hostile (rule 7 of the standards synthesis: reconcile by layer, and there is no symbol layer).

## DAY face — positive polarity, lit room

| Token | Value | Contrast on ground | Rule |
|---|---|---|---|
| bg | `#ECE5DF` | 79% of white, L* 91 | paper, not white: reflections read less on a bright ground (FAA 5.3.2.1.6) but a full-white field over-drives a 300–500 lx room (ISO 9241-303 5.2.4 office example 100–150 cd/m²) |
| panel / panel-2 | `#F5F0EC` / `#E2D9D3` | — | two levels, chrome only |
| ink | `#372A2F` | 11.0:1 | inside 10:1 preferred; contrast control: soft `#4A3C42` 8.4:1 · high `#221619` 14.1:1 |
| ink-2 | `#5A4B51` | 6.6:1 | secondary text, MIL 4.5–6:1 band, rounded up for 4–8 h |
| ink-3 | `#7E6E75` | 3.8:1 | chrome only, never reading (HF-STD-010A floor 3:1) |
| accent | `#8A1F44` | 7.1:1 | ROSE, unchanged; ΔE 37 from bad |
| link | `#2B5F9E` | 5.2:1 | desaturated blue; blue on light is not a forbidden pair |
| good | `#2E6B3F` | 5.1:1 | |
| warn | `#7A5D06` | 5.0:1 | ochre, because yellow on white is a forbidden pair (FAA Exhibit 5.6.6.2.5.2) |
| bad | `#B03A22` | 4.8:1 | orange-red, held ≥20 ΔE from ROSE |
| help | `#55627A` | 4.9:1 | |
| mark | `#F3E6B4` | ink on mark 12:1 | pale amber fill behind dark text; not yellow text |

## NIGHT face — negative polarity, dark room

| Token | Value | Contrast on ground | Rule |
|---|---|---|---|
| bg | `#1C191B` | 1.0% of white, L* 8 | ≈1–2 cd/m² at a 110 cd/m² white: under FAA's 2 cd/m² black cap (5.3.1.9.7), near S-52's 1.3 cd/m² night ceiling; not #000000 |
| ink | `#CFC6C8` | 10.4:1 | 78–85% luminance band; pure white reserved for the selected state (FAA 5.6.6.3.7); soft `#B5ABAE` 7.8:1 · high `#E6DEE0` 13.2:1 |
| ink-2 / ink-3 | `#A0959A` / `#7B7176` | 6.0:1 / 3.7:1 | |
| accent | `#D25A82` | 4.6:1 | ROSE lifted to clear 4.5:1 on the night ground |
| link | `#6CC3D9` | 8.7:1 | aqua near HF-STD-010A's validated `07CDED`, desaturated; never pure blue on dark |
| good | `#7EC38F` | 8.4:1 | |
| warn | `#D9B65A` | 9.0:1 | amber, far from the mark fill |
| bad | `#E58A70` | 6.8:1 | coral, because red on black is a forbidden pair for text |
| help | `#9AA7B8` | 7.1:1 | |
| mark | `#4A3F1E` | ink on mark 6.2:1 | dark amber fill |

## Type

Body 17 px ≈ 18 arcmin at 60 cm; thesis 18 px; tooltips 15 px ≈ 16 arcmin; nothing read below 14 px; chrome labels 11–12 px (above the 10 arcmin floor). Window: FAA 5.6.2.5.6.5-9 (20–22 preferred, 16 minimum, 24 maximum); MIL-STD-1472H 5.17.18.2 (≥10, should be ≥15). Regular and semibold weights only; the polarity penalty falls on small thin type (Piepenbrock, Mayr, Buchner 2014; Dobres, Chahine, Reimer 2017).

## What the app cannot do, and the operator can

- **Surround.** Keep the wall behind the monitor within 1/3 to 3× the screen's luminance and never darker than 1/10 (MIL-STD-1472H Table XXII; ISO 9241-303 5.2.4). With the overhead light on, DAY face; light off, NIGHT face. The theme button says which.
- **Off-axis monitor.** The screen sits to the left. Rotate it to face the chair or accept contrast loss at the far edge; the standards assume on-axis viewing (MIL-STD-1472H 5.2.2.11).
- **Monitor white.** Set it near 100–150 cd/m² in a lit room, lower at night; dim first, warm second (NASA-STD-3001 Rev F Table 8.7-2; Figueiro 2016).
- **Breaks.** Not built in; the 20-20-20 rule has no supporting evidence (Johnson and Rosenfield 2023).

## Applied

WARROOM 1.1 (`MCDP-CODEX.html`, `_tools/mcdp_codex_template.html`): both faces as the light/dark token blocks, theme button relabeled *day · lit room / night · dark room / auto*, a three-step contrast control, type raised to the arcminute window. DARKROOM untouched by ruling (BOLO 34 Q1: WARROOM only for now).

## Open

1. **Filing** (BOLO 34 Q2): a fifth register in `📐 ssot_00_bold_venture_design_system.md`, or a WARROOM-only theme. The name WATCH is a working name.
2. **DARKROOM.** Its NOIR livery is pure-black-adjacent with white-ish text; the same two faces would apply. Waits on Papi's word after living in WARROOM 1.1.
3. **Viewing distance** assumed 60 cm; if the monitor sits farther, body type goes to 18–19 px.
