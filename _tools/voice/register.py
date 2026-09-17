import re, json, sys, os

S = sys.argv[1]
g = json.load(open('_tools/sitrep/glossary.json', encoding='utf8'))
labels = sorted({v['t'].lower() for v in g.values() if len(v['t']) > 2}, key=len, reverse=True)


def syl(w):
    w = re.sub(r'[^a-z]', '', w.lower())
    if not w:
        return 0
    c = len(re.findall(r'[aeiouy]+', w))
    if w.endswith('e') and not w.endswith('le') and c > 1:
        c -= 1
    return max(1, c)


def stats(name, txt):
    t = txt.replace('\n', ' ')
    sents = [s for s in re.split(r'(?<=[.!?])\s+', t) if len(s.split()) > 1]
    words = re.findall(r"[A-Za-z0-9'/\-]+", t)
    W = len(words); Sn = len(sents); syls = sum(syl(w) for w in words)
    asl = W / Sn; asw = syls / W
    fk = 0.39 * asl + 11.8 * asw - 15.59
    fre = 206.835 - 1.015 * asl - 84.6 * asw
    long = sum(1 for s in sents if len(s.split()) > 25)
    codes = len(re.findall(r'\b(BOLO|Block|BORESIGHT|DOPE SHEET|FRAGO|v)\s?[0-9IVX]+\b|#\d+|\b[0-9]{1,2}/[0-9]{1,2}\b', t))
    low = t.lower()
    lex = sorted({l for l in labels if re.search(r'\b' + re.escape(l) + r'\b', low)})
    you = sum(1 for s in sents if re.match(r"^(you|your|when you|if you)\b", s.strip(), re.I))
    agent = sum(1 for s in sents if re.match(r"^(claude|it|i|he|chief|judy|i'm|i've)\b", s.strip(), re.I))
    dots = t.count(' · ')
    print(f"\n== {name}")
    print(f" words {W} · sentences {Sn} · avg sentence {asl:.1f} words · over-25-word sentences {long}/{Sn}")
    print(f" Flesch reading ease {fre:.0f} · FK grade {fk:.1f}")
    print(f" sentences opening on you {you} ({100*you/Sn:.0f}%) · on a named actor {agent} ({100*agent/Sn:.0f}%)")
    print(f" code-tokens (BOLO N · Block V · #N · dates · vN) {codes} -> one per {W/max(1,codes):.0f} words")
    print(f" Command-lexicon terms present {len(lex)} -> {', '.join(lex[:20])}{' ...' if len(lex) > 20 else ''}")
    print(f" dot separators {dots}")


for f in ['sample_docs', 'sample_reply_sitrep', 'sample_reply_pitch', 'sample_board_plain', 'sample_leverage']:
    p = f'{S}/voice/{f}.txt'
    if os.path.exists(p):
        stats(f, open(p, encoding='utf8').read())
