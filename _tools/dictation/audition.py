"""
audition.py — try candidate voices on the words JUDY will actually say.

BOLO 56. A voice that reads prose beautifully can still mangle "BOLO", "Oscar Mike"
or "DCUS", and you find out when she is live. So the script is the real job: a
greeting, a dense status read with the Command lexicon and numbers, a bratty beat,
and a close. Every candidate gets identical settings, so what you hear is the voice
and not the dials.

    python audition.py                       # the standing cast, the standing script
    python audition.py --cast blondie,kira
    python audition.py --brat                # same cast at the brat settings
    python audition.py --line "one line"     # a single line instead of the script
    python audition.py --list                # the cast list with ids

Output lands in _PRIVATE/voice-auditions/ — gitignored, because audio does not
belong in a public repo.
"""

import argparse
import os
import sys
import time
import wave

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import speak  # noqa: E402

OUT = os.path.join(speak.ROOT, "_PRIVATE", "voice-auditions")

# Chief's shortlist. Add a row and it joins the next run.
CAST = {
    "blondie":  ("Blondie — Conversational, British",        "exsUS4vynmxd379XN4yO"),
    "emmaline": ("Emmaline — young British girl",            "nDJIICjR9zfJExIFeSCN"),
    "amelia":   ("Amelia — Enthusiastic & Expressive, Brit", "ZF6FPAbjXT4488VcRRnw"),
    "kira":     ("Kira — Video Game, Bold & Cinematic",      "W3C2vBPukr5b5jvoXhPK"),
    "samara":   ("Samara X — Smooth Classy British",         "19STyYD15bswVz51nqLf"),
    "alice":    ("Alice — Clear, Engaging Educator, Brit",   "Xb7hH8MSUJpSbSDYk0k2"),
}

# Four beats, because a voice can pass one and fail another.
SCRIPT = {
    "1-hail": (
        "Judy on station. Go ahead, Chief."
    ),
    "2-board": (
        "Sit rep, seventeen September. Six rows blocked on you, and the oldest has "
        "been sitting since March third. BOLO twenty-four is at gate three with the "
        "slice standing built. BOLO forty-six is still priority one, by your own word, "
        "from the eleventh. DARKROOM is down. Stash is up. The tree is clean."
    ),
    "3-brat": (
        "And before you ask — yes, the dental row is still open. It has been open "
        "since the nineteenth of August. I am not going to nag you about it. I am "
        "simply going to mention it every single time you ask me for the board."
    ),
    "4-close": (
        "That is the whole board. Say the word and I will walk it with you, or say "
        "Oscar Mike and I will close us out for the night."
    ),
}

# One setting for every candidate, so the comparison is honest.
NORMAL = {"stability": 0.35, "style": 0.55, "similarity_boost": 0.80,
          "use_speaker_boost": True, "speed": 1.05}
BRAT = {"stability": 0.15, "style": 0.85, "similarity_boost": 0.80,
        "use_speaker_boost": True, "speed": 1.08}


def render(key, label, vid, beats, settings, model, tag):
    print(f"\n  {label}")
    print(f"  {'-' * len(label)}")
    total_audio = total_time = 0.0
    for beat, text in beats:
        path = os.path.join(OUT, f"{key}--{beat}{tag}.wav")
        t0 = time.time()
        try:
            speak.synth_eleven(text, voice_id=vid, model=model,
                               settings=settings, out_wav=path)
        except Exception as e:
            print(f"    {beat:9s} FAILED: {str(e)[:110]}")
            continue
        took = time.time() - t0
        with wave.open(path, "rb") as w:
            dur = w.getnframes() / float(w.getframerate())
        total_audio += dur
        total_time += took
        print(f"    {beat:9s} {dur:5.2f}s audio  {took:5.2f}s synth  ({dur / took:5.1f}x)")
    if total_time:
        print(f"    {'total':9s} {total_audio:5.2f}s audio  {total_time:5.2f}s synth")
    return total_audio, total_time


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    ap = argparse.ArgumentParser(description="Audition candidate voices (BOLO 56)")
    ap.add_argument("--cast", help="comma-separated keys; default is all of them")
    ap.add_argument("--brat", action="store_true", help="render at the brat settings")
    ap.add_argument("--line", help="one line instead of the four-beat script")
    ap.add_argument("--model", default="eleven_turbo_v2_5")
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()

    if a.list:
        print("cast:")
        for k, (label, vid) in CAST.items():
            print(f"  {k:9s} {label:42s} {vid}")
        return

    keys = [k.strip().lower() for k in a.cast.split(",")] if a.cast else list(CAST)
    unknown = [k for k in keys if k not in CAST]
    if unknown:
        raise SystemExit(f"unknown: {', '.join(unknown)} — try --list")

    os.makedirs(OUT, exist_ok=True)
    beats = [("line", a.line)] if a.line else sorted(SCRIPT.items())
    settings = BRAT if a.brat else NORMAL
    tag = "-brat" if a.brat else ""

    print(f"audition · {len(keys)} voices · {len(beats)} beat(s) · "
          f"{'BRAT' if a.brat else 'normal'} settings · {a.model}")
    print(f"  stability {settings['stability']}  style {settings['style']}  "
          f"speed {settings['speed']}")

    for k in keys:
        label, vid = CAST[k]
        render(k, label, vid, beats, settings, a.model, tag)

    print(f"\n  files: {OUT}")
    print("  compare beat by beat, not voice by voice — play every 2-board first,")
    print("  then every 3-brat. The proper nouns are where they differ most.")


if __name__ == "__main__":
    main()
