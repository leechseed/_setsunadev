# _YOYO — the inbox for the idea that springs

BOLO 69. One file per yo-yo, numbered, newest last. A yo-yo is a flash Chief spoke into
the yo-yo pad on the MPK (top-left, far from talk / focus / send). The pad's script is
`_tools/yoyo/yoyo.py`; the page it writes is the one you are looking at in this folder.

**The words.** The *trick* lays an idea down: the raw text as the ears heard it, a readable
rewrite, and Pepper's opener for the explore phase. The *wind* stores it properly, through
plan → implement → commit, cross-referenced to the spine and the other tables. Until then a
yo-yo is *unwound*, and unwound yo-yos count against a cap (twelve, provisional).

**The phases** (ruled 9/18, from Claude Code's best practices): explore → plan → implement
→ commit. Every page names the phase it is in.

**Front matter** on every file: `yoyo` · `when` · `state` (unwound · wound · overflow) ·
`tricks` · `phase` · `title` · the ears' seconds · the run's tokens, cost and seconds.
The numbers are on the page so the F1 line — least tokens, least time — is always visible.

    python _tools/yoyo/yoyo.py count        # unwound against the cap
    python _tools/yoyo/yoyo.py show 12      # one yo-yo
    python _tools/yoyo/yoyo.py trick "…"    # a trick from text (the pad does this by voice)
