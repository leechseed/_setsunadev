---
title: "Bold Venture Design System: concept"
type: concept
for: "Chief or a builder deciding how any BoldVenture screen, label, or page should look and behave"
does: "explains why one design system governs all Bold Venture output and how the Roster and the token tiers fit together"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/09_OPERATIONS/📐 ssot_00_bold_venture_design_system.md
source_version: 2.0.2
---

**Who it's for:** Chief or a builder deciding how any BoldVenture screen, label, or page should look and behave · **What it does:** explains why one design system governs all Bold Venture output. It also shows how the Roster and the token tiers fit together · **Type:** concept

# One design system sets the look of all Bold Venture output

The **Bold Venture Design System** is the mandatory visual and interaction standard for all digital output under Bold Venture. Every application, dashboard, tool, template renderer, and interactive artifact conforms to it. It is a Command-wide base tool. It is not part of the storytelling stack: it holds no story method, and no story system depends on it.

## The system is adapted, not invented

The source adapts it wholesale from the Astro UXDS v7, a military-grade, open-source design system built by Rocket Communications Inc. for the U.S. Space Force. Astro complies with MIL-STD-1472H, MIL-STD-2525D, and WCAG 2.1 AA. Bold Venture inherits those properties, then rebrands the names: the `rux-` prefix becomes `bvx-`.

## The brand color layer is proprietary

Version 2.0.0 (2026-09-01) added the **Roster**, the brand color layer. The Roster holds one identity and four registers. The Astro palettes remain only as legacy infrastructure. They keep the grey ramp for chrome and the status system, which the source calls sacred. The blues are retired from brand duty.

## One identity, four registers

The identity is rose, flesh, grounds, and gold. It appears on every surface. The four registers are EMBER (all-hours ambient), PUNCH (the live edge), DUST (daylight), and NOIR (the deep default). Each surface gets an assigned register. The adhesive rule says every surface carries at least one identity element. The rose quota says a rose-family hue holds a top-two role on every branded surface.

## The Luminance Law protects skin

Warm color flatters skin only when it outshines the brightest flesh token. Below that luminance it jaundices. The law makes the rule measurable, and it replaces the earlier vibe-rule.

## Three token tiers keep change cheap

Reference tokens hold raw values. System tokens carry meaning and change with the theme. Component tokens follow their system tokens. A rebrand replaces the reference palette, and the change cascades down.

## Status is sacred

Status colors serve status and nothing else. Every status level also carries a shape, so color is never the only signal. The Roster leaves the status tokens unchanged.

For every component and token, read the [reference](2-reference.md). For the tasks, read the [how-to](3-how-to.md). For a worked screen, read the [tutorial](4-tutorial.md).

## The long read

The source's own history shows the layering. Version 1.0.0 (2026-03-09) was the wholesale Astro adaptation. It had 15 hues, dark and light themes, a six-level status system, and 18 typography styles. It also had a 15-step spacing scale and a 40-component inventory. Version 2.0.0 added the Roster after a challenge bench of 11 palettes and a four-lens panel (record `wf_5b0af08b-c49`). Version 2.0.1 (2026-10-04, BOLO 100) repaired the frontmatter and added `trunk: ORANGE` and the scope line. It changed no design content. The Astro hex values below the Roster section are legacy numbers. A reader who builds a surface today reads the Roster first, then the semantic remap, then the rest.
