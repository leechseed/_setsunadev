---
name: launch
description: Run the launch sequence (BOLO 58) — one word stands the Command up. A zero-token script brings the local stations up (the DARKROOM, JUDY in session voice, the wire probe) and opens the two boards (the sit rep page, the SOI), then the sit rep runs in the formation and the reply carries the station poll above the board. Fires on "launch sequence", "start launch sequence", "stand-to" / "stand to" (the benched word), "light the candle", "all stations", "stand the Command up".
---

# The launch sequence — BOLO 58

Stations RULED 2026-09-17 by Chief: the sit rep page · the SOI · zero DOPE SHEETs · the DARKROOM · JUDY in session voice (the full loop: whisper ears on the 3090, the face, Blondie reading the session) · her seven spoken tools over the wire. The proword is still benched (STAND-TO rec); "launch sequence" is the working phrase. No questions, no preamble.

## 1 · Stations (zero tokens)

```
python _tools/launch/launch.py
```

Brings up what is down and reports what is up: pings the DARKROOM (:8484) and starts it if needed; finds a running `judy.py --session` or starts one (stopping a standalone JUDY first, same hotkey); runs `wire_probe.py` for the seven tools; opens the sit rep page and the SOI in Edge app windows. Prints the station poll:

```
STATIONS · 2026-09-17 04:20
  DARKROOM  GO     http://127.0.0.1:8484/  (already live)
  JUDY      GO     session voice · pid 25096  (already running)
  WIRE      GO     server judy · 7/7 tools  (probe ok · 2.1 s)
  SITREP    GO     https://…  (opened)
  SOI       GO     https://…  (opened)
  ALL GO
```

Keep the poll verbatim. A NO-GO is reported, never retried in a loop; the sit rep still runs.

## 2 · The sit rep

Run the `sitrep` skill exactly as written (prep → three specialists at gear 1 → assemble → build, flush, publish). Nothing about the launch changes the formation.

## 3 · The reply

The station poll in a fenced block first, then the sit rep reply as the sitrep skill specifies (the link, Block 0 in three bullets, the leverage line, one caveat line if any). The spoken line (SOP §7 rule 10) opens the reply and names any NO-GO.
