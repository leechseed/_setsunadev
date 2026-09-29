#!/usr/bin/env python3
"""BOLO 93 · the world view compiler, first build ("Thin", ruled 9/29).

Reads the catalog files (09) and the 03 place headers, runs the script tests
CT1 · CT3 · CT5 · CT9, and writes two things. It edits nothing it reads.

  ShroomsQ/_CANON/_SSOT/09_WORLDBUILDING_SYSTEMS/catalog/_INDEX.md   (generated, never hand-edited)
  _tools/worldview/out/worldview.html                              (page content, publish as-is)

Later builds add the 02 · 04 · 08 reads (09 OPEN 6).
"""
import html, json, pathlib, re, sys, datetime

R = pathlib.Path(__file__).resolve().parents[2]
SYS = R / 'ShroomsQ/_CANON/_SSOT/09_WORLDBUILDING_SYSTEMS'
CAT = SYS / 'catalog'
SETTING = R / 'ShroomsQ/_CANON/_SSOT/03_SETTING_SYSTEMS/📐 ssot_03_setting_system.md'
OUT = pathlib.Path(__file__).resolve().parent / 'out'
REPO = 'https://github.com/leechseed/_setsunadev/blob/main/'

# ruled 9/29 (call 4 "Eight"): the open types; the other four wait for a story
TYPES = {
    'GRP': ('Groups', 'A body of people with a shared identity, rule and edge: clan, class, faction, nation, species. The faction card stays in 03; the entry links to it.'),
    'ARC': ('Architecture', 'A reusable way of building, with its materials and what it says about its makers. One building\'s fabric stays in 03 S1 BODY.'),
    'WDR': ('Wardrobe', 'How a group dresses and adorns itself, keyed to class and role. One person\'s outfit stays in 02.'),
    'CUS': ('Customs', 'A patterned group practice: ritual, festival, taboo, rite of passage, etiquette. A place\'s habit stays in 03 S8 HABIT.'),
    'TEC': ('Tech & vehicles', 'A working technique or device, including how people move and carry things. Vehicles live here.'),
    'INS': ('Institutions', 'A standing body or form of authority: a court, a school board, a guild, a standards body.'),
    'BEL': ('Beliefs', 'A religion, folk belief, cult, myth or philosophy, including the hidden layer under the public one.'),
    'FSU': ('Food & substances', 'What people eat, drink and take, and the system that supplies it.'),
}
WAITING = {'ECO': 'Goods, money and trade', 'LNG': 'Language and naming', 'BIO': 'Creatures and flora', 'RUL': 'World rules'}

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


def tests(entries, pl):
    by = lambda *ts: [e for e in entries if e.get('type') in ts]
    stub = lambda e: str(e.get('status', '')).startswith('stub')
    res = []
    pillars = {'governance': by('INS'), 'economics': by('FSU', 'ECO'), 'social relations': by('GRP'), 'cultural influences': by('CUS', 'BEL', 'WDR')}
    miss = [k for k, v in pillars.items() if not v]
    res.append(('CT1', 'Four pillars', 'The world has at least a stub for governance, economics, social relations and cultural influences.',
                'fail' if miss else 'pass', ('missing: ' + ', '.join(miss)) if miss else ' · '.join(f'{k} {len(v)}' for k, v in pillars.items()), 'BVX.0067'))
    ins = by('INS')
    no_origin = [e['id'] for e in ins if not e.get('origin')]
    s = 'stub' if no_origin and all(stub(e) for e in ins if e['id'] in no_origin) else ('fail' if no_origin else 'pass')
    res.append(('CT3', 'The gap-fill', 'Every institution names the rupture or need it fills, as a fabula event or an S5 SCAR.', s,
                f'{len(ins) - len(no_origin)} of {len(ins)} institutions name an origin', 'BVX.0575'))
    ends = by('GRP')
    no_end = [e['id'] for e in ends if len(e.get('era') or []) < 1]
    s = 'stub' if no_end and all(stub(e) for e in ends if e['id'] in no_end) else ('fail' if no_end else 'pass')
    res.append(('CT5', 'Bookends', 'Each group has a founding endpoint and a current endpoint; a founding line counts only if it still bites now.', s,
                f'{len(ends) - len(no_end)} of {len(ends)} groups carry eras', 'BVX.0465'))
    canon = [e for e in entries if e.get('status') == 'canon']
    unnarrated = [e['id'] for e in canon if not (e.get('fields') or {}).get('scene')]
    res.append(('CT9', 'Onstage canon', 'A fact enters canon only when a scene narrates it.', 'fail' if unnarrated else 'pass',
                f'{len(canon)} canon entries · {len(unnarrated)} without a scene' if canon else 'no canon entries yet', 'BVX.0538'))
    bad_place = sorted({p for e in entries for p in (e.get('places') or []) if p not in pl})
    if bad_place:
        res.append(('LINK', 'Place links', 'Every place an entry names exists as a 03 slice header.', 'fail', 'unknown: ' + ', '.join(bad_place), '03'))
    return res


def main():
    entries = sorted((frontmatter(p) for p in CAT.glob('*/*.md')), key=lambda e: e.get('id', ''))
    pl = places()
    ct = tests(entries, pl)
    counts = {t: sum(1 for e in entries if e.get('type') == t) for t in TYPES}
    gaps = []
    for code, name, holds, owners in INFRA:
        n = sum(counts.get(o, 0) for o in owners if o in TYPES)
        other = [o for o in owners if o in ('03', '04')]
        gaps.append({'code': code, 'name': name, 'holds': holds, 'owners': owners, 'n': n, 'other': other,
                     'state': 'owned' if other else ('gap' if n == 0 else 'held'),
                     'waiting': [o for o in owners if o in WAITING]})
    names = {e['id']: e.get('name', e['id']) for e in entries}
    today = datetime.date.today().isoformat()

    # ---- the generated index ----
    md = [f'# The catalog · generated {today}', '', 'Generated by `_tools/worldview/build.py`. Never hand-edit; edit the entry file.', '',
          '| id | type | name | places | status |', '|---|---|---|---|---|']
    for e in entries:
        rel = pathlib.PurePosixPath(e['_path']).relative_to('ShroomsQ/_CANON/_SSOT/09_WORLDBUILDING_SYSTEMS/catalog')
        md.append(f"| [{e['id']}]({rel}) | {e.get('type')} | {e.get('name')} | {', '.join(e.get('places') or []) or '—'} | {e.get('status')} |")
    (CAT / '_INDEX.md').write_text('\n'.join(md) + '\n', encoding='utf-8')

    data = {'entries': [{k: v for k, v in e.items()} for e in entries], 'places': pl, 'tests': ct, 'gaps': gaps,
            'types': TYPES, 'waiting': WAITING, 'names': names, 'repo': REPO, 'built': today}
    page = TEMPLATE.replace('/*DATA*/null', json.dumps(data, ensure_ascii=False))
    OUT.mkdir(exist_ok=True)
    (OUT / 'worldview.html').write_text(page, encoding='utf-8')
    print(f'world view · {len(entries)} entries · {len(pl)} places · tests: ' + ' '.join(f'{c[0]} {c[3]}' for c in ct))
    print(f'wrote {OUT / "worldview.html"} ({len(page) // 1024} KB) · {CAT / "_INDEX.md"}')


TEMPLATE = (pathlib.Path(__file__).resolve().parent / 'template.html').read_text(encoding='utf-8')

if __name__ == '__main__':
    main()
