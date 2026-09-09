---
title: PM Holdings Inventory — everything project-management-shaped the operation already holds
type: register / survey
domain: 05_OPERATIONS
status: survey banked 2026-09-03 — feeds BOLO 25 (the standard PM flow)
date: 2026-09-03
method: Explore-agent sweep of the repo + archive (medium breadth), paths verified where load-bearing
trunk: BLACK (systems) — serves every trunk
related: BOLO.md #25 · SOP.md · STATE.md · PROJECTS.md · DOCTRINE-0-INVARIANTS.md · BVX-ULTRASIN-twin-track.md · oscar-mike/lab-venture.md
---

# PM HOLDINGS INVENTORY

**The finding in one line: the method is already written; what is missing is assembly.** A complete six-phase lifecycle with decision gates exists in the Feb-2026 four-domains artifact, a matched PMBOK-7 mapping sits beside it, and every instrument a lightweight flow needs (charter · assumption log · decision ledger · task register · portfolio board · stage gates · document container · house style) exists as a finished artifact somewhere in the repo. No single document assembles them into "how a project runs here."

## 1 · PMBOK / PMI material

| Path | What it is | State | Reuse for the standard flow |
|---|---|---|---|
| `_CLAUDE_ARCHIVE_2026-08-15/projects/pmbok-6th-edition/_project.md` | Claude-project shell, no docs | stub | pointer only |
| `_CLAUDE_ARCHIVE_2026-08-15/files/2026-03-19_step1-warmup-study-guidemd.md` | Vargas reading flow step 1 — definitions, 5 process groups, 10 KAs, EEF/OPA, PMO types | finished distill | the vocabulary layer |
| `…/files/2026-03-19_step2-knowledge-areas-study-guidemd.md` | all 10 KAs, process tables, agile considerations per KA | finished distill | pick-list for which KAs a solo flow needs (Scope · Schedule · Risk) |
| `…/files/2026-03-19_step3-process-groups-study-guidemd.md` | process groups + the 49-process flow map, ASCII diagrams | finished distill | **closest ready-made process backbone** |
| `…/files/2026-03-19_step4-processes-detail-study-guidemd.md` | all 49 processes, EVM, risk responses, ITTO reference | finished distill | rigor layer, too heavy for daily use |
| `…/files/2026-03-19_step5-optional-reading-study-guidemd.md` | agile/adaptive continuum, **tailoring**, 132 tools catalog, glossary | finished distill | the tailoring appendix licenses stripping PMBOK to one person |
| `…/files/2026-03-19_bvipds-project-chartermd.md` | real PMBOK 4.1 charter for BVIPDS — 13 sections, 15 requirements, 7 risks, **M-001…M-007 deliverable-gated milestones**, exit criteria | finished distill | **best template in the repo** — gates keyed to artifacts, not dates |
| `…/files/2026-03-19_bvipds-assumption-logmd.md` | 12 assumptions × 6 fields, status OPEN / VALIDATED / INVALIDATED / REVISED, reviewed at every gate | finished distill | drop-in assumption/risk instrument |
| `_1.2.EMIRU/1.2.EMIRU/test documents/BVIPDS_project_charter.md` | in-repo copy of the charter, frontmatter collapsed, anchors rewritten to chat URLs | damaged | use the archive copy |
| `…/conversations/2026-03-19_bold-venture-initiative-project-charter-planning.md` | the session behind the charter; PM-tool landscape ending in a ClickUp mapping (Space → Folders=phases → Lists=milestones → Tasks) | raw, rich | the reasoning behind each charter choice + tool-layer decision (ClickUp tracks, Git canonical) |
| `…/conversations/2026-03-19_pmbok-6th-edition-study-guide-creation.md` | build session for the five guides; format contract (TOCs, mnemonics, ASCII, self-checks) | raw | reusable distill spec |
| `…/conversations/2026-03-28_work-breakdown-structure-in-pmbok.md` | WBS, 100% rule, work packages, WBS dictionary | stub | only WBS material in the corpus |
| `…/artifacts/2026-02-25_pmbok-and-ricardo-vargas-doctrine-grade-research-for-solo-.md` | PMBOK 6→7→8, 12 principles tiered by solo relevance, **"WBS is MECE is problem framing"**, Vargas 5–80% human-AI rule, **PMBOK 7 performance domains → six-phase lifecycle** | finished distill | **the synthesis** — which parts of PMBOK survive a team of one |
| `…/conversations/2026-02-12_3d-printing-business-models-and-market-entry.md` | complaint research → differentiation → limited-batch drop → unit economics → 12-week launch | raw, rich | a worked venture-launch sequence |
| `…/files/2026-07-04_spindle-master-business-plan-v01md.md` | 14-section master plan on a five-layer section architecture; Appendix C frames it as a reusable template | finished template | the venture-side counterpart to the charter |
| `…/files/2026-07-04_ultrasin-master-plan-architecture-v01md.md` | master-plan architecture only: horizons 0–6 / 6–18 / 18–36 mo, question sets | partial | the phase/horizon skeleton |
| `…/files/2026-06-16_fl-food-business-launch-checklistmd.md` | jurisdiction launch checklist | finished | example of the checklist artifact type |

No agile/scrum/kanban thread exists on its own. Agile appears only inside the PMBOK guides and the four-domains artifact's CDPR section (9-week milestones × three 3-week sprints).

## 2 · Marine Corps doctrine as PM method

| Path | What it is | State | Reuse for the standard flow |
|---|---|---|---|
| `OVER_EXIT_OUT_OBSIDIAN/OVEREXITOUT/00_IMPORTED_JOPLIN/MARINE CORPS DOCTRINAL PUBLICATIONS/` | **MCDP knowledgebase summaries (Dec 2025), one per publication**: 1 · 1-1 · 1-2 · 1-3 · 2 · 3 · "4 Security" · 5 · 6 · 7 · "8 Logistics". Abstract → TL;DR → section breakdown → TOC | **UNVERIFIED (9/3 repair pass)** — the 4 and 8 summaries were generated from filenames, not texts; MCDP 7's chapter list does not match the real book either; the whole Dec-2025 set is suspect | **superseded by the MIL.01–MIL.11 one-sheets** (built 9/3 from the full PDFs, `KNOWLEDGE_AREAS/`); audit the remaining 9 summaries before citing any |
| same folder | 4/8 repaired 9/3: both originals retagged `— UNVERIFIED`, real *MCDP 4 — Logistics (2023)* and *MCDP 8 — Information (2022)* summaries generated from source, index lists all 11 | done | — |
| same folder, `1 PROMPT TEMPLATE spec.md` + `2 KNOWLEDGEBASE spec.md` | the summarizer prompt (exact-replication, no invention) + KB spec | finished template | a distill pipeline reusable for PMBOK |
| `BVX-ULTRASIN-twin-track.md` §Doctrinal spine | the "Marine standard": Feb-9 SSOT Writing Guide canon · MCDP hierarchy ↔ doctrine stack · MCDP 7 ↔ BVX-LEARN · MAGTF ↔ full-stack company · acquisition queue (11 pubs, 4 PDFs in hand) | finished | the doctrine-to-operation mapping; its decision table is a ledger pattern |
| `DOCTRINE-0-INVARIANTS.md` | seven rules for what qualifies as a rule (earned by 2+ uses · written-only · names what it forbids · every scale · names derivation · fewer than seven · dies by countermand) | **RATIFIED 2026-09-03** (rename bench still open) | the governance layer; the project flow promotes under it |
| `SOP.md` | **the de-facto PM operating system**: prowords · sit rep blocks · Ready Rack/Magazine handoff · reading order · house format | finished, enforced | already a project-control cadence; governs the *session*, not the *project* |
| `STATE.md` | "Blocked on you" decision table (# · Decision · Unblocks) + dated Moved blocks | living | decision log + change log; "Unblocks" is a dependency field |
| `BOLO.md` | numbered task register, issued date, status flags, in-place addenda | living | task register with audit trail |
| `oscar-mike/` | parking lot: frontmatter contract, park/sweep | finished | backlog / WIP discipline |
| `_CACHE/` · `_LOG/` | Ready Rack → Magazine flush | finished | the session-close step |
| `…/files/2026-02-09_ssot-writing-guide-marine-corps-standardmd.md` | Marine Corps Doctrine Standard v1.0.0 for SSOT docs | finished | house style every process doc is written to |
| `…/conversations/2026-06-08_marine-corps-documentation-and-narrative-production.md` | BVMC coined; MCDP 1 as structural template; MCDP 7 + MAGTF as the applicable frameworks | raw | origin record |
| `…/conversations/2026-07-21_bvx-quartermaster-protocol.md` | the Quartermaster: car-and-cargo rule, **2+ concrete uses promotion gate**, tripwires | raw, rich | source of the DOCTRINE-0 promotion gate; an AAR-capture pattern |

## 3 · Pyramid Principle / answer-first doctrine

| Path | What it is | State | Reuse for the standard flow |
|---|---|---|---|
| `…/artifacts/2026-02-25_four-domains-converge-on-a-bold-venture-development-doctri.md` | **the Feb-2026 four-domains artifact**: USMC mission command · McKinsey MECE / Pyramid / 7-S · AAA pipelines (CDPR sprints, vertical slice) · DoD gates · five shared patterns · **a full-lifecycle doctrine for solo dev + AI: Phase 0 Problem Framing → 1 Concept & Intent → 2 Design & War-Gaming → 3 Vertical Slice → 4 Production → close, decision gate at each boundary** | finished distill, **never promoted** | **this is the standard flow, already written** |
| `…/artifacts/2026-02-25_pmbok-and-ricardo-vargas-…` §mapping | PMBOK 7 performance domains bolted onto the six phases | finished distill | matched pair with the above |
| `SOP.md` §7 | answer-first codified; ten-second test | finished v0.1 | the document standard for every PM artifact |
| `SOP.md` §1 boresight | readback → read → questions, no delivery until cleared | finished | the requirements sign-off gate |
| `STATE.md` Pyramid audit | source text absent from all libraries; `BVX.1107` reserved | earmark | known gap, slot held |
| `…/conversations/2026-03-28_the-pyramid-principle-explained.md` · `2026-04-04_mckinsey-pyramid-model-explained.md` | one-shot recalls | stub | superseded by the artifact |
| `05_OPERATIONS/📐 ssot_05_operations_legacy_styleguide_2024.md` | the 2024 ancestor style + naming guide | historical | naming section only |

## 4 · Templates, registries, gates, process docs

| Path | What it is | State | Reuse for the standard flow |
|---|---|---|---|
| `PROJECTS.md` | the board: ten projects × trunk/volume/state, re-ranked by **leverage** with cost-to-unblock and what-it-releases | living (regen 8/16) | the portfolio-prioritisation mechanic |
| `oscar-mike/lab-venture.md` §3 | **stage-gate sheet**: G1 90 days consistent output → gear · G2 $1–2k/mo ×3 → collab/testing · G3 60–70% of living ×3 → full-time; metrics (rebill >60% · ARPU · conversion 1–5%) | parked, unruled | **cleanest gate pattern**: a measured condition authorises a specific spend |
| `ShroomsQ/_CANON/_SSOT/05_OPERATIONS/` | SSOT_CREATION v1.8.0 · writing guide · **retrieval dossier protocol** · AI instruction protocol · variable registry · setup guide · two `Untitled` orphans | mostly finished | where a PM SSOT belongs; dossier protocol adapts to status reporting |
| `ShroomsQ/_CANON/_TEMPLATES/ssot/♨️_template_ssot_05_operations_standard_structure_template.md` | mandatory 8-component SSOT structure | canonical | **the container** for any new process doc |
| `ShroomsQ/_CANON/_TEMPLATES/authoritative/📋 BVX Learning Template v2.md` | one-sheet generator: invariants / heuristics / core concepts | finished | distill format for PMBOK/MCDP operator cards |
| `_0.1_BVX_LEARN/_meta/SPEC.BVX-LEARN.v3.md` | pipeline spec with **§9 Quality Gates** + §14 open decisions | draft | a spec carrying its own gates + decisions |
| `_0.1_BVX_LEARN/_meta/DECISIONS.md` · `REVIEW-QUEUE.md` · inventory/orphans/gap reports | per-subsystem decision log + review queue + reports | finished | the proven per-project document set |
| `_0.1_BVX_LEARN/KNOWLEDGE_AREAS/*.md` | one-sheets with `Invariants` + structured `feeds:` block | finished | traceability (requirement → artifact) in YAML |
| `…/files/2026-03-28_research-to-knowledgebase-templatemd.md` | two-stage prompt pipeline (research → KB) | finished template | the intake half of a research-driven flow |
| `00_EPISTEMOLOGY/📐 ssot_00_process_illustration_character_pipeline.md` | worked end-to-end pipeline illustration | finished | the "flow, illustrated once" artifact |
| `…/files/2026-02-25_ssot-00-system-architecture-mapmd.md` | components mapped, **every undefined interface marked** | finished | an interface-gap register = risk log |

## 5 · The Ultrasin master registry format
`…/files/2026-08-05_ultrasin-master-registrymd.md` (v0.1, living). Five-flag status vocabulary declared up front (🟢 locked · 🟡 in motion · 🔴 open decision · ⚪ parked · 📄 artifact in old chat) on every row. Shape: Goal Layer (gates) → Systems Registry (§A–§M one-liners pointing at deep docs) → Cross-System Principles → **Open Decisions Ledger (`# | Decision | Blocking?`)** → Chat Census (distill priority H/M/L) → Known Gaps → Maintenance. Governance: the canon rule (not written = does not exist) and rescission by dated strikethrough.

## 6 · Finished vs missing

- **Finished:** the six-phase lifecycle + gates (four-domains artifact) · the PMBOK-7 mapping · charter instance · assumption log · decision ledger (STATE + registry) · task register (BOLO) · portfolio board (PROJECTS) · backlog discipline (oscar-mike) · session handoff (Ready Rack) · stage gates (lab venture) · document container (SSOT template) · house style (Marine standard + SOP §7) · **11 MCDP summaries** (numbering drift on 4/8).
- **Missing:** one document that says how a project runs here · blank charter/gate/close-out templates (the charter is an instance) · a project lifecycle in the repo proper (SOP governs sessions) · a sprint/cadence layer beyond the CDPR paragraph · DOCTRINE-0 ratification (the promotion mechanic).
- **Known gaps already flagged:** Pyramid Principle source text (BVX.1107 reserved) · 7 of 11 MCDP PDFs (BOLO 1) — **summaries exist for all 11; the PDFs feed the catalog, not the method** · DOCTRINE-0 unratified.

## 7 · Cheapest path to a standard flow — TAKEN 2026-09-03 → `📐 ssot_05_operations_project_flow.md` v0.1
Promote the four-domains six-phase lifecycle into a `05_OPERATIONS` SSOT · strip the BVIPDS charter + assumption log into blanks · generalise the G1/G2/G3 gate pattern · adopt the registry's five-flag status + `# | Decision | Blocking?` ledger as the schema. Every input is a finished artifact today.

## 8 · Addendum 2026-09-09 — the Business-ops cluster, closed out (true-ancients R8)

PROJECTS rank 10 "Business ops" retired as a label. Of its six conversations, four are already in §1 (PMBOK study guides · the BVI charter · WBS · the 3D-printing market entry) and one by output (the SPINDLE master plan). **Not previously cited, pointed here so it is never re-derived:** `_CLAUDE_ARCHIVE_2026-08-15/conversations/2026-06-06_buying-and-reselling-unpublished-content-rights.md` (BOTH, 37k, 1 artifact) — the adult-industry entry consult: creator-led economics, LTV:CAC, §2257, Visa VAMP, three capital tiers, flagship→network, the third-party repository assessed as funnel-only. BOLO 27 / ULTRA DARK (9/3) reached the same funnel-only conclusion from §N + registry §E without this file; the next Ultrasin entry question starts here.
