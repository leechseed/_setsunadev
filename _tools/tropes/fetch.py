"""BOLO 77 wave 2 · the trope fetch (zero tokens).

Pulls the TV Tropes plot index and its category indexes, then every trope they
list, and keeps only what the trope graph needs: slug, name, the index's one-line
definition, which indexes list it, and the Main/ links inside each trope's article
(the raw edges). No page bodies are stored (the repo is public).

Direct fetch with a browser user agent (proven 9/23; WebFetch gets 403).
Polite: one request a second, resumable (a slug already in the cache is skipped).

usage: python _tools/tropes/fetch.py [--limit N]
out:   _tools/tropes/data/index.json · _tools/tropes/data/tropes.jsonl
"""
import html, json, re, sys, time, urllib.request
from pathlib import Path

UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"
BASE = "https://tvtropes.org/pmwiki/pmwiki.php/Main/"
OUT = Path(__file__).parent / "data"
# the plot index and its own categories only (ruled 9/23: "only the plot/narrative indexes").
# Tried 9/24 and dropped: the thematic indexes (Death 1,034 · TruthAndLies 328 · Family 218 ·
# Betrayal 146 · Revenge 97 · FateAndProphecy 89) doubled the pull without adding plot shape;
# MasterPlots · ProppsFunctionsOfFolktales · Conflict list no entries in this format.
SEEDS = ["Plots", "BeginningTropes", "CallToAdventure", "ClimacticTropes", "EndingTropes",
         "FlashbacksAndChronology", "GoalsAndObjectivesIndex", "TheHerosJourney", "PlotTwist",
         "RomanceArc"]
LINK = re.compile(r"""<a class='twikilink' href='/pmwiki/pmwiki\.php/Main/([A-Za-z0-9]+)'[^>]*>(.*?)</a>""", re.S)
ENTRY = re.compile(r"""<li>\s*<a class='twikilink' href='/pmwiki/pmwiki\.php/Main/([A-Za-z0-9]+)'[^>]*>(.*?)</a>\s*:?\s*(.*?)</li>""", re.S)


def get(slug):
    req = urllib.request.Request(BASE + slug, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.geturl(), r.read().decode("utf-8", "replace")


def article(page):
    i = page.find('id="main-article"')
    if i < 0:
        return ""
    m = page[i:]
    k = m.find('id="proper-footer"')
    return m[:k] if k > 0 else m


def text(s):
    s = re.sub(r"<[^>]+>", " ", s)
    return re.sub(r"\s+", " ", html.unescape(s)).strip()


def main():
    limit = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else 2000
    OUT.mkdir(parents=True, exist_ok=True)
    idx_path, tr_path = OUT / "index.json", OUT / "tropes.jsonl"
    index = json.loads(idx_path.read_text(encoding="utf-8")) if idx_path.exists() else {}
    done = set()
    if tr_path.exists():
        done = {json.loads(l)["slug"] for l in tr_path.read_text(encoding="utf-8").splitlines() if l.strip()}

    # 1 · the indexes: slug -> {name, def, indexes[]}
    for seed in SEEDS:
        if any(seed in v["indexes"] for v in index.values()):
            continue
        try:
            url, page = get(seed)
        except Exception as e:
            print(f"index {seed}: {e}")
            continue
        n = 0
        for slug, name, d in ENTRY.findall(article(page)):
            e = index.setdefault(slug, {"name": text(name), "def": text(d)[:300], "indexes": []})
            if seed not in e["indexes"]:
                e["indexes"].append(seed)
            n += 1
        print(f"index {seed:28} {n:4} entries")
        idx_path.write_text(json.dumps(index, ensure_ascii=False, indent=1), encoding="utf-8")
        time.sleep(1)

    # 2 · every listed trope: its outbound Main/ links (the raw edges)
    todo = [s for s in index if s not in done][:limit]
    print(f"tropes: {len(index)} listed · {len(done)} cached · fetching {len(todo)}")
    with tr_path.open("a", encoding="utf-8") as f:
        for n, slug in enumerate(todo, 1):
            try:
                url, page = get(slug)
            except Exception as e:
                print(f"  {slug}: {e}")
                time.sleep(2)
                continue
            art = article(page)
            links = sorted({s for s, _ in LINK.findall(art) if s != slug})
            f.write(json.dumps({"slug": slug, "final": url.rsplit("/", 1)[-1].split("?")[0],
                                "links": links}, ensure_ascii=False) + "\n")
            f.flush()
            if n % 50 == 0:
                print(f"  {n}/{len(todo)}")
            time.sleep(1)
    print("done")


if __name__ == "__main__":
    main()
