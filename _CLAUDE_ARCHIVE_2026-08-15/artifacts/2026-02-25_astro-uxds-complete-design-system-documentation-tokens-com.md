---
title: "Astro UXDS Complete Design System Documentation: Tokens, Components, and Compliance Specifications for LEECHSEED Rebranding"
source_conversation: "Character database system architecture with Dramatica and astrology integration"
created: 2026-02-25
trunk: BLACK
kind: artifact
---

# Astro UXDS: complete design system documentation

**Astro UXDS is a military-grade, open-source design system built by Rocket Communications Inc. for the U.S. Space Force**, providing the complete foundation for Department of Defense space operations applications. This document captures every token, color, component, and specification needed to produce a rebranded fork—the LEECHSEED UX Design System for Bold Venture. All values below are sourced directly from astrouxds.com (v7.x), the `@astrouxds/tokens` npm package (v1.14.0), and the GitHub monorepo at `RocketCommunicationsInc/astro`.

---

## Architecture and token hierarchy

Astro uses a **three-tier design token system** processed through a pipeline: Figma → `data/tokens.json` → Token Transformer → `/tokens/*.json` → Style Dictionary → `/dist` (CSS, SCSS, JSON, iOS). The npm package `@astrouxds/tokens` ships all output formats. The web components live in `@astrouxds/astro-web-components` (Stencil.js), with framework wrappers in `@astrouxds/react` and `@astrouxds/angular`.

**Tier 1 — Reference Tokens** are raw palette values with no semantic meaning (e.g., `--color-palette-brightblue-500: #4dacff`). **Tier 2 — System Tokens** carry intent and are the preferred tier for custom UI (e.g., `--color-background-interactive-default: #4dacff`). **Tier 3 — Component Tokens** are scoped to individual components and may change across releases (e.g., `--button-color-background-default`).

The naming convention follows up to nine levels: `[group]-[component]-[element]-[category]-[property]-[concept]-[variant]-[state]-[scale]`. Not all tokens use every level. Dark theme is the default; light theme is activated by adding the `.light-theme` CSS class to a wrapping element. Token files are distributed as:

| Format | Files |
|---|---|
| CSS Custom Properties | `dist/css/index.css`, `base.reference.css`, `base.system.css`, `base.component.css` |
| CSS Light Theme | `dist/css/theme.light.css` (`.light-theme` class) |
| CSS Typography | `dist/css/classes/typography.css` |
| SCSS Variables | `dist/scss/base.reference.scss`, `base.system.scss`, `base.component.scss` |
| JSON (flat + nested) | `dist/json/base.reference.json`, `base.system.json`, `base.component.json` |

---

## Complete reference color palettes

Every hex value below is a Reference Token accessed via `var(--color-palette-{hue}-{shade})`.

### Neutral

| Token | Hex |
|---|---|
| `neutral-1000` | `#000000` |
| `neutral-000` | `#ffffff` |
| `neutral-1000a00` | `#00000000` (transparent) |

### Dark Blue

| Token | Hex | Token | Hex |
|---|---|---|---|
| `darkblue-100` | `#cbdee9` | `darkblue-600` | `#004872` |
| `darkblue-200` | `#98bdd3` | `darkblue-700` | `#1c3f5e` |
| `darkblue-300` | `#649cbd` | `darkblue-800` | `#1b2d3e` |
| `darkblue-400` | `#2f7aa7` | `darkblue-900` | `#172635` |
| `darkblue-500` | `#005a8f` | `darkblue-950` | `#080c11` |

### Bright Blue

| Token | Hex | Token | Hex |
|---|---|---|---|
| `brightblue-100` | `#daeeff` | `brightblue-600` | `#3a87cf` |
| `brightblue-200` | `#cee9fc` | `brightblue-700` | `#2b659b` |
| `brightblue-300` | `#b7dcff` | `brightblue-800` | `#1c3851` |
| `brightblue-400` | `#92cbff` | `brightblue-850` | `#142435` |
| `brightblue-500` | `#4dacff` | `brightblue-900` | `#101923` |

### Grey

| Token | Hex | Token | Hex |
|---|---|---|---|
| `grey-100` | `#f5f6f9` | `grey-500` | `#a4abb6` |
| `grey-200` | `#eaeef4` | `grey-600` | `#7b8089` |
| `grey-250` | `#e0e5eb` | `grey-700` | `#51555b` |
| `grey-300` | `#d4d8dd` | `grey-800` | `#3c3e42` |
| `grey-400` | `#bbc1c9` | `grey-900` | `#292a2d` |

### Red

| Token | Hex | Token | Hex |
|---|---|---|---|
| `red-400` | `#ff5f60` | `red-700` | `#c8102e` |
| `red-500` | `#ff3838` | `red-800` | `#8b1703` |
| `red-600` | `#ff2a04` | `red-900` | `#661102` |

### Orange

| Token | Hex | Token | Hex |
|---|---|---|---|
| `orange-400` | `#ffcc57` | `orange-700` | `#ff8c00` |
| `orange-500` | `#ffb302` | `orange-800` | `#975f0e` |
| `orange-600` | `#ffaf3d` | `orange-900` | `#664618` |

### Yellow

| Token | Hex | Token | Hex |
|---|---|---|---|
| `yellow-400` | `#fded61` | `yellow-700` | `#c7ab00` |
| `yellow-500` | `#fce83a` | `yellow-800` | `#917d01` |
| `yellow-600` | `#fad800` | `yellow-900` | `#645600` |

### Green

| Token | Hex | Token | Hex |
|---|---|---|---|
| `green-400` | `#99f666` | `green-700` | `#00ad23` |
| `green-500` | `#56f000` | `green-800` | `#007a33` |
| `green-600` | `#00e200` | `green-900` | `#005a00` |

### Cyan

| Token | Hex | Token | Hex |
|---|---|---|---|
| `cyan-400` | `#5ce2ff` | `cyan-700` | `#20a9d5` |
| `cyan-500` | `#64d9ff` | `cyan-800` | `#35798e` |
| `cyan-600` | `#2dccff` | `cyan-900` | `#285766` |

### Teal (tag/data-viz palette)

| Token | Hex | Token | Hex |
|---|---|---|---|
| `teal-100` | `#d0f4f4` | `teal-600` | `#009fa3` |
| `teal-200` | `#a1e9eb` | `teal-700` | `#00777a` |
| `teal-300` | `#70dde0` | `teal-800` | `#035051` |
| `teal-400` | `#3ed2d6` | `teal-900` | `#032828` |
| `teal-500` | `#00c7cb` | | |

### Purple (tag/data-viz palette)

| Token | Hex | Token | Hex |
|---|---|---|---|
| `purple-100` | `#e4e2f7` | `purple-600` | `#6058a8` |
| `purple-200` | `#c9c5ed` | `purple-700` | `#48417f` |
| `purple-300` | `#aea8e5` | `purple-800` | `#302c54` |
| `purple-400` | `#938bdb` | `purple-900` | `#18152b` |
| `purple-500` | `#786dd3` | | |

### Pink (tag palette)

| Token | Hex | Token | Hex |
|---|---|---|---|
| `pink-100` | `#edcef3` | `pink-600` | `#81009a` |
| `pink-200` | `#da9ce7` | `pink-700` | `#610074` |
| `pink-300` | `#c76ada` | `pink-800` | `#41004d` |
| `pink-400` | `#b534ce` | `pink-900` | `#200227` |
| `pink-500` | `#a200c1` | | |

### Hot Orange (tag palette)

| Token | Hex | Token | Hex |
|---|---|---|---|
| `hotorange-100` | `#f8ddd1` | `hotorange-600` | `#af420a` |
| `hotorange-200` | `#f0baa3` | `hotorange-700` | `#833209` |
| `hotorange-300` | `#ea9875` | `hotorange-800` | `#572108` |
| `hotorange-400` | `#e27545` | `hotorange-900` | `#2b1105` |
| `hotorange-500` | `#da5309` | | |

### Special single-shade hues

| Token | Hex |
|---|---|
| `violet-800` | `#502b85` |
| `blue-800` | `#0033a0` |

---

## System tokens — dark theme (default)

All accessed via `var(--{token-name})`. These carry semantic meaning and are the **preferred tier for custom UI**.

### Background colors

| CSS Custom Property | Hex | Reference | Usage |
|---|---|---|---|
| `--color-background-base-default` | `#101923` | brightblue-900 | App background, popup menus |
| `--color-background-base-header` | `#172635` | darkblue-900 | Header of base elements |
| `--color-background-base-hover` | `#142435` | brightblue-850 | Base hover state |
| `--color-background-base-selected` | `#1c3f5e` | darkblue-700 | Base selected state |
| `--color-background-surface-default` | `#1b2d3e` | darkblue-800 | Panels, dialogs, cards |
| `--color-background-surface-header` | `#172635` | darkblue-900 | Dialog/table headers |
| `--color-background-surface-hover` | `#1c3851` | brightblue-800 | Card/table row hover |
| `--color-background-surface-selected` | `#1c3f5e` | darkblue-700 | Card/table row selected |
| `--color-background-interactive-default` | `#4dacff` | brightblue-500 | Primary interactive BG |
| `--color-background-interactive-hover` | `#92cbff` | brightblue-400 | Interactive hover BG |
| `--color-background-interactive-muted` | `#2b659b` | brightblue-700 | Muted interactive BG |
| `--color-background-transparent` | `#00000000` | neutral-1000a00 | Transparent |

### Text colors

| CSS Custom Property | Hex | Reference |
|---|---|---|
| `--color-text-primary` | `#ffffff` | neutral-000 |
| `--color-text-secondary` | `#d4d8dd` | grey-300 |
| `--color-text-placeholder` | `#a4abb6` | grey-500 |
| `--color-text-inverse` | `#080c11` | darkblue-950 |
| `--color-text-interactive-default` | `#4dacff` | brightblue-500 |
| `--color-text-interactive-hover` | `#92cbff` | brightblue-400 |
| `--color-text-white` | `#ffffff` | neutral-000 |
| `--color-text-black` | `#000000` | neutral-1000 |
| `--color-text-error` | `#ff3838` | red-500 |

### Border colors

| CSS Custom Property | Hex | Reference |
|---|---|---|
| `--color-border-interactive-default` | `#4dacff` | brightblue-500 |
| `--color-border-interactive-hover` | `#92cbff` | brightblue-400 |
| `--color-border-interactive-muted` | `#2b659b` | brightblue-700 |
| `--color-border-error` | `#ff3838` | red-500 |

### Status colors (dark theme)

| Status | Hex | RGB | CSS Custom Property |
|---|---|---|---|
| **Critical** | `#ff3838` | 255, 56, 56 | `--color-status-critical` |
| **Serious** | `#ffb302` | 255, 179, 2 | `--color-status-serious` |
| **Caution** | `#fce83a` | 252, 232, 58 | `--color-status-caution` |
| **Normal** | `#56f000` | 86, 240, 0 | `--color-status-normal` |
| **Standby** | `#2dccff` | 45, 204, 255 | `--color-status-standby` |
| **Off** | `#a4abb6` | 164, 171, 182 | `--color-status-off` |

### Data visualization (dark theme)

| Token | Hex | Reference |
|---|---|---|
| `--color-data-visualization-1` | `#00c7cb` | teal-500 |
| `--color-data-visualization-2` | `#938bdb` | purple-400 |
| `--color-data-visualization-3` | `#4dacff` | brightblue-500 |
| `--color-data-visualization-4` | `#70dde0` | teal-300 |
| `--color-data-visualization-5` | `#c9c5ed` | purple-200 |
| `--color-data-visualization-6` | `#92cbff` | brightblue-400 |
| `--color-data-visualization-7` | `#a1e9eb` | teal-200 |
| `--color-data-visualization-8` | `#b7dcff` | brightblue-300 |

### Classification marking colors (identical in both themes)

| Level | Hex | RGB | Font Color |
|---|---|---|---|
| Top Secret//SCI | `#fce83a` | 252, 232, 58 | black |
| Top Secret | `#ff8c00` | 255, 140, 0 | black |
| Secret | `#c8102e` | 200, 16, 46 | white |
| Confidential | `#0033a0` | 0, 51, 160 | white |
| CUI | `#502b85` | 80, 43, 133 | white |
| Unclassified | `#007a33` | 0, 122, 51 | white |

CSS tokens: `--color-classification-topsecretsci`, `--color-classification-topsecret`, `--color-classification-secret`, `--color-classification-confidential`, `--color-classification-cui`, `--color-classification-unclassified`. Banner component tokens: `--classification-banner-color-background-{level}`.

### Focus, shadow, and opacity (dark theme)

| Token | Value |
|---|---|
| `--color-border-focus-default` | `#da9ce7` (pink-200) |
| `--border-width-focus-default` | `1px` |
| `--spacing-focus-default` | `0.125rem` (2px) |
| `--shadow-overlay` | `0px 4px 4px 1px rgba(0, 0, 0, 0.45)` |
| `--opacity-disabled` | `40%` |

---

## System tokens — light theme

Applied via the `.light-theme` CSS class. Same property names, different values.

### Background colors (light)

| CSS Custom Property | Hex | Reference |
|---|---|---|
| `--color-background-base-default` | `#eaeef4` | grey-200 |
| `--color-background-base-header` | `#f5f6f9` | grey-100 |
| `--color-background-base-hover` | `#98bdd3` | darkblue-200 |
| `--color-background-base-selected` | `#cee9fc` | brightblue-200 |
| `--color-background-surface-default` | `#ffffff` | neutral-000 |
| `--color-background-surface-header` | `#f5f6f9` | grey-100 |
| `--color-background-surface-hover` | `#daeeff` | brightblue-100 |
| `--color-background-surface-selected` | `#cee9fc` | brightblue-200 |
| `--color-background-interactive-default` | `#005a8f` | darkblue-500 |
| `--color-background-interactive-hover` | `#1c3f5e` | darkblue-700 |
| `--color-background-interactive-muted` | `#2f7aa7` | darkblue-400 |

### Text colors (light)

| CSS Custom Property | Hex | Reference |
|---|---|---|
| `--color-text-primary` | `#292a2d` | grey-900 |
| `--color-text-secondary` | `#51555b` | grey-700 |
| `--color-text-placeholder` | `#7b8089` | grey-600 |
| `--color-text-inverse` | `#ffffff` | neutral-000 |
| `--color-text-interactive-default` | `#005a8f` | darkblue-500 |
| `--color-text-interactive-hover` | `#1c3f5e` | darkblue-700 |
| `--color-text-error` | `#c8102e` | red-700 |

### Border colors (light)

| CSS Custom Property | Hex |
|---|---|
| `--color-border-interactive-default` | `#005a8f` |
| `--color-border-interactive-hover` | `#1c3f5e` |
| `--color-border-interactive-muted` | `#2f7aa7` |
| `--color-border-error` | `#c8102e` |

### Status colors (light theme — fill + required WCAG border)

| Status | Fill Hex | Border Hex | Fill CSS Token | Border CSS Token |
|---|---|---|---|---|
| Critical | `#ff2a04` | `#661102` | `--status-symbol-color-fill-critical` | `--status-symbol-color-border-critical` |
| Serious | `#ffaf3d` | `#664618` | `--status-symbol-color-fill-serious` | `--status-symbol-color-border-serious` |
| Caution | `#fad800` | `#645600` | `--status-symbol-color-fill-caution` | `--status-symbol-color-border-caution` |
| Normal | `#00e200` | `#005a00` | `--status-symbol-color-fill-normal` | `--status-symbol-color-border-normal` |
| Standby | `#64d9ff` | `#285766` | `--status-symbol-color-fill-standby` | `--status-symbol-color-border-standby` |
| Off | `#7b8089` | `#3c3e42` | `--status-symbol-color-fill-off` | `--status-symbol-color-border-off` |

### Data visualization (light theme)

| Token | Hex | Reference |
|---|---|---|
| `--color-data-visualization-1` | `#035051` | teal-800 |
| `--color-data-visualization-2` | `#6058a8` | purple-600 |
| `--color-data-visualization-3` | `#1c3851` | brightblue-800 |
| `--color-data-visualization-4` | `#00777a` | teal-700 |
| `--color-data-visualization-5` | `#786dd3` | purple-500 |
| `--color-data-visualization-6` | `#2b659b` | brightblue-700 |
| `--color-data-visualization-7` | `#009fa3` | teal-600 |
| `--color-data-visualization-8` | `#3a87cf` | brightblue-600 |

### Focus and shadow (light)

| Token | Value |
|---|---|
| `--color-border-focus-default` | `#b534ce` (pink-400) |
| `--shadow-overlay` | `0px 4px 4px 1px rgba(0, 0, 0, 0.35)` |

---

## Typography system

Astro 7 uses **Roboto** as the sole typeface. Roboto Mono was dropped in v7; the Monospace 1 style now uses the same sans-serif stack. All typography tokens follow the pattern `--font-{identifier}-{property}`.

### Font family

```
--font-family-sans: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI',
  Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif;
```

### Font size scale

| Token | CSS Custom Property | rem | px |
|---|---|---|---|
| `font-size-xs` | `var(--font-size-xs)` | 0.75 | 12 |
| `font-size-sm` | `var(--font-size-sm)` | 0.875 | 14 |
| `font-size-base` | `var(--font-size-base)` | 1 | 16 |
| `font-size-lg` | `var(--font-size-lg)` | 1.125 | 18 |
| `font-size-xl` | `var(--font-size-xl)` | 1.25 | 20 |
| `font-size-2xl` | `var(--font-size-2xl)` | 1.5 | 24 |
| `font-size-3xl` | `var(--font-size-3xl)` | 1.75 | 28 |
| `font-size-4xl` | `var(--font-size-4xl)` | 2.125 | 34 |
| `font-size-5xl` | `var(--font-size-5xl)` | 3 | 48 |
| `font-size-6xl` | `var(--font-size-6xl)` | 3.75 | 60 |

### Font weights

| Token | Value |
|---|---|
| `--font-weight-light` | 300 |
| `--font-weight-regular` | 400 |
| `--font-weight-medium` | 500 |
| `--font-weight-bold` | 700 |

### Line height scale

| Token | rem | px |
|---|---|---|
| `--line-height-2xs` | 0.875 | 14 |
| `--line-height-xs` | 1 | 16 |
| `--line-height-sm` | 1.25 | 20 |
| `--line-height-base` | 1.5 | 24 |
| `--line-height-lg` | 1.75 | 28 |
| `--line-height-xl` | 2 | 32 |
| `--line-height-2xl` | 2.5 | 40 |
| `--line-height-3xl` | 3.5 | 56 |
| `--line-height-4xl` | 4.375 | 70 |

### Letter spacing scale

| Token | Value |
|---|---|
| `--letter-spacing-sm` | −0.005em |
| `--letter-spacing-base` | 0em |
| `--letter-spacing-lg` | 0.0015em |
| `--letter-spacing-xl` | 0.0025em |
| `--letter-spacing-2xl` | 0.005em |

### Complete typography styles

Each style produces five CSS custom properties: `--font-{id}-font-family`, `--font-{id}-font-size`, `--font-{id}-font-weight`, `--font-{id}-letter-spacing`, `--font-{id}-line-height`.

| Style | CSS Class | Size (rem/px) | Weight | Line Height | Letter Spacing |
|---|---|---|---|---|---|
| **Display 1** | `.rux-display-1` | 3.75 / 60 | 300 (Light) | calc(70/60) ≈ 1.167 | −0.005em |
| **Display 2** | `.rux-display-2` | 3 / 48 | 400 (Regular) | calc(56/48) ≈ 1.167 | 0em |
| **Heading 1** | `.rux-heading-1` | 2.125 / 34 | 400 (Regular) | calc(40/34) ≈ 1.176 | 0.0025em |
| **Heading 1 Bold** | `.rux-heading-1-bold` | 2.125 / 34 | 700 (Bold) | calc(40/34) ≈ 1.176 | 0.0025em |
| **Heading 2** | `.rux-heading-2` | 1.5 / 24 | 400 (Regular) | calc(28/24) ≈ 1.167 | 0em |
| **Heading 3** | `.rux-heading-3` | 1.25 / 20 | 500 (Medium) | calc(24/20) = 1.2 | 0.0015em |
| **Heading 4** | `.rux-heading-4` | 1.25 / 20 | 300 (Light) | calc(24/20) = 1.2 | 0.0015em |
| **Heading 5** | `.rux-heading-5` | 1.125 / 18 | 400 (Regular) | calc(24/18) ≈ 1.333 | 0em |
| **Heading 6** | `.rux-heading-6` | 1.125 / 18 | 300 (Light) | calc(24/18) ≈ 1.333 | 0em |
| **Body 1** | `.rux-body-1` | 1 / 16 | 400 (Regular) | calc(24/16) = 1.5 | 0.005em |
| **Body 1 Bold** | `.rux-body-1-bold` | 1 / 16 | 700 (Bold) | calc(24/16) = 1.5 | 0.005em |
| **Body 2** | `.rux-body-2` | 0.875 / 14 | 400 (Regular) | calc(20/14) ≈ 1.429 | 0.005em |
| **Body 2 Bold** | `.rux-body-2-bold` | 0.875 / 14 | 700 (Bold) | calc(20/14) ≈ 1.429 | 0.005em |
| **Body 3** | `.rux-body-3` | 0.75 / 12 | 400 (Regular) | calc(16/12) ≈ 1.333 | 0.005em |
| **Body 3 Bold** | `.rux-body-3-bold` | 0.75 / 12 | 700 (Bold) | calc(16/12) ≈ 1.333 | 0.005em |
| **Control Body 1** | `.rux-control-body-1` | 1 / 16 | 400 (Regular) | calc(20/16) = 1.25 | 0.005em |
| **Control Body 1 Bold** | `.rux-control-body-1-bold` | 1 / 16 | 700 (Bold) | calc(20/16) = 1.25 | 0.005em |
| **Monospace 1** | `.rux-monospace-1` | 1.75 / 28 | 500 (Medium) | calc(32/28) ≈ 1.143 | 0em |

---

## Spacing system

Built on a **4px base grid**. The token number multiplied by 4 gives the pixel value (exceptions: `025` = 1px, `050` = 2px). Border-collapse sizing is used—borders overlap padding.

| Token | CSS Custom Property | rem | px |
|---|---|---|---|
| `spacing-0` | `var(--spacing-0)` | 0 | 0 |
| `spacing-025` | `var(--spacing-025)` | 0.0625 | 1 |
| `spacing-050` | `var(--spacing-050)` | 0.125 | 2 |
| `spacing-1` | `var(--spacing-1)` | 0.25 | 4 |
| `spacing-2` | `var(--spacing-2)` | 0.5 | 8 |
| `spacing-3` | `var(--spacing-3)` | 0.75 | 12 |
| `spacing-4` | `var(--spacing-4)` | 1 | 16 |
| `spacing-6` | `var(--spacing-6)` | 1.5 | 24 |
| `spacing-8` | `var(--spacing-8)` | 2 | 32 |
| `spacing-10` | `var(--spacing-10)` | 2.5 | 40 |
| `spacing-12` | `var(--spacing-12)` | 3 | 48 |
| `spacing-14` | `var(--spacing-14)` | 3.5 | 56 |
| `spacing-16` | `var(--spacing-16)` | 4 | 64 |
| `spacing-20` | `var(--spacing-20)` | 5 | 80 |
| `spacing-24` | `var(--spacing-24)` | 6 | 96 |

### Border, radii, and opacity reference tokens

| Token | Value |
|---|---|
| `--border-width-none` | 0 |
| `--border-width-xs` | 1px |
| `--border-width-sm` | 2px |
| `--border-width-lg` | 4px |
| `--radius-base` | 3px |
| `--radius-circle` | 50% |
| `--opacity-0` | 0% |
| `--opacity-25` | 25% |
| `--opacity-35` | 35% |
| `--opacity-40` | 40% |
| `--opacity-45` | 45% |
| `--opacity-50` | 50% |

### Responsive grid

| Breakpoint | Columns | Margin | Gap (default) | Gap (compact) |
|---|---|---|---|---|
| 0–360px | 4 | 16px | 16px | 8px |
| 361–768px | 8 | 24px | 24px | 12px |
| 769–1920px | 12 | 24px | 24px | 12px |
| 1921–3840px | 12 | 48px | 48px | 24px |

---

## Component tokens — dark theme (key components)

These Tier 3 tokens are scoped to individual components. All accessed via `var(--{token})`.

### Button

| Token | Value |
|---|---|
| `--button-color-background-default` | `#4dacff` |
| `--button-color-background-hover` | `#92cbff` |
| `--button-color-background-secondary` | `#00000000` (transparent) |
| `--button-color-background-borderless` | `#00000000` |
| `--button-color-text-default` | `#080c11` |
| `--button-color-text-secondary-default` | `#4dacff` |
| `--button-color-text-secondary-hover` | `#92cbff` |
| `--button-color-text-borderless-default` | `#4dacff` |
| `--button-border-width` | 1px |
| `--button-radius` | 3px |
| `--button-icon-dimension` | 20px |
| `--button-padding-x-large` | 1rem |
| `--button-padding-x-medium` | 1rem |
| `--button-padding-x-small` | 1rem |
| `--button-padding-y-large` | 0.75rem |
| `--button-padding-y-medium` | 0.5rem |
| `--button-padding-y-small` | 0.25rem |

### Input

| Token | Value |
|---|---|
| `--input-color-background` | `#101923` |
| `--input-color-border-default` | `#2b659b` |
| `--input-color-border-hover` | `#92cbff` |
| `--input-color-border-invalid` | `#ff3838` |
| `--input-color-text` | `#ffffff` |
| `--input-color-placeholder` | `#a4abb6` |
| `--input-color-icon` | `#4dacff` |
| `--input-icon-dimension` | 20px |
| `--input-radius` | 3px |
| `--input-border-width` | 1px |
| `--input-padding-x-large` | 0.75rem |
| `--input-padding-x-medium` | 0.5rem |
| `--input-padding-y-large` | 0.5rem |
| `--input-padding-y-medium` | 0.5rem |
| `--input-padding-y-small` | 0.25rem |

### Table

| Token | Value |
|---|---|
| `--table-header-color-background` | `#172635` |
| `--table-header-shadow` | `0px 4px 8px 0px rgba(0,0,0,0.45)` |
| `--table-row-color-background-default` | `#1b2d3e` |
| `--table-row-color-background-selected` | `#1c3f5e` |
| `--table-row-color-background-hover` | `#1c3851` |
| `--table-row-color-text` | `#ffffff` |
| `--table-row-color-border` | `#101923` |
| `--table-row-border-width` | 1px |
| `--table-body-cell-padding-y` | 0.25rem |
| `--table-body-cell-padding-x` | 0.5rem |

### Global Status Bar

| Token | Value |
|---|---|
| `--global-status-bar-color-background` | `#172635` |
| `--global-status-bar-color-text` | `#ffffff` |
| `--global-status-bar-icon-color-default` | `#4dacff` |
| `--global-status-bar-icon-color-hover` | `#92cbff` |

### Tab

| Token | Value |
|---|---|
| `--tab-color-text-default` | `#4dacff` |
| `--tab-color-text-hover` | `#92cbff` |
| `--tab-color-text-selected` | `#ffffff` |
| `--tab-border-color-selected` | `#4dacff` |
| `--tab-border-width-bottom` | 4px |

### Other component tokens

| Component | Key Tokens |
|---|---|
| **Card** | `--card-color-border: #51555b`, `--card-color-background: #101923`, `--card-radius: 3px`, `--card-border-width: 1px`, `--card-shadow: 0px 4px 4px 1px rgba(0,0,0,0.45)` |
| **Notification Banner** | `--notification-banner-color-background: #101923`, `--notification-banner-radius-outer: 3px`, `--notification-banner-radius-inner: 2px`, prefix dimension 32px. Status border colors match system status colors. |
| **Tooltip** | `--tooltip-color-background: #3c3e42`, `--tooltip-color-text: #ffffff`, `--tooltip-radius: 1px` |
| **Progress** | `--progress-radius-inner: 8px`, `--progress-radius-outer: 10px`, `--progress-border-width: 1px`, `--progress-color-background: #1b2d3e`, `--progress-color-inner: #4dacff` |
| **Select** | `--select-color-background: #101923`, `--select-border-width: 1px`, `--select-radius: 3px`, `--select-caret-dimension: 30px` |
| **Checkbox** | `--checkbox-control-dimension: 24px`, `--checkbox-control-padding: 0.125rem`, `--checkbox-control-radius: 2px`, `--checkbox-label-margin-left: 0.5rem` |
| **Radio** | `--radio-control-dimension: 24px`, `--radio-control-radius: 50%`, `--radio-control-padding: 0.125rem` |
| **Slider** | `--slider-thumb-dimension: 20px`, `--slider-thumb-radius: 50%`, `--slider-thumb-border-width: 2px`, `--slider-track-height-active: 4px`, `--slider-track-height-inactive: 1px` |
| **Switch** | `--switch-track-radius: 10px` |
| **Tag** | `--tag-radius: 4px`, `--tag-color-text: #ffffff`. Status variants: `--tag-shadow-inner-pass: inset 0 0 5px rgb(86,240,0)`, `--tag-shadow-inner-fail: inset 0 0 5px rgb(255,56,56)` |

---

## All components — complete inventory

Astro ships **34+ components** as W3C Web Components built with Stencil.js. All tag names use the `rux-` prefix. Package: `@astrouxds/astro-web-components`.

| # | Component | Web Component Tag(s) | Category |
|---|---|---|---|
| 1 | Accordion | `rux-accordion`, `rux-accordion-item` | Layout |
| 2 | Application State | (pattern within GSB) | Navigation |
| 3 | Breadcrumb | `rux-breadcrumb`, `rux-breadcrumb-item` | Navigation |
| 4 | Button | `rux-button` | Actions |
| 5 | Card | `rux-card` | Layout |
| 6 | Checkbox | `rux-checkbox`, `rux-checkbox-group` | Form Controls |
| 7 | Classification Markings | `rux-classification-marking` | Data Display |
| 8 | Clock | `rux-clock` | Data Display |
| 9 | Container | `rux-container` | Layout |
| 10 | Date Picker | `rux-datetime` (custom) | Form Controls |
| 11 | Dialog | `rux-dialog` | Feedback/Overlay |
| 12 | Global Status Bar | `rux-global-status-bar` | Navigation |
| 13 | Icon | `rux-icon` | Data Display |
| 14 | Indeterminate Progress | `rux-indeterminate-progress` | Feedback |
| 15 | Input Field | `rux-input` | Form Controls |
| 16 | Link | (native `<a>` styled via CSS) | Navigation |
| 17 | Log | `rux-log` | Data Display |
| 18 | Menu | `rux-menu`, `rux-menu-item`, `rux-menu-item-divider` | Actions |
| 19 | Monitoring Icon | `rux-monitoring-icon` | Data Display |
| 20 | Monitoring Progress Icon | `rux-monitoring-progress-icon` | Data Display |
| 21 | Notification Banner | `rux-notification` | Feedback |
| 22 | Pagination | `rux-pagination` | Navigation |
| 23 | Pop Up | `rux-pop-up` | Actions |
| 24 | Progress | `rux-progress` | Feedback |
| 25 | Push Button | `rux-push-button` | Actions |
| 26 | Radio Button | `rux-radio`, `rux-radio-group` | Form Controls |
| 27 | Search | (rux-input variant) | Form Controls |
| 28 | Segmented Button | `rux-segmented-button` | Actions |
| 29 | Select | `rux-select`, `rux-option`, `rux-option-group` | Form Controls |
| 30 | Slider | `rux-slider` | Form Controls |
| 31 | Status Symbol | `rux-status` | Data Display |
| 32 | Switch | `rux-switch` | Form Controls |
| 33 | Table | `rux-table` | Data Display |
| 34 | Tabs | `rux-tabs`, `rux-tab`, `rux-tab-panels`, `rux-tab-panel` | Navigation |
| 35 | Tag | `rux-tag` | Data Display |
| 36 | Textarea | `rux-textarea` | Form Controls |
| 37 | Timeline (beta) | `rux-timeline`, `rux-time-region`, `rux-track`, `rux-ruler` | Layout |
| 38 | Toast (beta) | `rux-toast`, `rux-toast-stack` | Feedback |
| 39 | Tooltip | `rux-tooltip` | Feedback/Overlay |
| 40 | Tree | `rux-tree`, `rux-tree-node` | Navigation |

### Key component APIs (selected detail)

**rux-button** — Properties: `borderless` (bool), `disabled` (bool), `icon` (string), `iconOnly` (bool), `secondary` (bool), `size` (`"small"` | `"medium"` | `"large"`), `type` (`"button"` | `"submit"`). Shadow Parts: `container`, `icon`. Slots: default (label text).

**rux-dialog** — Properties: `clickToClose` (bool), `confirmText` (string, default `'Confirm'`), `denyText` (string, default `'Cancel'`), `header` (string), `message` (string), `open` (bool). Events: `ruxdialogclosed` (detail: bool|null), `ruxdialogopened`. Shadow Parts: `confirm-button`, `container`, `deny-button`, `dialog`, `footer`, `header`, `message`. Slots: default, `header`, `footer`.

**rux-global-status-bar** — Properties: `appDomain`, `appName`, `appState`, `appStateColor` (`"tag1"` | `"tag2"` | `"tag3"` | `"tag4"`), `appVersion`, `includeIcon` (bool), `menuIcon` (string, default `'apps'`), `username`. Slots: default (center content), `left-side`, `app-meta`, `right-side`. Shadow Parts: `app-meta`, `app-state`, `center`, `container`, `middle`, `username`.

**rux-pop-up** — Properties: `closeOnSelect` (bool), `disableAutoUpdate` (bool), `enableAnimationFrame` (bool), `open` (bool), `placement` (12 options + `"auto"`), `strategy` (`"absolute"` | `"fixed"`). Methods: `show()`, `hide()`. Events: `ruxpopupclosed`, `ruxpopupopened`. Shadow Parts: `arrow`, `container`, `popup-content`, `trigger-container`.

**rux-tabs** — Properties: `small` (bool). Sub-components: `rux-tab` (props: `id`, `selected`, `disabled`), `rux-tab-panels`, `rux-tab-panel`. Event: `ruxselected`.

### Event naming convention

All events use the `rux` prefix with no separator: `ruxchange`, `ruxselected`, `ruxdialogclosed`, `ruxdialogopened`, `ruxpopupclosed`, `ruxpopupopened`. React wrappers use `onRux{Event}` pattern.

### CSS Shadow Parts

All components expose Shadow Parts for external styling via `rux-component::part(part-name) { ... }`. Common part names: `container`, `label`, `icon`, `header`, `footer`, `message`.

### Common component states

Default, Hover, Focus, Disabled (40% opacity), Invalid (red border + error text), Read-only.

---

## UX patterns

### The status system — Astro's most critical pattern

The status system uses a **temperature-based severity scale** (cold → hot) mapped to color + unique shape. This is the foundation of the entire design system and the #1 compliance requirement.

| Severity | Color Family | Meaning | Shape |
|---|---|---|---|
| **Off** | Gray | Unavailable, disabled | Unique shape per status |
| **Standby** | Cyan | Available, enabled | Unique shape per status |
| **Normal** | Green | OK, go, satisfactory | Unique shape per status |
| **Caution** | Yellow | Warning, unstable, watch | Unique shape per status |
| **Serious** | Orange | Distress, error, needs attention | Unique shape per status |
| **Critical** | Red | Emergency, alert, urgent | Unique shape per status |

**Mandatory rules**: Status Symbols shall not be altered (required for ADA 508 and WCAG 2.0). Consolidate to highest urgency (if sub-statuses are green/yellow/red, the parent shows red). Reserve red strictly for urgent, immediate-attention states. Never add custom colors to the status palette. Dark theme status colors pass WCAG AA contrast without borders; **light theme requires a darker 1px inner border** because fill colors alone fail WCAG AA on light backgrounds.

### Navigation patterns

Five primary patterns, often combined:

- **List-Detail**: List panel left, detail panel right. For small flat collections.
- **Tab Navigation**: Distinct categories or step-wise workflows. Best when tasks complete within a single tab.
- **Tree Navigation**: Hierarchical single-taxonomy objects. Avoid mixing unrelated types.
- **Table Navigation**: Full-screen tabular view for large uniform datasets with search/sort/filter.
- **Timeline Navigation**: Event-based real-time scheduling. Timeline atop page, details below.

**Global Status Bar** always sits at the top of the application, always uses dark theme styling (even in light-themed apps), and is reserved for truly global elements (app name, state, clock, monitoring icons, emergency controls).

### Table patterns

Columns arranged by importance left-to-right. Left-align general data; right-align dates, times, currency, and numerical data. Column headers match data alignment. **Minimum text size: 14px / 0.875rem (Body 2)**. Sorting via column header click; default ascending first click, toggle on subsequent clicks. Selection via row click or checkboxes for multi-select. AG Grid integration: `@astrouxds/ag-grid-theme` with `ag-theme-astro` (dark) and `ag-theme-astro-light` classes.

### Forms and validation

One-column layout preferred. Labels top-left aligned above fields. Help text 8px below field, secondary color, sentence case. **Inline validation** triggers on focus loss with red border and red bold text replacing help text. **Form-level validation** triggers on submit. Required fields: asterisk (`*`) right of label when most fields are optional. Optional fields: `(optional)` right of label when most fields are required.

**Astro voice**: Direct, confident, commanding. Omit pronouns. Never personify the application. No salutations. Error messages must state: what the problem is, why invalid, how to fix.

### Data visualization patterns

Maximum **11 colors per data set**. Status colors are reserved exclusively for status—never for general data visualization. Eight data-viz colors provided per theme. Chart types supported: pie/donut, line/area, scatter/bubble, histograms, heat maps, Gantt charts, fill gauges.

### Notification patterns

Three types ordered by disruption level: **Log** (least disruptive, recorded in event log), **Banner** (app-level, must not block interactions), **Toast** (temporary, auto-dismisses, stacks vertically newest-at-top, must not cover critical elements). All notifications follow the principle of being timely, relevant, and actionable.

---

## Compliance and standards

### Astro Design Compliance (v4.2.0) — three-tier system

| Tier | Requirements | Scope |
|---|---|---|
| **Tier 1** | Status icons + status colors only | Minimum for operator familiarity |
| **Tier 2** | Tier 1 + Astro colors, typography, visual design patterns | Full visual compliance |
| **Tier 3** | Tier 2 + interaction patterns, behavioral compliance | Complete UX compliance |

Compliance rules span four categories: General (1.0), Design Guidelines (2.0), Patterns (3.0), Components (4.0). Each rule carries a tier designation and uses SHALL/SHALL NOT language.

### MIL-STD-1472H — Section 5.17 (Information Systems)

Astro 7 was formally audited against MIL-STD-1472H Section 5.17 on **September 29, 2022**. Key results:

- **5.17.1.1–5.17.1.4** (Functional interface, personnel compatibility, human performance, display content): **Compliant**
- **5.17.2** (Command dialogs): **Not Applicable** (developer responsibility)
- **5.17.3.1.1** (Drop-down menus): **Compliant**
- **5.17.3.1.2** (Submenus): **Compliant**
- **5.17.3.1.3** (Toolbar): Mostly **Compliant** with two exceptions
- **5.17.3.1.3.5** (Toolbar labels/tooltips): **Non-Compliant**
- **5.17.3.1.3.6** (Non-standard icons): **Non-Compliant**

Most "Not Applicable" items represent developer/application-level responsibilities where Astro provides guidance but cannot enforce compliance. The two non-compliant items relate to toolbar tooltip label requirements for non-standard icons.

### WCAG 2.0/2.1 and Section 508

Astro's colors were specifically overhauled in v7 to meet **WCAG 2.1** contrast guidelines. Dark theme status colors pass **WCAG AA** on dark backgrounds without additional treatment. Light theme status colors fail WCAG AA on light backgrounds—mandatory darker borders were introduced to compensate. Status symbols use **unique shapes per level** for colorblind accessibility, meeting ADA Section 508 requirements. Application State text must meet WCAG AA contrast against its background. The focus state uses **bright pink** (`#da9ce7` dark / `#b534ce` light) specifically chosen to contrast with the blue-dominant Astro palette.

### MIL-STD-2525D

Astro does not directly implement MIL-STD-2525D military tactical symbology. Its six-level status system with combined color + shape serves as the primary symbology for space operations interfaces, designed to align with MIL-STD-2525D's intent for consistent battlefield symbology but adapted for the space domain.

---

## Theming architecture — how dark/light switching works

**Dark theme** is the default. All CSS custom properties resolve to dark-theme values when no class is applied. **Light theme** is activated by adding the `light-theme` class to any wrapping HTML element—this overrides system and component tokens via CSS specificity. The Global Status Bar **always** uses dark theme styling regardless of the application theme.

The token cascade: Reference tokens remain constant across themes. System tokens change between themes (e.g., `--color-text-primary` changes from `#ffffff` to `#292a2d`). Component tokens follow their system token references automatically. AG Grid theming uses `ag-theme-astro` (dark) and `ag-theme-astro-light` (light).

For rebranding as LEECHSEED, the key architectural insight is that **replacing the Reference Token palette** automatically cascades changes through System and Component tokens. The token pipeline (Figma → Token Transformer → Style Dictionary) means a rebrand requires modifying only the source `tokens.json` and regenerating all output formats.

---

## Conclusion

This document captures **every publicly documented specification** of Astro UXDS v7: 15 reference color palettes totaling 100+ hex values, 18 typography styles with exact rem/px/weight/line-height specifications, a 15-step spacing scale, 40+ web components with their properties and shadow parts, 5 navigation patterns, the six-level status system, three-tier compliance framework, and the complete token architecture from reference through system to component levels.

For building the LEECHSEED UX Design System, the most efficient approach is to fork the `@astrouxds/tokens` repository, replace the reference color palette with Bold Venture's brand colors, swap Roboto for a custom typeface, rename the `rux-` component prefix, and regenerate all output formats through Style Dictionary. The three-tier token architecture means **a palette swap at the reference level will automatically cascade** through every system and component token—exactly the kind of systematic rebranding this system was designed to support. The compliance tiers, status system logic, spacing scale, and component APIs can transfer directly to LEECHSEED with only cosmetic changes to naming and color values.