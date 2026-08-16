---
title: "relationship-needs-profiler_1.jsx"
project: "DESIRE PROFILE"
trunk: ORANGE
kind: project-knowledge
---

import { useState, useMemo } from "react";

// ---------- PALETTE (utility-military: olive-black, OD green, coyote, paper) ----------
const C = {
  bg: "#14160F",
  panel: "#1B1E13",
  panel2: "#22261A",
  ink: "#E8E4D8",
  dim: "#9A9784",
  olive: "#8A9A5B",
  oliveDeep: "#4E5A33",
  coyote: "#B08D57",
  line: "#3A3E2C",
  red: "#A45A52",
};

const MONO = "'IBM Plex Mono','JetBrains Mono',ui-monospace,'SF Mono',Menlo,monospace";
const BODY = "'Inter','Helvetica Neue',-apple-system,system-ui,sans-serif";

const STYLES = `
  .rnp input[type=range]{ -webkit-appearance:none; appearance:none; width:100%; height:4px; border-radius:2px; background:${C.line}; outline:none; }
  .rnp input[type=range]::-webkit-slider-thumb{ -webkit-appearance:none; appearance:none; width:22px; height:22px; border-radius:3px; background:${C.olive}; border:1px solid ${C.bg}; cursor:pointer; }
  .rnp input[type=range]::-moz-range-thumb{ width:22px; height:22px; border-radius:3px; background:${C.olive}; border:1px solid ${C.bg}; cursor:pointer; }
  .rnp button:focus-visible, .rnp input:focus-visible, .rnp textarea:focus-visible{ outline:2px solid ${C.coyote}; outline-offset:2px; }
  @media (prefers-reduced-motion: no-preference){ .rnp .fadein{ animation: rnpfade .25s ease; } }
  @keyframes rnpfade{ from{ opacity:0; transform:translateY(4px);} to{ opacity:1; transform:none;} }
`;

// ---------- QUESTION DATA ----------
// kinds: likert (1-5) | rate (0-10) | single | pick (ordered, max) | flex (importance+flexibility) | check (select + mark absolute)

const SECTIONS = [
  {
    code: "01",
    name: "BONDING PATTERN",
    blurb: "How you attach, and what threatens the bond. Answer from your actual history — not your ideal self.",
    items: [
      { kind: "likert", id: "a1", key: "anx", text: "I worry that people I'm close to won't stay interested in me for the long haul." },
      { kind: "likert", id: "a2", key: "anx", text: "When a partner goes distant or slow to respond, I feel it in my body — restlessness, spinning thoughts." },
      { kind: "likert", id: "a3", key: "anx", text: "I need regular reassurance that things between us are still good." },
      { kind: "likert", id: "a4", key: "anx", text: "I sometimes want to merge so completely with someone that it risks scaring them off." },
      { kind: "likert", id: "a5", key: "anx", text: "If someone pulls back even slightly, I start scanning for what went wrong." },
      { kind: "likert", id: "a6", key: "anx", text: "Long stretches alone make me feel unmoored more than free." },
      { kind: "likert", id: "v1", key: "avd", text: "I get uncomfortable when someone wants to be emotionally closer than I'm ready for." },
      { kind: "likert", id: "v2", key: "avd", text: "I prefer not to show a partner how I feel deep down." },
      { kind: "likert", id: "v3", key: "avd", text: "I find it hard to fully rely on a romantic partner." },
      { kind: "likert", id: "v4", key: "avd", text: "When things get very intimate, part of me wants to create distance." },
      { kind: "likert", id: "v5", key: "avd", text: "I keep parts of my inner life walled off, even in good relationships." },
      { kind: "likert", id: "v6", key: "avd", text: "When independence and closeness conflict, independence wins." },
    ],
  },
  {
    code: "02",
    name: "SUPPLY LINES",
    blurb: "What the relationship must feed. Rate what each is actually worth to you — not what sounds mature.",
    items: [
      { kind: "rate", id: "n_aff", text: "Physical affection & tenderness", sub: "Warmth, casual touch, closeness outside of sex" },
      { kind: "rate", id: "n_sex", text: "Sexual fulfillment", sub: "Frequency and quality that match your drive" },
      { kind: "rate", id: "n_des", text: "Feeling desired", sub: "They initiate. They visibly want you." },
      { kind: "rate", id: "n_adm", text: "Admiration & respect", sub: "They're proud of you and treat your competence as real" },
      { kind: "rate", id: "n_rec", text: "Recreational companionship", sub: "A genuine partner-in-crime for play and hobbies" },
      { kind: "rate", id: "n_conv", text: "Deep conversation", sub: "A real confidant for the inner life" },
      { kind: "rate", id: "n_hon", text: "Honesty & transparency", sub: "Nothing hidden. No games." },
      { kind: "rate", id: "n_auto", text: "Autonomy & space", sub: "Room to be your own person without penalty" },
      { kind: "rate", id: "n_dom", text: "Domestic partnership", sub: "Running a home and life logistics well together" },
      { kind: "rate", id: "n_amb", text: "Shared ambition", sub: "They're building something too" },
      { kind: "rate", id: "n_peace", text: "Peace & low conflict", sub: "A calm baseline, not a battlefield" },
      { kind: "rate", id: "n_need", text: "Being needed", sub: "They lean on you. You're essential." },
      { kind: "rate", id: "n_grow", text: "Mutual growth", sub: "The relationship levels you both up" },
    ],
  },
  {
    code: "03",
    name: "CRITICAL SUPPLY",
    blurb: "Scarcity test. Suppose only three of these ever get fully met. Choose in order — first pick is your number one.",
    items: [
      {
        kind: "pick", id: "crit", max: 3,
        options: [
          { v: "n_aff", label: "Physical affection & tenderness" },
          { v: "n_sex", label: "Sexual fulfillment" },
          { v: "n_des", label: "Feeling desired" },
          { v: "n_adm", label: "Admiration & respect" },
          { v: "n_rec", label: "Recreational companionship" },
          { v: "n_conv", label: "Deep conversation" },
          { v: "n_hon", label: "Honesty & transparency" },
          { v: "n_auto", label: "Autonomy & space" },
          { v: "n_dom", label: "Domestic partnership" },
          { v: "n_amb", label: "Shared ambition" },
          { v: "n_peace", label: "Peace & low conflict" },
          { v: "n_need", label: "Being needed" },
          { v: "n_grow", label: "Mutual growth" },
        ],
      },
    ],
  },
  {
    code: "04",
    name: "IGNITION SYSTEM",
    blurb: "Accelerator and brakes. This is mechanics, not preference — answer from what actually happens.",
    items: [
      { kind: "likert", id: "e1", key: "ses", text: "My desire switches on fast when the context is right." },
      { kind: "likert", id: "e2", key: "ses", text: "Novelty — new scenarios, new energy — amps me hard." },
      { kind: "likert", id: "e3", key: "ses", text: "Buildup and flirtation through the day strongly drive me." },
      { kind: "likert", id: "e4", key: "ses", text: "Visual and sensory cues have an outsized effect on me." },
      { kind: "likert", id: "p1", key: "sis1", text: "Worry about performing well can shut my arousal down." },
      { kind: "likert", id: "p2", key: "sis1", text: "If I think they're not into it, I lose steam fast." },
      { kind: "likert", id: "p3", key: "sis1", text: "Pressure and expectation make desire harder to reach, not easier." },
      { kind: "likert", id: "c1", key: "sis2", text: "Life stress kills my drive hard." },
      { kind: "likert", id: "c2", key: "sis2", text: "Unresolved tension between us makes desire nearly impossible." },
      { kind: "likert", id: "c3", key: "sis2", text: "Obligation or pity kills it instantly — I need real want." },
      { kind: "likert", id: "ds1", key: "dstand", text: "Feeling wanted matters as much to me as the act itself." },
      { kind: "likert", id: "ds2", key: "dstand", text: "Deep familiarity beats constant novelty for me." },
      { kind: "likert", id: "ds3", key: "dstand", text: "I want a partner who initiates as often as I do." },
    ],
  },
  {
    code: "05",
    name: "CURRENCY",
    blurb: "How you pay love out — and what denomination actually lands when it comes back.",
    items: [
      { kind: "rate", id: "g_words", group: "WHEN I CARE, I NATURALLY…", text: "Say it", sub: "Affirmation, praise, naming what I see in them" },
      { kind: "rate", id: "g_time", text: "Give undivided time", sub: "Full presence, no split attention" },
      { kind: "rate", id: "g_acts", text: "Handle things", sub: "Fix, cook, carry, solve" },
      { kind: "rate", id: "g_touch", text: "Touch", sub: "Physical closeness as a constant channel" },
      { kind: "rate", id: "g_gifts", text: "Give things", sub: "Chosen objects that prove I was paying attention" },
      { kind: "rate", id: "r_words", group: "IT LANDS DEEPEST WHEN THEY…", text: "Tell me what I mean to them", sub: "Out loud, unprompted" },
      { kind: "rate", id: "r_time", text: "Give me real time", sub: "Undistracted, protected time together" },
      { kind: "rate", id: "r_acts", text: "Do things for me", sub: "Without being asked" },
      { kind: "rate", id: "r_touch", text: "Reach for me", sub: "Casual, constant physical contact" },
      { kind: "rate", id: "r_gifts", text: "Bring me things that prove they know me", sub: "Specificity over price" },
    ],
  },
  {
    code: "06",
    name: "TARGETING",
    blurb: "What pulls you — and how much tolerance each standard really has. Flexibility means how much deviation from ideal you'd genuinely accept.",
    items: [
      { kind: "flex", id: "w", text: "Warmth & trustworthiness", sub: "Kind, loyal, emotionally safe" },
      { kind: "flex", id: "vt", text: "Vitality & attractiveness", sub: "Physical pull, energy, style" },
      { kind: "flex", id: "st", text: "Status & resources", sub: "Ambition, earning power, standing" },
      { kind: "likert", id: "t1", key: "pull", text: "I'm most pulled toward intensity and spark, even when it comes with chaos." },
      { kind: "likert", id: "t2", key: "pull", text: "Calm, steady energy attracts me more than electricity." },
      { kind: "likert", id: "t3", key: "pull", text: "I'm often drawn to people who are struggling or need saving in some way." },
      { kind: "likert", id: "t4", key: "pull", text: "I'm drawn to people who aren't fully available or are hard to win." },
      { kind: "likert", id: "t5", key: "pull", text: "Without strong physical pull early on, it won't grow for me." },
      {
        kind: "single", id: "mirror", text: "The partner that works long-term for me is…",
        options: [
          { v: "mirror", label: "A mirror — someone like me" },
          { v: "counter", label: "A counterweight — someone unlike me" },
          { v: "blend", label: "A blend — core values mirrored, texture different" },
        ],
      },
    ],
  },
  {
    code: "07",
    name: "DOCTRINE",
    blurb: "Long-run alignment. Values, structure, lifestyle — the stuff that decides year five, not week five.",
    items: [
      {
        kind: "pick", id: "vals", max: 3,
        text: "Pick your top three values — in order.",
        options: [
          { v: "freedom", label: "Freedom & self-direction" },
          { v: "adventure", label: "Adventure & stimulation" },
          { v: "pleasure", label: "Pleasure & enjoyment" },
          { v: "achieve", label: "Achievement & mastery" },
          { v: "status", label: "Influence & status" },
          { v: "security", label: "Security & stability" },
          { v: "tradition", label: "Tradition & rootedness" },
          { v: "loyalty", label: "Loyalty & devotion" },
          { v: "care", label: "Care & kindness" },
          { v: "purpose", label: "Purpose beyond yourself" },
        ],
      },
      {
        kind: "single", id: "structure", text: "Relationship structure that fits what you actually want:",
        options: [
          { v: "mono", label: "Strictly monogamous" },
          { v: "mono_open", label: "Monogamous, but open to the conversation" },
          { v: "enm", label: "Open / ENM" },
          { v: "unsure", label: "Genuinely unsure" },
        ],
      },
      { kind: "likert", id: "d1", key: "life", text: "Our social batteries need to match — mismatch there wears me down." },
      { kind: "likert", id: "d2", key: "life", text: "How a home is kept and run matters a lot to me." },
    ],
  },
  {
    code: "08",
    name: "FIELD CONDUCT",
    blurb: "How you fight, and what repair requires. Your pattern under threat, not your best behavior.",
    items: [
      {
        kind: "single", id: "conflict", text: "When conflict hits, my default is…",
        options: [
          { v: "withdraw", label: "I go quiet and pull back" },
          { v: "defend", label: "I explain, justify, argue my case" },
          { v: "attack", label: "I go on offense — the problem, and sometimes the person" },
          { v: "appease", label: "I smooth it over and absorb it" },
        ],
      },
      {
        kind: "single", id: "repair", text: "After a fight, what I actually need is…",
        options: [
          { v: "space", label: "Space first, talk later" },
          { v: "talk", label: "Talk it out immediately" },
          { v: "touch", label: "Physical reconnection before words" },
          { v: "written", label: "Written words — I process on paper" },
        ],
      },
      { kind: "likert", id: "f1", key: "conduct", text: "I need more verbal reassurance than I let on." },
      { kind: "likert", id: "f2", key: "conduct", text: "Jealousy hits me harder than I admit." },
      { kind: "likert", id: "f3", key: "conduct", text: "I can't relax in a low-communication relationship." },
    ],
  },
  {
    code: "09",
    name: "THE KNIGHT AXIS",
    blurb: "Being needed, rescuing, provision as love. No judgment coded in — just measure it.",
    items: [
      { kind: "likert", id: "k1", key: "knight", text: "Feeling essential to my partner's life is part of what makes love feel real." },
      { kind: "likert", id: "k2", key: "knight", text: "I show love most naturally by solving, fixing, and providing." },
      { kind: "likert", id: "k3", key: "knight", text: "I've pursued people partly because they needed me." },
      { kind: "likert", id: "k4", key: "knight", text: "If a partner were fully self-sufficient, part of me would wonder what I'm for." },
    ],
  },
  {
    code: "10",
    name: "RED LINES",
    blurb: "Dealbreakers. Mark them now, while you're calm — you will be tempted to trade them later. Tag up to three as absolute.",
    items: [
      {
        kind: "check", id: "db", maxAbs: 3,
        options: [
          "Dishonesty or cheating",
          "Addiction that goes untreated",
          "Contempt or disrespect",
          "Dead bedroom",
          "Financial recklessness",
          "No ambition or drive",
          "Constant conflict",
          "Controlling or jealous behavior",
          "Misaligned on kids",
          "Misaligned on monogamy",
          "Refuses to grow or change",
          "No shared play or fun",
          "Chronic negativity",
          "Dismisses my work or craft",
          "No independence — can't function alone",
          "Emotionally sealed off",
        ],
      },
    ],
  },
];

const NEED_LABELS = {
  n_aff: "Physical affection & tenderness", n_sex: "Sexual fulfillment", n_des: "Feeling desired",
  n_adm: "Admiration & respect", n_rec: "Recreational companionship", n_conv: "Deep conversation",
  n_hon: "Honesty & transparency", n_auto: "Autonomy & space", n_dom: "Domestic partnership",
  n_amb: "Shared ambition", n_peace: "Peace & low conflict", n_need: "Being needed", n_grow: "Mutual growth",
};

const DRIVE_WORD = {
  n_aff: "Tender", n_sex: "Hedonic", n_des: "Flame", n_adm: "Champion", n_rec: "Co-Pilot",
  n_conv: "Confidant", n_hon: "Plainspeak", n_auto: "Ranger", n_dom: "Homesteader",
  n_amb: "Builder", n_peace: "Harbor", n_need: "Knight", n_grow: "Ascendant",
};

// ---------- SMALL COMPONENTS ----------

function Stamp({ code, name }) {
  return (
    <div style={{ border: `1px solid ${C.line}`, display: "inline-block", padding: "6px 12px", borderRadius: 2 }}>
      <div style={{ fontFamily: MONO, fontSize: 10, letterSpacing: 3, color: C.dim }}>RNP-1 // SECTION {code}</div>
      <div style={{ fontFamily: MONO, fontSize: 18, letterSpacing: 4, color: C.olive, fontWeight: 700 }}>{name}</div>
    </div>
  );
}

function LikertItem({ item, value, onSet }) {
  return (
    <div style={{ padding: "14px 0", borderBottom: `1px solid ${C.line}` }}>
      <div style={{ fontFamily: BODY, fontSize: 15, lineHeight: 1.45, color: C.ink, marginBottom: 10 }}>{item.text}</div>
      <div style={{ display: "flex", gap: 6, alignItems: "center" }}>
        <span style={{ fontFamily: MONO, fontSize: 9, color: C.dim, width: 52, letterSpacing: 1 }}>DISAGREE</span>
        <div style={{ display: "flex", gap: 6, flex: 1, justifyContent: "center" }}>
          {[1, 2, 3, 4, 5].map((n) => (
            <button key={n} onClick={() => onSet(n)}
              style={{
                width: 40, height: 40, borderRadius: 3, cursor: "pointer",
                fontFamily: MONO, fontSize: 14, fontWeight: 700,
                border: `1px solid ${value === n ? C.olive : C.line}`,
                background: value === n ? C.olive : C.panel2,
                color: value === n ? C.bg : C.dim,
              }}>{n}</button>
          ))}
        </div>
        <span style={{ fontFamily: MONO, fontSize: 9, color: C.dim, width: 52, textAlign: "right", letterSpacing: 1 }}>AGREE</span>
      </div>
    </div>
  );
}

function RateItem({ item, value, onSet }) {
  const v = value === undefined ? 5 : value;
  const touched = value !== undefined;
  return (
    <div style={{ padding: "14px 0", borderBottom: `1px solid ${C.line}` }}>
      {item.group && (
        <div style={{ fontFamily: MONO, fontSize: 10, letterSpacing: 3, color: C.coyote, margin: "6px 0 12px" }}>{item.group}</div>
      )}
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline", gap: 10 }}>
        <div>
          <div style={{ fontFamily: BODY, fontSize: 15, color: C.ink }}>{item.text}</div>
          {item.sub && <div style={{ fontFamily: BODY, fontSize: 12.5, color: C.dim, marginTop: 2 }}>{item.sub}</div>}
        </div>
        <div style={{
          fontFamily: MONO, fontSize: 16, fontWeight: 700, minWidth: 34, textAlign: "center",
          color: touched ? C.olive : C.dim, border: `1px solid ${touched ? C.olive : C.line}`, borderRadius: 3, padding: "2px 4px",
        }}>{touched ? v : "–"}</div>
      </div>
      <input type="range" min="0" max="10" step="1" value={v} aria-label={item.text}
        onChange={(e) => onSet(Number(e.target.value))}
        onPointerUp={() => { if (!touched) onSet(v); }}
        style={{ marginTop: 12 }} />
      <div style={{ display: "flex", justifyContent: "space-between", fontFamily: MONO, fontSize: 9, color: C.dim, letterSpacing: 1, marginTop: 4 }}>
        <span>0 · IRRELEVANT</span><span>10 · VITAL</span>
      </div>
    </div>
  );
}

function SingleItem({ item, value, onSet }) {
  return (
    <div style={{ padding: "14px 0", borderBottom: `1px solid ${C.line}` }}>
      {item.text && <div style={{ fontFamily: BODY, fontSize: 15, color: C.ink, marginBottom: 10 }}>{item.text}</div>}
      <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
        {item.options.map((o) => (
          <button key={o.v} onClick={() => onSet(o.v)}
            style={{
              textAlign: "left", padding: "12px 14px", borderRadius: 3, cursor: "pointer",
              fontFamily: BODY, fontSize: 14.5,
              border: `1px solid ${value === o.v ? C.olive : C.line}`,
              background: value === o.v ? C.oliveDeep : C.panel2,
              color: value === o.v ? C.ink : C.dim,
            }}>{o.label}</button>
        ))}
      </div>
    </div>
  );
}

function PickItem({ item, value = [], onSet }) {
  const toggle = (v) => {
    if (value.includes(v)) onSet(value.filter((x) => x !== v));
    else if (value.length < item.max) onSet([...value, v]);
  };
  return (
    <div style={{ padding: "14px 0" }}>
      {item.text && <div style={{ fontFamily: BODY, fontSize: 15, color: C.ink, marginBottom: 10 }}>{item.text}</div>}
      <div style={{ fontFamily: MONO, fontSize: 10, letterSpacing: 2, color: value.length === item.max ? C.olive : C.coyote, marginBottom: 10 }}>
        SELECTED {value.length}/{item.max} — TAP AGAIN TO REMOVE
      </div>
      <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
        {item.options.map((o) => {
          const idx = value.indexOf(o.v);
          const sel = idx >= 0;
          return (
            <button key={o.v} onClick={() => toggle(o.v)}
              style={{
                display: "flex", alignItems: "center", gap: 10, textAlign: "left",
                padding: "12px 14px", borderRadius: 3, cursor: "pointer",
                fontFamily: BODY, fontSize: 14.5,
                border: `1px solid ${sel ? C.olive : C.line}`,
                background: sel ? C.oliveDeep : C.panel2,
                color: sel ? C.ink : C.dim,
              }}>
              <span style={{
                fontFamily: MONO, fontSize: 11, fontWeight: 700, width: 26, height: 26, borderRadius: 2,
                display: "inline-flex", alignItems: "center", justifyContent: "center",
                border: `1px solid ${sel ? C.olive : C.line}`, color: sel ? C.olive : C.dim, background: C.bg,
              }}>{sel ? idx + 1 : "·"}</span>
              {o.label}
            </button>
          );
        })}
      </div>
    </div>
  );
}

function FlexItem({ item, imp, flex, onSet }) {
  const row = (label, val, key, lo, hi) => {
    const touched = val !== undefined;
    const v = touched ? val : 5;
    return (
      <div style={{ marginTop: 10 }}>
        <div style={{ display: "flex", justifyContent: "space-between", fontFamily: MONO, fontSize: 10, letterSpacing: 2, color: C.dim }}>
          <span>{label}</span>
          <span style={{ color: touched ? C.olive : C.dim, fontWeight: 700 }}>{touched ? v : "–"}</span>
        </div>
        <input type="range" min="0" max="10" step="1" value={v} aria-label={item.text + " " + label}
          onChange={(e) => onSet(key, Number(e.target.value))}
          onPointerUp={() => { if (!touched) onSet(key, v); }}
          style={{ marginTop: 6 }} />
        <div style={{ display: "flex", justifyContent: "space-between", fontFamily: MONO, fontSize: 9, color: C.dim, marginTop: 2 }}>
          <span>{lo}</span><span>{hi}</span>
        </div>
      </div>
    );
  };
  return (
    <div style={{ padding: "14px 0", borderBottom: `1px solid ${C.line}` }}>
      <div style={{ fontFamily: BODY, fontSize: 15, color: C.ink }}>{item.text}</div>
      {item.sub && <div style={{ fontFamily: BODY, fontSize: 12.5, color: C.dim, marginTop: 2 }}>{item.sub}</div>}
      {row("IMPORTANCE", imp, item.id + "_imp", "0 · DON'T CARE", "10 · CORE")}
      {row("FLEXIBILITY", flex, item.id + "_flex", "0 · ZERO TOLERANCE", "10 · FULLY FLEXIBLE")}
    </div>
  );
}

function CheckItem({ item, sel = [], abs = [], onSel, onAbs }) {
  const toggleSel = (o) => {
    if (sel.includes(o)) { onSel(sel.filter((x) => x !== o)); onAbs(abs.filter((x) => x !== o)); }
    else onSel([...sel, o]);
  };
  const toggleAbs = (o) => {
    if (abs.includes(o)) onAbs(abs.filter((x) => x !== o));
    else if (abs.length < item.maxAbs) onAbs([...abs, o]);
  };
  return (
    <div style={{ padding: "14px 0" }}>
      <div style={{ fontFamily: MONO, fontSize: 10, letterSpacing: 2, color: C.coyote, marginBottom: 10 }}>
        ABSOLUTES MARKED {abs.length}/{item.maxAbs}
      </div>
      <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
        {item.options.map((o) => {
          const s = sel.includes(o); const a = abs.includes(o);
          return (
            <div key={o} style={{
              display: "flex", alignItems: "center", gap: 8, padding: "10px 12px", borderRadius: 3,
              border: `1px solid ${a ? C.red : s ? C.olive : C.line}`,
              background: s ? C.panel2 : C.panel,
            }}>
              <button onClick={() => toggleSel(o)} style={{
                flex: 1, textAlign: "left", background: "none", border: "none", cursor: "pointer",
                fontFamily: BODY, fontSize: 14.5, color: s ? C.ink : C.dim, padding: 0,
              }}>{o}</button>
              {s && (
                <button onClick={() => toggleAbs(o)} style={{
                  fontFamily: MONO, fontSize: 9, letterSpacing: 2, padding: "5px 8px", borderRadius: 2, cursor: "pointer",
                  border: `1px solid ${a ? C.red : C.line}`, background: a ? C.red : "transparent",
                  color: a ? C.ink : C.dim,
                }}>{a ? "ABSOLUTE" : "MARK ABS"}</button>
              )}
            </div>
          );
        })}
      </div>
    </div>
  );
}

function Bar({ label, val, max = 5, color = C.olive, note }) {
  const pct = Math.round((val / max) * 100);
  return (
    <div style={{ marginBottom: 10 }}>
      <div style={{ display: "flex", justifyContent: "space-between", fontFamily: MONO, fontSize: 10.5, letterSpacing: 1.5, color: C.dim }}>
        <span>{label}</span><span style={{ color }}>{typeof val === "number" ? val.toFixed(1) : val}{note ? " · " + note : ""}</span>
      </div>
      <div style={{ height: 6, background: C.line, borderRadius: 3, marginTop: 4 }}>
        <div style={{ width: pct + "%", height: "100%", background: color, borderRadius: 3 }} />
      </div>
    </div>
  );
}

// ---------- SCORING ----------

function band(v) { return v < 2.4 ? "LOW" : v < 3.6 ? "MODERATE" : "HIGH"; }

function computeResults(ans) {
  const avg = (ids) => ids.reduce((s, i) => s + (ans[i] || 0), 0) / ids.length;

  const anx = avg(["a1", "a2", "a3", "a4", "a5", "a6"]);
  const avd = avg(["v1", "v2", "v3", "v4", "v5", "v6"]);
  const pattern = anx >= 3.2 && avd >= 3.2 ? "GUARDED" : anx >= 3.2 ? "ALL-IN" : avd >= 3.2 ? "SOVEREIGN" : "STEADY";

  const needIds = Object.keys(NEED_LABELS);
  const ranked = [...needIds].sort((a, b) => (ans[b] || 0) - (ans[a] || 0));
  const crit = ans.crit || [];

  const ses = avg(["e1", "e2", "e3", "e4"]);
  const sis1 = avg(["p1", "p2", "p3"]);
  const sis2 = avg(["c1", "c2", "c3"]);

  const giveIds = ["g_words", "g_time", "g_acts", "g_touch", "g_gifts"];
  const recvIds = ["r_words", "r_time", "r_acts", "r_touch", "r_gifts"];
  const curLabel = { words: "words", time: "time & presence", acts: "acts of service", touch: "touch", gifts: "gifts" };
  const topOf = (ids) => ids.reduce((best, i) => ((ans[i] || 0) > (ans[best] || 0) ? i : best), ids[0]);
  const giveTop = topOf(giveIds), recvTop = topOf(recvIds);
  const giveKey = giveTop.slice(2), recvKey = recvTop.slice(2);

  const flexClass = (imp, flx) =>
    imp >= 8 && flx <= 3 ? "NON-NEGOTIABLE" : imp >= 7 ? "PRIORITY" : imp >= 4 ? "PREFERENCE" : "LOW-WEIGHT";
  const ideals = [
    { id: "w", label: "Warmth & trust" },
    { id: "vt", label: "Vitality & attraction" },
    { id: "st", label: "Status & resources" },
  ].map((x) => ({
    ...x, imp: ans[x.id + "_imp"] ?? 0, flex: ans[x.id + "_flex"] ?? 0,
    cls: flexClass(ans[x.id + "_imp"] ?? 0, ans[x.id + "_flex"] ?? 0),
  }));

  const chaos = ans.t1 || 0, steady = ans.t2 || 0, rescue = ans.t3 || 0, chase = ans.t4 || 0, spark = ans.t5 || 0;
  const lean = chaos - steady >= 1 ? "SPARK-LEANING" : steady - chaos >= 1 ? "STEADY-LEANING" : "BALANCED";

  const knight = avg(["k1", "k2", "k3", "k4"]);
  const knightFlag = knight >= 3.5 ? "ACTIVE" : knight >= 2.8 ? "ELEVATED" : "LOW";

  let drive = DRIVE_WORD[crit[0]] || "Seeker";
  if (knightFlag === "ACTIVE" && crit.includes("n_need")) drive = "Knight";
  const attachWord = { STEADY: "Steady", "ALL-IN": "All-In", SOVEREIGN: "Sovereign", GUARDED: "Guarded" }[pattern];
  const archetype = "THE " + attachWord.toUpperCase() + " " + drive.toUpperCase();

  return {
    anx, avd, pattern, ranked, crit, ses, sis1, sis2,
    dstand: { desired: ans.ds1 || 0, familiar: ans.ds2 || 0, init: ans.ds3 || 0 },
    giveIds, recvIds, giveTop, recvTop, giveKey, recvKey, curLabel,
    ideals, chaos, steady, rescue, chase, spark, lean,
    knight, knightFlag, archetype,
    vals: ans.vals || [], structure: ans.structure, mirror: ans.mirror,
    conflict: ans.conflict, repair: ans.repair,
    conduct: { reassure: ans.f1 || 0, jealousy: ans.f2 || 0, commFloor: ans.f3 || 0 },
    life: { social: ans.d1 || 0, home: ans.d2 || 0 },
    dbSel: ans.db_sel || [], dbAbs: ans.db_abs || [],
  };
}

const ATTACH_TEXT = {
  STEADY: "You bond steady — closeness doesn't threaten you and distance doesn't destabilize you.",
  "ALL-IN": "You bond hot and fast — you attach hard, and distance registers as threat before it registers as information. Consistent, legible reassurance isn't neediness for you; it's operating requirements.",
  SOVEREIGN: "You bond on your own terms — the connection is real, but pressure to merge reads as danger. You need a partner who can hold closeness without demanding fusion.",
  GUARDED: "You bond in push-pull — you crave the exact closeness that trips your alarms. You need patience and steadiness from the other side on both fronts.",
};

const CONFLICT_TEXT = {
  withdraw: "Withdraw — you go quiet and pull back",
  defend: "Defend — you argue your case",
  attack: "Offense — you push into the problem, sometimes the person",
  appease: "Appease — you smooth it over and absorb it",
};
const REPAIR_TEXT = {
  space: "space first, talk later", talk: "talking it out immediately",
  touch: "physical reconnection before words", written: "written words",
};
const STRUCTURE_TEXT = {
  mono: "Strictly monogamous", mono_open: "Monogamous, open to the conversation",
  enm: "Open / ENM", unsure: "Genuinely unsure",
};
const MIRROR_TEXT = { mirror: "A mirror of you", counter: "A counterweight to you", blend: "Values mirrored, texture different" };
const VAL_LABELS = {
  freedom: "Freedom & self-direction", adventure: "Adventure & stimulation", pleasure: "Pleasure & enjoyment",
  achieve: "Achievement & mastery", status: "Influence & status", security: "Security & stability",
  tradition: "Tradition & rootedness", loyalty: "Loyalty & devotion", care: "Care & kindness", purpose: "Purpose beyond yourself",
};

function modelStatement(r) {
  const p = [];
  p.push(ATTACH_TEXT[r.pattern]);
  const top3 = r.crit.map((id) => NEED_LABELS[id].toLowerCase());
  if (top3.length === 3) p.push(`The relationship has to feed ${top3[0]}, ${top3[1]}, and ${top3[2]} — starve those and nothing else built inside it will hold.`);
  const brakeMain = r.sis2 >= r.sis1 ? "context" : "performance";
  let ign = `Your ignition runs a ${band(r.ses).toLowerCase()} accelerator against a ${band(Math.max(r.sis1, r.sis2)).toLowerCase()} ${brakeMain} brake`;
  if (band(Math.max(r.sis1, r.sis2)) !== "LOW") {
    ign += brakeMain === "context"
      ? " — unresolved tension and feeling like an obligation are your kill switch, so peace and genuine want are prerequisites, not luxuries."
      : " — pressure and doubt about their enthusiasm are your kill switch, so a partner whose want is obvious is a requirement, not a bonus.";
  } else { ign += " — your brakes run light; context rarely stops you."; }
  p.push(ign);
  if (r.dstand.desired >= 4) p.push("Feeling wanted is load-bearing: initiation from their side is fuel, not garnish.");
  let cur = `You pay love out in ${r.curLabel[r.giveKey]} and it lands deepest as ${r.curLabel[r.recvKey]}.`;
  if (r.giveKey !== r.recvKey) cur += " Note the mismatch — what you give by default is not the denomination you most need back. Say that out loud early.";
  p.push(cur);
  const nn = r.ideals.filter((i) => i.cls === "NON-NEGOTIABLE").map((i) => i.label.toLowerCase());
  if (nn.length) p.push(`Non-negotiable standard${nn.length > 1 ? "s" : ""}: ${nn.join(", ")}.`);
  if (r.lean !== "BALANCED") p.push(r.lean === "SPARK-LEANING"
    ? "Your pull runs toward spark and intensity — audit whether the chaos tax is one you actually want to keep paying."
    : "Your pull runs toward steady over spark — protect that; electricity you can build, calm you can't fake.");
  if (r.knightFlag !== "LOW") p.push("The Knight axis is " + r.knightFlag.toLowerCase() + ": being needed reads as love and provision is your native tongue. It's a feature when you choose it — a trap when it does the choosing. Watch for picking partners by their need for rescue instead of their fit.");
  if (r.conflict && r.repair) p.push(`Under fire you ${CONFLICT_TEXT[r.conflict].split(" — ")[1]}; repair runs through ${REPAIR_TEXT[r.repair]}.`);
  p.push("Treat this whole sheet as hypotheses — test it against who you actually reach for.");
  return p;
}

function buildYaml(r) {
  const L = [];
  L.push("profile: romantic-needs-v1");
  L.push("generated: " + new Date().toISOString().slice(0, 10));
  L.push('archetype: "' + r.archetype + '"');
  L.push("attachment:");
  L.push("  anxiety: " + r.anx.toFixed(2) + "   # 1-5");
  L.push("  avoidance: " + r.avd.toFixed(2));
  L.push("  pattern: " + r.pattern);
  L.push("needs_ranked:");
  r.ranked.forEach((id) => L.push("  - " + NEED_LABELS[id] + ": " + (r.crit.includes(id) ? "CRITICAL" : "")));
  L.push("critical_three:");
  r.crit.forEach((id, i) => L.push("  " + (i + 1) + ": " + NEED_LABELS[id]));
  L.push("desire:");
  L.push("  accelerator: " + r.ses.toFixed(2) + "   # " + band(r.ses));
  L.push("  brake_performance: " + r.sis1.toFixed(2) + "   # " + band(r.sis1));
  L.push("  brake_context: " + r.sis2.toFixed(2) + "   # " + band(r.sis2));
  L.push("  feeling_desired_weight: " + r.dstand.desired + "/5");
  L.push("  familiarity_over_novelty: " + r.dstand.familiar + "/5");
  L.push("  initiation_parity: " + r.dstand.init + "/5");
  L.push("love_currency:");
  L.push("  give_top: " + r.curLabel[r.giveKey]);
  L.push("  receive_top: " + r.curLabel[r.recvKey]);
  L.push("ideals:");
  r.ideals.forEach((i) => L.push("  " + i.label.replace(/ & /g, "_").toLowerCase() + ": { importance: " + i.imp + ", flexibility: " + i.flex + ", class: " + i.cls + " }"));
  L.push("pull_pattern:");
  L.push("  lean: " + r.lean);
  L.push("  chaos: " + r.chaos + "/5, steady: " + r.steady + "/5, rescue_pull: " + r.rescue + "/5, chase: " + r.chase + "/5, spark_req: " + r.spark + "/5");
  L.push("values_top3: [" + r.vals.map((v) => VAL_LABELS[v]).join(", ") + "]");
  L.push("structure: " + (STRUCTURE_TEXT[r.structure] || ""));
  L.push("partner_shape: " + (MIRROR_TEXT[r.mirror] || ""));
  L.push("field_conduct:");
  L.push("  conflict_default: " + (r.conflict || ""));
  L.push("  repair_mode: " + (r.repair || ""));
  L.push("  reassurance_need: " + r.conduct.reassure + "/5, jealousy: " + r.conduct.jealousy + "/5, communication_floor: " + r.conduct.commFloor + "/5");
  L.push("knight_axis: { score: " + r.knight.toFixed(2) + ", flag: " + r.knightFlag + " }");
  L.push("red_lines:");
  r.dbSel.forEach((d) => L.push("  - " + d + (r.dbAbs.includes(d) ? "   # ABSOLUTE" : "")));
  return L.join("\n");
}

// ---------- RESULTS VIEW ----------

function Panel({ title, children }) {
  return (
    <div style={{ border: `1px solid ${C.line}`, borderRadius: 3, padding: 16, background: C.panel, marginBottom: 14 }}>
      <div style={{ fontFamily: MONO, fontSize: 10, letterSpacing: 3, color: C.coyote, marginBottom: 12 }}>{title}</div>
      {children}
    </div>
  );
}

function Chip({ text, tone = C.olive }) {
  return (
    <span style={{
      fontFamily: MONO, fontSize: 9, letterSpacing: 1.5, padding: "3px 7px", borderRadius: 2,
      border: `1px solid ${tone}`, color: tone, marginLeft: 8, whiteSpace: "nowrap",
    }}>{text}</span>
  );
}

function Results({ r, onRevise, onReset }) {
  const [copied, setCopied] = useState(false);
  const yaml = useMemo(() => buildYaml(r), [r]);
  const statement = useMemo(() => modelStatement(r), [r]);

  const copy = async () => {
    try { await navigator.clipboard.writeText(yaml); setCopied(true); }
    catch {
      const ta = document.getElementById("rnp-yaml");
      if (ta) { ta.select(); try { document.execCommand("copy"); setCopied(true); } catch {} }
    }
    setTimeout(() => setCopied(false), 2000);
  };

  return (
    <div className="fadein">
      <div style={{ border: `1px solid ${C.olive}`, borderRadius: 3, padding: "20px 18px", marginBottom: 18, background: C.panel }}>
        <div style={{ fontFamily: MONO, fontSize: 10, letterSpacing: 3, color: C.dim }}>RNP-1 // PROFILE DOSSIER · {new Date().toISOString().slice(0, 10)}</div>
        <div style={{ fontFamily: MONO, fontSize: 26, letterSpacing: 3, color: C.olive, fontWeight: 700, margin: "10px 0 4px" }}>{r.archetype}</div>
        <div style={{ fontFamily: MONO, fontSize: 10.5, letterSpacing: 1.5, color: C.dim }}>
          BOND: {r.pattern} · #1 SUPPLY: {(NEED_LABELS[r.crit[0]] || "—").toUpperCase()} · KNIGHT AXIS: {r.knightFlag}
        </div>
      </div>

      <Panel title="THE MODEL — READ THIS ONE OUT LOUD">
        {statement.map((s, i) => (
          <p key={i} style={{ fontFamily: BODY, fontSize: 14.5, lineHeight: 1.65, color: C.ink, margin: "0 0 10px" }}>{s}</p>
        ))}
      </Panel>

      <Panel title="01 · BONDING PATTERN">
        <Bar label="ATTACHMENT ANXIETY" val={r.anx} note={r.anx >= 3.2 ? "ELEVATED" : "LOW"} color={r.anx >= 3.2 ? C.coyote : C.olive} />
        <Bar label="ATTACHMENT AVOIDANCE" val={r.avd} note={r.avd >= 3.2 ? "ELEVATED" : "LOW"} color={r.avd >= 3.2 ? C.coyote : C.olive} />
      </Panel>

      <Panel title="02–03 · SUPPLY LINES — RANKED">
        {r.ranked.slice(0, 8).map((id, i) => (
          <div key={id} style={{ display: "flex", alignItems: "center", padding: "7px 0", borderBottom: i < 7 ? `1px solid ${C.line}` : "none" }}>
            <span style={{ fontFamily: MONO, fontSize: 11, color: C.dim, width: 26 }}>{String(i + 1).padStart(2, "0")}</span>
            <span style={{ fontFamily: BODY, fontSize: 14, color: C.ink, flex: 1 }}>{NEED_LABELS[id]}</span>
            {r.crit.includes(id) && <Chip text={"CRITICAL #" + (r.crit.indexOf(id) + 1)} tone={C.coyote} />}
          </div>
        ))}
      </Panel>

      <Panel title="04 · IGNITION SYSTEM">
        <Bar label="ACCELERATOR" val={r.ses} note={band(r.ses)} />
        <Bar label="BRAKE — PERFORMANCE" val={r.sis1} note={band(r.sis1)} color={C.coyote} />
        <Bar label="BRAKE — CONTEXT" val={r.sis2} note={band(r.sis2)} color={C.coyote} />
        <div style={{ fontFamily: MONO, fontSize: 10.5, color: C.dim, letterSpacing: 1, marginTop: 8, lineHeight: 1.8 }}>
          FEELING-DESIRED WEIGHT {r.dstand.desired}/5 · FAMILIARITY-OVER-NOVELTY {r.dstand.familiar}/5 · INITIATION PARITY {r.dstand.init}/5
        </div>
      </Panel>

      <Panel title="05 · CURRENCY">
        <div style={{ fontFamily: BODY, fontSize: 14.5, color: C.ink, lineHeight: 1.6 }}>
          You give in <span style={{ color: C.olive, fontWeight: 700 }}>{r.curLabel[r.giveKey]}</span>. It lands as <span style={{ color: C.olive, fontWeight: 700 }}>{r.curLabel[r.recvKey]}</span>.
          {r.giveKey !== r.recvKey && <span style={{ color: C.coyote }}> Mismatch on record — brief your partner.</span>}
        </div>
      </Panel>

      <Panel title="06 · TARGETING">
        {r.ideals.map((i) => (
          <div key={i.id} style={{ display: "flex", alignItems: "center", padding: "8px 0", borderBottom: `1px solid ${C.line}` }}>
            <span style={{ fontFamily: BODY, fontSize: 14, color: C.ink, flex: 1 }}>{i.label}</span>
            <span style={{ fontFamily: MONO, fontSize: 10.5, color: C.dim }}>IMP {i.imp} · FLEX {i.flex}</span>
            <Chip text={i.cls} tone={i.cls === "NON-NEGOTIABLE" ? C.red : i.cls === "PRIORITY" ? C.coyote : C.dim} />
          </div>
        ))}
        <div style={{ fontFamily: MONO, fontSize: 10.5, color: C.dim, letterSpacing: 1, marginTop: 10, lineHeight: 1.8 }}>
          PULL: {r.lean} · RESCUE-PULL {r.rescue}/5 · CHASE {r.chase}/5 · SPARK-REQUIREMENT {r.spark}/5<br />
          PARTNER SHAPE: {(MIRROR_TEXT[r.mirror] || "—").toUpperCase()}
        </div>
      </Panel>

      <Panel title="07 · DOCTRINE">
        <div style={{ fontFamily: BODY, fontSize: 14, color: C.ink, lineHeight: 1.7 }}>
          Values: {r.vals.map((v, i) => (i + 1) + ". " + VAL_LABELS[v]).join("  ·  ")}<br />
          Structure: {STRUCTURE_TEXT[r.structure] || "—"}
        </div>
        <div style={{ fontFamily: MONO, fontSize: 10.5, color: C.dim, letterSpacing: 1, marginTop: 8 }}>
          SOCIAL-BATTERY MATCH {r.life.social}/5 · HOME-STANDARD WEIGHT {r.life.home}/5
        </div>
      </Panel>

      <Panel title="08 · FIELD CONDUCT">
        <div style={{ fontFamily: BODY, fontSize: 14, color: C.ink, lineHeight: 1.7, marginBottom: 8 }}>
          Default under fire: {CONFLICT_TEXT[r.conflict] || "—"}.<br />
          Repair: {REPAIR_TEXT[r.repair] || "—"}.
        </div>
        <Bar label="REASSURANCE NEED" val={r.conduct.reassure} />
        <Bar label="JEALOUSY SENSITIVITY" val={r.conduct.jealousy} color={C.coyote} />
        <Bar label="COMMUNICATION FLOOR" val={r.conduct.commFloor} />
      </Panel>

      <Panel title="09 · THE KNIGHT AXIS">
        <Bar label="KNIGHT SCORE" val={r.knight} note={r.knightFlag} color={r.knightFlag === "ACTIVE" ? C.coyote : C.olive} />
        <div style={{ fontFamily: BODY, fontSize: 13.5, color: C.dim, lineHeight: 1.6 }}>
          {r.knightFlag === "LOW"
            ? "Being needed isn't a primary driver for you. Provision is a choice, not the currency of love."
            : "Being needed reads as love. Cross-check every strong attraction against rescue-pull before committing resources."}
        </div>
      </Panel>

      <Panel title="10 · RED LINES">
        {r.dbSel.length === 0 && <div style={{ fontFamily: BODY, fontSize: 13.5, color: C.dim }}>None marked. That itself is data — revisit when calm.</div>}
        {r.dbSel.map((d) => (
          <div key={d} style={{ fontFamily: BODY, fontSize: 14, padding: "5px 0", color: r.dbAbs.includes(d) ? C.red : C.ink }}>
            {r.dbAbs.includes(d) ? "■ " : "· "}{d}{r.dbAbs.includes(d) ? " — ABSOLUTE" : ""}
          </div>
        ))}
      </Panel>

      <Panel title="EXPORT — OBSIDIAN-READY YAML">
        <textarea id="rnp-yaml" readOnly value={yaml} style={{
          width: "100%", height: 220, background: C.bg, color: C.ink, border: `1px solid ${C.line}`,
          borderRadius: 3, fontFamily: MONO, fontSize: 11, padding: 10, resize: "vertical", boxSizing: "border-box",
        }} />
        <button onClick={copy} style={{
          marginTop: 10, width: "100%", padding: "13px 0", borderRadius: 3, cursor: "pointer",
          fontFamily: MONO, fontSize: 12, letterSpacing: 3, fontWeight: 700,
          background: copied ? C.oliveDeep : C.olive, color: copied ? C.ink : C.bg, border: "none",
        }}>{copied ? "COPIED TO CLIPBOARD" : "COPY PROFILE"}</button>
      </Panel>

      <div style={{ fontFamily: BODY, fontSize: 12, color: C.dim, lineHeight: 1.6, margin: "4px 0 16px" }}>
        Self-reflection instrument with original items modeled on established constructs (attachment dimensions, dual-control desire, ideal standards). Not a clinical measure — for percentile-benchmarked scores, run the validated instruments in your reference doc (ECR-R, SES/SIS, SOI-R). Re-run this in 6 months; patterns drift.
      </div>

      <div style={{ display: "flex", gap: 10 }}>
        <button onClick={onRevise} style={{
          flex: 1, padding: "12px 0", borderRadius: 3, cursor: "pointer", fontFamily: MONO, fontSize: 11,
          letterSpacing: 2, background: "transparent", color: C.dim, border: `1px solid ${C.line}`,
        }}>REVISE ANSWERS</button>
        <button onClick={onReset} style={{
          flex: 1, padding: "12px 0", borderRadius: 3, cursor: "pointer", fontFamily: MONO, fontSize: 11,
          letterSpacing: 2, background: "transparent", color: C.dim, border: `1px solid ${C.line}`,
        }}>START OVER</button>
      </div>
    </div>
  );
}

// ---------- MAIN APP ----------

export default function RelationshipNeedsProfiler() {
  const [stage, setStage] = useState("intro"); // 'intro' | section index | 'results'
  const [ans, setAns] = useState({});
  const set = (id, val) => setAns((p) => ({ ...p, [id]: val }));

  const units = (item) => (item.kind === "flex" ? 2 : 1);
  const totalUnits = SECTIONS.reduce((s, sec) => s + sec.items.reduce((t, i) => t + units(i), 0), 0);

  const answeredUnits = (item) => {
    if (item.kind === "flex") return (ans[item.id + "_imp"] !== undefined ? 1 : 0) + (ans[item.id + "_flex"] !== undefined ? 1 : 0);
    if (item.kind === "pick") return (ans[item.id] || []).length === item.max ? 1 : 0;
    if (item.kind === "check") return 1;
    return ans[item.id] !== undefined ? 1 : 0;
  };
  const doneUnits = SECTIONS.reduce((s, sec) => s + sec.items.reduce((t, i) => t + answeredUnits(i), 0), 0);

  const sectionRemaining = (sec) => sec.items.reduce((t, i) => t + (units(i) - answeredUnits(i)), 0);

  const results = useMemo(() => (stage === "results" ? computeResults(ans) : null), [stage, ans]);

  const renderItem = (item) => {
    switch (item.kind) {
      case "likert": return <LikertItem key={item.id} item={item} value={ans[item.id]} onSet={(v) => set(item.id, v)} />;
      case "rate": return <RateItem key={item.id} item={item} value={ans[item.id]} onSet={(v) => set(item.id, v)} />;
      case "single": return <SingleItem key={item.id} item={item} value={ans[item.id]} onSet={(v) => set(item.id, v)} />;
      case "pick": return <PickItem key={item.id} item={item} value={ans[item.id]} onSet={(v) => set(item.id, v)} />;
      case "flex": return <FlexItem key={item.id} item={item} imp={ans[item.id + "_imp"]} flex={ans[item.id + "_flex"]} onSet={set} />;
      case "check": return <CheckItem key={item.id} item={item} sel={ans.db_sel} abs={ans.db_abs} onSel={(v) => set("db_sel", v)} onAbs={(v) => set("db_abs", v)} />;
      default: return null;
    }
  };

  const shell = (children) => (
    <div className="rnp" style={{ minHeight: "100vh", background: C.bg, padding: "0 0 60px" }}>
      <style>{STYLES}</style>
      <div style={{ maxWidth: 620, margin: "0 auto", padding: "20px 16px" }}>{children}</div>
    </div>
  );

  if (stage === "intro") {
    return shell(
      <div className="fadein" style={{ paddingTop: 40 }}>
        <div style={{ border: `1px solid ${C.line}`, borderRadius: 3, padding: "26px 22px", background: C.panel }}>
          <div style={{ fontFamily: MONO, fontSize: 11, letterSpacing: 4, color: C.dim }}>FORM RNP-1</div>
          <div style={{ fontFamily: MONO, fontSize: 30, letterSpacing: 2, color: C.olive, fontWeight: 700, margin: "10px 0 6px", lineHeight: 1.15 }}>
            RELATIONSHIP NEEDS PROFILE
          </div>
          <div style={{ fontFamily: MONO, fontSize: 10.5, letterSpacing: 2, color: C.coyote, marginBottom: 20 }}>
            10 SECTIONS · {totalUnits} ITEMS · 25–30 MIN
          </div>
          <div style={{ fontFamily: BODY, fontSize: 14.5, color: C.ink, lineHeight: 1.7, marginBottom: 18 }}>
            One pass through the full stack: how you bond, what the relationship must feed, how your desire actually works,
            what pulls you, where your lines are. Output is a dossier — an archetype, a model statement, and a YAML block
            for your vault.
          </div>
          <div style={{ fontFamily: MONO, fontSize: 11, color: C.dim, lineHeight: 2.1, letterSpacing: 1, borderTop: `1px solid ${C.line}`, paddingTop: 14 }}>
            → ANSWER FROM HISTORY, NOT ASPIRATION<br />
            → PATTERN BEATS PREFERENCE<br />
            → NOTHING LEAVES THIS SCREEN UNLESS YOU EXPORT IT
          </div>
          <button onClick={() => setStage(0)} style={{
            marginTop: 22, width: "100%", padding: "15px 0", borderRadius: 3, cursor: "pointer",
            fontFamily: MONO, fontSize: 13, letterSpacing: 4, fontWeight: 700,
            background: C.olive, color: C.bg, border: "none",
          }}>BEGIN</button>
        </div>
        <div style={{ fontFamily: BODY, fontSize: 11.5, color: C.dim, lineHeight: 1.6, marginTop: 14 }}>
          Original items modeled on established constructs. Self-reflection instrument, not a clinical or diagnostic measure.
        </div>
      </div>
    );
  }

  if (stage === "results" && results) {
    return shell(<Results r={results} onRevise={() => setStage(0)} onReset={() => { setAns({}); setStage("intro"); }} />);
  }

  const sec = SECTIONS[stage];
  const remaining = sectionRemaining(sec);
  const last = stage === SECTIONS.length - 1;

  return shell(
    <div className="fadein" key={sec.code}>
      <div style={{ position: "sticky", top: 0, background: C.bg, padding: "10px 0 12px", zIndex: 5 }}>
        <div style={{ display: "flex", justifyContent: "space-between", fontFamily: MONO, fontSize: 10, letterSpacing: 2, color: C.dim, marginBottom: 6 }}>
          <span>SECTION {sec.code}/10</span><span>ITEMS {doneUnits}/{totalUnits}</span>
        </div>
        <div style={{ height: 3, background: C.line, borderRadius: 2 }}>
          <div style={{ width: Math.round((doneUnits / totalUnits) * 100) + "%", height: "100%", background: C.olive, borderRadius: 2 }} />
        </div>
      </div>

      <div style={{ margin: "14px 0 6px" }}><Stamp code={sec.code} name={sec.name} /></div>
      <div style={{ fontFamily: BODY, fontSize: 13.5, color: C.dim, lineHeight: 1.6, margin: "10px 0 6px" }}>{sec.blurb}</div>

      <div>{sec.items.map(renderItem)}</div>

      <div style={{ display: "flex", gap: 10, marginTop: 22 }}>
        <button onClick={() => setStage(stage === 0 ? "intro" : stage - 1)} style={{
          padding: "13px 18px", borderRadius: 3, cursor: "pointer", fontFamily: MONO, fontSize: 11,
          letterSpacing: 2, background: "transparent", color: C.dim, border: `1px solid ${C.line}`,
        }}>BACK</button>
        <button
          disabled={remaining > 0}
          onClick={() => setStage(last ? "results" : stage + 1)}
          style={{
            flex: 1, padding: "13px 0", borderRadius: 3, fontFamily: MONO, fontSize: 12, letterSpacing: 3, fontWeight: 700,
            cursor: remaining > 0 ? "not-allowed" : "pointer",
            background: remaining > 0 ? C.panel2 : C.olive,
            color: remaining > 0 ? C.dim : C.bg,
            border: `1px solid ${remaining > 0 ? C.line : C.olive}`,
          }}>
          {remaining > 0 ? remaining + " REMAINING" : last ? "COMPILE DOSSIER" : "CONTINUE"}
        </button>
      </div>
    </div>
  );
}
