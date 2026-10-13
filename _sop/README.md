# _sop · how the SOP changes (borrowed from OpenSpec, trial ruled 10/12, BOLO 139)

SOP.md is the living doctrine: it always reads as the current rules, never as a pile of appended notes.

A change to the SOP goes through a folder, not an edit in place:

1. **Propose:** `_sop/changes/<date>-<name>/` holds `proposal.md` (why, what changes, a list of ADDED / MODIFIED / REMOVED rules) and `after.md` (the section as it should read). `before.md` keeps the section as it was.
2. **Apply:** the section in SOP.md is replaced with `after.md`.
3. **Archive:** the folder moves to `_sop/archive/`. The archive is the history; SOP.md stays clean.

Every converted rule has the shape:

```
### 7.N · <short name>
<the rule: what Claude does, 1–3 plain sentences>
- **WHEN** <trigger> **THEN** <observable result>
<sub>Ruled <date> · <source></sub>
```

`_tools/audit/sop_audit.py` (finding class S) flags any `### N.n` rule without a WHEN/THEN line. Converted so far: §7 (10/12).
