---

## type: ssot_00_foundations category: design_system version: 1.0.0 last_updated: 2026-03-09 applies_to: [OVEREXITOUT, ASTRO7EX, LAKAD, BOLD_VENTURE] status: canonical purpose: Defines the Bold Venture Design System as the mandatory visual and interaction standard for all Bold Venture digital output. Adapted wholesale from the Astro UXDS v7 military-grade design system with Bold Venture naming conventions. dependencies: [] source_system: Astro UXDS v7 (Rocket Communications Inc. / U.S. Space Force) compliance: [MIL-STD-1472H, MIL-STD-2525D, WCAG 2.1 AA]
---
# 📐 ssot_00_bold_venture_design_system

## Table of Contents

1. [Purpose](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#purpose)
2. [Core Methodology](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#core-methodology)
    1. [Design System Architecture](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#design-system-architecture)
    2. [Token Hierarchy](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#token-hierarchy)
    3. [Color System — Reference Palettes](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#color-system-reference-palettes)
    4. [Color System — Semantic Tokens Dark Theme](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#color-system-semantic-tokens-dark-theme)
    5. [Color System — Semantic Tokens Light Theme](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#color-system-semantic-tokens-light-theme)
    6. [Status System](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#status-system)
    7. [Classification Markings](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#classification-markings)
    8. [Data Visualization Palette](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#data-visualization-palette)
    9. [Typography System](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#typography-system)
    10. [Spacing System](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#spacing-system)
    11. [Border Radius and Opacity](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#border-radius-and-opacity)
    12. [Responsive Grid](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#responsive-grid)
    13. [Component Inventory](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#component-inventory)
    14. [Component Token Specifications](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#component-token-specifications)
    15. [UX Patterns](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#ux-patterns)
    16. [Compliance Framework](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#compliance-framework)
    17. [Theming Architecture](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#theming-architecture)
    18. [Naming Convention — Astro to Bold Venture Translation](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#naming-convention)
3. [Implementation](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#implementation)
4. [Examples](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#examples)
5. [Version History](https://claude.ai/chat/cbd60897-8768-4f3b-885b-d07c31f028c1#version-history)

---

## Purpose

This document defines the **Bold Venture Design System** as the mandatory visual and interaction standard for all digital output produced under the Bold Venture umbrella. Every application, dashboard, tool, template renderer, and interactive artifact conforms to this system. The system is adapted wholesale from the **Astro UXDS v7**, a military-grade, open-source design system built by **Rocket Communications Inc.** for the **U.S. Space Force**. Astro UXDS is compliant with **MIL-STD-1472H**, **MIL-STD-2525D**, and **WCAG 2.1 AA**. The Bold Venture Design System inherits all compliance properties, color science, typography specifications, spacing scales, component APIs, and UX patterns from Astro UXDS and rebrands them under Bold Venture naming conventions.

---

## Core Methodology

### Design System Architecture

The Bold Venture Design System operates as a **three-tier token system** with a processing pipeline. The source of truth is a structured token file. That file is processed through a build pipeline that generates output in CSS Custom Properties, SCSS variables, and JSON for consumption by any frontend framework.

The upstream source system (Astro UXDS) uses the following pipeline: Figma design files produce a `tokens.json` source file. That file is processed through **Token Transformer** into structured token sets. Those sets are processed through **Style Dictionary** into distributable output formats (CSS, SCSS, JSON, iOS Swift).

The Bold Venture fork of this pipeline replaces the reference-level palette values with Bold Venture brand colors, replaces the **Roboto** typeface with a Bold Venture typeface selection, and renames the `rux-` component prefix to `bvx-`. All system-level and component-level tokens cascade automatically from the reference-level replacements.

The web component library in the upstream system is built with **Stencil.js** and ships as W3C-compliant Web Components with framework wrappers for React and Angular. The npm packages in the upstream system are `@astrouxds/tokens`, `@astrouxds/astro-web-components`, `@astrouxds/react`, and `@astrouxds/angular`. The Bold Venture equivalents are `@boldventure/tokens`, `@boldventure/web-components`, `@boldventure/react`, and `@boldventure/angular`.

### Token Hierarchy

The token system operates across three tiers. Each tier serves a distinct purpose and audience.

**Tier 1 — Reference Tokens** are raw palette values with no semantic meaning. They define the complete color space, font size scale, spacing scale, and other primitive values. Reference Tokens are accessed via `var(--color-palette-{hue}-{shade})` for colors and `var(--font-size-{scale})` for typography. Reference Tokens do not change between themes.

**Tier 2 — System Tokens** carry semantic intent. They map Reference Tokens to functional roles such as "background color for interactive elements" or "text color for error states." System Tokens are the preferred tier for custom UI development. They are accessed via `var(--color-background-interactive-default)` or `var(--color-text-error)`. System Tokens change between dark and light themes.

**Tier 3 — Component Tokens** are scoped to individual components. They define the specific visual properties of buttons, inputs, tables, and other UI elements. Component Tokens may change across releases and are accessed via `var(--button-color-background-default)` or `var(--table-row-color-background-hover)`. Component Tokens follow their parent System Token references automatically.

The **Token Naming Convention** follows up to nine levels: `[group]-[component]-[element]-[category]-[property]-[concept]-[variant]-[state]-[scale]`. Not all tokens use every level.

### Color System — Reference Palettes

Every hex value below is a **Reference Token** accessed via `var(--color-palette-{hue}-{shade})`. These values do not change between dark and light themes. They represent the complete color space of the design system.

#### Neutral

|Token|Hex|
|---|---|
|`neutral-1000`|`#000000`|
|`neutral-000`|`#ffffff`|
|`neutral-1000a00`|`#00000000`|

#### Dark Blue

|Token|Hex|Token|Hex|
|---|---|---|---|
|`darkblue-100`|`#cbdee9`|`darkblue-600`|`#004872`|
|`darkblue-200`|`#98bdd3`|`darkblue-700`|`#1c3f5e`|
|`darkblue-300`|`#649cbd`|`darkblue-800`|`#1b2d3e`|
|`darkblue-400`|`#2f7aa7`|`darkblue-900`|`#172635`|
|`darkblue-500`|`#005a8f`|`darkblue-950`|`#080c11`|

#### Bright Blue

|Token|Hex|Token|Hex|
|---|---|---|---|
|`brightblue-100`|`#daeeff`|`brightblue-600`|`#3a87cf`|
|`brightblue-200`|`#cee9fc`|`brightblue-700`|`#2b659b`|
|`brightblue-300`|`#b7dcff`|`brightblue-800`|`#1c3851`|
|`brightblue-400`|`#92cbff`|`brightblue-850`|`#142435`|
|`brightblue-500`|`#4dacff`|`brightblue-900`|`#101923`|

#### Grey

|Token|Hex|Token|Hex|
|---|---|---|---|
|`grey-100`|`#f5f6f9`|`grey-500`|`#a4abb6`|
|`grey-200`|`#eaeef4`|`grey-600`|`#7b8089`|
|`grey-250`|`#e0e5eb`|`grey-700`|`#51555b`|
|`grey-300`|`#d4d8dd`|`grey-800`|`#3c3e42`|
|`grey-400`|`#bbc1c9`|`grey-900`|`#292a2d`|

#### Red

|Token|Hex|Token|Hex|
|---|---|---|---|
|`red-400`|`#ff5f60`|`red-700`|`#c8102e`|
|`red-500`|`#ff3838`|`red-800`|`#8b1703`|
|`red-600`|`#ff2a04`|`red-900`|`#661102`|

#### Orange

|Token|Hex|Token|Hex|
|---|---|---|---|
|`orange-400`|`#ffcc57`|`orange-700`|`#ff8c00`|
|`orange-500`|`#ffb302`|`orange-800`|`#975f0e`|
|`orange-600`|`#ffaf3d`|`orange-900`|`#664618`|

#### Yellow

|Token|Hex|Token|Hex|
|---|---|---|---|
|`yellow-400`|`#fded61`|`yellow-700`|`#c7ab00`|
|`yellow-500`|`#fce83a`|`yellow-800`|`#917d01`|
|`yellow-600`|`#fad800`|`yellow-900`|`#645600`|

#### Green

|Token|Hex|Token|Hex|
|---|---|---|---|
|`green-400`|`#99f666`|`green-700`|`#00ad23`|
|`green-500`|`#56f000`|`green-800`|`#007a33`|
|`green-600`|`#00e200`|`green-900`|`#005a00`|

#### Cyan

|Token|Hex|Token|Hex|
|---|---|---|---|
|`cyan-400`|`#5ce2ff`|`cyan-700`|`#20a9d5`|
|`cyan-500`|`#64d9ff`|`cyan-800`|`#35798e`|
|`cyan-600`|`#2dccff`|`cyan-900`|`#285766`|

#### Teal

|Token|Hex|Token|Hex|
|---|---|---|---|
|`teal-100`|`#d0f4f4`|`teal-600`|`#009fa3`|
|`teal-200`|`#a1e9eb`|`teal-700`|`#00777a`|
|`teal-300`|`#70dde0`|`teal-800`|`#035051`|
|`teal-400`|`#3ed2d6`|`teal-900`|`#032828`|
|`teal-500`|`#00c7cb`|||

#### Purple

|Token|Hex|Token|Hex|
|---|---|---|---|
|`purple-100`|`#e4e2f7`|`purple-600`|`#6058a8`|
|`purple-200`|`#c9c5ed`|`purple-700`|`#48417f`|
|`purple-300`|`#aea8e5`|`purple-800`|`#302c54`|
|`purple-400`|`#938bdb`|`purple-900`|`#18152b`|
|`purple-500`|`#786dd3`|||

#### Pink

|Token|Hex|Token|Hex|
|---|---|---|---|
|`pink-100`|`#edcef3`|`pink-600`|`#81009a`|
|`pink-200`|`#da9ce7`|`pink-700`|`#610074`|
|`pink-300`|`#c76ada`|`pink-800`|`#41004d`|
|`pink-400`|`#b534ce`|`pink-900`|`#200227`|
|`pink-500`|`#a200c1`|||

#### Hot Orange

|Token|Hex|Token|Hex|
|---|---|---|---|
|`hotorange-100`|`#f8ddd1`|`hotorange-600`|`#af420a`|
|`hotorange-200`|`#f0baa3`|`hotorange-700`|`#833209`|
|`hotorange-300`|`#ea9875`|`hotorange-800`|`#572108`|
|`hotorange-400`|`#e27545`|`hotorange-900`|`#2b1105`|
|`hotorange-500`|`#da5309`|||

#### Special Single-Shade Hues

|Token|Hex|
|---|---|
|`violet-800`|`#502b85`|
|`blue-800`|`#0033a0`|

### Color System — Semantic Tokens Dark Theme

The **Dark Theme** is the default. All CSS Custom Properties resolve to dark theme values when no theme class is applied. These are **System Tokens** and represent the preferred tier for custom UI development.

#### Background Colors

|CSS Custom Property|Hex|Reference Source|Usage|
|---|---|---|---|
|`--color-background-base-default`|`#101923`|brightblue-900|Application background, popup menus|
|`--color-background-base-header`|`#172635`|darkblue-900|Header of base elements|
|`--color-background-base-hover`|`#142435`|brightblue-850|Base element hover state|
|`--color-background-base-selected`|`#1c3f5e`|darkblue-700|Base element selected state|
|`--color-background-surface-default`|`#1b2d3e`|darkblue-800|Panels, dialogs, cards|
|`--color-background-surface-header`|`#172635`|darkblue-900|Dialog and table headers|
|`--color-background-surface-hover`|`#1c3851`|brightblue-800|Card and table row hover|
|`--color-background-surface-selected`|`#1c3f5e`|darkblue-700|Card and table row selected|
|`--color-background-interactive-default`|`#4dacff`|brightblue-500|Primary interactive background|
|`--color-background-interactive-hover`|`#92cbff`|brightblue-400|Interactive element hover|
|`--color-background-interactive-muted`|`#2b659b`|brightblue-700|Muted interactive background|
|`--color-background-transparent`|`#00000000`|neutral-1000a00|Transparent|

#### Text Colors

|CSS Custom Property|Hex|Reference Source|
|---|---|---|
|`--color-text-primary`|`#ffffff`|neutral-000|
|`--color-text-secondary`|`#d4d8dd`|grey-300|
|`--color-text-placeholder`|`#a4abb6`|grey-500|
|`--color-text-inverse`|`#080c11`|darkblue-950|
|`--color-text-interactive-default`|`#4dacff`|brightblue-500|
|`--color-text-interactive-hover`|`#92cbff`|brightblue-400|
|`--color-text-white`|`#ffffff`|neutral-000|
|`--color-text-black`|`#000000`|neutral-1000|
|`--color-text-error`|`#ff3838`|red-500|

#### Border Colors

|CSS Custom Property|Hex|Reference Source|
|---|---|---|
|`--color-border-interactive-default`|`#4dacff`|brightblue-500|
|`--color-border-interactive-hover`|`#92cbff`|brightblue-400|
|`--color-border-interactive-muted`|`#2b659b`|brightblue-700|
|`--color-border-error`|`#ff3838`|red-500|

#### Focus and Shadow

|Token|Value|
|---|---|
|`--color-border-focus-default`|`#da9ce7` (pink-200)|
|`--border-width-focus-default`|`1px`|
|`--spacing-focus-default`|`0.125rem` (2px)|
|`--shadow-overlay`|`0px 4px 4px 1px rgba(0, 0, 0, 0.45)`|
|`--opacity-disabled`|`40%`|

### Color System — Semantic Tokens Light Theme

The **Light Theme** is activated by adding the `.light-theme` CSS class to any wrapping HTML element. The same CSS Custom Property names resolve to different values.

#### Background Colors (Light)

|CSS Custom Property|Hex|Reference Source|
|---|---|---|
|`--color-background-base-default`|`#eaeef4`|grey-200|
|`--color-background-base-header`|`#f5f6f9`|grey-100|
|`--color-background-base-hover`|`#98bdd3`|darkblue-200|
|`--color-background-base-selected`|`#cee9fc`|brightblue-200|
|`--color-background-surface-default`|`#ffffff`|neutral-000|
|`--color-background-surface-header`|`#f5f6f9`|grey-100|
|`--color-background-surface-hover`|`#daeeff`|brightblue-100|
|`--color-background-surface-selected`|`#cee9fc`|brightblue-200|
|`--color-background-interactive-default`|`#005a8f`|darkblue-500|
|`--color-background-interactive-hover`|`#1c3f5e`|darkblue-700|
|`--color-background-interactive-muted`|`#2f7aa7`|darkblue-400|

#### Text Colors (Light)

|CSS Custom Property|Hex|Reference Source|
|---|---|---|
|`--color-text-primary`|`#292a2d`|grey-900|
|`--color-text-secondary`|`#51555b`|grey-700|
|`--color-text-placeholder`|`#7b8089`|grey-600|
|`--color-text-inverse`|`#ffffff`|neutral-000|
|`--color-text-interactive-default`|`#005a8f`|darkblue-500|
|`--color-text-interactive-hover`|`#1c3f5e`|darkblue-700|
|`--color-text-error`|`#c8102e`|red-700|

#### Border Colors (Light)

|CSS Custom Property|Hex|
|---|---|
|`--color-border-interactive-default`|`#005a8f`|
|`--color-border-interactive-hover`|`#1c3f5e`|
|`--color-border-interactive-muted`|`#2f7aa7`|
|`--color-border-error`|`#c8102e`|

#### Focus and Shadow (Light)

|Token|Value|
|---|---|
|`--color-border-focus-default`|`#b534ce` (pink-400)|
|`--shadow-overlay`|`0px 4px 4px 1px rgba(0, 0, 0, 0.35)`|

### Status System

The **Status System** is the most critical pattern in the design system. It uses a **Temperature-Based Severity Scale** mapped to color and unique shape. Color alone does not communicate status. Every status level carries a distinct shape to ensure accessibility for color-blind operators.

#### Status Levels

|Severity|Color Family|Meaning|Temperature|
|---|---|---|---|
|**Off**|Grey|Unavailable, disabled|Cold|
|**Standby**|Cyan|Available, enabled, idle|Cool|
|**Normal**|Green|Operational, satisfactory|Neutral|
|**Caution**|Yellow|Warning, unstable, requires monitoring|Warm|
|**Serious**|Orange|Distress, error, requires attention|Hot|
|**Critical**|Red|Emergency, alert, requires immediate action|Maximum|

#### Status Colors — Dark Theme

|Status|Hex|RGB|CSS Custom Property|
|---|---|---|---|
|Critical|`#ff3838`|255, 56, 56|`--color-status-critical`|
|Serious|`#ffb302`|255, 179, 2|`--color-status-serious`|
|Caution|`#fce83a`|252, 232, 58|`--color-status-caution`|
|Normal|`#56f000`|86, 240, 0|`--color-status-normal`|
|Standby|`#2dccff`|45, 204, 255|`--color-status-standby`|
|Off|`#a4abb6`|164, 171, 182|`--color-status-off`|

Dark theme status colors pass **WCAG AA** contrast on dark backgrounds without borders.

#### Status Colors — Light Theme (Fill and Required Border)

|Status|Fill Hex|Border Hex|Fill Token|Border Token|
|---|---|---|---|---|
|Critical|`#ff2a04`|`#661102`|`--status-symbol-color-fill-critical`|`--status-symbol-color-border-critical`|
|Serious|`#ffaf3d`|`#664618`|`--status-symbol-color-fill-serious`|`--status-symbol-color-border-serious`|
|Caution|`#fad800`|`#645600`|`--status-symbol-color-fill-caution`|`--status-symbol-color-border-caution`|
|Normal|`#00e200`|`#005a00`|`--status-symbol-color-fill-normal`|`--status-symbol-color-border-normal`|
|Standby|`#64d9ff`|`#285766`|`--status-symbol-color-fill-standby`|`--status-symbol-color-border-standby`|
|Off|`#7b8089`|`#3c3e42`|`--status-symbol-color-fill-off`|`--status-symbol-color-border-off`|

Light theme status fills do not pass WCAG AA on light backgrounds alone. The darker border is mandatory.

#### Status System Rules

1. Status Symbols shall not be altered. They are required for ADA Section 508 and WCAG 2.0 compliance.
2. Consolidate to the highest urgency level. If sub-statuses are green, yellow, and red, the parent indicator displays red.
3. Reserve red strictly for urgent, immediate-attention states. Overuse of red degrades operator response.
4. Do not add custom colors to the status palette. Additional colors reduce the operator's ability to learn the system.

### Classification Markings

**Classification Marking Colors** are identical across both themes.

|Level|Hex|RGB|Font Color|
|---|---|---|---|
|Top Secret//SCI|`#fce83a`|252, 232, 58|Black|
|Top Secret|`#ff8c00`|255, 140, 0|Black|
|Secret|`#c8102e`|200, 16, 46|White|
|Confidential|`#0033a0`|0, 51, 160|White|
|CUI|`#502b85`|80, 43, 133|White|
|Unclassified|`#007a33`|0, 122, 51|White|

CSS tokens follow the pattern `--color-classification-{level}`. Banner component tokens follow `--classification-banner-color-background-{level}`.

### Data Visualization Palette

A maximum of **11 colors per data set** is permitted. Status colors are reserved exclusively for status indication and shall never be used for general data visualization.

#### Dark Theme Data Visualization

|Token|Hex|Reference Source|
|---|---|---|
|`--color-data-visualization-1`|`#00c7cb`|teal-500|
|`--color-data-visualization-2`|`#938bdb`|purple-400|
|`--color-data-visualization-3`|`#4dacff`|brightblue-500|
|`--color-data-visualization-4`|`#70dde0`|teal-300|
|`--color-data-visualization-5`|`#c9c5ed`|purple-200|
|`--color-data-visualization-6`|`#92cbff`|brightblue-400|
|`--color-data-visualization-7`|`#a1e9eb`|teal-200|
|`--color-data-visualization-8`|`#b7dcff`|brightblue-300|

#### Light Theme Data Visualization

|Token|Hex|Reference Source|
|---|---|---|
|`--color-data-visualization-1`|`#035051`|teal-800|
|`--color-data-visualization-2`|`#6058a8`|purple-600|
|`--color-data-visualization-3`|`#1c3851`|brightblue-800|
|`--color-data-visualization-4`|`#00777a`|teal-700|
|`--color-data-visualization-5`|`#786dd3`|purple-500|
|`--color-data-visualization-6`|`#2b659b`|brightblue-700|
|`--color-data-visualization-7`|`#009fa3`|teal-600|
|`--color-data-visualization-8`|`#3a87cf`|brightblue-600|

### Typography System

The upstream system uses **Roboto** as the sole typeface across all styles. The Bold Venture fork retains this default until a custom typeface selection is made.

#### Font Family

```
--font-family-sans: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI',
  Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif;
```

#### Font Size Scale

|Token|CSS Custom Property|rem|px|
|---|---|---|---|
|`font-size-xs`|`var(--font-size-xs)`|0.75|12|
|`font-size-sm`|`var(--font-size-sm)`|0.875|14|
|`font-size-base`|`var(--font-size-base)`|1|16|
|`font-size-lg`|`var(--font-size-lg)`|1.125|18|
|`font-size-xl`|`var(--font-size-xl)`|1.25|20|
|`font-size-2xl`|`var(--font-size-2xl)`|1.5|24|
|`font-size-3xl`|`var(--font-size-3xl)`|1.75|28|
|`font-size-4xl`|`var(--font-size-4xl)`|2.125|34|
|`font-size-5xl`|`var(--font-size-5xl)`|3|48|
|`font-size-6xl`|`var(--font-size-6xl)`|3.75|60|

#### Font Weights

|Token|Value|
|---|---|
|`--font-weight-light`|300|
|`--font-weight-regular`|400|
|`--font-weight-medium`|500|
|`--font-weight-bold`|700|

#### Line Height Scale

|Token|rem|px|
|---|---|---|
|`--line-height-2xs`|0.875|14|
|`--line-height-xs`|1|16|
|`--line-height-sm`|1.25|20|
|`--line-height-base`|1.5|24|
|`--line-height-lg`|1.75|28|
|`--line-height-xl`|2|32|
|`--line-height-2xl`|2.5|40|
|`--line-height-3xl`|3.5|56|
|`--line-height-4xl`|4.375|70|

#### Letter Spacing Scale

|Token|Value|
|---|---|
|`--letter-spacing-sm`|-0.005em|
|`--letter-spacing-base`|0em|
|`--letter-spacing-lg`|0.0015em|
|`--letter-spacing-xl`|0.0025em|
|`--letter-spacing-2xl`|0.005em|

#### Complete Typography Styles

Each style produces five CSS Custom Properties following the pattern `--font-{id}-{property}`.

|Style|CSS Class|Size (rem / px)|Weight|Line Height|Letter Spacing|
|---|---|---|---|---|---|
|Display 1|`.bvx-display-1`|3.75 / 60|300 Light|1.167|-0.005em|
|Display 2|`.bvx-display-2`|3 / 48|400 Regular|1.167|0em|
|Heading 1|`.bvx-heading-1`|2.125 / 34|400 Regular|1.176|0.0025em|
|Heading 1 Bold|`.bvx-heading-1-bold`|2.125 / 34|700 Bold|1.176|0.0025em|
|Heading 2|`.bvx-heading-2`|1.5 / 24|400 Regular|1.167|0em|
|Heading 3|`.bvx-heading-3`|1.25 / 20|500 Medium|1.2|0.0015em|
|Heading 4|`.bvx-heading-4`|1.25 / 20|300 Light|1.2|0.0015em|
|Heading 5|`.bvx-heading-5`|1.125 / 18|400 Regular|1.333|0em|
|Heading 6|`.bvx-heading-6`|1.125 / 18|300 Light|1.333|0em|
|Body 1|`.bvx-body-1`|1 / 16|400 Regular|1.5|0.005em|
|Body 1 Bold|`.bvx-body-1-bold`|1 / 16|700 Bold|1.5|0.005em|
|Body 2|`.bvx-body-2`|0.875 / 14|400 Regular|1.429|0.005em|
|Body 2 Bold|`.bvx-body-2-bold`|0.875 / 14|700 Bold|1.429|0.005em|
|Body 3|`.bvx-body-3`|0.75 / 12|400 Regular|1.333|0.005em|
|Body 3 Bold|`.bvx-body-3-bold`|0.75 / 12|700 Bold|1.333|0.005em|
|Control Body 1|`.bvx-control-body-1`|1 / 16|400 Regular|1.25|0.005em|
|Control Body 1 Bold|`.bvx-control-body-1-bold`|1 / 16|700 Bold|1.25|0.005em|
|Monospace 1|`.bvx-monospace-1`|1.75 / 28|500 Medium|1.143|0em|

**Minimum text size for data-dense displays is 14px (0.875rem, Body 2).** Text below this threshold degrades readability under sustained operational use.

### Spacing System

The spacing system is built on a **4px base grid**. The token number multiplied by 4 produces the pixel value. Exceptions exist at the sub-grid level for fine adjustments.

|Token|CSS Custom Property|rem|px|
|---|---|---|---|
|`spacing-0`|`var(--spacing-0)`|0|0|
|`spacing-025`|`var(--spacing-025)`|0.0625|1|
|`spacing-050`|`var(--spacing-050)`|0.125|2|
|`spacing-1`|`var(--spacing-1)`|0.25|4|
|`spacing-2`|`var(--spacing-2)`|0.5|8|
|`spacing-3`|`var(--spacing-3)`|0.75|12|
|`spacing-4`|`var(--spacing-4)`|1|16|
|`spacing-6`|`var(--spacing-6)`|1.5|24|
|`spacing-8`|`var(--spacing-8)`|2|32|
|`spacing-10`|`var(--spacing-10)`|2.5|40|
|`spacing-12`|`var(--spacing-12)`|3|48|
|`spacing-14`|`var(--spacing-14)`|3.5|56|
|`spacing-16`|`var(--spacing-16)`|4|64|
|`spacing-20`|`var(--spacing-20)`|5|80|
|`spacing-24`|`var(--spacing-24)`|6|96|

### Border Radius and Opacity

|Token|Value|
|---|---|
|`--border-width-none`|0|
|`--border-width-xs`|1px|
|`--border-width-sm`|2px|
|`--border-width-lg`|4px|
|`--radius-base`|3px|
|`--radius-circle`|50%|
|`--opacity-0`|0%|
|`--opacity-25`|25%|
|`--opacity-35`|35%|
|`--opacity-40`|40%|
|`--opacity-45`|45%|
|`--opacity-50`|50%|

### Responsive Grid

|Breakpoint|Columns|Margin|Gap Default|Gap Compact|
|---|---|---|---|---|
|0 to 360px|4|16px|16px|8px|
|361 to 768px|8|24px|24px|12px|
|769 to 1920px|12|24px|24px|12px|
|1921 to 3840px|12|48px|48px|24px|

### Component Inventory

The design system ships 40 components as W3C Web Components. All tag names use the `bvx-` prefix (upstream: `rux-`).

|Number|Component|Tag|Category|
|---|---|---|---|
|1|Accordion|`bvx-accordion`|Layout|
|2|Breadcrumb|`bvx-breadcrumb`|Navigation|
|3|Button|`bvx-button`|Actions|
|4|Card|`bvx-card`|Layout|
|5|Checkbox|`bvx-checkbox`|Form Controls|
|6|Classification Marking|`bvx-classification-marking`|Data Display|
|7|Clock|`bvx-clock`|Data Display|
|8|Container|`bvx-container`|Layout|
|9|Date Picker|`bvx-datetime`|Form Controls|
|10|Dialog|`bvx-dialog`|Feedback|
|11|Global Status Bar|`bvx-global-status-bar`|Navigation|
|12|Icon|`bvx-icon`|Data Display|
|13|Indeterminate Progress|`bvx-indeterminate-progress`|Feedback|
|14|Input Field|`bvx-input`|Form Controls|
|15|Log|`bvx-log`|Data Display|
|16|Menu|`bvx-menu`|Actions|
|17|Monitoring Icon|`bvx-monitoring-icon`|Data Display|
|18|Monitoring Progress Icon|`bvx-monitoring-progress-icon`|Data Display|
|19|Notification Banner|`bvx-notification`|Feedback|
|20|Pagination|`bvx-pagination`|Navigation|
|21|Pop Up|`bvx-pop-up`|Actions|
|22|Progress|`bvx-progress`|Feedback|
|23|Push Button|`bvx-push-button`|Actions|
|24|Radio Button|`bvx-radio`|Form Controls|
|25|Search|`bvx-input` (variant)|Form Controls|
|26|Segmented Button|`bvx-segmented-button`|Actions|
|27|Select|`bvx-select`|Form Controls|
|28|Slider|`bvx-slider`|Form Controls|
|29|Status Symbol|`bvx-status`|Data Display|
|30|Switch|`bvx-switch`|Form Controls|
|31|Table|`bvx-table`|Data Display|
|32|Tabs|`bvx-tabs`|Navigation|
|33|Tag|`bvx-tag`|Data Display|
|34|Textarea|`bvx-textarea`|Form Controls|
|35|Timeline|`bvx-timeline`|Layout|
|36|Toast|`bvx-toast`|Feedback|
|37|Tooltip|`bvx-tooltip`|Feedback|
|38|Tree|`bvx-tree`|Navigation|
|39|Application State|(pattern within GSB)|Navigation|
|40|Link|(native anchor styled via CSS)|Navigation|

### Component Token Specifications

#### Button

|Token|Value|
|---|---|
|`--button-color-background-default`|`#4dacff`|
|`--button-color-background-hover`|`#92cbff`|
|`--button-color-background-secondary`|`#00000000`|
|`--button-color-text-default`|`#080c11`|
|`--button-color-text-secondary-default`|`#4dacff`|
|`--button-border-width`|1px|
|`--button-radius`|3px|
|`--button-padding-x-large`|1rem|
|`--button-padding-x-medium`|1rem|
|`--button-padding-x-small`|1rem|
|`--button-padding-y-large`|0.75rem|
|`--button-padding-y-medium`|0.5rem|
|`--button-padding-y-small`|0.25rem|

#### Input

|Token|Value|
|---|---|
|`--input-color-background`|`#101923`|
|`--input-color-border-default`|`#2b659b`|
|`--input-color-border-hover`|`#92cbff`|
|`--input-color-border-invalid`|`#ff3838`|
|`--input-color-text`|`#ffffff`|
|`--input-color-placeholder`|`#a4abb6`|
|`--input-radius`|3px|
|`--input-border-width`|1px|

#### Table

|Token|Value|
|---|---|
|`--table-header-color-background`|`#172635`|
|`--table-header-shadow`|`0px 4px 8px 0px rgba(0,0,0,0.45)`|
|`--table-row-color-background-default`|`#1b2d3e`|
|`--table-row-color-background-selected`|`#1c3f5e`|
|`--table-row-color-background-hover`|`#1c3851`|
|`--table-row-color-text`|`#ffffff`|
|`--table-row-color-border`|`#101923`|

#### Global Status Bar

|Token|Value|
|---|---|
|`--global-status-bar-color-background`|`#172635`|
|`--global-status-bar-color-text`|`#ffffff`|
|`--global-status-bar-icon-color-default`|`#4dacff`|
|`--global-status-bar-icon-color-hover`|`#92cbff`|

#### Tab

|Token|Value|
|---|---|
|`--tab-color-text-default`|`#4dacff`|
|`--tab-color-text-hover`|`#92cbff`|
|`--tab-color-text-selected`|`#ffffff`|
|`--tab-border-color-selected`|`#4dacff`|
|`--tab-border-width-bottom`|4px|

#### Additional Components

|Component|Key Tokens|
|---|---|
|Card|`--card-color-border: #51555b`, `--card-color-background: #101923`, `--card-radius: 3px`|
|Notification|`--notification-banner-color-background: #101923`, `--notification-banner-radius-outer: 3px`|
|Tooltip|`--tooltip-color-background: #3c3e42`, `--tooltip-color-text: #ffffff`, `--tooltip-radius: 1px`|
|Progress|`--progress-color-background: #1b2d3e`, `--progress-color-inner: #4dacff`, `--progress-radius-inner: 8px`|
|Tag|`--tag-radius: 4px`, `--tag-color-text: #ffffff`|

### UX Patterns

#### Status Pattern

The **Status Pattern** is the single most important pattern in the system. It governs all status indication across every application. The six-level temperature scale (Off through Critical) is mandatory. Status colors shall not be used for any purpose other than status indication. Status Symbols combine color and shape to ensure colorblind accessibility.

#### Navigation Patterns

Five primary navigation patterns exist. They may be combined.

**List-Detail** places a list panel on the left and a detail panel on the right. It is appropriate for small, flat collections.

**Tab Navigation** separates distinct categories or step-wise workflows. It is appropriate when tasks complete within a single tab.

**Tree Navigation** handles hierarchical single-taxonomy objects. Mixing unrelated types within a single tree is prohibited.

**Table Navigation** provides a full-screen tabular view for large uniform datasets with search, sort, and filter.

**Timeline Navigation** handles event-based real-time scheduling. The timeline sits at the top of the page with details below.

The **Global Status Bar** always occupies the top of the application. It always uses dark theme styling regardless of the application theme. It is reserved for truly global elements: application name, state, clock, monitoring icons, and emergency controls.

#### Table Pattern

Columns are arranged by importance from left to right. General data is left-aligned. Dates, times, currency, and numerical data are right-aligned. Column headers match their data alignment. Minimum text size within tables is 14px (Body 2). Sorting activates via column header click. The first click sorts ascending. Subsequent clicks toggle direction.

#### Form Pattern

One-column layout is preferred. Labels are top-left aligned above fields. Help text appears 8px below the field in secondary text color using sentence case. **Inline Validation** triggers on focus loss. The field border turns red and red bold text replaces the help text. **Form-Level Validation** triggers on submit.

Required fields display an asterisk right of the label when most fields are optional. Optional fields display "(optional)" right of the label when most fields are required.

#### Notification Pattern

Three notification types exist, ordered by disruption level. **Log** is the least disruptive and is recorded in an event log. **Banner** is application-level and shall not block interactions. **Toast** is temporary, auto-dismisses, stacks vertically with newest at top, and shall not cover critical elements.

#### Voice Guidelines

Application text is direct, confident, and commanding. Pronouns are omitted. The application is never personified. No salutations are used. Error messages must state: what the problem is, why the input is invalid, and how to fix it.

### Compliance Framework

The upstream Astro UXDS defines a **Three-Tier Compliance System** for measuring application adherence.

|Tier|Requirements|Scope|
|---|---|---|
|Tier 1|Status icons and status colors only|Minimum for operator familiarity|
|Tier 2|Tier 1 plus Astro colors, typography, and visual design patterns|Full visual compliance|
|Tier 3|Tier 2 plus interaction patterns and behavioral compliance|Complete UX compliance|

The Bold Venture Design System targets **Tier 3** for all character system tooling and **Tier 2** minimum for all other digital output.

#### MIL-STD-1472H Compliance

The upstream system was formally audited against **MIL-STD-1472H Section 5.17** (Information Systems) on September 29, 2022. The audit found compliance across functional interface, personnel compatibility, human performance, display content, drop-down menus, and submenus. Two non-compliant items were identified in toolbar tooltip label requirements for non-standard icons.

#### WCAG 2.1 AA Compliance

The color system was overhauled in Astro v7 specifically to meet **WCAG 2.1 AA** contrast guidelines. Dark theme status colors pass WCAG AA on dark backgrounds without additional treatment. Light theme status colors require mandatory darker borders because fill colors alone fail WCAG AA on light backgrounds. The focus state uses bright pink specifically chosen to contrast against the blue-dominant palette.

### Theming Architecture

The **Dark Theme** is the default for all Bold Venture applications. All CSS Custom Properties resolve to dark theme values when no theme class is applied.

The **Light Theme** is activated by adding the `.light-theme` CSS class to any wrapping HTML element. This class overrides System Tokens and Component Tokens via CSS specificity. Reference Tokens remain constant across themes.

The **Global Status Bar** always uses dark theme styling regardless of the application theme.

The token cascade operates as follows: Reference Tokens remain constant. System Tokens change between themes. Component Tokens follow their parent System Token references automatically.

For rebranding, replacing the Reference Token palette automatically cascades changes through all System and Component Tokens. The token pipeline processes the source file through Style Dictionary and regenerates all output formats.

### Naming Convention — Astro to Bold Venture Translation

|Astro UXDS|Bold Venture|
|---|---|
|`rux-` (component prefix)|`bvx-`|
|`.rux-` (CSS class prefix)|`.bvx-`|
|`@astrouxds/tokens`|`@boldventure/tokens`|
|`@astrouxds/astro-web-components`|`@boldventure/web-components`|
|`@astrouxds/react`|`@boldventure/react`|
|`@astrouxds/angular`|`@boldventure/angular`|
|`ruxchange` (event prefix)|`bvxchange`|
|`onRux{Event}` (React wrapper)|`onBvx{Event}`|
|Astro UXDS|Bold Venture Design System|
|Rocket Communications Inc.|Bold Venture X|

All CSS Custom Property names for tokens (colors, spacing, typography, borders) remain unchanged. Only component-scoped names that include the `rux` prefix are translated to `bvx`.

---

## Implementation

### Adopting the Design System for a New Application

1. Install the token package: `npm install @boldventure/tokens`.
2. Import the CSS into the application entry point: `import '@boldventure/tokens/dist/css/index.css'`.
3. The dark theme activates automatically. No additional class is required.
4. To activate light theme on any element, add the `.light-theme` class to the wrapping container.
5. Reference System Tokens for all color, spacing, and typography decisions. Do not reference Reference Tokens directly unless building custom reference-level extensions.
6. Install the component library if using Web Components: `npm install @boldventure/web-components`.
7. For React applications: `npm install @boldventure/react`.

### Applying the Status System

1. Identify the severity level of the condition being displayed.
2. Use the corresponding status color and status symbol from the Status System section.
3. Do not use status colors for any non-status purpose.
4. If multiple sub-statuses exist, consolidate to the highest urgency level.
5. On light theme backgrounds, include the mandatory darker border for all status symbols.

### Building a Custom Component

1. Use System Tokens for all visual properties (background, text, border).
2. If the component requires states (default, hover, focus, disabled, invalid), map each state to the corresponding System Token variant.
3. Apply `--opacity-disabled` (40%) for disabled states.
4. Apply `--color-border-focus-default` for focus rings.
5. Apply `--color-border-error` and `--color-text-error` for invalid states.
6. Register the component in the Bold Venture component inventory with the `bvx-` prefix.

### Extending the Color System

1. New colors are added only at the Reference Token level.
2. New Reference Tokens follow the naming pattern `--color-palette-{hue}-{shade}`.
3. New colors shall not conflict with existing status colors.
4. New colors require System Token mappings before they may be used in UI.
5. All new colors must pass WCAG AA contrast testing against both dark and light theme backgrounds.

---

## Examples

### Example 1: System Explorer Application

The **System Explorer** (Phase 3 deliverable of the character systems pipeline) applies the Bold Venture Design System as follows. The application background uses `--color-background-base-default` (#101923). The navigation tabs use `--tab-color-text-default` (#4dacff) for default state and `--tab-color-text-selected` (#ffffff) for the active tab with a 4px bottom border in `--tab-border-color-selected` (#4dacff). Layer cards use `--color-background-surface-default` (#1b2d3e) with `--color-background-surface-hover` (#1c3851) on hover. Status flags use the temperature-based status colors: ACTIVE flags display in `--color-status-critical` (#ff3838), PENDING flags display in `--color-status-serious` (#ffb302), FIRED_PRE_STORY flags display in `--color-status-off` (#a4abb6). Derived statistics that exceed their expected range (Truth Exposure Index exceeding 60) display in `--color-status-serious` (#ffb302) with a caution indicator. Derived statistics that go negative (Stress Threshold below zero) display in `--color-status-critical` (#ff3838) with a critical indicator.

### Example 2: Character Database Editor Application

The **Database Editor** (Phase 4 deliverable) applies the Bold Venture Design System to a read-write interface. In browse mode, all fields render as read-only text using `--color-text-primary` (#ffffff) on `--color-background-surface-default` (#1b2d3e). The mode toggle button uses the secondary button style with `--button-color-text-secondary-default` (#4dacff). When the operator switches to edit mode, input fields activate with `--input-color-background` (#101923) and `--input-color-border-default` (#2b659b). A persistent indicator in the **Global Status Bar** changes to `--color-status-caution` (#fce83a) to signal that the application is in an editable state. Form validation follows the inline validation pattern: fields that violate scale class constraints (such as an odd number entered for a variable that requires even values) display `--input-color-border-invalid` (#ff3838) with red error text stating the constraint and the nearest valid value. The point budget tracker in the bottom panel uses `--progress-color-inner` (#4dacff) for the budget utilization bar and shifts to `--color-status-serious` (#ffb302) when utilization exceeds 90%.

---

## Version History

|Version|Date|Changes|
|---|---|---|
|1.0.0|2026-03-09|Initial Bold Venture Design System SSOT. Wholesale adaptation of Astro UXDS v7. Complete reference palettes (15 hues, 100+ hex values), dark and light theme semantic tokens, six-level status system, classification markings, data visualization palettes, 18 typography styles, 15-step spacing scale, 40-component inventory, component token specifications, 5 navigation patterns, 3 notification types, three-tier compliance framework, theming architecture, and Astro-to-Bold-Venture naming translation.|