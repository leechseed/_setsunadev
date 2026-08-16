---
original_path: "/mnt/user-data/outputs/sex-menu-profiler.jsx"
source_conversation: "Male romantic relationship profiling questionnaires"
created: 2026-07-15
trunk: ORANGE
kind: generated-file
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
