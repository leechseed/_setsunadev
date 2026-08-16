---
title: "sex-menu-profiler.jsx"
project: "DESIRE PROFILE"
trunk: ORANGE
kind: project-knowledge
---

import { useState, useMemo } from "react";

// ---------- PALETTE (matches FORM RNP-1: olive-black, OD green, coyote, paper) ----------
const C = {
  bg: "#14160F",
  panel: "#1B1E13",
  panel2: "#22261A",
  ink: "#E8E4D8",
  dim: "#9A9784",
  olive: "#8A9A5B",
  oliveHi: "#A9BC6F",
  oliveDeep: "#4E5A33",
  coyote: "#B08D57",
  slate: "#7C93A8",
  line: "#3A3E2C",
  red: "#A45A52",
};

const MONO = "'IBM Plex Mono','JetBrains Mono',ui-monospace,'SF Mono',Menlo,monospace";
const BODY = "'Inter','Helvetica Neue',-apple-system,system-ui,sans-serif";

const RATING_COLOR = {
  hard: C.red, soft: C.coyote, indiff: C.dim, try: C.slate,
  occas: "#74854C", love: C.olive, need: C.oliveHi,
};
const SCORE = { hard: 0, soft: 1, indiff: 2, try: 3, occas: 4, love: 5, need: 6 };

const STYLES = `
  .smp button:focus-visible, .smp input:focus-visible, .smp textarea:focus-visible{ outline:2px solid ${C.coyote}; outline-offset:2px; }
  @media (prefers-reduced-motion: no-preference){ .smp .fadein{ animation: smpfade .22s ease; } }
  @keyframes smpfade{ from{ opacity:0; transform:translateY(4px);} to{ opacity:1; transform:none;} }
`;
// ---------- DATA — generated verbatim from adlaw_sex_profiler.xlsx ----------
const SCALE = [
  {key:"hard",label:"Hard limit",chip:"HARD",def:"Under no circumstances do you want this"},
  {key:"soft",label:"Soft limit",chip:"SOFT",def:"Not ruled out completely, but would probably only do it if your partner really wanted it"},
  {key:"indiff",label:"Indifferent",chip:"INDIFF",def:"You don\u2019t have any objections to it, but can\u2019t say it turns you on"},
  {key:"try",label:"Try it",chip:"TRY",def:"You have never done it but are open or intrigued to try it"},
  {key:"occas",label:"Occasionally",chip:"OCCAS",def:"You enjoy doing it every once in a while"},
  {key:"love",label:"Love it",chip:"LOVE",def:"You really enjoy this and want to do lots of it"},
  {key:"need",label:"Need it",chip:"NEED",def:"You can't go without this. You NEED it as part of your sex life"},
];
const QUESTIONS = [{"id":"q1","text":"What does being submissive mean or look like to you?"},{"id":"q2","text":"What does being dominant mean or look like to you?"},{"id":"q3","text":"What are the feelings YOU most want to feel during sex?"},{"id":"q4","text":"What are the feelings you want ME to feel during sex?"},{"id":"q5","text":"I promise to never judge. Is there anything your shy, insecure, or nervous about that I should know?"}];
const HEALTH = [{"id":"h1","text":"List any allergies (e.g. Latex, food, scents, oils, lotions, wool, feathers, etc)"},{"id":"h2","text":"Any medical problems/issues? (if yes, give details:)"},{"id":"h3","text":"Do you have any known sexually transmitted diseases (STDs)?"},{"id":"h4","text":"When were you last tested?"},{"id":"h5","text":"Do you practice safe sex?"},{"id":"h6","text":"Any specific subject not described in this list that you wish to note?"},{"id":"h7","text":"Any thing else you'd like to share:"}];
const CATEGORIES = [
  {"name":"RELATIONSHIPS","items":[{"id":"i22","label":"Monogamy/ Exclusivity"},{"id":"i23","label":"Polyamory / multiple play partners/lovers"},{"id":"i24","label":"Friends with benefits"}]},
  {"name":"GENERAL","items":[{"id":"i26","label":"Condoms"},{"id":"i27","label":"Aftercare"},{"id":"i28","label":"Cuddles"},{"id":"i29","label":"Bed sharing"},{"id":"i30","label":"Bath/ shower together"},{"id":"i31","label":"Hygiene"},{"id":"i32","label":"Public Displays of Affection"},{"id":"i33","label":"Kissing"},{"id":"i34","label":"Neck kissing/Hickies"},{"id":"i35","label":"Dirty talk"},{"id":"i36","label":"Extreme dirty talk (involving extreme taboos)"},{"id":"i37","label":"Hairy/ Shaved genitals"}]},
  {"name":"MANUAL","items":[{"id":"i39","label":"Clitoris stimulation with hand/finger"},{"id":"i40","label":"Fingering - vaginal"},{"id":"i41","label":"Fisting - vaginal"},{"id":"i42","label":"Hand jobs"},{"id":"i43","label":"Foot Jobs"},{"id":"i44","label":"Cock worship"},{"id":"i45","label":"Masturbation"},{"id":"i46","label":"Mutual masturbation"},{"id":"i47","label":"Breast/nipple kissing/ licking/ sucking"},{"id":"i48","label":"Breast fucking"},{"id":"i49","label":"Spanking"}]},
  {"name":"ORAL","items":[{"id":"i51","label":"Cunnilingus (oral on female genitalia)"},{"id":"i52","label":"Fellatio (oral on male genitalia)"},{"id":"i53","label":"Cockwarming"},{"id":"i54","label":"Deepthroating"},{"id":"i55","label":"Face fucking"},{"id":"i56","label":"Face sitting"}]},
  {"name":"INTERCOURSE","items":[{"id":"i58","label":"Intercourse"},{"id":"i59","label":"Double penetration"},{"id":"i60","label":"Triple penetration"},{"id":"i61","label":"Sex while asleep"},{"id":"i62","label":"Sex during menstruation"}]},
  {"name":"ANAL PLAY","items":[{"id":"i64","label":"Anal fingering"},{"id":"i65","label":"Anal fisting"},{"id":"i66","label":"Anal sex"},{"id":"i67","label":"Rimming (oral/anal play)"}]},
  {"name":"ORGASM","items":[{"id":"i69","label":"Delay methods (creams etc)"},{"id":"i70","label":"Edging"},{"id":"i71","label":"Orgasm control"},{"id":"i72","label":"Orgasm denial"},{"id":"i73","label":"Orgasm on command"},{"id":"i74","label":"Cumming in partner"},{"id":"i75","label":"Cumming on body"},{"id":"i76","label":"Cumming on face"},{"id":"i77","label":"Swallowing Cum"},{"id":"i78","label":"Squirting/ Female ejaculation"},{"id":"i79","label":"Sucking/licking sperm from a partners orifice"}]},
  {"name":"TOYS","items":[{"id":"i81","label":"Ben Wa balls"},{"id":"i82","label":"Cock ring"},{"id":"i83","label":"Dildos"},{"id":"i84","label":"Double-ended dildos"},{"id":"i85","label":"Fleshlight"},{"id":"i86","label":"Fucking machine"},{"id":"i87","label":"Hitachi Magic Wand"},{"id":"i88","label":"Inflatable toys"},{"id":"i89","label":"Love doll"},{"id":"i90","label":"Penis pump"},{"id":"i91","label":"Remote-controlled toys"},{"id":"i92","label":"Strap-on-dildo"},{"id":"i93","label":"Suction Cups"},{"id":"i94","label":"Suction toys"},{"id":"i95","label":"Vibrator"},{"id":"i96","label":"Anal dildos"},{"id":"i97","label":"Anal plug tails"},{"id":"i98","label":"Anal plugs"},{"id":"i99","label":"Anal plugs - public under clothes"},{"id":"i100","label":"Anal hooks"},{"id":"i101","label":"Anal spreader"},{"id":"i102","label":"Anal vibrators"}]},
  {"name":"DOMINANCE & SUBMISSION","items":[{"id":"i104","label":"Power exchange"},{"id":"i105","label":"Daddy/ little girl"},{"id":"i106","label":"Master/ slave"},{"id":"i107","label":"Honorifics (Sir, Master)"},{"id":"i108","label":"Following orders"},{"id":"i109","label":"Rules"},{"id":"i110","label":"Rewards"},{"id":"i111","label":"Punishment"},{"id":"i112","label":"Funishment"},{"id":"i113","label":"Bratty behaviour"},{"id":"i114","label":"Begging"},{"id":"i115","label":"Lecturing for misbehaviour"},{"id":"i116","label":"Mentoring"},{"id":"i117","label":"Assignments"},{"id":"i118","label":"Obedience training"},{"id":"i119","label":"Behaviour control and Modification"},{"id":"i120","label":"Bathroom control"},{"id":"i121","label":"Collars"},{"id":"i122","label":"Lead/leash"},{"id":"i123","label":"Dressing up to please Dom"},{"id":"i124","label":"Rituals"},{"id":"i125","label":"Contracts"},{"id":"i126","label":"Slave positions"},{"id":"i127","label":"Kneeling"},{"id":"i128","label":"Chastity"},{"id":"i129","label":"Service submission"},{"id":"i130","label":"Chores (domestic service/housework)"},{"id":"i131","label":"Enforced Bedtime"},{"id":"i132","label":"Diet plan"},{"id":"i133","label":"Financial submission"},{"id":"i134","label":"Hypnosis"},{"id":"i135","label":"Degradation"},{"id":"i136","label":"Eye contact restrictions"},{"id":"i137","label":"Speech Restrictions, what and when.."},{"id":"i138","label":"Ignoring/being ignored"},{"id":"i139","label":"Sleeping on the Floor"},{"id":"i140","label":"Objectification (Serving as sexual toy/plaything)"},{"id":"i141","label":"Objectification (Serving as art)"},{"id":"i142","label":"Objectification (Serving as furniture)"},{"id":"i143","label":"Inspection"},{"id":"i144","label":"Free Use"},{"id":"i145","label":"Submitting to a submissive"}]},
  {"name":"PRIMAL","items":[{"id":"i147","label":"Aggressive dominance"},{"id":"i148","label":"Rough play"},{"id":"i149","label":"Resistance play"},{"id":"i150","label":"Spitting"},{"id":"i151","label":"Tickling"},{"id":"i152","label":"Scratching"},{"id":"i153","label":"Hair pulling"},{"id":"i154","label":"Choking"},{"id":"i155","label":"Biting (being bitten)"},{"id":"i156","label":"Breast/nipple biting"},{"id":"i157","label":"Nipple Play - Pulls, Tugs, Twists"},{"id":"i158","label":"Sweat"},{"id":"i159","label":"Crawling"},{"id":"i160","label":"Wrestling"},{"id":"i161","label":"Predator/ Prey"}]},
  {"name":"TANTRA","items":[{"id":"i163","label":"Breathwork"},{"id":"i164","label":"Prolonged Eye Gazing"},{"id":"i165","label":"Sensation Play"},{"id":"i166","label":"Tantric Massage"},{"id":"i167","label":"Yoni Massage"},{"id":"i168","label":"Lingam Massage"},{"id":"i169","label":"Breast Massage"},{"id":"i170","label":"Mental/ Energetic orgasm"},{"id":"i171","label":"Prolonged Sex/ Multiple Orgasms"}]},
  {"name":"EXHIBITIONISM / VOYEURISM","items":[{"id":"i173","label":"Exhibitionism (before friends)"},{"id":"i174","label":"Exhibitionism (before strangers)"},{"id":"i175","label":"Fetish clubs"},{"id":"i176","label":"Fetish parties (non-play, being served)"},{"id":"i177","label":"Public Sex/ Play"},{"id":"i178","label":"Using toys in public"},{"id":"i179","label":"Erotic dance/ Stripping"},{"id":"i180","label":"Being filmed during sex acts"},{"id":"i181","label":"Being photographed naked/erotic by someone else"},{"id":"i182","label":"Erotic self photography (sending pictures)"},{"id":"i183","label":"Looking at pornographic images"},{"id":"i184","label":"Looking at pornographic films"},{"id":"i185","label":"Erotica"},{"id":"i186","label":"Watching sexual acts / Voyeurism"},{"id":"i187","label":"Cybersex"},{"id":"i188","label":"Phone sex"},{"id":"i189","label":"Sexting"}]},
  {"name":"ROLEPLAY","items":[{"id":"i191","label":"Age Play (not pedophilia)"},{"id":"i192","label":"Babysitter"},{"id":"i193","label":"Bimbofication/ Fuck Doll"},{"id":"i194","label":"Boss/secretary"},{"id":"i195","label":"Breeding/ Impregnation fantasy"},{"id":"i196","label":"Cheerleader"},{"id":"i197","label":"Incest - Daddy/daughter"},{"id":"i198","label":"Incest - Brother/ Sister"},{"id":"i199","label":"Incest - Mother/ son"},{"id":"i200","label":"Interrogations"},{"id":"i201","label":"Kidnapping"},{"id":"i202","label":"Livestock market and auctions"},{"id":"i203","label":"Maid"},{"id":"i204","label":"Nurse/Doctor + Patient"},{"id":"i205","label":"Prison scene"},{"id":"i206","label":"Prostitution"},{"id":"i207","label":"Religious Scenes"},{"id":"i208","label":"Stripper"},{"id":"i209","label":"Teacher/student"},{"id":"i210","label":"Massage Therapist"},{"id":"i211","label":"Zookeeper/ Pet"}]},
  {"name":"DRESSING UP","items":[{"id":"i213","label":"Provocative clothing"},{"id":"i214","label":"Lingerie"},{"id":"i215","label":"Corsets"},{"id":"i216","label":"Suits"},{"id":"i217","label":"Uniforms"},{"id":"i218","label":"Cross dressing"},{"id":"i219","label":"Fur"},{"id":"i220","label":"Latex"},{"id":"i221","label":"Leather"}]},
  {"name":"PVC","items":[{"id":"i223","label":"Rubber"},{"id":"i224","label":"Spandex"}]},
  {"name":"PETPLAY","items":[{"id":"i226","label":"Taking on the role of an animal"},{"id":"i227","label":"Pet beds"},{"id":"i228","label":"Pet bowls"},{"id":"i229","label":"Pet lead"},{"id":"i230","label":"Pet litter tray"},{"id":"i231","label":"Eating from the hand"}]},
  {"name":"GROUP PLAY","items":[{"id":"i233","label":"Cuckold"},{"id":"i234","label":"Serving other Doms (supervised only)"},{"id":"i235","label":"Given away (to another Dom)"},{"id":"i236","label":"Encounters with strangers"},{"id":"i237","label":"Glory hole"},{"id":"i238","label":"FMF Threesome"},{"id":"i239","label":"MFM Threesome"},{"id":"i240","label":"Gang bang (multiple men)"},{"id":"i241","label":"Reverse gang bang (multiple women)"},{"id":"i242","label":"Orgy"},{"id":"i243","label":"Harem"},{"id":"i244","label":"Including others (in a scene)"},{"id":"i245","label":"Munches"},{"id":"i246","label":"Play parties"},{"id":"i247","label":"Shared (given to another temporarily)"},{"id":"i248","label":"Swapping (with one other couple)"},{"id":"i249","label":"Swinging (multiple couples)"},{"id":"i250","label":"Slave market and auctions"}]},
  {"name":"BONDAGE","items":[{"id":"i252","label":"Blindfolds"},{"id":"i253","label":"Hoods"},{"id":"i254","label":"Masks"},{"id":"i255","label":"Bondage/sensory deprivation"},{"id":"i256","label":"Body bondage (using only hands/ body to restrain you)"},{"id":"i257","label":"Leather restraints"},{"id":"i258","label":"Bondage for prolonged periods of time"},{"id":"i259","label":"Mental bondage"},{"id":"i260","label":"Spreader Bars"},{"id":"i261","label":"Chains"},{"id":"i262","label":"Hog ties"},{"id":"i263","label":"Chastity device/belts"},{"id":"i264","label":"Rope/ Shibari"},{"id":"i265","label":"Harnesses"},{"id":"i266","label":"Straight jackets"},{"id":"i267","label":"Leather Gag"},{"id":"i268","label":"Metal gag"},{"id":"i269","label":"Metal restraints"},{"id":"i270","label":"Mouth hook"},{"id":"i271","label":"Nose hook"},{"id":"i272","label":"Vaginal hook"},{"id":"i273","label":"Suspension"},{"id":"i274","label":"Mouth Bit"},{"id":"i275","label":"Bagging"},{"id":"i276","label":"Ball gag"},{"id":"i277","label":"Cloth gag"},{"id":"i278","label":"Open Mouth gag"},{"id":"i279","label":"Phallic gag"},{"id":"i280","label":"PVC Gag"},{"id":"i281","label":"Rope Gag"},{"id":"i282","label":"Rubber gag"},{"id":"i283","label":"Tape gag"},{"id":"i284","label":"Using hands as a gag"},{"id":"i285","label":"Inflatable"}]},
  {"name":"IMPACT PLAY","items":[{"id":"i287","label":"Abrasion (scraping, sanding)"},{"id":"i288","label":"Caning"},{"id":"i289","label":"Clothespins/pegs"},{"id":"i290","label":"Evil stick"},{"id":"i291","label":"Face slapping"},{"id":"i292","label":"Flogger"},{"id":"i293","label":"Paddles"},{"id":"i294","label":"Riding crops"},{"id":"i295","label":"Trampling"},{"id":"i296","label":"Punching"},{"id":"i297","label":"Wartenburg Pinwheel"},{"id":"i298","label":"Whips"},{"id":"i299","label":"Nipple clamps"},{"id":"i300","label":"Breast binding"},{"id":"i301","label":"Breast caning"},{"id":"i302","label":"Breast press"},{"id":"i303","label":"Breast scratching"},{"id":"i304","label":"Breast spanking"},{"id":"i305","label":"Breast torture"},{"id":"i306","label":"Breast whipping"}]},
  {"name":"SADISM MASOCHISM","items":[{"id":"i308","label":"Threats"},{"id":"i309","label":"Fear"},{"id":"i310","label":"Crying"},{"id":"i311","label":"Humiliation in private"},{"id":"i312","label":"Humiliation in public"},{"id":"i313","label":"Emotional masochism"},{"id":"i314","label":"Emotional sadism"},{"id":"i315","label":"Abusive language"},{"id":"i316","label":"Blackmail"},{"id":"i317","label":"Sleep deprivation"},{"id":"i318","label":"Chamber-pot use"}]},
  {"name":"MARKS","items":[{"id":"i320","label":"Bruising"},{"id":"i321","label":"Branding"},{"id":"i322","label":"Burns"},{"id":"i323","label":"Flesh hook"},{"id":"i324","label":"Piercings (permanent)"},{"id":"i325","label":"Piercings (temporary)"},{"id":"i326","label":"Scarification (cutting,making scars)"},{"id":"i327","label":"Tattoos"}]},
  {"name":"GENITAL TORTURE","items":[{"id":"i329","label":"Anal torture"},{"id":"i330","label":"Nipple Piercing"},{"id":"i331","label":"Nipple torture"},{"id":"i332","label":"Nipple weights"},{"id":"i333","label":"Ball busting"},{"id":"i334","label":"Ball stretching"},{"id":"i335","label":"Ball weights"},{"id":"i336","label":"Clit spanking"},{"id":"i337","label":"Clit torture"},{"id":"i338","label":"Clit weights"},{"id":"i339","label":"Cock and ball torture"},{"id":"i340","label":"Genital clamps"},{"id":"i341","label":"Genital whipping"},{"id":"i342","label":"Labia stretching"},{"id":"i343","label":"Labia weights"}]},
  {"name":"EDGE PLAY","items":[{"id":"i345","label":"Consensual non-consent/rape"},{"id":"i346","label":"Needle (sewing) play"},{"id":"i347","label":"Wax Play"},{"id":"i348","label":"Fire play"},{"id":"i349","label":"Electricity - TENS unit"},{"id":"i350","label":"Internal electrical play"},{"id":"i351","label":"Violet wand"},{"id":"i352","label":"Smothering"},{"id":"i353","label":"Breath play"},{"id":"i354","label":"Drowning play"},{"id":"i355","label":"Knife play (no blood)"},{"id":"i356","label":"Cutting"},{"id":"i357","label":"Blood letting"},{"id":"i358","label":"Blood play"}]},
  {"name":"OTHER","items":[{"id":"i360","label":"Food play ('Splosh play')"},{"id":"i361","label":"Lactation"}]},
];

const TOTAL_ITEMS = CATEGORIES.reduce((s, c) => s + c.items.length, 0);
const RATING_LABEL = Object.fromEntries(SCALE.map((s) => [s.key, s.label]));

// ---------- SMALL COMPONENTS ----------

function Stamp({ code, name }) {
  return (
    <div style={{ border: `1px solid ${C.line}`, display: "inline-block", padding: "6px 12px", borderRadius: 2 }}>
      <div style={{ fontFamily: MONO, fontSize: 10, letterSpacing: 3, color: C.dim }}>SMP-1 // SECTION {code}</div>
      <div style={{ fontFamily: MONO, fontSize: 17, letterSpacing: 3, color: C.olive, fontWeight: 700 }}>{name}</div>
    </div>
  );
}

function Legend() {
  const [open, setOpen] = useState(false);
  return (
    <div style={{ margin: "12px 0" }}>
      <button onClick={() => setOpen(!open)} style={{
        fontFamily: MONO, fontSize: 10, letterSpacing: 2, padding: "7px 12px", borderRadius: 2, cursor: "pointer",
        background: "transparent", color: C.coyote, border: `1px solid ${C.line}`,
      }}>{open ? "▾ RATING KEY" : "▸ RATING KEY"}</button>
      {open && (
        <div style={{ border: `1px solid ${C.line}`, borderRadius: 3, padding: 12, marginTop: 8, background: C.panel }}>
          {SCALE.map((s) => (
            <div key={s.key} style={{ display: "flex", gap: 10, padding: "5px 0", alignItems: "baseline" }}>
              <span style={{ fontFamily: MONO, fontSize: 10, letterSpacing: 1, color: RATING_COLOR[s.key], width: 92, flexShrink: 0 }}>{s.label.toUpperCase()}</span>
              <span style={{ fontFamily: BODY, fontSize: 12.5, color: C.dim, lineHeight: 1.5 }}>{s.def}</span>
            </div>
          ))}
        </div>
      )}
    </div>
  );
}

function MenuItem({ item, rating, note, onRate, onNote }) {
  const [noteOpen, setNoteOpen] = useState(!!note);
  return (
    <div style={{ padding: "13px 0", borderBottom: `1px solid ${C.line}` }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline", gap: 10 }}>
        <div style={{ fontFamily: BODY, fontSize: 14.5, color: rating ? C.ink : C.dim, lineHeight: 1.4 }}>{item.label}</div>
        <button onClick={() => setNoteOpen(!noteOpen)} aria-label={"note for " + item.label} style={{
          fontFamily: MONO, fontSize: 9, letterSpacing: 1, padding: "3px 7px", borderRadius: 2, cursor: "pointer", flexShrink: 0,
          background: "transparent", color: note ? C.coyote : C.dim, border: `1px solid ${note ? C.coyote : C.line}`,
        }}>{note ? "NOTE ●" : "NOTE"}</button>
      </div>
      <div style={{ display: "flex", flexWrap: "wrap", gap: 5, marginTop: 9 }}>
        {SCALE.map((s) => {
          const sel = rating === s.key;
          return (
            <button key={s.key} onClick={() => onRate(sel ? undefined : s.key)} style={{
              fontFamily: MONO, fontSize: 9.5, letterSpacing: 1, fontWeight: sel ? 700 : 400,
              padding: "6px 8px", borderRadius: 2, cursor: "pointer",
              border: `1px solid ${sel ? RATING_COLOR[s.key] : C.line}`,
              background: sel ? RATING_COLOR[s.key] : C.panel2,
              color: sel ? C.bg : C.dim,
            }}>{s.chip}</button>
          );
        })}
      </div>
      {noteOpen && (
        <input value={note || ""} onChange={(e) => onNote(e.target.value)}
          placeholder="note — conditions, context, specifics"
          style={{
            marginTop: 8, width: "100%", boxSizing: "border-box", padding: "9px 10px", borderRadius: 2,
            background: C.bg, color: C.ink, border: `1px solid ${C.line}`, fontFamily: BODY, fontSize: 13,
          }} />
      )}
    </div>
  );
}

function TextBlock({ item, value, onSet }) {
  return (
    <div style={{ padding: "13px 0", borderBottom: `1px solid ${C.line}` }}>
      <div style={{ fontFamily: BODY, fontSize: 14.5, color: C.ink, lineHeight: 1.5, marginBottom: 8 }}>{item.text}</div>
      <textarea value={value || ""} onChange={(e) => onSet(e.target.value)} rows={3}
        style={{
          width: "100%", boxSizing: "border-box", padding: "9px 10px", borderRadius: 2, resize: "vertical",
          background: C.bg, color: C.ink, border: `1px solid ${C.line}`, fontFamily: BODY, fontSize: 13.5, lineHeight: 1.5,
        }} />
    </div>
  );
}

function Panel({ title, children }) {
  return (
    <div style={{ border: `1px solid ${C.line}`, borderRadius: 3, padding: 16, background: C.panel, marginBottom: 14 }}>
      <div style={{ fontFamily: MONO, fontSize: 10, letterSpacing: 3, color: C.coyote, marginBottom: 12 }}>{title}</div>
      {children}
    </div>
  );
}

function HBar({ label, val, max, color = C.olive, right }) {
  const pct = max > 0 ? Math.round((val / max) * 100) : 0;
  return (
    <div style={{ marginBottom: 9 }}>
      <div style={{ display: "flex", justifyContent: "space-between", fontFamily: MONO, fontSize: 10, letterSpacing: 1.2, color: C.dim }}>
        <span>{label}</span><span style={{ color }}>{right !== undefined ? right : val}</span>
      </div>
      <div style={{ height: 6, background: C.line, borderRadius: 3, marginTop: 3 }}>
        <div style={{ width: pct + "%", height: "100%", background: color, borderRadius: 3 }} />
      </div>
    </div>
  );
}

// ---------- RESULTS + EXPORT ----------

function computeResults(ans) {
  const counts = { hard: 0, soft: 0, indiff: 0, try: 0, occas: 0, love: 0, need: 0 };
  const byRating = { hard: [], soft: [], indiff: [], try: [], occas: [], love: [], need: [] };
  const catStats = [];
  let rated = 0;
  for (const cat of CATEGORIES) {
    let sum = 0, n = 0, hardN = 0;
    for (const it of cat.items) {
      const r = ans["r_" + it.id];
      if (!r) continue;
      rated++; counts[r]++; n++; sum += SCORE[r];
      if (r === "hard") hardN++;
      byRating[r].push({ label: it.label, cat: cat.name, note: ans["n_" + it.id] || "" });
    }
    catStats.push({ name: cat.name, n, total: cat.items.length, avg: n ? sum / n : 0, hardN });
  }
  const heat = catStats.filter((c) => c.n >= 3).sort((a, b) => b.avg - a.avg);
  const limitDense = [...catStats].filter((c) => c.hardN > 0).sort((a, b) => b.hardN - a.hardN).slice(0, 4);
  return { counts, byRating, catStats, heat, limitDense, rated };
}

function buildExport(ans, r) {
  const L = [];
  L.push("# SEX MENU PROFILE — SMP-1");
  L.push("generated: " + new Date().toISOString().slice(0, 10));
  L.push("source: adlaw_sex_profiler.xlsx (Brandon The Dom sex menu template)");
  L.push("rated: " + r.rated + "/" + TOTAL_ITEMS);
  L.push("");
  L.push("## SUMMARY");
  L.push(SCALE.map((s) => s.label + ": " + r.counts[s.key]).join(" · "));
  L.push("");
  const listBlock = (title, arr, withNotes = true) => {
    L.push("## " + title);
    if (!arr.length) L.push("_none marked_");
    arr.forEach((x) => L.push("- " + x.label + " *(" + x.cat + ")*" + (withNotes && x.note ? " — " + x.note : "")));
    L.push("");
  };
  listBlock("NON-NEGOTIABLES — NEED IT", r.byRating.need);
  listBlock("HARD LIMITS", r.byRating.hard);
  listBlock("SOFT LIMITS", r.byRating.soft);
  listBlock("EXPLORATION QUEUE — TRY IT", r.byRating.try);
  L.push("## FULL MENU BY CATEGORY");
  L.push("");
  for (const cat of CATEGORIES) {
    const ratedItems = cat.items.filter((it) => ans["r_" + it.id]);
    if (!ratedItems.length) continue;
    L.push("### " + cat.name + " (" + ratedItems.length + "/" + cat.items.length + " rated)");
    for (const it of ratedItems) {
      const rt = ans["r_" + it.id];
      const note = ans["n_" + it.id];
      L.push("- " + it.label + " — **" + RATING_LABEL[rt] + "**" + (note ? " — " + note : ""));
    }
    L.push("");
  }
  const unrated = TOTAL_ITEMS - r.rated;
  if (unrated > 0) L.push("_" + unrated + " items left unrated (omitted above)._\n");
  const qAnswered = QUESTIONS.filter((q) => (ans["q_" + q.id] || "").trim());
  if (qAnswered.length) {
    L.push("## OPEN QUESTIONS");
    qAnswered.forEach((q) => { L.push("**" + q.text + "**"); L.push(ans["q_" + q.id].trim()); L.push(""); });
  }
  const hAnswered = HEALTH.filter((h) => (ans["h_" + h.id] || "").trim());
  if (hAnswered.length) {
    L.push("## HEALTH & NOTES");
    hAnswered.forEach((h) => { L.push("**" + h.text + "**"); L.push(ans["h_" + h.id].trim()); L.push(""); });
  }
  return L.join("\n");
}

function Results({ ans, onBack, onReset }) {
  const r = useMemo(() => computeResults(ans), [ans]);
  const md = useMemo(() => buildExport(ans, r), [ans, r]);
  const [copied, setCopied] = useState(false);
  const maxCount = Math.max(1, ...Object.values(r.counts));

  const copy = async () => {
    try { await navigator.clipboard.writeText(md); setCopied(true); }
    catch {
      const ta = document.getElementById("smp-md");
      if (ta) { ta.select(); try { document.execCommand("copy"); setCopied(true); } catch {} }
    }
    setTimeout(() => setCopied(false), 2000);
  };

  const list = (arr, tone) => arr.map((x, i) => (
    <div key={i} style={{ padding: "6px 0", borderBottom: i < arr.length - 1 ? `1px solid ${C.line}` : "none" }}>
      <div style={{ fontFamily: BODY, fontSize: 14, color: tone }}>{x.label}
        <span style={{ fontFamily: MONO, fontSize: 9, letterSpacing: 1, color: C.dim, marginLeft: 8 }}>{x.cat}</span>
      </div>
      {x.note && <div style={{ fontFamily: BODY, fontSize: 12, color: C.dim, marginTop: 2 }}>↳ {x.note}</div>}
    </div>
  ));
  const commaBlock = (arr) => (
    <div style={{ fontFamily: BODY, fontSize: 13.5, color: C.ink, lineHeight: 1.7 }}>
      {arr.length ? arr.map((x) => x.label).join(" · ") : <span style={{ color: C.dim }}>none marked</span>}
    </div>
  );

  return (
    <div className="fadein">
      <div style={{ border: `1px solid ${C.olive}`, borderRadius: 3, padding: "20px 18px", marginBottom: 18, background: C.panel }}>
        <div style={{ fontFamily: MONO, fontSize: 10, letterSpacing: 3, color: C.dim }}>SMP-1 // MENU DOSSIER · {new Date().toISOString().slice(0, 10)}</div>
        <div style={{ fontFamily: MONO, fontSize: 22, letterSpacing: 3, color: C.olive, fontWeight: 700, margin: "10px 0 6px" }}>SEX MENU PROFILE</div>
        <div style={{ fontFamily: MONO, fontSize: 10.5, letterSpacing: 1.5, color: C.dim, lineHeight: 1.8 }}>
          RATED {r.rated}/{TOTAL_ITEMS} · NEED {r.counts.need} · HARD LIMITS {r.counts.hard} · EXPLORATION {r.counts.try}
        </div>
      </div>

      <Panel title="RATING DISTRIBUTION">
        {SCALE.map((s) => (
          <HBar key={s.key} label={s.label.toUpperCase()} val={r.counts[s.key]} max={maxCount} color={RATING_COLOR[s.key]} />
        ))}
      </Panel>

      <Panel title="HEAT BY CATEGORY — INTEREST INDEX (0–6, MIN 3 RATED)">
        {r.heat.length === 0 && <div style={{ fontFamily: BODY, fontSize: 13, color: C.dim }}>Rate at least 3 items in a category to register heat.</div>}
        {r.heat.slice(0, 10).map((c) => (
          <HBar key={c.name} label={c.name} val={c.avg} max={6} right={c.avg.toFixed(1)} color={c.avg >= 4 ? C.oliveHi : c.avg >= 2.5 ? C.olive : C.coyote} />
        ))}
        {r.limitDense.length > 0 && (
          <div style={{ fontFamily: MONO, fontSize: 10, letterSpacing: 1.2, color: C.red, marginTop: 10, lineHeight: 1.8 }}>
            LIMIT-DENSE: {r.limitDense.map((c) => c.name + " (" + c.hardN + ")").join(" · ")}
          </div>
        )}
      </Panel>

      <Panel title={"NON-NEGOTIABLES — NEED IT (" + r.counts.need + ")"}>{r.byRating.need.length ? list(r.byRating.need, C.oliveHi) : <span style={{ fontFamily: BODY, fontSize: 13, color: C.dim }}>none marked</span>}</Panel>
      <Panel title={"HARD LIMITS (" + r.counts.hard + ")"}>{r.byRating.hard.length ? list(r.byRating.hard, C.red) : <span style={{ fontFamily: BODY, fontSize: 13, color: C.dim }}>none marked — if that's accurate, fine; if it's unexamined, revisit</span>}</Panel>
      <Panel title={"SOFT LIMITS (" + r.counts.soft + ")"}>{commaBlock(r.byRating.soft)}</Panel>
      <Panel title={"EXPLORATION QUEUE — TRY IT (" + r.counts.try + ")"}>{r.byRating.try.length ? list(r.byRating.try, C.slate) : <span style={{ fontFamily: BODY, fontSize: 13, color: C.dim }}>none marked</span>}</Panel>
      <Panel title={"GREEN BOARD — LOVE IT (" + r.counts.love + ")"}>{commaBlock(r.byRating.love)}</Panel>
      <Panel title={"ROTATION — OCCASIONALLY (" + r.counts.occas + ")"}>{commaBlock(r.byRating.occas)}</Panel>

      <Panel title="EXPORT — MARKDOWN (VAULT / PARTNER BRIEF)">
        <textarea id="smp-md" readOnly value={md} style={{
          width: "100%", height: 240, background: C.bg, color: C.ink, border: `1px solid ${C.line}`,
          borderRadius: 3, fontFamily: MONO, fontSize: 11, padding: 10, resize: "vertical", boxSizing: "border-box",
        }} />
        <button onClick={copy} style={{
          marginTop: 10, width: "100%", padding: "13px 0", borderRadius: 3, cursor: "pointer",
          fontFamily: MONO, fontSize: 12, letterSpacing: 3, fontWeight: 700,
          background: copied ? C.oliveDeep : C.olive, color: copied ? C.ink : C.bg, border: "none",
        }}>{copied ? "COPIED TO CLIPBOARD" : "COPY FULL MENU"}</button>
      </Panel>

      <div style={{ fontFamily: BODY, fontSize: 12, color: C.dim, lineHeight: 1.6, margin: "4px 0 16px" }}>
        Self-inventory and negotiation aid for consenting adults, built verbatim from your uploaded template. It records interest and limits — it does not teach technique. Edge-play and impact categories carry real physical risk; skills, safety planning, and partner negotiation live outside this form. Limits are binding, not opening offers. Ratings drift — re-run periodically.
      </div>

      <div style={{ display: "flex", gap: 10 }}>
        <button onClick={onBack} style={{ flex: 1, padding: "12px 0", borderRadius: 3, cursor: "pointer", fontFamily: MONO, fontSize: 11, letterSpacing: 2, background: "transparent", color: C.dim, border: `1px solid ${C.line}` }}>BACK TO INDEX</button>
        <button onClick={onReset} style={{ flex: 1, padding: "12px 0", borderRadius: 3, cursor: "pointer", fontFamily: MONO, fontSize: 11, letterSpacing: 2, background: "transparent", color: C.dim, border: `1px solid ${C.line}` }}>START OVER</button>
      </div>
    </div>
  );
}

// ---------- MAIN APP ----------

export default function SexMenuProfiler() {
  const [stage, setStage] = useState("intro"); // 'intro' | 'hub' | 'questions' | 'health' | 'results' | number (category index)
  const [ans, setAns] = useState({});
  const set = (id, val) => setAns((p) => {
    const n = { ...p };
    if (val === undefined || val === "") delete n[id]; else n[id] = val;
    return n;
  });

  const ratedInCat = (cat) => cat.items.filter((it) => ans["r_" + it.id]).length;
  const ratedTotal = CATEGORIES.reduce((s, c) => s + ratedInCat(c), 0);
  const qDone = QUESTIONS.filter((q) => (ans["q_" + q.id] || "").trim()).length;
  const hDone = HEALTH.filter((h) => (ans["h_" + h.id] || "").trim()).length;

  const shell = (children) => (
    <div className="smp" style={{ minHeight: "100vh", background: C.bg, padding: "0 0 60px" }}>
      <style>{STYLES}</style>
      <div style={{ maxWidth: 640, margin: "0 auto", padding: "20px 16px" }}>{children}</div>
    </div>
  );

  const hubBtn = (label, sub, done, total, onClick, tone = C.olive) => (
    <button onClick={onClick} style={{
      width: "100%", textAlign: "left", padding: "13px 14px", borderRadius: 3, cursor: "pointer",
      background: C.panel, border: `1px solid ${done > 0 ? tone : C.line}`, marginBottom: 8,
    }}>
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline" }}>
        <span style={{ fontFamily: MONO, fontSize: 12, letterSpacing: 1.5, color: done === total && total > 0 ? tone : C.ink }}>{label}</span>
        <span style={{ fontFamily: MONO, fontSize: 10, color: done > 0 ? tone : C.dim }}>{done}/{total}</span>
      </div>
      {sub && <div style={{ fontFamily: BODY, fontSize: 11.5, color: C.dim, marginTop: 3 }}>{sub}</div>}
      <div style={{ height: 3, background: C.line, borderRadius: 2, marginTop: 8 }}>
        <div style={{ width: (total ? Math.round((done / total) * 100) : 0) + "%", height: "100%", background: tone, borderRadius: 2 }} />
      </div>
    </button>
  );

  // ---- INTRO ----
  if (stage === "intro") {
    return shell(
      <div className="fadein" style={{ paddingTop: 40 }}>
        <div style={{ border: `1px solid ${C.line}`, borderRadius: 3, padding: "26px 22px", background: C.panel }}>
          <div style={{ fontFamily: MONO, fontSize: 11, letterSpacing: 4, color: C.dim }}>FORM SMP-1</div>
          <div style={{ fontFamily: MONO, fontSize: 30, letterSpacing: 2, color: C.olive, fontWeight: 700, margin: "10px 0 6px", lineHeight: 1.15 }}>
            SEX MENU PROFILE
          </div>
          <div style={{ fontFamily: MONO, fontSize: 10.5, letterSpacing: 2, color: C.coyote, marginBottom: 20 }}>
            {CATEGORIES.length} SECTIONS · {TOTAL_ITEMS} ITEMS · 7-POINT SCALE · SOURCE: YOUR UPLOADED TEMPLATE
          </div>
          <div style={{ fontFamily: BODY, fontSize: 14.5, color: C.ink, lineHeight: 1.7, marginBottom: 18 }}>
            The full menu, every item, every resolution level — Hard limit through Need it — with notes per item and the
            open questions from the sheet. Work in any order from the index. Compile whenever you want: output is a dossier
            with heat-by-category, your non-negotiables, hard lines, exploration queue, and a markdown export for the vault
            or a partner brief.
          </div>
          <div style={{ fontFamily: MONO, fontSize: 11, color: C.dim, lineHeight: 2.1, letterSpacing: 1, borderTop: `1px solid ${C.line}`, paddingTop: 14 }}>
            → RATE FROM DESIRE, NOT PERFORMANCE<br />
            → LIMITS ARE DATA, NOT FAILURES<br />
            → A LIMIT IS BINDING, NOT AN OPENING OFFER<br />
            → NOTHING LEAVES THIS SCREEN UNLESS YOU EXPORT IT
          </div>
          <button onClick={() => setStage("hub")} style={{
            marginTop: 22, width: "100%", padding: "15px 0", borderRadius: 3, cursor: "pointer",
            fontFamily: MONO, fontSize: 13, letterSpacing: 4, fontWeight: 700,
            background: C.olive, color: C.bg, border: "none",
          }}>OPEN INDEX</button>
        </div>
        <div style={{ fontFamily: BODY, fontSize: 11.5, color: C.dim, lineHeight: 1.6, marginTop: 14 }}>
          Adults only. Self-inventory and negotiation aid — records interest and limits, does not teach technique or safety.
        </div>
      </div>
    );
  }

  // ---- RESULTS ----
  if (stage === "results") {
    return shell(<Results ans={ans} onBack={() => setStage("hub")} onReset={() => { setAns({}); setStage("intro"); }} />);
  }

  // ---- QUESTIONS / HEALTH ----
  if (stage === "questions" || stage === "health") {
    const isQ = stage === "questions";
    const items = isQ ? QUESTIONS : HEALTH;
    const prefix = isQ ? "q_" : "h_";
    return shell(
      <div className="fadein">
        <div style={{ margin: "6px 0" }}><Stamp code={isQ ? "00" : "XX"} name={isQ ? "OPEN QUESTIONS" : "HEALTH & NOTES"} /></div>
        <div style={{ fontFamily: BODY, fontSize: 13.5, color: C.dim, lineHeight: 1.6, margin: "10px 0 6px" }}>
          {isQ ? "The template's long-form prompts. Write plainly — this is the part a partner actually reads." : "Safety and logistics block from the template. Fill what applies."}
        </div>
        <div>{items.map((it) => <TextBlock key={it.id} item={it} value={ans[prefix + it.id]} onSet={(v) => set(prefix + it.id, v)} />)}</div>
        <button onClick={() => setStage("hub")} style={{
          marginTop: 20, width: "100%", padding: "13px 0", borderRadius: 3, cursor: "pointer",
          fontFamily: MONO, fontSize: 12, letterSpacing: 3, fontWeight: 700, background: C.olive, color: C.bg, border: "none",
        }}>BACK TO INDEX</button>
      </div>
    );
  }

  // ---- CATEGORY SCREEN ----
  if (typeof stage === "number") {
    const cat = CATEGORIES[stage];
    const done = ratedInCat(cat);
    const last = stage === CATEGORIES.length - 1;
    return shell(
      <div className="fadein" key={cat.name}>
        <div style={{ position: "sticky", top: 0, background: C.bg, padding: "10px 0 12px", zIndex: 5 }}>
          <div style={{ display: "flex", justifyContent: "space-between", fontFamily: MONO, fontSize: 10, letterSpacing: 2, color: C.dim, marginBottom: 6 }}>
            <span>SECTION {String(stage + 1).padStart(2, "0")}/{CATEGORIES.length}</span>
            <span>THIS SECTION {done}/{cat.items.length} · TOTAL {ratedTotal}/{TOTAL_ITEMS}</span>
          </div>
          <div style={{ height: 3, background: C.line, borderRadius: 2 }}>
            <div style={{ width: Math.round((ratedTotal / TOTAL_ITEMS) * 100) + "%", height: "100%", background: C.olive, borderRadius: 2 }} />
          </div>
        </div>
        <div style={{ margin: "12px 0 0" }}><Stamp code={String(stage + 1).padStart(2, "0")} name={cat.name} /></div>
        <Legend />
        <div>{cat.items.map((it) => (
          <MenuItem key={it.id} item={it} rating={ans["r_" + it.id]} note={ans["n_" + it.id]}
            onRate={(v) => set("r_" + it.id, v)} onNote={(v) => set("n_" + it.id, v)} />
        ))}</div>
        <div style={{ display: "flex", gap: 10, marginTop: 22 }}>
          <button onClick={() => setStage("hub")} style={{ padding: "13px 16px", borderRadius: 3, cursor: "pointer", fontFamily: MONO, fontSize: 11, letterSpacing: 2, background: "transparent", color: C.dim, border: `1px solid ${C.line}` }}>INDEX</button>
          {stage > 0 && <button onClick={() => setStage(stage - 1)} style={{ padding: "13px 16px", borderRadius: 3, cursor: "pointer", fontFamily: MONO, fontSize: 11, letterSpacing: 2, background: "transparent", color: C.dim, border: `1px solid ${C.line}` }}>PREV</button>}
          <button onClick={() => setStage(last ? "hub" : stage + 1)} style={{
            flex: 1, padding: "13px 0", borderRadius: 3, cursor: "pointer", fontFamily: MONO, fontSize: 12, letterSpacing: 3, fontWeight: 700,
            background: C.olive, color: C.bg, border: "none",
          }}>{last ? "BACK TO INDEX" : "NEXT SECTION"}</button>
        </div>
      </div>
    );
  }

  // ---- HUB / INDEX ----
  return shell(
    <div className="fadein">
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "baseline", margin: "6px 0 4px" }}>
        <div>
          <div style={{ fontFamily: MONO, fontSize: 10, letterSpacing: 3, color: C.dim }}>SMP-1 // INDEX</div>
          <div style={{ fontFamily: MONO, fontSize: 20, letterSpacing: 3, color: C.olive, fontWeight: 700 }}>MENU SECTIONS</div>
        </div>
        <div style={{ fontFamily: MONO, fontSize: 10.5, color: C.coyote, letterSpacing: 1.5 }}>{ratedTotal}/{TOTAL_ITEMS}</div>
      </div>
      <div style={{ height: 3, background: C.line, borderRadius: 2, margin: "8px 0 16px" }}>
        <div style={{ width: Math.round((ratedTotal / TOTAL_ITEMS) * 100) + "%", height: "100%", background: C.olive, borderRadius: 2 }} />
      </div>

      {hubBtn("OPEN QUESTIONS", "Long-form prompts — sub/dom meaning, feelings sought, disclosures", qDone, QUESTIONS.length, () => setStage("questions"), C.coyote)}
      {CATEGORIES.map((cat, i) => hubBtn(
        String(i + 1).padStart(2, "0") + " · " + cat.name, null, ratedInCat(cat), cat.items.length, () => setStage(i)
      ))}
      {hubBtn("HEALTH & NOTES", "Allergies, medical, testing, anything else", hDone, HEALTH.length, () => setStage("health"), C.coyote)}

      <button onClick={() => setStage("results")} style={{
        marginTop: 14, width: "100%", padding: "15px 0", borderRadius: 3, cursor: "pointer",
        fontFamily: MONO, fontSize: 13, letterSpacing: 4, fontWeight: 700,
        background: ratedTotal > 0 ? C.olive : C.panel2, color: ratedTotal > 0 ? C.bg : C.dim,
        border: `1px solid ${ratedTotal > 0 ? C.olive : C.line}`,
      }}>COMPILE DOSSIER {ratedTotal > 0 ? "" : "(RATE ITEMS FIRST)"}</button>
      <div style={{ fontFamily: BODY, fontSize: 11.5, color: C.dim, marginTop: 10, lineHeight: 1.6 }}>
        Work in any order. Nothing saves between sessions — export from the dossier before closing.
      </div>
    </div>
  );
}
