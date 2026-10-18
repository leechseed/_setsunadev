---
name: oscar-mike
description: 'Use when Chief closes out the session: "Oscar Mike" or "we''re Oscar Mike".'
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

Launch **NOTE** as the agent `drafting-session-note` (haiku; by name, never general-purpose, BOLO 155 M2) with the brief verbatim. The brief opens with its `JOB:` line; the reply ends with a status line (DONE, DONE_WITH_CONCERNS, NEEDS_CONTEXT or BLOCKED). It writes the session note into `_CACHE/` in the Command shape (transmission · built · ruled · measured · memory · **Open at close** · **AAR** · `- Oscar Mike.`). It reads nothing else and touches nothing else.

## H2 · The main line's judgment (~3 KB read)

1. Read the drafted note. Correct only what is wrong (a misquote, a missing ruling, a file path). Do not rewrite the register.
2. Write STATE.md's Moved bullet for the day (`## ✅ Moved <date> (…)` section: add or create), and touch the Live row and any Blocked row the session changed. This is the one write that needs the session's judgment.
3. If a memory was earned this session (a correction, a confirmed way of working, a project fact not in the repo), write it now.

## H3 · Journal, then out

```
python _tools/oscarmike/journal.py
```

Appends the note's bullets under a timed header to `_devlog/_devlog_docs/_devlog_journals/MMDDYYYY.journal.md` (idempotent per note). The reply carries the STATIONS DOWN block, then ends with the OUT block (SOP §7 rule 9) and nothing after it. Autocommit fires on stop.

## H4 · Stage the next launch (BOLO 86, ruled 10/12, provisional)

```
python _tools/oscarmike/stage_next.py
```

Writes `_tools/launch/next.json`: the leverage line from the newest board, every DOPE SHEET touched today, and the note's Open-at-close bullets. `launch.py` reads it and FRAGOs each named sheet before the boards open. Run it after H3, before the OUT block.

## Verify before done

The close claims only what a fresh command proved this turn. Before the OUT block, run the proving command for each claim (the file exists, the journal line is there, the commit landed, lint reads 0 errors), read its output, then write the claim. A claim with no command run this turn is left out or marked unchecked.

## Lessons

One bullet per correction Chief made this session, written into the note under its own heading. Each bullet: what I did, what he corrected, the rule in one line. Three or more of the same kind become a memory or SOP candidate (SOP spit rule).

## Rules

- The note is the wire, STATE is the index: detail goes in the note, the index line goes in STATE.
- No second specialist. The journal is a script. The Moved bullet is yours.
- If the transcript is enormous, the prep script keeps the tail; the head is in the earlier notes already.

## The handoff shape

What a note must carry so the next session resumes cold (the note stays the wire, STATE the index):

1. **Ground in the repo, not the chat.** Read `git status -s` and `git diff --stat` before writing; list files touched from that output.
2. **Goal in one sentence, then verified versus partial.** A thing is verified only if a command ran this session and passed; anything else is marked `[UNVERIFIED]`.
3. **Decisions and dead ends.** Each ruling with its reason, plus every approach tried and dropped, so nobody retries it.
4. **Open loops with an owner and a check.** Each names Chief or an agent and the command or file that shows it closed.
5. **One next action.** The exact file or command to start on, never "continue the work".

Never paste the transcript into the note.

<sub>Source: sickn33/agentic-awesome-skills skills/session-handoff (alapha888/session-handoff-kit), MIT. Adapted in our words, BOLO 140.</sub>
