# BOLO 102 · batch A · fix the source · brief (MS, one per slice)

Repo root: C:\Users\U01_LEECHSEED\Desktop\_setsunadev. Write every file as UTF-8.

Chief ruled 10/5: "All recs go". Each call below is now RULED. You apply the calls in YOUR SLICE (listed in your prompt) and nothing else.

## For each call

1. **Fix the source doc** in `ShroomsQ/_CANON/_SSOT/<system>/`. Change only what the call says. Keep the doc's voice and layout.
2. **Bump the source's version** (patch level, e.g. 1.2.1 → 1.2.2) in its front matter, and set its updated / last_updated date to 2026-10-05 if it has one.
3. **Add one version-history line** at the top of its history: `- **x.y.z · 2026-10-05** — BOLO 102 batch A (Chief: "All recs go"): <what changed, one line>.`
4. **Fix the matching core-doc pages** under `ShroomsQ/_CANON/_DOCS/<system>/<doc>/`: delete the `> **OPEN:** …` line for this gap, correct the fact on the page if the page stated it, and set `source_version` to the new version on all four pages of that doc.
5. Find the OPEN lines with: `_tools/docs/out/open_gaps.json` (each gap has its number `n`, file and line).

## Rules

- Change nothing a call doesn't name. No other rewording.
- Sentences you write: 20 words at most, every sentence names who acts (DOC-SOP 3.2).
- If a call turns out wrong once you read the source (e.g. the table you were told wins is itself broken), do NOT apply it: leave the OPEN line and report it.
- Do not edit outside your slice. Do not consult other agents.

## Reply

Three lines at most: calls applied (by gap number) · docs bumped (name → version) · any call not applied and why.
