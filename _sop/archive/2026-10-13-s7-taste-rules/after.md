### 7.23 · The copy self-audit
Every deliverable gets one pass before it goes out, checking four things: slop words, filler openers, fake precision (a number with no measurement behind it), and claims with no source. The `prose-taste` agent and `_tools/prose/prose_lint.py` run the same list.
- **WHEN** Claude finishes a deliverable (page, note, brief, spec) **THEN** it makes one pass for those four things and fixes or cuts each hit before handing it over.
<sub>Ruled 2026-10-13 · provisional · BOLO 140 (taste-16, taste-17)</sub>

### 7.24 · Fake precision
A number appears only when something measured it. Otherwise the word stands: about, a few, most.
- **WHEN** Claude writes a figure with no measurement behind it **THEN** it replaces the figure with a word, or names the file, command or source that measured it.
<sub>Ruled 2026-10-13 · provisional · BOLO 140 (taste-17)</sub>

### 7.25 · Deliverables are complete
Deliverables carry no placeholders and no truncation. Replies stay under the Spartan dial (7.6) and are exempt.
- **WHEN** Claude hands over a deliverable (file, page, script, spec) **THEN** it contains no "TODO", "rest of code", "for brevity" or "..." standing in for content, and every requested item is built in full.
- **WHEN** Claude writes a reply to Chief **THEN** the Spartan dial governs and this rule does not apply.
<sub>Ruled 2026-10-13 · provisional · BOLO 140 (taste-05, taste-17)</sub>
