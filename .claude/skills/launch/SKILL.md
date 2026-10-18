---
name: launch
description: Use when Chief says "go for launch", the garbles "go for log" and "go for lunch", or "launch sequence", "start launch sequence" or "run launch sequence" spoken alone. Never on "go N".
---

# The launch sequence (BOLO 58)

Ask no questions and write no preamble. The procedure lives in the script (BOLO 155 M7, 10/18): run it and do exactly what its `NEXT` lines say.

```
python _tools/launch/launch.py
```

**Run it from the Bash tool, never the PowerShell tool** (confirmed 9/20): PowerShell-tool children sit in a job object and JUDY's paste into VS Code stops landing. The same goes for any JUDY relaunch.

## What the script does (zero tokens)

AUDIT first (Chief 10/6), then PULL, ARMORY, DARKROOM, STASH, NAHIMIC, JUDY, FACES, DECK, CONSOLE, KNOBS, WIRE, FRAGO and the board pages. It opens the boot screen window (Chief 10/17: the BoldVenture mark, Arch-style rows, the per-wave pull lines, the budget line), prints the station poll, then prints the NEXT lines: what to publish where, whether to arm the pull report, whether the Roster needs a rebuild, the sit rep, and the reply shape.

## Standing rules

- `mirror.py --check` runs on Chief's word only; a page with changed headings is a call for Chief before any skill or hook edit (10/13).
- An AUDIT NO-GO (private detail in a public file, a stale BOLO row, an old note on the rack) goes in the reply's caveat with "clean your station". Retired words and the tree are advisory.
- The pull waves run until the queue is empty (standing order 10/12); the 30-minute report never starts or kills a wave.

The pre-M7 skill text (every station in detail) is in `references/SKILL.pre-M7.md`; history and measurements in `references/history.md`.
