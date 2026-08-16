---
original_path: "/mnt/user-data/outputs/bootycamp-tracker.jsx"
source_conversation: "Daily glute activation routine for aesthetic results"
created: 2026-07-11
trunk: BLACK
kind: generated-file
---

import { useState, useEffect, useRef, useMemo } from "react";

/* ============================================================
   GDP-1 · BOOTYCAMP — Glute Doctrine Publication 1
   Four-phase program tracker · field manual · progress log
   ============================================================ */

const KEY = "bootycamp:v1";
const todayISO = () => {
  const d = new Date();
  const off = d.getTimezoneOffset() * 60000;
  return new Date(d.getTime() - off).toISOString().slice(0, 10);
};
const NEXT_DAY = { A: "B", B: "C", C: "A" };

/* ---------------- PROGRAM DATA ---------------- */

const PHASE_META = {
  1: { code: "P1", name: "ACTIVATION BOOTCAMP", span: "WK 1–3", goal: "Fire every muscle on command, independently. Neural work — frequency beats intensity. Two short sessions daily, no failure block yet." },
  2: { code: "P2", name: "BODYWEIGHT BASE", span: "WK 3–8", goal: "The full 20-minute daily with failure blocks at full intensity. Past 30 clean reps → make it harder, never longer." },
  3: { code: "P3", name: "LOAD", span: "WK 8–16", goal: "Kettlebell + plates come off the bench. Double progression: own 8 reps, build to 15, add weight, drop back to 8." },
  4: { code: "P4", name: "AESTHETIC SCULPT", span: "WK 16+", goal: "Ratio over mass. Grow hips, guard the waist, carve the under-butt fold, build the V-taper. Camera becomes the metric." },
};

const FAILURE_PLANS = {
  2: {
    A: { name: "PROJECTION — GLUTE MAX", items: ["Glute bridge · 2s top squeeze", "Frog pumps", "Reverse lunge · weaker leg"] },
    B: { name: "SHELF — MED / MIN", items: ["Toe-down side raise · weaker side", "Paused clamshell · weaker side", "Fire hydrant · weaker side", "Hip hike · weaker side"] },
    C: { name: "SUPPORT CREW", items: ["Long-lever bridge (feet far out)", "Cossack squat · weaker side", "Single-leg RDL · weaker side"] },
  },
  3: {
    A: { name: "HINGE", items: ["KB Romanian deadlift", "KB swing", "Hip thrust · plate / couch-back"] },
    B: { name: "LATERAL", items: ["Monster walk · band series", "Side raise · ankle weight", "Cossack · loaded"] },
    C: { name: "SQUAT / LUNGE", items: ["Goblet squat", "KB reverse lunge", "Single-leg RDL · KB in hand"] },
  },
  4: {
    A: { name: "PROJECTION+", items: ["Hip thrust · heavy", "Frog pump burnout", "Step-up · heel drive, forward lean"] },
    B: { name: "SHELF + RATIO", items: ["Band lateral series", "Band row (tree / anchor)", "Band pulldown"] },
    C: { name: "FOLD + LINE", items: ["Sliding leg curl", "Nordic negative", "Back-extension squeeze", "Copenhagen plank · secs per side"] },
  },
};

const STRETCH_FOCUS = {
  1: "Mobility floor — hip CARs, 90/90, deep-squat accumulation, couch stretch",
  2: "Splits track — low lunge, half-split, lizard, pigeon · 60–90s holds",
  3: "Loaded — weighted cossack, light Jefferson curl, horse stance, bridge push-up",
  4: "Performance — square the splits, arch line: cobra → camel → full",
};

const GRAD = {
  1: [
    "10 clean single-cheek squeezes per side, standing, no hip shift",
    "60-second max squeeze hold, no shake-out",
    "Bridges feel ≥90% glute — no hamstring takeover",
  ],
  2: [
    "15+ single-leg bridges per side",
    "Cossack squats smooth and full-depth, both sides",
    "Every Block-3 lift progressed past the 30-rep ceiling at least once",
  ],
  3: [
    "Hip thrust: completed the 8→15 double progression twice (weight added ×2)",
    "Full band lateral series with zero TFL takeover",
    "Single-leg RDL smooth with KB in hand, both sides",
  ],
  4: [
    "Front split flat (or fist-height) both sides",
    "Deep-squat wine survives a full track, no breaks",
    "Arch on command — cobra → camel → full line",
    "Monthly photo / video check logged on schedule",
  ],
};

const MANUAL = [
  {
    t: "THE 20-MINUTE STRUCTURE",
    lines: [
      "B1 Groove warm-up (4 min) → B2 Isolation lab (5 min) → B3 Failure block (~8 min) → B4 One-song finisher (3 min).",
      "B1 + B2 run every single day. B3 rotates A / B / C. B4 is the dance tier for your current phase.",
      "Phase 1 exception: run B1 + B2 twice daily (AM + PM) and skip B3 entirely — activation is neural, not muscular.",
      "Dedicated stretch block: separate 15 min, 3 evenings per week, on warm tissue. The wind-down ritual.",
    ],
  },
  {
    t: "B1 — GROOVE WARM-UP",
    lines: [
      "Slow wine — 5 circles each direction, max range, ~5s per circle. Hands on head, upper body frozen: only the pelvis moves. That constraint is the skill. This is hip CARs in disguise.",
      "Figure-8s — 10 each way.",
      "Body rolls — 10, let the wave finish through the hips.",
      "Pelvic tilt isolations — 20 slow, 20 fast. This is the twerk mechanic.",
      "Mobility floor rides here: 90/90 transitions, deep-squat hold accumulation (build to 5 min total across the day), couch stretch — tight hip flexors inhibit glutes (reciprocal inhibition), so this makes everything downstream fire better.",
    ],
  },
  {
    t: "B2 — ISOLATION LAB",
    lines: [
      "Single-cheek squeezes — 20 per side. Builds the on-command isolation.",
      "Standing hip hikes — 15 per side. Drop one hip, lift with the standing-side glute med.",
      "Side-lying leg raise, toe pointed DOWN — 12 per side, slow. Internal rotation biases glute min. Honest note: min can't be fully isolated from med — toe-down + single-leg balance work is as close as it gets.",
      "Clamshell pulses — 15 per side. Deep six rotators.",
      "Pelvic floor set: kegels + reverse kegels folded into the daily floor. Biofeedback device counts as a legit tool here — it cues the exact contraction being trained.",
      "Not to failure. This block is practice, not punishment.",
    ],
  },
  {
    t: "B3 — FAILURE DOCTRINE",
    lines: [
      "Failure = technical failure: stop when form breaks, not when you collapse. The last clean rep is the number.",
      "Log the weaker side on unilateral moves. It sets the pace; the strong side matches, never exceeds by more than one set.",
      "30-rep rule: past 30 clean reps you're training endurance, not size. Make it harder — single-leg, 3-second negatives, pauses — and let the number reset.",
      "Phase 3+ progression is double progression: own 8, build to 15, add weight, drop to 8. Log as weight × reps.",
      "Red in this app means failure block. Nothing else gets that color.",
    ],
  },
  {
    t: "B4 — FINISHER",
    lines: [
      "Pick one track and survive it. The dance tier for your phase replaces this block — it is baked into the 20 minutes, never stacked on top.",
      "The wine ladder: standing wine 30s → half-squat wine 30s → deep-squat wine 30s, repeat until the song ends.",
      "Songs survived is a real metric. Log it.",
    ],
  },
  {
    t: "MIND-MUSCLE PLAYBOOK",
    lines: [
      "Hands on. Palpate the muscle you're firing — skin-to-brain feedback shortcuts the learning.",
      "Squeeze before you move. Own the static contraction first, then add movement with a pre-squeeze. Contraction leads, motion follows.",
      "Light and slow only. Heavy load recruits everything and teaches nothing. 3–5 second peak holds, every rep.",
      "Internal cues. 'Crush a walnut.' 'Close the left cheek.' At light loads, internal focus measurably boosts activation.",
      "Hunt compensators — see Compensation Fixes.",
      "Find the lazy cheek. One side fires late. It gets an extra set of everything until even.",
    ],
  },
  {
    t: "COMPENSATION FIXES",
    lines: [
      "Hamstrings cramping on bridges → heels closer to hips, tilt the pelvis before lifting.",
      "Burn on the FRONT of the hip during abduction → TFL is stealing the rep. Toe down, angle the leg slightly behind you, and it goes back to the glutes.",
      "Lower back working during tilts or bridges → shrink the range, re-find the tuck, rebuild from the squeeze.",
      "Sharp pain is a stop sign, not a rep. Ache and burn are workload; sharp and sudden is not.",
    ],
  },
  {
    t: "DANCE LADDER",
    lines: [
      "P1 · CONTROL — single-cheek pops on beat, pelvic tilt in rhythm, slow wine. The activation curriculum with a beat under it.",
      "P2 · ENDURANCE — standing twerk basics, hands-on-knees, knees drive rhythm while glutes pop on top. One-song survival.",
      "P3 · POWER — squat-hold twerk, drop transitions (up-downs), wall twerk. Strength moves wearing a costume.",
      "P4 · PERFORMANCE — floor work (all-fours, face-down), shaking vs popping as distinct skills, one-cheek isolation on beat, combos, splits and arch inside the choreography.",
    ],
  },
  {
    t: "FLEXIBILITY LADDER + SPLITS PROTOCOL",
    lines: [
      "P1 · MOBILITY — hip CARs (the slow wine), 90/90 transitions, deep-squat accumulation to 5 min/day, couch stretch, cat-cow spinal waves.",
      "P2 · PASSIVE — splits track opens: low lunge, half-split, lizard, pigeon. 60–90 second holds, 3 evenings a week, 15 min, on warm tissue after training.",
      "P3 · LOADED — weighted cossacks push middle-split range with strength behind it, light Jefferson curls, horse stance holds, bridge push-up progressions.",
      "P4 · PERFORMANCE — splits square off; the arch becomes a pose you own: cobra → camel → full arch on command, snapped into floor work.",
      "Honest timeline: front splits take most adults 6–12 months of consistency. Middle splits take longer and some hip anatomies never go flat — front splits are the guaranteed win, so they lead.",
    ],
  },
  {
    t: "BUILD BRIEF — MISSION SPEC",
    lines: [
      "Frame: 5'6\", stocky, low center of gravity. The build that wins is COMPACT AND EXAGGERATED — full bubble projection, hard shelf, thighs thick enough to match. Proportional thickness reads right on this frame; slim-thick reads wrong.",
      "V-taper from behind: band pulldowns and rows widen the lats, which makes the waist read smaller and hips wider from the money angle. Cheapest ratio hack on a short frame.",
      "Zero loaded oblique work — ever. Heavy side work thickens the waist and murders the ratio. Waist control is vacuums, dead bugs, planks.",
      "Under-butt fold: sliding leg curls, Nordic negatives, back-extension squeezes. The difference between 'big' and 'shelf with a shadow line'.",
      "Quads get minimum effective volume — step-ups with forward lean through the heel. Adductors keep cossacks + copenhagen planks so the inner line stays tight.",
      "Condition target: full and soft-over-muscle beats lean and striated for this lane. Bulk longer, cut lighter.",
      "Movement is the top-two ticket. In a lineup, almost nobody else can drop a split, hold a deep-squat groove for a full track, and arch on command. That is the differentiator.",
    ],
  },
  {
    t: "FUEL",
    lines: [
      "~1g protein per pound of bodyweight, daily. Non-negotiable in every phase.",
      "P1–P3: small calorie surplus. Flat-to-built requires eating for it.",
      "P4: slight deficit to reveal the shape the first three phases built — this is when the aesthetic actually shows up.",
      "Kitchen access makes this the easiest pillar of the whole program. Use it.",
    ],
  },
  {
    t: "GO BAG — DRAFT (BOM PENDING)",
    lines: [
      "Current draft: 3 mini loop bands · one 41\" long band (tree anchor = pull-throughs, kickbacks, rows) · sliders or two towels · 5-lb ankle weights · foldable mat. Kettlebell rides in the car.",
      "Any park bench = hip thrust station, step-up box, Bulgarian split squat rack, back-extension pad.",
      "Full bill of materials with prices and sourcing → next session.",
    ],
  },
];

/* ---------------- STATE HELPERS ---------------- */

const defaultData = () => ({
  phase: 1,
  startDate: todayISO(),
  lastPhoto: null,
  grad: { 1: [false, false, false], 2: [false, false, false], 3: [false, false, false], 4: [false, false, false, false] },
  logs: {},
});

const mkEntry = (phase) => ({
  phase,
  dayType: null,
  b1: false,
  b2: false,
  am: false,
  pm: false,
  floor: false,
  pf: false,
  dsMin: "",
  couch: false,
  waist: false,
  failures: {},
  squeezeHold: "",
  songs: "",
  stretch: false,
  notes: "",
});

/* ---------------- SMALL COMPONENTS ---------------- */

function Check({ label, sub, checked, onToggle }) {
  return (
    <button className={"row" + (checked ? " on" : "")} onClick={onToggle} type="button">
      <span className="box">{checked ? "✓" : ""}</span>
      <span className="rowtxt">
        <span className="rowlabel">{label}</span>
        {sub ? <span className="rowsub">{sub}</span> : null}
      </span>
    </button>
  );
}

function Field({ label, value, onChange, placeholder, suffix }) {
  return (
    <label className="field">
      <span className="fieldlabel">{label}</span>
      <span className="fieldwrap">
        <input className="in" value={value} placeholder={placeholder || ""} onChange={(e) => onChange(e.target.value)} />
        {suffix ? <span className="suffix">{suffix}</span> : null}
      </span>
    </label>
  );
}

function Stopwatch({ onLog }) {
  const [sec, setSec] = useState(0);
  const [run, setRun] = useState(false);
  const ref = useRef(null);
  useEffect(() => {
    if (run) {
      ref.current = setInterval(() => setSec((s) => s + 1), 1000);
    } else if (ref.current) {
      clearInterval(ref.current);
    }
    return () => ref.current && clearInterval(ref.current);
  }, [run]);
  const mm = String(Math.floor(sec / 60)).padStart(2, "0");
  const ss = String(sec % 60).padStart(2, "0");
  return (
    <div className="watch">
      <span className="watchtime">{mm}:{ss}</span>
      <button className="btn sm" type="button" onClick={() => setRun(!run)}>{run ? "STOP" : "START"}</button>
      <button className="btn sm ghost" type="button" onClick={() => { setRun(false); setSec(0); }}>RESET</button>
      <button className="btn sm coyote" type="button" disabled={sec === 0} onClick={() => onLog(String(sec))}>LOG AS HOLD</button>
    </div>
  );
}

function Fold({ title, children, openDefault }) {
  const [open, setOpen] = useState(!!openDefault);
  return (
    <div className="fold">
      <button className="foldhead" type="button" onClick={() => setOpen(!open)}>
        <span>{title}</span>
        <span className="foldmark">{open ? "–" : "+"}</span>
      </button>
      {open ? <div className="foldbody">{children}</div> : null}
    </div>
  );
}

/* ---------------- APP ---------------- */

export default function App() {
  const [data, setData] = useState(defaultData());
  const [loaded, setLoaded] = useState(false);
  const [sync, setSync] = useState("LOADING");
  const [tab, setTab] = useState("today");
  const [showExport, setShowExport] = useState(false);
  const saveT = useRef(null);
  const day = todayISO();

  /* load */
  useEffect(() => {
    (async () => {
      try {
        const r = await window.storage.get(KEY, false);
        if (r && r.value) {
          const parsed = JSON.parse(r.value);
          setData({ ...defaultData(), ...parsed, grad: { ...defaultData().grad, ...(parsed.grad || {}) } });
        }
        setSync("SYNCED");
      } catch (e) {
        setSync("LOCAL ONLY");
      }
      setLoaded(true);
    })();
  }, []);

  /* debounced save */
  useEffect(() => {
    if (!loaded) return;
    setSync("SAVING");
    if (saveT.current) clearTimeout(saveT.current);
    saveT.current = setTimeout(async () => {
      try {
        await window.storage.set(KEY, JSON.stringify(data), false);
        setSync("SYNCED");
      } catch (e) {
        setSync("LOCAL ONLY");
      }
    }, 700);
    return () => saveT.current && clearTimeout(saveT.current);
  }, [data, loaded]);

  const entry = data.logs[day] || mkEntry(data.phase);

  const patch = (p) =>
    setData((d) => ({ ...d, logs: { ...d.logs, [day]: { ...(d.logs[day] || mkEntry(d.phase)), phase: d.phase, ...p } } }));

  const patchFail = (name, v) => patch({ failures: { ...(entry.failures || {}), [name]: v } });

  /* rotation suggestion */
  const suggestedDay = useMemo(() => {
    const dates = Object.keys(data.logs).filter((k) => k < day && data.logs[k].dayType).sort();
    if (!dates.length) return "A";
    return NEXT_DAY[data.logs[dates[dates.length - 1]].dayType] || "A";
  }, [data.logs, day]);

  const week = useMemo(() => {
    const ms = new Date(day) - new Date(data.startDate);
    return Math.max(1, Math.floor(ms / (7 * 86400000)) + 1);
  }, [data.startDate, day]);

  const photoDays = useMemo(() => {
    if (!data.lastPhoto) return null;
    return Math.floor((new Date(day) - new Date(data.lastPhoto)) / 86400000);
  }, [data.lastPhoto, day]);

  /* PR board — best numeric per exercise */
  const prs = useMemo(() => {
    const best = {};
    Object.values(data.logs).forEach((e) => {
      Object.entries(e.failures || {}).forEach(([name, v]) => {
        const n = Number(v);
        if (Number.isFinite(n) && n > 0) best[name] = Math.max(best[name] || 0, n);
      });
    });
    return Object.entries(best).sort((a, b) => b[1] - a[1]);
  }, [data.logs]);

  const history = useMemo(
    () => Object.entries(data.logs).sort((a, b) => (a[0] < b[0] ? 1 : -1)),
    [data.logs]
  );

  const phase = data.phase;
  const dType = entry.dayType || suggestedDay;
  const plan = phase >= 2 ? FAILURE_PLANS[phase][dType] : null;

  /* ---------------- RENDER ---------------- */

  return (
    <div className="app">
      <style>{CSS}</style>

      {/* masthead */}
      <header className="mast">
        <div className="publine">GLUTE DOCTRINE PUBLICATION 1 · FOR TRAINING USE</div>
        <h1 className="title">GDP-1 · BOOTYCAMP</h1>
        <div className="ctrl">
          <span className="ctrlcell">PHASE <b>{PHASE_META[phase].code}</b></span>
          <span className="ctrlcell">WK <b>{week}</b></span>
          <span className="ctrlcell">DAY <b>{phase >= 2 ? dType : "—"}</b></span>
          <span className={"ctrlcell sync " + (sync === "SYNCED" ? "ok" : sync === "SAVING" ? "mid" : "warn")}>
            <b>{sync}</b>
          </span>
        </div>
      </header>

      {/* tabs */}
      <nav className="tabs">
        {[["today", "TODAY"], ["log", "LOG"], ["phases", "PHASES"], ["manual", "MANUAL"]].map(([k, label]) => (
          <button key={k} type="button" className={"tab" + (tab === k ? " active" : "")} onClick={() => setTab(k)}>
            {label}
          </button>
        ))}
      </nav>

      {!loaded ? (
        <div className="loading">LOADING DOCTRINE…</div>
      ) : tab === "today" ? (
        /* ================= TODAY ================= */
        <main>
          <div className="datebar">
            <span>{day}</span>
            <span className="dim">{PHASE_META[phase].name}</span>
          </div>

          {phase === 1 ? (
            <>
              <section className="blk">
                <div className="blkhead"><span className="tag">B1+B2</span> TWICE-DAILY SESSIONS</div>
                <Check label="AM session" sub="Groove warm-up + isolation lab · light, slow, hands on" checked={entry.am} onToggle={() => patch({ am: !entry.am })} />
                <Check label="PM session" sub="Same drills · hunt the lazy cheek, give it the extra set" checked={entry.pm} onToggle={() => patch({ pm: !entry.pm })} />
              </section>

              <section className="blk">
                <div className="blkhead"><span className="tag">FLOOR</span> DAILY NON-NEGOTIABLES</div>
                <Check label="Single-cheek squeezes + tilt isolations" sub="20/side · 20 slow + 20 fast tilts" checked={entry.floor} onToggle={() => patch({ floor: !entry.floor })} />
                <Check label="Pelvic floor set" sub="Kegels + reverse kegels · biofeedback session optional" checked={entry.pf} onToggle={() => patch({ pf: !entry.pf })} />
                <Check label="Couch stretch" sub="Hip flexors open = glutes uninhibited" checked={entry.couch} onToggle={() => patch({ couch: !entry.couch })} />
                <Field label="Deep-squat accumulation" value={entry.dsMin} onChange={(v) => patch({ dsMin: v })} placeholder="0" suffix="min (build to 5)" />
              </section>

              <section className="blk">
                <div className="blkhead"><span className="tag">HOLD</span> MAX SQUEEZE</div>
                <Stopwatch onLog={(s) => patch({ squeezeHold: s })} />
                <Field label="Best hold today" value={entry.squeezeHold} onChange={(v) => patch({ squeezeHold: v })} placeholder="0" suffix="sec · grad target 60" />
              </section>

              <section className="blk">
                <div className="blkhead"><span className="tag">B4</span> CONTROL ON BEAT</div>
                <Field label="Songs survived" value={entry.songs} onChange={(v) => patch({ songs: v })} placeholder="0" suffix="tracks · pops + tilts + slow wine" />
              </section>
            </>
          ) : (
            <>
              <section className="blk">
                <div className="blkhead"><span className="tag">B1</span> GROOVE WARM-UP · 4 MIN</div>
                <Check label="Warm-up complete" sub="Slow wine ×5 each way · figure-8s · body rolls · tilts 20+20 · mobility floor" checked={entry.b1} onToggle={() => patch({ b1: !entry.b1 })} />
              </section>

              <section className="blk">
                <div className="blkhead"><span className="tag">B2</span> ISOLATION LAB · 5 MIN</div>
                <Check label="Isolation lab complete" sub="Cheek squeezes · hip hikes · toe-down raises · clam pulses · not to failure" checked={entry.b2} onToggle={() => patch({ b2: !entry.b2 })} />
              </section>

              <section className="blk fail">
                <div className="blkhead red"><span className="tag redtag">B3</span> FAILURE BLOCK — {plan.name}</div>
                <div className="dayrow">
                  {["A", "B", "C"].map((d) => (
                    <button key={d} type="button" className={"daybtn" + (dType === d ? " on" : "")} onClick={() => patch({ dayType: d })}>
                      {d}
                      {suggestedDay === d && !entry.dayType ? <span className="sug">NEXT</span> : null}
                    </button>
                  ))}
                </div>
                {plan.items.map((name) => (
                  <Field
                    key={name}
                    label={name}
                    value={(entry.failures || {})[name] || ""}
                    onChange={(v) => patchFail(name, v)}
                    placeholder={phase === 2 ? "reps" : "wt × reps"}
                    suffix={phase === 2 ? "to technical failure" : "8→15 then add"}
                  />
                ))}
                <div className="note">Log the last CLEAN rep. Past 30 → harder variant, not more reps.</div>
              </section>

              <section className="blk">
                <div className="blkhead"><span className="tag">B4</span> FINISHER · ONE SONG</div>
                <Field label="Songs survived" value={entry.songs} onChange={(v) => patch({ songs: v })} placeholder="0" suffix={phase === 2 ? "endurance tier" : phase === 3 ? "power tier" : "performance tier"} />
              </section>

              <section className="blk">
                <div className="blkhead"><span className="tag">HOLD</span> MAX SQUEEZE</div>
                <Stopwatch onLog={(s) => patch({ squeezeHold: s })} />
                <Field label="Best hold today" value={entry.squeezeHold} onChange={(v) => patch({ squeezeHold: v })} placeholder="0" suffix="sec" />
              </section>

              <section className="blk">
                <div className="blkhead"><span className="tag">PM</span> EVENING STRETCH · 3× / WK</div>
                <Check label="Stretch block done" sub={STRETCH_FOCUS[phase]} checked={entry.stretch} onToggle={() => patch({ stretch: !entry.stretch })} />
              </section>

              {phase === 4 ? (
                <section className="blk">
                  <div className="blkhead"><span className="tag">P4</span> SCULPT EXTRAS</div>
                  <Check label="Waist control" sub="Vacuums + dead bugs · zero loaded obliques, ever" checked={entry.waist} onToggle={() => patch({ waist: !entry.waist })} />
                  <div className="photorow">
                    <span className="fieldlabel">
                      Photo check · {photoDays === null ? "never logged" : photoDays === 0 ? "logged today" : photoDays + " days ago"}
                      {photoDays !== null && photoDays >= 30 ? " · DUE" : ""}
                    </span>
                    <button className="btn sm coyote" type="button" onClick={() => setData((d) => ({ ...d, lastPhoto: day }))}>
                      LOG PHOTO TODAY
                    </button>
                  </div>
                  <div className="note">Same spot, same lighting, same angles. The camera is the P4 metric.</div>
                </section>
              ) : null}
            </>
          )}

          <section className="blk">
            <div className="blkhead"><span className="tag">FIELD</span> NOTES</div>
            <textarea
              className="in area"
              placeholder="Compensations felt, lazy-cheek status, song used, anything…"
              value={entry.notes}
              onChange={(e) => patch({ notes: e.target.value })}
            />
          </section>
        </main>
      ) : tab === "log" ? (
        /* ================= LOG ================= */
        <main>
          {prs.length ? (
            <section className="blk">
              <div className="blkhead"><span className="tag coyotetag">PR</span> BEST FAILURE NUMBERS</div>
              {prs.map(([name, n]) => (
                <div className="prrow" key={name}>
                  <span className="prname">{name}</span>
                  <span className="prnum">{n}</span>
                </div>
              ))}
              <div className="note">Numeric logs only — Phase 3+ weight × reps entries live in the day cards below.</div>
            </section>
          ) : null}

          <section className="blk">
            <div className="blkhead"><span className="tag">HX</span> SESSION HISTORY</div>
            {history.length === 0 ? (
              <div className="empty">No sessions logged yet. Today is day one — go squeeze something.</div>
            ) : (
              history.map(([d, e]) => (
                <div className="hxrow" key={d}>
                  <div className="hxtop">
                    <span className="hxdate">{d}</span>
                    <span className="hxmeta">
                      P{e.phase}{e.dayType ? " · " + e.dayType : ""}{e.stretch ? " · STR" : ""}{e.songs ? " · ♪" + e.songs : ""}{e.squeezeHold ? " · " + e.squeezeHold + "s" : ""}
                    </span>
                  </div>
                  {Object.keys(e.failures || {}).length ? (
                    <div className="hxfails">
                      {Object.entries(e.failures).filter(([, v]) => v).map(([k, v]) => (
                        <span className="hxchip" key={k}>{k.split("·")[0].trim()}: <b>{v}</b></span>
                      ))}
                    </div>
                  ) : null}
                  {e.notes ? <div className="hxnotes">{e.notes}</div> : null}
                </div>
              ))
            )}
          </section>

          <section className="blk">
            <div className="blkhead"><span className="tag">IO</span> EXPORT</div>
            <button className="btn" type="button" onClick={() => setShowExport(!showExport)}>
              {showExport ? "HIDE JSON" : "SHOW JSON FOR VAULT"}
            </button>
            {showExport ? <textarea className="in area mono" readOnly value={JSON.stringify(data, null, 2)} /> : null}
          </section>
        </main>
      ) : tab === "phases" ? (
        /* ================= PHASES ================= */
        <main>
          {[1, 2, 3, 4].map((p) => (
            <section className={"blk phase" + (p === phase ? " current" : "")} key={p}>
              <div className="blkhead">
                <span className={"tag" + (p === phase ? " odtag" : "")}>{PHASE_META[p].code}</span> {PHASE_META[p].name}
                <span className="span">{PHASE_META[p].span}</span>
              </div>
              <p className="phasegoal">{PHASE_META[p].goal}</p>
              <div className="gradhead">{p === 4 ? "PERFORMANCE STANDARDS" : "GRADUATION CRITERIA"}</div>
              {GRAD[p].map((g, i) => (
                <Check
                  key={i}
                  label={g}
                  checked={!!(data.grad[p] && data.grad[p][i])}
                  onToggle={() =>
                    setData((d) => {
                      const arr = [...(d.grad[p] || [])];
                      arr[i] = !arr[i];
                      return { ...d, grad: { ...d.grad, [p]: arr } };
                    })
                  }
                />
              ))}
              {p !== phase ? (
                <button className="btn" type="button" onClick={() => setData((d) => ({ ...d, phase: p }))}>
                  SET AS CURRENT PHASE
                </button>
              ) : (
                <div className="currentmark">▸ CURRENT PHASE</div>
              )}
            </section>
          ))}
          <div className="note center">Pass every box before moving up. The phases are a ladder, not a menu.</div>
        </main>
      ) : (
        /* ================= MANUAL ================= */
        <main>
          {MANUAL.map((s, i) => (
            <Fold key={s.t} title={s.t} openDefault={i === 0}>
              {s.lines.map((l, j) => (
                <p className="mline" key={j}>{l}</p>
              ))}
            </Fold>
          ))}
          <div className="note center">GDP-1 · doctrine is a living document — amendments ship as the program evolves.</div>
        </main>
      )}

      <footer className="foot">BUILD · CONTROL · PERFORM — GDP-1</footer>
    </div>
  );
}

/* ---------------- STYLES ---------------- */

const CSS = `
@import url('https://fonts.googleapis.com/css2?family=Oswald:wght@500;600;700&family=IBM+Plex+Mono:wght@400;500;600&display=swap');

:root{
  --ink:#15170f; --panel:#1e2115; --panel2:#232719; --line:#343827;
  --bone:#e6e2d3; --dust:#94927e; --od:#8a9a5b; --coyote:#b3854d; --signal:#cf5c48;
}
*{box-sizing:border-box; -webkit-tap-highlight-color:transparent;}
.app{
  min-height:100vh; background:var(--ink); color:var(--bone);
  font-family:-apple-system,'Segoe UI',Roboto,Helvetica,Arial,sans-serif;
  max-width:640px; margin:0 auto; padding:0 14px 40px;
}
button{font:inherit; cursor:pointer;}
button:focus-visible, input:focus-visible, textarea:focus-visible{outline:2px solid var(--od); outline-offset:2px;}
@media (prefers-reduced-motion: reduce){ *{transition:none !important;} }

/* masthead */
.mast{padding:18px 0 10px; border-bottom:2px solid var(--od);}
.publine{font-family:'IBM Plex Mono',monospace; font-size:10px; letter-spacing:.22em; color:var(--dust);}
.title{
  font-family:'Oswald',Impact,sans-serif; font-weight:700; font-size:34px;
  letter-spacing:.06em; margin:4px 0 10px; color:var(--bone); text-transform:uppercase;
}
.ctrl{display:flex; flex-wrap:wrap; gap:6px;}
.ctrlcell{
  font-family:'IBM Plex Mono',monospace; font-size:11px; letter-spacing:.08em;
  color:var(--dust); border:1px solid var(--line); padding:4px 8px; background:var(--panel);
}
.ctrlcell b{color:var(--bone); font-weight:600;}
.sync.ok b{color:var(--od);} .sync.mid b{color:var(--coyote);} .sync.warn b{color:var(--signal);}

/* tabs */
.tabs{display:flex; gap:2px; margin:14px 0 16px; border:1px solid var(--line); background:var(--line);}
.tab{
  flex:1; padding:10px 0; background:var(--panel); color:var(--dust); border:none;
  font-family:'Oswald',sans-serif; font-weight:600; font-size:13px; letter-spacing:.12em;
}
.tab.active{background:var(--od); color:var(--ink);}

/* today */
.datebar{
  display:flex; justify-content:space-between; align-items:baseline;
  font-family:'IBM Plex Mono',monospace; font-size:12px; letter-spacing:.1em; margin-bottom:12px;
}
.dim{color:var(--dust);}
.blk{background:var(--panel); border:1px solid var(--line); padding:12px; margin-bottom:14px;}
.blk.fail{border-left:3px solid var(--signal);}
.blkhead{
  font-family:'Oswald',sans-serif; font-weight:600; font-size:14px; letter-spacing:.14em;
  text-transform:uppercase; margin-bottom:10px; display:flex; align-items:center; gap:8px; flex-wrap:wrap;
}
.blkhead.red{color:var(--signal);}
.tag{
  font-family:'IBM Plex Mono',monospace; font-size:10px; letter-spacing:.14em;
  background:var(--line); color:var(--bone); padding:2px 6px;
}
.redtag{background:var(--signal); color:var(--ink);}
.odtag{background:var(--od); color:var(--ink);}
.coyotetag{background:var(--coyote); color:var(--ink);}
.span{margin-left:auto; font-family:'IBM Plex Mono',monospace; font-size:10px; color:var(--dust); letter-spacing:.12em;}

/* check rows */
.row{
  display:flex; gap:10px; width:100%; text-align:left; background:var(--panel2);
  border:1px solid var(--line); padding:10px; margin-bottom:8px; color:var(--bone);
  transition:border-color .12s;
}
.row.on{border-color:var(--od);}
.box{
  width:22px; height:22px; min-width:22px; border:1px solid var(--dust);
  display:flex; align-items:center; justify-content:center;
  font-family:'IBM Plex Mono',monospace; font-size:14px; color:var(--od);
}
.row.on .box{border-color:var(--od); background:rgba(138,154,91,.12);}
.rowtxt{display:flex; flex-direction:column; gap:2px;}
.rowlabel{font-size:14px; line-height:1.35;}
.rowsub{font-size:11.5px; color:var(--dust); line-height:1.4;}

/* fields */
.field{display:block; margin-bottom:8px;}
.fieldlabel{display:block; font-size:12px; color:var(--dust); margin-bottom:4px; line-height:1.35;}
.fieldwrap{display:flex; align-items:center; gap:8px;}
.in{
  width:100%; background:var(--ink); border:1px solid var(--line); color:var(--bone);
  padding:10px; font-family:'IBM Plex Mono',monospace; font-size:15px;
}
.in::placeholder{color:#5a5c4c;}
.suffix{font-family:'IBM Plex Mono',monospace; font-size:10px; color:var(--dust); letter-spacing:.06em; white-space:nowrap;}
.area{min-height:76px; resize:vertical; font-family:inherit; font-size:14px; line-height:1.5;}
.area.mono{font-family:'IBM Plex Mono',monospace; font-size:11px; min-height:180px;}

/* buttons */
.btn{
  background:var(--od); color:var(--ink); border:none; padding:10px 14px;
  font-family:'Oswald',sans-serif; font-weight:600; letter-spacing:.12em; font-size:12px;
}
.btn.sm{padding:8px 10px; font-size:11px;}
.btn.ghost{background:transparent; color:var(--dust); border:1px solid var(--line);}
.btn.coyote{background:var(--coyote);}
.btn:disabled{opacity:.4; cursor:default;}

/* day selector */
.dayrow{display:flex; gap:8px; margin-bottom:12px;}
.daybtn{
  flex:1; padding:12px 0; background:var(--panel2); border:1px solid var(--line); color:var(--dust);
  font-family:'Oswald',sans-serif; font-weight:700; font-size:18px; letter-spacing:.1em; position:relative;
}
.daybtn.on{border-color:var(--signal); color:var(--bone); background:rgba(207,92,72,.1);}
.sug{
  position:absolute; top:3px; right:4px; font-family:'IBM Plex Mono',monospace;
  font-size:8px; letter-spacing:.1em; color:var(--coyote);
}

/* stopwatch */
.watch{display:flex; align-items:center; gap:8px; flex-wrap:wrap; margin-bottom:10px;}
.watchtime{
  font-family:'IBM Plex Mono',monospace; font-size:26px; font-weight:600; color:var(--bone);
  min-width:86px; letter-spacing:.04em;
}

/* notes + misc */
.note{font-size:11.5px; color:var(--dust); line-height:1.5; margin-top:6px;}
.note.center{text-align:center; margin:18px 0;}
.photorow{display:flex; align-items:center; justify-content:space-between; gap:10px; margin-bottom:6px; flex-wrap:wrap;}
.loading, .empty{
  text-align:center; padding:34px 0; color:var(--dust);
  font-family:'IBM Plex Mono',monospace; font-size:12px; letter-spacing:.14em;
}

/* log tab */
.prrow{display:flex; justify-content:space-between; border-bottom:1px solid var(--line); padding:8px 2px; font-size:13px;}
.prname{color:var(--bone);}
.prnum{font-family:'IBM Plex Mono',monospace; color:var(--coyote); font-weight:600;}
.hxrow{border-bottom:1px solid var(--line); padding:10px 2px;}
.hxtop{display:flex; justify-content:space-between; align-items:baseline; gap:8px;}
.hxdate{font-family:'IBM Plex Mono',monospace; font-size:12px; color:var(--bone);}
.hxmeta{font-family:'IBM Plex Mono',monospace; font-size:10.5px; color:var(--coyote); letter-spacing:.06em;}
.hxfails{display:flex; flex-wrap:wrap; gap:6px; margin-top:6px;}
.hxchip{
  font-family:'IBM Plex Mono',monospace; font-size:10.5px; color:var(--dust);
  border:1px solid var(--line); padding:2px 6px;
}
.hxchip b{color:var(--bone);}
.hxnotes{font-size:12px; color:var(--dust); margin-top:6px; line-height:1.45;}

/* phases tab */
.blk.phase.current{border-color:var(--od);}
.phasegoal{font-size:13px; line-height:1.55; color:var(--bone); margin:0 0 10px;}
.gradhead{
  font-family:'IBM Plex Mono',monospace; font-size:10px; letter-spacing:.18em;
  color:var(--dust); margin-bottom:8px;
}
.currentmark{
  font-family:'Oswald',sans-serif; font-size:12px; letter-spacing:.16em; color:var(--od); padding:6px 0;
}

/* manual */
.fold{border:1px solid var(--line); background:var(--panel); margin-bottom:10px;}
.foldhead{
  width:100%; display:flex; justify-content:space-between; align-items:center;
  background:none; border:none; color:var(--bone); padding:12px;
  font-family:'Oswald',sans-serif; font-weight:600; font-size:13px; letter-spacing:.14em; text-align:left;
}
.foldmark{font-family:'IBM Plex Mono',monospace; color:var(--od); font-size:16px;}
.foldbody{padding:0 12px 12px; border-top:1px solid var(--line);}
.mline{font-size:13px; line-height:1.6; color:var(--bone); margin:10px 0 0;}
.mline:first-child{margin-top:12px;}

.foot{
  text-align:center; font-family:'IBM Plex Mono',monospace; font-size:9px;
  letter-spacing:.28em; color:var(--dust); margin-top:26px;
}
`;
