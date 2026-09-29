#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BOLO 79 (RULED 2026-09-29, "all recommendations") — the tracking-file loader.

Reads ONE tracking file per story (ssot_08 format) —
  ShroomsQ/_CANON/_TRACKING/<story>.yaml
— validates every time code against that file's own `scenes:` list, resolves
every trope slug against the trope register, and returns one JSON-able dict
that build.py embeds for the Told lens (The Arrangement).

`load` only READS the tracking file; `pull` (step 6, RULED 2026-09-29) folds the page's
edits into it per _tools/bolostatus/work/90/EDIT-CONTRACT.md.

Grammar (ssot_08 §4): M<n> · Q<n> · S<nn> | bar.beat[.tick]
  - the M · Q · S must name a scene in `scenes:`
  - bar must sit within that scene's own bar count
  - beat must sit within that scene's own meter (the numerator of `sig`)
  - tick has no fixed ceiling (ssot_08 §3) — only checked to be >= 1 when given
  - a trailing "⧗" (proposed, not ruled canon) is stripped before parsing

Fails loudly (SystemExit) on a bad time code or an unregistered trope slug,
per the tasking order — never silently drops or guesses.
"""
import json
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[2]
TRACKING_DIR = ROOT / "ShroomsQ" / "_CANON" / "_TRACKING"
REGISTER = ROOT / "_tools" / "tropes" / "data" / "domains" / "register.json"

# M<n> · Q<n> · S<nn> | bar.beat[.tick]  (the "·" is U+00B7, as written in the tracking file)
CODE_RE = re.compile(
    r"^\s*(M\d+)\s*·\s*(Q\d+)\s*·\s*(S\d+)\s*\|\s*(\d+)\.(\d+)(?:\.(\d+))?\s*$"
)


def _strip_provisional(text):
    """⧗ marks a value as proposed, not ruled canon (ssot_08 conventions) —
    strip it before grammar-checking the time code underneath it."""
    return (text or "").replace("⧗", "").strip()


def _load_register():
    if not REGISTER.exists():
        raise SystemExit(f"tracking.py: trope register not found at {REGISTER}")
    with REGISTER.open(encoding="utf-8") as f:
        return json.load(f)


class _CodeIndex:
    """Parses and validates ssot_08 time codes against one story's `scenes:`."""

    def __init__(self, scenes, story):
        self.story = story
        self.by_key = {}
        for i, sc in enumerate(scenes):
            for req in ("mv", "q", "s", "bars"):
                if req not in sc:
                    raise SystemExit(f"tracking.py [{story}]: scenes[{i}] is missing {req!r}")
            num, den = self._sig(sc.get("sig", "4/4"), f"scenes[{i}]")
            key = (sc["mv"], sc["q"], sc["s"])
            if key in self.by_key:
                raise SystemExit(
                    f"tracking.py [{story}]: duplicate scene {key[0]} · {key[1]} · {key[2]} in scenes:"
                )
            self.by_key[key] = {**sc, "num": num, "den": den}

    @staticmethod
    def _sig(sig, where):
        parts = str(sig).split("/")
        if len(parts) != 2 or not all(p.isdigit() for p in parts):
            raise SystemExit(f"tracking.py: bad time signature {sig!r} at {where} — want num/den, e.g. 7/8")
        return int(parts[0]), int(parts[1])

    def check(self, raw_code, where):
        code = _strip_provisional(raw_code)
        m = CODE_RE.match(code)
        if not m:
            raise SystemExit(
                f"tracking.py [{self.story}]: BAD TIME CODE {raw_code!r} at {where} — "
                f"grammar is M<n> · Q<n> · S<nn> | bar.beat[.tick] (ssot_08 §4)"
            )
        mv, q, s, bar, beat, tick = m.groups()
        key = (mv, q, s)
        sc = self.by_key.get(key)
        if sc is None:
            raise SystemExit(
                f"tracking.py [{self.story}]: BAD TIME CODE {raw_code!r} at {where} — "
                f"no scene {mv} · {q} · {s} in scenes:"
            )
        bar_i, beat_i = int(bar), int(beat)
        if not (1 <= bar_i <= sc["bars"]):
            raise SystemExit(
                f"tracking.py [{self.story}]: BAD TIME CODE {raw_code!r} at {where} — "
                f"bar {bar_i} is outside {mv} · {q} · {s}'s {sc['bars']} bars"
            )
        if not (1 <= beat_i <= sc["num"]):
            raise SystemExit(
                f"tracking.py [{self.story}]: BAD TIME CODE {raw_code!r} at {where} — "
                f"beat {beat_i} is outside {mv} · {q} · {s}'s {sc['num']}/{sc['den']} meter"
            )
        if tick is not None and int(tick) < 1:
            raise SystemExit(f"tracking.py [{self.story}]: BAD TIME CODE {raw_code!r} at {where} — tick must be >= 1")


def load(story: str) -> dict:
    """Load ShroomsQ/_CANON/_TRACKING/<story>.yaml, validate every time code it
    carries against its own `scenes:`, resolve every trope slug via the
    register (name + keys), and return one JSON-able dict. The tool only
    reads this file — no editing (read-only v1)."""
    path = TRACKING_DIR / f"{story}.yaml"
    if not path.exists():
        raise SystemExit(f"tracking.py: no tracking file at {path}")
    raw = yaml.safe_load(path.read_text(encoding="utf-8"))
    if not raw:
        raise SystemExit(f"tracking.py: {path} is empty")
    if raw.get("story") != story:
        raise SystemExit(f"tracking.py: {path} declares story: {raw.get('story')!r}, expected {story!r}")

    scenes = raw.get("scenes") or []
    if not scenes:
        raise SystemExit(f"tracking.py [{story}]: no scenes — nothing to lay a told order on")
    idx = _CodeIndex(scenes, story)

    out_scenes = []
    for sc in scenes:
        num, den = idx._sig(sc.get("sig", "4/4"), f"scenes ({sc.get('mv')} · {sc.get('q')} · {sc.get('s')})")
        out_scenes.append({
            "mv": sc["mv"], "q": sc["q"], "s": sc["s"],
            "num": num, "den": den, "bars": sc["bars"],
            "label": sc.get("label", ""), "event": sc.get("event"),
            "frequency_mode": sc.get("frequency_mode"),
            "card": sc.get("card"),
        })

    points = []
    for i, p in enumerate(raw.get("story_points") or []):
        where = f"story_points[{i}] ({p.get('subject')}.{p.get('field')})"
        if "subject" not in p or "at" not in p or "field" not in p:
            raise SystemExit(f"tracking.py [{story}]: {where} is missing subject/at/field")
        idx.check(p["at"], where)
        points.append({
            "subject": p["subject"], "at": _strip_provisional(p["at"]),
            "field": p["field"], "value": p.get("value"),
            "origin_event": p.get("origin_event"),
            "repeat_count": p.get("repeat_count"),
            "span": p.get("span"),
        })

    register = _load_register()
    tropes = []
    for i, t in enumerate(raw.get("tropes") or []):
        slug = t.get("slug")
        where = f"tropes[{i}] ({slug})"
        if not slug:
            raise SystemExit(f"tracking.py [{story}]: {where} is missing slug")
        entry = register.get(slug)
        if entry is None:
            raise SystemExit(f"tracking.py [{story}]: UNKNOWN TROPE SLUG {slug!r} at {where} — not in the register")
        idx.check(t["at"], where)
        tropes.append({
            "slug": slug, "name": entry.get("name", slug),
            "keys": entry.get("keys", {}), "at": _strip_provisional(t["at"]),
        })

    automation = []
    for a in raw.get("automation") or []:
        aid = a.get("id", "?")
        pts = []
        for i, p in enumerate(a.get("points") or []):
            idx.check(p["at"], f"automation[{aid}].points[{i}]")
            pts.append({"at": _strip_provisional(p["at"]), "v": p["v"], "ramp": bool(p.get("ramp", False))})
        automation.append({
            "id": aid, "subject": a.get("subject"), "field": a.get("field"),
            "range": a.get("range", [0, 1]), "points": pts,
        })

    tempo = raw.get("tempo") or {}

    def _tempo_pts(key):
        pts = []
        for i, p in enumerate(tempo.get(key) or []):
            idx.check(p["at"], f"tempo.{key}[{i}]")
            pts.append({"at": _strip_provisional(p["at"]), "bpm": p["bpm"], "ramp": bool(p.get("ramp", False))})
        return pts

    tempo_out = {"planned": _tempo_pts("planned"), "measured": _tempo_pts("measured")}

    theme = raw.get("theme") or {}

    def _theme_pts(key):
        pts = []
        for i, p in enumerate(theme.get(key) or []):
            idx.check(p["at"], f"theme.{key}[{i}]")
            pts.append({"at": _strip_provisional(p["at"]), "v": p["v"]})
        return pts

    theme_out = {
        "rail": theme.get("rail"), "scale": theme.get("scale"),
        "in_world": _theme_pts("in_world"), "audience": _theme_pts("audience"),
    }

    cables = []
    for i, c in enumerate(raw.get("cables") or []):
        cid = c.get("id", f"cable[{i}]")
        setup = c.get("setup")
        if not setup:
            raise SystemExit(f"tracking.py [{story}]: cables[{cid}] has no setup")
        idx.check(setup["at"], f"cables[{cid}].setup")
        payoff = c.get("payoff")
        if payoff:
            idx.check(payoff["at"], f"cables[{cid}].payoff")
        cables.append({
            "id": cid,
            "setup": {"track": setup["track"], "at": _strip_provisional(setup["at"])},
            "payoff": {"track": payoff["track"], "at": _strip_provisional(payoff["at"])} if payoff else None,
            "orphan": c.get("orphan", "none"),
            "why": c.get("why", ""),
        })

    world = []
    for w in raw.get("world") or []:
        world.append({
            "id": w["id"], "m": w.get("m"), "label": w.get("label", ""),
            "dcus_name": w.get("dcus_name"),
        })

    return {
        "story": raw["story"], "title": raw.get("title", ""),
        "version": raw.get("version"), "last_updated": str(raw.get("last_updated") or ""),
        "movements": raw.get("movements") or [],
        "sequences": raw.get("sequences") or [],
        "scenes": out_scenes,
        "points": points,
        "tropes": tropes,
        "automation": automation,
        "tempo": tempo_out,
        "theme": theme_out,
        "cables": cables,
        "world": world,
    }


# ---- step 6 · the pull (BOLO 90, RULED 2026-09-29 session 4) -------------------------
# The page writes edits to its db (`edits`); Claude dumps them to disk with ArtifactData
# (out_dir) and runs `tracking.py pull <story> <dir>`. Contract:
# _tools/bolostatus/work/90/EDIT-CONTRACT.md. The yaml stays the one source; a bad edit is
# flagged in the ledger with its reason, never dropped or guessed.

def _ledger_path(story):
    return TRACKING_DIR / f"{story}.edits.ledger.json"


def load_ledger(story):
    p = _ledger_path(story)
    if not p.exists():
        return {"applied": [], "undone": [], "flagged": {}}
    led = json.loads(p.read_text(encoding="utf-8"))
    for k, v in (("applied", []), ("undone", []), ("flagged", {})):
        led.setdefault(k, v)
    return led


def _read_edits(edits_dir, story):
    edits = []
    for f in sorted(Path(edits_dir).rglob("*.json")):
        obj = json.loads(f.read_text(encoding="utf-8"))
        body = obj.get("data") if isinstance(obj.get("data"), dict) and "op" not in obj else obj
        eid = obj.get("id") or f.stem
        if body.get("story", story) != story or not body.get("op"):
            continue
        edits.append((eid, body))
    edits.sort(key=lambda e: (e[1].get("seq", 0), e[0]))
    return edits


def pull(story, edits_dir):
    import io
    from datetime import date
    from ruamel.yaml import YAML
    from ruamel.yaml.comments import CommentedMap, CommentedSeq

    def flow(d):
        m = CommentedMap(d)
        m.fa.set_flow_style()
        return m

    path = TRACKING_DIR / f"{story}.yaml"
    original = path.read_text(encoding="utf-8")
    ry = YAML()
    ry.preserve_quotes = True
    ry.width = 4096
    ry.indent(mapping=2, sequence=4, offset=2)
    data = ry.load(original)
    led = load_ledger(story)
    done = set(led["applied"]) | set(led["undone"]) | set(led["flagged"])
    pending = [(i, b) for i, b in _read_edits(edits_dir, story) if i not in done]

    # undo first: an undo cancels its target (the target stays in the log, marked undone)
    cancelled = set()
    for eid, b in pending:
        if b["op"] != "undo":
            continue
        ref = (b.get("data") or {}).get("ref")
        if ref in led["applied"]:
            led["flagged"][eid] = f"undo target {ref} was already pulled into the yaml"
        elif ref:
            cancelled.add(ref)
            led["applied"].append(eid)
    for ref in cancelled:
        if ref not in led["undone"]:
            led["undone"].append(ref)

    idx = _CodeIndex(data["scenes"], story)

    def bad(code):
        try:
            idx.check(code, "edit")
            return None
        except SystemExit as e:
            return str(e).split(" — ", 1)[-1]

    def find_point(key):
        for p in data.get("story_points") or []:
            if (p.get("subject") == key.get("subject") and p.get("field") == key.get("field")
                    and _strip_provisional(p.get("at")) == _strip_provisional(key.get("at"))):
                return p
        return None

    applied_now = 0
    for eid, b in pending:
        op, d = b["op"], b.get("data") or {}
        if op == "undo" or eid in cancelled or eid in led["flagged"]:
            continue
        why = None
        if op == "point.move":
            p = find_point(d.get("key") or {})
            why = "no story point matches the key" if p is None else bad(d.get("to"))
            if not why:
                p["at"] = d["to"]
        elif op == "point.add":
            if not all(d.get(k) for k in ("subject", "field", "at")):
                why = "point.add needs subject, field and at"
            else:
                why = bad(d["at"])
            if not why:
                row = {k: d[k] for k in ("subject", "at", "field")}
                row["value"] = d.get("value", "")
                if d.get("origin_event"):
                    row["origin_event"] = d["origin_event"]
                data.setdefault("story_points", CommentedSeq()).append(flow(row))
        elif op == "point.remove":
            p = find_point(d.get("key") or {})
            if p is None:
                why = "no story point matches the key"
            else:
                data["story_points"].remove(p)
        elif op == "cable.add":
            cid, setup, payoff = d.get("id"), d.get("setup") or {}, d.get("payoff")
            if not cid or any(c.get("id") == cid for c in data.get("cables") or []):
                why = f"cable id {cid!r} is missing or already used"
            else:
                why = bad(setup.get("at")) or (bad(payoff.get("at")) if payoff else None)
            if not why:
                row = CommentedMap()
                row["id"] = cid
                row["setup"] = flow({"track": setup["track"], "at": setup["at"]})
                row["payoff"] = flow({"track": payoff["track"], "at": payoff["at"]}) if payoff else None
                row["orphan"] = "provisional" if payoff else "setup_no_payoff"
                row["why"] = d.get("why", "")
                data.setdefault("cables", CommentedSeq()).append(row)
        elif op == "cable.remove":
            hit = [c for c in data.get("cables") or [] if c.get("id") == d.get("id")]
            if not hit:
                why = f"no cable {d.get('id')!r}"
            else:
                data["cables"].remove(hit[0])
        elif op == "tempo.planned":
            pts = d.get("points") or []
            why = next((f"{p.get('at')}: {bad(p.get('at'))}" for p in pts if bad(p.get("at"))), None)
            if not why and not all(isinstance(p.get("bpm"), (int, float)) and p["bpm"] > 0 for p in pts):
                why = "every tempo point needs a bpm above 0"
            if not why:
                seq = CommentedSeq()
                for p in pts:
                    row = {"at": p["at"], "bpm": p["bpm"]}
                    if p.get("ramp"):
                        row["ramp"] = True
                    seq.append(flow(row))
                data.setdefault("tempo", CommentedMap())["planned"] = seq
        else:
            why = f"unknown op {op!r}"
        if why:
            led["flagged"][eid] = why
        else:
            led["applied"].append(eid)
            applied_now += 1

    if applied_now:
        v = str(data.get("version", "0.1.0")).split(".")
        v[-1] = str(int(v[-1]) + 1)
        data["version"] = ".".join(v)
        data["last_updated"] = date.today().isoformat()
        buf = io.StringIO()
        ry.dump(data, buf)
        path.write_text(buf.getvalue(), encoding="utf-8")
        try:
            load(story)
        except SystemExit:
            path.write_text(original, encoding="utf-8")
            raise
    _ledger_path(story).write_text(json.dumps(led, indent=1, ensure_ascii=False), encoding="utf-8")
    ids = {i for i, _ in pending}
    return {"pending": len(pending), "applied": applied_now, "undone": len(cancelled),
            "flagged": {k: v for k, v in led["flagged"].items() if k in ids},
            "version": str(data.get("version"))}


if __name__ == "__main__":
    import sys
    if len(sys.argv) >= 4 and sys.argv[1] == "pull":
        print(json.dumps(pull(sys.argv[2], sys.argv[3]), indent=2, ensure_ascii=False))
        raise SystemExit(0)
    data = load("oxo")
    print(json.dumps({
        "scenes": len(data["scenes"]), "points": len(data["points"]),
        "tropes": len(data["tropes"]), "automation": len(data["automation"]),
        "tempo_planned": len(data["tempo"]["planned"]), "tempo_measured": len(data["tempo"]["measured"]),
        "cables": len(data["cables"]), "world": len(data["world"]),
    }, indent=2))
