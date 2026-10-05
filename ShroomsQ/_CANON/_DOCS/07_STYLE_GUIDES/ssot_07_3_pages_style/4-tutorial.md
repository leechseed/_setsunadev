---
title: "Pages style: tutorial"
type: tutorial
for: "A new page builder learning the rulings by building one internal board page"
does: "Teaches the page rulings by building a thin-chrome dark board with hover terms"
owner: Chief
state: draft
reviewed: 2026-10-05
source: "ShroomsQ/_CANON/_SSOT/07_STYLE_GUIDES/📐 ssot_07_3_pages_style.md"
source_version: "1.1.0"
---

**Who it's for:** a new page builder learning by doing · **What it does:** builds one internal board page that follows the rulings · **Type:** tutorial

# Pages style: build one internal board

The source's worked cases are the sit rep, the DOPE SHEET and the SOI. You will build a small board in the same style. Keep the [reference](2-reference.md) open.

## Step 1: pick the layer

Your board is an internal working tool. So you use the creator-cases palette, not the brand rose. Set the accent to orange `#FF5A1F`.

## Step 2: set the theme

Build in DARK only. Do not add a toggle. If something forces a light face, use `#D8D8D2`, never white.

## Step 3: set the type

Load the three faces from Google Fonts. Barlow Condensed goes on headings and labels. Atkinson Hyperlegible goes on body text. IBM Plex Mono goes on codes and counts.

## Step 4: build a thin header

Make one strip about 48px tall. Put the board's name, a search box, a few counts and links in it. Put edition and provenance behind a button.

Open the page. Check that content starts within the top 100px. The SOI masthead failed this check, which is why the ruling exists.

## Step 5: add hover terms

Pick every system term in your content. Make each hoverable. Nest one tooltip inside another. Wire Space to lock, Esc to close and click to pin.

Plain hover fills the Info View strip. The nested tooltip opens on click or Space.

## Step 6: add one diagram

Write the diagram into static `<pre class="mermaid">` markup at build time. Do not inject it with a script.

## Step 7: publish to the standing URL

The board republishes to one standing URL. Publish there and never mint a new one.

## Step 8: check your work

Walk the seven rulings once. They are palette, thin chrome, hover layer, static Mermaid, standing URL, minimal learning tools (not needed here), and type. Fix any miss. For single tasks, see the [how-to](3-how-to.md).
