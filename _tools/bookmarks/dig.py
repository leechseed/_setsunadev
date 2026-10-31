"""dig.py - THE BOOKMARK DIG (BOLO 167). Zero tokens, stdlib only.

Reads a COPY of Firefox's bookmark store (places.sqlite), dedupes, checks for
dead links, ranks the keepers, saves offline text copies, and builds one local
judging page. Every byte of bookmark data (titles, URLs, folders, pages) lives
under _PRIVATE/reference/bookmarks/ ; this script holds no URL from the data.

Never touches the live Firefox profile: copy places.sqlite (+ -wal) into
_PRIVATE/reference/bookmarks/src/ first. Deletes nothing in Firefox.

Verbs (each takes --json to print its result as JSON):
  scan      read the copy -> records.json (unique URLs, dupes, groups)
  check     dead-link check -> check.json (resumable cache)
  rank      score keepers -> ranked.json ; --titles N prints the top N for hand tagging
  ingest    save readable text of top live keepers -> pages/<id>.txt (cap 500)
  build     write bookmarks.html (Gold / Dupes / Dead / All)
  summary   counts
  marks F   read a marks export from the page and list the proposed tosses
  all       scan + check + rank + build

THE SCORE (rank), written down so Chief can argue with it:
  + visits       min(10, 2.5 * log2(1 + visit_count))
  + recent       +2 if last visited within 365 days
  + age, live    min(6, 1.5 * years since added), only when the link is live
  + named folder +3 when it sits in a folder Chief made (not loose in Toolbar/Other/Menu/Mobile)
  + saved twice  +1 when the same URL was bookmarked more than once (copies collapse into one)
  + real title   +1 when the title is not empty and not just the URL
  - home/login   -6 for a bare home page or a login/account/auth page
  - dead/gone    -20 (drops out of Gold)
  - error/timeout -2
  Gold = the top keepers with score > 0 that are not dead or gone.

Statuses: live (2xx/3xx) | dead (404/410) | gone (DNS fails) | blocked (401/403/429/451)
  | timeout | error (5xx, TLS, refused, other 4xx, too many redirects)
  | unchecked (sites that refuse bots, and non-web links).
"""
from __future__ import annotations

import argparse
import concurrent.futures as cf
import datetime as dt
import html
import html.parser
import json
import math
import re
import socket
import sqlite3
import ssl
import sys
import threading
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BM = ROOT / "_PRIVATE" / "reference" / "bookmarks"
SRC = BM / "src" / "places.sqlite"
RECORDS = BM / "records.json"
CHECK = BM / "check.json"
RANKED = BM / "ranked.json"
TOPICS = BM / "topics.json"          # hand-judged {pid: topic}, written by the CDR reading titles
ADULT_FILE = BM / "adult_domains.txt"  # private, one domain per line
BOT_FILE = BM / "bot_refuse.txt"       # private, extra sites that wall off bots
NO_TEXT_FILE = BM / "no_text.txt"      # private, sites whose pages come back as a bot wall
INGEST = BM / "ingest.json"
PAGES = BM / "pages"
PAGE = BM / "bookmarks.html"

UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:131.0) "
      "Gecko/20100101 Firefox/131.0")
HEADERS = {
    "User-Agent": UA,
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
}
TIMEOUT = 10
WORKERS = 8
PER_HOST = 2
MAX_REDIRECTS = 5
GET_CAP = 64 * 1024            # dead-link GET fallback reads at most this
PAGE_FETCH_CAP = 3 * 1024 * 1024
TEXT_CAP = 200 * 1024

# Sites known to refuse bots: never checked, never called dead.
BOT_REFUSE = ("x.com", "twitter.com", "reddit.com", "onlyfans.com", "pornhub.com")
# Generic words that mark a domain adult (text is never saved for these).
ADULT_WORDS = ("porn", "xxx", "sex", "nsfw", "hentai", "onlyfans", "fansly", "camgirl", "escort")
TRACKING = re.compile(r"^(utm_.*|fbclid|gclid|dclid|msclkid|mc_cid|mc_eid|igshid|ref_src|ref_url|si|spm)$", re.I)
LOGINISH = re.compile(r"(log-?in|sign-?in|sign-?up|signon|/account|/auth|oauth|/dashboard|logout|/register|/session)", re.I)
ROOT_NAMES = {1: "", 2: "Menu", 3: "Toolbar", 4: "Tags", 5: "Other", 6: "Mobile"}


# ---------------------------------------------------------------- helpers

def out(data, as_json: bool, text: str = ""):
    if as_json:
        print(json.dumps(data, ensure_ascii=False, indent=1))
    else:
        print(text or json.dumps(data, ensure_ascii=False, indent=1))


def load(p: Path, default):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return default


def save(p: Path, data):
    p.parent.mkdir(parents=True, exist_ok=True)
    tmp = p.with_suffix(p.suffix + ".tmp")
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=0), encoding="utf-8")
    tmp.replace(p)


def host_of(url: str) -> str:
    try:
        h = (urllib.parse.urlsplit(url).hostname or "").lower()
    except ValueError:
        return ""
    return h[4:] if h.startswith("www.") else h


def domain_match(host: str, names) -> bool:
    return any(host == n or host.endswith("." + n) for n in names)


def normalize(url: str) -> str:
    """Same page, same key: drop scheme difference, www., default port,
    fragment, tracking params, trailing slash; sort the query."""
    try:
        s = urllib.parse.urlsplit(url.strip())
    except ValueError:
        return url.strip()
    if s.scheme not in ("http", "https"):
        return url.strip()
    host = (s.hostname or "").lower()
    if host.startswith("www."):
        host = host[4:]
    try:
        port = s.port
    except ValueError:
        port = None
    if port and port not in (80, 443):
        host = f"{host}:{port}"
    path = s.path or "/"
    if len(path) > 1:
        path = path.rstrip("/")
    q = [(k, v) for k, v in urllib.parse.parse_qsl(s.query, keep_blank_values=True) if not TRACKING.match(k)]
    q.sort()
    return f"{host}{path}" + (("?" + urllib.parse.urlencode(q)) if q else "")


def adult_domains() -> set[str]:
    try:
        return {ln.strip().lower() for ln in ADULT_FILE.read_text(encoding="utf-8").splitlines()
                if ln.strip() and not ln.startswith("#")}
    except OSError:
        return set()


def is_adult(host: str, topic: str | None, extra: set[str]) -> bool:
    if topic and topic.startswith("adult"):
        return True
    if domain_match(host, extra) or domain_match(host, ("onlyfans.com", "pornhub.com")):
        return True
    return any(w in host for w in ADULT_WORDS)


def is_home_or_login(url: str) -> bool:
    try:
        s = urllib.parse.urlsplit(url)
    except ValueError:
        return False
    if (s.path in ("", "/")) and not s.query:
        return True
    return bool(LOGINISH.search(s.path + "?" + s.query))


def us_to_iso(us) -> str | None:
    if not us:
        return None
    try:
        return dt.datetime.fromtimestamp(us / 1_000_000, dt.timezone.utc).strftime("%Y-%m-%d")
    except (OverflowError, OSError, ValueError):
        return None


# ---------------------------------------------------------------- scan

def scan(src: Path = SRC) -> dict:
    if not src.exists():
        raise SystemExit(f"no copy at {src}; copy places.sqlite there first")
    # read-only URI so the copy is never altered either (the -wal next to it is read in)
    con = sqlite3.connect(f"file:{src.as_posix()}?mode=ro", uri=True)
    folders = {fid: (parent, title or "") for fid, parent, title in
               con.execute("select id, parent, title from moz_bookmarks where type=2")}

    def path_of(fid: int) -> str:
        parts, seen = [], set()
        while fid and fid not in seen:
            seen.add(fid)
            if fid in ROOT_NAMES:
                if ROOT_NAMES[fid]:
                    parts.append(ROOT_NAMES[fid])
                break
            parent, title = folders.get(fid, (0, "?"))
            parts.append(title or "(untitled)")
            fid = parent
        return " / ".join(reversed(parts))

    rows = con.execute("""
        select b.id, b.parent, b.title, b.dateAdded, p.id, p.url, p.title,
               p.visit_count, p.last_visit_date
        from moz_bookmarks b join moz_places p on p.id = b.fk
        where b.type = 1 order by b.dateAdded, b.id""").fetchall()
    con.close()

    groups: dict[str, list] = defaultdict(list)
    for bid, parent, btitle, added, pid, url, ptitle, visits, last in rows:
        groups[normalize(url)].append({
            "bid": bid, "pid": pid, "url": url,
            "title": (btitle or ptitle or "").strip(),
            "folder": path_of(parent), "named": parent not in ROOT_NAMES,
            "added": us_to_iso(added), "added_us": added or 0,
            "visits": visits or 0, "last": us_to_iso(last), "last_us": last or 0,
        })

    items, dupes = [], []
    for key, copies in groups.items():
        copies.sort(key=lambda c: (not c["named"], -c["visits"], c["added_us"]))
        keep = dict(copies[0])
        keep["id"] = f"b{keep['bid']}"
        keep["key"] = key
        keep["host"] = host_of(keep["url"])
        keep["copies"] = len(copies)
        keep["visits"] = max(c["visits"] for c in copies)
        keep["last_us"] = max(c["last_us"] for c in copies)
        keep["last"] = us_to_iso(keep["last_us"])
        keep["added_us"] = min(c["added_us"] for c in copies)
        keep["added"] = us_to_iso(keep["added_us"])
        keep["named"] = any(c["named"] for c in copies)
        if not keep["title"]:
            keep["title"] = next((c["title"] for c in copies if c["title"]), "")
        items.append(keep)
        if len(copies) > 1:
            dupes.append({"id": keep["id"], "key": key, "title": keep["title"],
                          "url": keep["url"], "host": keep["host"],
                          "copies": [{"bid": c["bid"], "folder": c["folder"], "added": c["added"],
                                      "title": c["title"]} for c in copies]})

    by_domain = Counter(i["host"] for i in items)
    by_folder = Counter(c["folder"] for cs in groups.values() for c in cs)
    data = {
        "scanned": dt.datetime.now().isoformat(timespec="seconds"),
        "total": len(rows), "unique": len(items),
        "dupe_copies": len(rows) - len(items), "dupe_groups": len(dupes),
        "by_domain": by_domain.most_common(), "by_folder": by_folder.most_common(),
        "items": items, "dupes": dupes,
    }
    save(RECORDS, data)
    return data


# ---------------------------------------------------------------- dead-link check

class _FewRedirects(urllib.request.HTTPRedirectHandler):
    max_redirections = MAX_REDIRECTS
    max_repeats = 2


def _ssl_ctx():
    # The Windows store on this box carries an expired root that OpenSSL picks
    # ("certificate has expired" on big live sites); certifi's bundle builds the
    # right chain. Fall back to the system store when certifi is absent.
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except (ImportError, OSError):
        return ssl.create_default_context()


def _opener():
    # a fresh cookie jar per request: some sites set a cookie on the first hop and loop without it
    import http.cookiejar
    ctx = _ssl_ctx()
    return urllib.request.build_opener(_FewRedirects(), urllib.request.HTTPSHandler(context=ctx),
                                       urllib.request.HTTPCookieProcessor(http.cookiejar.CookieJar()))


def private_list(p: Path) -> tuple[str, ...]:
    try:
        return tuple(ln.strip().lower() for ln in p.read_text(encoding="utf-8").splitlines()
                     if ln.strip() and not ln.startswith("#"))
    except OSError:
        return ()


def bot_refuse() -> tuple[str, ...]:
    """BOT_REFUSE plus the private list (domains that answered with an anti-bot wall)."""
    return BOT_REFUSE + private_list(BOT_FILE)


_host_locks: dict[str, threading.Semaphore] = defaultdict(lambda: threading.Semaphore(PER_HOST))
_host_guard = threading.Lock()


def _host_sem(host: str) -> threading.Semaphore:
    with _host_guard:
        return _host_locks[host]


def classify_code(code: int) -> str:
    if 200 <= code < 400:
        return "live"
    if code in (404, 410):
        return "dead"
    if code in (401, 403, 429, 451):
        return "blocked"
    return "error"


def _classify_exc(e: BaseException) -> tuple[str, str]:
    if isinstance(e, urllib.error.HTTPError):
        if 300 <= e.code < 400:
            return "error", "too many redirects"
        return classify_code(e.code), f"HTTP {e.code}"
    reason = getattr(e, "reason", e)
    if isinstance(reason, socket.gaierror):
        return "gone", "DNS"
    if isinstance(reason, (socket.timeout, TimeoutError)) or "timed out" in str(reason).lower():
        return "timeout", "timeout"
    if isinstance(reason, ssl.SSLError) or "ssl" in str(reason).lower() or "certificate" in str(reason).lower():
        return "error", "TLS"
    return "error", type(reason).__name__ + ": " + str(reason)[:80]


def _request(opener, url: str, method: str):
    req = urllib.request.Request(url, headers=HEADERS, method=method)
    with opener.open(req, timeout=TIMEOUT) as r:
        if method == "GET":
            r.read(GET_CAP)
        return r.status, r.geturl()


def check_one(url: str) -> dict:
    host = host_of(url)
    scheme = urllib.parse.urlsplit(url).scheme
    if scheme not in ("http", "https"):
        return {"status": "unchecked", "why": "not a web link"}
    if domain_match(host, bot_refuse()):
        return {"status": "unchecked", "why": "site refuses bots"}
    opener = _opener()
    with _host_sem(host):
        first = None
        try:
            code, final = _request(opener, url, "HEAD")
            st = classify_code(code)
            if st == "live":
                return {"status": "live", "code": code, "final": final if final != url else None}
            first = (st, f"HTTP {code}")
        except Exception as e:  # noqa: BLE001 - every failure is a status
            first = _classify_exc(e)
            if first[0] in ("gone",):
                return {"status": first[0], "why": first[1]}
        # HEAD failed or refused: one capped GET decides
        try:
            code, final = _request(opener, url, "GET")
            st = classify_code(code)
            return {"status": st, "code": code, "final": final if final != url else None}
        except Exception as e:  # noqa: BLE001
            st, why = _classify_exc(e)
            return {"status": st, "why": why, "head": first[1] if first else None}


def check(limit: int | None = None, recheck: bool = False, workers: int = WORKERS,
          redo: str | None = None) -> dict:
    rec = load(RECORDS, None) or scan()
    cache = {} if recheck else load(CHECK, {})
    if redo:  # recheck only rows with these statuses, e.g. "error,timeout"
        want = set(redo.split(","))
        cache = {k: v for k, v in cache.items() if v.get("status") not in want}
    todo = [i for i in rec["items"] if i["key"] not in cache]
    if limit:
        todo = todo[:limit]
    lock = threading.Lock()
    done = 0
    t0 = time.time()
    with cf.ThreadPoolExecutor(max_workers=min(workers, WORKERS)) as ex:
        futs = {ex.submit(check_one, i["url"]): i for i in todo}
        for f in cf.as_completed(futs):
            i = futs[f]
            try:
                res = f.result()
            except Exception as e:  # noqa: BLE001
                res = {"status": "error", "why": repr(e)[:80]}
            res["at"] = dt.datetime.now().isoformat(timespec="seconds")
            with lock:
                cache[i["key"]] = res
                done += 1
                if done % 50 == 0:
                    save(CHECK, cache)
                    print(f"  checked {done}/{len(todo)} ({time.time()-t0:.0f}s)", file=sys.stderr, flush=True)
    save(CHECK, cache)
    counts = Counter(cache.get(i["key"], {}).get("status", "pending") for i in rec["items"])
    return {"checked_now": done, "seconds": round(time.time() - t0), "status": dict(counts)}


# ---------------------------------------------------------------- rank

def score(item: dict, status: str, now_us: int) -> float:
    s = min(10.0, 2.5 * math.log2(1 + item["visits"]))
    if item["last_us"] and now_us - item["last_us"] < 365 * 86400 * 1_000_000:
        s += 2
    if status == "live" and item["added_us"]:
        years = (now_us - item["added_us"]) / (365.25 * 86400 * 1_000_000)
        s += min(6.0, 1.5 * max(0.0, years))
    if item["named"]:
        s += 3
    if item["copies"] > 1:
        s += 1
    if item["title"] and item["title"] != item["url"]:
        s += 1
    if is_home_or_login(item["url"]):
        s -= 6
    if status in ("dead", "gone"):
        s -= 20
    elif status in ("error", "timeout"):
        s -= 2
    return round(s, 2)


def rank() -> dict:
    rec = load(RECORDS, None) or scan()
    cache = load(CHECK, {})
    now_us = int(time.time() * 1_000_000)
    ranked = []
    for i in rec["items"]:
        st = cache.get(i["key"], {}).get("status", "pending")
        ranked.append({"id": i["id"], "score": score(i, st, now_us), "status": st})
    ranked.sort(key=lambda r: -r["score"])
    for n, r in enumerate(ranked, 1):
        r["rank"] = n
    save(RANKED, ranked)
    gold = [r for r in ranked if r["score"] > 0 and r["status"] not in ("dead", "gone")]
    return {"ranked": len(ranked), "gold_pool": len(gold)}


def titles(n: int) -> list[str]:
    """Top-n lines for the hand read: id | title | host | folder."""
    rec = load(RECORDS, None)
    by_id = {i["id"]: i for i in rec["items"]}
    lines = []
    for r in load(RANKED, [])[:n]:
        i = by_id[r["id"]]
        lines.append(f"{r['id']}\t{i['title'][:90]}\t{i['host']}\t{i['folder']}")
    return lines


# ---------------------------------------------------------------- ingest

SKIP_TAGS = {"script", "style", "noscript", "svg", "nav", "header", "footer", "aside", "form",
             "button", "select", "template", "iframe", "canvas", "object", "head"}
BLOCK_TAGS = {"p", "div", "br", "li", "ul", "ol", "h1", "h2", "h3", "h4", "h5", "h6", "tr",
              "section", "article", "main", "blockquote", "pre", "table", "dd", "dt", "hr", "figcaption"}


class _Text(html.parser.HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.skip = 0
        self.main = 0
        self.all: list[str] = []
        self.core: list[str] = []
        self.title = ""
        self._in_title = False

    def handle_starttag(self, tag, attrs):
        if tag == "title":
            self._in_title = True
        if tag in SKIP_TAGS:
            self.skip += 1
        if tag in ("article", "main"):
            self.main += 1
        if tag in BLOCK_TAGS:
            self._emit("\n")
        if tag in ("h1", "h2", "h3") and not self.skip:
            self._emit("# ")

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
        if tag in SKIP_TAGS and self.skip:
            self.skip -= 1
        if tag in ("article", "main") and self.main:
            self.main -= 1
        if tag in BLOCK_TAGS:
            self._emit("\n")

    def handle_data(self, data):
        if self._in_title:
            self.title += data
            return
        if not self.skip:
            self._emit(data)

    def _emit(self, s):
        self.all.append(s)
        if self.main:
            self.core.append(s)


def _tidy(parts: list[str]) -> str:
    t = "".join(parts)
    t = re.sub(r"[ \t\r\f\v]+", " ", t)
    t = re.sub(r" *\n *", "\n", t)
    t = re.sub(r"\n{3,}", "\n\n", t)
    return t.strip()


def extract_text(raw: bytes, ctype: str) -> tuple[str, str]:
    m = re.search(r"charset=([\w-]+)", ctype or "", re.I)
    enc = m.group(1) if m else None
    if not enc:
        m2 = re.search(rb"<meta[^>]+charset=[\"']?([\w-]+)", raw[:4096], re.I)
        enc = m2.group(1).decode("ascii", "ignore") if m2 else "utf-8"
    try:
        doc = raw.decode(enc, errors="replace")
    except LookupError:
        doc = raw.decode("utf-8", errors="replace")
    if "html" not in (ctype or "").lower() and "<html" not in doc[:2000].lower():
        return "", doc
    p = _Text()
    try:
        p.feed(doc)
        p.close()
    except Exception:  # noqa: BLE001 - broken markup still gives partial text
        pass
    core, full = _tidy(p.core), _tidy(p.all)
    return html.unescape(p.title.strip()), core if len(core) >= 500 else full


def ingest_one(item: dict) -> dict:
    host = item["host"]
    opener = _opener()
    with _host_sem(host):
        try:
            req = urllib.request.Request(item["url"], headers=HEADERS)
            with opener.open(req, timeout=TIMEOUT) as r:
                ctype = r.headers.get("Content-Type", "")
                if "pdf" in ctype.lower():
                    return {"saved": False, "why": "pdf"}
                if not any(k in ctype.lower() for k in ("html", "text", "xml")) and ctype:
                    return {"saved": False, "why": "not text: " + ctype[:40]}
                raw = r.read(PAGE_FETCH_CAP)
        except Exception as e:  # noqa: BLE001
            return {"saved": False, "why": _classify_exc(e)[1]}
    ptitle, text = extract_text(raw, ctype)
    if len(text) < 200:
        return {"saved": False, "why": "thin (script-only page)"}
    head = (f"TITLE: {item['title'] or ptitle}\nURL: {item['url']}\nFOLDER: {item['folder']}\n"
            f"ADDED: {item['added']}\nSAVED: {dt.date.today().isoformat()}\n\n")
    body = (head + text).encode("utf-8")[:TEXT_CAP].decode("utf-8", "ignore")
    PAGES.mkdir(parents=True, exist_ok=True)
    (PAGES / f"{item['id']}.txt").write_text(body, encoding="utf-8")
    return {"saved": True, "chars": len(body)}


def ingest(max_pages: int = 500, dry_run: bool = False) -> dict:
    rec = load(RECORDS, None)
    by_id = {i["id"]: i for i in rec["items"]}
    topics = load(TOPICS, {})
    extra = adult_domains()
    log = load(INGEST, {})
    picks, adult_listed = [], []
    refuse = bot_refuse()
    no_text = private_list(NO_TEXT_FILE)  # sites that wall page fetches behind a bot check
    for r in load(RANKED, []):
        if r["status"] != "live" or r["score"] <= 0:
            continue
        i = by_id[r["id"]]
        if domain_match(i["host"], refuse) or "(toss)" in topics.get(i["id"], ""):
            continue
        if is_adult(i["host"], topics.get(i["id"]), extra):
            adult_listed.append(i["id"])
            continue
        tried = log.get(i["id"])
        if tried and not tried.get("saved"):
            continue  # tried once and failed: the cap counts pages saved, so move down the list
        if i["id"] not in topics:
            continue  # text is saved only for rows a reader has tagged
        if not tried and domain_match(i["host"], no_text):
            continue
        picks.append(i)
        if len(picks) >= max_pages:
            break
    todo = [i for i in picks if not log.get(i["id"], {}).get("saved")]
    if dry_run:
        return {"would_fetch": len(todo), "already": len(picks) - len(todo), "adult_listed_only": len(adult_listed)}
    with cf.ThreadPoolExecutor(max_workers=WORKERS) as ex:
        futs = {ex.submit(ingest_one, i): i for i in todo}
        for n, f in enumerate(cf.as_completed(futs), 1):
            i = futs[f]
            try:
                log[i["id"]] = f.result()
            except Exception as e:  # noqa: BLE001
                log[i["id"]] = {"saved": False, "why": repr(e)[:80]}
            if n % 25 == 0:
                save(INGEST, log)
                print(f"  ingest {n}/{len(todo)}", file=sys.stderr, flush=True)
    save(INGEST, log)
    saved = sum(1 for v in log.values() if v.get("saved"))
    why = Counter(v.get("why") for v in log.values() if not v.get("saved"))
    return {"picked": len(picks), "saved_total": saved, "skipped": dict(why.most_common(12)),
            "adult_listed_only": len(adult_listed)}


# ---------------------------------------------------------------- summary

def summary() -> dict:
    rec = load(RECORDS, None)
    if not rec:
        return {"error": "run scan first"}
    cache = load(CHECK, {})
    topics = load(TOPICS, {})
    st = Counter(cache.get(i["key"], {}).get("status", "pending") for i in rec["items"])
    ing = load(INGEST, {})
    return {
        "total": rec["total"], "unique": rec["unique"], "dupe_copies": rec["dupe_copies"],
        "dupe_groups": rec["dupe_groups"], "status": dict(st),
        "topics": dict(Counter(topics.values()).most_common()),
        "pages_saved": sum(1 for v in ing.values() if v.get("saved")),
        "folders": len(rec["by_folder"]), "domains": len(rec["by_domain"]),
    }


def marks(path: Path) -> dict:
    m = load(path, {})
    rec = load(RECORDS, None)
    by_id = {i["id"]: i for i in rec["items"]}
    toss = [k for k, v in m.get("marks", m).items() if v == "toss"]
    keep = [k for k, v in m.get("marks", m).items() if v == "keep"]
    prop = [{"id": k, "title": by_id[k]["title"], "folder": by_id[k]["folder"]} for k in toss if k in by_id]
    save(BM / "toss_proposal.json", prop)
    return {"keep": len(keep), "toss": len(toss), "proposal": str(BM / "toss_proposal.json"),
            "note": "proposal only; nothing in Firefox is changed"}


# ---------------------------------------------------------------- build

def build() -> dict:
    rec = load(RECORDS, None)
    cache = load(CHECK, {})
    ranked = {r["id"]: r for r in load(RANKED, [])}
    topics = load(TOPICS, {})
    ing = load(INGEST, {})
    extra = adult_domains()
    rows = []
    for i in rec["items"]:
        c = cache.get(i["key"], {})
        r = ranked.get(i["id"], {})
        topic = topics.get(i["id"])
        rows.append({
            "id": i["id"], "t": i["title"] or i["url"], "u": i["url"], "h": i["host"],
            "f": i["folder"], "s": c.get("status", "pending"), "w": c.get("why") or (f"HTTP {c['code']}" if c.get("code") else ""),
            "sc": r.get("score", 0), "rk": r.get("rank", 0), "tp": topic or "",
            "v": i["visits"], "a": i["added"] or "", "l": i["last"] or "", "n": i["copies"],
            "off": bool(ing.get(i["id"], {}).get("saved")),
            "ad": is_adult(i["host"], topic, extra),
        })
    dupes = rec["dupes"]
    meta = summary()
    payload = json.dumps({"rows": rows, "dupes": dupes, "meta": meta}, ensure_ascii=False).replace("</", "<\\/")
    PAGE.write_text(PAGE_TEMPLATE.replace("/*DATA*/null", payload), encoding="utf-8")
    return {"page": str(PAGE), "rows": len(rows), "gold": sum(1 for r in rows if r["tp"])}


PAGE_TEMPLATE = r"""<!doctype html>
<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Bookmark Dig</title>
<style>
:root{--bg:#141414;--panel:#1d1d1d;--line:#2c2c2c;--ink:#e6e6e6;--dim:#9a9a9a;--acc:#FF5A1F;
--live:#5fbf6a;--dead:#e0533d;--gone:#b0453a;--blocked:#d9a33a;--timeout:#8e8ad8;--error:#c77;--unchecked:#777;--pending:#555}
*{box-sizing:border-box}html,body{margin:0;background:var(--bg);color:var(--ink);font:14px/1.45 system-ui,Segoe UI,sans-serif}
header{height:44px;display:flex;align-items:center;gap:14px;padding:0 16px;border-bottom:2px solid var(--acc);background:#101010;position:sticky;top:0;z-index:5}
header b{color:var(--acc);letter-spacing:.06em;white-space:nowrap}
.tabs{display:flex;gap:4px}.tab{background:none;border:0;color:var(--dim);padding:6px 10px;cursor:pointer;font:inherit;border-radius:4px}
.tab.on{color:#fff;background:#2a1a12;box-shadow:inset 0 -2px 0 var(--acc)}
#q{margin-left:auto;background:var(--panel);border:1px solid var(--line);color:var(--ink);padding:5px 9px;border-radius:4px;width:min(320px,40vw)}
main{padding:12px 16px;max-width:1300px;margin:0 auto}
.todo{background:var(--panel);border-left:3px solid var(--acc);padding:10px 14px;margin-bottom:12px;border-radius:3px}
.todo h3{margin:0 0 4px;font-size:14px;color:var(--acc)}.todo ol{margin:4px 0 0 18px;padding:0}
.stats{color:var(--dim);font-size:12px;margin:6px 0 0}
.bar{display:flex;gap:8px;align-items:center;margin:8px 0;flex-wrap:wrap}
.btn{background:#222;color:var(--ink);border:1px solid var(--line);padding:4px 10px;border-radius:4px;cursor:pointer;font:inherit;font-size:12px}
.btn:hover{border-color:var(--acc)}
h2{font-size:13px;color:var(--acc);text-transform:uppercase;letter-spacing:.08em;margin:18px 0 6px;border-bottom:1px solid var(--line);padding-bottom:3px}
h2 span{color:var(--dim)}
table{width:100%;border-collapse:collapse;table-layout:fixed}
td{padding:4px 6px;border-bottom:1px solid var(--line);vertical-align:top;overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
tr:hover td{background:#1a1a1a}
td.t{width:40%}td.h{width:15%;color:var(--dim)}td.f{width:17%;color:var(--dim);font-size:12px}td.s{width:9%}td.k{width:19%;text-align:right}
td.t a{color:var(--ink);text-decoration:none}td.t a:hover{color:var(--acc)}
.chip{display:inline-block;font-size:11px;padding:1px 6px;border-radius:9px;background:#262626;color:var(--dim);cursor:help}
.st{color:#111;font-weight:600}
.sc{color:var(--dim);font-size:11px;margin-left:4px}
.mk{background:none;border:1px solid var(--line);color:var(--dim);border-radius:3px;font-size:11px;padding:1px 6px;cursor:pointer;margin-left:3px}
.mk.keep.on{background:var(--live);color:#111;border-color:var(--live)}.mk.toss.on{background:var(--dead);color:#111;border-color:var(--dead)}
.off{color:var(--acc);font-size:11px;margin-left:3px;text-decoration:none}
tr.tossed td{opacity:.45}
.dg td{white-space:normal}.copies{color:var(--dim);font-size:12px}
.more{color:var(--dim);font-size:12px;padding:6px}
.jump{display:flex;flex-wrap:wrap;gap:5px;margin:4px 0 6px}.jump .chip{cursor:pointer;text-decoration:none;color:var(--ink);background:#2a1a12;border:1px solid #4a2a1a}
.jump .chip:hover{border-color:var(--acc)}.jump .chip.dim{background:#222;color:var(--dim);border-color:var(--line)}
h2{scroll-margin-top:54px}
@media (max-width:760px){td.h,td.f{display:none}td.t{width:60%}td.k{width:28%}header{gap:8px}#q{width:30vw}}
</style></head><body>
<header><b>BOOKMARK DIG</b>
<nav class="tabs"><button class="tab on" data-t="gold">Gold</button><button class="tab" data-t="dupes">Dupes</button><button class="tab" data-t="dead">Dead</button><button class="tab" data-t="all">All</button></nav>
<input id="q" placeholder="filter: title, site, folder, topic" autocomplete="off"></header>
<main>
<div class="todo"><h3>What to do</h3><ol>
<li>Work the <b>Gold</b> tab first: these are the ranked keepers, sorted into topics. Click <b>keep</b> or <b>toss</b> on a row (click again to clear). Marks save in this browser as you go.</li>
<li>Then <b>Dead</b> (404, 410 and dead DNS: safe tosses) and <b>Dupes</b> (the same page saved more than once: toss the copies you don't need).</li>
<li>When done, press <b>Export marks</b> and save the file into <code>_PRIVATE/reference/bookmarks/</code>. Then say "bookmark marks" and the dig turns it into a toss list. Nothing in Firefox changes until you say so.</li>
</ol><div class="stats" id="stats"></div></div>
<div class="bar"><button class="btn" id="exp">Export marks</button><button class="btn" id="hideToss">Hide tossed</button><span class="stats" id="mcount"></span></div>
<div id="view"></div>
</main>
<script>
const D=/*DATA*/null;
const ST={live:"Answered (2xx/3xx). The page is up.",dead:"404 or 410. The page is gone; safe to toss.",gone:"The site's name no longer resolves (DNS). The site is gone.",blocked:"401/403/429: the site refused the checker. Probably fine; open it to see.",timeout:"No answer in 10 seconds. Try it by hand.",error:"Server error, TLS error or too many redirects. Try it by hand.",unchecked:"Site refuses bots (or not a web link), so it was never checked.",pending:"Not checked yet."};
const SC={live:"var(--live)",dead:"var(--dead)",gone:"var(--gone)",blocked:"var(--blocked)",timeout:"var(--timeout)",error:"var(--error)",unchecked:"var(--unchecked)",pending:"var(--pending)"};
let M={};try{M=JSON.parse(localStorage.getItem("bmdig.marks")||"{}")}catch(e){M={}}
let hideT=false,tab="gold",q="";
const byId=Object.fromEntries(D.rows.map(r=>[r.id,r]));
function saveM(){try{localStorage.setItem("bmdig.marks",JSON.stringify(M))}catch(e){};count()}
function count(){const v=Object.values(M);document.getElementById("mcount").textContent=v.filter(x=>x=="keep").length+" keep · "+v.filter(x=>x=="toss").length+" toss"}
function esc(s){return String(s).replace(/[&<>"]/g,c=>({"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;"}[c]))}
function hit(r){if(!q)return true;return (r.t+" "+r.h+" "+r.f+" "+r.tp).toLowerCase().includes(q)}
function row(r){const m=M[r.id]||"";if(hideT&&m=="toss")return"";
const tip="Score "+r.sc+" · rank "+r.rk+" · visits "+r.v+" · added "+r.a+(r.l?" · last visit "+r.l:"")+(r.n>1?" · saved "+r.n+" times":"");
return `<tr class="${m=="toss"?"tossed":""}" data-id="${r.id}"><td class="t" title="${esc(r.t)}"><a href="${esc(r.u)}" target="_blank" rel="noopener noreferrer">${esc(r.t)}</a><span class="sc" title="${esc(tip)}">${r.sc}</span></td><td class="h">${esc(r.h)}</td><td class="f" title="${esc(r.f)}">${esc(r.f)}</td><td class="s"><span class="chip st" style="background:${SC[r.s]}" title="${esc(ST[r.s]+(r.w?" ("+r.w+")":""))}">${r.s}</span></td><td class="k">${r.off?`<a class="off" href="pages/${r.id}.txt" target="_blank" title="Offline text copy">txt</a>`:""}${r.tp?`<span class="chip" title="Topic, hand-tagged by reading the title">${esc(r.tp)}</span>`:""}<button class="mk keep ${m=="keep"?"on":""}" data-m="keep">keep</button><button class="mk toss ${m=="toss"?"on":""}" data-m="toss">toss</button></td></tr>`}
function table(rs,cap){const shown=rs.slice(0,cap||rs.length);return `<table>${shown.map(row).join("")}</table>`+(rs.length>shown.length?`<div class="more">${rs.length-shown.length} more; type in the filter to narrow.</div>`:"")}
function render(){const v=document.getElementById("view");let h="";
if(tab=="gold"){const g=D.rows.filter(r=>r.tp&&hit(r));const by={};g.forEach(r=>(by[r.tp]=by[r.tp]||[]).push(r));
const tier=t=>t.startsWith("adult")?1:(t.includes("(toss)")?2:0);
const order=Object.entries(by).sort((a,b)=>tier(a[0])-tier(b[0])||b[1].length-a[1].length);
h+=`<div class="jump">`+order.map(([t,rs],k)=>`<a href="#tp${k}" class="chip${tier(t)?" dim":""}">${esc(t)} ${rs.length}</a>`).join(" ")+`</div>`;
order.forEach(([t,rs],k)=>{rs.sort((a,b)=>b.sc-a.sc);h+=`<h2 id="tp${k}">${esc(t)} <span>${rs.length}</span></h2>`+table(rs)});
if(!g.length)h="<p class=more>No rows match.</p>"}
else if(tab=="dupes"){const ds=D.dupes.filter(d=>{const r=byId[d.id];return r&&hit(r)});h=`<h2>Saved more than once <span>${ds.length} pages</span></h2><table class="dg">`+ds.map(d=>{const r=byId[d.id];return row(r).replace("</td><td class=\"h\">",`<div class="copies">${d.copies.map(c=>esc(c.folder)+" · "+(c.added||"")).join("<br>")}</div></td><td class="h">`)}).join("")+"</table>"}
else if(tab=="dead"){const dd=D.rows.filter(r=>(r.s=="dead"||r.s=="gone")&&hit(r));const dt=D.rows.filter(r=>(r.s=="timeout"||r.s=="error")&&hit(r));
h=`<h2>Dead or gone <span>${dd.length}: safe tosses</span></h2>`+table(dd)+`<h2>Check by hand <span>${dt.length}: timed out or errored</span></h2>`+table(dt)}
else{const a=D.rows.filter(hit).sort((x,y)=>x.rk-y.rk);h=`<h2>Everything <span>${a.length}, best first</span></h2>`+table(a,q?2000:600)}
v.innerHTML=h}
document.querySelectorAll(".tab").forEach(b=>b.onclick=()=>{document.querySelectorAll(".tab").forEach(x=>x.classList.remove("on"));b.classList.add("on");tab=b.dataset.t;try{localStorage.setItem("bmdig.tab",tab)}catch(e){};render()});
let tm;document.getElementById("q").oninput=e=>{clearTimeout(tm);tm=setTimeout(()=>{q=e.target.value.trim().toLowerCase();render()},150)};
document.getElementById("view").onclick=e=>{const b=e.target.closest(".mk");if(!b)return;const id=b.closest("tr").dataset.id,m=b.dataset.m;if(M[id]==m)delete M[id];else M[id]=m;saveM();render()};
document.getElementById("hideToss").onclick=e=>{hideT=!hideT;e.target.textContent=hideT?"Show tossed":"Hide tossed";render()};
document.getElementById("exp").onclick=()=>{const blob=new Blob([JSON.stringify({exported:new Date().toISOString(),marks:M},null,1)],{type:"application/json"});const a=document.createElement("a");a.href=URL.createObjectURL(blob);a.download="bookmark_marks.json";a.click()};
const m=D.meta,s=m.status||{};document.getElementById("stats").textContent=`${m.total} bookmarks · ${m.unique} unique · ${m.dupe_copies} duplicate copies · ${s.live||0} live · ${(s.dead||0)+(s.gone||0)} dead · ${s.blocked||0} blocked · ${(s.timeout||0)+(s.error||0)} check by hand · ${s.unchecked||0} unchecked · ${m.pages_saved} saved offline`;
try{const t=(location.hash.match(/tab=(\w+)/)||[])[1]||localStorage.getItem("bmdig.tab");if(t){tab=t;document.querySelectorAll(".tab").forEach(x=>x.classList.toggle("on",x.dataset.t==t))}}catch(e){}
count();render();
</script></body></html>"""


# ---------------------------------------------------------------- main

def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("verb", choices=["scan", "check", "rank", "ingest", "build", "summary", "marks", "all"])
    ap.add_argument("arg", nargs="?", help="marks: the exported marks file")
    ap.add_argument("--json", action="store_true", help="print the result as JSON")
    ap.add_argument("--limit", type=int, help="check: only this many new URLs")
    ap.add_argument("--recheck", action="store_true", help="check: ignore the cache")
    ap.add_argument("--redo", help="check: recheck rows with these statuses (comma list)")
    ap.add_argument("--titles", type=int, help="rank: print the top N for hand tagging")
    ap.add_argument("--max", type=int, default=500, help="ingest: page cap (max 500)")
    ap.add_argument("--dry-run", action="store_true", help="ingest: say what would be fetched")
    a = ap.parse_args(argv)
    if a.verb == "scan":
        d = scan()
        res = {k: d[k] for k in ("total", "unique", "dupe_copies", "dupe_groups")}
        res["folders"], res["domains"] = len(d["by_folder"]), len(d["by_domain"])
    elif a.verb == "check":
        res = check(a.limit, a.recheck, redo=a.redo)
    elif a.verb == "rank":
        res = rank()
        if a.titles:
            if a.json:
                res["titles"] = titles(a.titles)
            else:
                print("\n".join(titles(a.titles)))
                return
    elif a.verb == "ingest":
        res = ingest(min(a.max, 500), a.dry_run)
    elif a.verb == "build":
        res = build()
    elif a.verb == "marks":
        if not a.arg:
            ap.error("marks needs the exported file")
        res = marks(Path(a.arg))
    elif a.verb == "all":
        scan(); res = {"check": check(), "rank": rank(), "build": build()}
    else:
        res = summary()
    out(res, a.json)


if __name__ == "__main__":
    main()
