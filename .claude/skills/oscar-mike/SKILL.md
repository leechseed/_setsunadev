---
name: oscar-mike
description: 'Use when Chief closes out the session: "Oscar Mike" or "we''re Oscar Mike".'
---

# Oscar Mike, the close-out

The procedure lives in the driver script (BOLO 155 M7, 10/18). Run each phase and do exactly what its `NEXT` lines say. Pass this session's id prefix: two sessions run at once.

```
python _tools/oscarmike/run.py <sid>          # stations down, prep, then the H1 order
python _tools/oscarmike/run.py note <path>    # after NOTE drafts: the header, then your judgment
python _tools/oscarmike/run.py out            # journal, stage the next launch, the proofs, the reply
```

## The doctrine

- One specialist: `drafting-session-note`, launched **by name** with its brief verbatim. No second specialist; the journal and the staging are scripts. The STATE Moved bullet is the main line's.
- The note is the wire, STATE is the index. Never paste the transcript into the note. Private detail stays in `_PRIVATE/`.
- The session is done when this runs; nothing is parked into a card.
- **Verify before done:** the reply claims only what a command proved this turn (`run.py out` prints the proofs). Anything else is left out or marked unchecked.
- **The handoff shape:** ground the note in `git status`, mark verified versus `[UNVERIFIED]`, keep decisions and dead ends, give each open loop an owner and a check, end with one exact next action.

## The reply

The STATIONS DOWN block, then the OUT block (SOP §7 rule 9), and nothing after it.

The pre-M7 skill text is in `references/SKILL.pre-M7.md`.
