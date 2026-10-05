#!/usr/bin/env python3
"""BOLO 93 · the world view compiler, second build (09 to 1.0, ruled 9/29).

Reads the catalog files (09), the 03 place headers, the 02 character nodes,
the 04 fabula events, the 08 tracking files and the trope register; runs every
script-checkable coherence test (CT1 · CT3 · CT4 · CT5 · CT6 · CT9 · CT13) and
four link checks; writes two things. It edits nothing it reads.

  ShroomsQ/_CANON/_SSOT/05_WORLDBUILDING_SYSTEMS/catalog/_INDEX.md   (generated, never hand-edited)
  _tools/worldview/out/worldview.html                              (page content, publish as-is)

The reader tests (R) are judged by a PS and folded in from `reader_tests.json`.
"""
import json, pathlib, re, datetime

import yaml

R = pathlib.Path(__file__).resolve().parents[2]
SYS = R / 'ShroomsQ/_CANON/_SSOT/05_WORLDBUILDING_SYSTEMS'
CAT = SYS / 'catalog'
SETTING = R / 'ShroomsQ/_CANON/_SSOT/03_SETTING_SYSTEMS/📐 ssot_03_setting_system.md'
FABULA = R / 'ShroomsQ/_CANON/_SSOT/04_PLOT_SYSTEMS/📐 ssot_04_fabula.md'
TRACKING = R / 'ShroomsQ/_CANON/_TRACKING'
NODES = R / '_CANON_NODES'
REGISTER = R / '_tools/tropes/data/domains/register.json'
HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / 'out'
READER = HERE / 'reader_tests.json'
REPO = 'https://github.com/leechseed/_setsunadev/blob/main/'
ERAS = ['backstory', 'M1', 'M2', 'M3', 'M4', 'M5', 'M6']
SCALES = {'world-economy', 'nation-state', 'locality'}

# ruled 9/29 (call 4 "Eight"; BIO opened 9/29 for the Kudzu): the open types; the rest wait for a story
TYPES = {
    'GRP': ('Groups', 'A body of people with a shared identity, rule and edge: clan, class, faction, nation, species. The faction card stays in 03; the entry links to it.'),
    'ARC': ('Architecture', 'A reusable way of building, with its materials and what it says about its makers. One building\'s fabric stays in 03 S1 BODY.'),
    'WDR': ('Wardrobe', 'How a group dresses and adorns itself, keyed to class and role. One person\'s outfit stays in 02.'),
    'CUS': ('Customs', 'A patterned group practice: ritual, festival, taboo, rite of passage, etiquette. A place\'s habit stays in 03 S8 HABIT.'),
    'TEC': ('Tech & vehicles', 'A working technique or device, including how people move and carry things. Vehicles live here.'),
    'INS': ('Institutions', 'A standing body or form of authority: a court, a school board, a guild, a standards body.'),
    'BEL': ('Beliefs', 'A religion, folk belief, cult, myth or philosophy, including the hidden layer under the public one.'),
    'FSU': ('Food & substances', 'What people eat, drink and take, and the system that supplies it.'),
    'BIO': ('Creatures', 'A kind of animal, plant or non-human being, with where it fits in the food web. Opened 9/29 for the Kudzu.'),
}
WAITING = {'ECO': 'Goods, money and trade', 'LNG': 'Language and naming', 'RUL': 'World rules'}

INFRA = [  # I1–I10 → which catalog types (or other systems) answer for it
    ('I1', 'Space', 'Geography, climate, terrain, borders, settlements.', ['03']),
    ('I2', 'Time', 'History, founding, ruins, genealogy, events.', ['04']),
    ('I3', 'Peoples and groups', 'Clans, classes, factions, species.', ['GRP']),
    ('I4', 'Governance and law', 'Who rules, by what right, how enforced.', ['INS']),
    ('I5', 'Economy and material life', 'Trade, goods, money, food, work.', ['FSU', 'ECO']),
    ('I6', 'Belief, myth and thought', 'Religion, cosmology, philosophy, values.', ['BEL']),
    ('I7', 'Custom and belonging', 'Rites, festivals, taboos, dress, daily habit.', ['CUS', 'WDR']),
    ('I8', 'Knowledge, craft and tech', 'Science, tools, transport, language, arts.', ['TEC', 'LNG']),
    ('I9', 'Nature', 'Flora, fauna, ecosystem, non-human beings.', ['BIO']),
    ('I10', 'World rules', 'Magic, physics, causality: how the world departs from ours.', ['RUL']),
]


def frontmatter(p):
    t = p.read_text(encoding='utf-8')
    m = re.match(r'^---\n(.*?)\n---\n', t, re.S)
    d = {}
    for line in (m.group(1).splitlines() if m else []):
        k, _, v = line.partition(':')
        v = v.strip()
        try:
            d[k.strip()] = json.loads(v) if v[:1] in '["{' else v
        except json.JSONDecodeError:
            d[k.strip()] = v.strip('"')
    d['_path'] = p.relative_to(R).as_posix()
    return d


def places():
    t = SETTING.read_text(encoding='utf-8')
    out = {}
    for m in re.finditer(r'\*\*Header:\*\* `([a-z0-9_]+)` · names: (.*?) · scale: \*\*(.*?)\*\*', t):
        names = re.sub(r'[*_]', '', m.group(2)).split(' / ')
        out[m.group(1)] = {'id': m.group(1), 'name': names[0].strip(), 'aliases': [n.strip(' "') for n in names[1:]], 'scale': m.group(3)}
    return out


def characters():
    out = {}
    for p in NODES.glob('*.md'):
        m = re.match(r'^---\n(.*?)\n---', p.read_text(encoding='utf-8'), re.S)
        if not m or not re.search(r'^kind:\s*character', m.group(1), re.M):
            continue
        cid = re.search(r'^entity_id:\s*(\S+)', m.group(1), re.M)
        name = re.search(r'^entity:\s*(.+)$', m.group(1), re.M)
        if cid:
            out[cid.group(1)] = {'id': cid.group(1), 'name': name.group(1).strip().strip('"') if name else cid.group(1),
                                 'path': p.relative_to(R).as_posix()}
    return out


def events():
    out = {}
    for m in re.finditer(r'^event_id:\s*"([^"<]+)"\s*\ntransition:\s*"([^"]*)"', FABULA.read_text(encoding='utf-8'), re.M):
        out[m.group(1)] = {'id': m.group(1), 'label': m.group(2), 'src': '04 fabula'}
    for f in TRACKING.glob('*.yaml'):
        d = yaml.safe_load(f.read_text(encoding='utf-8'))
        for w in d.get('world') or []:
            out.setdefault(w['id'], {'id': w['id'], 'label': w.get('label', ''), 'src': f'08 {f.stem} world'})
    return out


def tracked():
    pts = {}
    for f in TRACKING.glob('*.yaml'):
        d = yaml.safe_load(f.read_text(encoding='utf-8'))
        for sp in d.get('story_points') or []:
            pts.setdefault(sp.get('subject'), []).append({'story': f.stem, 'at': sp.get('at'), 'field': sp.get('field'), 'value': sp.get('value')})
    return pts


def tests(entries, pl, ev, ch, tropes):
    by = lambda *ts: [e for e in entries if e.get('type') in ts]
    stub = lambda e: str(e.get('status', '')).startswith('stub')
    fl = lambda e: e.get('fields') if isinstance(e.get('fields'), dict) else {}
    ids = {e['id'] for e in entries}
    byid = {e['id']: e for e in entries}
    res = []

    def verdict(pool, bad):  # only a filled entry can fail; a stub is "not yet checkable"
        live_bad = [e['id'] for e in pool if e['id'] in bad and not stub(e)]
        return 'fail' if live_bad else ('stub' if bad else 'pass')

    def tail(bad, s):
        live_bad = [b for b in bad if not stub(byid[b])]
        return (' · open: ' + ', '.join(live_bad)) if live_bad and s == 'fail' else ''

    pillars = {'governance': by('INS'), 'economics': by('FSU', 'ECO'), 'social relations': by('GRP'), 'cultural influences': by('CUS', 'BEL', 'WDR')}
    miss = [k for k, v in pillars.items() if not v]
    res.append(('CT1', 'Four pillars', 'The world has at least a stub for governance, economics, social relations and cultural influences.',
                'fail' if miss else 'pass', ('missing: ' + ', '.join(miss)) if miss else ' · '.join(f'{k} {len(v)}' for k, v in pillars.items()), 'BVX.0067'))

    def origin_ok(e):
        o = e.get('origin') or ''
        return o in ev or (o.startswith('S5:') and o[3:] in pl)
    ins = by('INS')
    bad = [e['id'] for e in ins if not origin_ok(e)]
    s = verdict(ins, bad)
    res.append(('CT3', 'The gap-fill', 'Every institution names the rupture or need it fills, as a fabula event or an S5 SCAR.', s,
                f'{len(ins) - len(bad)} of {len(ins)} institutions name a real origin' + tail(bad, s), 'BVX.0575'))

    ruins = [e for e in entries if 'ruin' in str(fl(e).get('kind', ''))]
    bad = [e['id'] for e in ruins if not (origin_ok(e) and fl(e).get('builder'))]
    res.append(('CT4', 'Apocalypso', 'Every ruin has a dated fall on the timeline and a builder.', 'fail' if bad else 'pass',
                f'{len(ruins)} ruin entries' if ruins else 'no ruin entries yet', 'BVX.0458'))

    ends = by('GRP', 'INS', 'BEL')
    def ends_ok(e):
        er = e.get('era') or []
        return len(er) == 2 and all(x in ERAS for x in er) and ERAS.index(er[0]) <= ERAS.index(er[1])
    bad = [e['id'] for e in ends if not ends_ok(e)]
    s = verdict(ends, bad)
    res.append(('CT5', 'Bookends', 'Each group, institution and belief has a founding endpoint and a current endpoint, in order.', s,
                f'{len(ends) - len(bad)} of {len(ends)} carry two ordered eras' + tail(bad, s), 'BVX.0465'))

    gov = [e for e in entries if e.get('type') == 'INS' or 'coercion' in fl(e)]
    bad = [e['id'] for e in gov if not all(fl(e).get(k) for k in ('coercion', 'rule_making', 'consent'))]
    s = verdict(gov, bad)
    res.append(('CT6', 'Legitimacy', 'Every governing entry states coercion, rule-making and consent, or says which is missing.', s,
                f'{len(gov) - len(bad)} of {len(gov)} governing entries state all three' + tail(bad, s), 'BVX.1162'))

    canon = [e for e in entries if e.get('status') == 'canon']
    bad = [e['id'] for e in canon if not (NODES / f"{fl(e).get('scene', '-')}.md").exists()]
    res.append(('CT9', 'Onstage canon', 'A fact enters canon only when a scene narrates it.', 'fail' if bad else 'pass',
                f'{len(canon)} canon entries · {len(bad)} without a real scene card' if canon else 'no entry claims canon yet; filled entries wait for a scene', 'BVX.0538'))

    live = [e for e in entries if not stub(e)]
    bad = [e['id'] for e in live if fl(e).get('scale') not in SCALES]
    res.append(('CT13', 'Scale source', 'Every pressure names the rung it starts at: world-economy, nation-state or locality.',
                'fail' if bad else ('pass' if live else 'stub'), f'{len(live) - len(bad)} of {len(live)} filled entries name a rung' + (' · open: ' + ', '.join(bad) if bad else ''), 'BVX.1161'))

    links = [
        ('L03', 'Place links', 'Every place an entry names exists as a 03 slice header.', sorted({p for e in entries for p in (e.get('places') or []) if p not in pl})),
        ('L02', 'People links', 'Every character an entry names exists as a 02 node.', sorted({g for e in entries for g in (e.get('groups') or []) if g.startswith('character:') and g[10:] not in ch})),
        ('L09', 'Group links', 'Every group an entry names exists in the catalog.', sorted({g for e in entries for g in (e.get('groups') or []) if g.startswith('WB-') and g not in ids})),
        ('L04', 'Origin links', 'Every origin is a real fabula or world event, or an S5 scar.', sorted({e['id'] for e in entries if e.get('origin') and not origin_ok(e)})),
        ('LTR', 'Trope links', 'Every trope slug exists in the register.', sorted({t for e in entries for t in (e.get('tropes') or []) if t not in tropes})),
    ]
    for code, name, rule, badl in links:
        # a person with no 02 node is a gap 02 owes, not a 09 failure
        s = ('owed' if code == 'L02' else 'fail') if badl else 'pass'
        res.append((code, name, rule, s, (('no 02 node yet: ' if code == 'L02' else 'unknown: ') + ', '.join(badl)) if badl else 'all resolve', 'link'))
    return res


def main():
    every = sorted((frontmatter(p) for p in CAT.glob('*/*.md')), key=lambda e: e.get('id', ''))
    entries = [e for e in every if not str(e.get('status', '')).startswith('retired')]  # ids never reuse; retired files stay
    pl, ev, ch, pts = places(), events(), characters(), tracked()
    tropes = set(json.loads(REGISTER.read_text(encoding='utf-8')))
    ct = tests(entries, pl, ev, ch, tropes)
    rt = json.loads(READER.read_text(encoding='utf-8')) if READER.exists() else []
    for e in entries:
        e['_state'] = pts.get(e.get('state'), [])
        e['_origin'] = ev.get(e.get('origin') or '')
    for p in pl.values():
        p['_state'] = len(pts.get('place:' + p['id'], []))
    counts = {t: sum(1 for e in entries if e.get('type') == t) for t in TYPES}
    gaps = []
    for code, name, holds, owners in INFRA:
        n = sum(counts.get(o, 0) for o in owners if o in TYPES)
        other = [o for o in owners if o in ('03', '04')]
        gaps.append({'code': code, 'name': name, 'holds': holds, 'owners': owners, 'n': n, 'other': other,
                     'state': 'owned' if other else ('gap' if n == 0 else 'held')})
    names = {e['id']: e.get('name', e['id']) for e in entries}
    names.update({'character:' + c['id']: c['name'] for c in ch.values()})
    today = datetime.date.today().isoformat()

    # ---- the generated index ----
    md = [f'# The catalog · generated {today}', '', 'Generated by `_tools/worldview/build.py`. Never hand-edit; edit the entry file.', '',
          '| id | type | name | era | places | status |', '|---|---|---|---|---|---|']
    for e in entries:
        rel = pathlib.PurePosixPath(e['_path']).relative_to('ShroomsQ/_CANON/_SSOT/05_WORLDBUILDING_SYSTEMS/catalog')
        era = ' → '.join(e.get('era') or []) or '—'
        md.append(f"| [{e['id']}]({rel}) | {e.get('type')} | {e.get('name')} | {era} | {', '.join(e.get('places') or []) or '—'} | {e.get('status')} |")
    (CAT / '_INDEX.md').write_text('\n'.join(md) + '\n', encoding='utf-8')

    data = {'entries': entries, 'places': pl, 'tests': ct, 'reader': rt, 'gaps': gaps, 'types': TYPES, 'waiting': WAITING,
            'names': names, 'chars': ch, 'events': ev, 'eras': ERAS, 'repo': REPO, 'built': today}
    page = (HERE / 'template.html').read_text(encoding='utf-8').replace('/*DATA*/null', json.dumps(data, ensure_ascii=False))
    OUT.mkdir(exist_ok=True)
    (OUT / 'worldview.html').write_text(page, encoding='utf-8')
    print(f'world view · {len(entries)} entries · {len(pl)} places · {len(ch)} people · {len(ev)} events · reader tests {len(rt)}')
    print('tests: ' + ' · '.join(f'{c[0]} {c[3]}' for c in ct))
    for c in ct:
        if c[3] == 'fail':
            print(f'  FAIL {c[0]}: {c[4]}')
    print(f'wrote {OUT / "worldview.html"} ({len(page) // 1024} KB) · {CAT / "_INDEX.md"}')


if __name__ == '__main__':
    main()
