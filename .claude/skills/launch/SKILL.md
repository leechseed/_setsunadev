---
name: launch
description: Run the launch sequence (BOLO 58) — one word stands the Command up. A zero-token script brings the local stations up (the DARKROOM, JUDY in session voice, the wire probe) and opens the two boards (the sit rep page, the SOI), then the sit rep runs in the formation and the reply carries the station poll above the board. Fires on "go for launch" (RULED 9/17; garbles "go for log", "go for lunch") and on "launch sequence" / "start launch sequence" spoken alone. Never on "go N".
---

# The launch sequence — BOLO 58

**Steps (BOLO 64, provisional 9/23):** RECON = `launch.py` pings every station before it starts anything · ORDER = the proword · EXECUTE = the stations, then the sit rep in its own formation · CONSOLIDATE = the poll above the board in one reply.

Stations RULED 2026-09-17 by Chief: the sit rep page · the SOI · zero DOPE SHEETs · the DARKROOM · **Stash + the Stash deck (added 9/20, BOLO 75)** · JUDY in session voice (the full loop: whisper ears on the 3090, the face, Blondie reading the session) · her seven spoken tools over the wire. The proword is **go for launch** (RULED 9/17, the flight director's poll answered); the thing it fires is **the launch sequence** (RULED the same breath). No questions, no preamble.

## 1 · Stations (zero tokens)

```
python _tools/launch/launch.py
```

**Run it from the Bash tool, never the PowerShell tool** (confirmed 9/20: PowerShell-tool children sit in a job object and JUDY's paste into the VS Code box stops landing; the same goes for any relaunch of JUDY).

**AUDIT first (ruled 10/6, Chief: "audits to be done at the beginning of every launch, and that to be the first thing we always do"):** runs `_tools/audit/sop_audit.py` (zero tokens) and reports its counts; NO-GO when a public file carries private detail, a BOLO row is stale or unmarked, or the rack holds an old note; retired words and the tree are advisory. A NO-GO AUDIT line goes in the reply's caveat with the fix offered as "clean your station". Then it brings up what is down and reports what is up: pings the DARKROOM (:8484) and starts it if needed; pings Stash (:9999), starts `stash-win.exe` if down, then opens the Stash deck (`_PRIVATE/stash_deck/index.html`) in the default browser; **NAHIMIC (10/4):** kills any Nahimic audio process and reports NO-GO if its service or logon tasks came back (they re-route the audio devices under JUDY's mic; re-disabling needs admin); finds a running `judy.py --session` or starts one (stopping a standalone JUDY first, same hotkey); **FACES (10/4):** starts JUDY's console (:8787, `--no-open`) if it is down, then opens the face deck (`/faces`) as a browser tab; **DECK (ruled 10/6):** opens the Traffic Deck (`/traffic`: JUDY's last five replies in tabs, the open calls with Take rec and answer boxes, Take all recs, the net chart) as its own window, the same way as the face deck; starts `knobs.py --run` (the MPK knobs as scroll and zoom, BOLO 62) unless one is running; runs `wire_probe.py` for the seven tools; opens the sit rep page and the SOI as tabs in the default browser (Chief, 9/20: never the Edge app window). Prints the station poll:

```
STATIONS · 2026-09-17 04:20
  AUDIT     GO     SOP audit  (0 finding(s) · R 0 · P 0 · B 0 · K 0 · T 0 · report _tools/audit/out/ · 2.8 s)
  DARKROOM  GO     http://127.0.0.1:8484/  (already live)
  STASH     GO     http://127.0.0.1:9999/  (started · 4 s · deck opened)
  NAHIMIC   GO     audio guard  (service + tasks disabled · 1.4 s)
  JUDY      GO     session voice · pid 25096  (already running)
  FACES     GO     http://127.0.0.1:8787/faces  (already live · opened)
  DECK      GO     http://127.0.0.1:8787/traffic  (opened)
  KNOBS     GO     MPK knobs · pid 54508  (started · 2.2 s · scroll Y · scroll X · zoom)
  WIRE      GO     server judy · 7/7 tools  (probe ok · 2.1 s)
  SITREP    GO     https://…  (opened)
  SOI       GO     https://…  (opened)
  ALL GO
```

Keep the poll verbatim. A NO-GO is reported, never retried in a loop; the sit rep still runs.

**PULL UPDATES (BOLO 137, Chief 10/12: "give me regular updates please have that be part of the process"):** run `python _PRIVATE/taxonomy_engine/pull_queue.py report`. If any wave is live, arm one hourly CronCreate (minute 7) whose prompt runs the report and posts it as a short update; the poll gets a PULL line with the report's wave lines. Any turn that starts a wave arms the same job if none is armed (CronList first). The job deletes itself when the pull goes idle.

## 2 · The sit rep

Run the `sitrep` skill exactly as written (prep → three specialists at gear 1 → assemble → build, flush, publish). Nothing about the launch changes the formation.

## 3 · The reply

The station poll in a fenced block first, **then two lines before anything else (ruled 10/6, Chief: "one of the first things you'll say to me … is what we left off last time and what I think we should start on next … which BOLO"): `**Left off:**` one sentence from the last session's note (the last thing worked and where it stopped) · `**Start next:** BOLO N`, the one row you recommend starting on, with a five-word why. The spoken line says both.** Then the sit rep reply as the sitrep skill specifies (the link, Block 0 in three bullets, the leverage line, one caveat line if any). The spoken line (SOP §7 rule 10) opens the reply and names any NO-GO.
