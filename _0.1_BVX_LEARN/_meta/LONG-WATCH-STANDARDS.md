# Long-Watch Display Standards: Color, Luminance, Theme, Layout for Multi-Hour Monitoring

Research date 2026-09-06. HIGH = read in the primary document; MEDIUM = secondary source or search extract of the primary; LOW = single informal source or inference.

## Executive summary

1. No standard prefers dark themes for comfort. MIL-STD-1472H 5.2.2.6 allows light-on-dark only below ~0.1 lx ambient; FAA HF-STD-001B 5.3.2.1.6 says positive polarity "when all else is equal"; IHO S-52 goes black-background only at dusk/night. A dark theme is justified by a dark room. (HIGH)
2. The nearest published analog to a reference app watched for hours in a dim room is FAA HF-STD-010A: 11 foreground colors on black, validated at 40 lx, every object at least 3:1. (HIGH)
3. Text contrast: MIL-STD-1472H and NASA require 6:1, prefer 10:1; FAA requires 3:1, prefers 7:1, and allows 3:1 to 5:1 only for dark-ambient non-reading elements. Body text belongs at 7:1 to 10:1. (HIGH)
4. Black level: FAA caps black at 2 cd/m^2 for dark-adapted displays; S-52 night area colours at 1.3 cd/m^2. Near-black, not #000000. (HIGH)
5. Surround: task to adjacent surround 3:1, task to remote 10:1, screen to sequential task areas 0.1L to 10L (MIL-STD-1472H, HIDH, ISO 9241-303). Unanimous. (HIGH)
6. Hue budget: 11 nameable colors absolute (MIL-STD-1472H); FAA allows four per alphanumeric screen, seven per related set, six if meanings must be recalled. (HIGH)
7. Meanings collide: MIL-STD-2525D fixes red=hostile, cyan/blue=friend, green=neutral, yellow=unknown; every other standard fixes red=warning, yellow=caution, green=normal, blue=advisory. Reconcile by layer, not hue. (HIGH)
8. Navy blue CIC lighting is real (JHU APL 1981; MIL-STD-1472H 5.2.1.9.8 "low-level blue-filtered white" per SAE AS25050), but the 1983-84 NAVSEA/SUBDEVRON 12 finding was that brightness, not color, governs dark adaptation. (HIGH/MEDIUM)
9. The positive-polarity advantage (Buchner, Piepenbrock, Mayr; Dobres 2017) is largest for small type in near-dark rooms; mitigate with 16 to 22 arcmin type and brighter text, not dimmer. (HIGH)
10. Night shifts: NASA-STD-3001 Rev F specifies 250 melanopic lux blue-enriched while awake and 8 +/- 2 melanopic lux blue-depleted pre-sleep; red light keeps alertness without suppressing melatonin (Figueiro 2016, Sanchez-Cano 2025). Dim first, warm second. (HIGH)

## 1. Governing standards, with numbers

### MIL-STD-1472H (15 Sep 2020, active; no change notice found -- content HIGH)

- Luminance: adjustable range >= 50:1 (5.2.1.2.1); >= 35 cd/m^2 capable (5.2.1.2.2); ambient adds <= 25 percent of display luminance (5.5.3.1.9); uniformity <= 2:1, 1.5:1 preferred (5.2.2.4).
- Contrast: characters 6:1 minimum, 10:1 preferred (5.2.2.7); text <= 14 pt >= 4.5:1, larger >= 3:1, "black or dark text should be on a light background" in daylight (5.17.25.16.3); "white or light text should be on a dark background" in dark conditions (5.17.25.16.4).
- Polarity: light-on-dark only when ambient < ~0.1 lx, else dark-on-light (5.2.2.6). Bridge: dark-on-light at >= 540 lx, light-on-dark for dark-adapted watchstanders, "separate day and night color palettes may be necessary" (5.18.2.2.1-3).
- Dark adaptation: internal ambient <= 0.001 lx, 0.0001 preferred (5.2.1.9.7); displays dim to 3.5 cd/m^2 without adaptation, 0.35 to 0.03 cd/m^2 (0.003 preferred) with it (5.18.2.2.3.4-5).
- Lighting color: "low-level blue-filtered white color light shall be used for panel, display, task, and backlit keyboard lighting in accordance with SAE AS25050" (5.2.1.9.8); white dimmable to zero preferred (5.5.3.6.1); red "should not be used" where color symbology is read (5.5.3.6.2, 5.18.3.2.2); colored ambient otherwise prohibited (5.5.3.8).
- Surround: any two sources in view <= 5:1 (5.5.3.1.5); Table XXII task:adjacent 3:1, task:remote 10:1, luminaire 20:1, work area:rest 40:1; illuminance task:surround <= 3:1, task:background <= 10:1 (5.5.3.10). Table XXI: control rooms 540 lx; console fronts 300 lx recommended, 110 minimum.
- Type: >= 10 arcmin, should be >= 15 (5.17.18.2); stroke 1/12 to 1/6 of height, width 0.9 height (5.17.18.4-5); color-coded small symbols >= 20 arcmin, large >= 30, 45 preferred (5.17.25.13-14); viewing distance >= 33 cm, preferably >= 50, <= 70 near controls (5.2.2.11.2-4).
- Color: max 11 nameable colors (5.17.25.5); cool hues for infrequent/background, warm for action (5.17.25.8.1-2); color-coded elements > 10 cd/m^2 (5.17.25.9); symbol vs background >= 100 dE(Yu'v'), set members >= 20 dE (5.17.25.16.1-2); two brightness levels max, >= 2:1 apart (5.17.26.2); flash 0.8 to 5 Hz, 50 percent duty, two rates, mission-critical only (5.17.27). Table XV: red emergency/malfunction/stop, yellow caution/delay/check, green go/in tolerance, white in progress, blue advisory. Table XL tactical column: red hostile, yellow unknown, green neutral, blue/cyan friendly.
- Flicker: avoid 1 to 30 Hz, refresh >= 100 Hz recommended (5.12.1.4.2).

### MIL-STD-2525D (10 Jun 2014) -- HIGH

- 5.5: "maximize the contrast between symbology and the display background"; frames and icons black on light backgrounds, white on dark.
- Table XV fills, dark / medium / light RGB: hostile (200,0,0) / (255,48,49) / (255,128,128); friend (0,107,140) / (0,168,220) / (128,224,255); neutral (0,160,0) / (0,226,0) / (170,255,170); unknown (225,220,0) / (255,255,0) / (255,255,128); civilian option (80,0,80) / (128,0,128) / (255,161,255). Identity colors "shall vary only in terms of their luminance"; translucent fills 35 percent opacity. Table XVI unfilled: red (255,0,0), cyan (0,255,255), neon green (0,255,0), yellow (255,255,0), magenta (255,0,255).
- MIL-STD-2525 (1994) 5.4.2.1: symbols >= 1 fL; contrast 6:1 to 10:1; "avoid using saturated blue for small lines or dots when the background is dark."
- 2525E: exists per search results; jcs.mil returned Access Denied. Unverified.

### MIL-HDBK-759C (31 Jul 1995) -- BLOCKED

Companion to MIL-STD-1472 (MEDIUM); secondary citations give red low-level lighting at 0.07 to 0.35 cd/m^2 (MEDIUM) and resolving ambient-light vs dark-adaptation conflicts by task priority (HIGH via FAA 5.11.4.3.6).

### Navy shipboard

- DOD-HDBK-289(SH) Lighting on Naval Ships: BLOCKED.
- Common Display System consoles: three-eyed horizontal, WUXGA, "human systems integration design principles" (Lockheed 2019 order; GTS). MEDIUM
- IHO S-52 Ed. 6.1.1 (bridge ECDIS via IEC 62288): day table light background; dusk and night tables black; night area colours <= 1.3 cd/m^2 vs 80 bright-sun; bright-sun black <= 0.52 cd/m^2; calibration ambient Day 200 cd/m^2, Dusk 10, Night darkness; optional 0.9 ND filter. HIGH

### FAA HF-STD-001B (2016) -- HIGH

- Rooms: control room 5 to 50 fc, TRACON 1 to 50 fc (5.3.1.5.1). Contrast > 3:1, 7:1 preferred (5.3.1.5.9); >= 2:1 at peak ambient (5.3.1.5.10); nothing in the immediate surround brighter than the display except emergency indicators (5.3.1.5.12); black <= 2 cd/m^2 at maximum brightness for critical and dark-adapted displays (5.3.1.9.7).
- Polarity: positive "when all else is equal"; "reflections are less visible on a bright background" (5.3.2.1.6).
- Exhibit 5.6.2.2.1: bright ambient > 7:1; dark ambient 3:1 to 5:1; continuous reading > 7:1; dynamic text 8x background.
- Type: 20 to 22 arcmin preferred, 16 minimum where legibility matters, 24 maximum for reading (5.6.2.5.6.5-9).
- Color: short wavelengths for infrequent/status (5.6.6.2.2.6); blue not for fine foreground (5.6.6.2.2.7); red "only if high ambient illumination is expected" (5.6.6.2.2.8); light images on dark "viewed extensively ... should be amber or green rather than white" (5.6.6.2.2.11); pure blue never on dark for text or thin lines (5.6.6.2.2.14); pairs to avoid include blue on black, red on black, magenta on black, yellow on white (Exhibit 5.6.6.2.5.2); foreground >= 100 dE and >= 7:1 from background (5.6.6.2.6.3-4); "a medium achromatic background (for example, dark or medium gray)" maximizes foreground colors (5.6.6.2.6.6); four colors per alphanumeric screen, seven per set (5.6.6.2.7.3); six if recalled or searched (5.6.6.2.7.5); highlight on dark = white block, dark letters (5.6.6.3.7).
- Lighting: maximum dark adaptation via red or low-level white at x,y = 0.330 +/- 0.030 (5.11.4.3.1); specular <= 3x surround (5.11.4.5.1); brightness ratios 3:1 / 10:1 / 40:1 (Exhibit 5.11.4.6.3).
- FAA HF-STD-010A (2020) palette (DOT/FAA/AM-18/18, AM-20/08): white FFFFFF, gray B3B3B3, blue 5E8DF6, aqua 07CDED, green 23E162, yellow DFF334, orange FE930D, red FF1320, pink F684D8, purple D822FF, brown C5955B on black, plus weather backgrounds 173928, 5A4A14, 5D2E59; white pinned to 80 cd/m^2; every object >= 3:1; black chosen because it "provides maximum contrast" and controllers were used to it; validated at 40 lx; controllers found below 3:1 "did indeed impair legibility appreciably." HIGH

### NASA-STD-3001 Vol. 2 Rev. F (approved 2026-07-14) and HIDH -- HIGH

- Table 10.4-2: peak white > 100 cd/m^2 (400 preferred); ambient contrast ratio >= 100:1 (1000:1 preferred); 60 Hz minimum, 90 Hz for active control; 32 px/deg (64 preferred). Table 10.4-3: flashing red emergency, red warning/failed, yellow caution/off-nominal, green power/on/good.
- Appendix F: character height >= 0.25 deg (15 arcmin), 0.4 deg preferred; contrast 6:1, 10:1 preferred; red emergency, yellow caution, blue advisory; flash 0.8 Hz/70 percent low, 3 Hz/50 percent high.
- Table 8.7-1: general >= 350 lx horizontal, >= 200 vertical; sleep <= 0.02 lx. Table 8.7-2: awake 250 melanopic EDI lux, DER 0.7, ~480 nm blue-enriched; pre-sleep 8 +/- 2 melanopic lux, DER 0.3, blue-depleted. OCHMO TB-026: CCT 2700 to 6500 K.
- HIDH: luminance ratios 3:1 / 10:1 / 20:1 / 40:1 (Table 8.7-2); maximum dark adaptation red at 0.07 to 0.34 cd/m^2 (8.7.8); indicators 110 to 300 percent of panel luminance (8.7.10.1); color coding degrades beyond nine colors (5.4.10.7); HFES 2007 ambient contrast ratio default 10, >= 3; blue advisory "not recommended for general use" (10.11.5.5).
- Orion Program Display Format Standards CxP 72242 Rev A exists (NTRS 20110004034; IAC-17-B3.9) but is not public.

### ISO 9241-303/307/112

- 303:2011 5.2.4: task areas viewed in sequence 0.1L to 10L of screen average; walls up to 1:10 harmless; office positive-polarity example 100 to 150 cd/m^2 at 500 lx; at night luminance "should not be so high as to annihilate dark adaptation" (5.2.2). HIGH from preview. Clauses 5.5.2-5.5.3 (contrast, polarity) not in preview; the 3:1 minimum traces to ISO 9241-3 (MEDIUM). 307 = test methods; 112 scope only. Unverified beyond that.

## 2. US Navy CIC practice

- Blue lighting: APL's Combat System Evaluation Laboratory, "arranged like an AEGIS cruiser Combat Information Center," had "overhead conventional white and shipboard blue lighting" switchable by quadrant (Serpico, JHU APL Tech. Digest 2(4), 1981). HIGH. MIL-STD-1472H 5.2.1.9.8 codifies blue-filtered white per SAE AS25050. HIGH
- Rationale: the CRT-glare story (white light glared on amber/green phosphors) comes from Steemit and Medium posts, both BLOCKED; LOW. A former sonar chief citing the 1983-84 NAVSEA/COMSUBDEVRON 12 study says "the color made no difference, but the brightness did," yielding Low Level White; Virginia-class control rooms reportedly use "dim purple-ish lights directly over the screens to reduce glare." MEDIUM/LOW
- Environment: "dimly lit," "packed with glowing screens," "a very high level of cognitive attention" all deployment (TWZ, Jan 2025). HIGH. DVIDS photos of DDG-105 (2022) and DDG-108 (2019) show darkened consoles; captions do not state the lighting. LOW
- Console conventions: 1994 Aegis Display System large-screen was "bright blue background with white graphics," CROs "displayed in green for easy low light viewing," NTDS symbols, blink for lost tracks, red=error, blue=advisory, yellow=caution, green=go (Davidson, Virginia Tech 1994). HIGH. NSWC Dahlgren 2008 specifies RGB for Aegis map backgrounds and tested 2525 symbols on "de-saturated Aegis Baseline 6.1.7 map background colors" (DTIC ADA484484, BLOCKED; MEDIUM).
- Fatigue: NSMRL 2022 (Chabal et al.) gave submariners 470 nm blue glasses ~40 min after waking plus blue-blockers pre-sleep; wearers slept longer and reported less sleepiness. HIGH. NPS Crew Endurance Handbook v2.5 prescribes 3/9 circadian watchbills (HIGH); its light-exposure advice sits in a BLOCKED 2022 Proceedings piece (LOW).

## 3. Contractors

- Lockheed Martin: Aegis displays built to MIL-STD-1472 and HSI principles; a Moorestown Aegis "UI/UX Engineer - Display Products" posting (now 404) required HCI/HFE degrees; a Fort Worth HF posting pairs UX/UI with "MIL-STD-1472 and MIL-STD-516." MEDIUM. The 2006 PACE program adapts "the rate of information or ... its presentation format" under measured overload. HIGH. No public palette.
- Northrop Grumman: Sperry Marine VisionMaster FT is IEC 62288 type-approved with "four day/night presentation modes"; Navy ECDIS fleet-approved after LHD-3 trials. MEDIUM. Its palettes are S-52's. No IBCS UX guidance is public.
- Boeing: 787 deck "designed with direct input from pilots," 777-common, large LCDs, dual HUDs (HIGH); 777-9 HF campaign of 200+ pilots over three years (Boeing, May 2026, HIGH). Its color rules are FAA AC 25-11A: red warnings, amber/yellow cautions, green normal/engaged, white scales, cyan/blue sky, tan earth, magenta ILS/FD/bugs, light gray inactive; <= 6 coding colors (DO-257A); "saturated colors are not recommended ... for background"; avoid blue-on-black and red-on-black. HIGH. "Quiet, dark cockpit" (lit = abnormal) dates from the 767 and is partial on 777/787. MEDIUM

## 4. SpaceX and NASA

- Crew Dragon: "sleek black and white" cabin whose "only punch of color ... is from the flat panel displays" (Fox/SpaceX 2019, MEDIUM); three touchscreens, 38 covered hardware buttons, EJECT handle deadened in orbit (MEDIUM); Chromium/HTML/JS UI with hardware abort, deorbit and fire controls (RocketSTEM, MEDIUM). Hurley: "you've got to be very deliberate when you're putting in input"; Behnken: "the right answer for all flying is not to switch to a touchscreen" (TechCrunch 2020, HIGH). Designers Shane Mielke (Principal UI/UX, Crew Displays, 2018-20) and AJ Fitzpatrick ("style guide and design specifications ... touch targets for astronaut gloves and legibility during vibration") say details are ITAR-restricted. HIGH. No SpaceX statement explains the dark theme. LOW
- SpaceX mission control: 24 consoles, overhead screen, "librarylike silence"; "GSW" flashes red, "PROP 1" yellow (D. W. Brown, NYT, 2023). MEDIUM. No published palette.
- NASA MCC: Apollo mint-green consoles, monochrome CRTs, stencil/dichroic big boards (Hackaday 2020, MEDIUM); MCC-21 (2013) flat panels and wider front screen, no palette (MEDIUM). Crew conventions are Appendix F and Table 10.4-3. An ISS display rule set (red/yellow limit arrows, yellow asterisks on overflow, stale flags) surfaced in a search extract without a locatable URL. Unverified.

## 5. Eye-strain and vigilance literature

- Polarity: Piepenbrock, Mayr, Mund, Buchner, Ergonomics 56(7):1116-1124 (2013): 169 adults (18-33 and 60-85), dark room, 350 vs 1 cd/m^2; positive polarity better on acuity (young d = 2.17) and proofreading (eta^2 = 0.06) at both ages. HIGH. Piepenbrock, Mayr, Buchner, Human Factors (2014): advantage grows as type shrinks (MEDIUM). Piepenbrock et al., Ergonomics 57(11) (2014): smaller pupils explain it (MEDIUM). Buchner, Mayr, Brandt (2009): holds from 5 to 550 lx (HIGH as cited). Dobres, Chahine, Reimer, Applied Ergonomics 60:68-73 (2017): glance legibility at ~0 vs 4750 lx; negative polarity in the dark needed 122 ms vs 84 ms at 3 mm; no difference in bright light. HIGH. Counterweights: Legge et al. (1985) cloudy-media readers do better on dark; Aleman et al., Sci. Rep. (2018) choroidal thinning after an hour of light mode (NN/g, MEDIUM).
- Surround: 0.1L to 10L (ISO 9241-303); 3:1 / 10:1 (MIL-STD-1472H); 3:1 / 10:1 / 20:1 / 40:1 (IESNA via HIDH). HIGH
- Blue light: 6.5 h blue vs green suppressed melatonin twice as long and shifted phase 3 h vs 1.5 h; 8 lx suffices (Harvard Health, MEDIUM). Sanchez-Cano et al., Life 15(5):715 (2025): n = 12, 80 lx, 631 vs 464 nm, 3 h; melatonin 26.0 vs 7.5 pg/mL at 2 h. HIGH. Figueiro, Sahin, Wood, Plitnick, Biol. Res. Nurs. 18(1):90-100 (2016): red 630 nm and 2568 K white both improved GO/NOGO; only white suppressed melatonin. MEDIUM. Dimming beats filtering (Harvard, MEDIUM). Watchstanders who sleep after the watch want dim, long-wavelength screens late; those staying entrained to nights want the reverse (NASA Table 8.7-2; NSMRL 2022).
- Color temperature: NASA bounds 2700 to 6500 K (HIGH); screen-CCT fatigue studies (IJHCI 41(2) 2024; Zhang et al., Lighting Res. Technol. 2024) BLOCKED, LOW.
- Halation: only FAA's dark-ambient 3:1 to 5:1 and "amber or green rather than white" bound contrast from above (HIGH); "never pure black" web advice (UX Movement) is LOW.
- Flicker: MIL-STD-1472H 1 to 30 Hz forbidden, >= 100 Hz; NASA 60/90 Hz. HIGH. IEEE 1789-2015: low-risk modulation <= 0.08 x f (90 to 1250 Hz), no-effect <= 0.0333 x f (to 3 kHz), above 3 kHz unrestricted; secondaries disagree on labels. MEDIUM.
- Type: 16 to 22 arcmin at 50 to 70 cm (FAA, MIL-STD-1472H). HIGH
- Breaks: Johnson and Rosenfield, Optom. Vis. Sci. (2023): "little or no peer-reviewed evidence" for 20-20-20; Talens-Estarelles et al., CLAE (2023): 30 subjects, 40-min tablet task, 20-s breaks every 5/10/20/40 min, no significant differences. MEDIUM.

## 6. Synthesis: the long-watch palette rules

1. Keep the dark theme because the room is dark; at a 300 to 540 lx desk the standards prefer dark-on-light (MIL-STD-1472H 5.2.2.6; FAA 5.3.2.1.6). Ship a light theme too.
2. Background: near-black neutral or slightly cool gray at 1 to 3 percent of peak white (about #121518 to #1c2024), so black is <= 2 cd/m^2 at a 100 to 120 cd/m^2 white (FAA 5.3.1.9.7) and near S-52's 1.3 cd/m^2 night ceiling. Not #000000.
3. Primary text: not white; a neutral at 78 to 85 percent luminance (#c8ccd0 to #d6dade) yields 9:1 to 11:1 on that ground, inside MIL-STD-1472H's 6:1 to 10:1 and FAA's > 7:1 for continuous reading. Reserve pure white for the selected state (FAA 5.6.6.3.7).
4. Secondary text and chrome: 4.5:1 to 6:1 (MIL-STD-1472H 5.17.25.16.3; FAA 3:1 to 5:1 dark-ambient). Nothing readable below 3:1 (HF-STD-010A).
5. For the image-curation tool's hours-long sessions, consider a desaturated amber or green primary text (FAA 5.6.6.2.2.11), kept far from caution yellow.
6. Status colors exactly: red critical/failed, yellow/amber caution, green normal, blue advisory (MIL-STD-1472H Table XV; NASA Table 10.4-3; AC 25-11A). Flash only for emergencies, 0.8 to 5 Hz, two rates maximum, never chrome.
7. MIL-STD-2525 affiliation colors live on the symbol layer only, always with the redundant frame shape; on a dark ground use Table XV dark or medium fills, never the light column; never reuse those hues for UI status on the same screen. When both sets coexist, desaturate one; the standard permits luminance variation, not hue variation.
8. Hues: six meaningful per screen (FAA 5.6.6.2.7.5; DO-257A), 11 absolute (MIL-STD-1472H 5.17.25.5). Everything else grayscale.
9. Saturation: full saturation only for small, temporary, critical items (AC 25-11A); large fills low-saturation and low-luminance (HF-STD-010A weather colors; S-52 night areas). Symbol vs ground >= 100 dE; set members >= 20 dE.
10. Links: never pure blue on dark (FAA 5.6.6.2.2.14; MIL-STD-2525 1994). Use a light desaturated aqua near 60 to 70 percent luminance (HF-STD-010A 07CDED is validated), underline on hover, distinct from friend-cyan if 2525 symbols are present.
11. Forbidden pairs: red on black, blue on black, magenta on black, yellow on white, saturated red beside saturated blue (FAA Exhibit 5.6.6.2.5.2).
12. Accent: one hue for selection and focus, >= 4.5:1 on the ground, >= 20 dE from every status hue; two brightness levels at most, >= 2:1 apart (MIL-STD-1472H 5.17.26.2).
13. Surround: the screen within 1/3 to 3x of what it sits against and never > 10x the room (ISO 9241-303; MIL-STD-1472H Table XXII). Give the app its own brightness/contrast control (MIL-STD-1472H 5.2.2.7c).
14. Type: body 16 to 22 arcmin -- at 60 cm about 2.8 to 3.8 mm cap height, roughly 16 to 20 px at 96 dpi -- stroke 1/12 to 1/6 of height, nothing under 10 arcmin (MIL-STD-1472H 5.17.18). Regular over thin weights; negative polarity punishes small thin type most (Piepenbrock 2014; Dobres 2017).
15. Color-coded small symbols >= 20 arcmin, large >= 30, and color-coded elements > 10 cd/m^2 (MIL-STD-1472H 5.17.25.9, .13, .14).
16. Night mode: cap luminance first, then shift white toward 3000 to 4000 K; leave status and 2525 hues alone (NASA 2700 to 6500 K; Figueiro 2016; Harvard).
17. Motion: no blinking chrome, no animation in the 1 to 30 Hz band; the user's monitor may add PWM flicker when dimmed (IEEE 1789).
18. Do not build the 20-20-20 rule into the product; its numbers are unsupported. Keep dense pages scannable so eyes can leave the screen.
19. Where standards disagree: take 6:1 over 3:1 for text, FAA HF-STD-010A for dark-room palette practice (the only one built for a windowless room at 40 lx), and MIL-STD-1472H for polarity, surround and meanings.

## Sources

- MIL-STD-1472H: https://dn790000.ca.archive.org/0/items/mil-std-1472-g-chg-1/MIL-STD-1472H.pdf ; status https://everyspec.com/MIL-STD/MIL-STD-1400-1499/MIL-STD-1472H_57041/
- MIL-STD-2525D: http://www.mapsymbs.com/MilStd2525D.pdf ; MIL-STD-2525 (1994): https://nps.edu/documents/104517539/109705106/MIL-STD-2525.PDF/87529131-72ce-44a7-91fb-b6c05381f7a4 ; https://github.com/Esri/joint-military-symbology-xml/issues/524
- MIL-HDBK-759C: https://everyspec.com/MIL-HDBK/MIL-HDBK-0700-0799/MIL-HDBK-759C_22550/
- FAA HF-STD-001B: https://hf.tc.faa.gov/publications/2016-12-human-factors-design-standard/full_text.pdf ; https://hf.tc.faa.gov/hfds/download-hfds/hfds_pdfs/Ch5_Displays_and_printers.pdf
- FAA palette: https://www.faa.gov/sites/faa.gov/files/data_research/research/med_humanfacs/oamtechreports/202008.pdf ; https://www.faa.gov/sites/faa.gov/files/data_research/research/med_humanfacs/oamtechreports/201818.pdf
- FAA flight-deck color: https://hfcc.dot.gov/publications/docs/GeneralGuidance/zz_FAA_GeneralGuidanceDoc_Chapter_03_Section_07.pdf
- NASA: https://standards.nasa.gov/system/files/tmp/NASA-STD-3001%20Vol%202%20Rev%20F.pdf ; https://www.nasa.gov/reference/appendix-f-vol-2/ ; https://www.nasa.gov/wp-content/uploads/2023/12/ochmo-tb-026-lighting-design.pdf ; https://www.nasa.gov/wp-content/uploads/2015/03/human_integration_design_handbook_revision_1.pdf ; https://ntrs.nasa.gov/api/citations/20110004034/downloads/20110004034.pdf ; https://ntrs.nasa.gov/api/citations/20170008757/downloads/20170008757.pdf ; https://www.disti.com/case-study/nasa-orion
- ISO: https://cdn.standards.iteh.ai/samples/57992/bddfd91165b444f6b9815a6993feadc5/ISO-9241-303-2011.pdf ; https://www.iso.org/standard/64840.html
- IHO S-52: https://iho.int/uploads/user/pubs/standards/s-52/S-52%20Edition%206.1.1%20-%20June%202015.pdf
- Navy: https://secwww.jhuapl.edu/techdigest/content/techdigest/pdf/V02-N04/02-04-Serpico.pdf ; https://www.twz.com/news-features/red-sea-attacks-are-testing-combat-information-centers-aboard-u-s-navy-warships-like-never-before ; https://thetidesofhistory.com/2024/09/22/rigged-for-red-why-are-there-red-lights-on-a-submarine/ ; https://www.dvidshub.net/image/7033703/uss-deweys-combat-information-center ; https://www.dvidshub.net/image/5996189/uss-wayne-e-meyer-ddg-108-combat-information-center-watch-standing ; https://vtechworks.lib.vt.edu/server/api/core/bitstreams/1610d2ab-ea69-4a5d-8062-6c27f29f204d/content ; https://www.militaryaerospace.com/communications/article/14068099/open-architecture-displays-shipboard ; https://gts.us.com/weblog_GTS-Awarded-86M-Contract-to-Provide-Common-Display-System-CDS-Sustainment ; https://cet.org/wp-content/uploads/2024/09/AYO-DoD-Study-Navy-1.pdf ; https://nps.edu/documents/105475179/0/HSI-CrewEndurance-v2.5-web.pdf/17ee1a2c-1cac-4044-8611-3436c443b82e ; https://www.dvidshub.net/news/568561/fatigue-bio-threats-nhrc-expands-wearables-study-aboard-uss-essex-rimpac-2026
- Contractors: https://news.lockheedmartin.com/2006-08-10-Lockheed-Martin-to-Use-Augmented-Cognition-to-Develop-a-New-Human-Computer-Interactive-Interface ; https://www.lockheedmartinjobs.com/job/fort-worth/human-factors-design-engineer-for-training-systems/694/91103776432 ; https://www.ship-technology.com/products/integrated-bridge-system/ ; https://www.defensedaily.com/navy-approves-new-northrop-grumman-navigation-display-system/navy-usmc/ ; https://www.boeing.com/commercial/787/by-design ; https://www.boeing.com/features/2026/05/airline-pilots-advance-777-9-human-factors-testing ; https://www.skylegs.com/news/2017/11/dark-cockpit-philosophy
- SpaceX: https://www.foxnews.com/science/step-inside-crew-dragon-spacex-reveals-interior-of-crewed-space-capsule.amp ; https://science.slashdot.org/story/18/08/15/0455239/spacex-reveals-the-controls-of-its-dragon-spacecraft-for-the-first-time ; https://www.rocketstem.org/2020/11/12/from-cell-phones-to-spacecraft-touchscreens-are-taking-over-ui/ ; https://techcrunch.com/2020/05/04/this-is-certainly-different-astronauts-on-controlling-the-dragon-spacecraft-via-touchscreen/ ; https://www.shanemielke.com/work/spacex/crew-dragon-displays/ ; https://www.andrewjfitzpatrick.com/portfolio-spacex.html ; https://dillonbaird.io/articles/mutantdragon/ ; https://www.sfexaminer.com/news/business/31-hours-inside-spacex-mission-control/article_07587466-8ba0-11ed-8742-2b25cfec2892.html ; https://www.khaleejtimes.com/opinion/inside-spacex-mission-control-room ; https://www.nasa.gov/image-article/spacex-engineers-follow-countdown-4
- NASA MCC: https://hackaday.com/2020/10/29/a-look-behind-the-big-boards-at-mission-control-in-the-golden-age-of-nasa/ ; https://www.nbcnews.com/news/amp/wbna52935759 ; https://www.nasa.gov/johnson/history/apollo-mcc-restoration/
- Literature: https://www.psychologie.hhu.de/fileadmin/redaktion/Oeffentliche_Medien/Fakultaeten/Mathematisch-Naturwissenschaftliche_Fakultaet/Psychologie/AAP/Publikationen/2013/Piepenbrock-2013-Positive_display_polarity_is_.pdf ; https://journals.sagepub.com/doi/abs/10.1177/0018720813515509 ; https://pubmed.ncbi.nlm.nih.gov/25135324/ ; https://jdobr.es/pdf/Dobres-etal-2017-Ambient.pdf ; https://www.nngroup.com/articles/dark-mode/ ; https://www.health.harvard.edu/staying-healthy/blue-light-has-a-dark-side ; https://pmc.ncbi.nlm.nih.gov/articles/PMC12113466/ ; https://journals.sagepub.com/doi/abs/10.1177/1099800415572873 ; https://pubmed.ncbi.nlm.nih.gov/36473088/ ; https://www.sciencedirect.com/science/article/pii/S1367048422001990 ; https://www.dial.de/en-GB/news/ieee-1789-a-new-standard-for-evaluating-flickering-leds ; https://www.azom.com/article.aspx?ArticleID=14729 ; https://www.tandfonline.com/doi/abs/10.1080/10447318.2024.2305982 ; https://doi.org/10.1177/14771535231181502 ; https://uxmovement.com/content/why-you-should-never-use-pure-black-for-text-or-backgrounds/

## Blocked / Unverified

- BLOCKED: DTIC ADA484484, ADA552350, ADA148883; DOD-HDBK-289(SH) (maritime.dot.gov); MIL-HDBK-759C mirror (deepsloweasy.com); jcs.mil MIL-STD-2525D/E; Shipbucket CIC thread; Steemit and Medium CIC essays; USNI Proceedings (2013, 2022) and USNI News; colorusage.arc.nasa.gov (DNS) and web.archive.org (unreachable); NASA commercial-crew blog posts (redirect); Forbes Dragon piece; space.com (membership wall); uxdesign.cc and Medium recreations; Design News Orion article; Wright State 787 VSD paper; SAGE (Piepenbrock 2014, Figueiro 2016, Shattuck 2024); PubMed/Europe PMC abstract pages; Taylor and Francis (OLED flicker, IJHCI CCT); ScienceDirect; ISO 9241-303 clause 5.5 and ISO 9241-112 body; Lockheed Aegis UI/UX posting (404); Sperry Marine WECDIS brochure (empty); history.navy.mil "CIC Yesterday and Today" (404).
- UNVERIFIED: any MIL-STD-1472H change after Sep 2020 (none found; DLA QuickSearch not fetched); MIL-STD-2525E color table (assumed unchanged from D); MIL-HDBK-759C's 0.07 to 0.35 cd/m^2 figure; CRT-glare origin of blue CIC lighting; "purple-ish" Virginia-class lighting (single Quora-derived account); DVIDS lighting descriptions (from image, not caption); NASA ISS MCC display rules (no locatable URL); CxP 72242 content; SpaceX's reasons for the dark Dragon theme and its mission-control palette; Northrop "four day/night modes" (search extract); IEEE 1789 formula labeling; screen-CCT fatigue findings; 20-20-20 abstracts (search extracts only).
