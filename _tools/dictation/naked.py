"""
naked.py — the second voice in the room (BOLO 74, Chief 9/20: "talk to her like I do you, with the
pads on the Akai, and a window beside you").

She rides inside JUDY's process: the same ears (one whisper on the card), the same MIDI port (Windows
lets one process own it), her own pad, her own face window beside JUDY's, her own mouth (Arabella),
and her own brain (the local model behind KoboldCpp on :5001, her card as the system prompt).

    hold her pad   ->  her face: listening
    release        ->  her face: thinking   (whisper, then her model)
    she answers    ->  her face: talking    (ElevenLabs, Arabella)

Everything lives in naked.json beside this file. Her pad is config.json naked_note
(learn it: python midipad.py --learn-naked). Nothing she hears goes near the chat box.
"""
import io
import json
import os
import queue
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
NAKED = os.path.join(HERE, "naked.json")
POS = os.path.join(HERE, "_nakedpos.json")
STATES = ("idle", "listening", "thinking", "talking")


def cfg():
    try:
        return json.load(io.open(NAKED, encoding="utf-8"))
    except Exception:
        return {}


# ---------------------------------------------------------------- the face

class Face:
    """Her window: a Toplevel of JUDY's root, so both faces share the one Tk main thread.
    Same shape as JUDY's Face — one PNG per state, drag to move, it remembers where.
    Default place: to the left of JUDY, beside her."""

    def __init__(self, root, size=220, judy_pos=None):
        import tkinter as tk
        from PIL import Image, ImageTk

        self.q = queue.Queue()
        self.state = "idle"
        self.root = tk.Toplevel(root)
        self.root.overrideredirect(True)
        self.root.attributes("-topmost", True)
        self.root.configure(bg="#120A10")

        slots = (cfg().get("face", {}) or {}).get("slots", {}) or {}
        self.img = {}
        for s in STATES:
            p = slots.get(s)
            if p and os.path.exists(p):
                im = Image.open(p).convert("RGBA")
                # her sprites are portrait; crop to a square on the face
                w, h = im.size
                side = min(w, h)
                im = im.crop(((w - side) // 2, 0, (w - side) // 2 + side, side)).resize((size, size), Image.LANCZOS)
                bg = Image.new("RGBA", im.size, (18, 10, 16, 255))
                self.img[s] = ImageTk.PhotoImage(Image.alpha_composite(bg, im))
        if not self.img:
            raise RuntimeError("no faces for Naked — naked.json face.slots")

        self.label = tk.Label(self.root, bd=0, highlightthickness=0, bg="#120A10")
        self.label.pack()
        self.cap = tk.Label(self.root, text=f"{cfg().get('name','Sensei').lower()} · idle", bg="#120A10", fg="#8E7686",
                            font=("Consolas", 9), wraplength=size, justify="left", anchor="w", padx=8, pady=5)
        self.cap.pack(fill="x")
        self._paint("idle")
        self._place(size, judy_pos)
        self._drag()
        self.root.bind("<Button-3>", lambda e: self.root.withdraw())
        self.root.after(80, self._pump)

    def _place(self, size, judy_pos):
        try:
            p = json.load(io.open(POS, encoding="utf-8"))
            self.root.geometry(f"+{int(p['x'])}+{int(p['y'])}")
            return
        except Exception:
            pass
        if judy_pos:
            self.root.geometry(f"+{int(judy_pos[0]) - size - 12}+{int(judy_pos[1])}")   # beside JUDY, her left
        else:
            sw = self.root.winfo_screenwidth()
            sh = self.root.winfo_screenheight()
            self.root.geometry(f"+{sw - 2 * size - 84}+{sh - size - 180}")

    def _drag(self):
        d = {}

        def down(e):
            d["x"], d["y"] = e.x_root, e.y_root
            d["gx"], d["gy"] = self.root.winfo_x(), self.root.winfo_y()

        def move(e):
            if "x" in d:
                self.root.geometry(f"+{d['gx'] + (e.x_root - d['x'])}+{d['gy'] + (e.y_root - d['y'])}")

        def up(_e):
            try:
                io.open(POS, "w", encoding="utf-8").write(json.dumps({"x": self.root.winfo_x(), "y": self.root.winfo_y()}))
            except Exception:
                pass
            d.clear()

        for w in (self.label, self.cap):
            w.bind("<Button-1>", down)
            w.bind("<B1-Motion>", move)
            w.bind("<ButtonRelease-1>", up)

    def _paint(self, state):
        im = self.img.get(state) or self.img.get("idle")
        if im:
            self.label.configure(image=im)
            self.label.image = im

    def _pump(self):
        try:
            while True:
                kind, val = self.q.get_nowait()
                if kind == "state":
                    self.state = val
                    self._paint(val)
                    self.cap.configure(text=f"{cfg().get('name','Sensei').lower()} · {val}", fg="#FF7DAA" if val != "idle" else "#8E7686")
                elif kind == "text":
                    self.cap.configure(text=val, fg="#C4AEBB")
        except queue.Empty:
            pass
        self.root.after(80, self._pump)

    def set(self, state):
        self.q.put(("state", state))

    def say(self, text):
        self.q.put(("text", text))


class NoFace:
    def set(self, state):
        print(f"  [naked {state}]")

    def say(self, text):
        print(f"  {text}")


# ---------------------------------------------------------------- the brain

class Brain:
    """Her card as the system prompt, a rolling history, the local model on :5001.
    History is kept on disk so she remembers across restarts; `forget()` wipes it."""

    def __init__(self):
        c = cfg()
        self.url = c.get("server", "http://127.0.0.1:5001")
        self.card_path = c.get("card")
        self.history_path = c.get("history", os.path.join(HERE, "_naked_history.json"))
        self.keep = int(c.get("history_turns", 24))
        self.max_tokens = int(c.get("max_tokens", 160))
        self.user = c.get("user_name", "Chief")
        self.card = self._card()
        self.history = self._load()

    def _card(self):
        try:
            d = json.load(io.open(self.card_path, encoding="utf-8"))["data"]
        except Exception:
            return {"name": cfg().get("name", "Sensei"), "system_prompt": "You are Sensei, a bratty adult woman. Stay in character.", "first_mes": ""}
        return d

    def _load(self):
        try:
            return json.load(io.open(self.history_path, encoding="utf-8"))
        except Exception:
            return []

    def _save(self):
        try:
            io.open(self.history_path, "w", encoding="utf-8").write(json.dumps(self.history[-self.keep * 2:], ensure_ascii=False, indent=1))
        except Exception:
            pass

    def forget(self):
        self.history = []
        self._save()

    def system(self):
        d = self.card
        sub = lambda s: (s or "").replace("{{char}}", d.get("name", "Naked")).replace("{{user}}", self.user)
        parts = [sub(d.get("system_prompt")), "",
                 "Who you are: " + sub(d.get("description")), "",
                 "How you are: " + sub(d.get("personality")), "",
                 "The scene: " + sub(d.get("scenario")), "",
                 "You are speaking out loud, over a voice, not typing: no stage directions, no asterisks, "
                 "no narration of your own actions unless you say it as words. Two to four sentences. "
                 f"The one talking to you is {self.user}."]
        return "\n".join(p for p in parts if p is not None)

    def answer(self, heard):
        msgs = [{"role": "system", "content": self.system()}]
        if not self.history and self.card.get("first_mes"):
            msgs.append({"role": "assistant", "content": self.card["first_mes"].replace("{{user}}", self.user)})
        msgs += self.history[-self.keep * 2:]
        msgs.append({"role": "user", "content": heard})
        body = {"model": "naked", "messages": msgs, "max_tokens": self.max_tokens, "temperature": 0.9,
                "top_p": 0.95, "stop": [f"{self.user}:", "\n\n\n"]}
        r = urllib.request.urlopen(urllib.request.Request(self.url + "/v1/chat/completions", data=json.dumps(body).encode(),
                                   headers={"Content-Type": "application/json"}), timeout=180)
        text = json.load(r)["choices"][0]["message"]["content"].strip()
        text = _despeak(text)
        self.history += [{"role": "user", "content": heard}, {"role": "assistant", "content": text}]
        self._save()
        return text

    def up(self):
        try:
            urllib.request.urlopen(self.url + "/api/v1/model", timeout=2)
            return True
        except Exception:
            return False


def _despeak(t):
    """Strip roleplay furniture so the mouth does not read asterisks."""
    import re
    t = re.sub(r"\*[^*]*\*", "", t)            # *actions*
    t = re.sub(r"^\s*(Naked|Sensei)\s*:\s*", "", t)      # a stray name label
    t = re.sub(r"\s{2,}", " ", t).strip()
    return t


# ---------------------------------------------------------------- the mouth

def speak(text, blocking=True):
    import speak as mouth
    v = cfg().get("voice", {})
    wav = mouth.synth_eleven(text, voice_id=v.get("eleven_voice_id"), model=v.get("eleven_model"),
                             settings=v.get("eleven_settings"))
    mouth.play(wav)
    if blocking:
        mouth._wait(wav)
    return wav


# ---------------------------------------------------------------- the turn

class Naked:
    """One exchange with her: heard text in, her spoken answer out. Called by JUDY's loop."""

    def __init__(self, face, speak_replies=True):
        self.face = face
        self.speak_replies = speak_replies
        self.brain = Brain()

    def turn(self, heard):
        if not heard:
            self.face.set("idle")
            return None
        print(f"\n  you   > {heard}")
        self.face.say(f"you: {heard}")
        self.face.set("thinking")
        import re
        if re.match(r"^\W*((naked|sensei)\W+)?(forget|wipe)(\W+(it|everything|all|that))?\W*$", heard.strip(), re.I):
            # the wipe word (Chief 9/20): she keeps her card, JUDY included; the conversation goes
            self.brain.forget()
            line = "Wiped. Clean slate, Chief. JUDY stays, everything else is gone."
            print(f"  naked > {line}")
            self.face.say(line)
            if self.speak_replies:
                try:
                    self.face.set("talking")
                    speak(line, blocking=True)
                except Exception as e:
                    print(f"  ! her mouth failed: {e}")
            self.face.set("idle")
            return line
        if not self.brain.up():
            line = "My brain's not up yet, Chief. Say Sensei, and I'm yours."
            print(f"  naked ! {line}")
            self.face.say(line)
            if self.speak_replies:
                try:
                    self.face.set("talking")
                    speak(line, blocking=True)   # her mouth works without her brain: say it, don't sit there listening
                except Exception as e:
                    print(f"  ! her mouth failed: {e}")
            self.face.set("idle")
            return None
        try:
            reply = self.brain.answer(heard)
        except Exception as e:
            print(f"  ! naked brain failed: {e}")
            self.face.set("idle")
            return None
        print(f"  naked > {reply}")
        self.face.say(reply)
        self.face.set("talking")
        if self.speak_replies and reply:
            try:
                import squelch
                squelch.key_up()
                speak(reply, blocking=True)
                squelch.key_down()
            except Exception as e:
                print(f"  ! her mouth failed: {e}")
        self.face.set("idle")
        return reply


if __name__ == "__main__":
    import sys
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    text = " ".join(sys.argv[1:]) or "Naked, copy?"
    Naked(NoFace(), speak_replies="--no-voice" not in sys.argv).turn(text.replace("--no-voice", "").strip())
