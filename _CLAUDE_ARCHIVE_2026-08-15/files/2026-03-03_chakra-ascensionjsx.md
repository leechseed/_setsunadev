---
original_path: "/mnt/user-data/outputs/chakra_ascension.jsx"
source_conversation: "Summarizing Feeling is the Secret by Neville Goddard"
created: 2026-03-03
trunk: BLACK
kind: generated-file
---

import { useState, useEffect, useCallback, useRef } from "react";

const CHAKRAS = [
  {
    name: "MULADHARA",
    subtitle: "Root — Survival",
    color: "#E63946",
    glow: "rgba(230,57,70,0.6)",
    bgGrad: "linear-gradient(135deg, #1a0000 0%, #2d0a0a 40%, #0d0d0d 100%)",
    symbol: "◆",
    description: "Confront your survival fear. What actually keeps you alive — and what's just anxiety in disguise?",
    scenarios: [
      {
        prompt: "You've been offered a stable corporate job. It pays well but deadens your soul. Your savings can cover 6 months. What do you do?",
        choices: [
          { text: "Take the job. Security first.", alignment: -1, feedback: "Survival fear made this choice for you. You didn't even check what you actually need." },
          { text: "Calculate your real monthly burn rate before deciding.", alignment: 2, feedback: "You confronted the fear with data. Your actual needs are far less than your anxiety assumed." },
          { text: "Reject it immediately — money doesn't matter.", alignment: 0, feedback: "Brave, but denial of material reality isn't grounding. The first chakra demands honesty, not bravado." },
          { text: "Negotiate part-time so you can build your real work on the side.", alignment: 1, feedback: "A pragmatic bridge. You honored survival without surrendering to it completely." }
        ]
      },
      {
        prompt: "Your family says your creative ambitions are 'not realistic.' You feel the weight of their disapproval. What do you do?",
        choices: [
          { text: "They're right. I need to be practical.", alignment: -1, feedback: "Whose survival fear are you carrying — yours or theirs?" },
          { text: "Examine what 'realistic' actually means — run the numbers on what you truly need.", alignment: 2, feedback: "You separated inherited fear from material fact. The root chakra clears." },
          { text: "Cut them off. They don't understand.", alignment: 0, feedback: "Reactivity isn't grounding. You're still being moved by their energy, just in reverse." },
          { text: "Thank them, then quietly continue your own inquiry.", alignment: 1, feedback: "Grounded. You didn't fight and you didn't fold." }
        ]
      }
    ]
  },
  {
    name: "SVADHISTHANA",
    subtitle: "Sacral — Desire",
    color: "#F77F00",
    glow: "rgba(247,127,0,0.6)",
    bgGrad: "linear-gradient(135deg, #1a0d00 0%, #2d1a00 40%, #0d0d0d 100%)",
    symbol: "◎",
    description: "Recover what you actually want. Not what you should want. Not what's marketable. What makes you alive.",
    scenarios: [
      {
        prompt: "You're asked: 'What do you really want to do with your life?' You notice your mind goes blank. What do you do?",
        choices: [
          { text: "Say something impressive that sounds good.", alignment: -1, feedback: "You performed desire instead of feeling it. The sacral chakra stays locked." },
          { text: "Sit with the blankness. Ask your body what excites it. Follow the sensation.", alignment: 2, feedback: "You trusted somatic intelligence over social performance. Desire begins to surface." },
          { text: "List your skills and find the most profitable application.", alignment: -1, feedback: "You answered a different question. The market's desire is not your desire." },
          { text: "Recall the last time you lost track of time doing something. Start there.", alignment: 2, feedback: "Flow states are second-chakra breadcrumbs. You're following the right trail." }
        ]
      },
      {
        prompt: "You discover a deep pull toward an art form you abandoned at age 14. It's 'impractical.' The pull won't stop. What do you do?",
        choices: [
          { text: "Ignore it. You're an adult now.", alignment: -1, feedback: "You just told your authentic desire to shut up. The sacral chakra dims." },
          { text: "Give yourself permission to explore it — even 30 minutes a week.", alignment: 2, feedback: "Permission to want is the radical act. The second chakra opens." },
          { text: "Immediately quit your job to pursue it full-time.", alignment: 0, feedback: "Enthusiasm without grounding. You skipped the first chakra's lesson." },
          { text: "Research how others have monetized it.", alignment: 0, feedback: "You're already packaging it for the market before you've even let yourself feel it." }
        ]
      }
    ]
  },
  {
    name: "MANIPURA",
    subtitle: "Solar Plexus — Power",
    color: "#FCBF49",
    glow: "rgba(252,191,73,0.6)",
    bgGrad: "linear-gradient(135deg, #1a1500 0%, #2d2200 40%, #0d0d0d 100%)",
    symbol: "△",
    description: "Reclaim your authority. Stop waiting for permission. Define yourself through action.",
    scenarios: [
      {
        prompt: "A gatekeeper in your industry tells you your work 'isn't ready' and you should 'pay your dues' for a few more years. What do you do?",
        choices: [
          { text: "They probably know best. Wait.", alignment: -1, feedback: "You just handed your vocational power to someone else's timeline." },
          { text: "Evaluate their feedback honestly, then decide FOR YOURSELF whether it applies.", alignment: 2, feedback: "You neither submitted nor rebelled. You exercised sovereign judgment. The third chakra ignites." },
          { text: "Rage-post about gatekeepers online.", alignment: -1, feedback: "Reactivity is surrendered power wearing a mask of defiance." },
          { text: "Find a way around the gatekeeper entirely.", alignment: 1, feedback: "Strategic agency. You refused to let one person's opinion become your ceiling." }
        ]
      },
      {
        prompt: "You've been 'preparing' to launch your project for 18 months. Research, courses, certifications. You're still not 'ready.' What do you do?",
        choices: [
          { text: "Sign up for one more course. Almost there.", alignment: -1, feedback: "Infinite preparation is a power leak disguised as diligence." },
          { text: "Launch it today. Imperfect. Incomplete. Yours.", alignment: 2, feedback: "You chose definition through action over definition through credentials. The solar plexus blazes." },
          { text: "Ask a mentor if you're ready.", alignment: 0, feedback: "Seeking counsel can be wise, but 'Am I ready?' is a question only your third chakra can answer." },
          { text: "Set a hard deadline: two weeks, then it ships no matter what.", alignment: 1, feedback: "You created a commitment structure. The will has something to push against." }
        ]
      }
    ]
  },
  {
    name: "ANAHATA",
    subtitle: "Heart — Compassion",
    color: "#2A9D8F",
    glow: "rgba(42,157,143,0.6)",
    bgGrad: "linear-gradient(135deg, #001a17 0%, #002d26 40%, #0d0d0d 100%)",
    symbol: "✦",
    description: "THE PIVOT POINT. Your work must serve something beyond yourself — or it will eventually hollow out.",
    scenarios: [
      {
        prompt: "Your business is profitable and growing. But you feel a creeping emptiness. Something is missing. What do you do?",
        choices: [
          { text: "Push harder. Scale faster. The emptiness will fill itself.", alignment: -1, feedback: "More of what caused the emptiness won't cure it. The lower triad alone cannot sustain meaning." },
          { text: "Ask: 'Who does my work actually help? What suffering does it address?'", alignment: 2, feedback: "The heart chakra question. You just crossed the pivot point." },
          { text: "Add a charity donation feature and call it purpose.", alignment: 0, feedback: "Bolted-on compassion. The heart chakra demands integration, not accessories." },
          { text: "Burn it down and start a nonprofit.", alignment: 0, feedback: "Overcorrection. Service doesn't require abandoning everything you've built." }
        ]
      },
      {
        prompt: "A colleague is struggling. Helping them would cost you time on your own project. What do you do?",
        choices: [
          { text: "Not my problem. I need to focus.", alignment: -1, feedback: "Efficient. But the heart stays closed, and your work loses a dimension." },
          { text: "Help them — and notice how it changes the quality of your own work afterward.", alignment: 2, feedback: "Generosity as practice. The heart chakra opens and floods the whole system." },
          { text: "Help them but keep a mental ledger of favors owed.", alignment: -1, feedback: "Transactional compassion isn't compassion. That's the third chakra pretending to be the fourth." },
          { text: "Connect them with someone else who can help.", alignment: 1, feedback: "Service doesn't always mean direct action. Routing is its own form of care." }
        ]
      }
    ]
  },
  {
    name: "VISHUDDHA",
    subtitle: "Throat — Expression",
    color: "#457B9D",
    glow: "rgba(69,123,157,0.6)",
    bgGrad: "linear-gradient(135deg, #000d1a 0%, #001a2d 40%, #0d0d0d 100%)",
    symbol: "◇",
    description: "Your work must carry YOUR voice. Not the market's voice. Not your mentor's voice. Yours.",
    scenarios: [
      {
        prompt: "Your audience responds best to work that feels safe and familiar. But your authentic creative direction is stranger, harder, weirder. What do you do?",
        choices: [
          { text: "Give them what they want. Audience knows best.", alignment: -1, feedback: "You just silenced your creative signature to optimize engagement metrics." },
          { text: "Make the weird thing. Ship it. Let the audience catch up.", alignment: 2, feedback: "Voice over approval. The throat chakra opens and your work becomes unmistakably yours." },
          { text: "A/B test both versions.", alignment: 0, feedback: "Data won't tell you who you are. The fifth chakra isn't a hypothesis to validate." },
          { text: "Gradually introduce your real voice, one piece at a time.", alignment: 1, feedback: "Strategic revelation. Not as bold, but the voice is moving forward." }
        ]
      },
      {
        prompt: "Your work is 90% done. It's good. But you keep polishing, refining, not releasing. What's happening?",
        choices: [
          { text: "It's just not perfect yet. One more pass.", alignment: -1, feedback: "Perfectionism is the fifth chakra's favorite cage. Expression requires release." },
          { text: "Recognize the fear. Hit publish. Let it be imperfect and YOURS.", alignment: 2, feedback: "The word became flesh. The throat chakra completes its function: making the invisible visible." },
          { text: "Get feedback from 10 trusted people first.", alignment: 0, feedback: "Consensus-seeking before release can be wisdom or delay. Check your motive." },
          { text: "Release it anonymously to test the waters.", alignment: 0, feedback: "Expression without identity isn't full expression. The fifth chakra asks you to stand behind your voice." }
        ]
      }
    ]
  },
  {
    name: "AJNA",
    subtitle: "Third Eye — Vision",
    color: "#6A4C93",
    glow: "rgba(106,76,147,0.6)",
    bgGrad: "linear-gradient(135deg, #0d001a 0%, #1a002d 40%, #0d0d0d 100%)",
    symbol: "◈",
    description: "Trust what you see that others can't. Synchronicity, intuition, the vision that logic cannot produce.",
    scenarios: [
      {
        prompt: "Every rational analysis says your idea won't work. But something deeper — a persistent vision, a recurring dream — says otherwise. What do you do?",
        choices: [
          { text: "Trust the data. Dreams don't pay bills.", alignment: -1, feedback: "The rational mind is useful for execution but limited as a compass. You just fired your navigator." },
          { text: "Hold both. Act on the vision while staying attentive to reality.", alignment: 2, feedback: "Sixth-chakra mastery: you honored the vision without abandoning discernment. The third eye opens." },
          { text: "Follow the vision blindly. Logic is a trap.", alignment: 0, feedback: "Vision without grounding is fantasy. The sixth chakra works WITH the lower centers, not against them." },
          { text: "Wait for a clearer sign.", alignment: 0, feedback: "The sign is the persistent vision itself. Waiting for certainty is a way of refusing to see." }
        ]
      },
      {
        prompt: "A strange synchronicity occurs: a stranger mentions the exact idea you've been privately developing. You feel a chill of recognition. What do you do?",
        choices: [
          { text: "Coincidence. Ignore it.", alignment: -1, feedback: "The sixth chakra offered a signal. You classified it as noise." },
          { text: "Receive it as confirmation. Let it deepen your commitment.", alignment: 2, feedback: "You recognized the pattern. Synchronicity is the sixth chakra's language, and you just became fluent." },
          { text: "Panic — someone is going to beat you to it.", alignment: -1, feedback: "Scarcity consciousness. That's the first chakra hijacking a sixth-chakra moment." },
          { text: "Approach the stranger and explore the connection.", alignment: 1, feedback: "Active engagement with synchronicity. The vision becomes relational." }
        ]
      }
    ]
  },
  {
    name: "SAHASRARA",
    subtitle: "Crown — Sacred Livelihood",
    color: "#E8E8E8",
    glow: "rgba(232,232,232,0.6)",
    bgGrad: "linear-gradient(135deg, #0d0d0d 0%, #1a1a2e 40%, #0d0d15 100%)",
    symbol: "❋",
    description: "Work becomes practice. Livelihood becomes prayer. You are not the sole author — something larger moves through you.",
    scenarios: [
      {
        prompt: "You've achieved alignment across all dimensions. Your work is grounded, desired, powerful, compassionate, expressive, and visionary. Now what?",
        choices: [
          { text: "Optimize. Scale. Dominate the market.", alignment: -1, feedback: "You just collapsed the crown chakra back into the third. Power without surrender is just ambition." },
          { text: "Surrender attachment to outcomes. Work with full commitment. Let the results belong to something larger.", alignment: 2, feedback: "Sacred livelihood. The work is the practice. The practice is the offering. The crown opens." },
          { text: "Teach others what you've learned.", alignment: 1, feedback: "Beautiful — if it emerges from overflow rather than identity. Service through transmission." },
          { text: "Retire. You've made it.", alignment: -1, feedback: "The crown chakra isn't an endpoint. It's a way of being in perpetual creative engagement." }
        ]
      },
      {
        prompt: "You wake up and realize: the work you do IS your spiritual practice. There is no separation between livelihood and life. How does this change things?",
        choices: [
          { text: "It doesn't. I just keep working, but now with full presence.", alignment: 2, feedback: "That's it. That's the whole teaching. The seven centers sing as one. You have arrived — not at a destination, but at a way of being." },
          { text: "I should formalize this into a philosophy and brand it.", alignment: -1, feedback: "The ego just tried to own the transcendent. The crown chakra closes." },
          { text: "I feel gratitude. And I feel the weight of responsibility.", alignment: 1, feedback: "Honest. The crown doesn't eliminate the human — it illuminates it." },
          { text: "I'm afraid I'll lose this feeling.", alignment: 0, feedback: "Fear of loss is the first chakra echoing upward. Let it pass. The feeling isn't yours to hold — it holds you." }
        ]
      }
    ]
  }
];

const RANKS = [
  { min: 0, title: "Résumé Slave", desc: "Still trapped in the career paradigm." },
  { min: 5, title: "Restless Seeker", desc: "You sense something more but can't name it yet." },
  { min: 10, title: "Anti-Careerist", desc: "You've rejected the old model. Now build the new one." },
  { min: 15, title: "Dharma Apprentice", desc: "Your authentic path is taking shape." },
  { min: 20, title: "Chakra Walker", desc: "Moving through the centers with awareness." },
  { min: 24, title: "Sacred Worker", desc: "Livelihood and life are becoming one." },
  { min: 28, title: "Awakened Vessel", desc: "Your work is your offering to the whole." }
];

function getRank(score) {
  let rank = RANKS[0];
  for (const r of RANKS) {
    if (score >= r.min) rank = r;
  }
  return rank;
}

function Particles({ color }) {
  const canvasRef = useRef(null);
  const particlesRef = useRef([]);
  const animRef = useRef(null);

  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;
    const ctx = canvas.getContext("2d");
    canvas.width = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;

    particlesRef.current = Array.from({ length: 40 }, () => ({
      x: Math.random() * canvas.width,
      y: Math.random() * canvas.height,
      vx: (Math.random() - 0.5) * 0.3,
      vy: (Math.random() - 0.5) * 0.3,
      r: Math.random() * 2 + 0.5,
      a: Math.random() * 0.5 + 0.1
    }));

    const draw = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      for (const p of particlesRef.current) {
        p.x += p.vx;
        p.y += p.vy;
        if (p.x < 0) p.x = canvas.width;
        if (p.x > canvas.width) p.x = 0;
        if (p.y < 0) p.y = canvas.height;
        if (p.y > canvas.height) p.y = 0;
        ctx.beginPath();
        ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
        ctx.fillStyle = color.replace(")", `,${p.a})`).replace("rgb", "rgba");
        ctx.fill();
      }
      animRef.current = requestAnimationFrame(draw);
    };
    draw();
    return () => cancelAnimationFrame(animRef.current);
  }, [color]);

  return <canvas ref={canvasRef} style={{ position: "absolute", inset: 0, width: "100%", height: "100%", pointerEvents: "none" }} />;
}

export default function App() {
  const [screen, setScreen] = useState("title");
  const [chakraIndex, setChakraIndex] = useState(0);
  const [scenarioIndex, setScenarioIndex] = useState(0);
  const [score, setScore] = useState(0);
  const [feedback, setFeedback] = useState(null);
  const [selectedChoice, setSelectedChoice] = useState(null);
  const [unlockedChakras, setUnlockedChakras] = useState([]);
  const [fadeIn, setFadeIn] = useState(true);
  const [showChakraIntro, setShowChakraIntro] = useState(false);

  const currentChakra = CHAKRAS[chakraIndex];
  const currentScenario = currentChakra?.scenarios?.[scenarioIndex];

  const triggerFade = useCallback((cb) => {
    setFadeIn(false);
    setTimeout(() => { cb(); setFadeIn(true); }, 400);
  }, []);

  const handleChoice = (choice, idx) => {
    setSelectedChoice(idx);
    setFeedback(choice.feedback);
    const newScore = Math.max(0, score + choice.alignment);
    setScore(newScore);
  };

  const handleContinue = () => {
    if (scenarioIndex < currentChakra.scenarios.length - 1) {
      triggerFade(() => {
        setScenarioIndex(scenarioIndex + 1);
        setFeedback(null);
        setSelectedChoice(null);
      });
    } else {
      const newUnlocked = [...unlockedChakras, chakraIndex];
      setUnlockedChakras(newUnlocked);
      if (chakraIndex < CHAKRAS.length - 1) {
        triggerFade(() => {
          setChakraIndex(chakraIndex + 1);
          setScenarioIndex(0);
          setFeedback(null);
          setSelectedChoice(null);
          setShowChakraIntro(true);
        });
      } else {
        triggerFade(() => setScreen("results"));
      }
    }
  };

  const startGame = () => {
    triggerFade(() => {
      setScreen("game");
      setShowChakraIntro(true);
      setChakraIndex(0);
      setScenarioIndex(0);
      setScore(0);
      setFeedback(null);
      setSelectedChoice(null);
      setUnlockedChakras([]);
    });
  };

  const rank = getRank(score);

  const baseStyle = {
    minHeight: "100vh",
    background: currentChakra?.bgGrad || "#0d0d0d",
    color: "#e8e8e8",
    fontFamily: "'Courier New', Courier, monospace",
    transition: "background 0.8s ease",
    position: "relative",
    overflow: "hidden"
  };

  const fadeStyle = {
    opacity: fadeIn ? 1 : 0,
    transition: "opacity 0.4s ease",
  };

  if (screen === "title") {
    return (
      <div style={{ ...baseStyle, background: "linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #0a0a0a 100%)", display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", padding: "2rem", textAlign: "center" }}>
        <Particles color="rgb(106,76,147)" />
        <div style={{ ...fadeStyle, position: "relative", zIndex: 1 }}>
          <div style={{ fontSize: "3rem", letterSpacing: "0.3em", fontWeight: 700, marginBottom: "0.25rem", background: "linear-gradient(135deg, #E63946, #F77F00, #FCBF49, #2A9D8F, #457B9D, #6A4C93, #E8E8E8)", WebkitBackgroundClip: "text", WebkitTextFillColor: "transparent", lineHeight: 1.2 }}>
            CHAKRA
          </div>
          <div style={{ fontSize: "1.1rem", letterSpacing: "0.5em", color: "#888", marginBottom: "2rem", textTransform: "uppercase" }}>
            Ascension
          </div>
          <div style={{ width: 80, height: 1, background: "linear-gradient(90deg, transparent, #6A4C93, transparent)", margin: "0 auto 2rem" }} />
          <div style={{ fontSize: "0.7rem", letterSpacing: "0.15em", color: "#555", maxWidth: 380, margin: "0 auto 2.5rem", lineHeight: 1.8, textTransform: "uppercase" }}>
            Based on "Creating the Work You Love" by Rick Jarow Ph.D.
            <br /><br />
            Seven centers. Fourteen trials. One question:
            <br />
            <span style={{ color: "#999" }}>What is seeking to express itself through you?</span>
          </div>
          <div style={{ display: "flex", gap: "0.75rem", justifyContent: "center", marginBottom: "2.5rem" }}>
            {CHAKRAS.map((c, i) => (
              <div key={i} style={{ width: 10, height: 10, borderRadius: "50%", background: c.color, opacity: 0.7, boxShadow: `0 0 8px ${c.glow}` }} />
            ))}
          </div>
          <button
            onClick={startGame}
            style={{
              background: "transparent",
              border: "1px solid #6A4C93",
              color: "#ccc",
              padding: "0.75rem 2.5rem",
              fontSize: "0.8rem",
              letterSpacing: "0.3em",
              textTransform: "uppercase",
              cursor: "pointer",
              fontFamily: "inherit",
              transition: "all 0.3s ease",
              position: "relative"
            }}
            onMouseEnter={e => { e.target.style.background = "#6A4C93"; e.target.style.color = "#fff"; }}
            onMouseLeave={e => { e.target.style.background = "transparent"; e.target.style.color = "#ccc"; }}
          >
            Begin Ascension
          </button>
        </div>
      </div>
    );
  }

  if (screen === "results") {
    const maxScore = CHAKRAS.length * 2 * 2;
    const pct = Math.round((score / maxScore) * 100);
    return (
      <div style={{ ...baseStyle, background: "linear-gradient(135deg, #0a0a0a 0%, #1a1a2e 50%, #0a0a0a 100%)", display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", padding: "2rem", textAlign: "center" }}>
        <Particles color="rgb(232,232,232)" />
        <div style={{ ...fadeStyle, position: "relative", zIndex: 1 }}>
          <div style={{ fontSize: "0.65rem", letterSpacing: "0.4em", color: "#666", textTransform: "uppercase", marginBottom: "1.5rem" }}>Ascension Complete</div>
          <div style={{ display: "flex", gap: "0.75rem", justifyContent: "center", marginBottom: "2rem" }}>
            {CHAKRAS.map((c, i) => (
              <div key={i} style={{ width: 14, height: 14, borderRadius: "50%", background: unlockedChakras.includes(i) ? c.color : "#333", boxShadow: unlockedChakras.includes(i) ? `0 0 12px ${c.glow}` : "none", transition: "all 0.5s ease" }} />
            ))}
          </div>
          <div style={{ fontSize: "2.2rem", fontWeight: 700, color: "#e8e8e8", marginBottom: "0.25rem" }}>{rank.title}</div>
          <div style={{ fontSize: "0.75rem", color: "#888", marginBottom: "2rem", fontStyle: "italic" }}>{rank.desc}</div>
          <div style={{ width: 200, height: 4, background: "#222", borderRadius: 2, margin: "0 auto 0.5rem", overflow: "hidden" }}>
            <div style={{ width: `${pct}%`, height: "100%", background: "linear-gradient(90deg, #E63946, #F77F00, #FCBF49, #2A9D8F, #457B9D, #6A4C93, #E8E8E8)", borderRadius: 2, transition: "width 1s ease" }} />
          </div>
          <div style={{ fontSize: "0.65rem", color: "#666", letterSpacing: "0.2em", marginBottom: "2.5rem" }}>ALIGNMENT: {score} / {maxScore}</div>
          <div style={{ maxWidth: 400, margin: "0 auto 2.5rem", fontSize: "0.7rem", color: "#777", lineHeight: 1.8 }}>
            {pct >= 80
              ? "You moved through the seven centers with deep alignment. Your work is not a career — it is a practice, an offering, a way of being. The Anti-Career path is yours."
              : pct >= 50
              ? "You navigated with awareness but stumbled at key thresholds. Some chakras remain partially blocked. Revisit the centers where fear spoke louder than truth."
              : "The old paradigm still has its hooks in you. Survival fear, suppressed desire, and surrendered power shaped too many of your choices. The ascension awaits your return."
            }
          </div>
          <button
            onClick={() => triggerFade(() => { setScreen("title"); })}
            style={{
              background: "transparent",
              border: "1px solid #555",
              color: "#999",
              padding: "0.6rem 2rem",
              fontSize: "0.7rem",
              letterSpacing: "0.3em",
              textTransform: "uppercase",
              cursor: "pointer",
              fontFamily: "inherit",
              transition: "all 0.3s ease"
            }}
            onMouseEnter={e => { e.target.style.borderColor = "#999"; e.target.style.color = "#e8e8e8"; }}
            onMouseLeave={e => { e.target.style.borderColor = "#555"; e.target.style.color = "#999"; }}
          >
            Ascend Again
          </button>
        </div>
      </div>
    );
  }

  // GAME SCREEN
  if (showChakraIntro) {
    return (
      <div style={{ ...baseStyle, display: "flex", flexDirection: "column", alignItems: "center", justifyContent: "center", padding: "2rem", textAlign: "center" }}>
        <Particles color={currentChakra.color.replace("#", "rgb(").length ? `rgb(${parseInt(currentChakra.color.slice(1,3),16)},${parseInt(currentChakra.color.slice(3,5),16)},${parseInt(currentChakra.color.slice(5,7),16)})` : "rgb(200,200,200)"} />
        <div style={{ ...fadeStyle, position: "relative", zIndex: 1 }}>
          <div style={{ fontSize: "0.6rem", letterSpacing: "0.4em", color: "#666", textTransform: "uppercase", marginBottom: "1.5rem" }}>
            Center {chakraIndex + 1} of 7
          </div>
          <div style={{ fontSize: "3.5rem", marginBottom: "0.5rem", color: currentChakra.color, textShadow: `0 0 30px ${currentChakra.glow}`, lineHeight: 1 }}>
            {currentChakra.symbol}
          </div>
          <div style={{ fontSize: "1.6rem", fontWeight: 700, letterSpacing: "0.2em", color: currentChakra.color, marginBottom: "0.25rem" }}>
            {currentChakra.name}
          </div>
          <div style={{ fontSize: "0.7rem", letterSpacing: "0.2em", color: "#888", marginBottom: "2rem", textTransform: "uppercase" }}>
            {currentChakra.subtitle}
          </div>
          <div style={{ width: 60, height: 1, background: `linear-gradient(90deg, transparent, ${currentChakra.color}, transparent)`, margin: "0 auto 1.5rem" }} />
          <div style={{ maxWidth: 380, fontSize: "0.75rem", color: "#aaa", lineHeight: 1.8, marginBottom: "2.5rem" }}>
            {currentChakra.description}
          </div>
          <button
            onClick={() => triggerFade(() => setShowChakraIntro(false))}
            style={{
              background: "transparent",
              border: `1px solid ${currentChakra.color}`,
              color: currentChakra.color,
              padding: "0.6rem 2rem",
              fontSize: "0.7rem",
              letterSpacing: "0.3em",
              textTransform: "uppercase",
              cursor: "pointer",
              fontFamily: "inherit",
              transition: "all 0.3s ease"
            }}
            onMouseEnter={e => { e.target.style.background = currentChakra.color; e.target.style.color = "#0d0d0d"; }}
            onMouseLeave={e => { e.target.style.background = "transparent"; e.target.style.color = currentChakra.color; }}
          >
            Enter
          </button>
        </div>
      </div>
    );
  }

  return (
    <div style={{ ...baseStyle, display: "flex", flexDirection: "column", padding: "1.5rem", minHeight: "100vh" }}>
      <Particles color={`rgb(${parseInt(currentChakra.color.slice(1,3),16)},${parseInt(currentChakra.color.slice(3,5),16)},${parseInt(currentChakra.color.slice(5,7),16)})`} />
      
      {/* HUD */}
      <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: "1rem", position: "relative", zIndex: 1 }}>
        <div style={{ display: "flex", gap: "0.5rem", alignItems: "center" }}>
          {CHAKRAS.map((c, i) => (
            <div key={i} style={{
              width: i === chakraIndex ? 12 : 8,
              height: i === chakraIndex ? 12 : 8,
              borderRadius: "50%",
              background: unlockedChakras.includes(i) ? c.color : i === chakraIndex ? c.color : "#333",
              boxShadow: i === chakraIndex ? `0 0 10px ${c.glow}` : "none",
              transition: "all 0.3s ease",
              opacity: i === chakraIndex ? 1 : unlockedChakras.includes(i) ? 0.8 : 0.3
            }} />
          ))}
        </div>
        <div style={{ fontSize: "0.6rem", letterSpacing: "0.2em", color: "#666" }}>
          ALIGNMENT: {score}
        </div>
      </div>

      {/* Main content */}
      <div style={{ ...fadeStyle, flex: 1, display: "flex", flexDirection: "column", justifyContent: "center", maxWidth: 520, margin: "0 auto", width: "100%", position: "relative", zIndex: 1 }}>
        <div style={{ fontSize: "0.6rem", letterSpacing: "0.3em", color: currentChakra.color, textTransform: "uppercase", marginBottom: "0.5rem" }}>
          {currentChakra.name} — Trial {scenarioIndex + 1}/{currentChakra.scenarios.length}
        </div>
        
        <div style={{ fontSize: "0.85rem", color: "#ddd", lineHeight: 1.8, marginBottom: "1.5rem", borderLeft: `2px solid ${currentChakra.color}33`, paddingLeft: "1rem" }}>
          {currentScenario.prompt}
        </div>

        {!feedback ? (
          <div style={{ display: "flex", flexDirection: "column", gap: "0.6rem" }}>
            {currentScenario.choices.map((choice, i) => (
              <button
                key={i}
                onClick={() => handleChoice(choice, i)}
                style={{
                  background: "rgba(255,255,255,0.03)",
                  border: "1px solid rgba(255,255,255,0.1)",
                  color: "#bbb",
                  padding: "0.75rem 1rem",
                  fontSize: "0.72rem",
                  textAlign: "left",
                  cursor: "pointer",
                  fontFamily: "inherit",
                  lineHeight: 1.6,
                  transition: "all 0.2s ease",
                  borderRadius: 0
                }}
                onMouseEnter={e => { e.target.style.borderColor = currentChakra.color; e.target.style.color = "#e8e8e8"; e.target.style.background = `${currentChakra.color}11`; }}
                onMouseLeave={e => { e.target.style.borderColor = "rgba(255,255,255,0.1)"; e.target.style.color = "#bbb"; e.target.style.background = "rgba(255,255,255,0.03)"; }}
              >
                <span style={{ color: currentChakra.color, marginRight: "0.5rem", fontSize: "0.6rem" }}>{String.fromCharCode(65 + i)}.</span>
                {choice.text}
              </button>
            ))}
          </div>
        ) : (
          <div>
            <div style={{
              background: `${currentChakra.color}11`,
              border: `1px solid ${currentChakra.color}44`,
              padding: "1rem",
              marginBottom: "1.5rem"
            }}>
              <div style={{ fontSize: "0.6rem", letterSpacing: "0.2em", color: currentChakra.color, textTransform: "uppercase", marginBottom: "0.5rem" }}>
                {currentScenario.choices[selectedChoice].alignment >= 2 ? "⬆ Deep Alignment" : currentScenario.choices[selectedChoice].alignment >= 1 ? "↗ Partial Alignment" : currentScenario.choices[selectedChoice].alignment === 0 ? "→ Neutral" : "⬇ Misalignment"}
              </div>
              <div style={{ fontSize: "0.75rem", color: "#ccc", lineHeight: 1.7 }}>
                {feedback}
              </div>
            </div>
            <button
              onClick={handleContinue}
              style={{
                background: "transparent",
                border: `1px solid ${currentChakra.color}`,
                color: currentChakra.color,
                padding: "0.6rem 2rem",
                fontSize: "0.7rem",
                letterSpacing: "0.25em",
                textTransform: "uppercase",
                cursor: "pointer",
                fontFamily: "inherit",
                transition: "all 0.3s ease",
                display: "block",
                marginLeft: "auto"
              }}
              onMouseEnter={e => { e.target.style.background = currentChakra.color; e.target.style.color = "#0d0d0d"; }}
              onMouseLeave={e => { e.target.style.background = "transparent"; e.target.style.color = currentChakra.color; }}
            >
              {scenarioIndex < currentChakra.scenarios.length - 1 ? "Next Trial" : chakraIndex < CHAKRAS.length - 1 ? "Ascend" : "Complete"}
            </button>
          </div>
        )}
      </div>
    </div>
  );
}
