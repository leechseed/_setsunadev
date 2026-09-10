---
title: DARKROOM tagging — the tag layer, TAGGING + CAPTCHA, Tier 2 probes (BOLO 44)
type: parked work
status: parked (Oscar Mike 2026-09-10) — sweep done, Tier 2 shipped; resumes on "run the darkroom" + the 300-image calibration pass
updated: 2026-09-10
trunk: ORANGE (taxonomy engine, Stage 3)
open_on_resume: DARKROOM server is DOWN (died with the 9/10 session) · the 300 random-image carousel pass (the unbiased calibration set) · "retrain" after each session · the Retrain button + solo-only queue toggle ride the next server restart · Tier 3 = L2b cells, module 2 as the prior
---

# DARKROOM TAGGING — parked 2026-09-10

**What it is.** The taxonomy engine moved from Stage 1 to Stage 3 on 9/9–9/10: a tag layer on DARKROOM (1.1) with six vocabulary axes, two annotation modules built to Papi's spec (TAGGING = one image + Space commits, Prodigy pattern · CAPTCHA = one value, a grid of twenty, click the matches, unclicked = negatives), undo/redo, resizable rails, and Tier 2 probes trained on the sweep.

**Where the substance lives.** [BOLO 44](../BOLO.md) carries the full record. Code: `_PRIVATE/taxonomy_engine/` — `vocab.json` (the axes, Papi-revised through the night) · `zeroshot_pass.py` (Tier 1, saves the text prototypes) · `probe_pass.py` (Tier 2 bake-off: zero-shot / rocchio / one-vs-rest LR, 5-fold CV, best per axis) · `darkroom_server.py` (`/api/tags`). Page: `DARKROOM.html` in the corpus root (backup `.bak-1.0`). Data: `_pipeline/tags.json` (Papi's rulings + `~axis` negatives) · `tags_auto.json` + `darkroom_tags.js` (proposals).

**State at park.** CAPTCHA sweep closed by Papi 9/10: every value on every axis ≥ 40 confirmed, 16,496 judged images. Tier 2 shipped: one-vs-rest LR won all six axes on the combined metric (register 82 · setting 78 · dress 75 · styling 74 · framing 69 · mood 66; zero-shot 52–62). Proposals in DARKROOM now come from the probes.

**Resume order.**
1. "run the darkroom" (server down since the session ended).
2. Library CAST → Solo, press T, 300 in catalog order = the honest calibration set (the sweep's numbers carry sampling bias).
3. Say "retrain" → `probe_pass.py` (10 s). Repeat after every session.
4. Next server restart: the Retrain button in the Tags panel + a solo-only toggle on the tagging queue.
5. Tier 3: L2b cells (Papi's eyes) with the population-signatures module as the prior; then Stage 4 clustering off the same embeddings.

**Lessons banked.** A load-order bug killed the page once (dirty set declared after a prune step); the status bar now traps errors in red, and a jsdom boot test lives in the scratchpad pattern (headless Edge does not run in the sandbox). A hand-rolled probe shipped worse proposals for ten minutes before the bake-off replaced it: never ship a model without the CV table.
