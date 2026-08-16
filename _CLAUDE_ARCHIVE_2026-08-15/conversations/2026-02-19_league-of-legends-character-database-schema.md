---
title: "League of legends character database schema"
uuid: b1c40537-7e43-4843-9432-7183b4bb85b6
created: 2026-02-19
updated: 2026-02-19
trunk: ORANGE
messages: 4
chars: 25684
artifacts: 0
generated_files: 0
tools: []
source: claude.ai-export-2026-08-15
---

# League of legends character database schema

> **Conversation Overview**

The user is creating a comprehensive database system for League of Legends characters and requested Claude's help in designing a detailed character taxonomy schema. They wanted to move beyond basic character attributes to create a deeply searchable, multi-dimensional tagging system inspired by the granular categorization methods used on adult content platforms. The user specifically requested an outline before implementation, emphasizing they wanted to understand the full structure before populating any actual character data.

Claude developed a 14-domain database schema covering physical appearance through a "glamour fantasy" lens, subtextual physical attributes that suggest capabilities, personality archetypes, kinetic behavior from both animation and biomechanical perspectives, and fashion elements. The user then requested additional major domains focusing on psychological aspects including coping mechanisms, decompensation profiles, mental health predispositions, intimate relationship dynamics, personality disposition indicators, fetish alignment profiles, combat archetypes, social group positioning, and a meta-layer called "Design Focus Power Board" that shows percentage distribution of design energy across all domains.

The final schema spans 14 major domains with 6-8 subcategories each, creating what the user described as a "deeply cross-referenceable character taxonomy" that would allow complex queries across psychological, kinetic, social, martial, and aesthetic dimensions simultaneously. The user emphasized wanting this as a searchable system where one could filter characters by multiple attributes across different domains. Claude provided detailed breakdowns of each domain with specific subcategories and example applications, concluding with offers to begin building the actual database file and populating it with League of Legends champion data.

---
## 🧑 Papi  <sub>2026-02-19 05:31:09</sub>

I'm creating a database system for a project. Can you take all characters from league of legends and create attributes for said character? Primarily focus on their real world physical appearance (from a glamour fantasy sort of lens, or like I'm thinking of tags off of a porn site like pornhub or hamster) next would be the their subtextual attributes like what their physicality suggests about their capabilities. Same for personality. Next would be regarding their kinetic behavior. How they move this is from the perspective from first of an animation perspective and grounded anatomical scientific perspective. Finally I want there to be a section on fashion, clothing, and accessories. Can you outline this for me first before we do anything else. Then summarize the whole situation

---

## 🤖 Claude  <sub>2026-02-19 05:32:08</sub>

The user wants to create a database system for League of Legends characters with specific attribute categories. They want me to outline the schema first before populating it. Let me think about this carefully.

They're asking for character attributes organized into categories:

1. Physical appearance - described through a "glamour fantasy" lens with tagging similar to adult site tags
2. Subtextual attributes - what their physicality suggests about capabilities
3. Personality attributes
4. Kinetic behavior - how they move (animation perspective + anatomical/scientific perspective)
5. Fashion, clothing, and accessories

This is essentially a character database schema. The mention of porn site tags is about the tagging taxonomy style - descriptive, granular physical attribute tags. 

Now I'll map out the database structure with these five main attribute categories and define what fields belong under each one.Alright, let me outline the database schema structure first. This is essentially a character taxonomy system using granular, descriptive tagging — think the flat-tag + nested-category approach adult sites use for discoverability, but applied to a fantasy character database.

---

## Schema Outline: League of Legends Character Database

### 1. **Physical Appearance (Glamour/Fantasy Tagging)**

The idea here is flat, searchable descriptors — the way content platforms tag for body type, features, and aesthetic appeal.

**Subcategories:**

- **Body Type** — build silhouette (e.g., slim, athletic, muscular, thicc, petite, hulking, lithe, voluptuous, lanky, massive)
- **Body Proportions** — exaggerated or grounded ratios (e.g., long-legged, broad-shouldered, top-heavy, balanced, narrow-waisted, barrel-chested)
- **Height Class** — tiny, short, average, tall, towering, colossal (this matters since LoL has yordles through Aurelion Sol)
- **Skin/Surface** — skin tone, texture, material (human flesh, fur, scales, stone, ethereal/translucent, metallic, scarred, tattooed, glowing)
- **Hair** — length, color, style, texture (or bald, helmeted, hood-covered, flame, tendrils, etc.)
- **Face** — facial structure, expression archetype, eye type, distinguishing marks (sharp features, soft features, angular jaw, hidden face, mask, inhuman)
- **Species/Race Presentation** — human-passing, humanoid, bestial, monstrous, spectral, mechanical, chimeric
- **Sex Appeal Archetype** (the "glamour lens") — this is the tag layer that maps to fantasy desirability tropes: femme fatale, girl-next-door, amazonian, twunk, daddy, pretty boy, rugged, androgynous, monsterfucker-bait, inhuman/alien beauty, armored mystery, etc.

---

### 2. **Subtextual Physical Attributes (What the Body Implies)**

This layer reads the character design as visual storytelling — what does their physicality *communicate* about who they are?

**Subcategories:**

- **Implied Strength Class** — what their build suggests about raw power (e.g., explosive power, endurance fighter, deceptive strength, fragile, immovable)
- **Implied Speed/Agility** — visual cues for how fast or nimble they'd be (lean muscle, compact frame, heavy/grounded)
- **Implied Durability** — scarring, armor integration, thick limbs, supernatural resilience cues
- **Implied Dexterity/Precision** — long fingers, steady posture, surgeon-like composure vs. brute force indicators
- **Threat Posture** — does the design read as predator, ambush hunter, defensive wall, untouchable, or deceptive non-threat?
- **Sensory Implication** — visible cues for heightened senses (large ears, multiple eyes, blindfold suggesting other perception, antennae)
- **Supernatural Physicality Cues** — glowing elements, floating parts, asymmetry suggesting corruption/transformation, elemental integration into the body

---

### 3. **Personality Attributes**

Tagging personality the same way — flat descriptors plus archetype clustering.

**Subcategories:**

- **Core Archetype** — the dominant personality read (e.g., trickster, stoic warrior, mad scientist, noble protector, feral predator, brooding loner, charismatic leader, unhinged chaotic)
- **Emotional Signature** — their default emotional register (cold, warm, manic, serene, angry, playful, melancholic, hungry)
- **Social Orientation** — loner, pack leader, loyal follower, manipulator, reluctant ally, antisocial, gregarious
- **Moral Alignment Tag** — classic axis but with nuance (righteous, pragmatic, selfish, sadistic, protective, nihilistic, duty-bound, chaotic-fun)
- **Intelligence Presentation** — cunning, scholarly, instinctual, street-smart, naive, calculating, wise, unreadable
- **Confidence Level** — arrogant, quietly confident, insecure-masked-as-bravado, humble, oblivious, god-complex
- **Relationship to Power** — seeks it, wields it casually, fears it, serves it, transcends it, corrupted by it
- **Voice/Communication Style** — poetic, blunt, silent, taunting, formal, folksy, cryptic, screaming

---

### 4. **Kinetic Behavior (Movement Profile)**

Two parallel lenses on the same thing: how an animator would describe them, and how a biomechanist would.

**A. Animation Perspective:**

- **Movement Quality** — floaty, snappy, heavy, fluid, jerky, elastic, mechanical, ethereal
- **Idle Behavior** — what they do standing still (fidgets, weapon maintenance, breathing pattern, supernatural hovering, menacing stillness)
- **Locomotion Style** — walk/run characterization (prowl, march, glide, bound, lumber, skitter, teleport, slither)
- **Attack Kinematics** — the feel of their combat (precise strikes, wild swings, channeled energy, flowing combo chains, single devastating hits)
- **Signature Gesture** — the one motion that defines them (Yasuo's wind-sweep, Jinx's manic pointing, Darius's axe-plant)
- **Weight Class Feel** — how the animation sells mass and momentum (featherweight, middleweight, heavyweight, weightless)

**B. Anatomical/Biomechanical Perspective:**

- **Center of Gravity** — low/grounded, high/upright, shifting/dynamic, displaced (floating)
- **Primary Kinetic Chain** — where their power generates from (hip rotation, shoulder drive, full-body whip, wrist/finger precision, core torsion)
- **Dominant Movement Pattern** — push, pull, rotation, locomotion, ballistic, isometric hold
- **Flexibility Profile** — rigid/armored, normal human range, hypermobile, boneless/supernatural
- **Fatigue Implication** — does the design suggest sustained output, explosive burst, or tireless/inhuman endurance?
- **Injury Vulnerability Read** — what a body like theirs would be vulnerable to (joint stress, overextension, top-heavy tipping, exposed vitals)

---

### 5. **Fashion, Clothing & Accessories**

The costume design as its own data layer.

**Subcategories:**

- **Silhouette Category** — the overall shape their outfit creates (flowing, armored/bulky, skin-tight, layered, minimal/exposed, asymmetric)
- **Coverage Level** — full coverage, partial, strategic exposure, mostly exposed, fully armored
- **Material Read** — leather, plate, cloth/silk, fur/hide, magical energy, living material, tech-suit, tattered/worn
- **Color Palette** — dominant and accent colors, saturation level (muted, vibrant, monochrome, iridescent)
- **Cultural/Historical Reference** — what real-world fashion traditions the design draws from (samurai, Victorian, tribal, futuristic military, haute couture, streetwear, ancient Greek, etc.)
- **Accessories & Props** — weapons as fashion, jewelry, capes/cloaks, masks, crowns, belts, pouches, floating orbitals, companion creatures
- **Wear & Tear State** — pristine, battle-worn, decayed, cobbled-together, ceremonial, lived-in
- **Fashion Archetype** — what "vibe" the outfit communicates (dark knight, femme fatale gown, battle-ready punk, regal monarch, feral minimalist, tech-ninja, witch/warlock couture)

---

## Summary

You're building a **multi-dimensional character tagging database** for every League of Legends champion (~170 characters). The schema has **five major domains**, each with **6–8 subcategories**, creating a deeply searchable, cross-referenceable taxonomy. The design philosophy borrows the flat-tag discoverability model from adult content platforms and applies it to character design analysis across:

1. **Physical appearance** — granular body/face/aesthetic tags with a glamour-fantasy desirability lens
2. **Subtextual physicality** — what the body design *implies* about capability, threat, and power
3. **Personality** — archetype + emotional + social + moral tagging
4. **Kinetics** — dual-lens movement profiling from both animation craft and real biomechanics
5. **Fashion** — costume design as its own searchable layer covering silhouette, materials, cultural reference, and vibe

The end result is a system where you could query something like *"show me all champions tagged: athletic build + predator threat posture + trickster personality + fluid movement + skin-tight silhouette"* and get a meaningful filtered result set.

Want me to start building this out as an actual file — spreadsheet, database, or structured document — and begin populating champions?

---

## 🧑 Papi  <sub>2026-02-19 05:46:55</sub>

I want a few more major domains. One that focuses on psychology primarily focus on the behavior aspect rooted in coping. Another with whatever the opposite of coping is. Next would be associated predisposition of mental illness and associated variables. Next would be their sexuality profile. Their sort of degree of magnitude their physicality suggests their predisposition for oppenness and shit. And then after that is what fetishes their character is geared towards. Next would be their archetypal role in fights. After would be their social role in groups, what they would autmatically drift towards in positioning in social situations. And after that would be I guess a power board like what is the split of focus that the design exudes between the c categories

---

## 🤖 Claude  <sub>2026-02-19 05:48:29</sub>

The user wants me to add more major domains to the database schema. Let me outline these additional domains clearly.## Additional Major Domains (6–13)

---

### 6. **Psychology: Coping Mechanisms**

How the character manages stress, threat, loss, and emotional overload — read purely from design, lore tone, and behavioral presentation.

**Subcategories:**

- **Primary Coping Style** — the dominant strategy (intellectualization, humor/deflection, aggression channeling, withdrawal/isolation, hyper-competence, dissociation, ritualistic control, substance/sensation seeking, caretaking others to avoid self)
- **Secondary/Shadow Coping** — what they fall back on when the primary fails (e.g., Lux's brightness masking repression, Yasuo's wandering masking avoidance)
- **Attachment Strategy** — how they manage closeness under stress (avoidant, anxious-clinging, dismissive, secure-but-guarded, disorganized, parasitic)
- **Relationship to Pain** — do they suppress, externalize, aestheticize, weaponize, or surrender to it?
- **Self-Regulation Capacity** — high (disciplined containment), moderate (functional with cracks), low (volatile/reactive), absent (feral or consumed)
- **Defense Mechanisms** — projection, denial, splitting, sublimation, reaction formation, compartmentalization, grandiosity as defense
- **Adaptive vs. Maladaptive Rating** — is their coping actually working, barely holding, or actively self-destructive?

---

### 7. **Psychology: Decompensation Profile (Opposite of Coping)**

What it looks like when they *stop* coping — the unraveling, the break, the mask-off moment.

**Subcategories:**

- **Trigger Class** — what breaks them (betrayal, loss of control, isolation, helplessness, identity threat, moral injury, accumulated micro-erosion)
- **Decompensation Style** — how the breakdown manifests (explosive rage, catatonic shutdown, manic escalation, paranoid spiral, identity fragmentation, cold dissociation, regression to primal state)
- **Collapse Trajectory** — fast snap vs. slow erosion vs. oscillating destabilization
- **Behavioral Tells Pre-Break** — the warning signs the design/lore hints at (over-control tightening, humor becoming brittle, speech pattern changes, physical tension cues)
- **Rock Bottom Presentation** — what their worst version looks like (feral, hollow, tyrannical, suicidal-coded, predatory, comatose)
- **Recovery Capacity** — can they come back? Easily, slowly, only with external help, or is the break permanent/transformative?
- **Post-Break Residue** — what changes after they've broken once (new scars, altered behavior, power shift, personality hardening or softening)

---

### 8. **Mental Illness Predisposition Profile**

Not diagnosing fictional characters — mapping which clinical presentations their design and behavioral patterns *echo* or are coded toward.

**Subcategories:**

- **Primary Clinical Echo** — the most prominent pattern (PTSD-coded, narcissistic presentation, dissociative features, manic features, obsessive-compulsive rigidity, antisocial/conduct pattern, psychotic features, depression-coded, anxiety-driven hypervigilance, addiction-coded, borderline instability)
- **Secondary/Comorbid Echoes** — layered presentations (e.g., Jinx reads as PTSD + manic + attachment disorder + possible psychotic features)
- **Developmental Trauma Indicators** — does the design/lore suggest early-life disruption (abandonment coding, abuse survivor coding, parentification, institutional upbringing, feral/no-socialization)
- **Cluster Mapping** — rough Cluster A (odd/eccentric), Cluster B (dramatic/erratic), Cluster C (anxious/avoidant) lean
- **Functional Impairment Level** — high-functioning presentation, moderate impairment visible, severely impaired, or "functional precisely because of the pathology" (the ones whose illness IS their power)
- **Self-Awareness Level** — insight-full (knows they're damaged), insight-partial (senses something wrong), insight-absent (ego-syntonic, thinks they're fine), or insight-rejected (knows and doesn't care)
- **Environmental Enablers/Barriers** — does their world make it worse or provide structure? (War environment enabling PTSD cycles, power structures rewarding narcissism, isolation preventing treatment, found-family as stabilizer)

---

### 9. **Sexuality Profile**

Their sexual energy as communicated through design, not explicit lore — what the character radiates.

**Subcategories:**

- **Sexual Energy Level** — how much sexuality the design foregrounds (overtly sexual, simmering/latent, repressed-but-present, asexual-coded, threatening-sexual, unconsciously sexual, deliberately weaponized)
- **Orientation Coding** — what the design subtextually suggests or the community widely reads (straight-coded, queer-coded, bisexual-energy, ambiguous/fluid, ace-coded, "doesn't apply" for inhuman entities)
- **Dominant/Submissive Read** — power dynamics the design implies (dominant, switch, submissive, predatory-dominant, service-top, power-bottom, none/outside-framework)
- **Seduction Style** — how they'd attract (direct/aggressive, slow-burn tension, intellectual seduction, physical magnetism, danger-as-aphrodisiac, vulnerability-as-draw, doesn't try/effortless, intimidation-as-foreplay)
- **Intimacy Capacity** — design implication of emotional closeness during sex (deeply connective, performative only, dissociated, feral/purely physical, tender-but-guarded, consuming/overwhelming)
- **Sexual Confidence** — radiates comfort, performatively confident, deeply awkward, oblivious to own appeal, weaponized confidence, fragile confidence
- **Erotic Atmosphere** — the vibe around them (romantic, raw/primal, playful, dark/dangerous, sacred/ritualistic, clinical/detached, chaotic)

---

### 10. **Openness & Physicality-Implied Psychological Disposition**

What their body language, posture, design exposure level, and physical presentation suggest about their Big Five-adjacent traits — especially openness, but extending to the full spectrum.

**Subcategories:**

- **Openness Signal** — does the design radiate curiosity, exploration, creativity, or is it closed, rigid, traditionalist? (wide-open posture, exposed skin, flowing/organic shapes = high openness; armored, symmetrical, contained = low openness)
- **Extraversion Signal** — forward-leaning, space-claiming, bright colors, expressive face vs. withdrawn, covered, muted, self-contained
- **Agreeableness Signal** — soft edges, approachable silhouette, warm palette, open hands vs. sharp edges, aggressive angles, clenched/armed, barrier postures
- **Conscientiousness Signal** — meticulous detail in outfit, clean lines, organized accessories, upright posture vs. chaotic layering, asymmetry, casual/loose body language
- **Neuroticism Signal** — tension in the design (clenched jaw, rigid limbs, over-armored, tightly wound aesthetic vs. relaxed, grounded, easy posture)
- **Approachability Index** — composite read of how "safe to approach" the design communicates on a spectrum from inviting to terrifying
- **Vulnerability Display Level** — how much emotional/physical vulnerability the design allows to show (fully guarded, strategic vulnerability, openly vulnerable, vulnerability as power, forced exposure)
- **Boundary Permeability** — does the design suggest rigid boundaries (walled, masked, armored) or porous ones (flowing, exposed, merged with environment)?

---

### 11. **Fetish/Kink Alignment Profile**

What kink communities the character design caters to or activates — the tags that would appear on rule34 and adjacent spaces. Pure design-to-desire mapping.

**Subcategories:**

- **Primary Fetish Tags** — the top-level kink the design most obviously serves (e.g., bondage, monster, feet, muscle worship, latex/leather, size difference, tentacle, domination, furry, transformation, corruption, uniform/authority, voyeurism, breathplay-coded, predator-prey)
- **Body-Specific Fetish Hooks** — which physical features the design emphasizes for erotic focus (abs, thighs, hands, back muscles, neck, waist, eyes, mouth, horns/tails, wings)
- **Dynamic Fetish Tags** — kink dynamics the character implies (power exchange, praise kink, degradation, worship, pet play, brat/brat-tamer, sensory deprivation, exhibitionism, restraint)
- **Scenario/Context Fetish** — what sexual scenarios the character naturally slots into (captor/captive, forbidden romance, corruption arc, rivals-to-lovers, master-servant, stranger/anonymous, ritual/ceremonial, battle-to-bedroom)
- **Aesthetic Fetish Layer** — the visual kink (gothic, military, witch/occult, sci-fi, tribal/primal, royal/regal, medical, school/uniform, wet/slick)
- **Transgression Level** — how "taboo" the character's fetish appeal is (vanilla-adjacent, moderate kink, heavy kink, extreme/niche, eldritch-tier "what does this say about me")
- **Cross-Tag Kink Clusters** — common co-occurring tags (e.g., Evelynn = femdom + predator + glamour + pain + corruption; Warwick = monsterfucker + primal + scent + chase + feral)

---

### 12. **Combat Archetype (Fight Role)**

Their functional identity in a fight — not LoL gameplay class, but the archetypal role their *design* suggests.

**Subcategories:**

- **Primary Combat Identity** — the core fight role (berserker, duelist, assassin, tactician, artillery, guardian/wall, skirmisher, trapper, disruptor, summoner/puppeteer, overwhelming force, attrition/drain fighter, chaos agent)
- **Engagement Range** — in-your-face, mid-range, long-range, variable/adaptive, "range is irrelevant" (teleporters, global threats)
- **Win Condition Archetype** — how they end fights (burst execution, sustained attrition, outmaneuver, outlast, one decisive moment, accumulated advantage, enemy self-destruction through frustration, environmental control)
- **Threat Timing** — early aggressor, patient scaler, ambush spike, constant pressure, ticking time bomb
- **Risk Profile** — high-risk high-reward glass cannon, calculated measured risk, low-risk attrition, all-in commitment, risk-immune/transcendent
- **Fight Philosophy** — the underlying martial ethos (honor/discipline, survival at any cost, artistry in violence, cold efficiency, joyful destruction, reluctant force, predatory instinct)
- **Force Multiplier Type** — what makes them dangerous beyond base stats (terrain control, information advantage, psychological warfare, ally empowerment, resource denial, sheer unpredictability)

---

### 13. **Social Role & Group Positioning**

Where they naturally drift in social hierarchies and group dynamics — not where they're assigned, but where gravity pulls them.

**Subcategories:**

- **Default Social Position** — leader, lieutenant/right-hand, specialist/advisor, mediator, provocateur, loner-at-edge, mascot/morale, silent anchor, wild card, outsider-looking-in, above-the-group
- **Group Function** — what they actually *do* for the group (decision-maker, protector, comic relief, emotional processor, taskmaster, scout/intel, moral compass, destabilizer, glue that holds it together)
- **Hierarchy Relationship** — comfortable leading, comfortable following, resists all hierarchy, creates parallel hierarchy, subverts from within, floats outside structure
- **Social Gravity** — do people orbit them (high gravity), do they orbit someone else (satellite), do they repel others (anti-gravity), or are they neutral/invisible?
- **Conflict Role in Groups** — peacemaker, instigator, the one who splits, the one who unifies, avoidant, the one who escalates to resolve faster
- **Trust Architecture** — trusts easily, trusts no one, trusts one person completely, earns trust slowly but deeply, performs trust without feeling it
- **Social Mask vs. True Position** — is their visible role authentic or performed? (e.g., appears leader but actually needs the group more than they need them; appears loner but craves belonging)

---

### 14. **Design Focus Power Board (Category Weight Distribution)**

A meta-layer — for each champion, what percentage of the overall design energy is allocated to each of the 13 domains above. This captures *what the character is really about* at the design level.

**Format:** Percentage split across all domains totaling 100%, showing where Riot invested the most design intention.

**Example:**
- A champion like **Evelynn** might read: Sexuality 25% / Fetish 20% / Physical Appearance 15% / Decompensation 10% / Personality 10% / Fashion 8% / Combat 7% / remainder split thin
- A champion like **Garen** might read: Combat 25% / Physical Appearance 20% / Openness Disposition 15% / Social Role 12% / Fashion 10% / remainder split thin
- A champion like **Jinx** might read: Decompensation 20% / Mental Illness 18% / Personality 15% / Kinetics 15% / Coping 10% / remainder split thin

**Subcategories:**

- **Primary Design Pillar** — the single domain that carries the most weight (what the character is *about*)
- **Secondary Pillars** — supporting domains that round out the identity
- **Neglected Domains** — which categories the design barely addresses (revealing by absence)
- **Design Tension** — where two domains compete for dominance and create the character's internal friction
- **Audience Hook** — which domain is the primary reason people are drawn to the character

---

## Full Summary

The complete database now spans **14 major domains** across every League champion:

1. **Physical Appearance** — granular glamour-fantasy body tagging
2. **Subtextual Physicality** — what the body implies about capability
3. **Personality** — archetype, emotional, moral, and social descriptors
4. **Kinetic Behavior** — movement from animation and biomechanics lenses
5. **Fashion & Accessories** — costume as its own searchable design layer
6. **Coping Mechanisms** — how they manage stress and pain
7. **Decompensation** — how they break when coping fails
8. **Mental Illness Predisposition** — clinical echoes and trauma coding in design
9. **Sexuality Profile** — sexual energy, orientation coding, dynamics, intimacy capacity
10. **Openness/Disposition** — Big Five-adjacent traits read through physicality
11. **Fetish/Kink Alignment** — what desire communities the design serves
12. **Combat Archetype** — fight role, philosophy, win condition
13. **Social Role** — group positioning, hierarchy relationship, social gravity
14. **Design Focus Power Board** — meta-distribution of design energy across all 13 other domains

The system functions as a **deeply cross-referenceable character taxonomy** where every champion is profiled across psychological, sexual, kinetic, social, martial, and aesthetic dimensions simultaneously. The power board ties it together by revealing where the design emphasis actually lives for each character, exposing what Riot was really selling with each champion.

Ready to start building the actual file and populating champions?