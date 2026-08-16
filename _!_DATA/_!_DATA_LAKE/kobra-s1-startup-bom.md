# Kobra S1 + ACE Pro — Production Startup BOM

**Owner:** BVX / SlimeVR tracker line
**Machine:** Anycubic Kobra S1 Combo (enclosed CoreXY + ACE Pro 4-slot)
**Mission:** Product parts — tracker enclosures, functional prototypes
**Budget band:** $250–500 accessories · **Assumes:** solid existing tool collection (calipers, cutters, hex keys, hobby knives, soldering iron — anything you don't have from that list, add it back)

---

## Table of Contents

1. [Know Your Machine — Facts That Shape This List](#1-know-your-machine)
2. [Phase 1 — Calibration & Prototyping (order today)](#2-phase-1--calibration--prototyping)
3. [Phase 2 — Production Readiness](#3-phase-2--production-readiness)
4. [Phase 3 — Premium Finish & Expansion (optional)](#4-phase-3--premium-finish--expansion)
5. [Filament Strategy for Enclosures](#5-filament-strategy-for-enclosures)
6. [Budget Summary](#6-budget-summary)
7. [First 72 Hours — Commissioning Order](#7-first-72-hours--commissioning-order)
8. [Do-Not-Buy List](#8-do-not-buy-list)

---

## 1. Know Your Machine

Facts that determine what's on (and off) this list:

| Fact | Consequence |
|---|---|
| Hotend is a **tool-free quick-release unit** (nozzle + heatbreak + wiring as one cartridge, up to 320°C) | You don't buy loose nozzles — you buy whole hotend units. A spare = zero-downtime clog recovery. Generic MK8/V6 nozzles do not fit. |
| Ships with **0.4mm hotend**; 0.2 / 0.6 / 0.8 sold separately, hardened-steel versions available | 0.6 is your fast-draft unit; hardened steel only needed for carbon-fiber filaments. |
| **ACE Pro dries at max 55°C** (dual 200W PTC, can dry while printing, up to 24h) | Fine for PLA/PETG maintenance drying. **Not hot enough for ASA/ABS/nylon** — those need a standalone 70°C dryer. |
| **TPU is single-color, direct-feed only** — it cannot run through the ACE Pro | Flexibles go on the external spool holder, not in the box. |
| **Carbon/glass-fiber filaments should not feed through the ACE** (wears the internal channels) | CF materials = direct feed + hardened hotend. Phase 3 only. |
| **Matte PLA has known compatibility problems in the ACE Pro** (false tangle detection) | Skip matte PLA. Get the matte look from ASA (naturally satin) or the textured plate. |
| ACE Pro mounts on the **left side** of the printer; avoid cardboard spools in it | Plan your desk layout; buy plastic-spool filament or print an adapter ring. |
| Slicer: **Anycubic Slicer Next** (Orca-based) or OrcaSlicer | Free. No software spend. |

---

## 2. Phase 1 — Calibration & Prototyping

Goal: dialed-in machine, verified dimensional accuracy, first enclosure drafts in PETG. Order all of this today.

| Item | Spec / example | Est. | Why |
|---|---|---:|---|
| PLA, 2× 1kg | Any reputable basic (Elegoo, Sunlu, Anycubic) — regular finish, **not matte** | $28 | Calibration prints and fast shape iterations. Cheapest way to burn through design mistakes. |
| PETG, 3× 1kg | Overture or Polymaker PolyLite; make one spool your candidate production color | $50 | The v1 enclosure material — tough, slightly flexible, ~75°C heat tolerance, prints happily enclosed. |
| Glue stick, 2-pack | Plain PVP (Elmer's disappearing purple works) | $4 | On PETG it's a **release layer** — PETG can bond so hard to PEI it tears the coating. Also adhesion insurance later for ASA. |
| IPA 91%+ + microfiber cloths | Quart bottle | $8 | Plate degreasing between prints. Skip if already stocked. |
| Vacuum storage bag kit | ~10 bags with valves, hand pump, rechargeable silica gel, mini hygrometers | $28 | [CITY] humidity is your #1 print-quality enemy. Every spool not in the ACE lives in a sealed bag. |
| Spare 0.4mm hotend unit | Anycubic Kobra S1 quick-release, official | $18 | Clog at 11pm mid-production-run → swap in 60 seconds, keep printing, clean the dead one later. |

**Phase 1 subtotal: ~$135**

---

## 3. Phase 2 — Production Readiness

Goal: production-grade material, real fastener hardware, faster iteration. Order once Phase 1 prints are dialed (week 1–2).

| Item | Spec / example | Est. | Why |
|---|---|---:|---|
| ASA, 2× 1kg | Polymaker PolyLite ASA in production colorway (black; OD/army green exists if you want it on-palette) | $46 | The production-grade enclosure material: ~95°C heat resistance, UV stable, satin-matte finish that reads premium. The enclosed chamber makes it viable. |
| Standalone filament dryer | Sunlu FilaDryer S2 (single spool, hits 70°C) | $45 | Covers what the ACE can't: ASA wants ~70–80°C drying. Dry the spool you're about to run; the ACE babysits PLA/PETG. Upgrade path: S4 quad if throughput demands it. |
| Heat-set insert kit, M3 | Ruthex or CNC Kitchen style, ~100+ brass inserts | $18 | The professional answer for enclosures that open — and hot-swap 18650 access means yours open constantly. Threads directly into plastic bosses. |
| Insert-press soldering tips | M3 heat-set tip set for a standard iron | $12 | Clean, straight insert installs. (Assumes you own an iron — if not, a basic 60W adjustable is ~$20 more.) |
| M3 hardware assortment | Socket-head + button-head screws, nuts, washers, 6–20mm lengths | $18 | Matches the inserts. Button-head for visible exterior faces. |
| 0.6mm hotend unit | Anycubic quick-release, official | $20 | Draft iterations print ~40% faster with negligible quality cost at prototype stage. Keep 0.4 for final surfaces. |
| Super Lube 21030 | Synthetic grease w/ PTFE, 3oz | $10 | Rail and lead-screw maintenance, every ~1–2 months of heavy use. |
| PTFE tube (2m) + cutter + PC4-M6 quick couplings (4pk) | Capricorn-style tube fine | $15 | The ACE's four feed paths are wear items. The quick couplings on the ACE ports are a known community fix that makes filament removal painless. |

**Phase 2 subtotal: ~$185 · Running total: ~$320**

---

## 4. Phase 3 — Premium Finish & Expansion

Optional. Buy only when a specific need shows up.

| Item | Spec / example | Est. | Why / trigger |
|---|---|---:|---|
| Hardened-steel 0.4 hotend | Anycubic all-metal hardened quick-release | $28 | **Required before** touching any CF filament. |
| PETG-CF, 1kg | Polymaker or eSun | $28 | The premium-feel play: stiff, dead-matte, dimensionally stable — boutique enclosure energy. Direct feed only, hardened hotend only. |
| TPU 95A, 1kg | Overture or Polymaker | $22 | Gaskets, bumpers, battery-retention pads. Direct feed only. |
| Second build plate | Opposite finish to whatever shipped in your box (smooth vs. textured PEI) | $28 | Two surface finishes for product faces + hot-swap between prints for throughput. |
| Smart plug + smoke detector near printer | Any Kasa-style plug | $25 | Remote kill switch + basic fire sense for unattended production runs. |
| Activated carbon + printable BentoBox-style filter | Carbon pellets, ~$10; box prints free | $10 | Scrubs ASA styrene smell inside the chamber. Either way: ventilate the room during ASA runs. |

**Phase 3 subtotal: ~$140 · Full-stack total: ~$460**

---

## 5. Filament Strategy for Enclosures

| Material | Role in pipeline | Feed path | Drying |
|---|---|---|---|
| PLA | Shape iteration only — never ships | ACE Pro | ACE @ 50°C when needed |
| PETG | v1 ship candidate; fit + drop testing | ACE Pro | ACE @ 55°C, 6–8h before runs |
| ASA | Production grade — heat, UV, satin finish | ACE Pro (dry separately) | **S2 @ 70°C, 4–8h** — always, in Florida |
| PETG-CF | Premium tier finish | **Direct only** | S2 @ 70°C |
| TPU 95A | Gaskets, soft parts | **Direct only** | ACE or S2 @ 55°C |

Notes for the tracker line specifically: PETG handles 18650 skin temperatures fine; ASA gives extra margin near charging circuitry. Print shell exteriors face-down on the textured plate for a uniform premium bottom surface, keep inserts and bosses on the interior, and version every dialed profile in the slicer (e.g. `BVX-ASA-PROD-04`) so production settings are reproducible and never re-guessed.

---

## 6. Budget Summary

| Phase | Contents | Cost | Running |
|---|---|---:|---:|
| 1 — Calibration & prototyping | Filament base, storage, spare hotend | ~$135 | $135 |
| 2 — Production readiness | ASA, dryer, inserts, hardware, 0.6 | ~$185 | $320 |
| 3 — Premium & expansion | CF stack, TPU, plate, safety, filter | ~$140 | $460 |

Phases 1+2 land at ~$320 — the productive core, comfortably inside band. Phase 3 stretches to ~$460 only if every trigger fires.

---

## 7. First 72 Hours — Commissioning Order

1. **Firmware update first.** Touchscreen or Anycubic app, before any print.
2. **Full auto-calibration suite** — PID tune → resonance/feedback compensation → auto-level, in that order.
3. **Stock test print** (Benchy or the included model) in PLA. Confirms baseline health, nothing more.
4. **Dimensional truth test:** print a 25mm calibration cube plus a hole/peg tolerance test in PLA. Measure with calipers. Set flow and shrinkage compensation in the slicer profile. *This step is the whole difference between hobby printing and product printing.*
5. **Load PETG into the ACE, dry 6–8h @ 55°C** before its first print. New spools are not dry, even sealed ones.
6. **First enclosure draft in PETG, 0.4mm.** Measure critical dimensions, adjust CAD, reprint. Expect 3–5 iterations — that's the process working, not failing.
7. **Practice heat-set inserts on a scrap boss** before installing into a real part (Phase 2 gear).
8. **ASA only after PETG is dialed:** dry @ 70°C, glue-stick the plate, doors closed, room ventilated, and stay near the first run.
9. **Save named per-material slicer profiles** the moment each one is dialed. Never re-derive settings.

---

## 8. Do-Not-Buy List

Generic nozzle variety packs (MK8/V6 — physically incompatible with the quick-release hotend). Enclosure tents or kits (it's already enclosed). Boutique adhesion potions — a $4 glue stick covers this machine. Filament sampler multipacks (random small spools fight the ACE and produce nothing shippable). Matte PLA (ACE Pro false-tangle issue). A drying cabinet (ACE + S2 + vacuum bags already cover storage and drying at a third of the price).
