---
title: "Bold Venture Design System: reference"
type: reference
for: "a builder or designer looking up a token, color, component, status rule, or pattern in the design system"
does: "lists every component of the Bold Venture Design System"
owner: Chief
state: draft
reviewed: 2026-10-05
source: ShroomsQ/_CANON/_SSOT/05_OPERATIONS/📐 ssot_00_bold_venture_design_system.md
source_version: 2.0.2
---

**Who it's for:** a builder or designer. They look up a token, color, component, status rule, or pattern in the design system · **What it does:** lists every component of the Bold Venture Design System · **Type:** reference

# Bold Venture Design System: reference

The source has type `ssot_00_foundations`, category design_system, version 2.0.1, tier operations, trunk ORANGE, last updated 2026-10-04. It applies to BOLD_VENTURE. Status: canonical. Source system: Astro UXDS v7 (Rocket Communications Inc. / U.S. Space Force). Compliance: MIL-STD-1472H, MIL-STD-2525D, WCAG 2.1 AA. Dependencies: none.

The purpose line calls it a Command-wide base tool, not part of the storytelling stack. It calls it the mandatory visual and interaction standard for all Bold Venture digital output. The system adapts Astro UXDS v7 wholesale, with Bold Venture naming.


## THE BOLD VENTURE ROSTER — the brand color layer (RULED 2026-09-01)

The doctrine: one identity, four registers, every surface assigned. It is a total identity system across the gamut of the brand: labels, packaging, uniforms, signage, interiors, UI, content. It applies the Disney principle from the lexicon doctrine (SOP §6) to color: one castle, many lands.

### Layer 0 · THE IDENTITY — present on every surface, every hour

| Family | Tokens (reference: `--color-palette-{hue}-{shade}`) |
|---|---|
| **ROSE** (the anchor) | 100 `#F7D9E2` · 200 `#EFB3C6` · 300 `#E38AA6` · 400 `#D06184` · 500 `#B03A5B` (wet) · 600 `#9C2B4F` · **700 `#8A1F44` (BASE)** · 800 `#6E1C36` · 900 `#55112B` (bruise) · 950 `#2B0815` |
| **ROSE tint ladder** (Berry Rose Pop donation, the social/pop light end) | blush `#FFD7E3` · pink `#FF8FB1` · raspberry `#E34D7C` |
| **FLESH** | 100 `#FFF3EC` · 200 `#FFE7DA` · 300 `#FFDAC6` (light) · 400 `#FFD1BD` · **500 `#FFC8B5` (BASE)** · 600 `#EBAA9A` · 700 `#D68D8D` (flush) · 800 `#BF6B77` · 900 `#8F4A55` |
| **GROUNDS** (rose-cast blacks) | 800 `#241018` · 900 `#140A0E` · 950 `#0E0307` · maroon `#3F0D12` (Noir Garnet donation) |
| **GOLD** (core accent, ruled in via Ember) | deep `#D97706` · light `#FDE68A` |
| **Neutrals** | pure `#FFFFFF` / `#000000` free agents; the Astro grey ramp survives for chrome and disabled only |

**The adhesive rule:** every surface in every register carries at least one identity element. The element can be the mark in rose, a rose-black ground, or a flesh moment. **The rose quota (panel-ratified):** a rose-family hue holds a top-two role on every branded surface, in every register.

### The four registers

| Register | Lineage | Palette | Home surfaces | The law |
|---|---|---|---|---|
| **EMBER** | Autumn Kiss (absorbs Sunset Romance's dusk end: salmon `#FB7185`, amber `#F59E0B`) | deep amber `#D97706` · gold `#FDE68A` · russet `#9A3412` · grounds from the rose-blacks | interiors, signage, labels, packaging, wardrobe base: the all-hours ambient (honey light by day, candlelight by night) | Warmth arrives as LIGHT, never as pigment on skin (see the Luminance Law) |
| **PUNCH** | Tropical Punch | punch `#FF2D55` · coral `#FB7185` · citrus `#F97316` · yellow `#FACC15` · teal `#052E2B` (legal only inside Punch artboards, as water/depth) | drops, events, promos, social bursts, motion, summer sets: the live edge | An energy state, never the resting state. It detonates and recedes. It is barred from UI status surfaces (punch sits too near alarm red). Yellow fails the Luminance Law on skin, so it serves props, type, and light only. |
| **DUST** | Dusty Drama | blush `#E5B8C2` · lavender `#C4B5FD` · cool greys `#4B5563`/`#F3F4F6` · white | light-theme UI, documents, lookbooks, editorial, daytime rooms: the daylight | Greys serve surfaces and type only. Skin is never grayed, and dusty pink never touches skin. Lavender is capped at accent so violet never rivals rose. |
| **NOIR** | the rose's own deep end (Noir Garnet and Satin Berry donations) | garnet `#B11226` · maroon `#3F0D12` · bright berry `#D10F3A` · salmon `#FCA5A5` (the flesh bridge) · silver small-type `#CBD5E1` | dark UI (the default), premium packaging, the nightlife end. The Cabaret guest pair (`#FF1B6B` / `#6D28D9`) visits here only. | The luxury register; silver for small and regulatory type on the darkest grounds |

### THE LUMINANCE LAW (panel-derived, measurable — supersedes the vibe-rule)

Warm color **flatters** skin when it outshines the brightest flesh token. Gold `#FDE68A` (L about 92) above flesh-300 `#FFDAC6` (L about 91) reads as key light. Warm color **jaundices** when it sinks below flesh luminance inside the skin's hue band. Yellow `#FACC15` (L about 86) reads as stain. Therefore ambers and golds are legal in only two cases. (a) They sit above flesh luminance. (b) They appear as small source-motivated accents on dark grounds (candle, lamp, foil). They are never a midtone fill near skin. Skin always keeps the FLESH ramp with rose shadows. Warmth is applied as a photographic grade over the scene, never by re-tokenizing skin.

### The one-red ledger

The system holds one deep red family. Campaign reds resolve inward. `#E11D48` (Kiss/Sunset) is a campaign accent that defers to ROSE on anything mark-adjacent. `#B91C1C` (Dust) snaps to garnet `#B11226`. Alarm red `#FF3838` remains the status system's alone. Alarm stays bright and orange-leaning, brand rose stays deep and blue-leaning, and the two never trade lightness.

### Semantic token remap — dark theme (the Noir default)

| Token | v1 (Astro) | v2 (Roster) |
|---|---|---|
| `--color-background-base-default` | `#101923` | `#140A0E` (ground-900) |
| `--color-background-base-header` | `#172635` | `#0E0307` (ground-950) |
| `--color-background-surface-default` | `#1b2d3e` | `#241018` (ground-800) |
| `--color-background-surface-hover` | `#1c3851` | `#341820` (ground-700, new) |
| `--color-background-surface-selected` | `#1c3f5e` | `#55112B` (rose-900) |
| `--color-background-interactive-default` | `#4dacff` | `#B03A5B` (rose-500) |
| `--color-background-interactive-hover` | `#92cbff` | `#D06184` (rose-400) |
| `--color-text-primary` | `#ffffff` | `#F5EDE9` (flesh-cast ink) |
| `--color-text-interactive-default` | `#4dacff` | `#E38AA6` (rose-300) |
| `--color-border-focus-default` | `#da9ce7` | `#FDE68A` (gold, contrasts the rose field) |
| Status tokens | unchanged | unchanged, sacred |

The light theme is the DUST register. Its base is `#F3F4F6`, its surface `#FFFFFF`, and interactive rose-700 `#8A1F44`. Its text is `#1F1B1E`, selected blush `#E5B8C2`, and focus violet `#6D28D9`. Status light-theme fills and mandatory borders are unchanged.

### The surface map

- Labels and packaging: EMBER on NOIR grounds, rose mark.
- Uniforms: NOIR base, rose signature, gold detail.
- Signage: EMBER lit, NOIR unlit.
- UI: NOIR dark default, DUST light theme.
- Social: PUNCH bursts plus the tint ladder.
- Shoots: register per scene, warmth as light per the Luminance Law.
- Buildings and interiors: EMBER ambient over rose-black architecture, with rose identity moments.

### Governance

Guest colors are admitted by the sing-rule, enforced as the rose quota. PUNCH ships time-boxed: an event skin, re-ratified per campaign. Register drift is the failure mode the quota exists to catch. If daylight goes corporate or golden-hour becomes the default voice, the rose has receded, and the owner restores it. Panel record: `starred-palette-panel` run `wf_5b0af08b-c49`, 2026-09-01.

## Core Methodology

### Design System Architecture

The system is a **three-tier token system** with a processing pipeline. A structured token file is the source of truth. A build pipeline turns it into CSS Custom Properties, SCSS variables, and JSON. The upstream pipeline runs Figma design files into `tokens.json`. **Token Transformer** then converts that file into structured token sets. **Style Dictionary** then converts those sets into distributable formats (CSS, SCSS, JSON, iOS Swift).

The Bold Venture fork replaces the reference-level palette with Bold Venture brand colors. It replaces the **Roboto** typeface with a Bold Venture selection. It renames the `rux-` component prefix to `bvx-`. System-level and component-level tokens cascade from the reference-level replacements.

The upstream web component library uses **Stencil.js** and ships W3C-compliant Web Components with React and Angular wrappers. Upstream packages: `@astrouxds/tokens`, `@astrouxds/astro-web-components`, `@astrouxds/react`, `@astrouxds/angular`. Bold Venture equivalents: `@boldventure/tokens`, `@boldventure/web-components`, `@boldventure/react`, `@boldventure/angular`.

### Token Hierarchy

- **Tier 1, Reference Tokens:** raw palette values with no semantic meaning. They hold the complete color space, font size scale, spacing scale, and other primitives. Accessed as `var(--color-palette-{hue}-{shade})` and `var(--font-size-{scale})`. They do not change between themes.
- **Tier 2, System Tokens:** semantic intent; they map Reference Tokens to functional roles. The preferred tier for custom UI. Accessed as `var(--color-background-interactive-default)` or `var(--color-text-error)`. They change between dark and light themes.
- **Tier 3, Component Tokens:** scoped to individual components. They may change across releases. Accessed as `var(--button-color-background-default)` or `var(--table-row-color-background-hover)`. They follow their parent System Token references automatically.

The **Token Naming Convention** follows up to nine levels. The levels run `[group]-[component]-[element]-[category]-[property]-[concept]-[variant]-[state]-[scale]`. Not every token uses every level.

### Color System — Reference Palettes

The v2.0.0 note: these palettes are the Astro v7 legacy layer. Brand duty belongs to the Roster. Retained from this section: the **Grey ramp** (chrome, disabled states) and the **Status System** (sacred, untouched). The blues and every other hue below are retired from brand use. Every value is a Reference Token `var(--color-palette-{hue}-{shade})`, constant across themes.

- **Neutral:** `neutral-1000` `#000000` · `neutral-000` `#ffffff` · `neutral-1000a00` `#00000000`
- **Dark Blue:** 100 `#cbdee9` · 200 `#98bdd3` · 300 `#649cbd` · 400 `#2f7aa7` · 500 `#005a8f` · 600 `#004872` · 700 `#1c3f5e` · 800 `#1b2d3e` · 900 `#172635` · 950 `#080c11`
- **Bright Blue:** 100 `#daeeff` · 200 `#cee9fc` · 300 `#b7dcff` · 400 `#92cbff` · 500 `#4dacff` · 600 `#3a87cf` · 700 `#2b659b` · 800 `#1c3851` · 850 `#142435` · 900 `#101923`
- **Grey:** 100 `#f5f6f9` · 200 `#eaeef4` · 250 `#e0e5eb` · 300 `#d4d8dd` · 400 `#bbc1c9` · 500 `#a4abb6` · 600 `#7b8089` · 700 `#51555b` · 800 `#3c3e42` · 900 `#292a2d`
- **Red:** 400 `#ff5f60` · 500 `#ff3838` · 600 `#ff2a04` · 700 `#c8102e` · 800 `#8b1703` · 900 `#661102`
- **Orange:** 400 `#ffcc57` · 500 `#ffb302` · 600 `#ffaf3d` · 700 `#ff8c00` · 800 `#975f0e` · 900 `#664618`
- **Yellow:** 400 `#fded61` · 500 `#fce83a` · 600 `#fad800` · 700 `#c7ab00` · 800 `#917d01` · 900 `#645600`
- **Green:** 400 `#99f666` · 500 `#56f000` · 600 `#00e200` · 700 `#00ad23` · 800 `#007a33` · 900 `#005a00`
- **Cyan:** 400 `#5ce2ff` · 500 `#64d9ff` · 600 `#2dccff` · 700 `#20a9d5` · 800 `#35798e` · 900 `#285766`
- **Teal:** 100 `#d0f4f4` · 200 `#a1e9eb` · 300 `#70dde0` · 400 `#3ed2d6` · 500 `#00c7cb` · 600 `#009fa3` · 700 `#00777a` · 800 `#035051` · 900 `#032828`
- **Purple:** 100 `#e4e2f7` · 200 `#c9c5ed` · 300 `#aea8e5` · 400 `#938bdb` · 500 `#786dd3` · 600 `#6058a8` · 700 `#48417f` · 800 `#302c54` · 900 `#18152b`
- **Pink:** 100 `#edcef3` · 200 `#da9ce7` · 300 `#c76ada` · 400 `#b534ce` · 500 `#a200c1` · 600 `#81009a` · 700 `#610074` · 800 `#41004d` · 900 `#200227`
- **Hot Orange:** 100 `#f8ddd1` · 200 `#f0baa3` · 300 `#ea9875` · 400 `#e27545` · 500 `#da5309` · 600 `#af420a` · 700 `#833209` · 800 `#572108` · 900 `#2b1105`
- **Special single-shade hues:** `violet-800` `#502b85` · `blue-800` `#0033a0`

### Color System — Semantic Tokens Dark Theme

The Dark Theme is the default. All CSS Custom Properties resolve to dark values when no theme class is applied. These are System Tokens, the preferred tier for custom UI. The values below are the v1 (Astro) values; the Roster remap is in the Roster section above.

| CSS Custom Property | Hex | Reference source | Usage |
|---|---|---|---|
| `--color-background-base-default` | `#101923` | brightblue-900 | Application background, popup menus |
| `--color-background-base-header` | `#172635` | darkblue-900 | Header of base elements |
| `--color-background-base-hover` | `#142435` | brightblue-850 | Base element hover |
| `--color-background-base-selected` | `#1c3f5e` | darkblue-700 | Base element selected |
| `--color-background-surface-default` | `#1b2d3e` | darkblue-800 | Panels, dialogs, cards |
| `--color-background-surface-header` | `#172635` | darkblue-900 | Dialog and table headers |
| `--color-background-surface-hover` | `#1c3851` | brightblue-800 | Card and table row hover |
| `--color-background-surface-selected` | `#1c3f5e` | darkblue-700 | Card and table row selected |
| `--color-background-interactive-default` | `#4dacff` | brightblue-500 | Primary interactive background |
| `--color-background-interactive-hover` | `#92cbff` | brightblue-400 | Interactive hover |
| `--color-background-interactive-muted` | `#2b659b` | brightblue-700 | Muted interactive |
| `--color-background-transparent` | `#00000000` | neutral-1000a00 | Transparent |
| `--color-text-primary` | `#ffffff` | neutral-000 | |
| `--color-text-secondary` | `#d4d8dd` | grey-300 | |
| `--color-text-placeholder` | `#a4abb6` | grey-500 | |
| `--color-text-inverse` | `#080c11` | darkblue-950 | |
| `--color-text-interactive-default` | `#4dacff` | brightblue-500 | |
| `--color-text-interactive-hover` | `#92cbff` | brightblue-400 | |
| `--color-text-white` | `#ffffff` | neutral-000 | |
| `--color-text-black` | `#000000` | neutral-1000 | |
| `--color-text-error` | `#ff3838` | red-500 | |
| `--color-border-interactive-default` | `#4dacff` | brightblue-500 | |
| `--color-border-interactive-hover` | `#92cbff` | brightblue-400 | |
| `--color-border-interactive-muted` | `#2b659b` | brightblue-700 | |
| `--color-border-error` | `#ff3838` | red-500 | |

Focus and shadow: `--color-border-focus-default` `#da9ce7` (pink-200) · `--border-width-focus-default` 1px · `--spacing-focus-default` 0.125rem (2px) · `--shadow-overlay` `0px 4px 4px 1px rgba(0, 0, 0, 0.45)` · `--opacity-disabled` 40%.

### Color System — Semantic Tokens Light Theme

The Light Theme activates by adding the `.light-theme` CSS class to a wrapping HTML element. The same property names resolve to different values. These are the v1 (Astro) values; the Roster's light theme is the DUST register (see the remap above).

| CSS Custom Property | Hex | Reference source |
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
| `--color-text-primary` | `#292a2d` | grey-900 |
| `--color-text-secondary` | `#51555b` | grey-700 |
| `--color-text-placeholder` | `#7b8089` | grey-600 |
| `--color-text-inverse` | `#ffffff` | neutral-000 |
| `--color-text-interactive-default` | `#005a8f` | darkblue-500 |
| `--color-text-interactive-hover` | `#1c3f5e` | darkblue-700 |
| `--color-text-error` | `#c8102e` | red-700 |
| `--color-border-interactive-default` | `#005a8f` | |
| `--color-border-interactive-hover` | `#1c3f5e` | |
| `--color-border-interactive-muted` | `#2f7aa7` | |
| `--color-border-error` | `#c8102e` | |

Focus and shadow (light): `--color-border-focus-default` `#b534ce` (pink-400) · `--shadow-overlay` `0px 4px 4px 1px rgba(0, 0, 0, 0.35)`.

### Status System

The Status System is the most critical pattern in the design system. It uses a **Temperature-Based Severity Scale** mapped to color and a unique shape. Color alone never communicates status. Every level carries a distinct shape for color-blind operators.

| Severity | Color family | Meaning | Temperature |
|---|---|---|---|
| **Off** | Grey | Unavailable, disabled | Cold |
| **Standby** | Cyan | Available, enabled, idle | Cool |
| **Normal** | Green | Operational, satisfactory | Neutral |
| **Caution** | Yellow | Warning, unstable, requires monitoring | Warm |
| **Serious** | Orange | Distress, error, requires attention | Hot |
| **Critical** | Red | Emergency, alert, requires immediate action | Maximum |

Dark theme status colors (pass WCAG AA on dark backgrounds without borders): Critical `#ff3838` (255, 56, 56) `--color-status-critical` · Serious `#ffb302` (255, 179, 2) `--color-status-serious` · Caution `#fce83a` (252, 232, 58) `--color-status-caution` · Normal `#56f000` (86, 240, 0) `--color-status-normal` · Standby `#2dccff` (45, 204, 255) `--color-status-standby` · Off `#a4abb6` (164, 171, 182) `--color-status-off`.

Light theme status takes a fill and a required border. Fills alone fail WCAG AA, so the darker border is mandatory. The tokens are `--status-symbol-color-fill-{level}` and `--status-symbol-color-border-{level}`: Critical `#ff2a04` / `#661102` · Serious `#ffaf3d` / `#664618` · Caution `#fad800` / `#645600` · Normal `#00e200` / `#005a00` · Standby `#64d9ff` / `#285766` · Off `#7b8089` / `#3c3e42`.

Status System rules:

1. Status Symbols shall not be altered. They are required for ADA Section 508 and WCAG 2.0 compliance.
2. Consolidate to the highest urgency level. If sub-statuses are green, yellow, and red, the parent shows red.
3. Reserve red strictly for urgent, immediate-attention states. Overuse of red degrades operator response.
4. Do not add custom colors to the status palette. More colors reduce the operator's ability to learn the system.

### Classification Markings

Classification Marking colors are identical across both themes.

| Level | Hex | RGB | Font color |
|---|---|---|---|
| Top Secret//SCI | `#fce83a` | 252, 232, 58 | Black |
| Top Secret | `#ff8c00` | 255, 140, 0 | Black |
| Secret | `#c8102e` | 200, 16, 46 | White |
| Confidential | `#0033a0` | 0, 51, 160 | White |
| CUI | `#502b85` | 80, 43, 133 | White |
| Unclassified | `#007a33` | 0, 122, 51 | White |

CSS tokens follow `--color-classification-{level}`. Banner component tokens follow `--classification-banner-color-background-{level}`.

### Data Visualization Palette

A data set holds at most **8 colors**. Status colors are reserved for status indication and never serve general data visualization. Tokens are `--color-data-visualization-1` to `-8` in the source.

- **Dark theme:** 1 `#00c7cb` (teal-500) · 2 `#938bdb` (purple-400) · 3 `#4dacff` (brightblue-500) · 4 `#70dde0` (teal-300) · 5 `#c9c5ed` (purple-200) · 6 `#92cbff` (brightblue-400) · 7 `#a1e9eb` (teal-200) · 8 `#b7dcff` (brightblue-300)
- **Light theme:** 1 `#035051` (teal-800) · 2 `#6058a8` (purple-600) · 3 `#1c3851` (brightblue-800) · 4 `#00777a` (teal-700) · 5 `#786dd3` (purple-500) · 6 `#2b659b` (brightblue-700) · 7 `#009fa3` (teal-600) · 8 `#3a87cf` (brightblue-600)


### Typography System

The upstream system uses **Roboto** as its sole typeface. The Bold Venture fork keeps it until a custom typeface is chosen. `--font-family-sans: 'Roboto', -apple-system, BlinkMacSystemFont, 'Segoe UI', Oxygen-Sans, Ubuntu, Cantarell, 'Helvetica Neue', sans-serif;`

- **Font size scale** (token, rem, px): xs 0.75/12 · sm 0.875/14 · base 1/16 · lg 1.125/18 · xl 1.25/20 · 2xl 1.5/24 · 3xl 1.75/28 · 4xl 2.125/34 · 5xl 3/48 · 6xl 3.75/60. Each is `var(--font-size-{scale})`.
- **Font weights:** `--font-weight-light` 300 · `-regular` 400 · `-medium` 500 · `-bold` 700.
- **Line height scale** (rem/px): 2xs 0.875/14 · xs 1/16 · sm 1.25/20 · base 1.5/24 · lg 1.75/28 · xl 2/32 · 2xl 2.5/40 · 3xl 3.5/56 · 4xl 4.375/70.
- **Letter spacing:** sm -0.005em · base 0em · lg 0.0015em · xl 0.0025em · 2xl 0.005em.

Complete styles. Each produces five CSS Custom Properties following `--font-{id}-{property}`.

| Style | CSS class | Size (rem / px) | Weight | Line height | Letter spacing |
|---|---|---|---|---|---|
| Display 1 | `.bvx-display-1` | 3.75 / 60 | 300 Light | 1.167 | -0.005em |
| Display 2 | `.bvx-display-2` | 3 / 48 | 400 Regular | 1.167 | 0em |
| Heading 1 | `.bvx-heading-1` | 2.125 / 34 | 400 Regular | 1.176 | 0.0025em |
| Heading 1 Bold | `.bvx-heading-1-bold` | 2.125 / 34 | 700 Bold | 1.176 | 0.0025em |
| Heading 2 | `.bvx-heading-2` | 1.5 / 24 | 400 Regular | 1.167 | 0em |
| Heading 3 | `.bvx-heading-3` | 1.25 / 20 | 500 Medium | 1.2 | 0.0015em |
| Heading 4 | `.bvx-heading-4` | 1.25 / 20 | 300 Light | 1.2 | 0.0015em |
| Heading 5 | `.bvx-heading-5` | 1.125 / 18 | 400 Regular | 1.333 | 0em |
| Heading 6 | `.bvx-heading-6` | 1.125 / 18 | 300 Light | 1.333 | 0em |
| Body 1 | `.bvx-body-1` | 1 / 16 | 400 Regular | 1.5 | 0.005em |
| Body 1 Bold | `.bvx-body-1-bold` | 1 / 16 | 700 Bold | 1.5 | 0.005em |
| Body 2 | `.bvx-body-2` | 0.875 / 14 | 400 Regular | 1.429 | 0.005em |
| Body 2 Bold | `.bvx-body-2-bold` | 0.875 / 14 | 700 Bold | 1.429 | 0.005em |
| Body 3 | `.bvx-body-3` | 0.75 / 12 | 400 Regular | 1.333 | 0.005em |
| Body 3 Bold | `.bvx-body-3-bold` | 0.75 / 12 | 700 Bold | 1.333 | 0.005em |
| Control Body 1 | `.bvx-control-body-1` | 1 / 16 | 400 Regular | 1.25 | 0.005em |
| Control Body 1 Bold | `.bvx-control-body-1-bold` | 1 / 16 | 700 Bold | 1.25 | 0.005em |
| Monospace 1 | `.bvx-monospace-1` | 1.75 / 28 | 500 Medium | 1.143 | 0em |

The minimum text size for data-dense displays is 14px (0.875rem, Body 2).

### Spacing System

The spacing system uses a **4px base grid**. The token number times 4 gives the pixels. Sub-grid exceptions exist for fine adjustments. Tokens (`var(--spacing-N)`, rem, px): 0 · 0/0; 025 · 0.0625/1; 050 · 0.125/2; 1 · 0.25/4; 2 · 0.5/8; 3 · 0.75/12; 4 · 1/16; 6 · 1.5/24; 8 · 2/32; 10 · 2.5/40; 12 · 3/48; 14 · 3.5/56; 16 · 4/64; 20 · 5/80; 24 · 6/96.

### Border Radius and Opacity

`--border-width-none` 0 · `-xs` 1px · `-sm` 2px · `-lg` 4px · `--radius-base` 3px · `--radius-circle` 50% · `--opacity-0` 0% · `-25` 25% · `-35` 35% · `-40` 40% · `-45` 45% · `-50` 50%.

### Responsive Grid

| Breakpoint | Columns | Margin | Gap default | Gap compact |
|---|---|---|---|---|
| 0 to 360px | 4 | 16px | 16px | 8px |
| 361 to 768px | 8 | 24px | 24px | 12px |
| 769 to 1920px | 12 | 24px | 24px | 12px |
| 1921 to 3840px | 12 | 48px | 48px | 24px |

### Component Inventory

The system ships 40 components as W3C Web Components. Tag names use the `bvx-` prefix (upstream `rux-`). Format: number, component, tag, category.

1. Accordion, `bvx-accordion`, Layout
2. Breadcrumb, `bvx-breadcrumb`, Navigation
3. Button, `bvx-button`, Actions
4. Card, `bvx-card`, Layout
5. Checkbox, `bvx-checkbox`, Form Controls
6. Classification Marking, `bvx-classification-marking`, Data Display
7. Clock, `bvx-clock`, Data Display
8. Container, `bvx-container`, Layout
9. Date Picker, `bvx-datetime`, Form Controls
10. Dialog, `bvx-dialog`, Feedback
11. Global Status Bar, `bvx-global-status-bar`, Navigation
12. Icon, `bvx-icon`, Data Display
13. Indeterminate Progress, `bvx-indeterminate-progress`, Feedback
14. Input Field, `bvx-input`, Form Controls
15. Log, `bvx-log`, Data Display
16. Menu, `bvx-menu`, Actions
17. Monitoring Icon, `bvx-monitoring-icon`, Data Display
18. Monitoring Progress Icon, `bvx-monitoring-progress-icon`, Data Display
19. Notification Banner, `bvx-notification`, Feedback
20. Pagination, `bvx-pagination`, Navigation
21. Pop Up, `bvx-pop-up`, Actions
22. Progress, `bvx-progress`, Feedback
23. Push Button, `bvx-push-button`, Actions
24. Radio Button, `bvx-radio`, Form Controls
25. Search, `bvx-input` (variant), Form Controls
26. Segmented Button, `bvx-segmented-button`, Actions
27. Select, `bvx-select`, Form Controls
28. Slider, `bvx-slider`, Form Controls
29. Status Symbol, `bvx-status`, Data Display
30. Switch, `bvx-switch`, Form Controls
31. Table, `bvx-table`, Data Display
32. Tabs, `bvx-tabs`, Navigation
33. Tag, `bvx-tag`, Data Display
34. Textarea, `bvx-textarea`, Form Controls
35. Timeline, `bvx-timeline`, Layout
36. Toast, `bvx-toast`, Feedback
37. Tooltip, `bvx-tooltip`, Feedback
38. Tree, `bvx-tree`, Navigation
39. Application State, pattern within the Global Status Bar, Navigation
40. Link, native anchor styled via CSS, Navigation

### Component Token Specifications

- **Button:** `--button-color-background-default` `#4dacff` · `-hover` `#92cbff` · `-secondary` `#00000000` · `--button-color-text-default` `#080c11` · `--button-color-text-secondary-default` `#4dacff` · `--button-border-width` 1px · `--button-radius` 3px · `--button-padding-x-large|medium|small` 1rem · `--button-padding-y-large` 0.75rem · `-medium` 0.5rem · `-small` 0.25rem.
- **Input:** `--input-color-background` `#101923` · `--input-color-border-default` `#2b659b` · `-hover` `#92cbff` · `-invalid` `#ff3838` · `--input-color-text` `#ffffff` · `--input-color-placeholder` `#a4abb6` · `--input-radius` 3px · `--input-border-width` 1px.
- **Table:** `--table-header-color-background` `#172635` · `--table-header-shadow` `0px 4px 8px 0px rgba(0,0,0,0.45)` · `--table-row-color-background-default` `#1b2d3e` · `-selected` `#1c3f5e` · `-hover` `#1c3851` · `--table-row-color-text` `#ffffff` · `--table-row-color-border` `#101923`.
- **Global Status Bar:** `--global-status-bar-color-background` `#172635` · `-color-text` `#ffffff` · `--global-status-bar-icon-color-default` `#4dacff` · `-hover` `#92cbff`.
- **Tab:** `--tab-color-text-default` `#4dacff` · `-hover` `#92cbff` · `-selected` `#ffffff` · `--tab-border-color-selected` `#4dacff` · `--tab-border-width-bottom` 4px.
- **Card:** `--card-color-border` `#51555b` · `--card-color-background` `#101923` · `--card-radius` 3px.
- **Notification:** `--notification-banner-color-background` `#101923` · `--notification-banner-radius-outer` 3px.
- **Tooltip:** `--tooltip-color-background` `#3c3e42` · `--tooltip-color-text` `#ffffff` · `--tooltip-radius` 1px.
- **Progress:** `--progress-color-background` `#1b2d3e` · `--progress-color-inner` `#4dacff` · `--progress-radius-inner` 8px.
- **Tag:** `--tag-radius` 4px · `--tag-color-text` `#ffffff`.

### UX Patterns

- **Status Pattern:** the single most important pattern. It governs all status indication across every application. The six-level scale (Off through Critical) is mandatory. Status colors serve nothing but status. Symbols combine color and shape for colorblind access.
- **Navigation patterns:** five primary patterns, which may be combined. **List-Detail** puts a list panel left and a detail panel right, for small flat collections. **Tab Navigation** separates distinct categories or step-wise workflows, when tasks complete within one tab. **Tree Navigation** handles hierarchical single-taxonomy objects; mixing unrelated types in one tree is prohibited. **Table Navigation** gives a full-screen tabular view for large uniform datasets, with search, sort, and filter. **Timeline Navigation** handles event-based real-time scheduling, with the timeline at the top and details below.
- **Global Status Bar:** always at the top of the application and always dark theme, whatever the application theme. It holds only truly global elements: application name, state, clock, monitoring icons, and emergency controls.
- **Table pattern:** columns run by importance left to right. General data is left-aligned. Dates, times, currency, and numbers are right-aligned. Headers match their data alignment. Minimum text in tables is 14px (Body 2). A header click sorts ascending first, then toggles direction.
- **Form pattern:** one column preferred. Labels sit top-left above fields. Help text sits 8px below the field in secondary text color, sentence case. **Inline Validation** fires on focus loss: the border turns red and red bold text replaces the help text. **Form-Level Validation** fires on submit. Required fields show an asterisk right of the label when most fields are optional. Optional fields show "(optional)" when most fields are required.
- **Notification pattern:** three types, ordered by disruption. **Log** is least disruptive and goes to an event log. **Banner** is application-level and never blocks interaction. **Toast** is temporary, auto-dismisses, stacks vertically with the newest on top, and never covers critical elements.
- **Voice guidelines:** application text is direct, confident, and commanding. No pronouns, no personified application, no salutations. An error message states what the problem is, why the input is invalid, and how to fix it.

### Compliance Framework

The upstream Astro UXDS defines a **Three-Tier Compliance System**:

| Tier | Requirements | Scope |
|---|---|---|
| Tier 1 | Status icons and status colors only | Minimum for operator familiarity |
| Tier 2 | Tier 1 plus Astro colors, typography, and visual design patterns | Full visual compliance |
| Tier 3 | Tier 2 plus interaction patterns and behavioral compliance | Complete UX compliance |

Bold Venture targets **Tier 3** for all character system tooling and **Tier 2** minimum for all other digital output.

- **MIL-STD-1472H compliance:** the upstream system was audited against MIL-STD-1472H Section 5.17 (Information Systems) on September 29, 2022. The audit found compliance across functional interface, personnel compatibility, human performance, display content, drop-down menus, and submenus. It found two non-compliant items, in toolbar tooltip label requirements for non-standard icons.
- **WCAG 2.1 AA compliance:** Astro v7 overhauled the color system to meet WCAG 2.1 AA contrast guidelines. Dark theme status colors pass without extra treatment. Light theme status colors need mandatory darker borders. The focus state uses bright pink, chosen to contrast the blue-dominant palette.

### Theming Architecture

The Dark Theme is the default for all Bold Venture applications. All properties resolve to dark values when no theme class applies. The Light Theme activates with the `.light-theme` class on a wrapping element. That class overrides System and Component Tokens by CSS specificity. Reference Tokens stay constant across themes. The Global Status Bar stays dark in either theme. The cascade: Reference Tokens constant; System Tokens change between themes; Component Tokens follow their parent System Token references. A rebrand replaces the Reference palette, and the token pipeline (Style Dictionary) regenerates all output formats.

### Naming Convention — Astro to Bold Venture Translation

| Astro UXDS | Bold Venture |
|---|---|
| `rux-` (component prefix) | `bvx-` |
| `.rux-` (CSS class prefix) | `.bvx-` |
| `@astrouxds/tokens` | `@boldventure/tokens` |
| `@astrouxds/astro-web-components` | `@boldventure/web-components` |
| `@astrouxds/react` | `@boldventure/react` |
| `@astrouxds/angular` | `@boldventure/angular` |
| `ruxchange` (event prefix) | `bvxchange` |
| `onRux{Event}` (React wrapper) | `onBvx{Event}` |
| Astro UXDS | Bold Venture Design System |
| Rocket Communications Inc. | Bold Venture X |

All CSS Custom Property names for tokens (colors, spacing, typography, borders) stay unchanged. Only component-scoped names with the `rux` prefix become `bvx`.

## Implementation

### Adopting the Design System for a New Application

1. Install the token package: `npm install @boldventure/tokens`.
2. Import the CSS in the application entry point: `import '@boldventure/tokens/dist/css/index.css'`.
3. The dark theme activates automatically; no extra class is needed.
4. To use the light theme on an element, add `.light-theme` to the wrapping container.
5. Reference System Tokens for all color, spacing, and typography decisions. Do not reference Reference Tokens directly unless building custom reference-level extensions.
6. For Web Components, install `npm install @boldventure/web-components`.
7. For React, install `npm install @boldventure/react`.

### Applying the Status System

1. Identify the severity level of the condition.
2. Use the matching status color and symbol from the Status System.
3. Do not use status colors for any non-status purpose.
4. If sub-statuses exist, consolidate to the highest urgency level.
5. On light theme backgrounds, include the mandatory darker border on every status symbol.

### Building a Custom Component

1. Use System Tokens for all visual properties (background, text, border).
2. If the component has states (default, hover, focus, disabled, invalid), map each to the matching System Token variant.
3. Apply `--opacity-disabled` (40%) for disabled states.
4. Apply `--color-border-focus-default` for focus rings.
5. Apply `--color-border-error` and `--color-text-error` for invalid states.
6. Register the component in the Bold Venture component inventory with the `bvx-` prefix.

### Extending the Color System

1. Add new colors only at the Reference Token level.
2. Name new Reference Tokens `--color-palette-{hue}-{shade}`.
3. New colors shall not conflict with existing status colors.
4. New colors need System Token mappings before they appear in UI.
5. All new colors pass WCAG AA contrast testing against both dark and light theme backgrounds.

## Examples

### Example 1: System Explorer Application

The **System Explorer** (Phase 3 deliverable of the character systems pipeline) applies the system as follows:

- The application background uses `--color-background-base-default` (#140A0E).
- Navigation tabs use `--tab-color-text-default` (#E38AA6). The active tab uses `--tab-color-text-selected` (#F5EDE9) with a 4px bottom border in `--tab-border-color-selected` (#B03A5B).
- Layer cards use `--color-background-surface-default` (#241018) with `--color-background-surface-hover` (#341820) on hover.
- Status flags use the status colors. ACTIVE flags show `--color-status-critical` (#ff3838). PENDING flags show `--color-status-serious` (#ffb302). FIRED_PRE_STORY flags show `--color-status-off` (#a4abb6).
- A derived statistic above its expected range (Truth Exposure Index above 60) shows `--color-status-serious` (#ffb302) with a caution indicator.
- A derived statistic below zero (Stress Threshold below zero) shows `--color-status-critical` (#ff3838) with a critical indicator.

### Example 2: Character Database Editor Application

The **Database Editor** (Phase 4 deliverable) applies the system to a read-write interface:

- In browse mode, all fields are read-only text in `--color-text-primary` (#F5EDE9) on `--color-background-surface-default` (#241018).
- The mode toggle uses the secondary button style with `--button-color-text-secondary-default` (#E38AA6).
- In edit mode, inputs activate with `--input-color-background` (#140A0E) and `--input-color-border-default` (#2b659b).
- A persistent indicator in the Global Status Bar changes to `--color-status-caution` (#fce83a) to show the editable state.
- Form validation is inline. A field that breaks a scale class constraint (an odd number where the variable needs even values) shows `--input-color-border-invalid` (#ff3838). It also shows red error text with the constraint and the nearest valid value.
- The point budget tracker in the bottom panel uses `--progress-color-inner` (#B03A5B) and shifts to `--color-status-serious` (#ffb302) above 90% utilization.
