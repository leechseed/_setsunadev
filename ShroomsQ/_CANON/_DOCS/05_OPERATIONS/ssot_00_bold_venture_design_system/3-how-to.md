---
title: "Bold Venture Design System: how-to"
type: how-to
for: "a builder making a screen, component, or surface that must follow the Bold Venture Design System"
does: "gives the steps for each task the design system asks of a builder"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/05_OPERATIONS/📐 ssot_00_bold_venture_design_system.md
source_version: 2.0.2
---

**Who it's for:** a builder making a screen, component, or surface that must follow the Bold Venture Design System · **What it does:** gives the steps for each task the design system asks of a builder · **Type:** how-to

# Bold Venture Design System: how-to

## Adopt the design system in a new application

1. Install the token package with `npm install @boldventure/tokens`.
2. Import the CSS in the entry point: `import '@boldventure/tokens/dist/css/index.css'`.
3. Leave the theme alone. The dark theme is the default and needs no class.
4. Add `.light-theme` to a wrapping container where you need the light theme.
5. Reference System Tokens for every color, spacing, and typography choice.
6. Install `@boldventure/web-components` for Web Components, or `@boldventure/react` for React.

## Assign a register to a surface

1. Find the surface in the surface map: labels, uniforms, signage, UI, social, shoots, or buildings.
2. Use the register the map names: EMBER, PUNCH, DUST, or NOIR.
3. Check the register's law before you use its palette. PUNCH never goes on UI status surfaces.
4. Confirm the surface carries one identity element: the rose mark, a rose-black ground, or a flesh moment.
5. Confirm a rose-family hue holds a top-two role on the surface.

## Check a warm color against skin

1. Find the brightest flesh token on the surface (flesh-300 `#FFDAC6`, L about 91).
2. Keep ambers and golds above that luminance, or use them as small source-motivated accents on dark grounds.
3. Never use a warm color as a midtone fill near skin.
4. Keep skin on the FLESH ramp with rose shadows. Apply warmth as a grade over the scene.

## Apply the status system

1. Identify the severity: Off, Standby, Normal, Caution, Serious, or Critical.
2. Use that level's color and its symbol shape.
3. Use status colors only for status.
4. If sub-statuses exist, show the highest urgency level on the parent.
5. On light backgrounds, add the mandatory darker border to the status symbol.

## Build a custom component

1. Use System Tokens for background, text, and border.
2. Map each state (default, hover, focus, disabled, invalid) to a System Token variant.
3. Apply `--opacity-disabled` (40%) when disabled.
4. Apply `--color-border-focus-default` to the focus ring.
5. Apply `--color-border-error` and `--color-text-error` when invalid.
6. Register the component in the inventory with the `bvx-` prefix.

## Extend the color system

1. Add the color only at the Reference Token level, named `--color-palette-{hue}-{shade}`.
2. Check it does not conflict with a status color.
3. Map it to a System Token before UI uses it.
4. Test WCAG AA contrast against the dark and light theme backgrounds.

## Choose a navigation pattern

1. Pick List-Detail for a small flat collection.
2. Pick Tab Navigation for distinct categories or step-wise workflows that finish within one tab.
3. Pick Tree Navigation for one hierarchical taxonomy. Never mix unrelated types.
4. Pick Table Navigation for a large uniform dataset needing search, sort, and filter.
5. Pick Timeline Navigation for event-based real-time scheduling.

## Add a form field with validation

1. Place the label top-left above the field in a one-column layout.
2. Put help text 8px below the field in secondary text color, sentence case.
3. Mark required fields with an asterisk if most fields are optional. Otherwise mark optional fields "(optional)".
4. Validate inline on focus loss: red border, with red bold text replacing the help text.
5. Validate the whole form on submit.
6. Write each error to say what is wrong, why, and how to fix it.

## Choose a notification type

1. Use a Log entry for the least disruptive message.
2. Use a Banner for an application-level message that must not block interaction.
3. Use a Toast for a temporary message. It auto-dismisses, stacks newest on top, and never covers critical elements.

## Move a rebrand through the tokens

1. Replace the Reference Token palette.
2. Run the token pipeline (Style Dictionary) to regenerate the outputs.
3. System and Component Tokens follow the change.
