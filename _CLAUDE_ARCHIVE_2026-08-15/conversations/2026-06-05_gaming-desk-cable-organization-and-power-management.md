---
title: "Gaming desk cable organization and power management"
uuid: bc9b14b4-e4e5-4735-b2ff-c7c540df421a
created: 2026-06-05
updated: 2026-06-05
trunk: BLACK
messages: 6
chars: 28163
artifacts: 0
generated_files: 0
tools: [image_search]
source: claude.ai-export-2026-08-15
---

# Gaming desk cable organization and power management

> **Conversation Overview**

The person is planning a custom power management setup for a high-end gaming desk and wants to replace a messy surge protector situation with a clean, rack-mounted system. They have a specific aesthetic goal: a tactile, mechanical startup sequence inspired by analog fighter jet cockpits (F-14/F-15), where they flip individual physical switches to power up different devices — PC, router, and other peripherals — independently and in sequence. They are technically engaged and comfortable with hardware concepts, and they asked direct, iterative questions to refine the architecture toward something that matched both their functional and aesthetic goals.

Claude introduced the core terminology they were missing: a switched rack-mount PDU (Power Distribution Unit) as the outlet distribution layer, and a rolling open-frame 19-inch rack on casters as the enclosure. Claude walked through three increasingly refined approaches as the person's preferences clarified. First, a standard switched PDU with per-outlet toggles on the unit itself. Second, a separate switch panel interfacing with the PDU via either a network/API path (smart PDU + button box + controller) or a pure relay-control path (low-voltage switches driving sealed relay blocks, with no computer involved). When the person explicitly rejected the networked/API approach as too complicated and non-tactile, Claude pivoted fully to the electromechanical relay path: physical toggle switches on a low-voltage panel energizing relay or contactor coils, which physically switch the mains, producing an audible mechanical clack per device — zero processing, zero network, zero firmware. Claude recommended Digital Loggers sealed relay blocks as a safe, UL-listed way to handle the mains-switching side without hand-wiring 120V, and suggested aircraft-style guarded toggle switches with flip-up safety covers for the panel aesthetic.

The person communicates conversationally and iteratively, thinking out loud and refining their idea through dialogue. They appreciate direct, technically honest responses — Claude flagged safety concerns about hand-wiring line voltage clearly and early, and consistently steered toward solutions that kept mains wiring inside sealed, pre-engineered components. The conversation ended with Claude offering to spec the complete parts list (switch type, relay blocks sized to actual device loads, panel, and rack stack order relative to PDU and UPS), which the person had not yet confirmed or declined.

---
## 🧑 Papi  <sub>2026-06-05 12:27:57</sub>

okay i want to be able to fix two birds with one stone i have like a a really nice gaming desk however the sort of cable power organization situation is bag in the bat not the very good in the back like i have a power like a what do you call it a freaking surge protector back there but there's so many wires i have like these little extenders that all my things that are plugged into go into and it's all just stuck back there Like, is there a more elegant way to do this to keep it kind of... I'm... I I kind of want to sort of create my own custom, uh, sort of three prong gauge wiring that will go... have custom length, and that will go actually into a switch box. And then I'll have... I'll be able to control each power band. Like, I'd be able to turn on my PC separately than my router. They have little switches for it. And by having, like, a little custom panel box, I can actually, like, wire it elegantly in a way and insulate it before, I guess, running it all to a, uh, UPS. Is that even possible? Or what is that even... what is, like, a panel box? Is that what they call it? Like, the the kind that you can buy just off the shelf and put it into a sort of a a rolling rack. What is that called?

---

## 🤖 Claude  <sub>2026-06-05 12:29:41</sub>

They're looking to build a custom electrical setup for their gaming desk—creating custom-length power cables that feed into a switchable distribution panel where they can control different devices independently (like powering the PC separately from the router), then routing everything through a UPS for protection. The person seems to be describing a fairly involved electrical project to replace their current messy surge protector situation.

What they're actually asking about is whether this thing has a specific name—and it does. They're describing a rack-mount power distribution unit (PDU) with individually switched outlets, which is exactly what they need. These mount into a 19-inch rolling rack and let you toggle each outlet on and off independently. The custom wiring part is where I need to flag some caution—making your own mains power cables is possible but carries real electrical safety risks, and there are safer pre-made alternatives available. ched PDU) as the core answer, then address the custom wiring angle honestly — it's doable but mains AC work carries real risk, so I should highlight that the switched PDU already solves the per-outlet control they want without the custom wiring hazard. Given their background with UPS research and DIY rigging, they'll appreciate the direct tradeoff: off-the-shelf elegance versus custom work with genuine safety considerations. I'll skip the search since this is stable product-category knowledge and they're asking more about what exists than specific current models. ched PDU), and the rolling rack.
2. Address the custom wiring idea honestly — the per-outlet switching they want is already a solved product, so they probably don't need to build custom mains wiring (and the DIY mains part is the genuinely risky bit).
3. Connect it to their UPS (rack-mount UPS exists too; their CyberPower/APC choice matters for form factor).

Let me think about the terminology precisely:

- **PDU (Power Distribution Unit)**: rack-mount strip of outlets. Comes in basic, metered, switched, and switched+metered versions.
  - **Switched PDU**: lets you turn individual outlets on/off — often remotely via network. This is the "control each power band separately" thing.
  - There are also simpler ones with physical per-outlet toggle switches.
- **Rack / rolling rack**: 19-inch equipment rack. On casters = mobile/rolling rack. Open-frame vs enclosed. For a desk setup, an "open frame rack" or a small "rack cabinet" on wheels.
- **Furman**: brand known for rack-mount power conditioners and sequencers in the AV/studio world — they stage power-on sequences to avoid inrush current spikes.

For the custom wiring piece, they're probably thinking about making custom-length power cords with the right gauge for their current draw. Most computer gear uses IEC C13/C14 connectors, and while you can build cables from bulk cable and connectors, the factory-molded ones are safer and easier. The "panel box" they're imagining — where they'd wire and insulate everything — sounds like they're picturing either an electrical panel (which is way too permanent and complex) or a project enclosure, but really a PDU is the off-the-shelf solution that handles all of this. I should gently clarify that terminology so they understand what product actually solves their problem.

For the control piece: they want to turn the PC on/off separately from the router and other devices. A switched PDU does exactly this — either with physical per-outlet switches or network control. There are cheaper consumer options too (power strips with individual switches, smart plugs like Kasa), but for a rack setup, a switched PDU is the elegant solution.

One more thing to flag: the ordering of UPS → PDU in the power chain. Typically it's wall → UPS → PDU → devices. The UPS gives battery backup and surge protection; the PDU distributes and switches. If they're going rack-mount, they should check whether their UPS has a rack variant (like the APC SMT2200RM, which is the rack version of the SMT2200).

On the custom wiring safety angle: I want to be direct and helpful but honest. The risky part is building your own line-voltage AC wiring. If done with proper gauge, strain relief, and insulation, it's doable, but it's also where mistakes cause fires or shocks. The per-outlet switching they want is already a solved product, so they probably don't need to go down that road.

For the control piece, a switched PDU (physical switches or network-controlled) solves their desire to turn the PC on/off separately from the router and other devices. Cheaper alternatives exist like power strips with individual switches or smart plugs, but for a rack setup, a switched PDU is the cleanest approach. On the power chain: wall → UPS → PDU → devices, so if they're going rack-mount, they should verify their UPS has a rack variant (the APC SMT2200RM is the rack version of the SMT2200).

On custom wiring: I want to be direct but honest. Building your own line-voltage AC wiring is genuinely risky — mistakes cause fires. They don't need to do it anyway, since switched PDUs already provide per-outlet control, and they can get custom-length pre-made IEC cables for clean cable runs instead. For any DIY element, custom-length IEC jumper cables (C13-to-C14 for daisy-chaining within the rack) are standard rack components and available in exact lengths — that gives them the elegance without the safety risk of hand-wiring mains.

Now I'm thinking about format and whether to include images. This is a "what is it called" question, so I should lead with the product name and explain it, then address the custom wiring concern with honest pushback, then point toward the off-the-shelf solution. A switched PDU and rolling rack are visual products they're trying to identify, so images could genuinely help here — but I should be careful not to over-format for a mobile interface. I'm torn on whether to include images here. Two image searches would give me 6-8 results on mobile, which could feel cluttered, but they're asking "what is this thing called" and "does it exist" — visual confirmation would actually be pretty helpful for that. I think I'll do two searches: one for switched rack PDUs and one for rolling racks, interleaved at the relevant points. That's justified and not excessive.

I don't need web search for the terminology itself — PDU, switched PDU, and rack are stable concepts. But if they want specific product recommendations later, that's when I'd search for current models. For now I can answer from knowledge and offer to pull options if they ask.

I should also weave in that the CyberPower and APC units they were looking at earlier are tower form factors — if they're going full rack, they'd want the rackmount variants instead. That's a useful connection without over-surfacing memory.

Let me keep the response tight and mobile-friendly, trim the excess, and dial back the formatting. I'll lead with the key term they're looking for, include the two images at natural points, and end with the offer to search for current models since that's present-day product data.What you're describing already exists as a single off-the-shelf product: a **switched rack-mount PDU** (Power Distribution Unit). It's a strip of outlets where each outlet (or bank) has its own switch, so you can kill the PC without killing the router — exactly the "control each power band separately" thing you sketched. Your "panel box" instinct is right, just the wrong word. In electrical terms a "panel box" is a breaker/load center (permanent house wiring). The rack version of that idea is a PDU.
```
This block is not supported on your current device yet.
```

 Now moving on to the rolling rack image.The "rolling rack" is just a 19-inch equipment rack on casters. Open-frame ones are cheap and keep airflow clean for a desk-side setup; enclosed cabinets look more finished. The PDU bolts in, the UPS bolts in below it.
```
This block is not supported on your current device yet.
```


```
This block is not supported on your current device yet.
```

Now the pushback, since you'd rather hear it straight: you've basically reverse-engineered a product that already exists, so skip hand-building your own mains wiring. The per-outlet switching is solved by the switched PDU. The "custom length, clean runs" goal is solved by custom-length IEC cables (C13/C14) — buy them cut to length or make low-voltage-side jumpers without ever touching line-voltage wiring. Hand-wiring 120V mains is the one part of this with real fire/shock risk, and it buys you nothing the PDU doesn't already give you. Put the DIY energy into rack layout and cable management instead.

Stack order is wall → UPS → PDU → gear. One heads-up: the CP2200AVRLCD and SMT2200C you were eyeing are both tower units. If you're committing to a rack, grab the rackmount variant (e.g. APC SMT2200RM2UC) so it bolts in instead of squatting on the floor.

Switched PDUs come in three flavors: physical per-outlet toggles (cheapest, matches your "little switches" idea most directly), metered (shows live draw), and network/smart (toggle each outlet from your phone or PC). Want me to pull current models with real per-outlet physical switches in a given price range?

---

## 🧑 Papi  <sub>2026-06-05 12:47:49</sub>

Okay. So let's say I get a... just a a PDU, right, with twelve or nineteen outlets that come out the back. Is there a way I can still somehow interface a physical switch between it so I can at least have that type of experience in another rack, like, in a rack below it so I could just flip, flip, flip, flip, flip at a time? Like, I know there are switched PDUs, but, like, how would I be able to interface up with, like, an actual physical button press?

---

## 🤖 Claude  <sub>2026-06-05 12:49:27</sub>

I'm understanding what they're really after — a basic PDU feeding into a separate switch panel where each physical switch controls the power to individual outlets, essentially creating a manual relay system for the rack. This involves some serious electrical considerations since we're talking about interrupting mains power at each outlet, so I need to think through the safety implications and whether this is even feasible to wire safely. think about what the legit, safe, off-the-shelf ways to do this are versus the DIY-mains-wiring path (which is the dangerous part I flagged before).

Options for "a separate rack panel of physical switches that control individual outlets":

1. **Rackmount power strip / PDU that already has the switches built in** — but they specifically want the switches in a separate unit below, not on the PDU itself. So this is them deliberately separating the switch bank from the outlet bank.

2. **AV "switch panel" / "rack switch panel"** — there are rackmount panels with illuminated rocker switches. But the key question: what do those switches control? Generally these are either (a) low-voltage control switches that drive relays/contactors, or (b) actually switching mains directly (which means mains wiring runs to the panel — the risky part).

3. **The clean, safe answer: relay-based control.** Use switches that are low-voltage (e.g., 12V or even just dry-contact) that trigger relays which switch the mains. This way the physical switch panel only carries low voltage; the mains switching happens inside an enclosure near/at the PDU.

The practical approach is a smart PDU with a separate control surface — either a Stream Deck or a custom button box with an ESP32 that sends network commands to toggle outlets, keeping all mains switching contained within the PDU itself. They want the mechanical "flip flip flip" feel of physical buttons, and this gives them that without ever running mains to the panel. Lowell makes rackmount power panels with individual switches that can control power directly or via relays—that's the off-the-shelf AV solution. The genuinely safe approach for DIY would be a low-voltage switch panel controlling a bank of relays or contactors in a separate enclosure, keeping the user-facing switches safe while the mains-switching components stay properly engineered in a dedicated cabinet.

Given their technical background in hardware and electronics, I should recommend the proper architecture: separate control from switching, point them to existing products that do this safely, and be clear about which approaches expose mains to hand-touched panels versus which contain it properly. They probably want a separate switch panel because high-outlet PDUs rarely come with per-outlet physical switches, so they're looking to pair a basic PDU with a dedicated control panel.

The cleanest recommendation is a smart switched PDU paired with a physical button controller—something like a macropad or custom ESP box that sends commands over the network rather than directly switching mains. That gives them the tactile "press press press" experience safely. Alternatively, if they want true mechanical switches, I should describe a relay or SSR control panel where low-voltage rocker switches drive relays in an enclosure that handle the actual mains switching—keeping high voltage completely contained and away from their hands. If they insist on mechanical switches directly in the mains path, they need to be properly rated for both voltage and current, with enclosed, fused, and strain-relieved wiring—ideally a UL-listed assembly. For the "interface up" requirement, physically inserting switches into an already-assembled PDU's outlets isn't practical, so the better approach is to place relay modules downstream of the PDU outlets (each device cord connects through a switched relay to the PDU outlet) or use a PDU that's already designed with switching built in.

The cleanest consumer option is in-line cord switches or individually-switched smart plugs, but that doesn't have the rack-mounted aesthetic they're after. For a proper "flip flip flip" feel with safety, I should present two solid architectures: a command-based setup using a network switched PDU paired with a physical button box (Stream Deck or custom ESP32 macropad sending API calls—true mechanical presses, zero mains contact), or a relay-control panel with illuminated rockers on a rack unit carrying only low voltage, driving a relay/contactor bank in an enclosed box that handles the actual mains switching. Off-the-shelf options like Lowell or AV power sequencer panels already do this. The key safety principle is separating control (low voltage, safe to touch) from switching (relays sealed in a box, properly fused and rated).

I should also clarify that a switch in series with the hot line interrupts power, and it must be rated for at least the load's voltage and current. For a 12–19 outlet PDU, each branch could draw significant current, and the total can't exceed roughly 15A on a standard 120V/15A circuit. I don't think I need to search for this—it's mostly conceptual architecture and stable product-category knowledge. Lowell and Furman rack power panels with contact-closure triggers are long-standing AV products. I'll keep model references light and offer to search for current specific products if they want buy recommendations.

For format, this is a how-to/architecture question from a technical person, so I'll lead with the direct answer, present two named approaches clearly, flag the safety issue, and offer to spec it further or pull current products. I'll avoid heavy formatting and skip images since this is electrical architecture, not visual design. The key insight to lead with is that you can't easily insert a switch into a finished PDU's outlets—instead, you separate control (low voltage, safe) from switching (relays in an enclosed box, properly fused). I'll keep it tight and digestible for mobile.The simplest answer is a PDU with the toggles on its own front face — but you've said you want the switches separated into a unit below it, so here's the real constraint: you can't cleanly insert switches into a finished PDU's outlets. They're sealed, and you absolutely should not hand-wire 120V out to a row of rocker switches you touch. The correct move is to split *control* (your switch panel — low voltage, safe to touch) from *switching* (relays that actually break the mains, sealed in a box). Two ways to get the flip-flip-flip feel:

**1. Relay-control panel (true mechanical switches).** Illuminated rockers on a 1U panel carry only low voltage (12/24V). Each switch drives a relay or SSR sitting inline between the PDU outlet and the device. You flip it, the relay breaks the mains — your fingers never see line voltage, only the relay enclosure does, and that box gets proper fusing and strain relief (or you buy it pre-built). The AV industry sells exactly this as rackmount power sequencers / control panels with contact-closure triggers — Lowell and Furman are the usual names. That's the off-the-shelf version of your idea.

**2. Network PDU + button box (presses, not flips).** Get a switched/network PDU, then build a button panel — a Stream Deck, or arcade buttons on an ESP32 — that fires the PDU's API/SNMP toggle per outlet. Real physical press per device, zero mains contact, mountable anywhere, and you get "all-off" scenes for free. Less chunky-mechanical, more flexible.

The thing to avoid is the obvious-looking one: running each hot leg out to cheap panel rockers and wiring it yourself. A mechanical switch in the mains path has to be rated for the device's actual current (a 15A load on a 6A rocker is a fire), enclosed, and fused — which is the whole reason the relay approach exists. It keeps the dangerous part in one sealed, properly-built box and lets you have as many cheap finger-switches as you want.

Want me to spec one path end to end — panel + relay/contactor box + matching PDU — or pull current AV control panels that already do the mains side for you?

---

## 🧑 Papi  <sub>2026-06-05 12:51:30</sub>

Okay. There's, like, a whole, like, API run with it. It's, like, at the button box. Do I need, like, some sort of just... I don't know. Some sort of processing power, like, some sort of... I don't know. Raspberry Pi running or something in it, or is there, like, all that within the switch itself? Like, I I want this to be less complicated, like, less in the network and more just tactile. You know, it's meant to be very much akin to, like, the start up process for a... like, I'm starting a a fighter jet almost of, like, a f fifteen, maybe even f fourteen being a very analog and mechanical type feel start up sequence.

---

## 🤖 Claude  <sub>2026-06-05 12:53:07</sub>

They're really after that pure mechanical experience — flipping switches without any computer involvement. The relay-control panel approach is what they need, not the networked button box solution, since they want tactile feedback and zero network dependency. -14/F-15 analog feel. I should steer them hard to option 1 and kill the API path for their goal.

Let me explain the relay path cleanly: switches → relays/contactors → mains. No brain. The "processing" is just the relay coil being energized. It's the most analog thing possible.

Let me address their question directly: "do I need a Raspberry Pi or is it in the switch?" 

For the API/network PDU path: yes, you'd need something running — either the PDU has its own network controller built in (so the "brain" is in the PDU), or a Stream Deck has its own firmware, or an ESP32/Pi runs code. So that path always has a computer somewhere. That's the networked path.

But they want tactile/analog. So: drop the API path entirely. Go pure relay. No Pi, no network, no firmware, no API. Just: physical switch closes a low-voltage circuit → energizes relay coil → relay contacts close → mains flows to device. It's 100% electromechanical. The satisfying part is literal — the relay or contactor physically clacks when it pulls in, which is exactly the fighter jet aesthetic they're after.

The relay approach leans into what they actually want: contactors make a mechanical THUNK, and I can pair that with illuminated rockers or toggle switches with safety covers — those flip-up red guards are pure fighter jet vibes. For the physical setup, they'd need a row of low-voltage switches, a relay or solid-state relay for each device's mains current, a low-voltage power supply to energize the coils, and an enclosure to house everything. No microcontroller required — the switch directly triggers the relay coil. I'm now weighing whether they even need a separate low-voltage supply or if there's a simpler architecture using mechanical relays with low-voltage coils. mall DC/AC supply energizes coil, contacts carry mains. Switch panel is low voltage = safe to touch. Need a small PSU for the coil voltage.
2. **You could use a switch directly rated for mains** but then the switch panel carries line voltage = the dangerous thing we're avoiding. Don't.
3. **SSR (solid state relay)**: control side is low-voltage DC (3-32V typically), load side switches AC. No moving parts, silent, no clack. Less "analog feel" but reliable. For the fighter-jet THUNK they want, mechanical relays/contactors are better — they make noise.

So for maximum analog/tactile/mechanical feel: mechanical relays or contactors (the kind that go CLACK). The switch on the panel is low voltage. A small 12V or 24V DC supply powers the coils. Each switch energizes one coil. Done. No computer.

Actually, even simpler framing: this is just like how a car works — you flip a switch, a relay clicks, the headlights come on. No computer in a 1970s car. Same principle. Or a fighter jet's bus switches energizing relays. That's the whole brain right there — pure cause-and-effect electromechanics with no intelligence involved.

They could also sidestep building the mains side by buying a pre-assembled relay box or contactor module, or even an AV sequencer from companies like Lowell or Furman, then just wire their switch panel to the trigger inputs. This keeps the dangerous high-voltage work sealed and bought. The catch is that most AV sequencers power things in a timed sequence from one trigger, but they need individual per-switch control — each switch independently controlling its own relay zone. So they'd need a relay panel product that supports independent zone triggering rather than a sequencer.

The safest "buy it" approach: get a rackmount power controller with individual zone control via low-voltage triggers, wire the switch panel to those triggers, and avoid hand-wiring mains altogether. Or if they go DIY relay box, they could buy pre-wired modular units like DIN-rail contactors or UL-listed IoT relay boxes (like the Digital Loggers IoT Relay) that accept a simple 3-5V signal to switch AC mains — no network needed, just low-voltage trigger to high-voltage switching.

The Digital Loggers IoT Relay is actually a solid building block: it's a power strip with sealed mains internals, UL listed, and you just feed it a low-voltage control signal from the switch panel. Stack a few of them to get individual outlet control per zone, and the mains side is completely handled for them.

So the real distinction is: the networked path always needs a brain (PDU, Pi, Stream Deck), but the pure analog path is just relays with no network, no code, no computer—just a switch energizing a coil and the relay clacking. That's the tactile, fighter-jet feel they're after. They can buy sealed relay blocks and wire only the low-voltage control side to their switches, avoiding any mains wiring themselves.

For the sequencing question, individual switches give them manual sequencing (flip them in order), which is probably what they want—that hands-on startup ritual. If they need enforced sequencing where one device can't power up until another is already on, that's a separate sequencer device, but I think they're really just after the tactile experience of flipping switches one at a time.

The aesthetic angle is worth hitting: guarded toggle switches (the flip-up missile covers), illuminated toggles, engraved panel labels—that's the F-14 vibe they're describing, and it fits their aesthetic sensibility perfectly. I should keep the answer dense and direct since they prefer efficiency, lead with the conceptual answer (no Pi needed), explain the mechanism, cover the safety angle with sealed relay blocks, touch on the aesthetic, and offer to spec the exact parts.No Raspberry Pi. No network. No code. For the feel you're after, you want the *opposite* of the API path — drop it entirely. A network/smart PDU always has a brain somewhere: either built into the PDU, or a Stream Deck / ESP32 / Pi feeding it commands. That's the networked route, and it's exactly what you said you don't want.

The tactile path has zero processing. It's pure electromechanics — same logic as a fighter jet's bus switches or a car's headlight relay. You flip a switch, that closes a *low-voltage* circuit, the circuit energizes a relay coil, and the relay's contacts physically slam shut to pass the mains through. The "intelligence" is none; it's cause and effect. And it's more analog than you're picturing: a mechanical relay or contactor literally goes *thunk* when it pulls in. A row of them, flip-flip-flip, gives you a rack full of mechanical clacks as each device wakes up. That's the F-14 startup, for real.

How it stays safe and computer-free: your switch panel only ever carries low voltage (12 or 24V), so your fingers never touch line voltage. A small DC wall supply powers the coil side; the mains lives inside the relays. To avoid hand-wiring 120V yourself, buy sealed, UL-listed relay blocks — Digital Loggers makes boxes where you feed a low-voltage trigger and it switches the AC internally, so the dangerous part is done and listed. Wire your toggle panel to their control terminals and you're set. One block per device or zone, stacked below your PDU.
```
This block is not supported on your current device yet.
```

For the cockpit feel, the switch itself does most of the work: aircraft-style toggles with the flip-up safety guards (the "missile covers"), or illuminated toggles that glow when the relay's live. Engraved 1U panel, labeled per system. All of that is low-voltage and harmless to build — the menace is purely visual.

One honest caveat on the "startup sequence" part: individual switches give you *manual* sequencing — you flip them in the order you choose. If you ever want *enforced* staging (router must come up before the PC, or staggered power-on to soften inrush on the UPS), that's a true power sequencer's job, and it can coexist with your panel. But for the flip-flip-flip ritual, individual relays nail it.

Want me to spec the exact parts — switch type, relay blocks sized to your PC/router/monitor draw, the panel, and how it all stacks under the PDU and UPS?