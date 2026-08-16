---
original_path: "/home/claude/victoria_midnight_slice.md"
source_conversation: "Grab data analysis and findings"
created: 2026-02-17
trunk: BLACK
kind: generated-file
---

# VERTICAL SLICE — VICTORIA "TORI" MIDNIGHT
## Character Database Record v0.1
### IP: OVEREXITOUT (The Outliers) | Status: LOCKED SOURCE MATERIAL
---

## WHAT THIS DOCUMENT IS

This is the first vertical slice of the 12-Layer Character Database System. It demonstrates the full pipeline: raw source material → numeric layer values → derived stats → auto-fired flags → structured data block. Victoria Midnight was selected because her canonical documentation is the most complete and adversarial — she will stress-test the system hard.

This document answers: **does the layer system produce values that feel true to the character?**

If a value reads wrong, the layer definition needs adjustment — not the character. The character is locked. The system has to earn its numbers.

---

## TIER 1 — CORE LAYERS (Flat Character / 3 values)

### L1: CORE
**Domain:** Cognitive and psychological mass. What the mind can hold, process, and sustain. Governs every mental skill, problem-solving behavior, and ideological framework. Default human average = 10.

**Value: 13**

Tori is a meritocrat — she builds a sophisticated causal model of how the world works (merit → freedom), operates it consistently, and updates it under extreme pressure when the evidence becomes undeniable. That's high cognitive function. Her MC Problem is *Equity* — a philosophical framework error, not an intellectual one. She's not dumb. She's precisely wrong about a specific thing. Score above average but not maximum because her cognitive model has a structural flaw baked in.

**Point Cost:** 60 points (IQ equivalent at 20pts/level above 10)

---

### L2: VITAL
**Domain:** Physical and energetic presence. Raw physical capability, precision, endurance, body-as-instrument relationship. Default = 10.

**Value: 14**

She's a racing driver. Reaction time, spatial processing, physical courage, and mechanical intuition are her primary tools pre-crash. The hardware that activates post-crash is housed in a body already calibrated for performance. The FLCL manifestations (mechanical outbursts, digital puberty surges) require a VITAL score high enough to carry them without collapse. Motion under pressure, never ornamental — that's a 14.

**Point Cost:** 80 points (DX equivalent at 20pts/level above 10)

---

### L3: SOCIAL
**Domain:** Relational interface. How the character projects into the world and receives others. Governs reaction modifiers, social legibility, and relationship math. Default = 10.

**Value: 10**

Counterintuitive given how central her social situation is — but her SOCIAL score being exactly average is the point. Her Critical Flaw is Truth: when she speaks truth, it desyncs her hardware and triggers Noise. Her social interface isn't weak, it's *accurate to a world that can't process accuracy*. She doesn't lack social intelligence — she lacks the ability to perform social dishonesty. Average SOCIAL score with a specific catastrophic vulnerability is more precise than a high or low score.

**Point Cost:** 0 points (no modification from baseline)

**TIER 1 TOTAL: 140 points**

---

## TIER 2 — SECONDARY LAYERS (Standard Character / adds 3 values)

### L4: WILL
**Domain:** Psychological resistance to pressure, manipulation, coercion, and breakdown. Derived from CORE by default (WILL = CORE). Can be bought up or down independently. Represents the load-bearing capacity of the self under systemic assault.

**Default from CORE:** 13
**Bought Up:** +1 (5 points)
**Final Value: 14**

Her Resolve is *Change* — meaning she does eventually bend — but the whole story is about how much pressure it takes to make that happen. She survives the crash, the brother's death, the academy, the Ban, the erasure. That's a character with WILL above her cognitive baseline. She's slightly more stubborn than she is smart. The +1 above CORE captures this.

**Point Cost:** 5 points

---

### L5: WOUND
**Domain:** Accumulated psychological damage. Starts at 0 (undamaged) and fills during character history. High WOUND reduces effective WILL and SOCIAL under specific stress triggers. Not the same as backstory — this is the damage that *didn't heal* and is actively operating on behavior.

**Value: 8 / 10**

The wound is the pace-notes. She ignored her brother's guidance during the rally and the car exploded. He died. She didn't. The wound isn't just grief — it's the knowledge that she *chose* not to listen, and that choice killed him. That's catastrophic wound density. Score 8 because the story requires her to still function (she's the protagonist) — a 9 or 10 would produce total behavioral collapse, which is reserved for characters who aren't carrying the plot.

**Active wound triggers:** Any scene involving: (1) mechanical failure, (2) being given guidance she's inclined to ignore, (3) her brother's name, (4) moments where she could prevent harm by listening and chooses not to.

**Point Cost:** Not a bought stat — assigned during character history entry.

---

### L6: DRIVE
**Domain:** Narrative motivation fuel. Equivalent to Fatigue Points. Represents how much the character can invest in pursuit of their desire before depletion. Derives from VITAL by default (DRIVE = VITAL). Spent on active goal-pursuit scenes; recovered through resolution or rest.

**Default from VITAL:** 14
**Bought Down:** -2 (returns 6 points)
**Final Value: 12**

She's not driven by ambition — she's driven by meaning. The distinction matters mechanically. Ambition-driven characters can sustain indefinitely because each success refuels them. Meaning-driven characters burn out when the meaning is threatened and need narrative resolution to recover. Her DRIVE is slightly below her physical ceiling because her fuel source (the brother, the truth, fairness) is already damaged at story start. The crash didn't kill her DRIVE, but it dented the tank.

**Point Cost:** -6 points (returns to pool)

**TIER 2 TOTAL: 139 points (net of DRIVE reduction)**

---

## TIER 3 — DEEP LAYERS (Full Character / adds 6 variable stacks)

### L7: ORIGIN
**Domain:** Birth context, class position, family architecture, socioeconomic stability, and environmental formation. Feeds WOUND base values and SOCIAL defaults.

| Variable | Value | Notes |
|---|---|---|
| `origin_class` | Working-class / criminal adjacent | Salvage economy, syndicate-connected family |
| `origin_stability` | 4 / 10 | Unstable external world, tight internal unit |
| `family_coherence` | 7 / 10 | High coherence within family (her + brother), low coherence with any institution |
| `origin_wound_seed` | 6 / 10 | Pre-crash instability seeds susceptibility to the wound |
| `tech_level` | Near-future 6 | Southern Gothic + emerging surveillance/feed infrastructure |
| `system_exposure` | Early (M1A) | System noticed her before she knew it existed |

**Origin Narrative:** She didn't grow up inside the system — she was *acquired* by it. The salvage economy phase (M1A) means her origin is outside institutional legibility. She's self-made by necessity, not ideology. The Delta Coast racing scene is the first context where her output becomes visible at scale. The system's attention was acquisition, not admiration — and she didn't know the difference until it was too late.

---

### L8: IMPRINT
**Domain:** Formative emotional conditioning. How early experiences structured the character's emotional response patterns, attachment architecture, and default relationship behaviors.

| Variable | Value | Notes |
|---|---|---|
| `attachment_style` | Secure-Anxious / 6 | Secure WITH brother; destabilized by his loss into anxious orientation |
| `emotional_range` | 9 / 10 | Deep feeling; hardware physically responds to grief — maximum signal |
| `conditional_patterns` | `["merit_earns_freedom", "loyalty_to_kinship", "distrust_of_institution"]` | Three active operational beliefs |
| `imprint_flexibility` | 3 / 10 | Low — these patterns are load-bearing; she updates them only under catastrophic evidence |

**Imprint Narrative:** Her primary attachment object was her brother. He was the "Brains" to her "Body" — navigator to her driver. The pace-notes weren't just technical data; they were a communication system between two people who trusted each other completely. When she ignored them, she didn't just make a driving error — she violated the founding logic of her attachment system. The WOUND at L5 is the wound. The IMPRINT at L8 is why it cuts so deep.

---

### L9: EROS
**Domain:** Psycho-sexual conditioning. Desire structure, erotic patterning, shame architecture, and the mechanics of how the character wants and is wanted.

| Variable | Value | Notes |
|---|---|---|
| `erotic_blueprint_type` | Kinesthetic | Physical, motion-based, earned through performance — never ornamental |
| `desire_vector` | 3 / 10 | Low relational desire, high sovereignty desire — she wants freedom, not connection |
| `shame_index` | 2 / 10 | Very low — she is not ashamed of who she is; her flaw is Truth, not self-concealment |
| `intimacy_mode` | Parallel presence | Intimacy through shared activity (co-piloting), not disclosure |

**Eros Narrative:** Her aesthetic self-definition — "beauty that is earned, not curated; motion under pressure, never ornamental" — is also her desire template. She is attracted to and attractive through *performance under pressure*, not surface presentation. Low shame index is not naivety; it's the specific kind of self-possession that makes her Truth flaw so dangerous — she doesn't know how to hide herself because she doesn't think she needs to.

---

### L10: SHADOW
**Domain:** Jungian dark material. The repressed, projected, and denied content. High SHADOW scores generate disadvantage clusters and modify how the character behaves under stress.

| Variable | Value | Notes |
|---|---|---|
| `shadow_density` | 7 / 10 | The ignored pace-notes — she chose not to listen; she owns this but cannot process it |
| `projection_tendency` | 6 / 10 | Externalizes fault onto the system; "the institution is unfair" shields her from "I killed him" |
| `regression_pattern` | `control_escalation` | Under stress, doubles down on control behaviors rather than allowing input |
| `shadow_content` | `["culpability_for_brother", "distrust_of_own_judgment", "fear_of_being_right_and_wrong_simultaneously"]` | Core shadow material |

**Shadow Narrative:** The shadow isn't the grief — it's the *choice*. She made a decision in the car that day. She heard the pace-notes and decided she knew better. That decision lives in her shadow because processing it fully would mean accepting that she is capable of catastrophic error even when she's certain she's right. Her MC Problem (Equity) is the conscious version of this — she keeps demanding a fair system because the alternative is acknowledging that fairness doesn't protect you from yourself.

---

### L11: DESTINY
**Domain:** Directional growth vector. North Node logic — what the character is *trying to become*, what resists that becoming, and the archetypal journey shape.

| Variable | Value | Notes |
|---|---|---|
| `growth_axis` | Inequity | MC Solution element — she must embrace being "Rigged" rather than demanding fairness |
| `resistance_index` | 8 / 10 | High — she fights her solution almost to the end; Change resolve requires maximum pressure |
| `soul_evolution_archetype` | Tactical Disruptor | Not a hero; not a villain; a threat that refuses to vanish |
| `karmic_memory` | `meritocratic_certainty` | What she carries from before and must release |
| `growth_requirement` | `accept_asymmetry` | She must accept that the game is rigged and play it rigged, not demand it be made fair |

**Destiny Narrative:** Her Destiny vector points toward a specific kind of disillusionment that becomes power — not cynicism, but precision. The arc is: "Merit earns freedom" → "Visibility invites ownership" → "Control is the only form of safety left" → [final step not yet achieved at story start] "Rigged is not the same as wrong." The resistance_index of 8 is why the story takes this long to get there. She is constitutionally opposed to her own solution.

---

### L12: FUNCTION
**Domain:** Dramatica narrative role, objective story function, throughline assignment, and the character's mechanical purpose in the story engine.

| Variable | Value | Notes |
|---|---|---|
| `dramatica_archetype` | Protagonist | Drives the story toward a "Fair" truth |
| `motivation_element` | Equity | Core problem element |
| `methodology_element` | Proaction | She makes things happen; she drives toward goals |
| `evaluation_element` | Result | Judges by outcomes, not process |
| `purpose_element` | Actuality | Oriented toward what is real rather than what appears |
| `narrative_invariant` | Cost and Meaning | She pays for every advance; meaning is what survives when cost exceeds return |
| `story_outcome` | Failure | Erasure is complete |
| `story_judgement` | Good | Finds Meaning in the wreckage |
| `limit_type` | Optionlock | Exits close one by one, not a time limit |
| `resolve` | Change | She bends — eventually |

---

## DERIVED STATISTICS

These are computed from primary layer values. They are not entered — they are calculated.

| Stat | Formula | Value |
|---|---|---|
| Basic Damage Resistance | `WILL - (WOUND / 2)` | 14 - 4 = **10** |
| Social Legibility | `SOCIAL - (SHADOW.projection_tendency / 3)` | 10 - 2 = **8** |
| Narrative Momentum | `DRIVE + (DESTINY.resistance_index / 2)` | 12 + 4 = **16** |
| Stress Threshold | `WILL - WOUND` | 14 - 8 = **6** |
| Collapse Risk | `(WOUND + SHADOW.shadow_density) / 2` | (8 + 7) / 2 = **7.5 → 8** |
| Truth Exposure Index | `SOCIAL + (10 - SHADOW.shame_index)` | 10 + 8 = **18** (dangerously high legibility) |

**Reading the derived stats:** Her Stress Threshold (6) means she can absorb 6 units of pressure before behavioral disruption. Her Collapse Risk (8) is high but doesn't immediately trigger — it just means the window between "functional" and "broken" is narrow. Her Truth Exposure Index (18) is the key derived stat: it quantifies exactly why the Ban happens. She is maximally legible to the system because she has low shame and average social masking. She cannot hide herself.

---

## ACTIVE FLAGS

Flags are boolean conditions that fire when numeric thresholds are met. They represent derived character states — not assigned, computed.

---

### 🔴 FLAG: SHADOW_DENIAL
**Trigger:** `WOUND > 6 AND SHADOW.projection_tendency >= 5 AND IMPRINT.conditional_patterns contains "merit_earns_freedom"`
**Status: ACTIVE**

She denies her causal role in the crash by routing blame toward the system. "The institution is unfair" is true — and it is also functioning as a shield against "I chose not to listen and he died." Both can be true. She only holds one at a time. This flag drives the entire arc. Her journey is the slow, catastrophic collapse of this denial.

---

### 🔴 FLAG: TRUTH_VULNERABILITY
**Trigger:** `SOCIAL < 12 AND FUNCTION.motivation_element = "Equity" AND SHADOW.shadow_density > 6`
**Status: ACTIVE**

When she speaks truth, her wound surfaces through her social interface. She doesn't code-switch, she doesn't manage her signal, she doesn't perform legibility. The Ban is the system's response to this flag firing in a public context. Truth is not her virtue — it is her exploit vector.

---

### 🔴 FLAG: OPTIONLOCK_PROGRESSION
**Trigger:** `WOUND > 7 AND DESTINY.resistance_index > 7 AND FUNCTION.limit_type = "Optionlock"`
**Status: ACTIVE**

The story closes options on her because her wound + resistance combination systematically eliminates paths. She can't take the easy exit (truth won't lift the Ban), she can't take the institutional exit (she's been erased from the Feed), she can't take the relational exit (brother is dead). The exits close because of who she is, not because of a countdown clock. Optionlock confirmed by this flag.

---

### 🟡 FLAG: EARNED_JUDGEMENT
**Trigger:** `FUNCTION.dramatica_archetype = "Protagonist" AND FUNCTION.story_outcome = "Failure" AND WILL > 10`
**Status: PENDING (fires at story climax)**

Good judgement despite failure outcome. Her WILL score (14) is high enough that total systemic defeat cannot fully erase her personhood. She finds Meaning in the wreckage because she has enough internal structure remaining to assign meaning to anything — even her own destruction. This flag doesn't fire until the climax when all options are closed and the Judgement determination is made.

---

### ⬜ FLAG: KINSHIP_COLLAPSE
**Trigger:** `IMPRINT.attachment_style_score > 5 AND primary_attachment_object = "deceased" AND WOUND > 7`
**Status: ALREADY FIRED (pre-story)**

This flag fired at the crash. It is the origin condition for everything else. Including it here to document that the character entered the story in a post-collapse attachment state — there is no primary attachment object currently active. All relational behavior post-crash is operating without a secure base.

---

## STRUCTURED DATA BLOCK

*This is the machine-readable output. When the database is stood up, this block is what gets ingested. Everything above is the human-readable documentation of how these numbers were derived.*

```
CHARACTER_ID: victoria_midnight
IP: overexitout
STATUS: locked
VERSION: 0.1

--- TIER 1 ---
CORE: 13
VITAL: 14
SOCIAL: 10

--- TIER 2 ---
WILL: 14
WOUND: 8
DRIVE: 12

--- TIER 3: ORIGIN ---
origin_class: working_criminal_adjacent
origin_stability: 4
family_coherence: 7
origin_wound_seed: 6
tech_level: 6
system_exposure: early_pre_awareness

--- TIER 3: IMPRINT ---
attachment_style: secure_anxious
attachment_style_score: 6
emotional_range: 9
conditional_patterns: [merit_earns_freedom, loyalty_to_kinship, distrust_of_institution]
imprint_flexibility: 3
primary_attachment_object: brother_deceased

--- TIER 3: EROS ---
erotic_blueprint_type: kinesthetic
desire_vector: 3
shame_index: 2
intimacy_mode: parallel_presence

--- TIER 3: SHADOW ---
shadow_density: 7
projection_tendency: 6
regression_pattern: control_escalation
shadow_content: [culpability_for_brother, distrust_of_own_judgment, fear_of_being_right_and_wrong]

--- TIER 3: DESTINY ---
growth_axis: inequity
resistance_index: 8
soul_evolution_archetype: tactical_disruptor
karmic_memory: meritocratic_certainty
growth_requirement: accept_asymmetry

--- TIER 3: FUNCTION ---
dramatica_archetype: Protagonist
motivation_element: Equity
methodology_element: Proaction
evaluation_element: Result
purpose_element: Actuality
narrative_invariant: cost_and_meaning
story_outcome: Failure
story_judgement: Good
limit_type: Optionlock
resolve: Change

--- DERIVED ---
basic_damage_resistance: 10
social_legibility: 8
narrative_momentum: 16
stress_threshold: 6
collapse_risk: 8
truth_exposure_index: 18

--- FLAGS ---
SHADOW_DENIAL: ACTIVE
TRUTH_VULNERABILITY: ACTIVE
OPTIONLOCK_PROGRESSION: ACTIVE
EARNED_JUDGEMENT: PENDING
KINSHIP_COLLAPSE: FIRED_PRE_STORY
```

---

## SYSTEM NOTES

**What this slice confirmed:**

The three-tier modular structure holds. Tier 1 alone (CORE 13, VITAL 14, SOCIAL 10) produces a recognizable outline of Tori — fast, smart, but not socially armored. Tier 2 adds the crash and its consequences (WILL 14, WOUND 8, DRIVE 12) and suddenly she has a story shape. Tier 3 gives the specific texture that separates her from any other protagonist with similar Tier 1-2 values.

**What the numbers revealed that prose didn't:**

The Truth Exposure Index (18) is the single most important derived stat in her sheet. It quantifies why the system responds to her the way it does. She isn't persecuted because she's dangerous — she's persecuted because she's *maximally legible* while refusing to manage that legibility. The system can't handle a signal it can't categorize.

Her EROS.shame_index (2) and SHADOW.shadow_density (7) in combination produce a character who is simultaneously very exposed and very defended — just defended about the wrong things. She'll show you everything about herself except the one thing that would actually help.

**What the slice revealed that needs more data:**

L9 EROS is the thinnest layer. The source material doesn't have explicit psycho-sexual conditioning documentation for Victoria the way it does for Myrtle and Vivian. The kinesthetic / parallel-presence / low-shame readings are inferred from aesthetic documentation ("earned, not curated; motion under pressure, never ornamental"). This layer needs a dedicated extraction query before it's fully reliable.

**Next recommended query:**
`Victoria Midnight sexuality intimacy desire relationships OVEREXITOUT`

---

*Document prepared as part of the 12-Layer Character Database System development.*  
*Source: OVEREXITOUT canonical documentation (LOCKED).*
