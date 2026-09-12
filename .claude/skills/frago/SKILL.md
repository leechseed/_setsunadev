---
name: frago
description: Push a fragmentary order onto DOPE SHEET N (FRAGO N, ruled 9/11) without rewriting the sheet — pure script (BOLO 51 phase 2.3): the main line writes a ~1 KB patch, frago.py merges it, bumps the version, builds; publish to the sheet's standing URL. Fires on "FRAGO N", "update the sheet for N", "push that onto N".
---

# FRAGO N — the update

Canonical: SOP.md §1. A FRAGO carries only what changed; everything not mentioned stands as ordered; the Log keeps every FRAGO. No agent is involved.

## 1 · Write the patch (the only judgment)

Write `<scratchpad>/fragoN.json` with only the keys that changed. All optional:

```json
{
 "status": "the new header line",            "s": "hot|open|held|gated|done",
 "order": "the new next action",             "default": "Silence: …",
 "calls":  [{"q": "prefix of an existing q, or a new one", "s": "ruled", "ruling": "…"}],
 "phases": [{"n": 4, "s": "done", "when": "9/12", "t": "…"}],
 "files":  [{"path": "…", "what": "…", "s": "done"}],
 "items":  [{"p": "S", "label": "group label prefix (new label = new group)", "t": "…", "s": "done"}],
 "strand": {"E": {"you": "…", "next": "…"}},
 "log":    [{"who": "Papi", "t": "what was said"}, {"who": "Claude", "t": "what was done"}],
 "related":[{"n": 54, "why": "…"}]
}
```

Rules of the merge: calls match by `q` prefix, phases by `n`, files by `path`, items append to the named group, log entries are dated today, `asof` becomes today, the version bumps (v0.2 → v0.3). Never edit `boards/N.json` by hand for an update; the patch is the record.

## 2 · Merge and build

```
python _tools/bolostatus/frago.py N <scratchpad>/fragoN.json --build
```

Prints the change list and the fragment path. If the build reports a missing glossary key, add the key and rerun.

## 3 · Publish

Publish the fragment with the Artifact tool, passing the sheet's URL from `_tools/pages/pages.json` as `url`, with a short `label` ("v0.3 · what changed"). **The cross-session gate (measured 9/12 on sheet 51):** a publish to a sheet this session did not build is refused until the live page has been fetched in this session with the Artifact tool's `read` action on the URL (a saved copy handed back by a refusal does not count, even after Reading all of it). The fetch puts the whole page (~80 KB, about 65k tokens) into context; a second refusal can demand it again. That is more than the FRAGO itself costs by two orders of magnitude, so: **build locally, record the change, and leave the republish to the session that built the sheet, or to Papi's standing `force` order for sheets built from repo JSON (a call on DOPE SHEET 51; `force` needs his explicit word each time until ruled).** If the sheet was built in this session, none of this applies: publish with `url` and it lands. The reply: the link (or "built locally, republish owed"), the change list in one line.
