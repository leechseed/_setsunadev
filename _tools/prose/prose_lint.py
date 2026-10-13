#!/usr/bin/env python3
"""prose_lint.py - report-only prose checker for the Command's writing rules.

Usage:
    python _tools/prose/prose_lint.py <file.md|.html|.txt> [...] [--max N]
    cat draft.md | python _tools/prose/prose_lint.py [--max N]

Prints one line per finding: file:line · rule · detail. Never rewrites.
Checks: sentences over 20 words, em-dashes, exclamation marks, simple passive
voice, stock AI phrases (table below, with suggested replacement), headers in
files under 500 words. HTML input has tags, <script> and <style> stripped
first (line numbers are kept).
Exit 0 unless the finding count exceeds --max (default: unlimited -> always 0).
"""
import io
import re
import sys

if hasattr(sys.stdout, "buffer"):
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8", errors="replace")

# word/phrase -> suggested replacement (table from avoid-ai-writing, trimmed to regex-safe forms)
STOCK = {
    "delve": "explore, dig into, look at", "delve into": "explore, dig into, look at",
    "tapestry": "describe the actual complexity", "landscape": "field, space, industry (metaphor)",
    "realm": "area, field, domain", "paradigm": "model, approach, framework",
    "embark": "start, begin", "beacon": "example, guide", "testament to": "shows, proves",
    "robust": "strong, reliable", "comprehensive": "thorough, complete, full",
    "cutting-edge": "latest, newest", "pivotal": "important, key", "underscores": "highlights, shows",
    "meticulous": "careful, detailed", "meticulously": "carefully", "seamless": "smooth, easy",
    "seamlessly": "smoothly", "game-changer": "say what changed", "game-changing": "say what changed",
    "watershed moment": "turning point", "the future looks bright": "cut",
    "only time will tell": "cut", "nestled": "is in, sits", "vibrant": "lively (or be specific)",
    "thriving": "growing (or cite a number)", "showcasing": "showing", "deep dive": "look at, examine",
    "dive into": "look at, examine", "unpack": "explain, break down", "unpacking": "explaining",
    "bustling": "busy", "intricate": "complex", "intricacies": "details", "ever-evolving": "changing",
    "daunting": "hard, difficult", "holistic": "complete, whole", "holistically": "as a whole",
    "actionable": "practical, concrete", "impactful": "effective", "learnings": "lessons, findings",
    "thought leader": "expert", "best practices": "what works, standard approach",
    "at its core": "cut", "synergy": "combined effect", "synergies": "combined effects",
    "interplay": "relationship, interaction", "symphony": "coordination, balance",
    "utilize": "use", "in order to": "to", "due to the fact that": "because", "serves as": "is",
    "boasts": "has", "commence": "start, begin", "ascertain": "find out", "endeavor": "effort, try",
    "harness": "use", "navigate": "work through, handle", "navigating": "working through",
    "foster": "encourage, support", "elevate": "improve, raise", "unleash": "release, enable",
    "streamline": "simplify, speed up", "empower": "enable, let", "bolster": "support, strengthen",
    "spearhead": "lead, drive", "resonate": "connect with, matter to", "resonates with": "connects with",
    "revolutionize": "change, reshape", "facilitate": "enable, help, run", "facilitates": "enables, helps",
    "underpin": "support, form the basis of", "nuanced": "specific, subtle", "crucial": "important, key",
    "multifaceted": "having several parts", "ecosystem": "system, community, network (metaphor)",
    "myriad": "many (or give a number)", "plethora": "many (or give a number)",
    "encompass": "include, cover", "catalyze": "start, trigger", "reimagine": "rethink, redesign",
    "galvanize": "motivate, rally", "augment": "add to, expand", "cultivate": "build, develop",
    "illuminate": "clarify, explain", "elucidate": "explain, spell out", "juxtapose": "compare, contrast",
    "transformative": "changes how X works", "cornerstone": "foundation, key part",
    "paramount": "most important", "burgeoning": "growing, emerging", "nascent": "new, early-stage",
    "quintessential": "typical, classic", "overarching": "main, central",
    "it's worth noting": "cut, just say it", "it is worth noting": "cut, just say it",
    "in today's": "cut or name the date/context", "in the world of": "cut, name the thing",
    "world-class": "cite a benchmark", "state-of-the-art": "cite a benchmark", "best-in-class": "cite a benchmark",
    "unprecedented": "name the precedent it breaks", "plays a crucial role": "say what it does",
    "i hope this helps": "cut (chatbot sign-off)", "let's dive": "cut (stock opener)",
    "in conclusion": "cut, end on the point", "furthermore": "also, or cut", "moreover": "also, or cut",
}
STOCK_RE = [(re.compile(r"(?<![\w-])" + re.escape(k).replace(r"\ ", r"\s+") + r"(?![\w-])", re.I), k, v)
            for k, v in sorted(STOCK.items(), key=lambda kv: -len(kv[0]))]
LEVERAGE_VERB = re.compile(r"\b(?:to|will|can|could|should|we|they|you|i|that|which)\s+leverag(?:e|es|ed|ing)\b"
                           r"|\bleverag(?:ed|ing)\b|\bleverages\s+(?:the|a|an|our|your|its|their)\b", re.I)
TESTAMENT = re.compile(r"\btestament\b", re.I)
EMDASH = re.compile("—")
PASSIVE = re.compile(r"\b(?:was|were|is|are|been|being)\s+(?:\w+ly\s+)?(\w+(?:ed|en)|built|made|done|seen|shown|run|set|put|held|kept|sent|given|taken|known|written)\b", re.I)
PASSIVE_SKIP = {"need", "ed", "open", "even", "often", "token", "green", "seven", "children", "listen",
                "kitchen", "hidden", "golden", "garden", "taken_"}
HEADER = re.compile(r"^\s{0,3}#{1,6}\s+\S|<h[1-6][\s>]", re.I)


def strip_html(text):
    def blank(m):
        return re.sub(r"[^\n]", " ", m.group(0))
    text = re.sub(r"<(script|style)\b.*?</\1>", blank, text, flags=re.S | re.I)
    text = re.sub(r"<!--.*?-->", blank, text, flags=re.S)
    return text


def sentences(lines):
    """Yield (line_no, sentence) for prose lines; sentence assigned to the line it starts on."""
    buf, start = [], None
    for n, line in enumerate(lines, 1):
        s = line.strip()
        if not s or s.startswith(("```", "|", "#", "---")) or re.match(r"^\s*(<\w|[-*]\s+`)", line) and "<" in s[:2]:
            if buf:
                yield start, " ".join(buf)
                buf, start = [], None
            continue
        s = re.sub(r"^\s*(?:[-*+]|\d+[.)])\s+", "", s)
        for part in re.split(r"(?<=[.!?])\s+", s):
            if start is None:
                start = n
            buf.append(part)
            if re.search(r"[.!?][\"')\]]*$", part):
                yield start, " ".join(buf)
                buf, start = [], None
    if buf:
        yield start, " ".join(buf)


def lint(name, raw):
    out = []
    is_html = name.lower().endswith((".html", ".htm"))
    text = strip_html(raw) if is_html else raw
    if is_html:
        text = re.sub(r"<[^>]+>", " ", text)
    lines = text.splitlines()
    in_code = False
    clean = []
    for line in lines:
        if line.strip().startswith("```"):
            in_code = not in_code
            clean.append("")
            continue
        clean.append("" if in_code else line)
    words = len(re.findall(r"\b\w+\b", " ".join(clean)))

    for n, line in enumerate(clean, 1):
        for _ in EMDASH.finditer(line):
            out.append((n, "em-dash", "use a comma, colon, or period"))
        for m in re.finditer(r"!", line):
            if not re.search(r"!\[|<!|!=|^\s*!", line[max(0, m.start() - 1):m.start() + 2]):
                out.append((n, "exclamation", "cut the exclamation mark"))
                break
        low = line
        for rx, k, v in STOCK_RE:
            if rx.search(low):
                out.append((n, "stock-phrase", f'"{k}" -> {v}'))
        if LEVERAGE_VERB.search(low):
            out.append((n, "stock-phrase", '"leverage" (verb) -> use'))
        if TESTAMENT.search(low) and not re.search(r"\btestament to\b", low, re.I):
            out.append((n, "stock-phrase", '"testament" -> shows, proves'))
        if words < 500 and HEADER.search(line):
            out.append((n, "header-short-file", f"header in a {words}-word file; drop it"))

    for n, s in sentences(clean):
        wc = len(s.split())
        if wc > 20:
            out.append((n, "long-sentence", f"{wc} words: {s[:60]}..."))
        for m in PASSIVE.finditer(s):
            if m.group(1).lower() not in PASSIVE_SKIP:
                out.append((n, "passive", f'"{m.group(0)}" (name the actor)'))
                break
    out.sort(key=lambda t: t[0])
    return out


def main(argv):
    mx, files, i = None, [], 0
    while i < len(argv):
        if argv[i] == "--max":
            mx = int(argv[i + 1])
            i += 2
            continue
        if argv[i].startswith("--max="):
            mx = int(argv[i].split("=", 1)[1])
        else:
            files.append(argv[i])
        i += 1
    total = 0
    srcs = []
    if files:
        for f in files:
            try:
                with open(f, encoding="utf-8", errors="replace") as fh:
                    srcs.append((f, fh.read()))
            except OSError as e:
                print(f"{f} · error · {e}")
    else:
        srcs.append(("<stdin>", sys.stdin.read()))
    for name, raw in srcs:
        for n, rule, detail in lint(name, raw):
            print(f"{name}:{n} · {rule} · {detail}")
            total += 1
    print(f"prose_lint: {total} finding(s) in {len(srcs)} file(s)" + (f" (max {mx})" if mx is not None else ""))
    return 1 if mx is not None and total > mx else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

# adapted from Leonxlnx/taste-skill (MIT) + conorbronsdon/avoid-ai-writing (MIT) · BOLO 140 · 2026-10-12
