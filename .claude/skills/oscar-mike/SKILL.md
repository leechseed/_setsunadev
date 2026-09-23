---
name: oscar-mike
description: Run the close-out ("Oscar Mike", ruled 9/11) in the formation (BOLO 51 phase 2.2) — a script pulls the session's spoken turns from the local transcript, a Payload Specialist (PS, haiku) drafts the Ready Rack note, a script appends the journal, the main line rules the note and writes STATE's Moved bullet, then the OUT block. Fires on "Oscar Mike" or "we're Oscar Mike".
---

# Oscar Mike — the close-out

**Steps (BOLO 64, provisional 9/23):** RECON = `close.py` pulls the session's spoken turns · ORDER = the note brief to the PS · EXECUTE = the PS drafts, the script appends the journal · CONSOLIDATE = the main line rules the note, STATE's Moved bullet, the OUT block.

Canonical: SOP.md §1 (the command) · §3 (the Ready Rack) · §7 rule 9 (the OUT block). The session is done when this runs; nothing is parked into a card.

## H-1 · Stations down (zero tokens) — the closing sequence, BOLO 58, Chief 9/17

```
python _tools/launch/shutdown.py
```

The reverse of the launch sequence: the board windows (the sit rep page, the SOI) closed · JUDY session voice stopped · the DARKROOM server stopped. The wire and Stash stay. Keep the printed STATIONS DOWN block for the reply, above the OUT block's paragraph. A STUCK station is reported, not retried.

## H0 · Prep (zero tokens)

```
python _tools/oscarmike/close.py
```

Finds this session's transcript (or pass the session id prefix), writes `_tools/oscarmike/work/<date>/transcript.md` (Chief's turns in full, Claude's replies trimmed, tool traffic dropped), `meta.json`, and `brief.NOTE.md`. Prints the note's target name (today's note, or `-2`, `-3` if today already closed one; an open note from this session is finalized, not replaced).

## H1 · One specialist

Launch **NOTE** (haiku) with the brief verbatim. It writes the session note into `_CACHE/` in the Command shape (transmission · built · ruled · measured · memory · **Open at close** · **AAR** · `- Oscar Mike.`). It reads nothing else and touches nothing else.

## H2 · The main line's judgment (~3 KB read)

1. Read the drafted note. Correct only what is wrong (a misquote, a missing ruling, a file path). Do not rewrite the register.
2. Write STATE.md's Moved bullet for the day (`## ✅ Moved <date> (…)` section: add or create), and touch the Live row and any Blocked row the session changed. This is the one write that needs the session's judgment.
3. If a memory was earned this session (a correction, a confirmed way of working, a project fact not in the repo), write it now.

## H3 · Journal, then out

```
python _tools/oscarmike/journal.py
```

Appends the note's bullets under a timed header to `_devlog/_devlog_docs/_devlog_journals/MMDDYYYY.journal.md` (idempotent per note). The reply carries the STATIONS DOWN block, then ends with the OUT block (SOP §7 rule 9) and nothing after it. Autocommit fires on stop.

## Rules

- The note is the wire, STATE is the index: detail goes in the note, the index line goes in STATE.
- No second specialist. The journal is a script. The Moved bullet is yours.
- If the transcript is enormous, the prep script keeps the tail; the head is in the earlier notes already.
