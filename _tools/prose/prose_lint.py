#!/usr/bin/env python3
"""prose_lint.py - report-only prose checker for the Command's writing rules.

Usage:
    python _tools/prose/prose_lint.py <file.md|.html|.txt> [...] [--max N] [--families]
    cat draft.md | python _tools/prose/prose_lint.py [--max N] [--families]

Prints one line per finding: file:line · rule · detail. Never rewrites.
Checks: sentences over 20 words, em-dashes, exclamation marks, simple passive
voice, stock AI phrases (table below, with suggested replacement), headers in
files under 500 words. HTML input has tags, <script> and <style> stripped
first (line numbers are kept).
--families adds one summary line: findings per pattern family (slop words,
contrast frames, one-line closers, filler openers, passive, fake precision,
hedges, other). Curly quotes are read as straight ones before matching.
Table sources: avoid-ai-writing patterns.md (MIT), blader/humanizer (MIT).
Every replacement is the same length or shorter than the phrase it flags.
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

# merged 10/13 (BOLO 140): humanizer pairs + avoid-ai-writing entries the first pass trimmed.
# Replacements stay plain: "cut" or a shorter word. Setdefault keeps the older entry on a clash.
_MORE = {
    "that is the real win": "cut", "let that sink in": "cut", "read that again": "cut",
    "that distinction matters": "cut", "this shows the importance of": "cut, state the fact",
    "the message was clear": "cut", "the real question is": "the question is",
    "what really matters": "cut", "the heart of the matter": "cut", "the deeper issue": "say the issue",
    "here's the thing": "cut", "the thing is": "cut", "let's be honest": "cut", "real talk": "cut",
    "without further ado": "cut", "here's what you need to know": "cut", "let's break this down": "cut",
    "let's explore": "cut", "don't get me wrong": "cut", "i'm not saying": "cut, state the claim",
    "this is not to say": "cut", "to be clear": "cut", "a tempting approach": "cut",
    "one might be tempted": "cut", "great question": "cut (chatbot opener)",
    "you're absolutely right": "cut", "let me know if": "cut (chatbot sign-off)",
    "up to my last training": "cut", "not publicly available": "say what the source lacks",
    "maintains a low profile": "cut", "not widely documented": "say what the source lacks",
    "stands as": "is", "functions as": "is", "setting the stage for": "cut", "indelible mark": "cut",
    "exciting times": "cut", "a step in the right direction": "cut", "plays a key role": "say what it does",
    "breathtaking": "cut or be specific", "stunning": "cut or be specific",
    "renowned": "cut or name who says so", "groundbreaking": "say what it changed", "must-visit": "cut",
    "in the heart of": "in", "diverse array": "name the items", "natural beauty": "cut or be specific",
    "rich cultural heritage": "cut", "exemplifies": "shows", "experts argue": "name the expert or cut",
    "industry reports": "name the report or cut", "observers have cited": "name them or cut",
    "additionally": "also, or cut", "garner": "get, earn", "showcase": "show", "quietly": "cut",
    "profound": "cut or be specific",
    # avoid-ai-writing entries the first pass trimmed
    "hit differently": "cut or say what changed", "hits different": "cut or say what changed",
    "embrace": "adopt, use", "load-bearing": "essential, or say what breaks without it",
    "keen": "cut", "genuinely": "cut", "genuine": "cut", "truly": "cut", "quite frankly": "cut",
    "to be honest": "cut", "poised to": "ready to, about to", "underpinning": "basis",
    "underpinnings": "basis", "paradigm-shifting": "say what shifted", "complexities": "details",
    "enduring": "lasting", "worth reading": "say why", "worth exploring": "say why",
    "worth a look": "say why", "worth checking out": "say why", "worth your time": "say why",
    "when it comes to": "cut, talk about the thing", "at the end of the day": "cut",
    "that being said": "but", "in terms of": "rewrite", "the reality is that": "cut",
    "it's important to note that": "cut", "it is important to note that": "cut",
    "notably": "cut", "interestingly": "cut", "importantly": "cut", "undoubtedly": "cut",
    "make no mistake": "cut", "the truth is": "cut", "fundamentally": "cut",
    "imagine a world where": "state the claim", "picture a future in which": "state the claim",
    "envision a world where": "state the claim", "whether you're": "name the real audience",
    "the catch?": "cut, state it", "the kicker": "cut, state it", "plot twist": "cut",
    "the best part?": "cut, state it", "hot take": "cut", "pro tip": "cut", "fun fact": "cut",
    "chef's kiss": "cut", "mic drop": "cut", "sit with that": "cut", "that's not nothing": "cut",
    "batteries included": "list what ships", "it just works": "say what it does",
    "zero config": "say what is set", "sane defaults": "name the defaults",
    "as of my last update": "cut", "feel free to reach out": "cut", "in this article, we will": "cut",
    "what surprised me most": "state the fact", "i can't stop thinking about": "cut",
    "the line i keep coming back to": "cut", "i want to be upfront": "cut",
    "to be fully transparent": "cut", "to answer your question": "cut", "you're asking about": "cut",
    "one thing is certain": "cut", "as we move forward": "cut", "this matters because": "state the consequence",
    "here's what's interesting": "cut", "here's what stood out": "cut",
    "experts believe": "name the expert or cut", "studies show": "name the study or cut",
    "research suggests": "name the study or cut", "industry leaders agree": "name them or cut",
    "could potentially": "could", "may eventually": "may", "might ultimately": "might",
    "arguably": "cut", "emerging space": "name the sector", "the intersection of": "name the overlap",
    "community-driven": "say what the community does", "user engagement": "name the action",
    "i recently had the pleasure of": "say what happened",
}
for _k, _v in _MORE.items():
    STOCK.setdefault(_k, _v)

# family of each flagged phrase; anything not listed here is a slop word
_FILLER = """it's worth noting|it is worth noting|in today's|in the world of|in conclusion|furthermore|moreover|additionally
great question|you're absolutely right|let's dive|let's explore|let's break this down|here's what you need to know|to be clear
without further ado|here's the thing|the thing is|let's be honest|real talk|when it comes to|in terms of|the reality is that
notably|interestingly|importantly|undoubtedly|make no mistake|the truth is|fundamentally|imagine a world where
picture a future in which|envision a world where|whether you're|the catch?|the kicker|plot twist|the best part?|hot take|pro tip|fun fact
i want to be upfront|to be fully transparent|to answer your question|you're asking about|don't get me wrong|i'm not saying
this is not to say|a tempting approach|one might be tempted|feel free to reach out|let me know if|i hope this helps
in this article, we will|at the end of the day|that being said|what surprised me most|i can't stop thinking about
the line i keep coming back to|the real question is|what really matters|the heart of the matter|the deeper issue
quite frankly|truly|genuinely|genuine|to be honest|it's important to note that|it is important to note that
here's what's interesting|here's what stood out|i recently had the pleasure of""".replace("\n", "|").split("|")
_CLOSER = """that is the real win|let that sink in|read that again|that distinction matters|this shows the importance of
the message was clear|the future looks bright|only time will tell|exciting times|a step in the right direction
one thing is certain|as we move forward|sit with that|that's not nothing|mic drop|chef's kiss|this matters because""".replace("\n", "|").split("|")
_HEDGE = """could potentially|may eventually|might ultimately|up to my last training|not publicly available|maintains a low profile
not widely documented|as of my last update|experts believe|studies show|research suggests|industry leaders agree|experts argue
industry reports|observers have cited|arguably""".replace("\n", "|").split("|")
FAMILY = {}
for _names, _fam in ((_FILLER, "filler openers"), (_CLOSER, "one-line closers"), (_HEDGE, "hedges")):
    for _n in _names:
        FAMILY[_n.strip()] = _fam
FAMILIES = ["slop words", "contrast frames", "one-line closers", "filler openers", "passive",
            "fake precision", "hedges", "other"]
STOCK_RE = [(re.compile(r"(?<![\w-])" + re.escape(k).replace(r"\ ", r"\s+") + r"(?![\w-])", re.I), k, v)
            for k, v in sorted(STOCK.items(), key=lambda kv: -len(kv[0]))]
LEVERAGE_VERB = re.compile(r"\b(?:to|will|can|could|should|we|they|you|i|that|which)\s+leverag(?:e|es|ed|ing)\b"
                           r"|\bleverag(?:ed|ing)\b|\bleverages\s+(?:the|a|an|our|your|its|their)\b", re.I)
TESTAMENT = re.compile(r"\btestament\b", re.I)
CONTRAST = [
    (re.compile(r"\bnot (?:just|only|merely|simply)\b[^.]{0,80}\bbut\b", re.I), "not just X but Y"),
    (re.compile(r"\bnot (?:a|an|the)\b[^.;!?]{1,50}\bbut\b", re.I), "not X but Y"),
    (re.compile(r"\bit(?:'s| is) not\b[^.;]{1,60}[;,.]\s*it(?:'s| is)\b", re.I), "it's not X, it's Y"),
    (re.compile(r"\b(?:isn't|is not|aren't|are not)\s+(?:about|just)\b[^.;]{1,60}[;,]\s*(?:it's|it is|but)\b", re.I),
     "isn't about X, it's Y"),
    (re.compile(r"\bthis (?:does not|doesn't) mean\b", re.I), "this doesn't mean X (then 'It means Y')"),
]
FAKE_PRECISION = [
    re.compile(r"\b\d{1,3}(?:\.\d+)?%\s+of\s+(?:users|people|teams|developers|companies|customers|engineers|readers)\b", re.I),
    re.compile(r"\b\d+(?:\.\d+)?x\s+(?:faster|slower|more|better|cheaper|bigger|smaller|cleaner)\b", re.I),
]
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
            out.append((n, "em-dash", "use a comma, colon, or period", "other"))
        for m in re.finditer(r"!", line):
            if not re.search(r"!\[|<!|!=|^\s*!", line[max(0, m.start() - 1):m.start() + 2]):
                out.append((n, "exclamation", "cut the exclamation mark", "other"))
                break
        low = line.replace("\u2019", "'").replace("\u2018", "'")
        for rx, k, v in STOCK_RE:
            if rx.search(low):
                out.append((n, "stock-phrase", f'"{k}" -> {v}', FAMILY.get(k, "slop words")))
        if LEVERAGE_VERB.search(low):
            out.append((n, "stock-phrase", '"leverage" (verb) -> use', "slop words"))
        if TESTAMENT.search(low) and not re.search(r"\btestament to\b", low, re.I):
            out.append((n, "stock-phrase", '"testament" -> shows, proves', "slop words"))
        for rx, label in CONTRAST:
            if rx.search(low):
                out.append((n, "contrast-frame", f'"{label}" -> state the point directly', "contrast frames"))
                break
        for rx in FAKE_PRECISION:
            m = rx.search(low)
            if m:
                out.append((n, "fake-precision", f'"{m.group(0)}" -> name what measured it, or say about/most',
                            "fake precision"))
        if words < 500 and HEADER.search(line):
            out.append((n, "header-short-file", f"header in a {words}-word file; drop it", "other"))

    for n, s in sentences(clean):
        wc = len(s.split())
        if wc > 20:
            out.append((n, "long-sentence", f"{wc} words: {s[:60]}...", "other"))
        for m in PASSIVE.finditer(s):
            if m.group(1).lower() not in PASSIVE_SKIP:
                out.append((n, "passive", f'"{m.group(0)}" (name the actor)', "passive"))
                break
    out.sort(key=lambda t: t[0])
    return out


def main(argv):
    mx, files, i, fams = None, [], 0, False
    while i < len(argv):
        if argv[i] == "--families":
            fams = True
            i += 1
            continue
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
    counts = dict.fromkeys(FAMILIES, 0)
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
        for n, rule, detail, fam in lint(name, raw):
            print(f"{name}:{n} · {rule} · {detail}")
            total += 1
            counts[fam] += 1
    print(f"prose_lint: {total} finding(s) in {len(srcs)} file(s)" + (f" (max {mx})" if mx is not None else ""))
    if fams:
        print("families: " + " · ".join(f"{k} {counts[k]}" for k in FAMILIES))
    return 1 if mx is not None and total > mx else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

# adapted from Leonxlnx/taste-skill (MIT) + conorbronsdon/avoid-ai-writing (MIT) · BOLO 140 · 2026-10-12
