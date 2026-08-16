---
original_path: "/home/claude/dpapp/src/test-entry.jsx"
source_conversation: "Unified profiler UI with markdown export"
created: 2026-07-15
trunk: BOTH
kind: generated-file
---

import { renderToString } from "react-dom/server";
import { App, buildUnified } from "./main.jsx";
import MissionControl, { freshMc, mcMarkdown, computeObjective, doneCount, coachSystem } from "./mc.jsx";
import SexMenuProfiler, { computeResults as smpResults, buildExport, TOTAL_ITEMS } from "./smp.jsx";
import RelationshipNeedsProfiler, { computeResults as rnpResults, buildYaml, modelStatement, progressUnits } from "./rnp.jsx";

let pass = 0, fail = 0;
const ok = (cond, name) => { if (cond) { pass++; console.log("  ✓ " + name); } else { fail++; console.log("  ✗ FAIL: " + name); } };

// ---- sample data ----
const mc = freshMc();
mc.done["t1.inventory"] = true;
mc.notes.t1 = "22 items dumped; themes: being wanted, surrender";
mc.quiz.blueprint = "Sexual 60 / Energetic 20";
mc.done["t2.blueprint"] = true;
mc.syn.feel = ["desired", "surrender", "power", "", ""];
mc.syn.delivery = "desired: initiation, verbal wanting";
mc.ideas.push({ id: "i1", text: "revisit exhibitionism thread" });

const smp = {
  r_i33: "need", n_i33: "daily, non-negotiable",
  r_i49: "love", r_i345: "hard", n_i345: "not for me",
  r_i70: "try", r_i35: "occas", r_i26: "soft", r_i31: "indiff",
  q_q3: "wanted, consumed, safe",
  h_h1: "latex allergy",
};

const rnp = {
  a1: 4, a2: 4, a3: 3, a4: 2, a5: 4, a6: 3,
  v1: 2, v2: 2, v3: 2, v4: 1, v5: 2, v6: 2,
  n_aff: 9, n_sex: 8, n_des: 10, n_adm: 7, n_rec: 6, n_conv: 8, n_hon: 9,
  n_auto: 5, n_dom: 4, n_amb: 6, n_peace: 7, n_need: 8, n_grow: 7,
  crit: ["n_des", "n_sex", "n_hon"],
  e1: 4, e2: 5, e3: 4, e4: 5, p1: 3, p2: 4, p3: 3, c1: 4, c2: 5, c3: 5,
  ds1: 5, ds2: 3, ds3: 4,
  g_words: 7, g_time: 8, g_acts: 9, g_touch: 8, g_gifts: 4,
  r_words: 9, r_time: 7, r_acts: 6, r_touch: 8, r_gifts: 3,
  w_imp: 9, w_flex: 2, vt_imp: 8, vt_flex: 4, st_imp: 4, st_flex: 8,
  t1: 4, t2: 2, t3: 3, t4: 3, t5: 4, mirror: "blend",
  vals: ["freedom", "pleasure", "loyalty"], structure: "mono_open", d1: 4, d2: 3,
  conflict: "withdraw", repair: "talk", f1: 4, f2: 4, f3: 5,
  k1: 4, k2: 4, k3: 3, k4: 3,
  db_sel: ["Dishonesty or cheating", "Dead bedroom", "Contempt or disrespect"],
  db_abs: ["Dishonesty or cheating"],
};

console.log("== render smoke tests ==");
const appHtml = renderToString(<App />);
ok(appHtml.includes("BOOTING CONSOLE"), "App renders boot splash (pre-hydration)");

const stats = { smpRated: smpResults(smp).rated, smpTotal: TOTAL_ITEMS, rnpDone: progressUnits(rnp).done, rnpTotal: progressUnits(rnp).total };
const mcHtml = renderToString(<MissionControl mc={mc} patch={() => {}} stats={stats} goTab={() => {}} showToast={() => {}} />);
ok(mcHtml.includes("Current Objective"), "MissionControl renders status strip");
ok(mcHtml.includes("Erotic Journal") && mcHtml.includes("RNP-1"), "MissionControl renders stations incl. AUX");
ok(mcHtml.includes("DOCKED FORM · SMP-1"), "Tool 4 shows docked SMP line");
ok(mcHtml.includes("revisit exhibitionism thread"), "Parking lot renders ideas");

const smpHtml = renderToString(<SexMenuProfiler ans={smp} setAns={() => {}} />);
ok(smpHtml.includes("MENU SECTIONS"), "SMP with existing answers opens at hub (skips intro)");
const smpFresh = renderToString(<SexMenuProfiler ans={{}} setAns={() => {}} />);
ok(smpFresh.includes("FORM SMP-1"), "SMP fresh opens at intro");
ok(smpFresh.includes("AUTOSAVES TO THE CONSOLE"), "SMP intro copy updated for autosave");

const rnpHtml = renderToString(<RelationshipNeedsProfiler ans={rnp} setAns={() => {}} />);
ok(rnpHtml.includes("BONDING PATTERN"), "RNP with answers opens at section 01");
const rnpFresh = renderToString(<RelationshipNeedsProfiler ans={{}} setAns={() => {}} />);
ok(rnpFresh.includes("FORM RNP-1"), "RNP fresh opens at intro");

console.log("== builder tests ==");
const sr = smpResults(smp);
ok(sr.rated === 8, "SMP computeResults rated count = 8 (got " + sr.rated + ")");
const smd = buildExport(smp, sr);
ok(smd.includes("NON-NEGOTIABLES — NEED IT") && smd.includes("Kissing"), "SMP export lists NEED items");
ok(smd.includes("FULL MENU BY CATEGORY"), "SMP full export includes full menu");
const smdBrief = buildExport(smp, sr, { brief: true });
ok(!smdBrief.includes("FULL MENU BY CATEGORY"), "SMP brief export omits full menu");
ok(smdBrief.includes("HARD LIMITS"), "SMP brief export keeps limits");

const rr = rnpResults(rnp);
ok(typeof rr.archetype === "string" && rr.archetype.startsWith("THE "), "RNP archetype computed: " + rr.archetype);
const yaml = buildYaml(rr);
ok(yaml.includes("profile: romantic-needs-v1") && yaml.includes("Dishonesty or cheating   # ABSOLUTE"), "RNP YAML includes red lines + absolutes");
const stmt = modelStatement(rr);
ok(Array.isArray(stmt) && stmt.length >= 4, "RNP model statement has paragraphs (" + stmt.length + ")");
const pu = progressUnits(rnp);
ok(pu.done === pu.total, "RNP sample is fully answered: " + pu.done + "/" + pu.total);
ok(progressUnits({}).done === 0, "RNP empty progress = 0");

console.log("== unified archive ==");
const md = buildUnified({ mc, smp, rnp });
ok(md.includes("PART I — MISSION CONTROL"), "archive has Part I");
ok(md.includes("PART II — SEX MENU"), "archive has Part II");
ok(md.includes("PART III — RELATIONSHIP NEEDS"), "archive has Part III");
ok(md.includes("```yaml"), "archive embeds YAML block");
ok(md.includes("- [x] Turn-on inventory"), "archive carries tracker checkboxes");
ok(md.includes("**Archetype:** " + rr.archetype), "archive carries archetype");
const mdEmpty = buildUnified({ mc: freshMc(), smp: {}, rnp: {} });
ok(mdEmpty.includes("_Not started._"), "archive handles empty modules");
const brief = buildUnified({ mc, smp, rnp }, { brief: true });
ok(!brief.includes("FULL MENU BY CATEGORY"), "brief archive (kickoff) omits full menu");

const sys = coachSystem(mc, stats);
ok(sys.includes("SEX MENU station (SMP-1): 8/"), "coach system prompt carries live SMP stats");

console.log("\n--- unified archive preview (first 60 lines) ---");
console.log(md.split("\n").slice(0, 60).join("\n"));
console.log("\nRESULT: " + pass + " passed, " + fail + " failed");
process.exit(fail ? 1 : 0);
