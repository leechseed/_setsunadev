"""roster.py - the voices dashboard (Chief, 9/20): every voice the Command has set up, who wears it,
the dials, and a play button for every audition file on disk.
Reads: _tools/dictation/judy.json (JUDY) - _tools/dictation/audition.py (the cast + dial sets) -
SillyTavern's settings (Naked) - _PRIVATE/voice-auditions/*.wav (the samples).
Writes: _PRIVATE/voice-auditions/voices.html (private: the folder is gitignored) and opens it.
    python _tools/voice/roster.py [--no-open]
"""
import os, io, sys, json, glob, html, re, importlib.util

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
DICT = os.path.join(ROOT, "_tools", "dictation")
AUD = os.path.join(ROOT, "_PRIVATE", "voice-auditions")
ST = r"Q:\fun\_ULTRADARK\goon\SillyTavern\data\default-user\settings.json"
OUT = os.path.join(AUD, "voices.html")

sys.path.insert(0, DICT)
spec = importlib.util.spec_from_file_location("audition", os.path.join(DICT, "audition.py"))
aud = importlib.util.module_from_spec(spec)
try:
    spec.loader.exec_module(aud)
except Exception:
    aud = None

judy = json.load(io.open(os.path.join(DICT, "judy.json"), encoding="utf-8"))
jv = judy.get("voice", {})
cast = dict(getattr(aud, "CAST", {})) if aud else {}
dials = {k: getattr(aud, k, None) for k in ("NORMAL", "BRAT", "PEPPER")} if aud else {}

naked_vid, naked_dials, naked_voice, naked_name = None, None, "-", "Sensei"
try:
    nj = json.load(io.open(os.path.join(DICT, "naked.json"), encoding="utf-8"))
    nv = nj.get("voice", {})
    naked_name = nj.get("name", "Sensei")
    naked_vid = nv.get("eleven_voice_id")
    naked_dials = {**(nv.get("eleven_settings") or {}), "model": nv.get("eleven_model")}
    naked_voice = (nv.get("note") or "").split(":")[1].split(" for ")[0].strip() if ":" in (nv.get("note") or "") else "-"
except Exception:
    pass

SEATS = [
    {"seat": "JUDY", "role": "the Command's voice: session voice, the wire, the face", "voice": "Blondie - Conversational, British",
     "vid": jv.get("eleven_voice_id"), "model": jv.get("eleven_model"), "dials": jv.get("eleven_settings"),
     "ruled": "RULED 9/17 off a four-voice audition (Blondie, Emmaline, Amelia, Kira)", "prefix": "blondie", "trunk": "OPERATOR"},
    {"seat": "Pepper", "role": "the yo-yo's explore agent (BOLO 69), the debrief register", "voice": "Monika Sogam - Numbers & Data, en-IN",
     "vid": cast.get("monika", ("", ""))[1], "model": "eleven_turbo_v2_5", "dials": dials.get("PEPPER"),
     "ruled": "RULED 9/18 (Chief's pick; Samara X and Alice auditioned)", "prefix": "monika", "trunk": "OPERATOR/BLACK"},
    {"seat": naked_name, "role": "the goon agent (BOLO 74): her pad, her window beside JUDY, SillyTavern on :8000", "voice": naked_voice,
     "vid": naked_vid, "model": (naked_dials or {}).get("model"), "dials": naked_dials,
     "ruled": "RULED 9/20 05:32: Arabella on v3 conversational for range (JUDY's pick after Chief narrowed it to Arabella or Serafina; Kailey, Anna, Vivian, Jean, Aurelia, Izumi, Serafina auditioned)", "prefix": "sensei--arabella", "trunk": "ORANGE"},
]

wavs = sorted(os.path.basename(p) for p in glob.glob(os.path.join(AUD, "*.wav")))


def files_for(prefix):
    return [w for w in wavs if w.startswith(prefix)]


def dials_html(d):
    if not d:
        return '<span class="muted">dials not recorded</span>'
    return " / ".join("%s <b>%s</b>" % (html.escape(str(k)), html.escape(str(v)))
                      for k, v in d.items() if v is not None and k != "model")


def audio(w):
    label = re.sub(r"\.wav$", "", w)
    return ('<div class="clip"><span>%s</span><audio controls preload="none" src="%s"></audio></div>'
            % (html.escape(label), html.escape(w)))


seats_html = ""
for s in SEATS:
    clips = files_for(s["prefix"])
    seats_html += """
    <section>
      <h2>%s <small>%s</small></h2>
      <p class="role">%s</p>
      <dl class="kv">
        <dt>voice</dt><dd>%s</dd>
        <dt>voice id</dt><dd><code>%s</code></dd>
        <dt>model</dt><dd><code>%s</code></dd>
        <dt>dials</dt><dd>%s</dd>
        <dt>ruling</dt><dd>%s</dd>
      </dl>
      <div class="clips">%s</div>
    </section>""" % (html.escape(s["seat"]), html.escape(s["trunk"]), html.escape(s["role"]), html.escape(s["voice"]),
                     html.escape(str(s["vid"] or "-")), html.escape(str(s["model"] or "-")), dials_html(s["dials"]),
                     html.escape(s["ruled"]), "".join(audio(w) for w in clips) or '<span class="muted">no samples on disk</span>')

bench_prefixes = sorted({w.split("--")[0] for w in wavs if "--" in w} - {"blondie", "monika", "sensei"}) + ["sensei"]
bench_html = ""
for pfx in bench_prefixes:
    clips = [w for w in wavs if w.startswith(pfx + "--") and not w.startswith("sensei--arabella")]
    if not clips:
        continue
    name = cast[pfx][0] if pfx in cast else pfx.title()
    if pfx == "naked":
        name = "Sensei's first audition, 9/20 02:50 (Arabella took it; Kailey, Anna, Vivian benched)"
    if pfx == "sensei":
        name = "Sensei's second audition, 9/20 05:30, on v3 for range (Arabella kept it; Jean, Aurelia, Izumi, Serafina benched)"
    bench_html += '<section class="bench"><h2>%s</h2><div class="clips">%s</div></section>' % (html.escape(name), "".join(audio(w) for w in clips))
loose = [w for w in wavs if "--" not in w]
if loose:
    bench_html += '<section class="bench"><h2>Loose samples</h2><div class="clips">%s</div></section>' % "".join(audio(w) for w in loose)

CSS = """
  :root { --bg:#0F1216; --panel:#171B21; --panel-2:#1F242C; --ink:#E8EAEE; --ink-2:#A9B0BC; --ink-3:#7B8492;
          --accent:#FF6B35; --line:#2B313B; --line-2:#3C4452; --grid:color-mix(in srgb,var(--ink) 8%,transparent);
          --display:"Barlow Condensed",Arial,sans-serif; --body:"Atkinson Hyperlegible","Segoe UI",sans-serif; --mono:"IBM Plex Mono",Consolas,monospace; color-scheme:dark; }
  :root:not([data-theme="light"]) { color-scheme:dark; } :root[data-theme="dark"] { color-scheme:dark; }
  * { box-sizing:border-box; }
  body { margin:0; background:var(--bg); color:var(--ink); font-family:var(--body); font-size:16px; line-height:1.5; background-image:radial-gradient(var(--grid) 1px,transparent 1px); background-size:22px 22px; }
  .wrap { max-width:1180px; margin:0 auto; padding:20px 16px 48px; }
  h1 { margin:0 0 4px; font-family:var(--display); font-weight:800; font-size:44px; line-height:1; text-transform:uppercase; }
  h1 i { display:inline-block; width:12px; height:12px; background:var(--accent); margin-right:10px; transform:translateY(-3px); }
  .sub { font-family:var(--mono); font-size:12px; color:var(--ink-2); margin-bottom:18px; }
  .grid { display:grid; grid-template-columns:repeat(auto-fit,minmax(340px,1fr)); gap:16px; }
  section { background:var(--panel); border:1px solid var(--line); padding:14px 16px 16px; min-width:0; }
  section.bench { grid-column:1/-1; }
  h2 { margin:0 0 6px; font-family:var(--display); font-weight:700; font-size:26px; text-transform:uppercase; display:flex; align-items:baseline; gap:10px; }
  h2 small { font-family:var(--mono); font-size:10.5px; letter-spacing:.12em; color:var(--ink-3); font-weight:400; margin-left:auto; }
  .role { margin:0 0 10px; color:var(--ink-2); font-size:14.5px; }
  .kv { display:grid; grid-template-columns:auto 1fr; gap:4px 12px; margin:0 0 12px; font-size:14px; }
  .kv dt { font-family:var(--mono); font-size:10.5px; letter-spacing:.12em; text-transform:uppercase; color:var(--ink-3); padding-top:3px; }
  .kv dd { margin:0; overflow-wrap:anywhere; } .kv b { color:var(--accent); font-weight:700; }
  code { font-family:var(--mono); font-size:12.5px; background:var(--panel-2); padding:1px 5px; }
  .clips { display:grid; gap:6px; }
  .clip { display:grid; grid-template-columns:1fr auto; gap:10px; align-items:center; padding:4px 0; border-top:1px solid var(--line); font-family:var(--mono); font-size:12px; color:var(--ink-2); }
  .clip audio { height:30px; width:260px; }
  .muted { color:var(--ink-3); }
  .foot { margin-top:22px; font-family:var(--mono); font-size:11px; color:var(--ink-3); }
  @media (max-width:640px) { .clip { grid-template-columns:1fr; } .clip audio { width:100%; } }
"""

page = """<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Voices</title>
<meta name="description" content="Every voice the Command has set up: who wears it, the dials, and every audition on disk with a play button.">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@600;700;800&family=Atkinson+Hyperlegible:wght@400;700&family=IBM+Plex+Mono:wght@400;500&display=swap">
<style>%s</style></head><body><div class="wrap">
  <h1><i></i>Voices</h1>
  <div class="sub">the Command's cast / ElevenLabs / %d audition files on disk / rebuilt by _tools/voice/roster.py</div>
  <div class="grid">%s%s</div>
  <div class="foot">Private page: the folder is gitignored. Rerun <code>python _tools/voice/roster.py</code> after any audition and it picks up the new files.</div>
</div></body></html>""" % (CSS, len(wavs), seats_html, bench_html)

os.makedirs(AUD, exist_ok=True)
io.open(OUT, "w", encoding="utf-8").write(page)
print("wrote", OUT, "-", len(wavs), "files")
if "--no-open" not in sys.argv:
    os.startfile(OUT)
