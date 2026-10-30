"""build_editors_page.py — 10/30: the org page for the eight OXO script editors, plus Chief's private to-do page.
Writes _tools/pages/oxo-editors.html (public-safe) and _PRIVATE/intake/paper/todo.html (private; ORANGE and personal items).
Reads each agent file for its book count so the page stays true. Run: python -X utf8 _tools/pages/build_editors_page.py
"""
import html
import os
import re

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", ".."))
AG = os.path.join(ROOT, ".claude", "agents")
CSS = """:root{--bg:#111;--panel:#1a1a1a;--line:#2e2e2e;--fg:#e8e6e1;--mut:#9b978f;--or:#FF5A1F}
*{box-sizing:border-box}body{margin:0;background:var(--bg);color:var(--fg);font:15px/1.45 system-ui,sans-serif}
header{position:sticky;top:0;height:44px;display:flex;align-items:center;gap:16px;padding:0 16px;background:#0b0b0b;border-bottom:1px solid var(--line);z-index:2}
header b{color:var(--or)}header span{color:var(--mut);font-size:13px}main{max-width:1100px;margin:0 auto;padding:16px}
h2{margin:24px 0 8px;font-size:17px;color:var(--or)}p.m{color:var(--mut);margin:4px 0 10px;font-size:14px}
.flow{display:flex;flex-wrap:wrap;gap:8px;margin:8px 0}.flow div{flex:1 1 200px;background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:10px 12px;font-size:14px}
.flow b{color:var(--or);display:block}.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(310px,1fr));gap:12px}
.card{background:var(--panel);border:1px solid var(--line);border-radius:8px;padding:12px 14px}
.card h3{margin:0;font-size:16px}.card h3 small{color:var(--mut);font-weight:400;font-size:12px;display:block}
.card ul{margin:6px 0;padding-left:18px;font-size:13.5px}.card .bk{color:var(--mut);font-size:12.5px;border-top:1px solid var(--line);padding-top:6px;margin-top:6px}
.tag{display:inline-block;font-size:11px;font-weight:700;border-radius:4px;padding:1px 6px;background:#3a1d12;color:var(--or);margin-right:4px}
.grp{color:var(--mut);font-size:12px;letter-spacing:.06em;text-transform:uppercase;margin:18px 0 6px}
.todo li{margin:8px 0}.todo{padding-left:20px}.rec{color:var(--or);font-weight:600}
@media(max-width:600px){main{padding:12px 16px}}"""

SEATS = [
    ("The story", [
        ("editing-structure", "Structure editor", "Act shape, turning points, pacing, setups and payoffs",
         ["Where each act turns, and whether the midpoint and the climax land", "Setups with no payoff, and payoffs with no setup", "The three slowest and three fastest stretches"]),
        ("editing-character", "Character editor", "Want vs need, arcs, motivation, choices, consistency",
         ["What each lead wants against what they need", "Choices that cost something, and choices that don't", "Where someone acts out of character"]),
        ("editing-theme-tone", "Theme and tone editor", "What the script is about underneath, tone, motifs, genre promises",
         ["The controlling idea, said in one line, and whether the pages prove it", "Tone breaks and motifs that repeat", "Genre promises made and kept or dropped"]),
    ]),
    ("The words", [
        ("editing-dialogue", "Dialogue editor", "Voice, subtext, on-the-nose lines, exposition, rhythm",
         ["Do the characters sound different from each other", "Lines that say the feeling out loud", "Exposition dumps and how they could be hidden"]),
        ("editing-line", "Line editor", "Action-line economy, scene headings, format, readability",
         ["Action blocks over four lines, and things the camera can't see", "Missing or inconsistent scene headings and cue names", "Real typos only (OCR slips are flagged, not counted)"]),
    ]),
    ("The world", [
        ("editing-continuity", "Continuity editor", "Timeline, who-knows-what, names, props, world rules",
         ["A timeline of the script and where it contradicts itself", "Who knows what, and when they learned it", "Names, props, locations and rules that change"]),
        ("editing-production", "Production editor", "What it would cost and demand to shoot or animate",
         ["Locations, cast size, effects and set pieces", "The most expensive beats, and the cheapest way to the same beat", "What an animated version simplifies"]),
    ]),
    ("The outsider", [
        ("reading-cold", "Cold reader", "A first-time reader's honest coverage, with no canon",
         ["What a stranger understands and where they get lost", "Where interest drops", "Pass, consider or recommend, with reasons"]),
    ]),
]


def info(name):
    t = open(os.path.join(AG, name + ".md"), encoding="utf8").read()
    books = re.findall(r"^- BVX\.(\d{4}) · ([^(:]+)", t, re.M)
    return len(books), [b[1].strip() for b in books[:4]]


def editors_page():
    groups = []
    total = 0
    for g, seats in SEATS:
        cards = []
        for name, title, lens, checks in seats:
            n, top = info(name)
            total += n
            lis = "".join(f"<li>{html.escape(c)}</li>" for c in checks)
            cards.append(f'<div class="card"><h3>{html.escape(title)}<small>agent <code>{name}</code> · Sonnet · MS seat</small></h3>'
                         f'<p class="m">{html.escape(lens)}</p><ul>{lis}</ul>'
                         f'<div class="bk"><span class="tag">{n} BOOKS</span>{html.escape("; ".join(top))}{" …" if n > 4 else ""}</div>'
                         f'<div class="bk"><span class="tag">NOT RUN</span>built 10/30, waits on your go</div></div>')
        groups.append(f'<div class="grp">{g}</div><div class="grid">{"".join(cards)}</div>')
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>OXO Script Editors</title><style>{CSS}</style></head><body>
<header><b>OXO SCRIPT EDITORS</b><span>8 seats · {total} book lines wired · none run yet</span></header><main>
<h2>How the run goes</h2><div class="flow">
<div><b>1 · RECON</b>zero tokens: the script file ({'_PRIVATE/BOLO-169/OXO-full-script.txt'.replace('_PRIVATE','private')}), 185 pages, one page per form-feed block</div>
<div><b>2 · ORDER</b>you say go, and name the slice: the whole script or a page range</div>
<div><b>3 · EXECUTE</b>all eight read the same pages at once. They never read each other's reports and never launch agents</div>
<div><b>4 · CONSOLIDATE</b>I merge the eight reports into one list for you. Findings stay in reports and never enter canon until you promote them (BOLO 156)</div></div>
<h2>The seats</h2>
<p class="m">Every editor is advisory: it points to a page with a short quote, ranks each problem A (breaks the story), B (weakens it) or C (polish), names what works, and asks you the questions only you can answer. None rewrites the script. Report size: under 900 words for 40 pages or fewer, under 1,500 for the whole script. The last line of each report is DONE, DONE_WITH_CONCERNS or BLOCKED.</p>
{''.join(groups)}
<h2>Who sits where</h2><p class="m">Structure, character and theme-tone judge the story. Dialogue and line judge the words. Continuity and production judge the world and its cost. The cold reader is the control: it has no canon, so it tells you what the page alone says. Shared rules live in <code>.claude/agents/references/editor-method.md</code>. Books come from the distilled library; the full list per seat is on the books page (oxo-editor-library.html).</p>
</main></body></html>"""


TODO = [
    ("One word unlocks the next build", [
        ("Say go on the script editors.", "Eight editors are built and ready. One pass over the 185-page script costs about 8 agents, around 1 to 1.5 million tokens. Say whole script or give a page range.", True),
        ("Confirm the page count.", "The script came out at 185 pages; you said 300-something. Page 233 has ghost text. Tell me if pages are missing.", False),
        ("Answer the canon condition (BOLO 156).", "Editor findings stay out of canon until you promote them. Say yes to keep that rule.", False),
    ]),
    ("Things only you can do", [
        ("Attach 9 PDFs in Zotero, then say rescan Zotero.", "BVX.0013 Film Production Management · 0068 Conventions and Obligatory Moments · 0094 Conflict and Suspense · 0159 Revision and Self-Editing · 0262 Write to TV · 0264 13 Steps to Evil · 0281 Writing Scary Scenes · 1021 Cinema Genre · 1046 Inside Story.", False),
        ("Paste Copy decisions from the sorter page.", "About 1,000 pages wait on it. Photo pre-fills are wrong for the brochure and the magazines.", False),
        ("Turn four Sprite pages by hand.", "Pages 23, 48, 55 and 56 fed in crooked.", False),
        ("Toss the blank backs from the notebooks.", "The transcripts wait on it.", False),
    ]),
    ("Questions to answer", [
        ("What is the Dramatica story called: Chess Test or Chest Test?", "Five scans carry the guess in their blurbs. I fix them all with one word.", False),
        ("Typewriter pages: which categories?", "The intake bins or your own list. Two batches are in; faint ink lines are unchecked.", False),
        ("Four unanswered blurbs.", "The Dirty Rotten Scoundrels year · why the Tallahassee pages matter · the Sprite film title and year · the Boston Skad phrase.", False),
        ("Recipe cards: handwritten or typed?", "And which notebook is the one I labeled B020.", False),
        ("Poster placement.", "Some pages are unnamed and one name isn't in the performer register. My placement is a provisional call.", False),
    ]),
    ("Offers on the table", [
        ("Distill fix pass.", "Twenty distilled books rest on partial reads. Re-reading only the unread chapters is cheaper than the first pass.", False),
        ("OCR the Ebert clichés book (BVX.1093).", "It is a scanned image with no text layer.", False),
        ("Notebook transcripts.", "502 pages of handwriting; scan-reader agents read the images. Costly, so it waits for your go.", False),
        ("Read the book covers and match them to the library.", "Offered earlier, not requested.", False),
    ]),
]


def todo_page():
    secs = []
    for head, items in TODO:
        lis = "".join(f'<li>{"<span class=rec>★ </span>" if rec else ""}<b>{html.escape(a)}</b><br><span class="m">{html.escape(b)}</span></li>' for a, b, rec in items)
        secs.append(f"<h2>{html.escape(head)}</h2><ol class='todo'>{lis}</ol>")
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Chief's To-Do</title><style>{CSS}</style></head><body>
<header><b>WHAT YOU NEED TO DO</b><span>private · 10/30</span></header><main>{''.join(secs)}
<h2>Done tonight, nothing to do</h2><p class="m">45 books distilled and wired into the editors · Dramatica set scanned and OCR'd (5 scans, 582 pages) · PMBOK, IB diploma, LAN party poster, friend photos, two typewriter batches scanned.</p>
</main></body></html>"""


open(os.path.join(ROOT, "_tools", "pages", "oxo-editors.html"), "w", encoding="utf8").write(editors_page())
os.makedirs(os.path.join(ROOT, "_PRIVATE", "intake", "paper"), exist_ok=True)
open(os.path.join(ROOT, "_PRIVATE", "intake", "paper", "todo.html"), "w", encoding="utf8").write(todo_page())
print("ok")
