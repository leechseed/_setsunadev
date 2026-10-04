import json

with open("C:/Users/U01_LEECHSEED/Desktop/_setsunadev/_tools/bolostatus/work/100/untagged_extracted.json", 'r', encoding='utf-8') as f:
    distills = json.load(f)

results = []

for distill in distills:
    dist_id = distill['id']
    title = distill['title']
    title_lower = title.lower()
    thesis = distill['thesis'].lower()
    
    system = 'NONE'
    layer = None
    reason = ""
    
    # TRACKING: Story structure analysis
    if 'story grid' in title_lower:
        system = 'tracking'
        layer = '?'
        reason = 'Dramatica-based structural editing analysis'
    
    # THEME: Sexuality as literary force  
    elif 'bloom' in title_lower and 'sexuality' in title_lower:
        system = 'theme'
        layer = 'T?'
        reason = 'Eros as structural force in literature'
    
    # THEME/CHARACTER: Queer theory, desire, sexuality studies
    elif any(word in title_lower for word in ['unlimited intimacy', 'threesome', 'adhd after dark', 'fuckology', 'sex and leisure']):
        system = 'character'  # These construct identity through desire/sexuality
        layer = 'C?'
        reason = 'Queer subjectivity and erotic identity'
    
    # CHARACTER: Sex techniques and masculine identity manuals
    elif any(word in title_lower for word in ['models:', 'no more mr', 'the game:', 'rational male', 'way of the superior', 'art of seduction', 'book of pook', 'mystery method', '3% man', 'mode one']):
        system = 'NONE'
        layer = None
        reason = 'Masculine pickup/seduction technique manuals (operations)'
    
    # CHARACTER: Gay sexual culture and technique manuals
    elif any(word in title_lower for word in ['cock like a pro', 'faggot', 'bottoming', 'topping', 'shogun method', 'sexual ecstasy', 'phallicism']):
        system = 'character'
        layer = 'C?'
        reason = 'Sexual identity and erotic practice in gay male culture'
    
    # STYLE: Prose and writing craft
    elif any(word in title_lower for word in ['writing', 'clarity', 'rhetorics of fantasy', 'point of view', 'focalization', 'prose']):
        system = 'style'
        layer = '?'
        reason = 'Prose craft and narrative voice'
    
    # GENRE: Film/literary genre theory
    elif any(word in title_lower for word in ['genre', 'hollywood']):
        system = 'genre'
        layer = '?'
        reason = 'Genre conventions and film/literary taxonomy'
    
    # SETTING: Worldbuilding and campaign design
    elif any(word in title_lower for word in ['pathfinder', 'gamemaster', 'game master', 'campaign', 'setting', 'travel index']):
        system = 'setting'
        layer = 'S?'
        reason = 'Place and world construction'
    
    # NONE: Military doctrine, operations, business
    elif any(word in title_lower for word in ['mcdp', 'warfighting', 'strategy', 'tactics', 'logistics', 'planning', 'intelligence', 'command', 'learning', 'information', 'expeditionary', 'underground economy', 'docs for developers', 'microsoft manual', 'nasa systems', 'minto pyramid', 'minimalism', 'efficiency', 'make it stick', 'teach yourself']):
        system = 'NONE'
        layer = None
        reason = 'Operational/technical doctrine (not story method)'
    
    results.append({
        'id': dist_id,
        'title': title,
        'system': system,
        'layer': layer,
        'reason': reason
    })

# Count and summarize
counts = {}
for r in results:
    s = r['system']
    counts[s] = counts.get(s, 0) + 1

results.sort(key=lambda x: x['id'])

# Generate markdown
lines = []
lines.append("# LIBRARY-UNTAGGED Distill Assignments")
lines.append("")
lines.append(f"**Summary:** {sum(1 for r in results if r['system'] != 'NONE')} distills to story systems · {counts.get('NONE', 0)} NONE")
lines.append("")
lines.append("## Counts")
for s in sorted(counts.keys()):
    if s != 'NONE':
        lines.append(f"- **{s}**: {counts[s]}")
lines.append(f"- **NONE**: {counts.get('NONE', 0)}")
lines.append("")
lines.append("## Assignments")
lines.append("")
lines.append("| id | title | system | layer | reason |")
lines.append("|---|---|---|---|---|")
for r in results:
    t = r['title'][:48].replace('|', '·')
    reason = r['reason'][:50].replace('|', '·')
    layer = r['layer'] if r['layer'] else '—'
    lines.append(f"| {r['id']} | {t} | {r['system']} | {layer} | {reason} |")

with open("C:/Users/U01_LEECHSEED/Desktop/_setsunadev/_tools/bolostatus/work/100/LIBRARY-UNTAGGED.md", 'w', encoding='utf-8') as f:
    f.write('\n'.join(lines))

print("Updated counts:")
for s in sorted(counts.keys()):
    print(f"  {s}: {counts[s]}")
print()
print(f"Total: {len(results)}")
