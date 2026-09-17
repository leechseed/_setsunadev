"""
speak.py — JUDY's mouth.

BOLO 56, voice call ruled 2026-09-16: Piper now, ElevenLabs eventually — and
"eventually" arrived the same day, when Papi got an ElevenLabs account.

Three engines behind one `say()`, so the engine is a config line, not a rewrite:

    sapi        Windows built-in. Robotic. The floor.
    piper       Local neural. Free, ~23x realtime, offline. The fallback that costs nothing.
    elevenlabs  Paid. The only one that can act — stability and style are real
                delivery dials, which is what Piper structurally cannot do.

THE REPO IS PUBLIC. The ElevenLabs key lives in an env var or _PRIVATE/elevenlabs.key,
never in judy.json or any tracked file. `--key-status` says where it found one.

    python speak.py "Judy on station."
    python speak.py --voice en_GB-alba-medium "Go ahead, Papi."
    python speak.py --list
    python speak.py --engine sapi "comparison test"
    python speak.py --key-status
    python speak.py --list-eleven
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
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
VOICES = os.path.join(HERE, "voices")
JUDY = os.path.join(HERE, "judy.json")

# THE REPO IS PUBLIC (github.com/leechseed/_setsunadev). The key never goes in
# judy.json, config.json, or anything else git tracks. Env var first, then this
# file, which lives under the gitignored _PRIVATE/ tree.
KEYFILE = os.path.join(ROOT, "_PRIVATE", "elevenlabs.key")

_CACHE = {}
_EL = {}
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


# ------------------------------------------------------------------ elevenlabs

def el_key():
    """Env var, then the gitignored key file. Never a tracked file."""
    for k in ("ELEVENLABS_API_KEY", "ELEVEN_API_KEY", "XI_API_KEY"):
        v = (os.environ.get(k) or "").strip()
        if v:
            return v
    try:
        v = io.open(KEYFILE, encoding="utf-8").read().strip()
        return v or None
    except Exception:
        return None


def el_client():
    with _LOCK:
        if "c" in _EL:
            return _EL["c"]
        key = el_key()
        if not key:
            raise RuntimeError(
                "no ElevenLabs key — set ELEVENLABS_API_KEY, or put the key in "
                f"{KEYFILE} (that tree is gitignored; this repo is public)")
        from elevenlabs.client import ElevenLabs
        _EL["c"] = ElevenLabs(api_key=key)
        return _EL["c"]


def el_voices():
    """Every voice on the account — the ones Papi builds show up here."""
    try:
        res = el_client().voices.search(page_size=100)
        out = []
        for v in getattr(res, "voices", []) or []:
            labels = dict(getattr(v, "labels", {}) or {})
            out.append({
                "voice_id": v.voice_id,
                "name": v.name,
                "category": getattr(v, "category", "") or "",
                "accent": labels.get("accent", ""),
                "gender": labels.get("gender", ""),
                "description": labels.get("description", ""),
            })
        return out
    except Exception as e:
        return {"error": str(e)}


def el_models():
    try:
        out = []
        for m in el_client().models.list() or []:
            if not getattr(m, "can_do_text_to_speech", True):
                continue
            out.append({"model_id": m.model_id, "name": getattr(m, "name", m.model_id)})
        return out
    except Exception as e:
        return {"error": str(e)}


def _wav_from_pcm(pcm, path, rate):
    """ElevenLabs PCM is raw 16-bit mono; winsound needs a RIFF header."""
    with wave.open(path, "wb") as w:
        w.setnchannels(1)
        w.setsampwidth(2)
        w.setframerate(rate)
        w.writeframes(pcm)
    return path


def synth_eleven(text, voice_id=None, model=None, settings=None, out_wav=None):
    """
    Text → wav via ElevenLabs. PCM rather than mp3 so playback stays on the same
    winsound path as Piper — one player, one code path, no ffmpeg dependency.
    """
    cfg = read_judy()["voice"]
    # Key first: with no key there is also no voice list, so "pick a voice" would
    # name a symptom and hide the cause.
    el_client()
    voice_id = voice_id or cfg.get("eleven_voice_id")
    if not voice_id:
        raise RuntimeError("no ElevenLabs voice chosen — pick one in the console's Voice panel")
    model = model or cfg.get("eleven_model") or "eleven_turbo_v2_5"
    rate = 24000
    from elevenlabs import VoiceSettings
    s = {**{"stability": 0.4, "similarity_boost": 0.75, "style": 0.35,
            "use_speaker_boost": True, "speed": 1.0},
         **(settings or cfg.get("eleven_settings") or {})}
    chunks = el_client().text_to_speech.stream(
        voice_id=voice_id,
        text=text,
        model_id=model,
        output_format=f"pcm_{rate}",
        voice_settings=VoiceSettings(**s),
    )
    pcm = b"".join(c for c in chunks if c)
    out_wav = out_wav or os.path.join(HERE, "_last.wav")
    return _wav_from_pcm(pcm, out_wav, rate)


def _wait(path):
    """Block for the length of the clip — playback is async by design."""
    try:
        import time
        with wave.open(path, "rb") as w:
            time.sleep(w.getnframes() / float(w.getframerate()))
    except Exception:
        pass


def read_judy():
    base = {"engine": "piper", "piper_voice": "", "name": "", "rate": 0, "volume": 100,
            "eleven_voice_id": "", "eleven_model": "eleven_turbo_v2_5",
            "eleven_settings": {"stability": 0.4, "similarity_boost": 0.75,
                                "style": 0.35, "use_speaker_boost": True, "speed": 1.0}}
    default = {"voice": dict(base)}
    try:
        j = json.load(io.open(JUDY, encoding="utf-8"))
        default.update({k: v for k, v in j.items() if k == "voice"} or {})
        default["voice"] = {**base, **j.get("voice", {})}
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
        # Raise rather than quietly dropping to Piper: a silent fallback would mean
        # JUDY sounds wrong and nobody knows why. A missing key is a bug to fix.
        wav = synth_eleven(text, voice_id=voice, settings=None)
        play(wav)
        if blocking:
            _wait(wav)
        return wav

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
        _wait(wav)
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
    ap.add_argument("--list-eleven", action="store_true", help="voices on the ElevenLabs account")
    ap.add_argument("--key-status", action="store_true")
    a = ap.parse_args()

    if a.key_status:
        k = el_key()
        src = ("env" if any(os.environ.get(x) for x in
               ("ELEVENLABS_API_KEY", "ELEVEN_API_KEY", "XI_API_KEY"))
               else ("file " + KEYFILE) if k else "nowhere")
        print(f"  ElevenLabs key: {'FOUND (' + str(len(k)) + ' chars) via ' + src if k else 'NOT SET'}")
        if not k:
            print(f"  put it in {KEYFILE}  (gitignored; this repo is public)")
        return

    if a.list_eleven:
        vs = el_voices()
        if isinstance(vs, dict):
            print("  error:", vs["error"])
            return
        print(f"ElevenLabs voices on the account ({len(vs)}):")
        for v in vs:
            tag = " / ".join(x for x in (v["category"], v["gender"], v["accent"]) if x)
            print(f"  {v['name']:28s} {tag:34s} {v['voice_id']}")
        return

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
