import json, urllib.request, time
subs=["OnlyFansAdvice","CreatorsAdvice","OnlyFans101","SexWorkersOnly","sexworkers","SluttyConfessions","TwoXSex","sex","relationship_advice","dating_advice","AskAstrologers","astrology","Situationships","BDSMAdvice","polyamory","AskWomenOver30","sexover30","FemaleDatingStrategy","Vent_Sexually","RedditForGrownups"]
out={}
for s in subs:
    u=f"https://api.pullpush.io/reddit/search/submission/?subreddit={s}&size=100&sort=desc"
    try:
        d=json.load(urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'research/0.1'}),timeout=30))['data']
        qs=[x for x in d if x.get('title','').strip().endswith('?') or '?' in (x.get('selftext') or '')[:400]]
        last=time.strftime('%Y-%m',time.gmtime(max(x['created_utc'] for x in d))) if d else '-'
        out[s]=d
        print(f"{s:22} posts {len(d):3}  questions {len(qs):3}  last {last}")
    except Exception as e:
        print(f"{s:22} ERR {e}")
    time.sleep(1.2)
json.dump(out,open('_tools/advice/pull.json','w',encoding='utf-8'),ensure_ascii=False)
