export const meta = {
  name: 'sitrep',
  description: 'Sit rep formation (BOLO 54/68): prep, then RACK + INDEX + WATCH in parallel, then assemble with RANGE. Stops before Block VI, build, flush and publish.',
  whenToUse: 'Provisional alternative to the sitrep skill. The skill stays canonical (.claude/skills/sitrep/SKILL.md).',
  phases: [
    { title: 'Prep', detail: 'H0: python _tools/sitrep/prep.py (zero-token script)', model: 'haiku' },
    { title: 'Fan out', detail: 'H1: RACK (haiku) · INDEX (sonnet) · WATCH (haiku), disjoint inputs', model: 'sonnet' },
    { title: 'Assemble', detail: 'H2: assemble.py (RANGE), one RERUN pass per named role', model: 'haiku' },
  ],
}

// The script has no filesystem access, so it cannot paste the brief files itself.
// Each specialist is told to read its own brief file and follow it verbatim (same text the skill pastes).
// Block VI, meta.patch.json, build/flush and the Artifact publish stay on the main line (skill H2 step 1-3, H3).

const DATE_SCHEMA = {
  type: 'object',
  properties: {
    date: { type: 'string', description: 'work folder name printed by prep.py, e.g. 2026-10-12-2' },
    digest: { type: 'string', description: 'the 20-line digest, verbatim' },
  },
  required: ['date', 'digest'],
}
const ASSEMBLE_SCHEMA = {
  type: 'object',
  properties: {
    digest: { type: 'string', description: 'the assemble.py output, verbatim' },
    blocking: { type: 'array', items: { type: 'string' }, description: 'blocking findings, empty if none' },
    rerun: { type: 'array', items: { type: 'string' }, description: 'ROLE names from RERUN <ROLE> lines (RACK, INDEX, WATCH), empty if none' },
  },
  required: ['digest', 'blocking', 'rerun'],
}

const ROOT = 'C:/Users/U01_LEECHSEED/Desktop/_setsunadev'
const brief = (date, role) =>
  `You are the ${role} specialist of the sit rep formation. Repo: ${ROOT}. ` +
  `Read ${ROOT}/_tools/sitrep/work/${date}/brief.${role}.md and follow it exactly, as your whole order. ` +
  `Read only the inputs it names. Write only the fragment files it names. Do not read another specialist's input or output. ` +
  `Return one line: the files you wrote.`

// H0 · Prep
phase('Prep')
const prep = await agent(
  `Run in ${ROOT}: python _tools/sitrep/prep.py . Read nothing else. Do not open STATE, BOLO, SOP, PROJECTS or the cache notes. ` +
  `Return the work folder name it prints and its digest verbatim.`,
  { label: 'H0 prep.py', phase: 'Prep', model: 'haiku', schema: DATE_SCHEMA })
if (!prep) throw new Error('prep.py failed; fix it and rerun')
const date = prep.date
log('prep done: ' + date)

// H1 · Fan out (RACK haiku · INDEX sonnet · WATCH haiku), no agent reads another's input or output
phase('Fan out')
const roles = [
  { role: 'RACK', model: 'haiku' },
  { role: 'INDEX', model: 'sonnet' },
  { role: 'WATCH', model: 'haiku' },
]
await parallel(roles.map(r => () =>
  agent(brief(date, r.role), { label: r.role, phase: 'Fan out', model: r.model })))

// H2 · Fan in: RANGE is the script
phase('Assemble')
const assemble = () => agent(
  `Run in ${ROOT}: python _tools/sitrep/assemble.py ${date} . Do not pass --build or --flush. ` +
  `Return its digest verbatim, the blocking findings, and every ROLE named on a "RERUN <ROLE>" line.`,
  { label: 'H2 assemble.py', phase: 'Assemble', model: 'haiku', schema: ASSEMBLE_SCHEMA })
let result = await assemble()

// Auto-rerun (BOLO 95): each named role once, brief = work/<date>/rerun.<ROLE>.md, then assemble again.
if (result && result.rerun && result.rerun.length) {
  const again = result.rerun.filter(r => ['RACK', 'INDEX', 'WATCH'].includes(r))
  log('RERUN ' + again.join(', '))
  await parallel(again.map(role => () =>
    agent(
      `You are the ${role} specialist, second pass. Repo: ${ROOT}. ` +
      `Read ${ROOT}/_tools/sitrep/work/${date}/rerun.${role}.md and follow it exactly. ` +
      `Return one line: the files you wrote.`,
      { label: role + ' rerun', phase: 'Assemble', model: role === 'INDEX' ? 'sonnet' : 'haiku' })))
  result = await assemble()
}

if (result && result.blocking && result.blocking.length) {
  log('BLOCKING findings: fix the one fragment, rerun assemble.py. Nothing is written until they clear.')
}
// Hand back to the main line: write frag/VI.json and meta.patch.json, then
// python _tools/sitrep/assemble.py <date> --build --flush, then publish (skill H2 steps 1-3, H3).
return { date, prep: prep.digest, assemble: result }
