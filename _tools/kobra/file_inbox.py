"""
file_inbox.py - files the Kobra Cart's link inbox into picks, price pulled from the link (Chief 10/8: "automatically take
the price from the link I send you"). Zero tokens past the two tool calls that move the inbox in and out.

    1. ArtifactData list  url=<cart>  collection=inbox  out_dir=<dir>     (saves each submitted link as JSON)
    2. python file_inbox.py <dir>                                         (this: fetch each page, write picks, rebuild)
    3. publish KOBRA-CART.html + KOBRA-ORDER.html, then batch-delete the inbox ids this prints

Per link: the Amazon page gives the title and the live price; the price Chief typed is only the fallback. A filament on a
cardboard spool gets flagged (the ACE Pro takes plastic spools only). A link with no item number lands in an "Added" phase.
"""
import glob
import io
import json
import os
import re
import subprocess
import sys
import html as H
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
UA = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/126 Safari/537.36"


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "en-US"})
    with urllib.request.urlopen(req, timeout=30) as r:
        raw = r.read()
    if r.headers.get("Content-Encoding") == "gzip":
        import gzip
        raw = gzip.decompress(raw)
    return raw.decode("utf-8", "ignore")


def read_page(url):
    """-> (clean url, title, price or None, flags)"""
    m = re.search(r"/(?:dp|gp/product)/([A-Z0-9]{10})", url)
    clean = "https://www.amazon.com/dp/%s?th=1" % m.group(1) if m else url
    try:
        s = fetch(clean)
    except Exception as e:
        return clean, None, None, ["page didn't load (%s)" % e.__class__.__name__]
    t = re.search(r'id="productTitle"[^>]*>([\s\S]*?)</span>', s)
    title = re.sub(r"\s+", " ", H.unescape(t.group(1))).strip() if t else None
    p = re.search(r'"priceAmount":([0-9.]+)', s) or re.search(r'class="a-offscreen">\$([0-9.,]+)<', s)
    price = float(p.group(1).replace(",", "")) if p else None
    bullets = re.search(r'id="feature-bullets"[\s\S]{0,20000}?</ul>', s)
    own = (title or "") + " " + (H.unescape(re.sub(r"<[^>]+>", " ", bullets.group(0))) if bullets else "")
    own += " " + url.split("?")[0].replace("-", " ")   # Amazon's own URL slug often names the spool ("...Cardboard/dp/...")
    flags = []
    if re.search(r"filament", own, re.I) and re.search(r"cardboard", own, re.I):
        flags.append("CARDBOARD spool: the ACE Pro takes plastic spools only")
    return clean, title, price, flags


def main(src):
    cart_p = os.path.join(HERE, "cart.json")
    cart = json.load(io.open(cart_p, encoding="utf-8"))
    byno = {it["no"]: it for ph in cart["phases"] for it in ph["items"]}
    docs = []
    for f in sorted(glob.glob(os.path.join(src, "**", "*.json"), recursive=True)):
        d = json.load(io.open(f, encoding="utf-8"))
        data = d.get("data", d)
        docs.append((d.get("id") or os.path.splitext(os.path.basename(f))[0], data))
    filed = []
    if docs:   # a new round: last round's highlights fade, this round's stand out
        for ph in cart["phases"]:
            for it in ph["items"]:
                it.pop("chg", None)
        cart["changes"] = {"when": __import__("datetime").datetime.now().strftime("%m/%d %H:%M"), "removed": []}
    for doc_id, v in docs:
        url = (v.get("url") or "").strip()
        if not url:
            continue
        clean, title, price, flags = read_page(url)
        typed = float(v["price"]) if str(v.get("price") or "").replace(".", "", 1).isdigit() else None
        if price is None:
            price = typed
            flags.append("price from what you typed" if typed is not None else "no price found: check it")
        name = (title or v.get("what") or "product")[:90]
        if flags:
            name += " · " + " · ".join(flags)
        no = v.get("item") or ""
        if no in byno:
            it = byno[no]
            it["pick"] = {"url": clean, "name": name, "price": price, "was": it.get("each", it["usd"] / it["q"])}
            it["chg"] = "picked · est $%s → $%s" % (it["pick"]["was"], price)
        else:   # not on the list: a new line in the "Added" phase
            added = next((ph for ph in cart["phases"] if ph["name"].startswith("Added")), None)
            if not added:
                added = {"name": "Added · from the inbox", "items": []}
                cart["phases"].append(added)
            used = [int(n) for n in byno if n.isdigit()]
            no = str(max([500] + [n for n in used if n >= 500]) + 1)
            it = {"no": no, "d": (v.get("what") or title or "added item")[:80], "q": 1, "usd": price or 0, "each": price or 0,
                  "link": clean, "pick": {"url": clean, "name": name, "price": price or 0}, "terms": []}
            it["chg"] = "new · $%s" % price
            added["items"].append(it)
            byno[no] = it
        filed.append(doc_id)
        print("%-4s $%-8s %s" % (no, price, name))
    io.open(cart_p, "w", encoding="utf-8").write(json.dumps(cart, ensure_ascii=False, indent=1))
    subprocess.run([sys.executable, "-I", os.path.join(HERE, "build.py")], check=True)
    print("FILED " + json.dumps(filed))


if __name__ == "__main__":
    main(sys.argv[1])
