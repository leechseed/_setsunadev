---
title: "Bold Venture Design System: tutorial"
type: tutorial
for: "a builder making a first screen in the design system"
does: "walks the source's System Explorer example, from background to status flags"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/05_OPERATIONS/📐 ssot_00_bold_venture_design_system.md
source_version: 2.0.1
---

**Who it's for:** a builder making a first screen in the design system · **What it does:** walks the source's System Explorer example, from background to status flags · **Type:** tutorial

# Style one screen: the System Explorer

You will follow the source's first example, the System Explorer. You finish with a screen whose background, tabs, cards, and flags use the right tokens.

The source's example uses the v1 (Astro) hex values. The Roster remap now sets the dark defaults, so the tutorial names tokens first and hex second.

> **OPEN:** the source's examples still cite v1 hex values. It does not say whether the Roster remap replaces them in these two examples.

## Step 1. Set the background

Use `--color-background-base-default` for the application background. The source gives `#101923` (v1). The Roster remap gives `#140A0E`.

## Step 2. Style the tabs

Use `--tab-color-text-default` for tabs at rest. Use `--tab-color-text-selected` for the active tab. Give the active tab a 4px bottom border in `--tab-border-color-selected`.

## Step 3. Style the layer cards

Use `--color-background-surface-default` for each card. Use `--color-background-surface-hover` on hover.

## Step 4. Color the status flags

Pick colors by severity, and use them for nothing else:

- ACTIVE flags: `--color-status-critical`.
- PENDING flags: `--color-status-serious`.
- FIRED_PRE_STORY flags: `--color-status-off`.

## Step 5. Flag out-of-range statistics

Show a Truth Exposure Index above 60 in `--color-status-serious` with a caution indicator. Show a Stress Threshold below zero in `--color-status-critical` with a critical indicator.

## Step 6. Check the surface

Confirm the screen is NOIR (dark UI), carries one identity element, and holds a rose hue in a top-two role. Confirm no non-status element uses a status color.

Next, read the [how-to](3-how-to.md) for each task alone.
