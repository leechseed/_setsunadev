---
title: PROJECTS — the board
type: dashboard
status: living document
updated: 2026-08-16
source: claude.ai export 2026-08-15 (319 conversations, Feb 9 → Aug 14 2026)
regenerate: python _tools/cluster_projects.py
---

# THE BOARD

Every project, ranked by how much development actually went into it. Volume = characters of conversation, which is a proxy for thought spent, not value.

> Regenerate after any new export: `python _tools/cluster_projects.py`

## The ten

| # | Project | Trunk | Volume | Convs | Span | State |
|---|---|---|---|---|---|---|
| 1 | **OVEREXITOUT / The Outliers** — narrative IP | BLACK | ~880k | 19 | Feb→Aug | 🟢 live |
| 2 | **BVIPDS / LEECHSEED** — system architecture, SSOT | BLACK | ~580k | 25 | Feb→Jul | 🟢 live |
| 3 | **Adult content venture** — brand, model, monetisation | ORANGE | ~504k | 16 | Feb→Aug | 🟢 live |
| 4 | **Desire Profile** — sexuality research & profiling | ORANGE | ~492k | 19 | Feb→Aug | 🟢 live |
| 5 | **Character system** — Dramatica × astrology × 12-layer | BLACK | ~489k | 8 | Feb→**Apr** | 🔴 **stalled** |
| 6 | **Social channels** — TikTok / YouTube growth | BOTH | ~432k | 25 | Feb→Aug | 🟢 live |
| 7 | **Food ventures** — bakery, takeout, eating show | BLACK | ~411k | 17 | Mar→Jul | 🟡 cooling |
| 8 | **ULTRASIN / GDP** — physique, gym build, training | ORANGE | ~400k | 11 | Feb→Aug | 🟢 live |
| 9 | **Tooling** — scripts, scrapers, UI builds | BLACK | ~266k | 16 | Feb→Jul | ⚪ support |
| 10 | **Business ops** — PM, charters, market entry | BLACK | ~203k | 6 | Feb→Jul | ⚪ dormant |

**BLACK ~2,830k · ORANGE ~1,400k · shared ~430k.** Black runs at roughly twice the volume of orange.

Not projects but large: **~712k personal** (self-regulation, interpersonal, admin) and **~375k gear/logistics**. Together ~17% of everything.

---

## The same ten, ranked by leverage

Volume measures thought already spent. Leverage measures what moves if you touch it. **The two orders disagree, and the disagreement is the finding.**

| Leverage | Project | Vol rank | Cost to unblock | What it releases |
|---|---|---|---|---|
| 1 | **Character system** | 5 🔴 | One afternoon in Dramatica | OXO, Tori, every downstream character. The whole BLACK trunk. |
| 2 | **Adult content venture** | 3 | One ruling — BVX↔Ultrasin firewall | Public launch. The entire money track. |
| 3 | **OVEREXITOUT** | 1 | Nothing of its own | Waits on #1. Cannot be worked around. |
| 4 | **BVIPDS / LEECHSEED** | 2 | Unblocked — absorbs work anytime | Supply line to #1. Never blocks others. |
| 5 | **ULTRASIN / GDP** | 8 | P1, 60-second squeeze hold | Self-contained. Physical, immediate. |
| 6 | **Desire Profile** | 4 | Tool 1 Step 1 checkoff | Feeds L9 EROS. No dependents. |
| 7 | **Social channels** | 6 | — | 25 conversations, zero artifacts. Nothing downstream. |
| 8 | **Food ventures** | 7 | — | Cooling. |
| 9 | **Tooling** | 9 | — | Support only. |
| 10 | **Business ops** | 10 | — | Dormant. |

**What the two orders reveal:**

1. **The most-developed project is the most blocked one.** OXO carries ~880k — the largest volume on the board — and cannot advance a step until the character system moves. The thing you have thought about hardest is downstream of the thing you abandoned in April.
2. **Both top blockers are single decisions, not projects.** An afternoon with the Dramatica software and one firewall ruling. Neither needs new building. Together they release ranks 1–4, roughly 2.4M of accumulated work.
3. **Volume is not progress.** Ranks 6 and 7 hold ~843k combined and have produced zero artifacts between them.

---

## What each one is, and what it's waiting on

### 1 · OVEREXITOUT / The Outliers — 🟢
The IP. Anchors: `THE OUTSIDERS SYSTEM` (304k), `MAIN SONNET` (192k). Six movements, tri-state Delta Coast Spiral, death-as-boot-sequence. Tori node built, L9 authored, IC candidate derived.
**Waiting on:** the Dramatica storyform (~65 fields) · IC ruling. ~~The school fusion name~~ **RULED 2026-08-24: the Delta Coast Ultra School (DCUS).**
→ `_CANON_NODES/` · `_OXO_SCHOOL_HANDOFF/`

### 2 · BVIPDS / LEECHSEED — 🟢
The machine that builds the IP. SSOT domains 00–05, Narrative Layer Stack 0–6, profiler UI, research catalog. BVX-LEARN now unblocked and running at 99% classification over 1,106 sources.
**Waiting on:** nothing structural. This one moved most today.
→ `_0.1_BVX_LEARN/_meta/` · `ShroomsQ/_CANON/`

### 3 · Adult content venture — 🟢
Ultrasin. Registry v0.1 covers systems A–M. Fiscal anchor May 4. Exit gate: 2× current income, $1,200/wk.
**Waiting on:** BVX↔Ultrasin firewall (blocks launch) · performer handle · commentary register.
→ Ultrasin master registry

### 4 · Desire Profile — 🟢
The research spine. *Mating in Captivity* review (187k), D/s dynamics guide (96k), profiling questionnaires. **Six artifacts — the most of any project.** Erotic Range shipped from it.
→ `_CLAUDE_ARCHIVE_2026-08-15/projects/desire-profile/`

### 5 · Character system — 🔴 **STALLED SINCE APRIL**
Dramatica → Character Astrology → 12-Layer. Validated 11/11 layers, zero contradictions. 259k in one conversation.
**This is the one that matters.** It went quiet in April and everything else depends on it. The block is a single afternoon with the Dramatica software.
→ `ShroomsQ/_CANON/_SSOT/02_CHARACTER_SYSTEMS/`

### 6 · Social channels — 🟢
YouTube income modelling, faceless listicle channel, TikTok mechanics. 25 conversations, **zero artifacts** — all exploration, nothing built.

### 7 · Food ventures — 🟡
Bakery, American-Chinese takeout, eating-content show. Real modelling. Cooled after July.

### 8 · ULTRASIN / GDP — 🟢
GDP-1 BOOTYCAMP four phases, Gate Keeper's Kata, FAC-1 NIGHTYARD build spec, tracker app. Primed Protocol documented 2026-08-15.
**Next physical action:** P1, gate out at a 60-second squeeze hold.
→ `Desktop/ULTRASIN-primed-protocol.md`

### 9 · Tooling — ⚪
yt-dlp, clipboard monitors, JSX, debugging. Serves other projects, no independent goal.

### 10 · Business ops — ⚪
PMBOK, charters, market entry. Dormant since spring.

---

## Not on the board yet

Real work with no volume, because it's new or buried:

| | State |
|---|---|
| **Leechseed Manifesto** — 10 doctrine docs, May 2025 | 🔴 found, not in canon |
| **L2b MORPHOLOGY** — frame/tissue/condition/line/archetype | 🟢 **gluteal module specced 2026-08-21** — 27-cell substrate, 13 named types, two sexed taxonomies. Next module: population signatures. |
| **Taxonomic-aesthetic practice** — the archive as revealed-preference data | engine-vs-voice fork unanswered since June |
| **SlimeVR tracker line** — Kobra S1 BOM, enclosures | product venture, scattered across Tooling |

---

## How volume was computed

Every archived conversation scored against project keyword sets — title matches weighted 12×, body 1× — best match wins, minimum threshold 3. Not perfect; two large conversations were hand-corrected after inspection (`Fixing awkward sentence construction` → OXO, `Grab data analysis` → Character system). Treat ranks as directional, not exact.

Numbers are frozen at the 2026-08-15 export. They drift the moment you have new conversations — rerun the script after the next export.
