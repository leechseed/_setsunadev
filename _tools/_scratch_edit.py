import os, shutil
def edit(p, f):
    s = open(p, encoding='utf8', newline='').read()
    n = f(s)
    assert n != s, p
    open(p, 'w', encoding='utf8', newline='').write(n)

def nl(s):
    return '\r\n' if '\r\n' in s else '\n'

edit('_tools/loci/collect.py', lambda s: s.replace('Every fetched URL appears at least once."', 'Every fetched URL appears at least once. Outline first (the domains, then the rows). Cite each claim. Keep one source per paragraph or row."', 1))

def bs(s):
    n = nl(s)
    s = s.replace('- **Go recommended (10/12):**', '- **Underspecified ask (10/13):** when the ask is underspecified, one question, then proceed on the obvious default.' + n + '- **Go recommended (10/12):**', 1)
    return s.replace('auto-trigger and commit steps cut -->', 'auto-trigger and commit steps cut; underspecified-ask rule from trailofbits/skills ask-questions-if-underspecified (license unconfirmed, idea only, body not retrieved) -->', 1)
edit('.claude/skills/brainstorm/SKILL.md', bs)

def pt(s):
    n = nl(s)
    add = ('- **So what:** a claim with no consequence for the reader. Fix: add what it means for them, or cut.' + n +
           '- **Vague noun:** "solution", "insights", "streamline" where a concrete thing exists. Fix: name the thing.' + n +
           '- **Loose pronoun:** "it", "this" or "they" with two possible referents. Fix: repeat the noun.' + n)
    i = s.index('- **Wrong reader:**')
    j = s.index(n, i) + len(n)
    s = s[:j] + add + s[j:]
    return s.replace('BOLO 140 · 2026-10-13 -->', 'BOLO 140 · 2026-10-13; so-what, specificity and clarity checks from coreyhaines31/marketingskills copy-editing (license unconfirmed, ideas only) -->', 1)
edit('.claude/agents/prose-taste.md', pt)

def sc(s):
    n = nl(s)
    i = s.rindex('<!--')
    sec = ('## 4. Threat model (before a tool or page goes public)' + n + n +
           'Write it in four short lists, each tied to files you read. Mark an assumption as an assumption.' + n + n +
           '- **Trust boundaries.** The edges where data crosses from one party or place to another: Chief to a script, a script to a fetched page, a local server to the browser, a private folder to a public one.' + n +
           '- **Assets.** What an attacker would want: credentials, private detail in `_PRIVATE/`, the repo history, the machine, the published pages.' + n +
           '- **Entry points.** Every place outside data gets in: arguments, fetched URLs, pasted text, parsed files, local ports, generated HTML.' + n +
           '- **Abuse paths.** For each: who does what to which asset through which entry point. Rate likelihood and impact low, medium or high, with one sentence of reason. Keep the list short; drop paths that need access the attacker does not have.' + n + n +
           'End with the two assumptions that move the ranking most, and the smallest fix for each high path.' + n + n)
    s = s[:i] + sec + s[i:]
    return s.replace('no text copied ·', 'no text copied; threat-model section idea from openai/skills security-threat-model (license unconfirmed, no text copied) ·', 1)
edit('.claude/agents/references/security-checklist.md', sc)

# SOP 7.23 via change folder
d = '_sop/changes/2026-10-13-s7-23-reader-test'
os.makedirs(d, exist_ok=True)
sop = open('SOP.md', encoding='utf8', newline='').read()
a = sop.index('### 7.23 ')
b = sop.index('### 7.24 ')
before = sop[a:b]
n = nl(sop)
old_when = '- **WHEN** Claude finishes a deliverable (page, note, brief, spec) **THEN** it makes one pass for those four things and fixes or cuts each hit before handing it over.'
assert old_when in before
after = before.replace(old_when, old_when + n + '- **WHEN** Claude finishes the pass **THEN** it reads the deliverable once as the stranger it is written for, and fixes anything that stranger could not follow.')
after = after.replace('<sub>Ruled 2026-10-13 · provisional · BOLO 140 (taste-16, taste-17)</sub>', '<sub>Ruled 2026-10-13 · provisional · BOLO 140 (taste-16, taste-17) · reader test added 10/13, Chief picked volt-02 (anthropics/skills doc-coauthoring, license unconfirmed, idea only)</sub>')
assert after != before
def w(name, t):
    open(os.path.join(d, name), 'w', encoding='utf8', newline='').write(t)
w('before.md', before)
w('after.md', after)
w('proposal.md', '# Change: 7.23 gets a reader test' + n + n + '**Why.** A deliverable can pass the four checks and still lose the person it is written for. Source: volt-02, the fresh-reader stage of doc-coauthoring (idea only).' + n + n + '**MODIFIED**' + n + '- 7.23 The copy self-audit: adds a second WHEN/THEN line, "read it once as the stranger it is written for".' + n)
open('SOP.md', 'w', encoding='utf8', newline='').write(sop[:a] + after + sop[b:])
dest = '_sop/archive/2026-10-13-s7-23-reader-test'
shutil.move(d, dest)
print('ok')
