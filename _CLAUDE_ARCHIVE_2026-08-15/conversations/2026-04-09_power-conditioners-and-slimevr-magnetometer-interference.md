---
title: "Power conditioners and SlimeVR magnetometer interference"
uuid: 5a566ba7-f35c-4141-819c-8ef9169bca6a
created: 2026-04-09
updated: 2026-04-09
trunk: BLACK
messages: 4
chars: 5757
artifacts: 0
generated_files: 0
tools: []
source: claude.ai-export-2026-08-15
---

# Power conditioners and SlimeVR magnetometer interference

> **Conversation Overview**

The person is working with SlimeVR full-body tracking technology and asked Claude to help them reconstruct and develop a line of thinking they had partially lost. The conversation centered on whether power conditioners and other electronics emit magnetic fields that could interfere with SlimeVR IMU (Inertial Measurement Unit) sensors, particularly magnetometers used for yaw orientation tracking.

Claude explained the core technical issue: SlimeVR trackers use IMU chips (such as the BNO085 or ICM-series) that include magnetometers reading Earth's magnetic field for absolute heading reference, and nearby electromagnetic sources — including power conditioners with transformer cores — can corrupt these readings through hard or soft iron distortion. The person then asked for a tiered breakdown of mitigation strategies organized as standard practice, leading edge, and bootstrap/DIY approaches for a room-based recording setup with significant electronics present.

Claude provided a structured three-tier response covering: standard approaches (mag-off mode, distance rules, in-room calibration), leading-edge techniques (BNO085 chip selection for its dynamic disturbance rejection, mu-metal shielding, active field mapping with a reference magnetometer), and hokey bootstrap methods (aluminum foil enclosures, relocating power strips, improvised soft iron compensation, and manual yaw reset workflows). The recommended practical combination for a production recording environment was identified as BNO085 with mag-off mode and a consistent room layout per session. The person demonstrated familiarity with SlimeVR hardware and framing technical problems in accessible, layered ways, and uses informal, exploratory speech when developing ideas.

---
## 🧑 Papi  <sub>2026-04-09 22:52:14</sub>

Power conditioners affect magnetic fields? Let's say if I was using a, If I was using slimeVR, those little chips with the, sensing with the multiple fields of direction. You know what I mean? Like, like, how let's help me develop this because I forgot where I

---

## 🤖 Claude  <sub>2026-04-09 22:52:30</sub>

The user is asking about power conditioners and whether they affect magnetic fields, specifically in the context of SlimeVR trackers. SlimeVR uses IMU (Inertial Measurement Unit) sensors that rely on magnetometers to detect Earth's magnetic field for orientation tracking. They're wondering if power conditioners could interfere with the magnetic sensing in SlimeVR trackers.

Let me think through this:

1. SlimeVR uses IMUs (like BNO085, MPU-6050, ICM-42688-P, etc.) that include accelerometers, gyroscopes, and sometimes magnetometers


2. Magnetometers detect Earth's magnetic field for absolute heading/yaw correction, and power conditioners with transformers and switching circuits can generate electromagnetic interference that might disrupt this magnetic sensing. The real concern here is whether the EMI from power conditioning equipment—especially the 50/60Hz magnetic fields from transformers—could actually interfere with the magnetometer-based orientation tracking in SlimeVR.You're circling around something real. Let me reconstruct what you're building toward:

**The core concern:**
SlimeVR trackers use IMUs — chips like the BNO085 or ICM chips — that contain **magnetometers**. The magnetometer reads Earth's magnetic field to anchor absolute **yaw** (rotation around the vertical axis). Without it, yaw drifts over time.

**The problem with magnetic interference:**
Magnetometers are extremely sensitive. Any nearby source of a magnetic or electromagnetic field can corrupt the reading — this is called **magnetic interference** or **hard/soft iron distortion**. Common culprits:

- Speakers, subwoofers
- Power strips and surge protectors
- **Power conditioners** — especially ones with large toroidal or EI-core transformers, which emit 50/60Hz AC magnetic fields
- Monitors, TVs
- PC cases with large PSUs

**So yes — power conditioners can absolutely interfere with SlimeVR magnetometers**, especially if a tracker is physically close to one.

**What this means practically:**
- SlimeVR's magnetic environment calibration ("6-point calibration") tries to compensate for *static* distortion, but *dynamic* interference (like fields that change based on load) is much harder to correct
- Some IMU modes on SlimeVR actually **disable the magnetometer entirely** and rely on gyro + accel only, which avoids this but increases yaw drift

**Where were you going with this?** Were you thinking about:
- Tracker placement strategy around your setup?
- Whether to use mag-on or mag-off mode?
- Something about your boutique SlimeVR build?

---

## 🧑 Papi  <sub>2026-04-09 22:54:23</sub>

Well, how would I like, if I was recording a lot of slime VR's tech stuff in a room with electronics in it, like, what would be the best way to mitigate all of that interference as much as possible? Like, what is the standard and then the leading edge and then kind of like a hokey bootstrap way.

---

## 🤖 Claude  <sub>2026-04-09 22:54:39</sub>

The user wants three tiers of magnetic interference mitigation for SlimeVR in an electronics-heavy room:
1. Standard/conventional
2. Leading edge
3. Hokey/bootstrap DIY

Let me think through this properly.Good framing. Three tiers:

---

## Standard (What the SlimeVR community actually recommends)

- **Mag-off mode** — just disable the magnetometer entirely. Use gyro+accel only, do a yaw reset at the start of each session. Drift is manageable for short takes.
- **Distance rule** — keep trackers at least 50–100cm from known emitters (PC, monitors, power strips)
- **Static calibration** — run the 6-point mag calibration *in the actual room* so it maps the specific distortion field of your space
- **Consistent tracker orientation on body** — reduces the impact of soft iron distortion from your own gear/clothing

---

## Leading Edge

- **IMU selection** — the BNO085 has onboard sensor fusion with dynamic magnetic disturbance rejection built into the FSAM algorithm. It actively detects and discards bad mag readings in real time. Choosing this chip specifically for mag-heavy environments is the move.
- **Mu-metal shielding** — a thin wrap of mu-metal (high-permeability nickel-iron alloy) around the tracker PCB attenuates low-frequency magnetic fields before they hit the chip. Used in pro audio and medical IMU applications.
- **Active field mapping** — place a reference magnetometer stationary in the room, log the ambient field, and use that as a noise baseline to subtract from tracker readings in post or live. Nobody in the SlimeVR consumer space is doing this yet.

---

## Hokey Bootstrap

- **Aluminum foil enclosure** — doesn't actually block magnetic fields (aluminum is non-ferromagnetic) but it *does* block some RF/electric field noise. People swear by it. It's doing something, just not what they think.
- **Move the power strip across the room** — genuinely effective, zero cost, zero tech
- **Stick steel wool or a fridge magnet sheet behind the tracker** — janky soft iron compensation. Chaotic but sometimes it accidentally helps calibration stick better.
- **Mag-off + manual yaw reset hotkey** — bind a key, reset yaw every 2–3 minutes during recording, edit around the snaps. Costs nothing, works fine for content.

---

The real answer for a production recording setup is probably **BNO085 + mag-off + consistent room layout** every session. That combo eliminates the variable without needing to fight the physics.