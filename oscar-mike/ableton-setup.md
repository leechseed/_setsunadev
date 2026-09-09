---
parked: 2026-09-08
title: The Ableton Rig — NI plugins, Massive presets, MPK Mini
handle: ableton setup
tags: OPERATOR, BLACK-adjacent (feeds BOLO 35), Ableton Live 10, Native Instruments, MIDI, tooling
status: parked on "Oscar Mike ×3" — two of three answered and done; one open item on the box; one phantom BOLO
open-decision: "(1) Massive Factory Library — not installed on the box (no .nmsv anywhere on the standard paths; user Sounds folder empty): Native Access → Massive → Repair / install the factory content · (2) the song with the chords — Papi asked for its BOLO; nothing in the vault carries it (only the 123 BPM ULTRA DARK track is on record); capture it when he describes it"
---

# THE ABLETON RIG

## What is on the box (read 9/8)

- **DAW:** Ableton Live 10 Standard, 10.1.43 (also FL Studio, REAPER, DaVinci Resolve).
- **NI VST2 (64-bit):** `C:\Program Files\Native Instruments\VSTPlugins 64 bit\` — Kontakt 6 (`Kontakt.dll`), Massive, Reaktor 6 (+ FX), Guitar Rig 6, Replika, Supercharger, Solid Bus Comp.
- **NI VST3:** `C:\Program Files\Common Files\VST3\` — the same set plus Kontakt 7, Kontakt 8, Komplete Kontrol.
- **Massive presets:** none found. `Documents\Native Instruments\Massive\Sounds` is empty; no `.nmsv` under Common Files, Public Documents, or ProgramData. The factory library content was never installed by Native Access (the plugin was).

## What was answered

1. **Plugins not detected** — Live had been pointed at the NI root folder (32-bit + 64-bit subfolders, no VST3 inside). Fix: Preferences → Plug-Ins → VST2 custom folder = the `VSTPlugins 64 bit` folder itself; VST3 System Folders = On; Alt-click Rescan. Third-party plugins show under **Plug-Ins** in the browser, never under Instruments.
2. **Where Massive and Kontakt sit in Live** — browser → Plug-Ins → VST2 / VST3 (or the search box). Kontakt opens empty: Libraries tab → drag an instrument into the rack. Packs live inside Kontakt/Massive, registered through Native Access, never in Live's browser.
3. **MPK Mini** — USB, class-compliant. Preferences → Link MIDI → the MPK input row: Track On, Remote On; arm a MIDI track; Drum Rack takes Bank A pads on the C1 row unmapped; Ctrl+M maps the knobs.

## Resume

1. Native Access: install or Repair the Massive factory library; confirm presets appear in Massive's Browser tab.
2. If Papi names the song, capture its BOLO and find the Live set (search was started 9/8 and stopped on his interrupt — do not resume it unasked).

## Related

[[story-timeline]] (BOLO 35 — the instrument is the point of the rig) · [[ultradark-walkthrough]] (the one track on record)
