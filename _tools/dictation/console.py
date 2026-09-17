"""
console.py — JUDY's console. The mod menu.

BOLO 56. A local control panel for the voice loop: every knob in one place, turned
with a mouse instead of a ruling. Runs on 127.0.0.1 only — it reads your config,
sees your mic, swaps files on disk and starts the daemon, so it cannot be a hosted
page. Same shape as DARKROOM on :8484.

    python _tools/dictation/console.py          # → http://127.0.0.1:8787
    python _tools/dictation/console.py --port N
    python _tools/dictation/console.py --no-open

Stdlib only. Nothing here is billed and no audio leaves the box.

Two config files, deliberately separate:
    config.json   the dictation daemon's settings (BOLO 26, shipped and working)
    judy.json     JUDY's own settings (BOLO 56) — persona, voice, face, wire
The console edits both; ptt.py only ever reads the first.
"""

import argparse
import base64
import io
import json
import mimetypes
import os
import re
import shutil
import subprocess
import sys
import threading
import time
import webbrowser
from collections import deque
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
SOP = os.path.join(ROOT, "SOP.md")
CONFIG = os.path.join(HERE, "config.json")
JUDY = os.path.join(HERE, "judy.json")
FACES = os.path.join(HERE, "faces")
PAGE = os.path.join(HERE, "console.html")

sys.path.insert(0, HERE)
import codebook  # noqa: E402
import speak  # noqa: E402

# Whisper models worth offering. Size is the download, not VRAM.
MODELS = [
    ("distil-large-v3", "1.5 GB", "near large-v3 on proper nouns, a fraction of the latency · English only · the default"),
    ("large-v3", "3.1 GB", "the most accurate · multilingual · slowest"),
    ("large-v3-turbo", "1.6 GB", "large-v3 distilled differently · multilingual · fast"),
    ("medium.en", "1.5 GB", "older, solid, English only"),
    ("small.en", "484 MB", "quick and light · proper nouns start to slip"),
    ("base.en", "141 MB", "fastest · already cached on this box · use for smoke tests"),
]

STATES = ["idle", "listening", "thinking", "talking"]

JUDY_DEFAULTS = {
    "persona": {"humor": 75, "honesty": 90, "brat": 65, "brevity": 70},
    "voice": {"engine": "piper", "piper_voice": "en_GB-jenny_dioco-medium",
              "name": "", "rate": 0, "volume": 100,
              "eleven_voice_id": "", "eleven_model": "eleven_turbo_v2_5",
              "eleven_settings": {"stability": 0.4, "similarity_boost": 0.75,
                                  "style": 0.35, "use_speaker_boost": True,
                                  "speed": 1.0}},
    "face": {"slots": {s: None for s in STATES}},
    "chat": {"model": "claude-haiku-4-5-20251001"},
    "wire": {"mode": "standalone"},
}

LOG = deque(maxlen=400)
DAEMON = {"proc": None, "started": 0}


# ---------------------------------------------------------------- config i/o

def read_json(path, default):
    try:
        with io.open(path, encoding="utf-8") as f:
            data = json.load(f)
    except Exception:
        return json.loads(json.dumps(default))
    out = json.loads(json.dumps(default))
    _merge(out, data)
    return out


def _merge(base, over):
    for k, v in (over or {}).items():
        if isinstance(v, dict) and isinstance(base.get(k), dict):
            _merge(base[k], v)
        else:
            base[k] = v


def write_json(path, obj):
    with io.open(path, "w", encoding="utf-8", newline="\n") as f:
        json.dump(obj, f, ensure_ascii=False, indent=2)
        f.write("\n")


def dictation_defaults():
    import ptt
    return dict(ptt.DEFAULTS)


# ---------------------------------------------------------------- the box

def gpu_info():
    out = {"cuda": False, "name": "", "compute": []}
    try:
        import ctranslate2
        n = ctranslate2.get_cuda_device_count()
        out["cuda"] = n > 0
        if n:
            out["compute"] = sorted(ctranslate2.get_supported_compute_types("cuda"))
    except Exception as e:
        out["error"] = str(e)
    try:
        r = subprocess.run(["nvidia-smi", "--query-gpu=name,memory.total",
                            "--format=csv,noheader"], capture_output=True, text=True, timeout=6)
        if r.returncode == 0:
            out["name"] = r.stdout.strip().splitlines()[0]
    except Exception:
        pass
    return out


def input_devices():
    try:
        import sounddevice as sd
        default = sd.default.device[0]
        devs, seen = [], set()
        for i, d in enumerate(sd.query_devices()):
            if d["max_input_channels"] <= 0:
                continue
            # Windows lists the same mic once per host API; 70 rows is an unusable
            # dropdown. Keep the first of each name, and never drop the default.
            key = d["name"].strip().lower()
            if key in seen and i != default:
                continue
            seen.add(key)
            devs.append({"id": i, "name": d["name"],
                         "channels": d["max_input_channels"],
                         "default": i == default})
        return devs
    except Exception as e:
        LOG.append(f"! device probe failed: {e}")
        return []


def mic_level(device, ms=180):
    """One short sample, for the meter. Cheap enough to poll."""
    try:
        import numpy as np
        import sounddevice as sd
        n = int(16000 * ms / 1000)
        a = sd.rec(n, samplerate=16000, channels=1, dtype="float32",
                   device=device if device not in (None, "", -1) else None)
        sd.wait()
        a = a.reshape(-1)
        if not len(a):
            return {"peak": 0.0, "rms": 0.0}
        return {"peak": float(np.abs(a).max()),
                "rms": float(np.sqrt((a ** 2).mean()))}
    except Exception as e:
        return {"peak": 0.0, "rms": 0.0, "error": str(e)}


def model_cached(name):
    """
    Is this model already downloaded? Saves a surprise 3 GB wait mid-sentence.

    Matched against the real repo names rather than a loose substring: "large-v3"
    is a substring of "faster-distil-whisper-large-v3", so the naive check marked
    the wrong model cached and the right one missing — exactly backwards.
    """
    hub = os.path.join(os.path.expanduser("~"), ".cache", "huggingface", "hub")
    if not os.path.isdir(hub):
        return False
    if name.startswith("distil-"):
        repo = "faster-distil-whisper-" + name[len("distil-"):]
    else:
        repo = "faster-whisper-" + name
    for d in os.listdir(hub):
        if not d.lower().endswith("--" + repo.lower()):
            continue
        snaps = os.path.join(hub, d, "snapshots")
        # a stub directory with no snapshot is an interrupted download, not a model
        if os.path.isdir(snaps) and any(os.scandir(snaps)):
            return True
    return False


# ---------------------------------------------------------------- voice (SAPI)

def _ps():
    """
    pwsh 7 first. Windows PowerShell 5.1 sees only the two legacy SAPI voices; pwsh
    on .NET Core also surfaces the OneCore ones (5 on this box, 2 of them female).
    Measured, not assumed — 5.1 returned 2 and pwsh returned 5 for the same script.
    """
    exe = shutil.which("pwsh") or "powershell"
    return [exe, "-NoProfile", "-NonInteractive", "-Command"]


def sapi_voices():
    """Windows ships these. Free floor for JUDY until the voice call is ruled."""
    script = (
        "Add-Type -AssemblyName System.Speech;"
        "$s=New-Object System.Speech.Synthesis.SpeechSynthesizer;"
        "$s.GetInstalledVoices()|%{$i=$_.VoiceInfo;"
        "'{0}|{1}|{2}' -f $i.Name,$i.Gender,$i.Culture}"
    )
    try:
        r = subprocess.run(_ps() + [script], capture_output=True, text=True, timeout=25)
        out = []
        for line in r.stdout.strip().splitlines():
            parts = line.strip().split("|")
            if len(parts) == 3:
                out.append({"name": parts[0], "gender": parts[1], "culture": parts[2]})
        return out
    except Exception as e:
        LOG.append(f"! sapi probe failed: {e}")
        return []


def sapi_speak(name, text, rate=0, volume=100):
    text = (text or "").replace("'", "''")
    name = (name or "").replace("'", "''")
    pick = f"$s.SelectVoice('{name}');" if name else ""
    script = (
        "Add-Type -AssemblyName System.Speech;"
        "$s=New-Object System.Speech.Synthesis.SpeechSynthesizer;"
        f"{pick}$s.Rate={int(rate)};$s.Volume={int(volume)};"
        f"$s.Speak('{text}');$s.Dispose()"
    )
    subprocess.Popen(_ps() + [script], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


# ---------------------------------------------------------------- the daemon

def daemon_running():
    p = DAEMON["proc"]
    return p is not None and p.poll() is None


def daemon_start(extra=None):
    if daemon_running():
        return "already running"
    cmd = [sys.executable, os.path.join(HERE, "ptt.py")] + (extra or [])
    p = subprocess.Popen(cmd, cwd=ROOT, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                         text=True, encoding="utf-8", errors="replace", bufsize=1)
    DAEMON["proc"] = p
    DAEMON["started"] = time.time()
    LOG.append(f"— daemon started (pid {p.pid})")

    def pump():
        for line in p.stdout:
            LOG.append(line.rstrip())
        LOG.append("— daemon exited")

    threading.Thread(target=pump, daemon=True).start()
    return f"started pid {p.pid}"


def daemon_stop():
    if not daemon_running():
        return "not running"
    p = DAEMON["proc"]
    p.terminate()
    try:
        p.wait(timeout=5)
    except Exception:
        p.kill()
    LOG.append("— daemon stopped")
    return "stopped"


# ---------------------------------------------------------------- SOP §8

def add_codebook_row(heard, read_as, note=""):
    """
    Write a new garble row into SOP §8. This is the documented growth path — §8 is a
    standing table that grows a row per catch — so the console writes to the SOP
    itself rather than keeping a private list that would drift out of sync.
    """
    heard = " ".join((heard or "").split())
    read_as = " ".join((read_as or "").split())
    if not heard or not read_as:
        raise ValueError("both fields are required")
    s = io.open(SOP, encoding="utf-8").read()
    if re.search(r"^\|\s*" + re.escape(heard) + r"\s*(?:·|\|)", s, re.M):
        raise ValueError(f"§8 already has a row starting {heard!r}")
    stamp = time.strftime("%-m/%-d") if os.name != "nt" else time.strftime("%m/%d").lstrip("0").replace("/0", "/")
    gloss = f" (coded {stamp}" + (f" — {note}" if note else "") + ", from the console)"
    row = f"| {heard} | **{read_as}**{gloss} |\n"
    anchor = '| year ranges spoken as "twenty twelve'
    if anchor not in s:
        raise ValueError("§8 anchor row not found — has SOP.md been reorganized?")
    s = s.replace(anchor, row + anchor, 1)
    io.open(SOP, "w", encoding="utf-8", newline="\n").write(s)
    LOG.append(f"— §8 grew a row: {heard!r} -> {read_as!r}")
    return row.strip()


# ---------------------------------------------------------------- state

def eleven_state():
    """Key presence, then the account's voices — never the key itself."""
    key = speak.el_key()
    out = {"key": bool(key), "keyfile": speak.KEYFILE, "voices": [], "models": []}
    if not key:
        return out
    v = speak.el_voices()
    m = speak.el_models()
    if isinstance(v, dict):
        out["error"] = v.get("error")
    else:
        out["voices"] = v
    if isinstance(m, dict):
        out.setdefault("error", m.get("error"))
    else:
        out["models"] = m
    return out


def build_state():
    cfg = read_json(CONFIG, dictation_defaults())
    judy = read_json(JUDY, JUDY_DEFAULTS)
    rules_active = codebook.rules(aggressive=cfg.get("aggressive", False))
    parsed, notes, _ = codebook.parse()
    gated = [{"heard": h, "read": r} for h, r, g in parsed if g]
    return {
        "config": cfg,
        "judy": judy,
        "devices": input_devices(),
        "gpu": gpu_info(),
        "models": [{"name": n, "size": s, "note": t, "cached": model_cached(n)}
                   for n, s, t in MODELS],
        "voices": sapi_voices(),
        "piper_voices": speak.voices(),
        "eleven": eleven_state(),
        "codebook": {
            "active": len(rules_active),
            "gated": gated,
            "notes": len(notes),
            "lexicon": codebook.lexicon().split(", "),
            "rules": [{"heard": h, "read": r} for h, r in rules_active[:400]],
        },
        "faces": {s: face_url(judy, s) for s in STATES},
        "daemon": {"running": daemon_running(),
                   "uptime": int(time.time() - DAEMON["started"]) if daemon_running() else 0},
        "paths": {"config": CONFIG, "judy": JUDY, "sop": SOP, "faces": FACES, "root": ROOT},
    }


def face_url(judy, slot):
    p = (judy.get("face", {}).get("slots", {}) or {}).get(slot)
    if p and os.path.exists(p):
        return f"/face/{slot}?v={int(os.path.getmtime(p))}"
    return None


# ---------------------------------------------------------------- server

class Handler(BaseHTTPRequestHandler):
    server_version = "JudyConsole/0.1"

    def log_message(self, *a):
        pass  # the page is the log

    # -- helpers
    def _send(self, code, body, ctype="application/json; charset=utf-8"):
        if isinstance(body, (dict, list)):
            body = json.dumps(body, ensure_ascii=False).encode("utf-8")
        elif isinstance(body, str):
            body = body.encode("utf-8")
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        try:
            self.wfile.write(body)
        except Exception:
            pass

    def _body(self):
        n = int(self.headers.get("Content-Length") or 0)
        if not n:
            return {}
        return json.loads(self.rfile.read(n).decode("utf-8"))

    # -- routes
    def do_GET(self):
        path, _, qs = self.path.partition("?")
        q = dict(p.split("=", 1) for p in qs.split("&") if "=" in p)

        if path == "/":
            try:
                html = io.open(PAGE, encoding="utf-8").read()
            except Exception as e:
                return self._send(500, f"console.html missing: {e}", "text/plain; charset=utf-8")
            return self._send(200, html, "text/html; charset=utf-8")

        if path == "/api/state":
            return self._send(200, build_state())

        if path == "/api/level":
            d = q.get("device")
            d = int(d) if (d or "").lstrip("-").isdigit() else None
            return self._send(200, mic_level(d))

        if path == "/api/log":
            return self._send(200, {"lines": list(LOG),
                                    "running": daemon_running()})

        if path.startswith("/face/"):
            slot = path.split("/")[-1]
            judy = read_json(JUDY, JUDY_DEFAULTS)
            p = (judy.get("face", {}).get("slots", {}) or {}).get(slot)
            if not p or not os.path.exists(p):
                return self._send(404, b"", "image/png")
            ctype = mimetypes.guess_type(p)[0] or "image/png"
            with open(p, "rb") as f:
                return self._send(200, f.read(), ctype)

        return self._send(404, {"error": "no such route"})

    def do_POST(self):
        path = self.path.split("?")[0]
        try:
            b = self._body()
        except Exception as e:
            return self._send(400, {"error": f"bad json: {e}"})

        try:
            if path == "/api/config":
                cfg = read_json(CONFIG, dictation_defaults())
                _merge(cfg, b)
                write_json(CONFIG, cfg)
                LOG.append(f"— config saved: {', '.join(b.keys())}")
                return self._send(200, {"ok": True, "config": cfg})

            if path == "/api/judy":
                judy = read_json(JUDY, JUDY_DEFAULTS)
                _merge(judy, b)
                write_json(JUDY, judy)
                LOG.append(f"— judy.json saved: {', '.join(b.keys())}")
                return self._send(200, {"ok": True, "judy": judy})

            if path == "/api/codebook/test":
                cfg = read_json(CONFIG, dictation_defaults())
                agg = b.get("aggressive", cfg.get("aggressive", False))
                out, hits = codebook.apply(b.get("text", ""), aggressive=agg)
                return self._send(200, {"out": out,
                                        "hits": [{"heard": h, "read": r, "n": n} for h, r, n in hits]})

            if path == "/api/codebook/add":
                row = add_codebook_row(b.get("heard"), b.get("read"), b.get("note", ""))
                return self._send(200, {"ok": True, "row": row})

            if path == "/api/voice/preview":
                judy = read_json(JUDY, JUDY_DEFAULTS)
                v = judy["voice"]
                engine = b.get("engine") or v.get("engine", "piper")
                text = b.get("text") or "Judy on station. Go ahead, Papi."
                if engine == "sapi":
                    sapi_speak(b.get("name", v.get("name")), text,
                               b.get("rate", v.get("rate", 0)),
                               b.get("volume", v.get("volume", 100)))
                else:
                    t0 = time.time()
                    speak.say(text, engine=engine,
                              voice=(b.get("eleven_voice_id") if engine == "elevenlabs"
                                     else b.get("piper_voice")))
                    LOG.append(f"— spoke via {engine} in {time.time() - t0:.2f}s")
                return self._send(200, {"ok": True})

            if path == "/api/face/set":
                slot, src = b.get("slot"), b.get("path")
                if slot not in STATES:
                    raise ValueError(f"unknown slot {slot!r}")
                judy = read_json(JUDY, JUDY_DEFAULTS)
                if b.get("clear"):
                    judy["face"]["slots"][slot] = None
                else:
                    if b.get("data"):
                        os.makedirs(FACES, exist_ok=True)
                        ext = (b.get("name") or "png").rsplit(".", 1)[-1].lower()
                        if ext not in ("png", "gif", "jpg", "jpeg", "webp"):
                            ext = "png"
                        dst = os.path.join(FACES, f"{slot}.{ext}")
                        raw = base64.b64decode(b["data"].split(",")[-1])
                        with open(dst, "wb") as f:
                            f.write(raw)
                        judy["face"]["slots"][slot] = dst
                    elif src:
                        if not os.path.exists(src):
                            raise ValueError(f"no such file: {src}")
                        os.makedirs(FACES, exist_ok=True)
                        dst = os.path.join(FACES, f"{slot}{os.path.splitext(src)[1] or '.png'}")
                        if os.path.abspath(src) != os.path.abspath(dst):
                            shutil.copyfile(src, dst)
                        judy["face"]["slots"][slot] = dst
                    else:
                        raise ValueError("nothing to set")
                write_json(JUDY, judy)
                LOG.append(f"— face[{slot}] set")
                return self._send(200, {"ok": True, "url": face_url(judy, slot)})

            if path == "/api/daemon":
                act = b.get("action")
                if act == "start":
                    extra = []
                    if b.get("no_type"):
                        extra.append("--no-type")
                    if b.get("toggle"):
                        extra.append("--toggle")
                    return self._send(200, {"ok": True, "msg": daemon_start(extra)})
                if act == "stop":
                    return self._send(200, {"ok": True, "msg": daemon_stop()})
                raise ValueError(f"unknown action {act!r}")

            if path == "/api/open":
                target = b.get("target")
                p = {"config": CONFIG, "judy": JUDY, "sop": SOP,
                     "faces": FACES, "dir": HERE}.get(target)
                if not p:
                    raise ValueError("unknown target")
                os.makedirs(p, exist_ok=True) if target == "faces" else None
                os.startfile(p)  # noqa: S606 — local, user-initiated
                return self._send(200, {"ok": True})

        except Exception as e:
            LOG.append(f"! {e}")
            return self._send(400, {"error": str(e)})

        return self._send(404, {"error": "no such route"})


def main():
    ap = argparse.ArgumentParser(description="JUDY's console (BOLO 56)")
    ap.add_argument("--port", type=int, default=8787)
    ap.add_argument("--no-open", action="store_true")
    a = ap.parse_args()

    if not os.path.exists(JUDY):
        write_json(JUDY, JUDY_DEFAULTS)
    os.makedirs(FACES, exist_ok=True)

    url = f"http://127.0.0.1:{a.port}"
    srv = ThreadingHTTPServer(("127.0.0.1", a.port), Handler)
    LOG.append("— console up")
    print(f"JUDY console · {url}")
    print(f"  dictation config  {CONFIG}")
    print(f"  judy config       {JUDY}")
    print("  ctrl-c to stop")
    if not a.no_open:
        threading.Timer(0.6, lambda: webbrowser.open(url)).start()
    try:
        srv.serve_forever()
    except KeyboardInterrupt:
        print("\nstopping…")
        daemon_stop()


if __name__ == "__main__":
    main()
