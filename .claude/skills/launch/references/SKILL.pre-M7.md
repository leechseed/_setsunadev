---
name: launch
description: Use when Chief says "go for launch", the garbles "go for log" and "go for lunch", or "launch sequence", "start launch sequence" or "run launch sequence" spoken alone. Never on "go N".
---

# The launch sequence — BOLO 58

**Steps (BOLO 64, provisional 9/23):** RECON = `launch.py` pings every station before it starts anything · ORDER = the proword · EXECUTE = the stations, then the sit rep in its own formation · CONSOLIDATE = the poll above the board in one reply.

Chief ruled the stations on 2026-09-17. They are the sit rep page, the SOI, zero DOPE SHEETs, the DARKROOM, JUDY in session voice and her seven spoken tools over the wire. Stash and the Stash deck joined on 9/20 (BOLO 75). The proword is **go for launch**; the thing it fires is **the launch sequence**. Ask no questions and write no preamble.

## 1 · Stations (zero tokens)

```
python _tools/launch/launch.py
```

**Run it from the Bash tool, never the PowerShell tool** (confirmed 9/20). PowerShell-tool children sit in a job object, and JUDY's paste into the VS Code box stops landing. The same goes for any JUDY relaunch.

**AUDIT first (ruled 10/6, Chief: "audits to be done at the beginning of every launch, and that to be the first thing we always do"):** the script runs `_tools/audit/sop_audit.py` and reports its counts. mirror.py --check runs on Chief's word, never on its own; a page with changed headings is a call for Chief before any skill or hook edit (ruled 10/13).
- NO-GO when a public file carries private detail, a BOLO row is stale or unmarked, or the rack holds an old note.
- Retired words and the tree are advisory.
- Put a NO-GO AUDIT line in the reply's caveat, with the fix offered as "clean your station".

Then it brings up what is down and reports what is up:
- **DARKROOM:** pings :8484 and starts it if needed.
- **STASH:** pings :9999, starts `stash-win.exe` if down, then opens the Stash deck (`_PRIVATE/stash_deck/index.html`) in the default browser.
- **NAHIMIC (10/4):** kills any Nahimic audio process. It reports NO-GO if the service or logon tasks came back, because they re-route the audio devices under JUDY's mic. Re-disabling needs admin.
- **JUDY:** finds a running `judy.py --session`, or starts one. It stops a standalone JUDY first (same hotkey).
- **FACES (10/4):** starts JUDY's console (:8787, `--no-open`) if down, then opens the face deck (`/faces`) as a browser tab.
- **DECK (ruled 10/6):** opens the Traffic Deck (`/traffic`) as its own window, like the face deck. It shows JUDY's last five replies in tabs, the open calls with Take rec and answer boxes, Take all recs, and the net chart.
- **KNOBS:** starts `knobs.py --run` (the MPK knobs as scroll and zoom, BOLO 62) unless one is running.
- **WIRE:** runs `wire_probe.py` for the seven tools.
- **SITREP and SOI:** opens both as tabs in the default browser (Chief, 9/20: never the Edge app window).

**THE BOOT SCREEN (Chief 10/17, "really cruncy arc linux boot sequence looking with an ascii logo of bold venture"; BOLO 153's first screen):** `launch.py` opens `_tools/launch/boot.py` in its own console window and writes each station's start and finish to `boot.jsonl`. The window draws the BoldVenture mark, an initramfs-style preamble, then one `[  OK  ]` / `[FAILED]` row per station with filling dots and the detail column. ALL GO closes it after 10 s; a NO-GO keeps it open until Enter. `--no-boot` skips it; `--json` never opens it.

It prints the station poll:

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

Keep the poll verbatim. Report a NO-GO and never retry it in a loop. The sit rep still runs.

**PULL + THE GLASS (BOLO 137, Chief 10/12: "give me regular updates please have that be part of the process" · "run the process at the beginning with the glass whenever we run the launch sequence"):** `launch.py` runs station **PULL** right after AUDIT, at zero tokens.
- It runs `pull_queue.py report` for the wave lines.
- It runs `pull_glass.py` to build the glass at `_PRIVATE/reference/pullqueue/pull-queue.html`.
- It starts any stopped runner (PullRunnerA/B). Standing order 10/12: the waves run until the queue is empty. A Startup-folder `pull_start.cmd` also starts them at logon.
- It reports NO-GO only on a stalled wave.

The main line then does two things:
1. Publish that file to the standing URL, `pages.json` "pullglass" (https://claude.ai/artifact/Lg323uYY1oB2HCfgHFDFQ6). In a new session, pass it as `url`. The first publish may be refused unread. The glass is generated, so resend once after the saved copy is acknowledged. The pages station opens it as a tab.
2. If any wave is live, arm ONE CronCreate every 30 min, at minutes 7 and 37 (Chief 10/12). Run CronList first. Its prompt runs the report, rebuilds the glass, republishes it and posts a short update.

Any turn that starts a wave arms the same job. The job deletes itself when the pull goes idle. It never starts or kills a wave.

**THE ROSTER (BOLO 139, Chief 10/12: "a roster file that can pop up with the sitrep at the launch sequence"):** the pages station opens the Roster (`pages.json` "roster") with the boards. If `.claude/agents/` changed since the last launch, run `python _tools/roster/build.py`. Then republish `_tools/roster/roster.html` to that URL.

**THE ARMORY (BOLO 154, Chief 10/17: "sure add armory to launch"):** station **ARMORY** starts `_tools/armory/armory.py` detached (~40 s), so the launch does not wait on the transcript scan. After the sit rep publishes, republish `_PRIVATE/reference/armory/armory.html` to `pages.json` "armory" (https://claude.ai/artifact/RYyy6zNoAHMaTTxBZoV9Hn). The pages station opens it with the boards.

## 2 · The sit rep

Run the `sitrep` skill exactly as written: prep, three specialists at gear 1, assemble, then build, flush, publish. The launch does not change the formation.

## 3 · The reply

Open with the station poll in a fenced block. Then write two lines before anything else (ruled 10/6, Chief: "one of the first things you'll say to me … is what we left off last time and what I think we should start on next … which BOLO"):
- `**Left off:**` one sentence from the last session's note: the last thing worked and where it stopped.
- `**Start next:** BOLO N`: the one row you recommend, with a five-word why.

The spoken line says both. Then give the sit rep reply as the sitrep skill specifies: the link, Block 0 in three bullets, the leverage line, and one caveat line if any. The spoken line (SOP §7 rule 10) opens the reply and names any NO-GO.

History and measurements: references/history.md
