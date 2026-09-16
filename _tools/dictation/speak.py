"""
speak.py — JUDY's mouth.

BOLO 56, voice call ruled 2026-09-16: **Piper now, ElevenLabs eventually.**

Piper is local, free, and fast — it runs on CPU in well under real time, so the 3090
stays free for Whisper. Two engines live behind one interface so swapping to
ElevenLabs later is a config change, not a rewrite:

    sapi        Windows built-in. Robotic. The floor.
    piper       Local neural. Free. What JUDY uses now.
    elevenlabs  Paid, best match for the 007 handler register. Wired, needs a key.

    python speak.py "Judy on station."
    python speak.py --voice en_GB-alba-medium "Go ahead, Papi."
    python speak.py --list
    python speak.py --engine sapi "comparison test"
"""

import argparse
import io
import json
import os
import subprocess
import sys
import threading
import wave

HERE = os.path.dirname(os.path.abspath(__file__))
VOICES = os.path.join(HERE, "voices")
JUDY = os.path.join(HERE, "judy.json")

_CACHE = {}
_LOCK = threading.Lock()


def voices():
    """Piper voices on disk. A voice is a .onnx plus its .onnx.json config."""
    out = []
    if not os.path.isdir(VOICES):
        return out
    for f in sorted(os.listdir(VOICES)):
        if not f.endswith(".onnx"):
            continue
        cfg = os.path.join(VOICES, f + ".json")
        if not os.path.exists(cfg):
            continue
        name = f[:-5]
        meta = {}
        try:
            j = json.load(io.open(cfg, encoding="utf-8"))
            meta = {"sample_rate": j.get("audio", {}).get("sample_rate"),
                    "language": (j.get("language") or {}).get("name_english", "")}
        except Exception:
            pass
        out.append({"name": name, "path": os.path.join(VOICES, f), **meta})
    return out


def _load(name):
    """Piper models take a moment to load; keep them warm between utterances."""
    with _LOCK:
        if name in _CACHE:
            return _CACHE[name]
        from piper import PiperVoice
        path = os.path.join(VOICES, name + ".onnx")
        if not os.path.exists(path):
            have = ", ".join(v["name"] for v in voices()) or "none"
            raise FileNotFoundError(f"no piper voice {name!r} in {VOICES} (have: {have})")
        v = PiperVoice.load(path)
        _CACHE[name] = v
        return v


def synth_piper(text, voice=None, rate=1.0, out_wav=None):
    """Text → a wav file. Returns its path."""
    cfg = read_judy()
    voice = voice or cfg["voice"].get("piper_voice") or (voices()[0]["name"] if voices() else None)
    if not voice:
        raise RuntimeError("no piper voices installed — python -m piper.download_voices "
                           "--download-dir _tools/dictation/voices en_GB-jenny_dioco-medium")
    v = _load(voice)
    out_wav = out_wav or os.path.join(HERE, "_last.wav")

    from piper import SynthesisConfig
    # length_scale is duration, so it is the INVERSE of rate: >1 is slower.
    sc = SynthesisConfig(length_scale=1.0 / max(0.25, float(rate)))
    with wave.open(out_wav, "wb") as w:
        v.synthesize_wav(text, w, syn_config=sc)
    return out_wav


def play(path):
    """Non-blocking playback so a spoken line never stalls the loop."""
    try:
        import winsound
        winsound.PlaySound(path, winsound.SND_FILENAME | winsound.SND_ASYNC)
        return True
    except Exception:
        pass
    try:
        subprocess.Popen(["ffplay", "-nodisp", "-autoexit", "-loglevel", "quiet", path],
                         stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return True
    except Exception:
        return False


def read_judy():
    default = {"voice": {"engine": "piper", "piper_voice": "", "name": "",
                         "rate": 0, "volume": 100}}
    try:
        j = json.load(io.open(JUDY, encoding="utf-8"))
        default.update({k: v for k, v in j.items() if k == "voice"} or {})
        default["voice"] = {**{"engine": "piper", "piper_voice": "", "name": "",
                               "rate": 0, "volume": 100}, **j.get("voice", {})}
    except Exception:
        pass
    return default


def say(text, engine=None, voice=None, rate=None, blocking=False):
    """The one entry point. Engine comes from judy.json unless overridden."""
    cfg = read_judy()["voice"]
    engine = engine or cfg.get("engine", "piper")
    text = (text or "").strip()
    if not text:
        return None

    if engine == "sapi":
        import shutil
        exe = shutil.which("pwsh") or "powershell"
        t = text.replace("'", "''")
        n = (voice or cfg.get("name") or "").replace("'", "''")
        pick = f"$s.SelectVoice('{n}');" if n else ""
        script = ("Add-Type -AssemblyName System.Speech;"
                  "$s=New-Object System.Speech.Synthesis.SpeechSynthesizer;"
                  f"{pick}$s.Rate={int(cfg.get('rate', 0))};"
                  f"$s.Volume={int(cfg.get('volume', 100))};$s.Speak('{t}');$s.Dispose()")
        run = subprocess.run if blocking else subprocess.Popen
        run([exe, "-NoProfile", "-NonInteractive", "-Command", script],
            stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        return None

    if engine == "elevenlabs":
        # Wired but not reachable without a key — say so rather than fall back
        # silently, or JUDY would quietly sound wrong and nobody would know why.
        if not os.environ.get("ELEVENLABS_API_KEY"):
            raise RuntimeError("engine is elevenlabs but ELEVENLABS_API_KEY is not set")
        raise NotImplementedError("elevenlabs not implemented yet — ruled 'eventually', not now")

    # piper
    r = 1.0
    if rate is not None:
        r = float(rate)
    elif cfg.get("rate"):
        # the console's dial is SAPI's -10..10; map it onto a speed multiplier
        r = 1.0 + (float(cfg["rate"]) / 20.0)
    wav = synth_piper(text, voice=voice or cfg.get("piper_voice") or None, rate=r)
    play(wav)
    if blocking:
        try:
            with wave.open(wav, "rb") as w:
                import time
                time.sleep(w.getnframes() / float(w.getframerate()))
        except Exception:
            pass
    return wav


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="JUDY's mouth (BOLO 56)")
    ap.add_argument("text", nargs="*")
    ap.add_argument("--engine", choices=["piper", "sapi", "elevenlabs"])
    ap.add_argument("--voice")
    ap.add_argument("--rate", type=float, help="piper speed multiplier, 1.0 = normal")
    ap.add_argument("--list", action="store_true")
    a = ap.parse_args()

    if a.list:
        vs = voices()
        print(f"piper voices in {VOICES} ({len(vs)}):")
        for v in vs:
            print(f"  {v['name']:36s} {v.get('language','')}  {v.get('sample_rate','')} Hz")
        return

    text = " ".join(a.text) or "Judy on station. Go ahead, Papi."
    import time
    t0 = time.time()
    wav = say(text, engine=a.engine, voice=a.voice, rate=a.rate, blocking=True)
    if wav:
        with wave.open(wav, "rb") as w:
            dur = w.getnframes() / float(w.getframerate())
        took = time.time() - t0
        print(f"  {dur:.2f}s of audio · synthesized+played in {took:.2f}s")


if __name__ == "__main__":
    main()
