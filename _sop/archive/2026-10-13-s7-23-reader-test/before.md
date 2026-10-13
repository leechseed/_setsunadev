### 7.23 · The copy self-audit
Every deliverable gets one pass before it goes out, checking four things: slop words, filler openers, fake precision (a number with no measurement behind it), and claims with no source. The `prose-taste` agent and `_tools/prose/prose_lint.py` run the same list.
- **WHEN** Claude finishes a deliverable (page, note, brief, spec) **THEN** it makes one pass for those four things and fixes or cuts each hit before handing it over.
<sub>Ruled 2026-10-13 · provisional · BOLO 140 (taste-16, taste-17)</sub>

