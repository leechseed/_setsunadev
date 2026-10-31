"""BOLO 89 · the definitions pass (zero tokens).
For every register trope whose index line carried no definition, fetch its page and keep
the FIRST SENTENCE of the article only (the public-repo rule: one line, never page text).
Polite: one request a second, a normal User-Agent (fetch.UA), resumable.

10/31 (Chief: "run what you need"):
  * certifi's CA bundle: Python's default store on this box carries an expired root
    (same fix as _tools/bookmarks/dig.py _ssl_ctx).
  * an empty first sentence is retried (the 9/29-10/03 runs stored 790 empty strings: the
    first <p> was empty or the intro was not in a <p>); the extractor now skips quotes,
    image captions and empty paragraphs.
  * 404s and redirects to another trope are recorded in defs_status.json and never fetched again.
    A redirect is known from tropes.jsonl `final` without a request.
  * a 403 or 429 stops the run at once (the site is refusing us; never hammer, never retry around it).

usage: python -X utf8 _tools/tropes/fetch_defs.py [--limit N]
out:   _tools/tropes/data/domains/defs.json         {slug: first sentence}
       _tools/tropes/data/domains/defs_status.json  {slug: "ok" | "404" | "redirect:<Slug>" | "empty" | "err:<msg>"}
"""
import json, re, ssl, sys, time, urllib.error, urllib.request
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import fetch

D = Path(__file__).parent / "data" / "domains"
OUT = D / "defs.json"
STATUS = D / "defs_status.json"


def ssl_ctx():
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except (ImportError, OSError):
        return ssl.create_default_context()


CTX = ssl_ctx()


def get(slug):
    req = urllib.request.Request(fetch.BASE + slug, headers={"User-Agent": fetch.UA})
    with urllib.request.urlopen(req, timeout=30, context=CTX) as r:
        return r.geturl(), r.read().decode("utf-8", "replace")


def first_sentence(page):
    art = fetch.article(page)
    # drop the opening quote blocks and image captions, then take the first real paragraph
    art = re.sub(r"<div class=['\"](?:indent|quoteright|acaptionright)['\"].*?</div>", " ", art, flags=re.S)
    art = re.sub(r"<div class=['\"]quoteright['\"].*?</div>", " ", art, flags=re.S)
    cands = [fetch.text(p) for p in re.findall(r"<p>(.*?)</p>", art, re.S)]
    if not any(len(c) > 30 for c in cands):  # the intro sometimes sits loose, split by <br>
        head = re.split(r"<h2|<div class=['\"]folder", art, 1)[0]
        cands = [fetch.text(x) for x in re.split(r"<br\s*/?>\s*<br\s*/?>", head)]
    for c in cands:
        if len(c) > 30 and not c.startswith(("\"", "“", "Above:", "Pictured", "Image")):
            return re.split(r"(?<=[.!?])\s", c, 1)[0][:300]
    return ""


def main():
    limit = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else None
    idx = json.loads((D / "index.json").read_text(encoding="utf-8"))
    defs = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {}
    status = json.loads(STATUS.read_text(encoding="utf-8")) if STATUS.exists() else {}
    final = {}
    for l in (D / "tropes.jsonl").read_text(encoding="utf-8").splitlines():
        if l.strip():
            j = json.loads(l); final[j["slug"]] = j.get("final") or j["slug"]
    todo = [s for s, v in idx.items() if v.get("domains") and not v["def"].strip()
            and not defs.get(s, "").strip() and not str(status.get(s, "")).startswith(("404", "redirect"))]
    # redirects already on record: no request needed
    for s in list(todo):
        f = final.get(s, s)
        if f.lower() != s.lower():
            status[s] = f"redirect:{f}"; todo.remove(s)
    if limit: todo = todo[:limit]
    print(f"empty defs: {len(todo)} to fetch")
    got = 0
    def save():
        OUT.write_text(json.dumps(defs, ensure_ascii=False), encoding="utf-8")
        STATUS.write_text(json.dumps(status, ensure_ascii=False, indent=0), encoding="utf-8")
    for n, s in enumerate(todo, 1):
        try:
            url, page = get(s)
        except urllib.error.HTTPError as e:
            if e.code in (403, 429):
                print(f"  {s}: HTTP {e.code}, the site is refusing; stopping (no retries)")
                save(); print(f"stopped · fetched {got}"); return 2
            status[s] = "404" if e.code == 404 else f"err:{e.code}"
            print(f"  {s}: HTTP {e.code}"); time.sleep(1); continue
        except Exception as e:
            status[s] = f"err:{type(e).__name__}"; print(f"  {s}: {e}"); time.sleep(2); continue
        f = url.rsplit("/", 1)[-1].split("?")[0]
        if f.lower() != s.lower():
            status[s] = f"redirect:{f}"
        else:
            t = first_sentence(page)
            defs[s] = t; status[s] = "ok" if t else "empty"; got += bool(t)
        if n % 25 == 0:
            save(); print(f"  {n}/{len(todo)} · defs {got}")
        time.sleep(1)
    save()
    print(f"done · fetched {got}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
