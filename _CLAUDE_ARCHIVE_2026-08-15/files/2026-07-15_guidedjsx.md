---
original_path: "/home/claude/dpapp/src/guided.jsx"
source_conversation: "Unified profiler UI with markdown export"
created: 2026-07-15
trunk: BOTH
kind: generated-file
---

import { TOOLS, ALL_IDS } from "./mc.jsx";

// ---------- per-step coaching copy ----------
const GUIDE = {
  "t1.inventory": {
    why: "Everything downstream feeds on this list — a thin inventory makes a thin profile.",
    how: [
      "Dump every turn-on you've got: fantasies, best real moments, intrusive thoughts, the porn you keep returning to.",
      "Sweep the Tag Board station — tap everything that sparks, then Copy Picks into the notes below.",
      "Quantity over quality. No editing, no explaining, no origin-hunting.",
    ],
    jump: "tags", jumpLabel: "OPEN TAG BOARD ▸",
  },
  "t1.feelings": {
    why: "Acts are the wrapper; the feeling is the payload. The whole method runs on naming it.",
    how: [
      "Take each inventory item and finish the sentence: “this gives me the feeling of ___” (powerful, taken, adored, filthy, safe, in charge…).",
      "One word or short phrase per item — gut answer beats careful answer.",
      "The same feeling repeating across items is signal. Star it.",
    ],
  },
  "t1.triggers": {
    why: "Feelings don't fire at random — something specific pulls the trigger. Find it and you own the mechanism.",
    how: [
      "For each item ask: what exactly delivers the charge — the setting, the power gap, the words, the way you're seen?",
      "Be surgical: “being told what to do” is a trigger; “BDSM” is a category.",
      "Note triggers that show up under multiple turn-ons.",
    ],
  },
  "t1.delivery": {
    why: "Once you know the feeling and trigger, acts become interchangeable — this is where your options multiply.",
    how: [
      "For each core feeling, list other activities that could hit it — including mild, low-risk ones.",
      "List partner qualities that make the feeling land: energy, attitude, dynamic.",
      "You're building routes, not commitments.",
    ],
  },
  "t1.matrix": {
    why: "Locking it into one grid turns a pile of notes into a working map.",
    how: [
      "One row per turn-on: turn-on → feeling → trigger → delivery (acts + partner qualities).",
      "Keep it in the Tool 1 notes or your journal — wherever you'll actually reread it.",
      "Gaps are fine. The matrix is living, not final.",
    ],
  },
  "t2.blueprint": {
    why: "Outside lens #1: your arousal wiring — how you get turned on, not just by what.",
    how: ["Take the quiz (button above) — answer fast and honest.", "Drop your type plus anything that surprised you into the result field on the Console."],
  },
  "t2.bdsmtest": {
    why: "The classic role map — a percentage breakdown across dom, sub, switch and friends.",
    how: ["Run it in solo mode with gut answers.", "Log your top 3–5 roles with percentages."],
  },
  "t2.sexualalpha": {
    why: "An overlapping lens with richer explanations — good for spotting which archetypes repeat.",
    how: ["Take it, then compare against the BDSM Test.", "Note where the two agree — repetition is signal."],
  },
  "t2.aellabig": {
    why: "A guided tour of the whole kink landscape plus your percentile — great for finding things you didn't know had names.",
    how: ["Block 20–30 minutes; it's long but worth it.", "Log your highest-percentile items and anything that made you feel seen."],
  },
  "t2.aellaarch": {
    why: "Maps your preferred dynamic and who you pair with — the relational cut of your kink data.",
    how: ["Take it, then log your archetype.", "Add one line: does it match how you actually show up?"],
  },
  "t3.person": {
    why: "Shame dissolves on contact with a safe witness — picking the right person IS the step.",
    how: [
      "A deeply trusted friend or partner, or a pro (therapist / coach). Conditions beat speed.",
      "Nobody fits yet? Booking a professional counts as done.",
    ],
  },
  "t3.container": {
    why: "The rules make the safety. Said out loud, they turn a chat into a container.",
    how: ["Agree explicitly: confidential, no judgment, no fixing — just witnessing.", "Set an exit: either of you can pause anytime."],
  },
  "t3.block": {
    why: "Disclosure can't be rushed — a clock in the room kills depth.",
    how: ["Book 60–90+ unhurried minutes, private, phones off.", "Pick a spot where you can speak plainly."],
  },
  "t3.done": {
    why: "This is the reference experience: being fully seen and not rejected is what rewires the shame.",
    how: [
      "Cover three layers: history + feelings, desires and kinks, and the shame itself.",
      "Read from notes if that's easier. Shaking is normal. Keep going.",
    ],
  },
  "t3.aftercare": {
    why: "The nervous system needs a landing — skipping this wastes half the work.",
    how: ["Ground yourself: water, food, a walk, warmth — whatever settles you.", "Within 24 hours, journal what surfaced that you didn't expect."],
  },
  "t4.grab": {
    why: "The 317-item menu is docked right in this console — no template hunting, no excuses.",
    how: ["Jump to the SEX MENU station and skim the categories first.", "This step is literally just opening it. Do it now."],
    jump: "smp", jumpLabel: "OPEN SEX MENU ▸",
  },
  "t4.fill": {
    why: "The menu turns self-knowledge into a communicable document — the capstone of the whole system.",
    how: [
      "Rate every item on the 7-point scale; add notes on anything with a story.",
      "Answer for YOU, not for a partner's comfort. Chip away across multiple sittings.",
    ],
    jump: "smp", jumpLabel: "OPEN SEX MENU ▸",
  },
  "t4.share": {
    why: "Optional but potent: two menus side by side is the fastest honest sex conversation two people can have.",
    how: [
      "Export the dossier via the archive button below.",
      "Trade with a partner; discuss overlaps and maybes with curiosity, not negotiation pressure.",
    ],
  },
};

const SYN_GUIDE = {
  why: "Everything funnels here: rank the feelings, map the routes, set the edges.",
  how: [
    "Rank your top 3–5 core feelings on the Console synthesis station.",
    "For each: triggers, green-light activities, partner qualities.",
    "Write your limits: hard, soft (with conditions), curiosities, mind-only.",
  ],
};

// ---------- sequence ----------
export function guideSeq() {
  const seq = [];
  TOOLS.forEach((t) => {
    (t.steps || []).forEach((s) => seq.push({ id: t.id + "." + s.id, tag: t.tag, tool: t.id, toolName: t.name, label: s.label }));
    (t.quizzes || []).forEach((q) => seq.push({ id: t.id + "." + q.id, tag: t.tag, tool: t.id, toolName: t.name, label: q.label, url: q.url, quiz: q.id }));
  });
  return seq;
}
const SEQ = guideSeq();

export function firstOpenIdx(mc) {
  const i = SEQ.findIndex((s) => !mc.done[s.id]);
  return i === -1 ? SEQ.length : i;
}

// ---------- component ----------
export default function GuidedRun({ mc, patch, goTab }) {
  const idx = typeof mc.guided === "number" ? Math.max(0, Math.min(SEQ.length, mc.guided)) : firstOpenIdx(mc);
  const setIdx = (i) => patch((m) => ({ ...m, guided: Math.max(0, Math.min(SEQ.length, i)) }));

  const dn = SEQ.filter((s) => mc.done[s.id]).length;

  // terminal: synthesis screen
  if (idx >= SEQ.length) {
    const synDn = (mc.syn.feel.filter(Boolean).length >= 3 ? 1 : 0) + (mc.syn.delivery.trim() ? 1 : 0) + (mc.syn.limits.trim() ? 1 : 0);
    return (
      <div className="card gpane">
        <div className="gstep-meta"><span>FINAL STAGE · {dn}/{SEQ.length} STEPS BANKED</span><span>{synDn}/3 SYNTHESIS PARTS</span></div>
        <div className="segs" style={{ marginBottom: 16 }}>{SEQ.map((s, i) => <div key={i} className={"seg" + (mc.done[s.id] ? " on" : "")} />)}</div>
        <div className="gtag">FINAL // SYNTHESIS</div>
        <div className="gtitle">{dn >= SEQ.length ? "Run complete — assemble your profile" : "Synthesis · Your Profile"}</div>
        <div className="gwhy">{SYN_GUIDE.why}</div>
        <ul className="ghow">{SYN_GUIDE.how.map((h, i) => <li key={i}>{h}</li>)}</ul>
        {dn < SEQ.length && <div className="auxbody" style={{ marginTop: 10 }}>Heads up: {SEQ.length - dn} step(s) still open behind you. Synthesis lands harder with all four tools banked — hit BACK to sweep them, or push on if you know what you're doing.</div>}
        <div className="gnav">
          <button className="btn" onClick={() => setIdx(idx - 1)}>◂ BACK</button>
          <button className="btn hot" onClick={() => goTab("mc")}>GO TO SYNTHESIS STATION ▸</button>
        </div>
      </div>
    );
  }

  const step = SEQ[idx];
  const g = GUIDE[step.id] || { why: "", how: [] };
  const on = !!mc.done[step.id];

  const markNext = () => {
    if (!on) patch((m) => ({ ...m, done: { ...m.done, [step.id]: true }, guided: Math.min(SEQ.length, idx + 1) }));
    else setIdx(idx + 1);
  };
  const setNote = (v) => patch((m) => ({ ...m, notes: { ...m.notes, [step.tool]: v } }));
  const setQuiz = (v) => patch((m) => ({ ...m, quiz: { ...m.quiz, [step.quiz]: v } }));

  return (
    <div className="card gpane">
      <div className="gstep-meta"><span>STEP {idx + 1} / {SEQ.length}</span><span>{dn} BANKED · {on ? "THIS ONE: DONE" : "THIS ONE: OPEN"}</span></div>
      <div className="segs" style={{ marginBottom: 16 }}>{SEQ.map((s, i) => <div key={i} className={"seg" + (mc.done[s.id] ? " on" : i === idx ? " cur" : "")} />)}</div>

      <div className="gtag">{step.tag} // {step.toolName}</div>
      <div className="gtitle">{step.label}</div>
      <div className="gwhy">{g.why}</div>
      <ul className="ghow">{g.how.map((h, i) => <li key={i}>{h}</li>)}</ul>

      <div style={{ display: "flex", gap: 10, flexWrap: "wrap", marginTop: 6 }}>
        {step.url && <a className="go" href={step.url} target="_blank" rel="noopener noreferrer">TAKE THE QUIZ ↗</a>}
        {g.jump && <button className="go asbtn" onClick={() => goTab(g.jump)}>{g.jumpLabel}</button>}
      </div>

      {step.quiz ? (
        <>
          <div className="note-lbl">▸ Result / key takeaways</div>
          <input className="txt" placeholder="log your result here…" value={mc.quiz[step.quiz] || ""} onChange={(e) => setQuiz(e.target.value)} />
        </>
      ) : (
        <>
          <div className="note-lbl">▸ {step.toolName} — findings / notes (shared with the Console)</div>
          <textarea rows={3} placeholder="capture what this step surfaced…" value={mc.notes[step.tool] || ""} onChange={(e) => setNote(e.target.value)} />
        </>
      )}

      <div className="gnav">
        <button className="btn" disabled={idx === 0} onClick={() => setIdx(idx - 1)}>◂ BACK</button>
        <button className="btn" onClick={() => setIdx(idx + 1)}>SKIP FOR NOW ▸</button>
        <button className="btn hot" onClick={markNext}>{on ? "NEXT ▸" : "✓ MARK DONE · NEXT ▸"}</button>
        {on && <button className="btn" onClick={() => patch((m) => ({ ...m, done: { ...m.done, [step.id]: false } }))}>UNMARK</button>}
      </div>
    </div>
  );
}
