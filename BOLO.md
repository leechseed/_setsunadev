---
title: BOLO — the watchlist
type: tasking board
status: living document — capture-fast, sit rep Block IV
updated: 2026-08-25
protocol: SOP.md §1 — a spoken tasking is written here in the same turn it is spoken
---

# BOLO — THE WATCHLIST

**Be On the Lookout.** What needs doing in the immediate-to-near future, captured the moment it is said. Not projects, not rulings — taskings.

> **Name RULED 2026-08-21.** Chosen for the bolas — the gaucho throwing weapon: thrown the moment the target is sighted, wraps it, holds it until you get there. That is the list. Retired bench: FRAGO · WARNO · Fire Watch.

## Active BOLOs

| # | Order | Issued | Status |
|---|---|---|---|
| 1 | **Grab the 7 remaining MCDP PDFs** from marines.mil (Publications → Doctrinal: 1-1 Strategy · 2 Intelligence · 3 Expeditionary Ops · 4 Logistics · 6 C2 · 7 Learning · 8 Information) → drop in `Desktop\_BVX_INBOX\mcdp\` | 2026-08-21 | 🔴 open — Papi grabs in browser (scripts blocked) |
| 2 | ~~**Run the z-lib favorites export** → drop in `Desktop\_BVX_INBOX\zlib\` → walker produces the gap-list~~ | 2026-08-19 | ✅ **done 2026-08-22** — export landed (4,573 books), parser built (`_tools/zlib_gap_parser.py`), report: [`ZLIB-GAP-REPORT.md`](_0.1_BVX_LEARN/_meta/ZLIB-GAP-REPORT.md) — 672 catalogued · **3,768 in THE GAP** · 133 maybes await ruling |
| 3 | **BBRT profile fill-ins** (QoS bracket + [Blunt Plug]/[taper] confirms) | 2026-08-19 | 🟡 open |
| 4 | **Focus doctrine** [OPERATOR] — build the learnable deliverable: what focus/flow is (the science), how to snap into it on command, how to train and maximize it. Fields called: attention science · sport/competitive/gaming psych · flow research · military attention training. Repo holdings flagged: BVX.0308 *Deep Work* · BVX.0219 *Mental Game of Writing* · "The Zone" entries in MSX.11/12/14 · PSY.07. Goalie/social-dynamics layer = its own section. **Form ruled 2026-08-21:** in-chat walkthrough first (readback-led, answer-first), doc produced same pass for Claude-retrieval. | 2026-08-21 | 🟡 staged — fires on Papi's go once the proword ruling lands |
| 5 | **Optimize the Papi↔Claude interface** [BLACK, feeds both trunks] — stand up the doctrine: conversation is Papi's primary interface; **docs are for Claude's retrieval, not for Papi's reading**; external-facing documents (blog etc.) are downstream transfers, not the point. Build toward trusted recall + one-pass doc-while-replying. **Prioritize speed.** | 2026-08-21 | 🔴 open |
| 6 | **Transmission pedagogy** [BLACK, feeds 4 & 5] — distill the learning-science method for how Claude teaches in-chat at max understanding, tuned to Papi's preference (instructional design · cognitive load theory · multimedia learning · tutoring-dialogue research). Becomes the standard walkthrough format. **House format v0.1 coded same day (SOP §7)** — full distill still open. | 2026-08-21 | 🟡 open — v0.1 live |
| 7 | ~~**Dramatica engine-verify pass** [BLACK] — enter the ruled storyform, confirm it resolves to ONE storyform, transcribe the ENGINE/VERIFY cells back~~ | 2026-08-24 | ✅ **done 2026-08-24** — ONE storyform, transcribed ([oxo-storyform.md](_CANON_NODES/oxo-storyform.md) §9); mc_concern → **The Past**; **flag struck same session: the rotated engine form RULED canon**, superseding the morning domain assignments |
| 8 | **GitHub Support purge ticket** [BLACK/ORANGE, strip follow-on] — file from the account owner: ask GitHub to run garbage collection on `leechseed/_setsunadev` and purge cached views/unreachable objects from the pre-strip history (support.github.com → sensitive-data removal). Old SHAs already fail to resolve via the API; the ticket makes it guaranteed instead of eventual | 2026-08-24 | 🟡 open — Papi files (owner-only action) |
| 9 | **Google outdated-content removal** [BLACK/ORANGE, strip follow-on] — run removed/changed repo URLs through search.google.com/search-console/remove-outdated-content so cached snippets of the pre-strip pages drop out of search | 2026-08-24 | 🟡 open |
| 10 | **Bongobabe v0 build** [ORANGE] — the clicker: one girl · click + idle · toy-size ladder + one act track + cosmetics · paper-doll chibi · single HTML file (Erotic Range pattern). First swing = the art-style test (base doll + three layers, prove the rig). Registry: `Desktop\BONGOBABE\BONGOBABE.md` — **project home is outside this repo, keep it that way** | 2026-08-25 | 🟡 staged — fires on Papi's go |
| 11 | **The GBD Plan** [ORANGE/OPERATOR] — consolidate every body/training system into ONE schedule: glute build (GDP-1 P1–P3 + Contreras progression) · capacity/wear program (8/19 in-chat design) · gape · oral (new module) · stamina · flexibility, on the Primed Protocol chassis. Name ruled: **Golden Brown Delicious**. Gather-first order — plan doc writes ONLY after Papi answers the open questions (asked 2026-08-25) | 2026-08-25 | 🟡 **parked (Oscar Mike 8/25)** — draft saved: `Desktop\ULTRASIN-gbd-plan-DRAFT.md`; resumes on review + "log it" |
| 12 | **The shoot set** [ORANGE] — design the content-production set: **bratty/WAP-core** (ruled 8/25) × gooner function, office room, paint + mounts cleared, camera purchase precedes build. Full design (layout · light plot · camera map · kit · build order) delivered in-chat 8/25. **Gate before registry logging: the §B locked-aesthetic ruling (scope to second lane vs supersede)** | 2026-08-25 | 🟡 **parked (Oscar Mike 8/25)** — draft saved: `Desktop\ULTRASIN-shoot-set-DRAFT.md`; resumes on the §B ruling + review |
| 13 | **Corpus intake — favorites pull** [ORANGE, feeds the taxonomy engine] — IG saved-posts pull into the corpus folder (account + URL + paths in the `_PRIVATE/` design doc). gallery-dl 1.32.9 · Firefox cookies (verified live) · `archive.db` incremental · `--sleep 2-6` · videos off · metadata sidecars on. Full pull chosen over the 3/21 date filter: saved lists carry post-date not save-date — pipeline dedupe absorbs the overlap | 2026-08-25 | 🟢 **DETACHED 8/26** — now runs under Windows Task Scheduler (`BVX_corpus_pull` → `_pull.cmd` in the corpus folder), survives session close; `archive.db` resumes incrementally; log: `_pull.log`. Cleanup when done: `schtasks /Delete /TN BVX_corpus_pull /F` + delete `_pull.cmd` |
| 14 | **The taxonomy engine — build** [ORANGE, feeds BLACK at girl-gen] — Stage 1 hygiene + lattice derivation + tagging passes per the boresighted design. **19 rulings locked 8/25**, full design: `_PRIVATE/ULTRASIN-taxonomy-engine-DRAFT.md` (gitignored). Project name unruled | 2026-08-25 | 🟡 staged — fires on Papi's clear-to-build (boresight chain open) |

| 15 | **BVX multimedia ingestion system** [BLACK] — spoken want: a multimedia ingestion system for the BVX reference system (media beyond books). Deferred mid-sentence by Papi — the story-tree boresight fires first. Specs unstated; captured as seed. **8/25 addendum — TV Tropes scope RULED: no site mining, no full-article ingestion; Papi hand-picks articles, each distilled to a summary in house/BVX vocabulary** (the BVX.0064 distill model applied to trope articles) → feeds the lattice trope register | 2026-08-25 | 🔵 seed — resumes on Papi's call |
| 16 | **Music-video + short-form grammar research pass** [BLACK/ORANGE, feeds the mediums module] — RULED 8/25: the medium-grammar gaps get filled by research, not acquisition. Scope: music videos · TikTok/short-form · PMV/HMV/porn grammar (ORANGE side rides the firewall) | 2026-08-25 | 🟡 open — mediums module delivered 8/26 with M6/M7/M8 as v1 scaffolds; this pass deepens them to sourced grammar (Vernallis = anchor candidate) |

Completed BOLOs get a dated strike-through, then move to the bottom under **Done** on the next pass.

## PMCS — Preventive Maintenance Checks & Services

**The operator is equipment.** Body, medical, and life-admin readiness — the military category is Individual Medical Readiness (IMR). Standing table; items land here the moment they are spoken.

| Item | Status | Next action |
|---|---|---|
| **Dental** — retainer advising | 🔴 open since 8/19 | Call the orthodontist. ⚠️ Dictation has twice produced "periodontist" — confirm which specialist; if there is also a gum concern, that is a **second** appointment |
| **PCP — establish care + physical** | 🔴 open | Book the physical. Sexual-health consult sequences after it: PrEP · DoxyPEP · site-specific panel · anal Pap · pelvic-floor PT referral. Timing decoupled from October — book now |
| **Pelvic-floor PT** | ⬜ gated | Referral comes out of the PCP consult above |

## Done

*(empty — completed BOLOs archive here with dates)*
