---
title: "NVMe BIOS update BSOD fix"
uuid: 143db29e-54eb-40cd-86f1-443d629751aa
created: 2026-03-21
updated: 2026-03-21
trunk: BLACK
messages: 6
chars: 5776
artifacts: 0
generated_files: 0
tools: []
source: claude.ai-export-2026-08-15
---

# NVMe BIOS update BSOD fix

> **Conversation Overview**

The person was troubleshooting a Blue Screen of Death (BSOD) error code 0xC000000E ("a required device isn't connected or can't be accessed") that occurred after updating their Windows BIOS. They suspected the issue was related to their NVMe drive and noted they had encountered this problem before. Their motherboard is an ASUS ROG Maximus VII or VIII (Z97/Z170 era).

Claude walked through the likely causes — storage controller mode reset (AHCI vs. IDE), CSM re-enabling after flash, and boot order changes — and provided specific navigation instructions for the ASUS ROG BIOS interface, including using F7 to enter Advanced Mode and checking Advanced → PCH Storage Configuration for SATA Mode, Boot → CSM settings, and Boot → Boot Option Priorities. The person confirmed there was only one boot option visible (Windows Boot Manager) and it was not functioning correctly, but then indicated mid-conversation that they may have identified a fix on their own. The conversation ended before they confirmed the outcome.

---
## 🧑 Papi  <sub>2026-03-21 05:43:51</sub>

I just updated my Windows BIOS, and it's giving me BSD error code 0 x-ray Charlie 0 0e don't know that's many zeros, but that's the recovery that's the code. I've had this problem before. I think it had something to do with my NVMe. I I just I just know I've I'm not too I've done this I've done this before.

---

## 🤖 Claude  <sub>2026-03-21 05:44:19</sub>

The user is describing a Blue Screen of Death (BSOD) error code. They're saying "0x-ray Charlie 0 0e" which sounds like they're spelling it out phonetically - "x-ray" = X, "Charlie" = C, so the code is 0xC00E... but that doesn't quite make sense. 

Actually, thinking about it more - "0 x-ray Charlie 0 0e" - they might mean 0xC000E... or perhaps it's **0xC0000034** or similar. But the most common BSOD after a BIOS update related to NVMe is **0xC0000034** (Windows Boot Manager error) or possibly **INACCESSIBLE_BOOT_DEVICE (0x0000007B)**.


Let me decode this more carefully - the phonetic spelling gives me 0xC000E, which could be **0xC000000E** (DEVICE_NOT_ACCESSIBLE), **0xC0000034** (OBJECT_NOT_FOUND), or **0x0000007B** (INACCESSIBLE_BOOT_DEVICE) - all of which are common after BIOS updates that affect NVMe boot configuration.

The practical troubleshooting steps are to check the BIOS storage controller settings, verify the NVMe mode hasn't switched between AHCI and NVMe/RST, confirm SATA mode is correct, and check if the boot order got reset.Sounds like **0xC000000E** — "A required device isn't connected or can't be accessed." This is one of the most common BSODs after a BIOS update, and your NVMe instinct is almost certainly right.

Here's what likely happened and how to fix it:

---

## What Caused It

When you flash a BIOS, it can **reset storage controller settings to defaults**. The most common culprits:

- **NVMe/AHCI mode got toggled** — BIOS reset the storage mode and now Windows can't find its boot drive
- **Secure Boot or CSM settings changed** — can block the bootloader from seeing the drive
- **Boot order got shuffled** — the system is trying to boot from the wrong device

---

## Fix Steps

### Step 1 — Get Back Into BIOS
Boot into BIOS setup (usually DEL or F2 on POST).

### Step 2 — Check Storage Settings
Look for something like:
- **SATA Mode / NVMe Mode** → Should be **AHCI** (not IDE, not RAID unless you had RAID before)
- Some boards have a separate **PCIe/NVMe config** — make sure it's not set to Legacy

### Step 3 — Check CSM / Secure Boot
- If your Windows install is **GPT/UEFI** (almost certainly is if it's modern), make sure **CSM is disabled** and **Secure Boot is on or at least not misconfigured**
- BIOS resets often re-enable CSM which breaks UEFI boot

### Step 4 — Check Boot Order
Make sure your NVMe SSD is listed as the **first boot device**, not a USB, optical drive, or network boot

### Step 5 — Save & Reboot
Save changes (usually F10), reboot, and see if Windows loads.

---

## If That Doesn't Work

If the BIOS settings look correct and it still BSODs, you may need to do a **Windows Startup Repair** from a bootable USB:
1. Boot a Windows 11/10 install USB
2. Choose **Repair your computer → Troubleshoot → Startup Repair**
3. Let it run — it usually fixes the bootloader automatically

---

The AHCI/CSM reset is the #1 cause of this after a BIOS flash. Start there and it'll likely sort itself out.

---

## 🧑 Papi  <sub>2026-03-21 05:46:29</sub>

Okay. I have an ROG Maximus 8 or 7 motherboard BIOS setup, if that helps.

---

## 🤖 Claude  <sub>2026-03-21 05:46:48</sub>

ROG Maximus Z790/Z890 or older? "Maximus 8 or 7" - these are older boards. Maximus VII and VIII are Z97 and Z170 chipset boards from around 2014-2015. The BIOS UI is ASUS UEFI, the ROG version. Let me give specific navigation guidance for that board's BIOS.Good info. The **ROG Maximus VII or VIII** (Z97/Z170 era) uses the **ASUS UEFI BIOS** with the ROG skin. Here's exactly where to look:

---

## ASUS ROG BIOS Navigation

When you boot into BIOS (DEL on POST), you'll land on the **EZ Mode** screen. You want **Advanced Mode** — press **F7** to switch.

---

### Check 1 — Storage Mode (Most Likely Culprit)
**Advanced → PCH Storage Configuration**
- Look for **"SATA Mode Selection"** → should be **AHCI**
- If it got reset to **IDE**, that's your problem right there

For the NVMe specifically on those boards, also check:
**Advanced → NVMe Configuration** (if present) — just make sure the drive is detected there

---

### Check 2 — CSM (Second Most Likely)
**Boot → CSM (Compatibility Support Module)**
- **Launch CSM** should be **Disabled** if you're running a modern UEFI Windows install
- If it got re-enabled after the flash, it can break the bootloader

---

### Check 3 — Boot Order
**Boot → Boot Option Priorities**
- **Boot Option #1** should be your NVMe/SSD, not a USB or "Windows Boot Manager" pointing nowhere

---

### Check 4 — Secure Boot
**Boot → Secure Boot**
- For most setups just leave it as-is, but if it got toggled it can cause issues

---

## Quick Tip for That BIOS

After a flash, ASUS sometimes prompts you to **load optimized defaults** — if you did that, it likely reset AHCI to IDE. That SATA Mode setting is almost certainly what broke it.

Fix that first, save with **F10**, and you should be back in Windows.

---

## 🧑 Papi  <sub>2026-03-21 06:02:23</sub>

Okay. So there's only one boot option, and that's, the goddamn what do you call it, boot manager or whatever. It's not really working. But hold on. I think I am hold on. I think I figured

---

## 🤖 Claude  <sub>2026-03-21 06:02:30</sub>

The user seems to be in the middle of troubleshooting and thinks they may have figured something out. I'll wait for them to finish their thought.Take your time, I'm right here. 👍