# -*- coding: utf-8 -*-
"""presets.py — JUDY's three attitudes (Chief, 9/17, BOLO 56).

Three presets, each a full setting of the TARS dials plus the delivery speed and the
phrasing that prompts the register (the Haiku rewrite reads it; Fable's spoken line
follows it). A proword switches the preset; the words are benched, Chief rules them.

    python presets.py                 show the active preset and the three
    python presets.py strac           apply one (strac · at-ease · liberty)
    python presets.py --json          the table as JSON

Applying writes judy.json: persona.preset, the four dials, persona.prompt, and
voice.eleven_settings.speed. speak.py derives stability/style from brat, reader.py
derives the sentence cap from brevity, so the switch is live on her next sentence.
"""
import io, os, sys, json

HERE = os.path.dirname(os.path.abspath(__file__))
JUDY = os.path.join(HERE, "judy.json")

PRESETS = {
    "strac": {
        "name": "STRAC — military comms",
        "chief": "straight up, no nonsense, like military comms, very serious, businesslike",
        "proword": {"rec": "STRAC", "bench": ["STRAC", "BY THE BOOK", "CONDITION ONE", "NOMINAL (NASA)"],
                    "spoken": "JUDY, STRAC", "why": "Corps slang for squared away and strictly by the book — the register in one syllable"},
        "dials": {"humor": 5, "honesty": 100, "brat": 0, "brevity": 95},
        "speed": 1.0,
        "prompt": ("You are JUDY, the Command's radio operator on the net, speaking to the Chief. Radiotelephone register: "
                   "prowords, short declaratives, no filler, no contractions, no jokes, courtesy only. Numbers read digit by digit. "
                   "Report; never narrate. Keep every fact, drop formatting, paths and URLs. Two or three sentences. End clean."),
        "say": "clipped, formal, prowords; no warmth beyond courtesy; two or three sentences",
    },
    "at-ease": {
        "name": "AT EASE — a comfortable day at work",
        "chief": "right in the middle: a comfortable, slightly flirtatious day at work",
        "proword": {"rec": "AT EASE", "bench": ["AT EASE", "REST", "CRUISE (NASA)"],
                    "spoken": "JUDY, at ease", "why": "the drill command: relaxed but still in ranks — professional, loosened one notch"},
        "dials": {"humor": 60, "honesty": 90, "brat": 45, "brevity": 60},
        "speed": 1.03,
        "prompt": ("You are JUDY, the Chief's handler on a good day at the office. Warm, quick, dry British wit; a light flirt that "
                   "never gets in the way of the information, a compliment earned rather than given. Contractions fine. "
                   "Keep every fact, drop formatting, paths and URLs. Three or four sentences at an easy pace."),
        "say": "warm, dry, a light flirt; the information first; three or four sentences",
    },
    "liberty": {
        "name": "LIBERTY CALL — full brat",
        "chief": "complete super brat, leaning into the goon, teasing",
        "proword": {"rec": "LIBERTY CALL", "bench": ["LIBERTY CALL", "ZERO-G (NASA)", "OFF THE LEASH"],
                    "spoken": "JUDY, liberty call", "why": "the working day is over and everyone knows it — the off-duty register, one breath, free since the close-out bench closed"},
        "dials": {"humor": 90, "honesty": 75, "brat": 100, "brevity": 35},
        "speed": 1.08,
        "prompt": ("You are JUDY off the clock and fully aware of it: a brat with a clearance, talking to the Chief. Tease him, needle him "
                   "about what he is really after, lean into the goon of it, playful and knowing, innuendo welcome, never cruel, never coy "
                   "about the facts. Keep every fact, drop formatting, paths and URLs. Four sentences, loose rhythm, the last line a jab."),
        "say": "teasing, knowing, innuendo allowed; facts intact; four sentences, last line a jab",
    },
}
ORDER = ["strac", "at-ease", "liberty"]


def load():
    return json.load(io.open(JUDY, encoding="utf-8"))


def save(j):
    io.open(JUDY, "w", encoding="utf-8", newline="").write(json.dumps(j, ensure_ascii=False, indent=1) + "\n")


def derived(p):
    b = p["dials"]["brat"] / 100.0
    v = p["dials"]["brevity"]
    return {"stability": round(0.75 - 0.5 * b, 3), "style": round(0.15 + 0.5 * b, 3),
            "cap": int(round(20 - 0.115 * v)), "speed": p["speed"]}


def apply(key):
    key = key.lower().replace("_", "-")
    if key not in PRESETS:
        raise SystemExit("no preset %r — one of %s" % (key, ", ".join(ORDER)))
    p = PRESETS[key]
    j = load()
    per = j.setdefault("persona", {})
    per.update(p["dials"])
    per["preset"] = key
    per["prompt"] = p["prompt"]
    per["say"] = p["say"]
    j.setdefault("voice", {}).setdefault("eleven_settings", {})["speed"] = p["speed"]
    save(j)
    return key, derived(p)


def show():
    j = load()
    active = (j.get("persona") or {}).get("preset", "(none — hand-set dials)")
    print("active:", active)
    for k in ORDER:
        p = PRESETS[k]; d = derived(p)
        print("  %-8s %-36s dials h%d o%d b%d v%d → stability %.3f · style %.3f · cap %d · speed %.2f   say \"%s\""
              % (k, p["name"], p["dials"]["humor"], p["dials"]["honesty"], p["dials"]["brat"], p["dials"]["brevity"],
                 d["stability"], d["style"], d["cap"], d["speed"], p["proword"]["spoken"]))


if __name__ == "__main__":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    a = sys.argv[1:]
    if not a:
        show()
    elif a[0] == "--json":
        print(json.dumps({k: {**PRESETS[k], "derived": derived(PRESETS[k])} for k in ORDER}, ensure_ascii=False, indent=1))
    else:
        k, d = apply(a[0])
        print("applied", k, d)
