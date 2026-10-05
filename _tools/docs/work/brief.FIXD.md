# BOLO 102 · batch D · the factual contradictions · brief (MS)

Repo root: C:\Users\U01_LEECHSEED\Desktop\_setsunadev. Write UTF-8, keep each file's line endings.

Chief ruled 10/5: "All recommendations." The facts pass found sources that contradict themselves. Each call below is RULED as written. Land each one in the SOURCE doc (`ShroomsQ/_CANON/_SSOT/...`), bump that doc one patch level with one history line in its own layout (`BOLO 102 batch D (Chief: "All recommendations"): <what>`), then on its core-doc pages (`ShroomsQ/_CANON/_DOCS/<system>/<doc>/`) replace the matching `> **OPEN:** …` line with the corrected fact and set `source_version`.

## The calls

1. **Module architecture · "requires no other module" vs Cross-Module Dependencies.** The dependencies section wins: a module may depend on another, through its declared `depends_on`. Reword "requires no other module" to "a module runs without any module it does not declare in `depends_on`".
2. **Module architecture · Creation step 2 "next deliverable".** Replace the phrase with the registry pointer its 1.0.1 note names.
3. **Variable registry · `DRV.truth_exposure_index` display formula `10 - shame_index`.** The internal formula and the base 60 doc use `12 - shame_index` (the 0–12 range, ruled 10/4). The display formula becomes `12 - shame_index`.
4. **Trope register · wave B "2,175 keys" vs parts summing to 2,195.** Check against `_tools/tropes/data/domains/register.json` with a short Python count. The number the data shows wins; if the data is not countable that way, the parts' sum (2,195) wins.
5. **Step 1 source verification · check 2.3 `story_limit`.** Rename to `limit_type` (the ingest template's name since 1.0.2).
6. **Setting system · scene card "Ten fields, one screen".** It lists twenty-four. Count the fields yourself; the count wins.
7. **Trope graph · "Love sits in seven of the ten pairs".** Its own table shows six. Count the table; the count wins.
8. **Trope graph · "Propp has no BVX id".** Its OPEN call 5 minted BVX.1136. The body cites BVX.1136.
9. **Theme system · "write the four steps worst to best" vs lists running best to worst.** The lists are canon and stay. The instruction becomes "best to worst" (positive first, the negation of the negation last).
10. **07.1 prose style · body recs still say "YA-adjacent" and "opt-in per IP".** Its OPEN calls 3 and 4 struck both. The body recs follow calls 3 and 4.
11. **The interface catalog's own pages (00) · four OPEN lines about ids renumbering and closed wirings.** The build was fixed on 10/5: ids never change once published (new rows take the next number), and a pair leaves THE WIRING FINDINGS when the silent side names it. Replace those four OPEN lines on `ssot_00_interface_catalog/2-reference.md` and `3-how-to.md` with the fixed behavior. The catalog source is generated: do NOT edit `📐 ssot_00_interface_catalog.md`.

## Rules

- Only what each call says. 20 words per sentence; every sentence names who acts.
- Do not consult other agents.

## Reply

Two lines: calls landed (numbers) · docs bumped (name → version), and any call where the count changed the ruling's number.
