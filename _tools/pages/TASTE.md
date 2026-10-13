# TASTE · the Command's page taste guide

Our standing rules come first and always win. The kit's rules below them apply only where they fit inside ours. (BOLO 140, picks taste-01, taste-05, taste-07.)

## 1 · Our standing rules (not negotiable)

- **DARK only.** No theme toggle. A light face, if ever needed, is E-INK Kindle gray, never white.
- **Palette:** background #121110, panels #1B1A18, accent #FF5A1F (the creator-cases orange). Rose "purple" belongs to DARKROOM and public-facing pages only.
- **Fonts:** Barlow Condensed for headings, Atkinson Hyperlegible for body, IBM Plex Mono for data and code.
- **Thin chrome:** one strip about 44px tall at the top. Metadata sits behind a button.
- **Hover layer:** dense pages carry nested hover terms (Space locks, click pins).
- **Check pages show the thing:** the picture or preview, the open link, and a what-to-do box. Never titles alone.
- **Clock:** every time Chief reads is 12-hour with AM or PM.
- **Mermaid:** static `<pre class="mermaid">` in the markup, never injected by script.

## 2 · From taste-skill: what fits

**Anti-slop rules**
- One accent color (ours, #FF5A1F), one corner-radius system, one theme.
- No purple gradients, no three-equal-feature-cards layout, no centered hero over a mesh background.
- No fake product screenshots built from divs. Show the real thing or leave it out.
- No filler chrome: scroll cues, section-number labels, version footers, locale strips.
- Contrast stays at WCAG AA or better on buttons and forms (the a11y-architect agent checks).
- Animate only transform and opacity, and honor reduced motion.
- Icons come from a real library, never hand-drawn SVG paths.

**The three dials, in our words**

| Kit dial | Our name | Our setting |
|---|---|---|
| DESIGN_VARIANCE | How far a page departs from the standard layout | Low. Same strip, same panels, same palette every time. |
| MOTION_INTENSITY | How much moves | Low. Hover and pin only. |
| VISUAL_DENSITY | How much sits on one screen | High on dense pages (they carry the hover layer), moderate elsewhere. |

The kit's own baselines (8, 6, 4) are rejected; our settings are in the table.

## 3 · From brutalist-skill: what fits inside orange-on-dark

- **Type scale:** heavy, tightly tracked uppercase Barlow Condensed for headings, sized with `clamp()`. Small, widely spaced IBM Plex Mono for metadata.
- **Grid:** strict CSS Grid with visible 1px borders and 1px-gap dividers. Wide negative space beside dense data.
- **No decoration:** flat color only. No gradients, soft shadows or translucency. No border-radius.
- **Semantic tags:** `<data>`, `<samp>`, `<kbd>`, `<output>` for machine values.
- **One archetype:** the Tactical Telemetry (dark, mono-heavy) archetype matches us.

## 4 · From output-skill: the output rule

- **Deliverables** (files, pages, scripts, specs) carry no placeholders and no truncation: no "rest of code", no TODO, no "for brevity", no "...". Count the requested items, build each in full, check the count before handing back.
- **Replies** stay Spartan (SOP 7.6): trim words, keep every fact. Replies are exempt from the completeness rule.
- If a deliverable is too long for one pass, stop at a clean breakpoint, end with a marker showing how far it got, and resume exactly there when told.

## 5 · Rejected (conflicts with ours)

| Kit rule | Why rejected |
|---|---|
| Hazard-red accent (brutalist) | Our one accent is #FF5A1F. |
| Terminal-green second accent | One accent only. |
| Swiss Industrial Print light substrate | DARK is the only theme; no light face but Kindle gray. |
| Global noise overlay, CRT scanlines, halftone and dithering | Decoration; our chrome is thin and flat. |
| ASCII framing, decorative (R) (C) TM marks, crosshairs, barcode lines | Decoration; clutters the 44px strip. |
| The kit's font picks and font bans | Our fonts are fixed: Barlow Condensed, Atkinson Hyperlegible, IBM Plex Mono. |
| Baseline dials 8 / 6 / 4 | Our dials are low, low, high on dense pages. |
| Next.js, Tailwind v4, Motion, GSAP stack | Our pages are static HTML built by scripts. |
| Official design systems (Fluent, Carbon, GOV.UK, shadcn) as foundation | Our palette and fonts are the foundation. |
| Ask one clarifying question before coding | Default-public, no-gating-questions rule: make the call and mark it provisional. |
| Dashboards, data tables, wizards declared out of scope | Dashboards and tables are most of what we build. |
| Ban on metadata strips and eyebrow labels | Thin metadata behind a button is our rule. |

## Source

taste-skill, brutalist-skill and output-skill by Leonxlnx, MIT: https://github.com/Leonxlnx/taste-skill/tree/main/skills/ . Fetched 2026-10-13 through a summarizing fetch tool, not verbatim; check the repo before quoting. Adopted 2026-10-13, provisional, BOLO 140.
