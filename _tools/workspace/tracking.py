#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BOLO 79 (RULED 2026-09-29, "all recommendations") — the tracking-file loader.

Reads ONE tracking file per story (ssot_08 format) —
  ShroomsQ/_CANON/_TRACKING/<story>.yaml
— validates every time code against that file's own `scenes:` list, resolves
every trope slug against the trope register, and returns one JSON-able dict
that build.py embeds for the Told lens (The Arrangement).

This module only READS the tracking file — no editing (ruling 4, read-only v1).

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
        "version": raw.get("version"), "last_updated": raw.get("last_updated"),
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


if __name__ == "__main__":
    data = load("oxo")
    print(json.dumps({
        "scenes": len(data["scenes"]), "points": len(data["points"]),
        "tropes": len(data["tropes"]), "automation": len(data["automation"]),
        "tempo_planned": len(data["tempo"]["planned"]), "tempo_measured": len(data["tempo"]["measured"]),
        "cables": len(data["cables"]), "world": len(data["world"]),
    }, indent=2))
