---
title: "Pages style: how-to"
type: how-to
for: "A page builder who knows the rulings and needs to do one page task"
does: "Gives numbered steps for the recurring tasks in pages style 07.3"
owner: Chief
state: draft
reviewed: 2026-10-05
source: "ShroomsQ/_CANON/_SSOT/07_STYLE_GUIDES/📐 ssot_07_3_pages_style.md"
source_version: "1.1.0"
---

**Who it's for:** a page builder doing one page task · **What it does:** gives numbered steps for each recurring 07.3 task · **Type:** how-to

# Pages style: how-to

Terms are defined in the [reference](2-reference.md).

## Choose the layer for a new page

1. Ask whether the page is brand-facing or a working tool.
2. If it is DARKROOM or public-facing, read the Bold Venture Design System and use rose.
3. If it is an internal board, dashboard or tool page, use the creator-cases palette with the orange accent.
4. Do not mix the two palettes on one page.

## Set the theme

1. Build in DARK. There is no toggle.
2. If a light face is forced, use E-INK Kindle gray `#D8D8D2`.
3. Never use white.

## Build the page header

1. Make the header one thin strip, about 48px at most.
2. Put name, search, a few counts and links in the strip.
3. Put front matter, edition and provenance behind a button.
4. Open the page and check the first screen. Content must start in the top 100px.

## Add the hover layer

1. List every system term on the page.
2. Make each term hoverable.
3. Nest tooltips at least two deep.
4. Wire Space to lock, Esc to close, click to pin to the rail.
5. Make plain hover fill the fixed Info View strip. Open the nested tooltip on click or Space.
6. Check each section has at least one hover term. A section with zero is a blocking RANGE finding.
7. On the world view page, make every catalog type and test a hover term. On the workspace arrangement view, make tracks, the rung ruler, the playhead and cables hover terms.

## Add a Mermaid diagram

1. Write the diagram into the static `<pre class="mermaid">` markup.
2. Write it into the page at build time.
3. Do not inject it with a page script or `innerHTML`.

## Republish a sit rep, DOPE SHEET or SOI

1. Find the page's standing URL.
2. Republish to that same URL.
3. Do not create a new URL.
4. Keep the internal working palette.

## Ship a learning page for Chief

1. Build the head version: the sentence and the buttons, nothing else on the card.
2. End with a score.
3. Offer the complete machine version only after, on request.

## Set the type

1. Load Barlow Condensed, Atkinson Hyperlegible and IBM Plex Mono from Google Fonts.
2. Set display, headings and labels in Barlow Condensed.
3. Set body text in Atkinson Hyperlegible.
4. Set codes, counts and metadata in IBM Plex Mono.
