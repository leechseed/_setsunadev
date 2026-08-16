---
title: "Choosing the right UPS for gaming"
uuid: bad0b36d-478d-4bd5-9e4b-3f7b1f24124e
created: 2026-04-10
updated: 2026-04-10
trunk: BLACK
messages: 6
chars: 10021
artifacts: 0
generated_files: 0
tools: []
source: claude.ai-export-2026-08-15
---

# Choosing the right UPS for gaming

> **Conversation Overview**

The person is selecting an uninterruptible power supply (UPS) for a high-end gaming PC setup and sought guidance on how to choose the right unit. The conversation covered three main topics: the principles of UPS selection (load calculation, sizing methodology, and topology types), how to identify hardware components using software tools and physical inspection, and finally a specific UPS recommendation based on the person's actual system specs.

The person's gaming PC (named "LEECHSEED") runs an Intel Core i9-10900K, NVIDIA GeForce RTX 3090 (EVGA), ASUS ROG MAXIMUS XII EXTREME motherboard, 64GB Corsair DDR4 RAM, and a Corsair RM850x 850W PSU across a substantial drive array (seven drives total including NVMe, SATA SSD, and a large external HDD). Claude walked the person through using HWiNFO64 to identify GPU, CPU, motherboard, and monitor details, and explained that PSU identification requires either physical inspection of the unit's label or checking purchase records, since no software can detect PSU model or wattage.

With the full system specs in hand, Claude calculated a realistic sustained gaming load of 550–700W with transient spikes potentially reaching 800–900W, driven largely by the RTX 3090's known power spike behavior. Claude flagged that standard 1500VA UPS units (rated ~900–1000W) are undersized for this rig and recommended stepping up to units in the 1500W+ class with pure sine wave output and line-interactive topology—specifically the CyberPower CP2200AVRLCD as a value pick or the APC Smart-UPS SMT2200C as a premium option. The conversation ended with Claude requesting monitor count and specifications, and the person's preferred runtime goal, to finalize the recommendation.

---
## 🧑 Papi  <sub>2026-04-10 01:33:32</sub>

Okay. How do I pick the best uninterrupted power supply for my gaming setup and just what I'm doing.

---

## 🤖 Claude  <sub>2026-04-10 01:33:56</sub>

The user is asking for UPS recommendations for gaming, which is straightforward enough to answer without needing current information—the core principles of selecting an uninterruptible power supply haven't changed. I'll focus on the practical factors that matter for their setup.Picking a UPS comes down to three things: how much power your setup draws, how long you need it to run on battery, and what kind of protection you actually need.

**Calculate your load first.** Add up the wattage of everything you want protected: PC (look at your PSU rating, but real draw is usually 40–70% of that under gaming load), monitor(s), modem, router, and maybe a desk lamp. A typical mid-to-high-end gaming PC pulls 300–500W actual under load, monitors add 30–60W each, networking gear is negligible. Don't plug printers, space heaters, or laser anything into a UPS — they spike hard and trip it.

**Then size the UPS.** UPS capacity is rated in VA (volt-amps) and watts. The watt number is what matters. Aim for a UPS whose wattage rating is roughly 1.5–2x your measured load — this gives you headroom and longer runtime. So if your setup pulls ~500W, look at UPS units rated 800–1000W (which is usually 1500VA class).

**Pick the right topology.** This is the part most people miss:
- **Standby (offline)** — cheapest, switches to battery when power drops. Fine for basic protection but the switchover (~4–8ms) can occasionally cause modern PCs with active PFC power supplies to hiccup or shut off anyway. Avoid for gaming PCs.
- **Line-interactive** — the sweet spot for gaming. Regulates voltage without switching to battery on minor sags, faster transfer time, handles brownouts well. This is what you want.
- **Online (double-conversion)** — overkill and expensive for home use. Skip it.

**Runtime expectations.** A 1500VA line-interactive UPS will give a 500W load roughly 5–10 minutes — enough to save your game, shut down cleanly, or ride out a brief blip. If you want to actually keep playing through outages, you need a much bigger unit and your wallet will feel it.

**Practical recommendations in the line-interactive 1500VA class:** CyberPower CP1500PFCLCD or PFCRT, APC BR1500MS2, Eaton 5S1500LCD. The "PFC" or "sine wave" designation matters — your PC's PSU has active PFC and wants a pure sine wave output, not simulated/stepped. Don't cheap out on this; a simulated sine wave UPS can damage or refuse to work with modern PSUs.

**One more thing:** plug only the PC, monitor, and networking into the battery-backed outlets. Most UPS units have a second bank of "surge only" outlets — speakers, chargers, and other non-critical stuff goes there so you're not wasting runtime on them.

If you tell me your PSU wattage and monitor setup I can ballpark a more specific size for you.

---

## 🧑 Papi  <sub>2026-04-10 01:34:45</sub>

Right. How do I find the products, names, of my PSU and my monitors and my GPU and all that shit from my

---

## 🤖 Claude  <sub>2026-04-10 01:35:01</sub>

The user is asking for practical steps to identify hardware components like PSU, GPU, and monitors on a Windows PC. I should walk through the most straightforward methods—checking Device Manager for GPU and monitors, using system information tools for PSU details, and maybe mentioning physical inspection or third-party utilities as fallbacks.Easiest path on Windows — you can get most of this without opening the case.

**GPU, CPU, RAM, motherboard** — install **HWiNFO64** (free, hwinfo.com) or **Speccy**. HWiNFO is the gold standard. Run it, hit "Summary only," and it'll list your CPU, GPU, motherboard model, RAM, and storage in one screen. For just the GPU quickly, you can also right-click the desktop → Display settings → Advanced display, or open Task Manager → Performance tab → GPU.

**Monitors** — HWiNFO will show the monitor model too, but the cleanest way is Windows Settings → System → Display → Advanced display → pick each monitor from the dropdown. It shows the manufacturer and model. If that's vague, the model number is also printed on a sticker on the back of the monitor near the power input.

**PSU — this is the annoying one.** No software can detect your power supply. Windows can't see it, HWiNFO can't see it, nothing can. You have two options:
1. **Check your records** — order history on Amazon/Newegg/wherever you bought the PC or built it, or the build invoice if it was prebuilt.
2. **Look at the sticker** — every PSU has a label on its side with the brand, model, and wattage. In most cases you can read it through the side panel of your case with a flashlight without removing anything. If your PSU is mounted with the label facing down (toward a basement vent), you'll need to pop the side panel off — four thumbscrews on the back of the case, takes 30 seconds.

**If it's a prebuilt** (Dell, HP, Alienware, iBuyPower, etc.) — go to the manufacturer's support site, punch in your service tag or serial number (usually a sticker on the top or back of the case), and it'll pull up the full original spec sheet including PSU wattage.

For UPS sizing the PSU **wattage rating** is what matters most — a 750W PSU means the PC can theoretically pull up to 750W, though under gaming load you're probably actually drawing 50–70% of that.

Once you've got the PSU wattage and monitor models, drop them here and I'll give you a sized recommendation.

---

## 🧑 Papi  <sub>2026-04-10 01:39:22</sub>

ok my power supply says rm850x

Computer:      ASUS 
CPU:           Intel Core i9-10900K (Comet Lake-S, Q0)
               3700 MHz (37.00x100.0) @ 4897 MHz (49.00x100.0)
Motherboard:   ASUS ROG MAXIMUS XII EXTREME
BIOS:          3201, 11/20/2024
Chipset:       Intel Z490 (Comet Lake PCH-H)
Memory:        65536 MBytes DDR4 SDRAM @ 1599 MHz, 16-20-20-38
               - 32768 MB PC25600 DDR4 SDRAM - Corsair CMK64GX4M2E3200C16
               - 32768 MB PC25600 DDR4 SDRAM - Corsair CMK64GX4M2E3200C16
Graphics:      NVIDIA GeForce RTX 3090 (GA102-300) [EVGA]
               NVIDIA GeForce RTX 3090, 24576 MB GDDR6X SDRAM
Drive:         Samsung SSD 860 EVO 1TB, 976.8 GB, Serial ATA 6Gb/s @ 6Gb/s
Drive:         Samsung SSD 860 EVO 1TB, 976.8 GB, Serial ATA 6Gb/s @ 6Gb/s
Drive:         WDC WDS100T2B0C-00PXH0, 976.8 GB, NVMe
Drive:         WDC WDS100T2B0C-00PXH0, 976.8 GB, NVMe
Drive:         WDC WDS200T2B0C-00PXH0, 1953.5 GB, NVMe
Drive:         WD_BLACK  SN750 2TB, 1953.5 GB, NVMe
Drive:         ST12000VN0007-2GS116, 11718.9 GB, Serial ATA 6Gb/s @ 6Gb/s <-> USB
Sound:         Intel Comet Lake PCH-H - cAVS (Audio, Voice, Speech) [A0]
Sound:         NVIDIA GA102 - High Definition Audio Controller
Network:       Intel Wi-Fi 6 AX201 160MHz
Network:       Marvell 10G Ethernet connection
Network:       Intel Ethernet Controller I225-V
OS:            Microsoft Windows 11 Home (x64) Build 26200.8037 (25H2)
Computer Name: LEECHSEED

---

## 🤖 Claude  <sub>2026-04-10 01:39:51</sub>

I'm breaking down the power consumption for their gaming setup—the CPU and GPU are the main draws, with the i9 pulling 125-250W under load and the RTX 3090 hitting 350-450W during gaming, plus another 50-80W for the rest of the system, which puts realistic gaming loads around 550-700W with potential spikes higher.

Given Nvidia's 750W minimum recommendation for the 3090 and those notorious transient spikes, a 1500VA UPS is cutting it close. I'd recommend stepping up to at least a 1500W-class unit like the CyberPower CP1500EPFCLCD or similar, since their system could pull 600-700W sustained with transient spikes exceeding 800W—anything smaller risks the UPS tripping under load.Solid rig. Let me ballpark your load — this matters because the 3090 is notorious for transient power spikes.

**Realistic power draw under gaming load:**
- i9-10900K: ~125–200W (can spike to 250W+ unlocked)
- RTX 3090: ~350W sustained, but **transient spikes up to 450–500W** for milliseconds
- Motherboard + 64GB RAM + your drive army (you've got 7 drives in there): ~60–90W
- **Sustained gaming total: ~550–700W**
- **Peak transients: 800–900W briefly**

Your RM850x (850W Corsair, 80+ Gold, fully modular — great PSU) is appropriately sized for that system, but it tells us the UPS needs real headroom. The 3090's transient spikes are the thing that catches people off guard and trips undersized UPS units into overload.

**What this means for sizing:** the usual "1500VA/900W" recommendation is **too small** for your setup. You want to step up.

**Target: 1500W+ capacity, line-interactive, pure sine wave.** Look at:
- **CyberPower CP1500PFCLCD** — 1000W, 1500VA. This is the *bare minimum* and I'd only suggest it if you have one monitor and aren't doing anything crazy. Tight on headroom for transients.
- **CyberPower CP2200AVRLCD** — ~1320W, much more breathing room. Better match.
- **APC BR1500MS2** — 900W, also too tight for a 3090 rig, skip.
- **APC SMT1500C / SMT2200C (Smart-UPS line)** — pro-grade, pure sine, excellent for your system. The SMT2200C (1980VA / 1980W) would handle your rig plus multiple monitors with generous runtime. More expensive but these are bulletproof.
- **Eaton 5S1500LCD** — 900W, too tight. Their **5PX1500** or **9PX1500** are better fits.

**Honest recommendation for your specific rig:** don't cheap out at the 1500VA tier. Go **CyberPower CP2200AVRLCD** as the value pick, or step up to an **APC Smart-UPS SMT2200C** if you want pro-grade and don't mind the price. Both will handle the 3090's transient spikes without tripping and give you 5–10 minutes of runtime to save and shut down cleanly.

**What to tell me to finalize:** how many monitors, their size/refresh rate (a 4K 144Hz OLED pulls very different wattage than a 1080p 60Hz panel), and whether you want "save and shut down" runtime (~5 min) or "keep playing through short outages" runtime (15+ min, much bigger unit).