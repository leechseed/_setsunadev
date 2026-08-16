---
original_path: "/mnt/user-data/outputs/relationship-needs-profiler.jsx"
source_conversation: "Male romantic relationship profiling questionnaires"
created: 2026-07-15
trunk: ORANGE
kind: generated-file
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
