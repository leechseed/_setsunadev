---
title: "Ice machine wash cycle duration"
uuid: 0bc14c59-eed9-4781-a288-abb1cf92eda0
created: 2026-07-09
updated: 2026-07-09
trunk: OTHER
messages: 8
chars: 4085
artifacts: 0
generated_files: 0
tools: []
source: claude.ai-export-2026-08-15
---

# Ice machine wash cycle duration

> **Conversation Overview**

The person is troubleshooting a Hoshizaki KM-650 commercial ice machine. The conversation began with a question about wash cycle duration for that specific model. Claude initially described a wash/rinse sequence, but the person corrected this — the KM-650 does not have a dedicated rinse cycle position, only a WASH/OFF/ICE switch. Claude acknowledged the correction and clarified that rinsing is accomplished by running additional plain-water passes through the wash cycle.

The conversation then shifted to the actual problem: the machine runs through the wash cycle normally but fails to produce ice when set to ICE mode. Claude walked through the most likely causes for this symptom pattern on the KM-650, including a bin control or thermistor falsely reading the bin as full, a float switch or water supply issue preventing reservoir fill in ICE mode, a control board safety lockout, or a compressor/fan not engaging. Claude recommended three immediate self-service steps: a full power-down reset (switch to OFF, kill power at breaker for 5 minutes, then restart), confirming water actually fills the reservoir in ICE mode, and checking that the bin control is not falsely triggered. Claude ended by asking whether the compressor and fan are running at all when switched to ICE, as that would narrow the diagnosis significantly. No resolution was reached within the conversation.

---
## 🧑 Papi  <sub>2026-07-09 20:23:02</sub>

how long to run wash cycle for ice machine

---

## 🤖 Claude  <sub>2026-07-09 20:23:27</sub>

The user is asking about wash cycle duration for an ice machine, and given that Papi works in a commercial kitchen at [EMPLOYER] in [CITY], this is definitely about a commercial unit. The timing varies significantly depending on the brand and model—Hoshizaki, Manitowoc, Scotsman, and Ice-O-Matic all have different specifications.

The cleaning process typically involves running a nickel-safe acid cleaner through the machine to remove mineral buildup, followed by a rinse and sanitize cycle, but without knowing the specific machine model, I can't give an exact timeframe. I should ask which ice machine they're working with or offer to look up the manufacturer's instructions for their particular unit.

---

## 🧑 Papi  <sub>2026-07-09 20:24:44</sub>

hoshizaki km-650

---

## 🤖 Claude  <sub>2026-07-09 20:24:49</sub>

For a Hoshizaki KM-650, the cleaning/wash cycle takes roughly 30–40 minutes end to end.

Rough breakdown using Hoshizaki's LoCO₃Ice or Scale Away cleaner:
- Wash switch on, add cleaner, run the wash cycle (~20–30 min for the cleaning solution to circulate).
- Switch to RINSE and run 2–3 rinse cycles (~5 min each) to flush all chemical.

Follow the exact steps on the door decal or in the service manual, and always sanitize after cleaning (separate sanitizer solution, more rinse cycles). Water and cleaner amounts are model-specific, so check the KM-650 manual for the correct dilution.

Want me to pull up the exact KM-650 cleaning procedure and cleaner-to-water ratios?

---

## 🧑 Papi  <sub>2026-07-09 20:26:19</sub>

there is no rinse cycle

---

## 🤖 Claude  <sub>2026-07-09 20:26:24</sub>

You're right — the KM-650 doesn't have a separate RINSE position. It's a WASH/OFF/ICE switch, so the rinsing is done by repeating the wash cycle with plain water.

General flow:
- Set switch to WASH, add cleaner, let it circulate the full wash cycle (~20–30 min) until it drains out.
- Then run the wash cycle again 2–3 times with plain water (no cleaner) to flush all the chemical — each pass is basically another full wash cycle.
- Repeat for sanitizer, then flush again with plain water passes.

So total cleaning wash cycle is ~20–30 min, plus each rinse pass adds another full cycle length.

I don't want to guess at the exact cycle timing or water-fill amounts for the KM-650 specifically — those vary and getting the cleaner dilution wrong matters. Want me to look up the exact KM-650 procedure from Hoshizaki's manual?

---

## 🧑 Papi  <sub>2026-07-09 20:27:16</sub>

i just need the ice machine to work i set it to on and it just doesn't make ice. but the wash cycle works

---

## 🤖 Claude  <sub>2026-07-09 20:27:25</sub>

Good diagnostic clue: if WASH runs (pump works, water moves) but ICE mode makes nothing, the wash side of the system is fine — it's the freezing/ice-making sequence that's stuck.

Common causes on a KM-650 when wash works but ICE doesn't:

- Bin control / thermostat thinks the bin is full. The bin switch or thermistor may be triggering "full" so it never starts. Check the bin control (some are a mechanical paddle, some a thermostatic bulb near the bin).
- Float switch / water supply. If the reservoir isn't filling in ICE mode, it won't start a freeze. Make sure the water valve is open and the float switch moves freely.
- Control board timing / lockout. The board may be in a safety lockout. Try a full power reset: switch to OFF, kill power at the breaker/plug for 5 min, restore, then switch to ICE.
- Ambient/head issues (fan, contactor, compressor not kicking on) — but you'd usually hear the compressor try.

Fastest things to try yourself right now:
1. Full power-down reset (5 min off), then set to ICE.
2. Confirm water is actually filling the reservoir in ICE mode.
3. Check the bin control isn't reading full (empty bin, make sure nothing's blocking the sensor).

Is the compressor/fan running at all when you switch to ICE, or is it dead silent? That narrows it down fast.