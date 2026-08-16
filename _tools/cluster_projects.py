"""Cluster conversations into projects. Title-weighted scoring, best match wins."""
import os, re, collections

ARC = r"c:\Users\U01_LEECHSEED\Desktop\_setsunadev\_CLAUDE_ARCHIVE_2026-08-15"
CONV = os.path.join(ARC, "conversations")

P = [
("OXO","BLACK","OVEREXITOUT / The Outliers — narrative IP",
 r"overexitout|\boxo\b|outlier|outsiders system|victoria midnight|tori midnight|"
 r"quinn bishop|riley moss|colson|red hills|inner spiral|student diaspora|"
 r"six movements|series bible|jebb|delta coast|astro7ex|lakad|worldbuild|"
 r"main sonnet|logline|screenplay|scene|narrative"),
("CHARSYS","BLACK","Character system — Dramatica × astrology × 12-layer",
 r"dramatica|storyform|throughline|12-?layer|twelve layer|character database|"
 r"vertical slice|narrative astrology|character astrology|character system|"
 r"astrolog|enneagram|character taxonomy|desires taxonomy"),
("BVXSYS","BLACK","BVIPDS / LEECHSEED — system architecture & SSOT",
 r"bvipds|leechseed|\bssot\b|bold venture|\bbvx\b|system explorer|profiler ui|"
 r"knowledge base|markdown knowledge|research catalog|system architecture|"
 r"epistemolog|clickup|repo structure|system design mapping|ui research|"
 r"knowledge management|obsidian|one-sheet|quartermaster"),
("ADULT","ORANGE","Adult content venture — brand, model, monetisation",
 r"adult (content|venture|industry|awards)|solo adult|content creator business|"
 r"onlyfans|vtuber|toy review|sex toy|affiliate|dildo|\bbbc\b|bulk filming|"
 r"lewd|camming|fansly|premium sex|m4mm|production set|gooning|"
 r"sex work|escort|porn"),
("DESIRE","ORANGE","Desire Profile — sexuality research & profiling",
 r"desire profile|sex menu|relationship needs|erotic blueprint|"
 r"dominance and submission|\bd/s\b|daddy dom|little sub|\bkink\b|somatic|"
 r"mating in captivity|body archetype|whole-body sex|threesome|intimacy|"
 r"chastity|anal play|arousal|seduction|female body archetypes|"
 r"sexual|eroti|perel|libido"),
("FITNESS","ORANGE","ULTRASIN / GDP — physique, gym build, training",
 r"ultrasin|nightyard|bootycamp|cavalry|glute|booty|weightlifting|"
 r"one rep max|power cage|squat|physique|training routine|gym|"
 r"activation routine|soreness|rep max|lifting|muscle"),
("SOCIAL","BOTH","Social channels — TikTok / YouTube growth",
 r"tiktok|youtube|listicle|faceless|monetization|monetisation|subscriber|"
 r"submagic|forza|gaming channel|shorts|thumbnail|viral|"
 r"channel|follower|content calendar"),
("FOOD","BLACK","Food ventures — bakery, takeout, eating show",
 r"food business|bakery|mary'?s french|takeout|chinese|eating content|"
 r"culinary|menu|[EMPLOYER]|restaurant|recipe|poultry|egg|kitchen|"
 r"food concept|food truck"),
("SELF","BOTH","Self-management — regulation, relationships, admin",
 r"overstimulation|self-regulation|trauma|emotionally draining|harassment|"
 r"disengaging|self-sabotage|win friends|speak her language|boundaries|"
 r"rapport|teasing|brain fog|medical card|therapy"),
("TOOLING","BLACK","Tooling — scripts, scrapers, UI builds",
 r"yt-dlp|ytdlp|clipboard|scraper|python script|react app|\bjsx\b|"
 r"debugging|regedit|vscode|automation|background removal|"
 r"file renaming|download error|power plan|3d print"),
("BIZOPS","BLACK","Business ops — PM, charters, market entry",
 r"pmbok|project charter|vargas|market entry|reselling|"
 r"content rights|business model|subventure|bill of materials|"
 r"procurement|one sheet summaries|\bpbx\b"),
("GEAR","BOTH","Gear, vehicles & personal logistics",
 r"truck|tundra|key fob|motorcycle|jansport|backpack|air filtration|"
 r"shower|hotel|desk cable|firearm|\bgun\b|glove|holster|cs2|"
 r"purchase list|3d printer"),
]
C = [(k, t, l, re.compile(p, re.I)) for k, t, l, p in P]
LAB = {k: (t, l) for k, t, l, _ in C}

agg = collections.defaultdict(lambda: {"n":0,"chars":0,"msgs":0,"arts":0,
                                       "dates":[],"titles":[]})
unassigned = []
for fn in sorted(os.listdir(CONV)):
    txt = open(os.path.join(CONV, fn), encoding="utf-8").read()
    cut = txt.find("\n---", 3)
    fm, body = txt[:cut], txt[cut:cut+9000]
    def g(k, d=""):
        m = re.search(rf"^{k}: (.*)$", fm, re.M)
        return m.group(1) if m else d
    title = g("title").strip('"')
    chars = int(g("chars","0") or 0); msgs = int(g("messages","0") or 0)
    arts = int(g("artifacts","0") or 0); created = g("created")

    best, bestscore = None, 0
    for k, t, l, rx in C:
        ts = len(rx.findall(title)) * 12
        bs = min(len(rx.findall(body)), 8)
        s = ts + bs
        if s > bestscore:
            best, bestscore = k, s
    if best and bestscore >= 3:
        a = agg[best]
        a["n"] += 1; a["chars"] += chars; a["msgs"] += msgs; a["arts"] += arts
        a["dates"].append(created); a["titles"].append((chars, title))
    else:
        unassigned.append((chars, title, created))

rows = sorted(agg.items(), key=lambda kv: -kv[1]["chars"])
total = sum(v["chars"] for v in agg.values()) + sum(c for c,_,_ in unassigned)

print(f"{'#':<3}{'PROJECT':<48}{'TRUNK':<8}{'CONV':>5}{'MSGS':>6}{'VOLUME':>9}{'SHARE':>7}  SPAN")
print("-"*108)
for i,(k,v) in enumerate(rows,1):
    t,l = LAB[k]; d = sorted(v["dates"])
    span = f"{d[0][2:7]}→{d[-1][2:7]}" if d else ""
    print(f"{i:<3}{l[:46]:<48}{t:<8}{v['n']:>5}{v['msgs']:>6}{v['chars']//1000:>8}k{100*v['chars']//total:>6}%  {span}")
print("-"*108)
print(f"{'':3}{'(unassigned / one-offs)':<48}{'':8}{len(unassigned):>5}{'':6}"
      f"{sum(c for c,_,_ in unassigned)//1000:>8}k{100*sum(c for c,_,_ in unassigned)//total:>6}%")
print(f"\nTOTAL {total//1000:,}k chars · 319 conversations\n")

for k,v in rows[:10]:
    t,l = LAB[k]
    d = sorted(v["dates"])
    print(f"\n### {l}  [{t}]")
    print(f"    {v['chars']//1000}k · {v['n']} convs · {v['msgs']} msgs · {v['arts']} artifacts · {d[0]}→{d[-1]}")
    for c,ti in sorted(v["titles"], reverse=True)[:7]:
        print(f"      {c//1000:>4}k  {ti[:70]}")
