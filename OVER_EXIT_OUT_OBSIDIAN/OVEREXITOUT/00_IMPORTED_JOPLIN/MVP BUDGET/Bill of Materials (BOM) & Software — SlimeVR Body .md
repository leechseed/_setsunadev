---
title: Bill of Materials (BOM) & Software — SlimeVR Body + ARKit Face
updated: 2025-09-28 18:27:50Z
created: 2025-09-28 18:25:01Z
latitude: 30.43825590
longitude: -84.28073290
altitude: 0.0000
---

# Bill of Materials (BOM) & Software — SlimeVR Body + ARKit Face

> This is a clean, drop-in Markdown parts list for a **SlimeVR body suit (10 nodes)** plus **ARKit facial capture**. No base stations, no optical.

---

## Table of Contents

* [A. Core System Overview](#a-core-system-overview)
* [B. Per-Node Hardware (×10 body nodes)](#b-per-node-hardware-×10-body-nodes)
* [C. Shared Hardware (one-time items)](#c-shared-hardware-one-time-items)
* [D. ARKit Facial Capture](#d-arkit-facial-capture)
* [E. Software Stack](#e-software-stack)
* [F. Tools, Consumables, and Printables](#f-tools-consumables-and-printables)
* [G. Optional: Prop Nodes (orientation-only)](#g-optional-prop-nodes-orientation-only)
* [H. Quick Ordering Checklist](#h-quick-ordering-checklist)

---

## A. Core System Overview

* **Body tracking:** 10× IMU nodes (ESP32-S3 + BNO085), **rotations only**, streamed to SlimeVR Server.
* **Face tracking:** iPhone (TrueDepth) → ARKit blendshapes to engine (Unreal/Unity/Blender bridge).
* **Position:** none (IK solves limbs; accept some foot skate).

---

## B. Per-Node Hardware (×10 body nodes)

| Item                           | Purpose                        | Key Specs / Notes                                                               |       Qty |
| ------------------------------ | ------------------------------ | ------------------------------------------------------------------------------- | --------: |
| **BNO085/BNO080 IMU**          | Orientation (on-sensor fusion) | Use **Game Rotation Vector** (mag off indoors). SPI preferred; I²C ok if short. |        10 |
| **ESP32-S3 dev board**         | MCU + Wi-Fi                    | USB-C; ideally **onboard LiPo charger (JST-PH)**.                               |        10 |
| **LiPo 3.7 V 750–1000 mAh**    | Power                          | ~6–10 h typical runtime.                                                        |        10 |
| **Mini slide switch**          | Power control                  | Inline with battery + board.                                                    |        10 |
| **Short wiring set**           | IMU↔MCU + battery              | SPI (or I²C) leads; **JST-PH** pigtail.                                         | as needed |
| **M2 standoffs/screws**        | Mounting                       | Secure PCB inside case.                                                         |       set |
| **3D-printed case (PETG/ABS)** | Enclosure                      | Strap slots; **UP/FWD** arrows on lid.                                          |        10 |
| **Elastic/Velcro straps**      | Wearable mount                 | Sizes for hips, chest, head, arms, feet.                                        |       set |

**Recommended placement (10):** Hips, Lower Spine, Upper Chest, Head, Upper Arms L/R, Forearms L/R, Feet L/R.

---

## C. Shared Hardware (one-time items)

| Item                         | Purpose                | Notes                                            |       Qty |
| ---------------------------- | ---------------------- | ------------------------------------------------ | --------: |
| **Wi-Fi router (dedicated)** | Low-latency link       | Use **5 GHz** SSID for suit; **PC on Ethernet**. |         1 |
| **Multi-port USB-C charger** | Fleet charging         | 6–12 ports; short cables.                        |         1 |
| **USB-C cables (short)**     | Charge/program         | 15–30 cm, reliable.                              |     10–15 |
| **Spare LiPos**              | Hot-swap/backup        | Same capacity/connector.                         |       2–4 |
| **Labels / ID set**          | Node IDs & orientation | “HIPS, CHEST, HEAD…”                             |     1 set |
| **Storage & ESD**            | Organization/safety    | Small bins, anti-static bags.                    | as needed |
| **Ethernet cable**           | PC↔router              | Cat6/6a, 2–5 m.                                  |         1 |

---

## D. ARKit Facial Capture

| Item                   | Purpose           | Notes                                                 |   Qty |
| ---------------------- | ----------------- | ----------------------------------------------------- | ----: |
| **iPhone (TrueDepth)** | Face capture      | Any FaceID device (X or newer).                       |     1 |
| **Face capture app**   | Blendshape stream | e.g., **Live Link Face** (Unreal) or **OSC/UDP** app. | 1 app |
| **Tripod/phone clamp** | Stable framing    | Consistent angle/distance.                            |     1 |
| **Same 5 GHz LAN**     | Networking        | Join suit network; keep link clean.                   |     — |

> In engine: **head rotation = IMU**; apply ARKit blendshapes as **local face offsets** (disable ARKit head pose if it conflicts).

---

## E. Software Stack

| Layer                | Name                         | Purpose / Notes                                   | Target |
| -------------------- | ---------------------------- | ------------------------------------------------- | ------ |
| **Toolchain**        | PlatformIO or Arduino IDE    | Build/flash ESP32-S3 firmware.                    | PC     |
| **USB drivers**      | CP210x / CH34x (as needed)   | For your ESP32 board.                             | PC     |
| **Tracker firmware** | **SlimeVR Tracker Firmware** | BNO085 Game Rot Vec; 100–200 Hz quats over UDP.   | ESP32  |
| **Tracker host**     | **SlimeVR Server**           | Receives trackers; body solve; engine bridge.     | PC     |
| **Face streamer**    | Live Link Face / OSC app     | Sends ARKit blendshapes (and optional head pose). | iPhone |
| **Engine**           | Unreal / Unity / Blender     | Apply quats; drive facial shapes; record/export.  | PC     |

---

## F. Tools, Consumables, and Printables

| Category            | Items                                                                    |
| ------------------- | ------------------------------------------------------------------------ |
| **Hand tools**      | Small screwdrivers, pliers, side-cutters, tweezers.                      |
| **Light soldering** | Fine-tip iron, 63/37 solder, flux pen, heat-shrink.                      |
| **3D printing**     | **PETG/ABS**; SlimeVR housing STLs; M2 brass inserts (optional).         |
| **Adhesives**       | Hot glue (strain relief), foam tape for pads.                            |
| **Wiring**          | JST-PH pigtails, silicone wire 26–28 AWG, Velcro/elastic strap material. |
| **Safety**          | LiPo-safe charging habits; (optional) fire-retardant pouch.              |

---

## G. Optional: Prop Nodes (orientation-only)

> Not required for the current build. Add later only if you want **prop rotation** (still no position).

| Item              | Purpose         | Notes                                         | Qty (example) |
| ----------------- | --------------- | --------------------------------------------- | ------------: |
| **Prop IMU node** | Prop rotation   | Same as body node (BNO085 + ESP32-S3 + LiPo). |             4 |
| **Prop mount**    | Rigid on prop   | Small printed case + clamp; mark **FWD/UP**.  |             4 |
| **Firmware IDs**  | Routing clarity | Use high IDs (e.g., 100–103).                 |             — |

---

## H. Quick Ordering Checklist

```text
[ELECTRONICS – BODY NODES ×10]
- BNO085/BNO080 IMU boards (10)
- ESP32-S3 dev boards, USB-C, LiPo charge preferred (10)
- LiPo 3.7 V 750–1000 mAh, JST-PH (10)
- Mini slide power switches (10)
- JST-PH pigtails + short SPI/I²C wiring sets
- M2 standoffs/screws

[MECHANICAL / WEARABLES]
- 3D-printed PETG/ABS cases (10) with strap slots + UP/FWD arrows
- Elastic/Velcro straps (hips, chest, head, upper arms L/R, forearms L/R, feet L/R)
- Thin rubber/foam pads (comfort)

[SHARED / INFRASTRUCTURE]
- Wi-Fi router (dedicated 5 GHz SSID)
- Multi-port USB-C charger (6–12 ports) + short USB-C cables
- Ethernet cable (PC ↔ router)
- Labels/ID set; storage bins
- Spare LiPos (2–4)

[ARKIT FACE]
- iPhone with TrueDepth (1)
- Face capture app (Live Link Face or OSC) (1)
- Tripod/phone clamp (1)

[SOFTWARE – PC]
- SlimeVR Server
- SlimeVR Tracker Firmware + PlatformIO/Arduino + USB drivers
- Engine (Unreal/Unity/Blender) + any OSC/Live Link bridges

[TOOLS & CONSUMABLES]
- Fine-tip soldering iron + solder/flux; heat-shrink
- Small hand tools (drivers, cutters, tweezers)
- PETG/ABS filament for prints
- Hot glue, Velcro, silicone wire
```

---

**Notes that matter**

* Keep **mounts rigid**; mark **UP/FWD** on every case; wear them the same way every session.
* Use **5 GHz** dedicated Wi-Fi and **wire the PC**.
* Warm up nodes 1–2 min; **T-pose alignment** every session; **magnetometer OFF** indoors.
