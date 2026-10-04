"""Pull recent question posts from women-facing advice subs (BOLO 99).
Reddit 403s this box; PullPush was down 10/4, so this reads the Arctic Shift archive.
Writes _PRIVATE/advice/pull.json (title + body + sub + score only; no usernames kept)."""
import json, urllib.request, time
SUBS = ["OnlyFansAdvice","CreatorsAdvice","OnlyFans101","SexWorkersOnly","sexworkers","SluttyConfessions","TwoXSex","sex",
        "relationship_advice","dating_advice","AskAstrologers","astrology","Situationships","BDSMAdvice","polyamory",
        "AskWomenOver30","sexover30","FemaleDatingStrategy","Vent_Sexually","RedditForGrownups"]
out = {}
for s in SUBS:
    u = f"https://arctic-shift.photon-reddit.com/api/posts/search?subreddit={s}&limit=100&sort=desc"
    try:
        d = json.load(urllib.request.urlopen(urllib.request.Request(u, headers={"User-Agent": "research/0.1"}), timeout=60))["data"]
        keep = [{"t": x.get("title", ""), "b": (x.get("selftext") or "")[:1500], "score": x.get("score", 0),
                 "when": time.strftime("%Y-%m-%d", time.gmtime(x["created_utc"]))}
                for x in d if x.get("selftext") not in ("[removed]", "[deleted]")]
        qs = [k for k in keep if "?" in k["t"] or "?" in k["b"][:500]]
        out[s] = qs
        print(f"{s:22} posts {len(d):3}  questions {len(qs):3}  newest {keep[0]['when'] if keep else '-'}")
    except Exception as e:
        print(f"{s:22} ERR {e}")
    time.sleep(1)
json.dump(out, open("_PRIVATE/advice/pull.json", "w", encoding="utf-8"), ensure_ascii=False)
