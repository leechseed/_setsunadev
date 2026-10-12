"""Heritage rolls for The Outliers' cast (BOLO 100, call W1-B, ruled by Chief 10/12).

Chief, 10/12: "I like B, but for each character and family … I want to use the option B to mix them … to come up
with what the mix would look like."

Usage:
  python _tools/leechseed/heritage.py roll            # one character
  python _tools/leechseed/heritage.py roll --n 30     # a class of 30, with the class census
  python _tools/leechseed/heritage.py family          # two parents and the kids they'd have
  options: --seed N (repeatable rolls)

Zero tokens. Option B is the census: White 30 · Black 24 · Latino 18 · Asian 14 · Mixed 8 · MENA 4 · Indigenous 2.
B picks a character's group. A Mixed roll draws two or three parent groups from the other six, weighted by B, and
splits the percentages. Inside each group a Gulf-weighted roots table picks the family's origin (the Delta Coast is
a Gulf coast). Families: each parent rolls, the kids take half of each. The script judges nothing; the writer and
Chief keep or reroll. Feeds LEECHSEED L7 ORIGIN (heritage, family).
"""
import random, sys

CENSUS = [("White", 30), ("Black", 24), ("Latino", 18), ("Asian", 14), ("Mixed", 8), ("MENA", 4), ("Indigenous", 2)]
ROOTS = {
    "White": [("Cajun", 22), ("Irish", 16), ("German", 14), ("Italian", 12), ("Scots-Irish", 12), ("English", 10), ("Polish", 6), ("Greek", 4), ("Croatian", 4)],
    "Black": [("Gulf Creole", 26), ("Deep South African American", 34), ("Haitian", 10), ("Jamaican", 8), ("Nigerian", 8), ("Ghanaian", 5), ("Trinidadian", 5), ("Ethiopian", 4)],
    "Latino": [("Mexican", 34), ("Honduran", 16), ("Cuban", 14), ("Puerto Rican", 12), ("Salvadoran", 8), ("Guatemalan", 8), ("Colombian", 5), ("Dominican", 3)],
    "Asian": [("Vietnamese", 34), ("Filipino", 16), ("Chinese", 14), ("Indian", 14), ("Korean", 8), ("Laotian", 6), ("Japanese", 4), ("Pakistani", 4)],
    "MENA": [("Lebanese", 34), ("Syrian", 18), ("Egyptian", 16), ("Palestinian", 14), ("Iranian", 10), ("Moroccan", 8)],
    "Indigenous": [("Houma", 34), ("Choctaw", 24), ("Seminole", 16), ("Chitimacha", 14), ("Coushatta", 12)],
}


def pick(table, rng):
    total = sum(w for _, w in table)
    x = rng.uniform(0, total)
    for name, w in table:
        x -= w
        if x <= 0:
            return name
    return table[-1][0]


def roll(rng):
    """One character: a dict {group: share}, plus the roots behind each group."""
    group = pick(CENSUS, rng)
    if group != "Mixed":
        return {group: 100}, {group: pick(ROOTS[group], rng)}
    others = [g for g in CENSUS if g[0] != "Mixed"]
    parts = 3 if rng.random() < 0.3 else 2
    groups = []
    while len(groups) < parts:
        g = pick(others, rng)
        if g not in groups:
            groups.append(g)
    shares = [50, 50] if parts == 2 else [50, 25, 25]
    mix = dict(zip(groups, shares))
    return mix, {g: pick(ROOTS[g], rng) for g in groups}


def show(mix, roots):
    return " + ".join("%d%% %s (%s)" % (s, g, roots[g]) for g, s in sorted(mix.items(), key=lambda x: -x[1]))


def family(rng, kids=2):
    """Kid-first, so a class built from families still matches the B census: roll the kid on B, then give the
    parents the groups that make that kid. A one-group kid has two parents of that group (roots may differ, e.g.
    Cajun + Irish). A 50/50 kid has one parent per group. A 50/25/25 kid has one single-group parent and one
    50/50 parent."""
    child, roots = roll(rng)
    gs = sorted(child, key=lambda g: -child[g])
    if len(gs) == 1:
        g = gs[0]
        r2 = pick(ROOTS[g], rng)
        p1, p2 = ({g: 100}, {g: roots[g]}), ({g: 100}, {g: r2})
        kid_roots = roots[g] if r2 == roots[g] else "%s and %s" % (roots[g], r2)
        print("PARENT 1  " + show(*p1))
        print("PARENT 2  " + show(*p2))
        print("KIDS (%d) 100%% %s (%s)" % (kids, g, kid_roots))
        return
    if len(gs) == 2:
        p1, p2 = ({gs[0]: 100}, {gs[0]: roots[gs[0]]}), ({gs[1]: 100}, {gs[1]: roots[gs[1]]})
    else:
        p1 = ({gs[0]: 100}, {gs[0]: roots[gs[0]]})
        p2 = ({gs[1]: 50, gs[2]: 50}, {gs[1]: roots[gs[1]], gs[2]: roots[gs[2]]})
    print("PARENT 1  " + show(*p1))
    print("PARENT 2  " + show(*p2))
    print("KIDS (%d) " % kids + show(child, roots))


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    a = sys.argv[1:]
    rng = random.Random(int(a[a.index("--seed") + 1]) if "--seed" in a else None)
    if a and a[0] == "family":
        family(rng)
    else:
        n = int(a[a.index("--n") + 1]) if "--n" in a else 1
        census = {}
        for i in range(n):
            mix, roots = roll(rng)
            key = "Mixed" if len(mix) > 1 else next(iter(mix))
            census[key] = census.get(key, 0) + 1
            print("%2d  %s" % (i + 1, show(mix, roots)))
        if n > 1:
            print("CENSUS  " + " · ".join("%s %d" % (g, census.get(g, 0)) for g, _ in CENSUS))
