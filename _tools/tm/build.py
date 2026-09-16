"""TM (Technical Manual) page — build.

Usage:  python _tools/tm/build.py 04

Parses a system SSOT markdown file (ShroomsQ/_CANON/_SSOT/...) into a data blob and
renders _tools/tm/out/TM-<NN>.html from template.html. Tolerant parser: 03 (setting)
renders rougher than 04 (plot) but must not crash.

Inputs : _tools/tm/systems.json     NN -> path · title · short name · shelf
         _tools/tm/terms.json       the term register for the hover tooltips
         _tools/tm/template.html    the page (artifact fragment)
Outputs: _tools/tm/out/TM-<NN>.html
"""
import io, json, os, re, sys, tempfile

sys.stdout.reconfigure(encoding="utf-8", errors="replace")

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))

TERMS = {}
TERMS_WIRED = [0]
USED_TERMS_GLOBAL = set()
SLICE_ROWS = []
INSTANCE_BY_ID = {}

LAYER_TERM_MAP = {
    "P1": "p1-address", "P2": "p2-driver", "P3": "p3-value-in", "P4": "p4-turn",
    "P5": "p5-value-out", "P6": "p6-signpost-seat", "P7": "p7-reveal", "P8": "p8-collision",
    "P9": "p9-stakes", "P10": "p10-genre-obligation", "P11": "p11-time", "P12": "p12-function",
    "S1": "s1-body", "S2": "s2-weather", "S3": "s3-sensorium", "S4": "s4-law",
    "S5": "s5-scar", "S6": "s6-economy", "S7": "s7-founding", "S8": "s8-habit",
    "S9": "s9-allure", "S10": "s10-underside", "S11": "s11-vector", "S12": "s12-function",
}


def load_text(p):
    with io.open(p, encoding="utf-8") as f:
        return f.read()


def load_json(p):
    return json.loads(load_text(p))


def esc(s):
    return (str(s) if s is not None else "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;").replace('"', "&quot;")


# ---------------------------------------------------------------- frontmatter

def parse_frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", text, re.S)
    if not m:
        return {}, text
    fm_text, body = m.group(1), m.group(2)
    fm = {}
    for line in fm_text.split("\n"):
        mm = re.match(r"^([A-Za-z_][A-Za-z0-9_]*):\s*(.*)$", line)
        if not mm:
            continue
        key, val = mm.group(1), mm.group(2).strip()
        if val.startswith("["):
            inner = val.strip()[1:-1] if val.strip().endswith("]") else val.strip()[1:]
            items = [x.strip().strip('"').strip("'") for x in inner.split(",") if x.strip()]
            fm[key] = items
        elif val.startswith('"'):
            v = val[1:]
            if v.endswith('"'):
                v = v[:-1]
            v = v.replace('\\"', '"')
            fm[key] = v
        elif val:
            fm[key] = val
    return fm, body


def parse_title(body):
    m = re.search(r"^#\s+(.*)$", body, re.M)
    if not m:
        return "UNTITLED", "", body
    h1 = m.group(1).strip()
    rest = body[m.end():]
    h1 = re.sub(r"^📐?\s*SSOT\s*[:·]?\s*", "", h1).strip()
    parts = re.split(r"\s+[—·]\s+", h1, maxsplit=1)
    title = parts[0].strip()
    subtitle = parts[1].strip() if len(parts) > 1 else ""
    return title, subtitle, rest


# ---------------------------------------------------------------- text helpers

def strip_md(text):
    if text is None:
        return ""
    s = text
    s = re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", lambda m: m.group(2) or (TERMS.get(m.group(1).strip(), {}).get("t") or m.group(1)), s)
    s = re.sub(r"\*\*(.+?)\*\*", r"\1", s)
    s = re.sub(r"`([^`]+)`", r"\1", s)
    s = re.sub(r"(?<!\*)\*(?!\*)(.+?)(?<!\*)\*(?!\*)", r"\1", s)
    s = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", s)
    return s.strip()


def render_inline(text, count=True):
    if text is None:
        return ""
    s = esc(text)
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"`([^`]+)`", r'<code class="inl">\1</code>', s)

    def wiki_repl(m):
        key = m.group(1).strip()
        label = m.group(2)
        g = TERMS.get(key)
        shown = label if label else (g["t"] if g else key)
        if not g:
            return shown
        if count:
            TERMS_WIRED[0] += 1
            USED_TERMS_GLOBAL.add(key)
        return f'<a class="t" data-t="{esc(key)}" tabindex="0">{shown}</a>'

    s = re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", wiki_repl, s)

    def link_repl(m):
        txt, url = m.group(1), m.group(2)
        if re.match(r"^https?://", url):
            return f'<a href="{esc(url)}" target="_blank" rel="noopener">{txt}</a>'
        return f'<span class="pathref" title="{esc(url)}">{txt}</span>'

    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link_repl, s)
    s = re.sub(r"(?<!\*)\*(?!\*)([^*]+?)(?<!\*)\*(?!\*)", r"<em>\1</em>", s)
    return s


def check_missing_keys(text):
    missing = set()
    for m in re.finditer(r"\[\[([^\]|]+)", text):
        key = m.group(1).strip()
        if key not in TERMS:
            missing.add(key)
    return sorted(missing)


# ---------------------------------------------------------------- auto-linker

def auto_link_section(text):
    store = []

    def protect(pattern, s, flags=0):
        def repl(m):
            store.append(m.group(0))
            return f"\x00P{len(store)-1}\x00"
        return re.sub(pattern, repl, s, flags=flags)

    t = text
    t = protect(r"```.*?```", t, re.S)
    t = protect(r"`[^`\n]+`", t)
    t = protect(r"\[\[[^\]]*\]\]", t)
    t = protect(r"\[[^\]]+\]\([^)]+\)", t)

    used = set()
    for stored in store:
        mm = re.match(r"^\[\[([^\]|]+)", stored)
        if mm:
            used.add(mm.group(1).strip())

    terms_sorted = sorted(TERMS.items(), key=lambda kv: -len(kv[1].get("t", "")))
    for key, val in terms_sorted:
        if key in used:
            continue
        display = val.get("t", "")
        if not display or len(display) < 3:
            continue
        pattern = r"\b" + re.escape(display) + r"\b"
        m = re.search(pattern, t, flags=re.I)
        if m:
            matched_text = m.group(0)
            replacement = f"[[{key}|{matched_text}]]"
            store.append(replacement)
            placeholder = f"\x00P{len(store)-1}\x00"
            t = t[:m.start()] + placeholder + t[m.end():]
            used.add(key)

    return re.sub(r"\x00P(\d+)\x00", lambda m: store[int(m.group(1))], t)


# ---------------------------------------------------------------- block parser

def split_blocks(text):
    lines = text.split("\n")
    n = len(lines)
    blocks = []
    para_buf = []

    def flush_para():
        if para_buf:
            joined = " ".join(l.strip() for l in para_buf if l.strip())
            if joined:
                blocks.append({"type": "p", "text": joined})
            para_buf.clear()

    i = 0
    while i < n:
        raw_line = lines[i]
        s = raw_line.strip()
        if s == "":
            flush_para(); i += 1; continue
        if re.match(r"^-{3,}$", s):
            flush_para(); i += 1; continue
        if s.startswith("```"):
            flush_para()
            lang = s[3:].strip()
            body_lines = []
            i += 1
            while i < n and not lines[i].strip().startswith("```"):
                body_lines.append(lines[i]); i += 1
            i += 1
            blocks.append({"type": "code", "lang": lang, "text": "\n".join(body_lines)})
            continue
        if s.startswith("#### ") or s.startswith("### "):
            flush_para()
            level = 3 if s.startswith("### ") else 4
            heading_text = s.lstrip("#").strip()
            blocks.append({"type": "h", "level": level, "text": heading_text})
            i += 1; continue
        if re.match(r"^\|.*\|\s*$", s):
            flush_para()
            table_lines = []
            while i < n and re.match(r"^\|.*\|\s*$", lines[i].strip()):
                table_lines.append(lines[i].strip()); i += 1
            blocks.append({"type": "table", "lines": table_lines})
            continue
        if re.match(r"^\d+\.\s+", s):
            flush_para()
            items = []; cur = None
            while i < n:
                s2 = lines[i].strip()
                mm = re.match(r"^\d+\.\s+(.*)$", s2)
                if mm:
                    if cur is not None:
                        items.append(cur)
                    cur = mm.group(1); i += 1
                elif s2 == "":
                    break
                elif re.match(r"^\|.*\|\s*$", s2) or s2.startswith("```") or s2.startswith("#"):
                    break
                else:
                    if cur is not None:
                        cur += " " + s2
                    i += 1
            if cur is not None:
                items.append(cur)
            blocks.append({"type": "ol", "items": items})
            continue
        if re.match(r"^[-*]\s+", s):
            flush_para()
            items = []; cur = None
            while i < n:
                s2 = lines[i].strip()
                mm = re.match(r"^[-*]\s+(.*)$", s2)
                if mm:
                    if cur is not None:
                        items.append(cur)
                    cur = mm.group(1); i += 1
                elif s2 == "":
                    break
                elif re.match(r"^\|.*\|\s*$", s2) or s2.startswith("```") or s2.startswith("#"):
                    break
                else:
                    if cur is not None:
                        cur += " " + s2
                    i += 1
            if cur is not None:
                items.append(cur)
            blocks.append({"type": "ul", "items": items})
            continue
        para_buf.append(raw_line); i += 1
    flush_para()
    return blocks


def compute_captions(blocks):
    n = len(blocks)
    consumed = set()
    captions = {}
    for idx, b in enumerate(blocks):
        if b["type"] == "code" and b.get("lang") == "mermaid":
            cap_idx = None
            if idx - 1 >= 0 and blocks[idx - 1]["type"] == "p" and (idx - 1) not in consumed:
                cap_idx = idx - 1
            elif idx + 1 < n and blocks[idx + 1]["type"] == "p" and (idx + 1) not in consumed:
                cap_idx = idx + 1
            if cap_idx is not None:
                captions[idx] = blocks[cap_idx]["text"]
                consumed.add(cap_idx)
            else:
                captions[idx] = None
    return consumed, captions


def parse_table(table_lines):
    def split_row(line):
        line = line.strip()
        if line.startswith("|"):
            line = line[1:]
        if line.endswith("|"):
            line = line[:-1]
        # a [[key|label]] wiki-link (inserted by the auto-linker or written by hand) can
        # carry a literal "|" — protect it before splitting the row into cells, or the
        # label half of the link ends up torn into its own column.
        protected = re.sub(r"\[\[([^\]]*?)\]\]", lambda m: "[[" + m.group(1).replace("|", "\x00PIPE\x00") + "]]", line)
        cells = [c.strip() for c in protected.split("|")]
        return [c.replace("\x00PIPE\x00", "|") for c in cells]
    header = split_row(table_lines[0]) if table_lines else []
    rows = [split_row(l) for l in table_lines[2:]] if len(table_lines) > 2 else []
    return header, rows


def layer_id_from_cell(cell):
    m = re.search(r"([A-Z]{1,2}\d{1,2})", cell or "")
    return m.group(1) if m else None


def render_table_html(header, rows, layer_ids=False):
    thead = "<tr>" + "".join(f"<th>{esc(h)}</th>" for h in header) + "</tr>"
    body_rows = []
    for r in rows:
        attrs = ""
        if layer_ids and r:
            lid = layer_id_from_cell(r[0])
            if lid:
                attrs = f' id="layer-{lid}" class="layer-row" data-layer="{lid}"'
        cells = "".join(f"<td>{render_inline(c)}</td>" for c in r)
        body_rows.append(f"<tr{attrs}>{cells}</tr>")
    return f'<div class="tblwrap"><table class="doct"><thead>{thead}</thead><tbody>{"".join(body_rows)}</tbody></table></div>'


def extract_slice(header, rows):
    for r in rows:
        if not r:
            continue
        lid = layer_id_from_cell(r[0])
        if not lid:
            continue
        name = strip_md(r[1]) if len(r) > 1 else lid
        fields = {}
        for h, v in zip(header[2:], r[2:]):
            fields[strip_md(h)] = render_inline(v, count=False)
        SLICE_ROWS.append({"id": lid, "name": name, "fields": fields, "term": LAYER_TERM_MAP.get(lid, "")})


def extract_instance(header, rows):
    for r in rows:
        if not r:
            continue
        lid = layer_id_from_cell(r[0])
        if not lid:
            continue
        fields = {}
        for h, v in zip(header[1:], r[1:]):
            fields[strip_md(h)] = render_inline(v, count=False)
        INSTANCE_BY_ID[lid] = fields


def render_block(b, idx, captions, layer_ids=False):
    if b["type"] == "h":
        return f'<h{b["level"]} class="subh">{render_inline(b["text"])}</h{b["level"]}>'
    if b["type"] == "p":
        return f'<p class="plain">{render_inline(b["text"])}</p>'
    if b["type"] == "code":
        if b.get("lang") == "mermaid":
            cap = captions.get(idx)
            cap_html = f"<figcaption>{render_inline(cap)}</figcaption>" if cap else ""
            return f'<figure class="diagram"><pre class="mermaid">{esc(b["text"])}</pre>{cap_html}</figure>'
        return f'<pre class="cardpre">{esc(b["text"])}</pre>'
    if b["type"] == "table":
        header, rows = parse_table(b["lines"])
        return render_table_html(header, rows, layer_ids=layer_ids)
    if b["type"] == "ol":
        return '<ol class="doclist">' + "".join(f"<li>{render_inline(it)}</li>" for it in b["items"]) + "</ol>"
    if b["type"] == "ul":
        return '<ul class="doclist">' + "".join(f"<li>{render_inline(it)}</li>" for it in b["items"]) + "</ul>"
    return ""


def extract_calls(blocks):
    global_ruled = False
    for i, b in enumerate(blocks):
        if b["type"] == "p" and i == 0 and re.match(r"^\*\*RULED", b["text"].strip(), re.I):
            global_ruled = True
    items_raw = []
    for b in blocks:
        if b["type"] in ("ol", "ul"):
            items_raw.extend(b["items"])
    calls = []
    for n, raw in enumerate(items_raw, start=1):
        m = re.match(r"^\*\*(.+?)\*\*\s*(.*)$", raw, re.S)
        if m:
            title_raw, remainder = m.group(1), m.group(2)
        else:
            title_raw, remainder = raw[:80], ""
        rec_m = re.search(r"\*Recommendation:\*\s*(.*)$", remainder, re.I | re.S)
        if rec_m:
            recommendation_raw = rec_m.group(1).strip()
            body_raw = remainder[:rec_m.start()].strip()
        else:
            recommendation_raw = ""
            body_raw = remainder.strip()
        calls.append({
            "n": n,
            "q": strip_md(title_raw),
            "body": render_inline(body_raw, count=True) if body_raw else "",
            "ruling": render_inline(recommendation_raw, count=True) if recommendation_raw else "",
            "ruled": global_ruled,
        })
    return calls


def render_calls_table(calls):
    if not calls:
        return '<p class="plain">No numbered calls parsed in OPEN.</p>'
    rows = []
    for c in calls:
        cls = "ruled" if c["ruled"] else ""
        rul = f'<span class="rul">{c["ruling"]}</span>' if c["ruling"] else ""
        chip_cls = "st-ruled" if c["ruled"] else "st-open"
        chip_lbl = "ruled" if c["ruled"] else "open"
        rows.append(f'<tr class="{cls}"><td class="n">{c["n"]}</td><td class="q">{esc(c["q"])}</td><td class="o">{c["body"]}{rul}</td><td class="s"><span class="chip {chip_cls}">{chip_lbl}</span></td></tr>')
    return '<div class="tblwrap"><table class="calls"><thead><tr><th></th><th>The call</th><th>Reading</th><th>State</th></tr></thead><tbody>' + "".join(rows) + "</tbody></table></div>"


def derive_state(status_text):
    s = (status_text or "").upper()
    if "RULED" in s:
        return "ruled", "RULED"
    if "CANON" in s:
        return "good", "CANONICAL"
    if "PROVISION" in s:
        return "open", "PROVISIONAL"
    return "open", "DRAFT"


def spine_shelf_count(shelf):
    try:
        txt = load_text(os.path.join(ROOT, "_0.1_BVX_LEARN", "_meta", "SPINE-KEYS.md"))
    except Exception:
        return None
    m = re.search(r"###\s+" + re.escape(shelf) + r"\s*\((\d+)\)", txt)
    return int(m.group(1)) if m else None


def main():
    if len(sys.argv) < 2:
        print("usage: build.py <NN>"); sys.exit(2)
    nn = sys.argv[1]

    systems = load_json(os.path.join(HERE, "systems.json"))
    if nn not in systems:
        print("unknown system", nn, "- known:", ", ".join(systems)); sys.exit(2)
    sysinfo = systems[nn]

    global TERMS
    TERMS = load_json(os.path.join(HERE, "terms.json"))

    doc_path = os.path.join(ROOT, sysinfo["path"])
    raw = load_text(doc_path)
    fm, body = parse_frontmatter(raw)

    missing = check_missing_keys(body)
    if missing:
        print("BLOCKING: [[key]] not found in terms.json:", ", ".join(missing))
        sys.exit(1)

    title, subtitle, rest = parse_title(body)

    heading_re = re.compile(r"^##\s+(.+)$", re.M)
    matches = list(heading_re.finditer(rest))
    raw_sections = []
    preface_text = rest[:matches[0].start()] if matches else rest
    if preface_text.strip():
        raw_sections.append({"name": "OVERVIEW", "body_text": preface_text, "is_pre": True})
    for i, m in enumerate(matches):
        start = m.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(rest)
        raw_sections.append({"name": m.group(1).strip(), "body_text": rest[start:end], "is_pre": False})

    sections_out = []
    calls_final = []
    diagrams_total = 0
    missing_caption_secs = []
    zero_term_secs = []

    for idx_s, sec in enumerate(raw_sections):
        text_linked = auto_link_section(sec["body_text"])
        blocks = split_blocks(text_linked)
        consumed, captions = compute_captions(blocks)

        name_up = sec["name"].upper()
        is_open = name_up.strip() == "OPEN" or name_up.strip().startswith("OPEN")
        is_parta = "PART A" in name_up
        is_instance = ("INSTANCE" in name_up) and not is_parta

        if is_parta:
            tbl = next((b for b in blocks if b["type"] == "table"), None)
            if tbl:
                header, rows = parse_table(tbl["lines"])
                extract_slice(header, rows)
        if is_instance:
            tbl = next((b for b in blocks if b["type"] == "table"), None)
            if tbl:
                header, rows = parse_table(tbl["lines"])
                extract_instance(header, rows)

        calls = extract_calls(blocks) if is_open else []
        calls_final.extend(calls)

        parts = []
        sec_diagrams = 0
        for idx_b, b in enumerate(blocks):
            if idx_b in consumed:
                continue
            if is_open and b["type"] in ("ol", "ul"):
                continue
            parts.append(render_block(b, idx_b, captions, layer_ids=(is_parta or is_instance)))
            if b["type"] == "code" and b.get("lang") == "mermaid":
                diagrams_total += 1
                sec_diagrams += 1
                if captions.get(idx_b) is None:
                    missing_caption_secs.append(sec["name"])
        if is_open:
            parts.append(render_calls_table(calls))

        html_out = "".join(parts)
        # a section that is mostly a bare card/table dump (a one-line lead-in into a
        # fenced card, say) has nowhere real to hang a hover term; only flag sections
        # that carry enough prose to reasonably expect one and still came up empty.
        prose_words = 0
        for bl in blocks:
            if bl["type"] in ("p", "h"):
                prose_words += len(bl["text"].split())
            elif bl["type"] in ("ol", "ul"):
                prose_words += sum(len(it.split()) for it in bl["items"])
        is_contents = "contents" in strip_md(sec["name"]).lower()  # a table of contents is links, nowhere to hang a term
        if prose_words >= 12 and 'class="t"' not in html_out and not is_contents:
            zero_term_secs.append(sec["name"])

        sections_out.append({
            "id": f"sec-{idx_s}",
            "no": "" if sec["is_pre"] else str(idx_s),
            "name": strip_md(sec["name"]),
            "pre": sec["is_pre"],
            "src": f"{sec_diagrams} diagram{'s' if sec_diagrams != 1 else ''}" if sec_diagrams else "",
            "html": html_out,
        })

    findings = []
    if missing_caption_secs:
        findings.append("mermaid block(s) lost their caption in: " + ", ".join(sorted(set(missing_caption_secs))))
    if zero_term_secs:
        findings.append("section(s) with zero hover terms: " + ", ".join(zero_term_secs))
    if nn == "04" and diagrams_total < 3:
        findings.append(f"only {diagrams_total} mermaid diagram(s) rendered for 04, need >= 3")
    if findings:
        print("BLOCKING findings:")
        for f in findings:
            print(" -", f)
        sys.exit(1)

    for row in SLICE_ROWS:
        row["instance"] = INSTANCE_BY_ID.get(row["id"])

    sources = fm.get("sources", [])
    shelf = sysinfo["shelf"]
    shelf_count = spine_shelf_count(shelf)
    feed = {
        "sources": sources,
        "paths": {sid: f"_0.1_BVX_LEARN/KNOWLEDGE_AREAS/{sid}.md" for sid in sources},
        "shelf": shelf,
        "shelf_count": shelf_count,
        "distilled": len(sources),
    }

    state, state_label = derive_state(fm.get("status", ""))
    tm = {
        "n": nn,
        "title": title,
        "subtitle": subtitle,
        "short": sysinfo["short"],
        "version": fm.get("version", ""),
        "status": fm.get("status", ""),
        "status_html": esc(fm.get("status", "")),
        "trunk": fm.get("trunk", ""),
        "last_updated": fm.get("last_updated", ""),
        "path": sysinfo["path"],
        "state": state,
        "state_label": state_label,
    }

    nested_count = 0
    for k in USED_TERMS_GLOBAL:
        d = TERMS.get(k, {}).get("d", "")
        nested_count += len(re.findall(r"\[\[", d))

    data = {
        "tm": tm,
        "sections": sections_out,
        "slice": SLICE_ROWS,
        "calls": calls_final,
        "feed": feed,
        "terms": TERMS,
    }

    text_json = json.dumps(data, ensure_ascii=False).replace("</script", "<\\/script")
    tpl = load_text(os.path.join(HERE, "template.html"))
    assert tpl.count("/*__DATA__*/null") == 1, "template.html must contain exactly one /*__DATA__*/null slot"
    frag = tpl.replace("/*__DATA__*/null", text_json).replace("<title>TM</title>", f"<title>TM {esc(nn)} · {esc(title)}</title>")

    # the document is written into the fragment STATICALLY: the artifact host renders <pre class="mermaid"> only in the
    # DOM it receives, never in markup a script injects later (found 9/16: the diagrams showed as text).
    tr_html = (f'<span class="tr"><span class="{"b" if tm.get("trunk") == "BLACK" else "o"}">{esc(tm["trunk"])}</span></span>' if tm.get("trunk") else "")
    page = [f'<h1 class="dt"><small>TM {esc(tm["n"])} · technical manual · {esc(tm.get("version") or "")}</small>{esc(tm["title"])}<em>{esc(tm.get("subtitle") or "")}</em></h1>',
            '<dl class="fm">',
            f'<dt>System</dt><dd>TM {esc(tm["n"])} {tr_html}</dd>',
            f'<dt>Version · updated</dt><dd>{esc(tm.get("version") or "")} · {esc(tm.get("last_updated") or "")}</dd>',
            f'<dt>Status</dt><dd>{tm.get("status_html") or esc(tm.get("status") or "")}</dd>',
            f'<dt>Path</dt><dd class="path">{esc(tm["path"])}</dd>',
            '</dl>']
    for s in sections_out:
        no = f'<span class="no">{esc(s["no"])}</span>' if s["no"] else ""
        src = f'<span class="src">{esc(s["src"])}</span>' if s["src"] else ""
        page.append(f'<section class="sec {"pre" if s["pre"] else ""}" id="{s["id"]}"><div class="sh">{no}<h2>{esc(s["name"])}</h2>{src}</div>{s["html"]}</section>')
    assert frag.count('<div class="page" id="page"></div>') == 1, "template.html must contain the empty #page div"
    frag = frag.replace('<div class="page" id="page"></div>', '<div class="page" id="page">' + "\n".join(page) + '</div>')

    out_dir = os.path.join(HERE, "out")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"TM-{nn}.html")
    full = ('<!doctype html>\n<html lang="en">\n<head>\n<meta charset="utf-8">\n'
            '<meta name="viewport" content="width=device-width,initial-scale=1">\n</head>\n<body>\n'
            + frag + "\n</body>\n</html>\n")
    with io.open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(full)

    scratch = os.environ.get("SITREP_SCRATCH") or tempfile.gettempdir()
    frag_path = os.path.join(scratch, f"TM-{nn}.fragment.html")
    with io.open(frag_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(frag)

    print(f"TM {nn}: sections {len(sections_out)} · terms wired {TERMS_WIRED[0]} · tooltips nested {nested_count} "
          f"· diagrams {diagrams_total} · slice rows {len(SLICE_ROWS)} · instance rows {len(INSTANCE_BY_ID)} "
          f"· calls {len(calls_final)}")
    print("wrote", out_path, f"({os.path.getsize(out_path)//1024} KB)")
    print("fragment", frag_path)


if __name__ == "__main__":
    main()
