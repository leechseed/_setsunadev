# creator-cases — the case-file tooling (RTB'd from oscar-mike 2026-09-10)

- `case-brief.md` — the shared agent brief for one creator case (BOLO 45 wave one). Reuse for wave two and the lane-C list: give each agent this file, the SUBJECT, the SLUG, and the register row.
- `land.py <slug> <register name> <note> <xhandle> [sex]` — after a case file lands: renames a leftover `## N · GOUGE` header to TTP and applies the row's note + X handle (+ sex if the cell is a dash) to `_CANON_NODES/performer-register.md`. Agents never touch the register; this does.
- The files live in `_CANON_NODES/creator-case-<slug>.md`; the synthesis and the venture read-across in `_PRIVATE/`; the board in BOLO.md row 45 and STATE.md.
