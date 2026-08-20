---
title: BOM — Kobra S1 Production Cell Startup
type: bill-of-materials
bom_no: BVX-BOM-0001
revision: v1.1 (color specifications added 2026-08-20)
project: BVX / SlimeVR tracker line
parent_assembly: Anycubic Kobra S1 Combo production cell (printer owned — not on BOM)
currency: USD
status: Phase 1 ready to order
source: distilled from `_CLAUDE_ARCHIVE_2026-08-15/files/2026-07-15_kobra-s1-startup-bommd.md` · spreadsheet twins: `KOBRA-S1-STARTUP-BOM.xlsx/.csv`
---

# BILL OF MATERIALS — KOBRA S1 STARTUP

**Machine constants governing all items:** filament Ø **1.75 mm** throughout · plastic spools only in ACE Pro · no matte PLA, no silk · hotend = quick-release cartridge system, official Anycubic only (generic MK8/V6 incompatible) · ACE Pro dry max 55 °C · TPU & CF direct-feed only · **color doctrine: black + light gray + OD green accent, nothing else**

## Phase 1 — Calibration & Prototyping (order now)

| Item № | Part / Description | Specification | Color | Qty | UOM | Unit $ | Ext $ |
|---|---|---|---|---:|---|---:|---:|
| 101 | PLA filament, calibration | 1.75 mm ±0.02, 1 kg plastic spool, regular gloss | Light gray | 1 | spool | 14 | 14 |
| 102 | PLA filament, shape drafts | 1.75 mm ±0.02, 1 kg plastic spool, regular gloss | Black | 1 | spool | 14 | 14 |
| 103 | PETG filament, v1 production | 1.75 mm ±0.03, 1 kg plastic spool | Black | 2 | spool | 17 | 34 |
| 104 | PETG filament, palette accent | 1.75 mm ±0.03, 1 kg plastic spool | OD green | 1 | spool | 17 | 17 |
| 105 | Glue stick, PVP | 22 g, 2-pack (release layer for PETG) | — | 1 | pack | 4 | 4 |
| 106 | IPA 91%+ w/ microfiber ×6 | 1 qt (plate degreasing) | — | 1 | kit | 8 | 8 |
| 107 | Vacuum filament storage kit | ~10 valved bags + pump + silica + hygrometers | — | 1 | kit | 28 | 28 |
| 108 | Hotend unit, spare 0.4 mm | Anycubic Kobra S1 quick-release, brass, official | — | 1 | ea | 18 | 18 |
| | | | | | | **Subtotal** | **137** |

## Phase 2 — Production Readiness (week 1–2, after Phase 1 dialed)

| Item № | Part / Description | Specification | Color | Qty | UOM | Unit $ | Ext $ |
|---|---|---|---|---:|---|---:|---:|
| 201 | ASA filament, production | 1.75 mm, 1 kg plastic spool · dry 70 °C before every run | Black | 1 | spool | 23 | 23 |
| 202 | ASA filament, accent | 1.75 mm, 1 kg plastic spool | OD green | 1 | spool | 23 | 23 |
| 203 | Filament dryer, standalone | Sunlu FilaDryer S2 class, reaches 70 °C | — | 1 | ea | 45 | 45 |
| 204 | Heat-set insert kit, M3 | Brass knurled, ~Ø5.0 × 4.0 mm, ≥100 pcs | Brass | 1 | kit | 18 | 18 |
| 205 | Heat-set installation tips, M3 | Fits standard soldering iron | — | 1 | set | 12 | 12 |
| 206 | Screw assortment, M3 | Socket + button head, 6–20 mm, + nuts/washers | Black-oxide | 1 | kit | 18 | 18 |
| 207 | Hotend unit, 0.6 mm | Anycubic quick-release, brass, official (draft speed) | — | 1 | ea | 20 | 20 |
| 208 | Grease, Super Lube 21030 | Synthetic w/ PTFE, 3 oz | — | 1 | tube | 10 | 10 |
| 209 | PTFE tube + cutter + couplings | 2 m, 1.9 ID × 4.0 OD (Capricorn-class) + PC4-M6 ×4 | — | 1 | kit | 15 | 15 |
| | | | | | | **Subtotal** | **184** |

## Phase 3 — Premium & Expansion (trigger-gated, do not pre-buy)

| Item № | Part / Description | Specification | Color | Qty | UOM | Unit $ | Ext $ | Trigger |
|---|---|---|---|---:|---|---:|---:|---|
| 301 | Hotend unit, hardened 0.4 mm | Anycubic all-metal hardened, official | — | 1 | ea | 28 | 28 | Before any CF filament |
| 302 | PETG-CF filament | 1.75 mm, 1 kg · **direct feed only** · hardened hotend only | Black (inherent) | 1 | spool | 28 | 28 | Premium-tier enclosure demand |
| 303 | TPU 95A filament | 1.75 mm, 1 kg · **direct feed only** | Black | 1 | spool | 22 | 22 | Gasket/bumper part designs exist |
| 304 | Build plate, second | Official Kobra S1, opposite finish to shipped | — | 1 | ea | 28 | 28 | Throughput or finish need |
| 305 | Smart plug + smoke detector | Kasa-class wifi plug + detector at printer | — | 1 | set | 25 | 25 | First unattended production run |
| 306 | Carbon filter, BentoBox style | Pellets purchased; box printed in-house (item 103 stock) | Black | 1 | ea | 10 | 10 | First ASA production block |
| | | | | | | **Subtotal** | **141** | |

## Rollup

| Phase | Ext $ | Cumulative |
|---|---:|---:|
| 1 — Calibration & prototyping | 137 | 137 |
| 2 — Production readiness | 184 | **321 ← the productive core** |
| 3 — Premium & expansion | 141 | 462 |

**Do-not-buy (standing):** generic nozzle packs · enclosure tents · boutique adhesion fluids · filament sampler multipacks · matte PLA · drying cabinets.

**Commissioning:** first-72-hours sequence lives in the source doc §7 — firmware → auto-cal suite → Benchy → dimensional truth test (calipers) → PETG dried 6–8 h → enclosure draft v1 → named slicer profiles per material.
