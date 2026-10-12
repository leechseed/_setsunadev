# Yo-yo first real run (BOLO 69), 2026-10-12

Idea used: "ten editing books for DaVinci, one process, a Zotero shelf" (from BOLO 136). Run by text, not by the pad.

What it showed:
- The trick works end to end: yo-yo 3 was written, with title, refined text and Pepper's opener. Took 7.3 s, $0.016, 197 tokens out.
- Cache cost is high on a cold call: 78.7k tokens written, 0 read. The earlier run wrote 57.8k. A gap over an hour means every trick pays full.
- The opener asks one question (which stage should book one teach you cold). It is useful and short. It did not give the three follow-ups the row promises (workflow fit, method question, "yes, and").
- The wind (plan, implement, commit) does not exist yet, so all three yo-yos stay unwound (3 of cap 12).
- Not tested: the pad itself, the ears (Whisper), the spoken ack, the visible stack window.
- Yo-yos 1 and 2 are old test runs; 1 is just "note 40", a pad-learn leftover.

Open call: build the three follow-ups, or the wind first? Rec: the three follow-ups, since the row promises them and Chief meets them first.

## Follow-ups built (2026-10-12, "take all recs")

- New command: `python _tools/yoyo/yoyo.py followups N`. It reads yo-yo N and appends a "Follow-ups" section with the three the row promises: (1) where it fits in a production workflow, (2) a question by a method, (3) a "yes, and". It sets `tricks: 2` and logs its own time and cost. It refuses to run twice on one yo-yo. Backup: `yoyo.py.bak-followups`.
- Method stand-in: Chief has not named his method, so (2) uses the five whys. Change `FOLLOWUPS` in yoyo.py when he names it.
- Run on yo-yo 3: 7.9 s, $0.0035, 219 tokens out. The cache was warm (66k read), so it cost a fifth of the first run. All three came back well formed.
- Not wired: `trick` does not call `followups` itself. Two separate calls keep the first ack fast. Joining them is one line if Chief wants it.
- Still not built: the wind (plan, implement, commit), the pad test, the ears, the stack window.
