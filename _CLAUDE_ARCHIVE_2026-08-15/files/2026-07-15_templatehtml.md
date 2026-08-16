---
original_path: "/home/claude/dpapp/template.html"
source_conversation: "Unified profiler UI with markdown export"
created: 2026-07-15
trunk: BOTH
kind: generated-file
---

<!doctype html>
<!-- Desire Profile — Mission Control v2. One file: tracker + Sex Menu (SMP-1) + Relationship Needs (RNP-1), unified autosave + one markdown archive. -->
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Desire Profile — Mission Control</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Bebas+Neue&family=Spectral:ital,wght@0,400;0,500;0,600;1,400&family=JetBrains+Mono:wght@400;500;700&display=swap" rel="stylesheet">
<style>
  :root{
    --bg:#0b0908; --bg2:#0f0c0a; --panel:#151010; --panel2:#1c1512; --raise:#241a15;
    --ink:#ece0cf; --ink2:#cdbfac; --muted:#8a7a68; --faint:#5a4d40;
    --ember:#ff7a2f; --ember-dim:#b8531f; --amber:#f4ad52; --gold:#ffcf7a;
    --blood:#c0392b; --ok:#e08a3c;
    --line:#2b211a; --line2:#3a2c21;
    --glow:0 0 18px rgba(255,122,47,.25);
    --font-disp:"Bebas Neue",sans-serif; --font-body:"Spectral",Georgia,serif; --font-mono:"JetBrains Mono",monospace;
  }
  *{box-sizing:border-box}
  html,body{margin:0}
  body{
    background:
      radial-gradient(1200px 700px at 88% -10%, rgba(255,122,47,.10), transparent 60%),
      radial-gradient(900px 600px at 0% 110%, rgba(192,57,43,.08), transparent 55%),
      var(--bg);
    color:var(--ink); font-family:var(--font-body); line-height:1.5;
    -webkit-font-smoothing:antialiased; min-height:100vh;
  }
  body::before{ /* grain */
    content:""; position:fixed; inset:0; pointer-events:none; opacity:.05; z-index:9999;
    background-image:url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
  }
  .wrap{max-width:1180px; margin:0 auto; padding:26px 20px 70px}
  a{color:var(--amber); text-decoration:none; border-bottom:1px dotted var(--ember-dim)}
  a:hover{color:var(--gold)}
  .boot{min-height:100vh;display:flex;align-items:center;justify-content:center;font-family:var(--font-mono);font-size:12px;letter-spacing:4px;color:var(--muted)}

  /* ---- header ---- */
  .top{display:flex; flex-wrap:wrap; align-items:flex-end; justify-content:space-between; gap:14px; padding-bottom:14px; border-bottom:1px solid var(--line)}
  .brand{display:flex; align-items:center; gap:14px}
  .reticle{width:34px;height:34px;border:1px solid var(--ember-dim);border-radius:50%;position:relative;flex:0 0 auto;box-shadow:var(--glow)}
  .reticle::before,.reticle::after{content:"";position:absolute;background:var(--ember)}
  .reticle::before{left:50%;top:5px;bottom:5px;width:1px;transform:translateX(-.5px)}
  .reticle::after{top:50%;left:5px;right:5px;height:1px;transform:translateY(-.5px)}
  .reticle i{position:absolute;inset:11px;border-radius:50%;background:var(--ember);box-shadow:var(--glow);animation:pulse 3.4s ease-in-out infinite}
  @keyframes pulse{0%,100%{opacity:.55}50%{opacity:1}}
  h1{font-family:var(--font-disp); font-weight:400; font-size:39px; letter-spacing:2px; margin:0; line-height:.92}
  h1 span{color:var(--ember)}
  .sub{font-family:var(--font-mono); font-size:10.5px; letter-spacing:3px; color:var(--muted); text-transform:uppercase; margin-top:3px}
  .meta-r{font-family:var(--font-mono); font-size:10px; letter-spacing:2px; color:var(--faint); text-align:right; text-transform:uppercase}
  .meta-r b{color:var(--ink2);font-weight:500}
  .dot{display:inline-block;width:7px;height:7px;border-radius:50%;background:var(--ember);box-shadow:var(--glow);margin-right:5px;vertical-align:middle}
  .dot.warn{background:var(--amber);box-shadow:0 0 10px rgba(244,173,82,.4)}

  /* ---- station rail (tabs) ---- */
  .tabs{display:flex; gap:8px; margin:16px 0 4px; flex-wrap:wrap}
  .tab{display:flex; align-items:center; gap:10px; font-family:var(--font-mono); font-size:11px; letter-spacing:2px; text-transform:uppercase;
    background:#171010; color:var(--muted); border:1px solid var(--line2); border-bottom:2px solid var(--line2);
    border-radius:7px 7px 0 0; padding:11px 16px; cursor:pointer; transition:.15s}
  .tab em{font-style:normal; font-size:9.5px; letter-spacing:1px; color:var(--faint); border:1px solid var(--line2); border-radius:4px; padding:2px 6px}
  .tab:hover{color:var(--ink2); border-color:var(--ember-dim)}
  .tab.on{background:linear-gradient(180deg,var(--panel2),var(--panel)); color:var(--gold); border-color:var(--ember);
    border-bottom-color:var(--ember); box-shadow:var(--glow)}
  .tab.on em{color:var(--amber); border-color:var(--ember-dim)}

  /* ---- status strip ---- */
  .status{display:grid; grid-template-columns:1.4fr 1fr; gap:14px; margin:18px 0 22px}
  @media(max-width:740px){.status{grid-template-columns:1fr}}
  .card{background:linear-gradient(180deg,var(--panel2),var(--panel)); border:1px solid var(--line); border-radius:10px; padding:16px 18px; position:relative; overflow:hidden}
  .card::after{content:"";position:absolute;top:8px;right:8px;width:18px;height:18px;border-top:1px solid var(--line2);border-right:1px solid var(--line2);opacity:.7}
  .lbl{font-family:var(--font-mono); font-size:9.5px; letter-spacing:2.5px; color:var(--muted); text-transform:uppercase; margin-bottom:9px}
  .objective .obj-title{font-family:var(--font-disp); font-size:25px; letter-spacing:1px; color:var(--gold); line-height:1.02}
  .objective .obj-detail{color:var(--ink2); font-size:14.5px; margin-top:7px}
  .objective .obj-detail em{color:var(--ember);font-style:normal}
  .gauge-wrap{display:flex; align-items:center; gap:14px}
  .pct{font-family:var(--font-disp); font-size:46px; color:var(--ember); line-height:.8; min-width:96px}
  .pct small{font-family:var(--font-mono);font-size:13px;color:var(--muted);letter-spacing:1px}
  .segs{display:flex; gap:3px; flex:1; height:24px}
  .seg{flex:1; border-radius:2px; background:#241a14; border:1px solid #2e221a; transition:.25s}
  .seg.on{background:linear-gradient(180deg,var(--amber),var(--ember)); border-color:var(--ember); box-shadow:0 0 7px rgba(255,122,47,.5)}
  .gnote{font-family:var(--font-mono); font-size:10px; letter-spacing:1.5px; color:var(--faint); margin-top:10px; text-transform:uppercase}

  /* ---- stations grid ---- */
  .grid{display:grid; grid-template-columns:repeat(2,1fr); gap:16px}
  @media(max-width:740px){.grid{grid-template-columns:1fr}}
  .station{background:linear-gradient(180deg,var(--panel),#120e0c); border:1px solid var(--line); border-radius:11px; padding:0; opacity:0; transform:translateY(8px); animation:rise .5s forwards}
  @keyframes rise{to{opacity:1;transform:none}}
  @media (prefers-reduced-motion: reduce){ .station{animation:none; opacity:1; transform:none} .reticle i{animation:none} }
  .st-head{display:flex; align-items:center; justify-content:space-between; padding:13px 16px; border-bottom:1px solid var(--line); background:rgba(255,122,47,.03)}
  .st-name{font-family:var(--font-disp); font-size:21px; letter-spacing:1px; color:var(--ink)}
  .st-name b{color:var(--ember-dim); font-weight:400}
  .led{font-family:var(--font-mono); font-size:9px; letter-spacing:2px; color:var(--muted); display:flex; align-items:center; gap:6px; text-transform:uppercase}
  .led i{width:8px;height:8px;border-radius:50%;background:#3a2c21;display:inline-block}
  .led.part i{background:var(--amber);box-shadow:0 0 7px rgba(244,173,82,.5)}
  .led.full i{background:var(--ember);box-shadow:var(--glow)}
  .st-body{padding:12px 16px 16px}

  .row{display:flex; align-items:center; gap:11px; padding:7px 0}
  .row + .row{border-top:1px dashed #221913}
  .tog{flex:0 0 auto; width:34px; height:20px; border-radius:4px; border:1px solid var(--line2); background:#171010; position:relative; cursor:pointer; transition:.18s}
  .tog::after{content:""; position:absolute; top:2px; left:2px; width:14px; height:14px; border-radius:3px; background:#4a3a2e; transition:.18s}
  .tog.on{background:linear-gradient(180deg,var(--amber),var(--ember-dim)); border-color:var(--ember)}
  .tog.on::after{left:16px; background:#fff3e3; box-shadow:0 0 8px rgba(255,243,227,.7)}
  .row label{flex:1; cursor:pointer; font-size:14.5px; color:var(--ink2)}
  .row.done label{color:var(--faint); text-decoration:line-through; text-decoration-color:var(--ember-dim)}
  .go{font-family:var(--font-mono); font-size:9.5px; letter-spacing:1px; padding:3px 8px; border:1px solid var(--line2); border-radius:4px; color:var(--amber); text-transform:uppercase; white-space:nowrap}
  .go:hover{border-color:var(--ember); color:var(--gold)}
  .asbtn{background:none; cursor:pointer}

  textarea, input.txt{width:100%; background:#100b09; border:1px solid var(--line2); border-radius:6px; color:var(--ink); font-family:var(--font-body); font-size:14px; padding:9px 11px; resize:vertical; outline:none}
  textarea:focus, input.txt:focus{border-color:var(--ember-dim); box-shadow:0 0 0 2px rgba(255,122,47,.10)}
  textarea::placeholder, input::placeholder{color:#5a4c3f}
  .note-lbl{font-family:var(--font-mono); font-size:9px; letter-spacing:1.5px; color:var(--muted); margin:11px 0 5px; text-transform:uppercase}
  .qrow{display:grid; grid-template-columns:auto 1fr; gap:8px 11px; align-items:center; padding:8px 0}
  .qrow + .qrow{border-top:1px dashed #221913}
  .qrow .qmeta{display:flex; align-items:center; gap:9px; min-width:0}
  .qrow .qmeta label{font-size:13.5px; cursor:pointer}
  .qrow input.txt{grid-column:2; font-size:13px; padding:6px 9px}
  .synrow{display:flex;align-items:center;gap:9px;padding:5px 0}
  .synrow .n{font-family:var(--font-disp);font-size:18px;color:var(--ember-dim);width:18px;text-align:center}

  .dockline{display:flex;align-items:center;justify-content:space-between;gap:10px;margin-top:12px;padding:9px 11px;
    border:1px dashed var(--line2);border-radius:6px;background:rgba(255,122,47,.04)}
  .dockstat{font-family:var(--font-mono);font-size:9.5px;letter-spacing:1.5px;color:var(--amber)}
  .auxbody{font-size:14px;color:var(--ink2);line-height:1.55}

  /* ---- dock: coach + ideas ---- */
  .dock{display:grid; grid-template-columns:1.25fr 1fr; gap:16px; margin-top:16px}
  @media(max-width:860px){.dock{grid-template-columns:1fr}}
  .coach .st-head{background:linear-gradient(90deg,rgba(192,57,43,.10),rgba(255,122,47,.04))}
  .clog{height:300px; overflow-y:auto; padding:14px 16px; display:flex; flex-direction:column; gap:11px; scrollbar-width:thin}
  .msg{max-width:88%; padding:9px 12px; border-radius:9px; font-size:14px; white-space:pre-wrap}
  .msg.user{align-self:flex-end; background:#241a14; border:1px solid var(--line2); color:var(--ink)}
  .msg.coach{align-self:flex-start; background:linear-gradient(180deg,#1a1310,#140f0d); border:1px solid var(--line2); border-left:2px solid var(--ember)}
  .msg.sys{align-self:center; font-family:var(--font-mono); font-size:10.5px; letter-spacing:1px; color:var(--amber); background:transparent; border:1px dashed var(--line2)}
  .msg.coach b.name{display:block; font-family:var(--font-mono); font-size:9px; letter-spacing:2px; color:var(--ember); text-transform:uppercase; margin-bottom:4px; font-weight:700}
  .greet{color:var(--muted); font-size:13.5px; text-align:center; padding:18px 10px; line-height:1.6}
  .cinput{display:flex; gap:8px; padding:11px 12px; border-top:1px solid var(--line)}
  .cinput textarea{height:42px; min-height:42px}
  .send{flex:0 0 auto; font-family:var(--font-mono); font-size:11px; letter-spacing:1.5px; text-transform:uppercase; background:linear-gradient(180deg,var(--ember),var(--ember-dim)); color:#1a0e07; border:none; border-radius:6px; padding:0 16px; font-weight:700; cursor:pointer}
  .send:hover{filter:brightness(1.1)} .send:disabled{opacity:.5; cursor:wait}
  .typing{display:inline-flex;gap:4px;align-items:center}
  .typing i{width:5px;height:5px;border-radius:50%;background:var(--ember);animation:blink 1.1s infinite}
  .typing i:nth-child(2){animation-delay:.18s}.typing i:nth-child(3){animation-delay:.36s}
  @keyframes blink{0%,80%,100%{opacity:.25}40%{opacity:1}}

  .ideasbody{display:flex;flex-direction:column;gap:10px}
  .idea-add{display:flex;gap:8px}
  .ideic{display:flex;flex-direction:column;gap:7px;max-height:230px;overflow-y:auto;scrollbar-width:thin}
  .idea{display:flex;align-items:flex-start;gap:9px;background:#140f0c;border:1px solid var(--line);border-radius:6px;padding:8px 10px;font-size:13.5px;color:var(--ink2)}
  .idea .x{margin-left:auto;cursor:pointer;color:var(--faint);font-family:var(--font-mono);flex:0 0 auto}
  .idea .x:hover{color:var(--blood)}
  .idea .pin{color:var(--ember-dim);flex:0 0 auto}
  .empty{color:var(--faint);font-size:13px;font-style:italic;padding:6px 2px}

  /* ---- forms pane ---- */
  .pane-form{margin-top:6px}
  .pane-form > div{min-height:auto !important}

  /* ---- controls ---- */
  .controls{display:flex;flex-wrap:wrap;gap:10px;margin-top:22px;padding-top:18px;border-top:1px solid var(--line)}
  .btn{font-family:var(--font-mono);font-size:10.5px;letter-spacing:1.5px;text-transform:uppercase;background:#191210;color:var(--ink2);border:1px solid var(--line2);border-radius:6px;padding:9px 14px;cursor:pointer;transition:.15s}
  .btn:hover{border-color:var(--ember);color:var(--gold)}
  .btn.hot{background:linear-gradient(180deg,var(--ember),var(--ember-dim));color:#1a0e07;font-weight:700;border-color:var(--ember)}
  .btn.hot:hover{filter:brightness(1.1);color:#1a0e07}
  .btn.danger:hover{border-color:var(--blood);color:#ff6b5c}
  .privacy{font-family:var(--font-mono);font-size:10px;letter-spacing:1px;color:var(--faint);margin-left:auto;align-self:center;text-transform:uppercase}

  .toast{position:fixed;bottom:22px;left:50%;transform:translateX(-50%) translateY(20px);background:#1c1512;border:1px solid var(--ember-dim);color:var(--gold);font-family:var(--font-mono);font-size:12px;letter-spacing:1px;padding:11px 18px;border-radius:8px;opacity:0;transition:.3s;z-index:10000;box-shadow:var(--glow);pointer-events:none;max-width:86vw;text-align:center}
  .toast.show{opacity:1;transform:translateX(-50%) translateY(0)}
  ::-webkit-scrollbar{width:9px}::-webkit-scrollbar-thumb{background:#2e221a;border-radius:5px}
</style>
</head>
<body>
<div id="root"></div>
<script>/*__APP_JS__*/</script>
</body>
</html>
