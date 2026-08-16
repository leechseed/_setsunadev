---
original_path: "/home/claude/glute-doctrine.jsx"
source_conversation: "Daily glute activation routine for aesthetic results"
created: 2026-07-11
trunk: BLACK
kind: generated-file
---

import React, { useEffect, useMemo, useRef, useState } from "react";

/* ============================================================
   GLUTE DOCTRINE · GD-1
   4-phase build program tracker · field-manual style
   ============================================================ */

const STYLES = `
@import url('https://fonts.googleapis.com/css2?family=Barlow+Condensed:wght@500;600;700&display=swap');
:root{
  --bg:#0d0f0a; --panel:#14170e; --panel2:#0a0c07; --line:#2b301f;
  --ink:#e2e5d3; --mut:#8f977c; --olive:#a7bc5b; --olive-dim:#5d6b3c;
  --coyote:#c49a6c;
}
*{box-sizing:border-box}
html,body{margin:0;background:var(--bg)}
.gd{min-height:100vh;background:var(--bg);color:var(--ink);
  font:13.5px/1.5 ui-monospace,'SF Mono',Menlo,Consolas,'Liberation Mono',monospace;
  padding-bottom:96px;-webkit-font-smoothing:antialiased}
.wrap{max-width:560px;margin:0 auto;padding:0 14px}
.strip{display:flex;justify-content:space-between;align-items:center;
  border-bottom:1px solid var(--line);padding:9px 14px;font-size:10px;
  letter-spacing:.16em;color:var(--mut);text-transform:uppercase}
.strip b{color:var(--olive);font-weight:400}
.h1{font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:36px;
  letter-spacing:.05em;line-height:.95;margin:18px 0 3px;text-transform:uppercase}
.h1 span{color:var(--olive)}
.sub{font-size:10px;letter-spacing:.18em;color:var(--mut);text-transform:uppercase;margin-bottom:6px}
.pillrow{display:flex;gap:6px;margin:10px 0 2px;flex-wrap:wrap}
.pill{border:1px solid var(--line);padding:3px 9px;font-size:10px;
  letter-spacing:.14em;color:var(--olive);text-transform:uppercase}
.pill.coy{color:var(--coyote)}
.seg{display:flex;gap:6px;margin:14px 0 4px}
.seg button{flex:1;background:var(--panel);border:1px solid var(--line);color:var(--mut);
  font-family:'Barlow Condensed',sans-serif;font-weight:600;font-size:15px;letter-spacing:.12em;
  padding:9px 0;cursor:pointer}
.seg button.on{border-color:var(--olive);color:var(--olive);background:rgba(167,188,91,.07)}
.seglbl{font-size:9px;letter-spacing:.2em;color:var(--mut);text-transform:uppercase;margin-top:12px}
.card{position:relative;background:var(--panel);border:1px solid var(--line);
  padding:13px 14px;margin:12px 0}
.ticks::before{content:'';position:absolute;top:-1px;left:-1px;width:11px;height:11px;
  border-top:2px solid var(--olive);border-left:2px solid var(--olive)}
.ticks::after{content:'';position:absolute;bottom:-1px;right:-1px;width:11px;height:11px;
  border-bottom:2px solid var(--olive);border-right:2px solid var(--olive)}
.chead{display:flex;align-items:baseline;gap:8px;margin-bottom:4px;flex-wrap:wrap}
.code{font-size:9px;letter-spacing:.16em;color:var(--coyote);border:1px solid var(--line);
  padding:2px 6px;white-space:nowrap}
.ctitle{font-family:'Barlow Condensed',sans-serif;font-weight:600;font-size:18px;
  letter-spacing:.09em;text-transform:uppercase}
.time{margin-left:auto;font-size:9px;color:var(--mut);letter-spacing:.14em;white-space:nowrap}
.tgt{font-size:10px;color:var(--mut);letter-spacing:.06em;margin:-2px 0 6px}
.ck{display:flex;gap:10px;padding:8px 0;width:100%;background:none;border:0;
  border-top:1px dashed var(--line);color:var(--ink);text-align:left;cursor:pointer;
  font:inherit;align-items:flex-start}
.ck .box{width:15px;height:15px;border:1px solid var(--mut);flex:none;margin-top:2px;
  display:grid;place-items:center;font-size:9px;color:var(--olive)}
.ck.on .box{border-color:var(--olive);background:rgba(167,188,91,.14)}
.ck.on .lbl{color:var(--mut)}
.ck .sub2{display:block;font-size:10.5px;color:var(--mut);margin-top:1px}
.exrow{display:flex;align-items:center;gap:9px;padding:9px 0;border-top:1px dashed var(--line)}
.exmain{flex:1;min-width:0}
.exnote{font-size:10.5px;color:var(--mut)}
.hint{font-size:9px;color:var(--mut);text-align:right;line-height:1.35;width:62px;flex:none}
input.rep{width:84px;background:var(--panel2);border:1px solid var(--line);color:var(--coyote);
  padding:8px;font:inherit;font-size:13px;text-align:right;flex:none}
input.rep:focus{outline:none;border-color:var(--olive)}
input.note,textarea.note{width:100%;background:var(--panel2);border:1px solid var(--line);
  color:var(--ink);padding:9px;font:inherit;font-size:12.5px}
input.note:focus{outline:none;border-color:var(--olive)}
.daychips{display:flex;gap:6px;margin:8px 0 2px}
.dchip{flex:1;background:var(--panel2);border:1px solid var(--line);color:var(--mut);
  font:inherit;font-size:10px;letter-spacing:.1em;padding:7px 2px;cursor:pointer;
  text-transform:uppercase;position:relative}
.dchip.on{border-color:var(--coyote);color:var(--coyote);background:rgba(196,154,108,.08)}
.dchip .nx{position:absolute;top:-7px;right:4px;font-size:8px;letter-spacing:.12em;
  color:var(--olive);background:var(--panel);padding:0 3px}
.btn{display:block;width:100%;background:var(--olive);color:#10130a;border:0;
  font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:17px;
  letter-spacing:.22em;padding:13px;cursor:pointer;text-transform:uppercase;margin:16px 0 4px}
.btn:active{transform:translateY(1px)}
.stampwrap{text-align:center;margin:18px 0 4px}
.stamp{display:inline-block;border:2px solid var(--coyote);color:var(--coyote);
  font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:19px;
  letter-spacing:.3em;padding:7px 16px 7px 19px;transform:rotate(-4deg);
  text-transform:uppercase;animation:stamp .3s cubic-bezier(.2,1.4,.4,1)}
@keyframes stamp{from{transform:scale(1.7) rotate(-15deg);opacity:0}
  to{transform:scale(1) rotate(-4deg);opacity:1}}
.undo{background:none;border:0;color:var(--mut);font:inherit;font-size:10px;
  letter-spacing:.14em;text-decoration:underline;cursor:pointer;display:block;margin:6px auto 0}
.nav{position:fixed;bottom:0;left:0;right:0;background:rgba(13,15,10,.97);
  border-top:1px solid var(--line);display:flex;z-index:50;backdrop-filter:blur(5px)}
.nav button{flex:1;padding:9px 0 11px;background:none;border:0;color:var(--mut);
  font:inherit;font-size:9px;letter-spacing:.16em;cursor:pointer;text-transform:uppercase}
.nav button .num{display:block;font-family:'Barlow Condensed',sans-serif;font-size:17px;
  font-weight:700;letter-spacing:.06em;margin-bottom:1px}
.nav button.act{color:var(--olive);box-shadow:inset 0 2px 0 var(--olive)}
.acc{background:var(--panel);border:1px solid var(--line);margin:10px 0}
.acch{display:flex;align-items:baseline;gap:8px;width:100%;background:none;border:0;
  color:var(--ink);font:inherit;padding:12px 14px;cursor:pointer;text-align:left}
.acch .chev{margin-left:auto;color:var(--mut);font-size:11px;transition:transform .15s}
.acc.open .chev{transform:rotate(90deg)}
.accb{padding:2px 14px 14px;border-top:1px dashed var(--line)}
.dh{font-size:10px;letter-spacing:.2em;color:var(--olive);text-transform:uppercase;margin:13px 0 5px}
.dp{margin:8px 0;color:var(--ink)}
.dli{display:flex;gap:9px;padding:5px 0;color:var(--ink)}
.dli::before{content:'▸';color:var(--olive-dim);flex:none}
.big{font-family:'Barlow Condensed',sans-serif;font-weight:700;font-size:54px;line-height:.9}
.statrow{display:flex;gap:10px}
.stat{flex:1;background:var(--panel);border:1px solid var(--line);padding:12px 13px}
.stat .lb{font-size:9px;letter-spacing:.18em;color:var(--mut);text-transform:uppercase}
.bars{display:flex;gap:3px;align-items:flex-end;height:32px;margin-top:6px}
.bar{width:9px;background:var(--coyote);min-height:2px}
.bar.last{background:var(--olive)}
.prow{display:flex;align-items:flex-end;gap:10px;padding:10px 0;border-top:1px dashed var(--line)}
.pmeta{font-size:10px;color:var(--mut);text-align:right;line-height:1.5;white-space:nowrap}
.pmeta b{color:var(--coyote);font-weight:400}
.mut{color:var(--mut)}
.small{font-size:10.5px}
.footer{margin:26px 0 8px;font-size:9px;letter-spacing:.18em;color:var(--olive-dim);
  text-transform:uppercase;text-align:center}
button:focus-visible,input:focus-visible{outline:2px solid var(--olive);outline-offset:2px}
@media (prefers-reduced-motion: reduce){*{animation:none!important;transition:none!important}}
`;

/* ---------------- PROGRAM DATA ---------------- */

const P2_DAYS = {
  A: { code: "DAY-A", name: "PROJECTION", tgt: "glute max", ex: [
    { id: "bridge",  n: "Glute bridge",     s: "2-s squeeze · single-leg past 30" },
    { id: "frog",    n: "Frog pumps",       s: "soles together, knees flared" },
    { id: "rlunge",  n: "Reverse lunge",    s: "per leg" } ] },
  B: { code: "DAY-B", name: "SHELF", tgt: "glute med / min", ex: [
    { id: "sraise",  n: "Side-lying raise", s: "toe down · slow" },
    { id: "pclam",   n: "Paused clamshell", s: "hold at top" },
    { id: "hydrant", n: "Fire hydrant",     s: "" },
    { id: "hike",    n: "Hip hike",         s: "to failure" } ] },
  C: { code: "DAY-C", name: "SUPPORT", tgt: "hams · adductors · balance", ex: [
    { id: "llb",     n: "Long-lever bridge", s: "feet far out" },
    { id: "cossack", n: "Cossack squat",     s: "feeds wine range" },
    { id: "slrdl",   n: "SL-RDL reach",      s: "balance lights med/min" } ] }
};

const P3_DAYS = {
  A: { code: "LD-A", name: "HINGE", tgt: "posterior power", ex: [
    { id: "kbrdl",    n: "KB Romanian DL",      s: "log wt × reps" },
    { id: "swing",    n: "KB swing",            s: "snap the hips" },
    { id: "thrust",   n: "Hip thrust",          s: "plate → couch-back" } ] },
  B: { code: "LD-B", name: "LATERAL", tgt: "shelf under load", ex: [
    { id: "monster",  n: "Monster walk",        s: "banded · steps/side" },
    { id: "awraise",  n: "Ankle-wt side raise", s: "toe down" },
    { id: "pcossack", n: "Plate cossack",       s: "" } ] },
  C: { code: "LD-C", name: "SQUAT / LUNGE", tgt: "legs to match", ex: [
    { id: "goblet",   n: "Goblet squat",        s: "" },
    { id: "kblunge",  n: "KB reverse lunge",    s: "per leg" },
    { id: "lslrdl",   n: "SL-RDL",              s: "loaded" } ] }
};

const EXMETA = {};
[P2_DAYS, P3_DAYS].forEach(g => Object.values(g).forEach(d => d.ex.forEach(e => { EXMETA[e.id] = e.n; })));

const STRETCH = {
  p2: ["Low lunge — 90 s / side", "Half-split — 90 s / side", "Lizard — 60 s / side", "Pigeon — 90 s / side"],
  p3x: ["Weighted cossack — 8 / side", "Jefferson curl — light × 8", "Horse stance — 60 s", "Bridge push-up progression"],
  p4: ["Front split square-off — 2 × 2 min / side", "Middle split — 2 min", "Cobra → camel → arch flow × 5", "Pigeon — 90 s / side"]
};

const KIT = [
  { id: "bands",  n: "Mini loop bands × 3",   s: "light / med / heavy" },
  { id: "long",   n: "41-inch long band",     s: "tree anchor — pull-throughs · kickbacks · rows" },
  { id: "slider", n: "Sliders (or 2 towels)", s: "leg curls · copenhagens" },
  { id: "ankle",  n: "Ankle weights · 5 lb",  s: "side raises" },
  { id: "mat",    n: "Foldable mat",          s: "" },
  { id: "kb",     n: "Kettlebell",            s: "rides in the car, not the bag" },
  { id: "pf",     n: "PF biofeedback trainer", s: "optional · pelvic floor cueing" }
];

const GRAD = {
  1: ["10 clean single-cheek squeezes / side — standing, no hip shift",
      "60-second max squeeze — no shake",
      "Bridges feel 90% glute"],
  2: ["15+ single-leg bridges / side",
      "Cossack squats smooth, full depth"],
  3: ["Loaded hip thrust owned through a full 8 → 15 cycle",
      "Power tier clean — wall twerk + drop transitions"],
  4: ["Front splits square",
      "Arch on command inside floor work",
      "3 monthly photo checks logged"]
};

const DOCTRINE = [
  { code: "PH-1", t: "ACTIVATION BOOTCAMP", tag: "WK 1–3 · NEURAL, NOT MUSCULAR", grad: 1, rows: [
    { p: "Goal: fire every muscle on command, independently. Frequency beats intensity — the floor runs twice a day, and the failure block waits." },
    { h: "PROTOCOL" },
    { li: [
      "Daily floor × 2/day — pelvic tilts · single-cheek squeezes · max hold",
      "Isolation lab × 2/day — hip hikes · toe-down raises · clam pulses",
      "Deep six rotators — figure-4 squeezes · clamshell holds",
      "Pelvic floor — 10 kegel + 10 reverse per session (biofeedback trainer optional)",
      "Mobility floor daily — CARs · 90/90 · deep squat 5 min · couch stretch · cat-cow" ] },
    { h: "DANCE TIER — THE POP" },
    { p: "Single-cheek pops on beat · pelvic tilt in rhythm · slow wine. This IS the activation curriculum with a beat under it." } ] },

  { code: "PH-2", t: "BODYWEIGHT BASE", tag: "WK 3–8 · 20-MIN DAILY", grad: 2, rows: [
    { p: "Full-intensity failure blocks unlock. A / B / C rotation — each group gets hit hard every third day, which is better for growth than every other." },
    { li: [
      "BLK-01 groove warm-up · 4 min",
      "BLK-02 isolation lab · 5 min",
      "BLK-03 failure — A projection / B shelf / C support",
      "BLK-04 one-song finisher · 3 min",
      "Splits track × 3/wk — evenings, 15 min, warm tissue" ] },
    { h: "THE 30-REP RULE" },
    { p: "Past 30 clean reps: harder, not longer. Single-leg → 3-second negatives → pauses. Past 30 you are building endurance, not size." },
    { h: "DANCE TIER — THE BOUNCE" },
    { p: "Standing twerk basics · hands-on-knees · knees drive rhythm while glutes pop on top. One-song survival finishers." } ] },

  { code: "PH-3", t: "LOAD", tag: "WK 8+ · KB + PLATES OFF THE BENCH", grad: 3, rows: [
    { li: [
      "LD-A HINGE — KB RDL · swings · plate bridge → couch hip thrust",
      "LD-B LATERAL — banded monster walks · ankle-weight raises · plate cossacks",
      "LD-C SQUAT / LUNGE — goblet · KB reverse lunge · SL-RDL" ] },
    { h: "DOUBLE PROGRESSION" },
    { p: "Own 8 → build to 15 → add weight → drop back to 8. Log weight × reps — the failure log carries straight over." },
    { h: "LOADED FLEX" },
    { li: ["Weighted cossacks push middle-split range with strength behind it",
      "Jefferson curls — light — full spinal articulation",
      "Horse stance holds", "Bridge push-up progressions open the backbend line"] },
    { h: "DANCE TIER — POWER" },
    { p: "Squat-hold twerk · drop transitions (up-downs) · wall twerk. Strength moves wearing a costume — you cannot wall twerk without the hip extension the kettlebell just built." } ] },

  { code: "PH-4", t: "AESTHETIC SCULPT", tag: "WK 16+ · RATIO OVER MASS", grad: 4, rows: [
    { p: "The question shifts from is-it-growing to is-it-growing-in-the-right-proportions. Three levers:" },
    { li: [
      "Waist: ZERO loaded oblique work — vacuums · dead bugs · planks only. The waist staying tight makes the glutes read twice as big",
      "Under-butt fold: slider leg curls · Nordic negatives · back-extension squeezes — the line between big and shelf-with-a-shadow",
      "Quads at minimum effective volume — heel-drive step-ups, no heavy front-loaded squats",
      "Adductors: cossacks + copenhagen planks — inner-thigh line smooth and tight",
      "Pump finishers: banded everything · 20–30 reps · metabolic roundness",
      "V-taper: band pulldowns + rows off the tree anchor — waist reads smaller, hips wider, from the money angle",
      "Slight deficit now reveals what three phases built" ] },
    { h: "TRACKING" },
    { p: "Monthly fixed-angle photo — same spot, same light. Numbers say the engine grew; the camera says the silhouette lands." },
    { h: "DANCE TIER — PERFORMANCE" },
    { p: "Floor work · shaking vs popping as separate skills · one-cheek isolation on beat · combos and transitions. Splits and arch inside the choreography is the finished product." } ] },

  { code: "MM-01", t: "MIND-MUSCLE PLAYBOOK", tag: "HOW TO WIRE THE CONNECTION", rows: [
    { li: [
      "Hands on — palpate the muscle you are firing. Skin-to-brain feedback shortcuts the learning",
      "Squeeze before you move — own the static contraction, then add motion. Contraction leads, movement follows",
      "Light + slow only — heavy load recruits everything and teaches nothing. 3–5 s peak holds every rep",
      "Internal cues — crush a walnut · close the left cheek. At light loads internal focus measurably boosts activation",
      "Hunt compensators — see FL-01",
      "Find the lazy cheek — everyone has one that fires late. It gets an extra set of everything until even" ] } ] },

  { code: "DN-01", t: "DANCE LADDER", tag: "BOLTED TO EACH PHASE", rows: [
    { li: [
      "PH-1 · CONTROL — the pop. Cheek pops on beat, tilt in rhythm, slow wine",
      "PH-2 · ENDURANCE — the bounce. Standing basics, one-song survival",
      "PH-3 · POWER — squat-hold, drops, wall twerk",
      "PH-4 · PERFORMANCE — floor work, shake vs pop, one-cheek on beat, full combos" ] },
    { p: "The dance tier always replaces the finisher block — baked into the 20 minutes, never stacked on top." } ] },

  { code: "FX-01", t: "FLEXIBILITY LADDER", tag: "MOBILITY FIRST, THEN RANGE", rows: [
    { li: [
      "PH-1 · MOBILITY — hip CARs (the slow wine) · 90/90 · deep squat accumulation to 5 min · couch stretch · cat-cow",
      "PH-2 · PASSIVE — splits track opens: low lunge, half-split, lizard, pigeon. 60–90 s holds, 3 evenings/wk on warm tissue",
      "PH-3 · LOADED — weighted cossacks · light Jefferson curls · horse stance · bridge push-ups",
      "PH-4 · PERFORMANCE — splits square off, arch becomes a pose you own: cobra → camel → full arch on command" ] },
    { h: "HONEST TIMELINE" },
    { p: "Front splits: 6–12 months of consistency for most adults. Middle splits: longer, and some hip anatomies never square flat — front splits lead because they are the guaranteed win." },
    { p: "Tight hip flexors literally inhibit glutes (reciprocal inhibition) — the couch stretch makes the activation work better. Flexibility is not a side quest; in a lineup, movement is the top-two ticket." } ] },

  { code: "FL-01", t: "COACHING FLAGS", tag: "WHEN IT FEELS WRONG", rows: [
    { li: [
      "Front-hip burn on any abduction = TFL stealing the rep → toe down, angle the leg slightly behind you",
      "Hamstrings cramp on bridges → heels closer, tilt the pelvis first",
      "Never grind past 30 — upgrade the movement instead",
      "Daily true failure on the same muscles just cooks you — the rotation IS the recovery plan" ] } ] },

  { code: "NU-01", t: "FUEL", tag: "FLAT-TO-BUILT REQUIRES EATING FOR IT", rows: [
    { li: [
      "~1 g protein per lb bodyweight, daily",
      "Small surplus through PH-1 → PH-3 — the build phases",
      "Slight deficit in PH-4 to reveal the shape",
      "Kitchen access makes this the easiest part of the whole program" ] } ] },

  { code: "TB-01", t: "TARGET BUILD", tag: "THE NORTH STAR", rows: [
    { p: "Compact and exaggerated, tuned for a 5'6\" low-center-of-gravity frame: full bubble projection + hard shelf, proportional thigh thickness (slim-thick reads wrong on a stocky frame — proportional reads right), V-taper from behind, moderate body fat over striation — full and soft-over-muscle beats lean and shredded in this lane." },
    { p: "The strategic read: in a lineup of ten, most will have an ass. Almost nobody can drop a full split, survive a whole track in a deep squat, and arch on command. Movement is the differentiator." } ] }
];

/* ---------------- HELPERS ---------------- */

const dkey = (d = new Date()) =>
  `${d.getFullYear()}-${String(d.getMonth() + 1).padStart(2, "0")}-${String(d.getDate()).padStart(2, "0")}`;

const fmtDate = (d = new Date()) =>
  d.toLocaleDateString("en-US", { weekday: "short", month: "short", day: "numeric", year: "numeric" }).toUpperCase();

const lastNum = v => {
  const m = String(v || "").match(/(\d+(?:\.\d+)?)(?!.*\d)/);
  return m ? +m[1] : null;
};

function calcStreak(logs) {
  let s = 0;
  const d = new Date();
  if (!(logs[dkey(d)] || {}).done) d.setDate(d.getDate() - 1);
  while ((logs[dkey(d)] || {}).done) { s++; d.setDate(d.getDate() - 1); }
  return s;
}

function suggestDay(logs) {
  const dates = Object.keys(logs).filter(k => logs[k] && logs[k].day).sort().reverse();
  const today = dkey();
  for (const k of dates) {
    if (k === today) continue;
    const last = logs[k].day;
    return last === "A" ? "B" : last === "B" ? "C" : "A";
  }
  return "A";
}

function buildBlocks(ph, stretchDay, dayOfMonth) {
  if (ph === 1) {
    const ses = [
      "Pelvic tilts — 20 slow · 20 fast",
      "Single-cheek squeezes — 20 / side",
      "Max squeeze hold — 60 s",
      "Standing hip hikes — 15 / side",
      "Toe-down side raise — 12 / side · slow",
      "Clamshell pulses — 15 / side",
      "Pelvic floor — 10 kegel · 10 reverse"];
    return [
      { code: "SES-01", t: "ACTIVATION — SESSION 1", time: "AM", type: "check", items: ses },
      { code: "SES-02", t: "ACTIVATION — SESSION 2", time: "PM", type: "check", items: ses },
      { code: "MOB-01", t: "MOBILITY FLOOR", time: "~8 MIN", type: "check", items: [
        "Hip CARs (slow wine) — 5 / direction",
        "90/90 transitions — × 10",
        "Deep squat hold — accumulate 5 min today",
        "Couch stretch — 60 s / side",
        "Cat-cow waves — × 10"] }
    ];
  }

  const wu = { code: "BLK-01", t: "GROOVE WARM-UP", time: "4 MIN", type: "check", items: [
    "Slow wine — 5 / direction · max range · 5 s per circle",
    "Figure-8s — 10 each way",
    "Body rolls — × 10 · wave finishes through the hips",
    "Pelvic tilts — 20 slow · 20 fast"] };

  const iso = { code: "BLK-02", t: "ISOLATION LAB", time: "5 MIN", type: "check", items: [
    "Single-cheek squeezes — 20 / side",
    "Standing hip hikes — 15 / side",
    "Toe-down side raise — 12 / side · slow",
    "Clamshell pulses — 15 / side"] };

  const log = { code: "BLK-03", t: ph >= 3 ? "LOAD BLOCK" : "FAILURE BLOCK",
    time: "8 MIN", type: "log", days: ph >= 3 ? P3_DAYS : P2_DAYS,
    ph, hint: ph >= 3 ? "24kg × 12" : "reps" };

  const fin = { code: "BLK-04", t: "FINISHER", time: "3 MIN", type: "check", items:
    ph === 2 ? ["One-song survival — squat-hold twerk OR wine ladder (30 s standing / half / deep · repeat)"] :
    ph === 3 ? ["POWER TIER — squat-hold twerk · drop transitions · wall twerk — one full track"] :
               ["PERFORMANCE — floor work · shake vs pop · one-cheek on beat — run the combo"] };

  const stretchItems = ph === 2 ? STRETCH.p2 : ph === 3 ? [...STRETCH.p2, ...STRETCH.p3x] : STRETCH.p4;
  const str = { code: "STR-01", t: "SPLITS TRACK", time: "15 MIN", type: "check",
    tag: stretchDay ? "SCHEDULED TONIGHT" : "OPTIONAL — SCHEDULED M · W · F",
    items: stretchItems };

  const blocks = [wu, iso, log];
  if (ph === 4) blocks.push({ code: "BLK-05", t: "SCULPT", time: "6 MIN", type: "check", items: [
    "Slider leg curls — × 12",
    "Nordic negatives — × 5",
    "Back-extension squeeze — × 15 (bench)",
    "Stomach vacuum — 5 × 10 s",
    "Copenhagen plank — 20 s / side",
    "Band row + pulldown — × 15 each",
    "Banded pump — pick one · 2 × 25"] });
  blocks.push(fin, str);
  if (ph === 4 && dayOfMonth <= 7) blocks.push({ code: "CHK-01", t: "MONTHLY PHOTO", time: "P4",
    type: "check", items: ["Fixed angle · same spot · same light — log it"] });
  return blocks;
}

/* ---------------- SMALL COMPONENTS ---------------- */

function Chk({ on, label, sub, onClick }) {
  return (
    <button className={"ck" + (on ? " on" : "")} onClick={onClick} aria-pressed={!!on}>
      <span className="box">{on ? "■" : ""}</span>
      <span className="lbl">{label}{sub ? <span className="sub2">{sub}</span> : null}</span>
    </button>
  );
}

function Head({ code, title, time, tag }) {
  return (
    <div>
      <div className="chead">
        <span className="code">{code}</span>
        <span className="ctitle">{title}</span>
        {time ? <span className="time">{time}</span> : null}
      </div>
      {tag ? <div className="tgt">{tag}</div> : null}
    </div>
  );
}

/* ---------------- MAIN APP ---------------- */

export default function GluteDoctrine() {
  const [ready, setReady] = useState(false);
  const [offline, setOffline] = useState(false);
  const [tab, setTab] = useState("today");
  const [phase, setPhase] = useState(1);
  const [logs, setLogs] = useState({});
  const [gobag, setGobag] = useState({});
  const [grad, setGrad] = useState({});
  const [openAcc, setOpenAcc] = useState("PH-1");
  const stateTimer = useRef(null);
  const logTimer = useRef(null);

  const store = typeof window !== "undefined" ? window.storage : null;

  /* load */
  useEffect(() => {
    (async () => {
      if (!store) { setOffline(true); setReady(true); return; }
      try {
        const r = await store.get("gd1-state");
        if (r && r.value) {
          const s = JSON.parse(r.value);
          if (s.phase) setPhase(s.phase);
          if (s.gobag) setGobag(s.gobag);
          if (s.grad) setGrad(s.grad);
        }
      } catch (e) { /* first run — no state yet */ }
      try {
        const r = await store.get("gd1-logs");
        if (r && r.value) setLogs(JSON.parse(r.value));
      } catch (e) { /* first run — no logs yet */ }
      setReady(true);
    })();
  }, []);

  /* save state */
  useEffect(() => {
    if (!ready || !store) return;
    clearTimeout(stateTimer.current);
    stateTimer.current = setTimeout(async () => {
      try { await store.set("gd1-state", JSON.stringify({ phase, gobag, grad })); }
      catch (e) { setOffline(true); }
    }, 500);
    return () => clearTimeout(stateTimer.current);
  }, [phase, gobag, grad, ready]);

  /* save logs */
  useEffect(() => {
    if (!ready || !store) return;
    clearTimeout(logTimer.current);
    logTimer.current = setTimeout(async () => {
      try { await store.set("gd1-logs", JSON.stringify(logs)); }
      catch (e) { setOffline(true); }
    }, 500);
    return () => clearTimeout(logTimer.current);
  }, [logs, ready]);

  /* today accessors */
  const tk = dkey();
  const today = logs[tk] || {};
  const patchToday = patch => setLogs(l => ({ ...l, [tk]: { ...(l[tk] || {}), ...patch, phase } }));

  const now = new Date();
  const stretchDay = [1, 3, 5].includes(now.getDay());
  const blocks = useMemo(() => buildBlocks(phase, stretchDay, now.getDate()), [phase, stretchDay]);
  const streak = useMemo(() => calcStreak(logs), [logs]);
  const totalDone = useMemo(() => Object.values(logs).filter(l => l && l.done).length, [logs]);
  const nextDay = useMemo(() => suggestDay(logs), [logs]);
  const activeDay = today.day || nextDay;

  const toggleItem = (code, i) => {
    const b = { ...(today.blocks || {}) };
    const arr = [...(b[code] || [])];
    arr[i] = !arr[i];
    b[code] = arr;
    patchToday({ blocks: b });
  };

  const setRep = (id, v) => patchToday({ reps: { ...(today.reps || {}), [id]: v } });

  const history = id => {
    const out = [];
    Object.keys(logs).sort().forEach(k => {
      if (k === tk) return;
      const v = logs[k] && logs[k].reps && logs[k].reps[id];
      if (v !== undefined && v !== "") out.push({ date: k, raw: v, num: lastNum(v) });
    });
    return out;
  };

  const gradFor = n => {
    const arr = grad[n] || [];
    return { done: GRAD[n].filter((_, i) => arr[i]).length, total: GRAD[n].length };
  };
  const toggleGrad = (n, i) => setGrad(g => {
    const arr = [...(g[n] || [])];
    arr[i] = !arr[i];
    return { ...g, [n]: arr };
  });

  if (!ready) return (
    <div className="gd"><style>{STYLES}</style>
      <div className="wrap" style={{ paddingTop: 80, textAlign: "center", color: "var(--mut)", letterSpacing: ".2em", fontSize: 11 }}>
        LOADING STORAGE…
      </div>
    </div>
  );

  /* ---------- views ---------- */

  const TodayView = (
    <div>
      <div className="seglbl">CURRENT PHASE</div>
      <div className="seg" role="group" aria-label="Phase select">
        {[1, 2, 3, 4].map(p => (
          <button key={p} className={phase === p ? "on" : ""} onClick={() => setPhase(p)}>PH-{p}</button>
        ))}
      </div>
      <div className="small mut" style={{ margin: "2px 0 4px" }}>
        {phase === 1 && "ACTIVATION BOOTCAMP — twice a day · failure block waits"}
        {phase === 2 && "BODYWEIGHT BASE — the 20-minute daily · A/B/C rotation"}
        {phase === 3 && "LOAD — KB + plates · double progression 8 → 15 → add"}
        {phase === 4 && "AESTHETIC SCULPT — ratio over mass · performance tier"}
      </div>

      {blocks.map(b => (
        <div className={"card" + (b.type === "log" ? " ticks" : "")} key={b.code}>
          <Head code={b.code} title={b.t} time={b.time} tag={b.tag || (b.type === "log" ? undefined : undefined)} />

          {b.type === "check" && b.items.map((it, i) => (
            <Chk key={i} on={(today.blocks || {})[b.code] && today.blocks[b.code][i]}
              label={it} onClick={() => toggleItem(b.code, i)} />
          ))}

          {b.type === "log" && (() => {
            const days = b.days;
            const d = days[activeDay];
            return (
              <div>
                <div className="daychips" role="group" aria-label="Rotation day">
                  {["A", "B", "C"].map(k => (
                    <button key={k} className={"dchip" + (activeDay === k ? " on" : "")}
                      onClick={() => patchToday({ day: k })}>
                      {days[k].code} · {days[k].name}
                      {nextDay === k && <span className="nx">NEXT</span>}
                    </button>
                  ))}
                </div>
                <div className="tgt">{d.tgt} — every entry to failure · log the number</div>
                {d.ex.map(e => {
                  const h = history(e.id);
                  const last = h.length ? h[h.length - 1].raw : "—";
                  const nums = h.map(x => x.num).filter(x => x !== null);
                  const best = nums.length ? Math.max(...nums) : "—";
                  return (
                    <div className="exrow" key={e.id}>
                      <div className="exmain">
                        <div>{e.n}</div>
                        {e.s ? <div className="exnote">{e.s}</div> : null}
                      </div>
                      <div className="hint">L {last}<br />B {best}</div>
                      <input className="rep" inputMode={phase >= 3 ? "text" : "numeric"}
                        placeholder={b.hint} value={(today.reps || {})[e.id] || ""}
                        onChange={ev => setRep(e.id, ev.target.value)}
                        aria-label={e.n + " result"} />
                    </div>
                  );
                })}
              </div>
            );
          })()}
        </div>
      ))}

      <div className="card">
        <Head code="FLD-01" title="FIELD NOTES" />
        <input className="note" placeholder="track survived · lazy cheek check · anything"
          value={today.note || ""} onChange={e => patchToday({ note: e.target.value })} />
      </div>

      {today.done ? (
        <div className="stampwrap">
          <span className="stamp">▪ LOGGED ▪</span>
          <button className="undo" onClick={() => patchToday({ done: false })}>undo</button>
        </div>
      ) : (
        <button className="btn" onClick={() => patchToday({ done: true })}>MARK DAY COMPLETE</button>
      )}
      <div className="footer">GD-1 · CONSISTENCY IS THE PROGRAM</div>
    </div>
  );

  const gp = gradFor(phase);
  const LogView = (
    <div>
      <div className="statrow" style={{ marginTop: 14 }}>
        <div className="stat"><div className="lb">STREAK</div><div className="big">{streak}<span style={{ fontSize: 20, color: "var(--mut)" }}> D</span></div></div>
        <div className="stat"><div className="lb">DAYS LOGGED</div><div className="big">{totalDone}</div></div>
        <div className="stat"><div className="lb">PHASE</div><div className="big" style={{ color: "var(--olive)" }}>{phase}</div></div>
      </div>

      <div className="card ticks">
        <Head code={"PH-" + phase} title="GRADUATION CHECK" time={gp.done + " / " + gp.total} />
        {GRAD[phase].map((c, i) => (
          <Chk key={i} on={(grad[phase] || [])[i]} label={c} onClick={() => toggleGrad(phase, i)} />
        ))}
        {gp.done === gp.total && phase < 4 && (
          <button className="btn" style={{ marginTop: 12 }} onClick={() => setPhase(phase + 1)}>
            ADVANCE TO PH-{phase + 1}
          </button>
        )}
      </div>

      <div className="card">
        <Head code="IDX-01" title="FAILURE INDEX" time="LAST 8" />
        {(() => {
          const rows = Object.keys(EXMETA).map(id => ({ id, h: history(id) })).filter(r => r.h.length);
          if (!rows.length) return (
            <div className="small mut" style={{ paddingTop: 8 }}>
              No failure data yet. PH-2 unlocks BLK-03 logging — every number you save lands here, with last / best and the trend.
            </div>
          );
          return rows.map(r => {
            const nums = r.h.map(x => x.num).filter(x => x !== null);
            const best = nums.length ? Math.max(...nums) : null;
            const lastRaw = r.h[r.h.length - 1].raw;
            const tail = nums.slice(-8);
            const mx = tail.length ? Math.max(...tail) : 1;
            return (
              <div className="prow" key={r.id}>
                <div style={{ flex: 1, minWidth: 0 }}>
                  <div>{EXMETA[r.id]}</div>
                  <div className="bars" aria-hidden="true">
                    {tail.map((v, i) => (
                      <div key={i} className={"bar" + (i === tail.length - 1 ? " last" : "")}
                        style={{ height: Math.max(2, Math.round((v / mx) * 32)) }} />
                    ))}
                  </div>
                </div>
                <div className="pmeta">LAST <b>{lastRaw}</b><br />BEST <b>{best !== null ? best : "—"}</b> · {r.h.length}×</div>
              </div>
            );
          });
        })()}
      </div>
      <div className="footer">NUMBERS SAY THE ENGINE GREW · THE CAMERA SAYS THE SILHOUETTE LANDS</div>
    </div>
  );

  const DoctrineView = (
    <div style={{ marginTop: 14 }}>
      {DOCTRINE.map(sec => {
        const open = openAcc === sec.code;
        return (
          <div className={"acc" + (open ? " open" : "")} key={sec.code}>
            <button className="acch" onClick={() => setOpenAcc(open ? null : sec.code)} aria-expanded={open}>
              <span className="code">{sec.code}</span>
              <span className="ctitle" style={{ fontSize: 16 }}>{sec.t}</span>
              <span className="chev">▸</span>
            </button>
            {open && (
              <div className="accb">
                <div className="tgt" style={{ marginTop: 8 }}>{sec.tag}</div>
                {sec.rows.map((r, i) => {
                  if (r.p) return <p className="dp" key={i}>{r.p}</p>;
                  if (r.h) return <div className="dh" key={i}>{r.h}</div>;
                  if (r.li) return <div key={i}>{r.li.map((x, j) => <div className="dli" key={j}>{x}</div>)}</div>;
                  return null;
                })}
                {sec.grad && (
                  <div>
                    <div className="dh">GRADUATION — CHECK TO PASS</div>
                    {GRAD[sec.grad].map((c, i) => (
                      <Chk key={i} on={(grad[sec.grad] || [])[i]} label={c} onClick={() => toggleGrad(sec.grad, i)} />
                    ))}
                  </div>
                )}
              </div>
            )}
          </div>
        );
      })}
      <div className="footer">DOCTRINE OVER MOTIVATION</div>
    </div>
  );

  const packed = KIT.filter(k => gobag[k.id]).length;
  const KitView = (
    <div>
      <div className="card ticks" style={{ marginTop: 14 }}>
        <Head code="BAG-01" title="GO BAG" time={packed + " / " + KIT.length + " IN BAG"} />
        <div className="tgt">~$45 all-in · any park bench = hip thrust station, step-up box, split-squat rack</div>
        {KIT.map(k => (
          <Chk key={k.id} on={!!gobag[k.id]} label={k.n} sub={k.s}
            onClick={() => setGobag(g => ({ ...g, [k.id]: !g[k.id] }))} />
        ))}
      </div>
      <div className="card">
        <Head code="BOM-01" title="BILL OF MATERIALS" time="PENDING" />
        <div className="small mut" style={{ paddingTop: 6 }}>
          Full BOM — brands, prices, where to buy — is the next build. Say the word and it slots in here.
        </div>
      </div>
      <div className="footer">THE WHOLE PROGRAM TRAVELS</div>
    </div>
  );

  return (
    <div className="gd">
      <style>{STYLES}</style>
      <div className="strip">
        <span>GD-1 // <b>GLUTE DOCTRINE</b></span>
        <span>{offline ? "STORAGE OFFLINE — SESSION ONLY" : fmtDate(now)}</span>
      </div>
      <div className="wrap">
        <div className="h1">GLUTE<span> DOCTRINE</span></div>
        <div className="sub">BUILD PROGRAM · FLAT → SHELF · V1.0</div>
        <div className="pillrow">
          <span className="pill">PH-{phase}</span>
          <span className="pill coy">STREAK {streak}D</span>
          {stretchDay && phase > 1 ? <span className="pill">STRETCH NIGHT</span> : null}
        </div>

        {tab === "today" && TodayView}
        {tab === "log" && LogView}
        {tab === "doctrine" && DoctrineView}
        {tab === "kit" && KitView}
      </div>

      <nav className="nav" aria-label="Sections">
        {[["today", "01", "TODAY"], ["log", "02", "LOG"], ["doctrine", "03", "DOCTRINE"], ["kit", "04", "KIT"]].map(([k, n, l]) => (
          <button key={k} className={tab === k ? "act" : ""} onClick={() => setTab(k)}>
            <span className="num">{n}</span>{l}
          </button>
        ))}
      </nav>
    </div>
  );
}
