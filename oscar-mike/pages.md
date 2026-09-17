---
title: The Pages — SITREP · OPORD/FRAGO · SOI (BOLO 38 and its siblings)
type: parked work
status: CHARLIE MIKE'D 2026-09-11 — steps 1–4 done; step 5 (names) Chief's; step 6 (refactor) deferred to the next page. Card stays until step 6 lands or is struck; RTB then
updated: 2026-09-10
trunk: BLACK (the board's own tooling; every trunk rides on it)
pointer-only: false — the resume order below is the whole handoff
open_on_resume: the OPORD/FRAGO retitle · the SOI publish + re-point · the sit rep board's BOLO 45 deltas · the READYROOM / MINT names · the OPORD word (provisional)
---

# THE PAGES — parked 2026-09-10 late

**What it is.** On 9/10 evening Chief ordered the board off the chat scroll and onto pages: the sit rep as a dashboard (BOLO 38), a per-BOLO status page in the five-paragraph order, and the house tongue as its own book. Three pipelines now exist, all on the same core (colorway, tooltip engine, glossary), each a data file plus a template plus a build script.

**Standing links.**
- Sit rep: https://claude.ai/code/artifact/aebe5f9c-9f2c-4cb8-abbf-714a0a6ea28a — v0.4 live (FRAGO · TTP · RTB · Charlie Mike in the SOI card; glossary still opens in-page).
- BOLO 45 page: https://claude.ai/code/artifact/9d12db54-dc85-4221-8868-bc26d132e1f6 — v0.1 live (stale: does not yet show scope M or the five landed cases).
- SOI: **published 9/11** https://claude.ai/code/artifact/4c2fc9c7-e0d2-4626-8142-9740ff8ee0e5 (edition 2026-09-11-1). Both page templates link to it; the in-page views are gone.
- OPORD 38: https://claude.ai/code/artifact/414c9a5c-c320-4e09-9d3f-4d4c6bd0acbd · OPORD 42: https://claude.ai/code/artifact/134d6364-1825-4088-a737-ca7bf16ea557
- (was) SOI: not yet published. `_tools/soi/` is written; `python _tools/soi/build.py` produces `SOI.html` at root; first publish needs a favicon.

**Rulings that landed on this line, 9/10.**
- The page becomes the board (BOLO 38). The explainer register on every panel. Skin: CK3 IA × Death Stranding surface.
- The colorway: the creator-cases explainer palette for every internal board; the rose stays with DARKROOM and public-facing work.
- **SOI** = the tongue's book, its own dashboard: search, A to Z, by section, Marine SOI format (edition · effective · supersedes · authentication · codebook · changes).
- **OPORD N** = the standing BOLO page (provisional word); **FRAGO N** = the update pushed onto it (ruled). Chief: "I thought FRAGO was just the update after we've made the BOLO status page." The Log keeps every FRAGO.
- The three that govern the BOLO page, from MIL.01 §4 / invariant 8: SPEED · FOCUS · BOLDNESS.
- TTP for the lessons block (over GOUGE) · RTB replaces sweep · Charlie Mike resumes a card · scope M on BOLO 45 (ruled in the parallel session, folded into `boards/45.json`, not yet rebuilt).

**Where the substance lives.**
- [_tools/sitrep/](../_tools/sitrep/) — `boards/2026-09-10.json` · `glossary.json` (the shared register, 90+ terms; the parallel session edits it too — re-read before writing) · `template.html` · `build.py` → `SITREP.html` at root.
- [_tools/bolostatus/](../_tools/bolostatus/) — `boards/45.json` · `template.html` · `build.py` → `out/BOLO-45.html`.
- [_tools/soi/](../_tools/soi/) — `soi.json` (edition, sections, authentication, changes) · `template.html` · `build.py` (parses SOP §8 live) → `SOI.html` at root.
- SOP §1 (the sit rep row, the OPORD/FRAGO row) · §2 (the front-page rule, the colorway, the glossary page) · §8 (garbles: me this it rep · Rebel Writer · desk training · CK three · Frango · Ebola).
- Memory: `sitrep-front-page` · `default-colorway`.

**Resume order (Charlie Mike pages).**
1. **Retitle for the OPORD/FRAGO split:** `_tools/bolostatus/template.html` masthead `FRAGO · BOLO` → `OPORD · BOLO`; `build.py` title `FRAGO {n}` → `OPORD {n}`; `boards/45.json` `version` → `v0.3 · OPORD` and its Log entries stay as FRAGOs. Glossary already carries `opord` (provisional) and `frago` (the update).
2. **Rebuild + republish BOLO 45** (`python _tools/bolostatus/build.py 45`, publish with its URL) — the scope-M deltas are in the board already.
3. **Fold the same deltas into the sit rep board** (`boards/2026-09-10.json`: Block 0 · Block I item 1 · Block IV hot 45 · Block V item 3 → the case-set size question; agents in flight = the wave-one seven if still running, else 0), rebuild, republish.
4. **Build + publish the SOI** (`python _tools/soi/build.py`; favicon on first publish; title SOI). Then re-point both page templates: the GLOSSARY button becomes an outbound `SOI` link to the SOI URL, the in-page glossary view and the G key go; rebuild and republish both. Patch SOP §0 (SOI is now also the page) and the glossary `soi` entry.
5. **Names still Chief's:** READYROOM (the sit rep program) · MINT (the loop, BOLO 37) · OPORD (confirm the word).
6. **Refactor owed, not urgent:** the three templates share ~300 lines of CSS and the tooltip engine by copy; extract `_tools/sitrep/house.css` + `house.js` when the next page is added.

**Lessons banked.** Check the other sessions before declaring a file dead (the 16:00 false alarm). A peer session's autosave commits your untracked files mid-turn; that is fine but means "not yet committed" is never a safe assumption. Long heredocs die in Git Bash; scripts go to the scratchpad. Every `[[key]]` in a board must exist in `glossary.json` or the build fails on purpose.
