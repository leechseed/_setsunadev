---
type: ssot_01_narrative_frameworks
category: narratology_shelf
version: 1.0.0
last_updated: 2026-09-03
status: PROMOTED 2026-09-03 from the archived 1.04 MARIMARI EN build (the terminal build of the 2024 narratology lineage) — ruling: the ancients pass, sit rep 2026-09-03
purpose: "The house narratology reference shelf: 109 framework distills (one per theorist-model, UID-keyed) filed by tier and competency, plus the competency catalog, the General Model propositions, and the pre-alpha Rulebook. Feeds BOLO 18 stage 2 (spine `feeds:` sweep) and the craft-shelf distill count."
dependencies: ["ssot_01_story_spine_comparative_tree", "ssot_01_spine_house_inventory"]
trunk: BLACK
provenance:
  origin: "_ARCHIVE/_1.04 RC1_MARIMARI_EN_BUILD/ (bin/ · 2_guiding documents/)"
  authored: "Aug 2024 – Jan 2025, builds BELLE → 1.04; distills are AI-assisted, template-driven (1_PRE-ALPHA-AI_TEMPLATE)"
  coverage_check: "2026-09-03 hash + UID pass: 1.04 carries every UID present in BELLE / EMIWU / 1.02 plus 16 more — earlier builds superseded, archive-only"
---

# 📐 SSOT: THE NARRATOLOGY SHELF

**What this is.** The 2024 narratology curriculum, recovered from the build lineage and given a live home. Every file in `frameworks/` is one theorist-model distill (Booth's implied author, Genette's focalization, Greimas's actantial model, Propp's 31 functions, Bakhtin's heteroglossia, Ryan's immersion, Sternberg's exposition, McKee's character-and-conflict …), UID-keyed, with mermaid mindmaps and a fixed Definition / Characteristics / Contextualization skeleton.

**Why it matters.** BOLO 18 stage 1 scored the craft shelf **0.6% distilled (2 of 353)**. That count missed this shelf because it sat under an `X_` build prefix. The house already holds **109 finished framework distills** and a tiered index.

**How GUTS99 relates.** In 2024 "GUTS99" was the working title of this documentation project (see `_ARCHIVE/_1.04 …/.CONTENT/guts99_documentation/`). In 2025 the name was reused for the media-DNA influence system (`_ARCHIVE/_grognard/`), retired 2026-09-03 with its twelve subsystem coinages carried into BOLO 15.

## Layout

| Path | Holds | Count |
|---|---|---|
| `frameworks/Tier 1–4/<CODE> <Competency>/` | the distills, one per framework; `WICKED/` sub-folders hold the craft-book (non-academic) sources | 109 (15 wicked) |
| `UID_index.md` | UID → framework → tier → competency code, the master key | 1 table |
| `competencies/` | the 28 competency one-sheets (NS-3301 … MN-3706) + TOC + two expanded drafts | 31 |
| `propositions/` | P1–P8: the General Model of Narratology thesis · Ascertaining Truth · additional-references ledger | 12 |
| `narratology_core_rulebook_pre-alpha_draft.md` | the Rulebook: 20 core competencies + concerns and challenges of the field | 1 |

## The tier map

| Tier | Code | Competency | Distills | of which wicked |
|---|---|---|---|---|
| Tier 1 | `CH-3302` | Characterization | 5 | 1 |
| Tier 1 | `NS-3301` | Narrative Structure | 9 | 5 |
| Tier 1 | `PA-3303` | Plot and Event Analysis | 5 | 3 |
| Tier 2 | `CL-3406` | Narrative Coherence and Logic | 2 | 0 |
| Tier 2 | `FO-3403` | Focalization | 3 | 0 |
| Tier 2 | `NA-3402` | Narration and Narrator Analysis | 7 | 0 |
| Tier 2 | `NV-3405` | Narrative Voice and Point of View | 4 | 0 |
| Tier 2 | `SD-3401` | Story vs. Discourse (Fabula vs. Sjuzhet) | 3 | 0 |
| Tier 2 | `TMV-3407` | Tense, Mood, and Voice in Narrative Grammar | 1 | 0 |
| Tier 2 | `TT-3404` | Time and Temporality | 7 | 0 |
| Tier 3 | `DM-3503` | Diegesis and Mimesis | 8 | 0 |
| Tier 3 | `FM-3506` | Function and Motif Analysis | 8 | 0 |
| Tier 3 | `GT-3505` | Genre and Narrative Typology | 5 | 1 |
| Tier 3 | `INT-3502` | Intertextuality | 3 | 0 |
| Tier 3 | `MT-3508` | Metalepsis and Narrative Transgression | 1 | 0 |
| Tier 3 | `NE-3509` | Narrative Ethics and Ideology | 1 | 0 |
| Tier 3 | `NLE-3501` | Narrative Levels and Embedding | 3 | 0 |
| Tier 3 | `NR-3507` | Narratee and Implied Reader | 5 | 1 |
| Tier 3 | `SN-3504` | Semiotics of Narrative | 11 | 0 |
| Tier 4 | `AS-3601` | Advanced Semiotics and Symbolic Interpretation | 3 | 1 |
| Tier 4 | `TN-3602` | Transmedia Narratology | 1 | 0 |
| Tier 5 | `CA-3705` | Creative Application | 1 | 0 |
| Tier 5 | `CC-3704` | Cultural and Contextual Analysis | 1 | 0 |
| Tier 5 | `CMS-3703` | Cross-Media Narrative Study | 2 | 0 |
| Tier 5 | `HN-3701` | Holistic Narrative Analysis | 6 | 2 |
| Tier 5 | `MN-3706` | Meta-Narrative Awareness | 1 | 0 |
| Tier 5 | `TI-3702` | Theoretical Integration | 1 | 0 |
| Tier 5 | `TN-3602` | Transmedia Narratology | 2 | 1 |

Codes run **NS-3301 … TN-3602**; the 3300s are foundations, 3400s discourse mechanics, 3500s structure and meaning, 3600s advanced. Competencies 3701–3706 (holistic analysis, theoretical integration, cross-media, cultural, creative application, meta-narrative awareness) have one-sheets in `competencies/` but no distills yet.

## Spine hook (BOLO 18 stage 2)

Each distill takes a `feeds: SPINE.Lx` key on the sweep. Provisional mapping by competency: **NS/PA/SD/TT → L1–L3** (structure, event, time) · **CH → L5 + the 12-layer character stack** · **NA/FO/NV/NR/NLE/MT → L4 (texture / telling)** · **INT/GT/SN/FM/DM → L6–L7 (intertext, genre, motif)** · **NE/AS/TN → L0 root theory**. Confirm against the comparative tree before keying.

## Not promoted (stays in the archive)

`RETIRED QUERIES/` (the 2024 query scripts) · `.CONTENT/guts99_documentation/` (doc-site scaffolds) · the Mermaid format guidelines · the Rulebook PDF (binary, gitignored class) · the BELLE / EMIWU / 1.02 earlier drafts of the same distills.
