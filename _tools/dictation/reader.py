"""
reader.py — session voice. JUDY reads the VS Code session aloud as it is written.

BOLO 56, FRAGO 9/17 ("session voice"). Chief talks into the chat, Fable answers in
the chat, and this follows the session's transcript on disk and speaks every block
Fable writes, sentence by sentence, as it lands — she starts on the first sentence
while the third is still being written. A new turn from Chief cuts her off and
plays an acknowledgment so the wait has a voice.

    python reader.py                 # follow the newest session, speak it
    python reader.py --test          # speak the last block Fable wrote, then exit
    python reader.py --transcript P  # follow one file
    python judy.py --session         # the same reader with the face and the ears

Speech form. Replies are written for the eye. The reader:
  · speaks only the marked line when one exists:   <!-- say: ... -->
    (SOP §7 rule 10 — Fable opens a long reply with what she should say)
  · otherwise strips markdown, skips code and tables, reads links by label,
    and stops after `max_sentences` with "the rest is on screen"
  · mode "haiku" (judy.json → session.reader) rewrites each block into talk
    through the bundled claude CLI first — conversational, two to three seconds
    slower per block; "script" is the default.
"""

import argparse
import glob
import io
import json
import os
import queue
import random
import re
import subprocess
import sys
import threading
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)

import speak  # noqa: E402

JUDY = os.path.join(HERE, "judy.json")
ACKS = os.path.join(ROOT, "_PRIVATE", "voice-acks")
# RULED 2026-09-17 by Chief: only these prowords confirm receipt ("copy" · "good traffic, stand by").
ACK_LINES = ["Copy.", "Good traffic, stand by."]
SAY = re.compile(r"<!--\s*say:\s*(.*?)\s*-->", re.S | re.I)


def scfg():
    base = {"reader": "script", "max_sentences": 12, "acks": True, "min_chars": 12}
    try:
        j = json.load(io.open(JUDY, encoding="utf-8"))
        return {**base, **(j.get("session") or {})}
    except Exception:
        return base


# ---------------------------------------------------------------- the transcript

def project_dir():
    """~/.claude/projects/<slug>/ for this repo. The slug is the path with every
    separator and underscore turned into a dash; the drive letter is lowercased."""
    home = os.path.expanduser("~")
    base = os.path.join(home, ".claude", "projects")
    slug = ROOT.replace(":", "-").replace("\\", "-").replace("/", "-").replace("_", "-")
    slug = slug[0].lower() + slug[1:]
    p = os.path.join(base, slug)
    if os.path.isdir(p):
        return p
    tail = os.path.basename(ROOT).replace("_", "-").lower()
    for d in glob.glob(os.path.join(base, "*")):
        if os.path.isdir(d) and d.lower().endswith(tail):
            return d
    raise RuntimeError(f"no transcript folder for {ROOT} under {base}")


def newest_transcript(folder):
    fs = [f for f in glob.glob(os.path.join(folder, "*.jsonl"))]
    if not fs:
        return None
    return max(fs, key=os.path.getmtime)


def parse(line):
    try:
        d = json.loads(line)
    except Exception:
        return None
    if d.get("isSidechain"):
        return None
    t = d.get("type")
    m = d.get("message") or {}
    c = m.get("content")
    if t == "assistant" and isinstance(c, list):
        texts = [b.get("text", "") for b in c if b.get("type") == "text"]
        texts = [x for x in texts if x and x.strip()]
        if texts:
            return ("assistant", "\n\n".join(texts))
    if t == "user" and d.get("promptSource"):
        # a real prompt from Chief; injected skill text and tool results carry no promptSource
        if isinstance(c, str):
            return ("user", c)
        if isinstance(c, list):
            texts = [b.get("text", "") for b in c if b.get("type") == "text"]
            if texts and not any(b.get("type") == "tool_result" for b in c):
                return ("user", "\n".join(texts))
    return None


# ---------------------------------------------------------------- speech form

def plain(md):
    """Markdown for the eye → sentences for the ear."""
    s = md
    s = re.sub(r"<!--.*?-->", " ", s, flags=re.S)
    s = re.sub(r"```.*?```", " ", s, flags=re.S)
    s = "\n".join(l for l in s.splitlines() if not l.strip().startswith("|"))
    s = re.sub(r"^\s{0,3}#{1,6}\s*", "", s, flags=re.M)
    s = re.sub(r"\[\[([^\]|]+)\|([^\]]+)\]\]", r"\2", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    s = re.sub(r"https?://\S+", "the link", s)
    s = re.sub(r"`([^`]*)`", r"\1", s)
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s, flags=re.S)
    s = re.sub(r"(?<!\w)[*_](.+?)[*_](?!\w)", r"\1", s)
    s = re.sub(r"^\s*(?:[-*+]|\d+\.)\s+", "", s, flags=re.M)
    s = re.sub(r"[\U0001F300-\U0001FAFF☀-➿]", "", s)
    s = s.replace("—", ", ").replace("–", ", ").replace(" · ", ", ")
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n{2,}", "\n", s)
    return s.strip()


def sentences(text):
    out = []
    for para in text.split("\n"):
        para = para.strip()
        if not para:
            continue
        for s in re.split(r"(?<=[.!?])\s+(?=[A-Z0-9\"'])", para):
            s = s.strip()
            if s:
                if s[-1] not in ".!?":
                    s += "."
                out.append(s)
    return out


def speech_form(block, cfg):
    m = SAY.search(block)
    if m:
        return sentences(m.group(1)), "say-line"
    if cfg.get("reader") == "haiku":
        r = rewrite_haiku(block)
        if r:
            return sentences(r), "haiku"
    ss = sentences(plain(block))
    cap = int(cfg.get("max_sentences") or 0)
    if cap and len(ss) > cap:
        ss = ss[:cap] + ["The rest is on screen."]
    return ss, "script"


# ---------------------------------------------------------------- the haiku rewrite

def claude_exe():
    e = os.environ.get("CLAUDE_EXE")
    if e and os.path.exists(e):
        return e
    home = os.path.expanduser("~")
    hits = glob.glob(os.path.join(home, ".vscode", "extensions", "anthropic.claude-code-*",
                                  "resources", "native-binary", "claude.exe"))
    if hits:
        return max(hits, key=os.path.getmtime)
    import shutil
    return shutil.which("claude")


REWRITE = ("Rewrite the following assistant reply as two to four spoken sentences, "
           "the way a sharp, affable, slightly bratty British handler would say it out "
           "loud to the person she works for. Keep every fact; drop formatting, paths, "
           "and URLs. Output only the sentences.\n\n")


def rewrite_haiku(block, timeout=25):
    exe = claude_exe()
    if not exe:
        return None
    env = {k: v for k, v in os.environ.items() if k not in ("CLAUDECODE", "CLAUDE_CODE_ENTRYPOINT")}
    try:
        r = subprocess.run([exe, "-p", REWRITE + block[:6000], "--model", "haiku",
                            "--output-format", "text"],
                           capture_output=True, text=True, timeout=timeout, env=env,
                           cwd=ROOT, encoding="utf-8", errors="replace")
        out = (r.stdout or "").strip()
        return out or None
    except Exception:
        return None


# ---------------------------------------------------------------- the mouth

def synth(text, path):
    v = speak.read_judy()["voice"]
    if v.get("engine") == "elevenlabs":
        return speak.synth_eleven(text, out_wav=path)
    return speak.synth_piper(text, voice=v.get("piper_voice") or None, out_wav=path)


def wav_seconds(path):
    import wave
    try:
        with wave.open(path, "rb") as w:
            return w.getnframes() / float(w.getframerate())
    except Exception:
        return 0.0


def purge():
    try:
        import winsound
        winsound.PlaySound(None, winsound.SND_PURGE)
    except Exception:
        pass


def ensure_acks():
    os.makedirs(ACKS, exist_ok=True)
    have = glob.glob(os.path.join(ACKS, "*.wav"))
    if have:
        return have
    out = []
    for i, line in enumerate(ACK_LINES):
        p = os.path.join(ACKS, f"ack{i}.wav")
        try:
            synth(line, p)
            out.append(p)
        except Exception as e:
            print(f"  ! ack render failed: {e}")
            break
    return out


class Mouth:
    """Sentences in, speech out, in order, interruptible. The producer synthesizes
    one sentence ahead of the player so there is no gap between sentences."""

    def __init__(self, face=None, log=print):
        self.face = face
        self.log = log
        self.q = queue.Queue()
        self.gen = 0            # bumps on interrupt; stale work is dropped
        self.lock = threading.Lock()
        self.n = 0
        threading.Thread(target=self._run, daemon=True).start()

    def speak(self, sents, tag=""):
        with self.lock:
            g = self.gen
        for s in sents:
            self.q.put((g, s, tag))

    def interrupt(self):
        with self.lock:
            self.gen += 1
        purge()
        try:
            while True:
                self.q.get_nowait()
        except queue.Empty:
            pass

    def ack(self):
        acks = ensure_acks()
        if acks:
            speak.play(random.choice(acks))

    def _run(self):
        tmp = os.path.join(HERE, "_reader")
        os.makedirs(tmp, exist_ok=True)
        pending = None  # (gen, wav path, seconds, sentence)
        while True:
            g, s, tag = self.q.get()
            with self.lock:
                if g != self.gen:
                    continue
            # synthesize this one; play the previous while it renders
            self.n += 1
            p = os.path.join(tmp, f"s{self.n % 8}.wav")
            t0 = time.perf_counter()
            try:
                synth(s, p)
            except Exception as e:
                self.log(f"  ! synth failed: {e}")
                continue
            dt = time.perf_counter() - t0
            with self.lock:
                if g != self.gen:
                    continue
            if self.face:
                self.face.set("talking")
                self.face.say(s)
            self.log(f"  judy > {s}   [{tag} · {dt:.2f}s synth]")
            speak.play(p)
            secs = wav_seconds(p)
            # wait out the clip, but stay interruptible
            end = time.time() + secs
            while time.time() < end:
                with self.lock:
                    if g != self.gen:
                        break
                time.sleep(0.05)
            if self.q.empty() and self.face:
                self.face.set("idle")


# ---------------------------------------------------------------- the reader

class Reader:
    def __init__(self, face=None, transcript=None, log=print):
        self.face = face
        self.log = log
        self.cfg = scfg()
        self.mouth = Mouth(face, log)
        self.folder = None if transcript else project_dir()
        self.path = transcript
        self.pos = 0
        self.stop = threading.Event()

    def _pick(self):
        if self.folder:
            p = newest_transcript(self.folder)
            if p and p != self.path:
                self.path = p
                self.pos = os.path.getsize(p)   # start at the end: never read history aloud
                self.log(f"  following {os.path.basename(p)}")

    def _handle(self, kind, text):
        if kind == "user":
            self.mouth.interrupt()
            if self.face:
                self.face.set("thinking")
                self.face.say("you: " + text[:120])
            if self.cfg.get("acks", True):
                self.mouth.ack()
            self.log(f"\n  you  > {text[:100]}")
        elif kind == "assistant":
            if len(text.strip()) < int(self.cfg.get("min_chars", 12)):
                return
            self.cfg = scfg()
            sents, tag = speech_form(text, self.cfg)
            if sents:
                self.mouth.speak(sents, tag)

    def run(self):
        self._pick()
        if not self.path:
            self.log("  no transcript yet — waiting for a session")
        buf = ""
        last_scan = 0
        while not self.stop.is_set():
            if time.time() - last_scan > 5:
                self._pick()
                last_scan = time.time()
            if self.path and os.path.exists(self.path):
                size = os.path.getsize(self.path)
                if size < self.pos:
                    self.pos = 0
                if size > self.pos:
                    with io.open(self.path, "r", encoding="utf-8", errors="replace") as f:
                        f.seek(self.pos)
                        chunk = f.read()
                        self.pos = f.tell()
                    buf += chunk
                    while "\n" in buf:
                        line, buf = buf.split("\n", 1)
                        r = parse(line)
                        if r:
                            self._handle(*r)
            time.sleep(0.25)

    def test(self):
        """Speak the last block Fable wrote in the newest transcript, then exit."""
        self._pick()
        last = None
        with io.open(self.path, "r", encoding="utf-8", errors="replace") as f:
            for line in f:
                r = parse(line)
                if r and r[0] == "assistant":
                    last = r[1]
        if not last:
            self.log("  nothing to read")
            return
        sents, tag = speech_form(last, self.cfg)
        self.log(f"  {len(sents)} sentence(s) via {tag}")
        self.mouth.speak(sents, tag)
        while not self.mouth.q.empty():
            time.sleep(0.2)
        time.sleep(1.0)


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="JUDY — session voice (BOLO 56)")
    ap.add_argument("--transcript", help="follow this file instead of the newest session")
    ap.add_argument("--test", action="store_true", help="speak the last block Fable wrote, then exit")
    a = ap.parse_args()
    r = Reader(transcript=a.transcript)
    print(f"JUDY · session voice · reader={r.cfg.get('reader')} · cap={r.cfg.get('max_sentences')}")
    if a.test:
        r.test()
        return
    r.run()


if __name__ == "__main__":
    main()
