---
title: "Pages style: reference"
type: reference
for: "A page builder looking up one design foundation or page ruling"
does: "Lists every component of pages style 07.3 with values and citations"
owner: Chief
state: draft
reviewed: 2026-10-05
source: "ShroomsQ/_CANON/_SSOT/07_STYLE_GUIDES/📐 ssot_07_3_pages_style.md"
source_version: "1.1.0"
---

**Who it's for:** a page builder looking up one ruling · **What it does:** lists every component of 07.3 with values and citations · **Type:** reference

# Pages style: reference

One entry per component of the source, in source order. See the [concept](1-concept.md) for the why.

## THE FOUNDATION

- **What it is:** the Bold Venture Design System, `ssot_00_bold_venture_design_system.md`, which lives in `00_EPISTEMOLOGY`. It is not duplicated.
- **Holds:** the ROSE anchor (`#8A1F44`), the FLESH ramp, the four registers (EMBER, PUNCH, DUST, NOIR). It also holds the Luminance Law and the one-red ledger.
- **Ruled:** 2026-09-01, v2.0.0.
- **Use for:** anything brand-facing or DARKROOM-facing. Read it before designing either.
- **Reads from 00 (IF-07-09-05):** the design system's color tokens (`--color-*`), `.bvx-*` typography classes and voice guidelines style any rendered page or template.
- **Connects to:** the page rulings below, which cover the internal-tool layer.

## THE PAGE RULINGS

The internal-tool layer. Seven rulings, each with its citation.

| # | Rule | Citation |
|---|---|---|
| 1 | **Palette.** Internal boards, dashboards and tool pages use the creator-cases palette, accent orange `#FF5A1F` or `#FF6B35`. Never the brand rose; rose is DARKROOM's and public-facing only. DARK is the only theme, no toggle. A forced light face is E-INK Kindle gray (`#D8D8D2`), never white. | RULED 2026-09-10 (colorway), 2026-09-11 (dark-only) |
| 2 | **Thin chrome.** A page header is one thin strip, about 48px at most: name, search, a few counts, links. Front matter, edition and provenance sit behind a button. Audit a page's first screen before publishing. Content starts in the top 100px. | Feedback 2026-09-24, on the SOI masthead |
| 3 | **CK3 hover layer.** Every system term is hoverable. Tooltips nest at least two deep. Space locks, Esc closes, click pins to the rail. A section with zero hover terms is a blocking RANGE finding. Amended 2026-09-24: plain hover fills a fixed Info View strip. The nested tooltip opens on click or Space, not on every hover. | Ruled 2026-09-16; amended 2026-09-24, BOLO 79 |
| 4 | **Mermaid static DOM.** Write a Mermaid diagram into the static `<pre class="mermaid">` markup the host receives at build time. A page script never injects it via `innerHTML`. The host's Mermaid pass runs once, over the DOM it is handed. | Found 2026-09-16, TM 04 |
| 5 | **Standing URL.** Every sit rep, and its siblings DOPE SHEET N and the SOI, republishes as a dashboard page to one standing URL, never a new one. It uses the internal working palette (CK3 information architecture crossed with Death Stranding surface). | RULED 2026-09-10 to 11, BOLO 38 |
| 6 | **Learning tools minimal.** Chief-facing learning material ships as the head version first: the sentence and the buttons, nothing else on the card, a score at the end. The complete machine version is offered only after, never by default. | Feedback 2026-09-06 |
| 7 | **Type.** Three faces, loaded from Google Fonts: Barlow Condensed (display, headings, labels), Atkinson Hyperlegible (body), IBM Plex Mono (codes, counts, metadata). | RULED 2026-09-10/11; folded here 2026-09-29 (BOLO 92, OPEN 3 rec) |

**Pages ruled by name (IF catalog call 7, ruled 2026-10-05).** The compiled world view page (IF-05-07-05, IF-05-07-07) takes the dark palette, the thin header strip, CK3 hover terms on every catalog type and test, and static Mermaid. The story workspace arrangement view (IF-07-08-05, BOLO 79) makes tracks, the rung ruler, the playhead and cables hoverable. Plain hover fills the Info View strip.

**Held sources.** The source also lists eleven tier-1 references from the Zotero shelf's 07.3 section. Nobody has read any of them into a rule yet. The first six are BVX.0292, BVX.1191, BVX.0294, BVX.0295, BVX.1031, BVX.1042. The last five are BVX.1192, BVX.1047, BVX.1193, BVX.1103, BVX.0301. BVX.1002 is skipped as a misfit.

**Ruled 2026-09-29 (source OPEN):** when a page rule needs backing beyond memory, pull first from Harris, *Information Graphics* (BVX.1192). Also pull from Lidwell, Holden and Butler, *Universal Principles of Design* (BVX.0301).
