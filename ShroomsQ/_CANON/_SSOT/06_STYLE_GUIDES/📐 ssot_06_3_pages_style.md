---
type: ssot_06_style_guides
category: style_guide
version: 0.1.0
last_updated: 2026-09-29
applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD, BVX-LEARN]
status: "draft — BOLO 92, RULED 2026-09-29"
purpose: "How artifacts and pages look: the foundation design system, then the page rulings (colorway, chrome, the hover layer, diagram rendering, the dashboard pattern, learning-tool density) gathered from memory for the first time; held-not-distilled sources from the Zotero shelf."
dependencies: ["[[📐 ssot_00_bold_venture_design_system]]"]
trunk: BLACK
sources: ["memory: default-colorway", "memory: thin-chrome", "memory: ck3-hover-layer-required", "memory: mermaid-static-dom-only", "memory: sitrep-front-page", "memory: learning-tools-minimal", "_tools/bolostatus/work/92/SHELF.md §06.3 Pages"]
---

# 📐 ssot_06_3_pages_style — how the Command's pages look

## TABLE OF CONTENTS

- [Purpose](#purpose)
- [The foundation](#the-foundation)
- [The page rulings](#the-page-rulings)
- [SOURCES — held, not yet distilled](#sources--held-not-yet-distilled)
- [OPEN](#open)
- [Version History](#version-history)

## PURPOSE

Every artifact and tool page the Command publishes answers to two layers. The **foundation** is the Bold Venture Design System — the brand's rose/NOIR palette, the FLESH ramp, the Luminance Law — for DARKROOM and anything public-facing. The **page rulings** below are the internal-tool layer: the working palette, the chrome, the interaction pattern for every SITREP, DOPE SHEET, SOI, and TM. The two do not compete — a page is either brand-facing (foundation) or a working tool (this page's rulings); [[default-colorway]] draws that line explicitly.

## THE FOUNDATION

**[📐 ssot_00_bold_venture_design_system.md](../00_EPISTEMOLOGY/📐%20ssot_00_bold_venture_design_system.md)** stays in `00_EPISTEMOLOGY` — it is not moved or duplicated here. It holds the ROSE anchor (`#8A1F44`), the FLESH ramp, the four registers (EMBER · PUNCH · DUST · NOIR), the Luminance Law, and the one-red ledger, ruled 2026-09-01 (v2.0.0). Read it before designing anything brand-facing or DARKROOM-facing.

## THE PAGE RULINGS

| Rule, in one line | Citation |
|---|---|
| Internal boards, dashboards and tool pages use the creator-cases palette (accent orange `#FF5A1F`/`#FF6B35`), never the brand rose — rose is DARKROOM's and public-facing surfaces only. **DARK is the only theme**, no toggle; a forced light face is E-INK Kindle-gray (`#D8D8D2`), never white. | RULED 2026-09-10 (colorway) and 2026-09-11 (dark-only) (memory: default-colorway) |
| Page headers are one thin strip, ≤ ~48px (name, search, a few counts, links); front-matter, edition and provenance sit behind a button, never across the top. Audit a page's first screen before publishing — content starts in the top ~100px. | Feedback 2026-09-24, on the SOI masthead (memory: thin-chrome) |
| Every Command page is dense with the CK3 hover-term pattern: every system term is hoverable, tooltips nest at least two deep, Space locks, Esc closes, click pins to the rail. A section with zero hover terms is a blocking RANGE finding. Amended 2026-09-24: plain hover fills a fixed Info View strip; the nested tooltip opens on click or Space, not on every hover. | Ruled 2026-09-16; amended 2026-09-24, BOLO 79 (memory: ck3-hover-layer-required) |
| A Mermaid diagram is written into the static `<pre class="mermaid">` markup the artifact host receives at build time; a page script must never inject it via `innerHTML` — the host's Mermaid pass runs once, over the DOM it is handed. | Found 2026-09-16, TM 04 (memory: mermaid-static-dom-only) |
| Every sit rep — and its siblings, DOPE SHEET N and the SOI — republishes as a dashboard page to one standing URL, never a new one, in the internal working palette (CK3 information architecture × Death Stranding surface). | RULED 2026-09-10–11, BOLO 38 (memory: sitrep-front-page) |
| Chief-facing learning material ships as the head version first — the sentence and the buttons, nothing else on the card, a score at the end. The complete, machine-facing version is offered only after, never by default. | Feedback 2026-09-06 (memory: learning-tools-minimal) |

## SOURCES — HELD, NOT YET DISTILLED

Tier 1 of the Zotero shelf's **06.3 Pages** section, `_tools/bolostatus/work/92/SHELF.md`. These are references the shelf pass held as foundational; none has been read into a rule above yet. `BVX.1002` (*Usage-Driven Database Design*) is skipped as an obvious misfit — a database-design text mis-tagged into the page-design shelf.

| BVX | Title | Author | Year |
|---|---|---|---|
| BVX.0292 | Building Design Systems: Unify User Experiences through a Shared Design Language | Vesselov, Davis | 2019 |
| — | Design Systems: A Practical Guide to Creating Design Languages for Digital Products | Kholmatova | — |
| BVX.0294 | Designing Information: Human Factors and Common Sense in Information Design | Katz | — |
| — | Designing Interfaces: Patterns for Effective Interaction Design | Tidwell, Brewer, Valencia | — |
| BVX.1031 | Elements of Design: Rowena Reed Kostellow and the Structure of Visual Relationships | Hannah | 2002 |
| BVX.1042 | Grammar of the Shot | Bowen | 2018 |
| — | Information Graphics: A Comprehensive Illustrated Reference | Harris | — |
| BVX.1047 | Layout and Composition for Animation | Ghertner | 2010 |
| — | The Photographer's Eye Graphic Guide: Composition and Design for Better Digital Photos | Freeman | — |
| BVX.1103 | The Visual Story: Creating the Structure of Film, TV, and Digital Media | Block | 2013 |
| — | Universal Principles of Design: 200 Ways to Increase Appeal, Enhance Usability, Influence Perception, and Make Better Design Decisions | Lidwell, Holden, Butler | 2023 |

## OPEN

- **Five of the eleven held sources carry no BVX id** — the shelf pass logged them by title only. Rec: run the next Zotero inventory pass (`_tools/zotero/inventory.py`) against these five titles and assign ids so they can be cited precisely instead of by title.
- **No ruling distills any of the eleven sources into a page rule yet.** Rec: when a page rule needs backing beyond memory (e.g. the CK3 hover pattern's information-density claim), pull first from Harris (*Information Graphics*) and Lidwell/Holden/Butler (*Universal Principles of Design*) — both are general-audience references already tier-1 and closest to the working-tool page problem.
- **Typography tokens** (Barlow Condensed / Atkinson Hyperlegible / IBM Plex Mono) live inside the default-colorway memory but have no SSOT home yet. Rec: fold them into this page's rulings table on the next FRAGO once a live reference page is repointed here.

## VERSION HISTORY

- **0.1.0 · 2026-09-29** — bootstrap: the foundation link to 00_EPISTEMOLOGY; six page rulings gathered from memory for the first time (colorway/dark-only, thin chrome, CK3 hover layer, Mermaid static DOM, the sit-rep dashboard pattern, minimal learning tools); eleven tier-1 SOURCES from the BOLO 92 shelf (one misfit skipped); three OPEN calls.
