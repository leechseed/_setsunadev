---
name: rtb
description: Run the card-clearing pass ("RTB", ruled 9/10) in the formation (BOLO 51 phase 2.6) — a script compiles every open card in oscar-mike/ with its resume lines, a Payload Specialist (PS, haiku) proposes one disposition per card, the main line rules the lines and executes. Fires on "RTB", "RTB oscar-mike", "clear the cards", "send the cards home".
---

# RTB — return to base

Canonical: SOP.md §1. RTB keeps one meaning: the pass that sends a parked card home (promote · delete · keep) and clears the folder. It retires itself when `oscar-mike/` is empty.

## H0 · Prep (zero tokens)

```
python _tools/oscarmike/rtb_prep.py
```

Writes `_tools/oscarmike/work/rtb/cards.md` (every open card: handle · title · parked · tags · status · its own resume/decision lines) and `brief.DISPO.md`.

## H1 · One specialist

Launch **DISPO** (haiku) with the brief verbatim. It writes `dispositions.md`: one line per card, `PROPOSE: PROMOTE → <home file> | DELETE | KEEP`, with one clause of why. It edits nothing.

## H2 · The ruling (the main line, ~22 lines read)

Read `dispositions.md`. For each line, rule it or defer it to Papi when the card holds an open decision that is his (a ruling, a purchase, a send). The reply lists the rulings as a table: handle · disposition · where it went. Papi's word overrides any line.

## H3 · Execute

- PROMOTE: move the keeper content into its home (STATE / PROJECTS / the build dir / the canon node), add a one-line receipt to the card's INDEX row (`✅ RTB <date> — promoted → <path>`), delete the card file.
- DELETE: receipt on the INDEX row, delete the file.
- KEEP: leave the card, add the named resume event to its INDEX status.

Update `oscar-mike/INDEX.md` in one pass, STATE's Moved bullet in one line, the session note. Never launch a second agent to check the first; a wrong line is re-ruled by you.
