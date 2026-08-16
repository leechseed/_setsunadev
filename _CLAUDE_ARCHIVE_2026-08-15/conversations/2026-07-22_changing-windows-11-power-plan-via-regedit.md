---
title: "Changing Windows 11 power plan via regedit"
uuid: 4f79a36b-1c86-4a83-85e8-96c5db9d0dc9
created: 2026-07-22
updated: 2026-07-22
trunk: BLACK
messages: 6
chars: 9733
artifacts: 0
generated_files: 0
tools: []
source: claude.ai-export-2026-08-15
---

# Changing Windows 11 power plan via regedit

> **Conversation Overview**

The person sought help changing their Windows 11 power plan to Ultimate Performance on a desktop PC, starting from the registry path `Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Power\User\PowerSchemes`. Claude explained that the `ActivePowerScheme` registry value controls the active plan but recommended using elevated Command Prompt with `powercfg` commands instead of direct registry editing for reliable, immediate results.

Claude walked the person through unlocking the hidden Ultimate Performance plan using `powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61`, then activating it with `powercfg /setactive`, and verifying with `powercfg /getactivescheme`. Claude also provided standard GUIDs for Balanced, High Performance, and Power Saver plans for reference, and explained the distinction between power plans and the power mode overlay system used on modern standby laptops (noted as not relevant for their desktop).

When the person shared their `powercfg /list` output, it revealed they had two duplicate Ultimate Performance entries (GUIDs `f0c997af-a408-4fac-a903-50c1c66f573f` and `fdeeafbd-16a3-4c28-b681-ae15203dda79`), with their current active plan being a vendor-created "GameTurbo (High Performance)" plan (GUID `01e7d7b7-f37c-4307-8406-e50b005b90be`), indicating OEM software such as MSI Center. Claude provided specific commands to activate one Ultimate Performance GUID and delete the duplicate, and flagged that OEM gaming software actively managing power plans may silently revert the selection on reboot or game launch, requiring the person to disable auto power plan management within that software. Claude also noted that GameTurbo and Ultimate Performance would yield minimal real-world performance differences.

---
## 🧑 Papi  <sub>2026-07-22 04:38:13</sub>

what regedit value do i need to change to  change the powerplan in windows 11? i'm here rn Computer\HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Power\User\PowerSchemes

---

## 🤖 Claude  <sub>2026-07-22 04:38:41</sub>

The user is asking about modifying Windows 11 power plans through the registry. I'm recalling that power schemes are stored as GUIDs in the registry path they've navigated to, with each power plan having its own subkey under that location.

The key value to modify is `ActivePowerScheme`, which is a string value containing the GUID of the currently active power plan. I'm thinking through the standard GUIDs for common power plans like Balanced, High Performance, and Power Saver, along with the less common Ultimate Performance option. To change the active plan, you'd replace the GUID in that `ActivePowerScheme` value with the GUID of whichever plan you want to activate.

There's an important caveat though—directly editing the registry value often doesn't work reliably because the power service caches these settings. The proper approach is using the `powercfg /setactive` command from an elevated command prompt instead, which ensures the change takes effect correctly.

On Windows 11, there's an additional layer of complexity with modern standby systems. Windows 11 uses power mode overlays on top of the base power plan, stored in separate registry values like `ActiveOverlayAcPowerScheme` and `ActiveOverlayDcPowerScheme`. These overlay GUIDs represent the power mode slider you see in Settings—Best Power Efficiency, Balanced, and Best Performance. So on modern Windows 11 laptops, what users interact with as the power mode slider is actually these overlay values, while the underlying power plan is still controlled by `ActivePowerScheme`. If someone wants to change the actual power plan versus just the power mode overlay, they need to know which registry value they're targeting. I'll point them to the `ActivePowerScheme` value in that registry key and explain that they can set it to the GUID of whichever power plan they want, but emphasize that powercfg /setactive is the proper way to actually apply the change immediately rather than editing the registry directly.You're in the right spot. The value you want is `ActivePowerScheme` — a string (REG_SZ) value directly in that `PowerSchemes` key. It holds the GUID of the currently active plan. The subkeys listed under `PowerSchemes` are the plans installed on your system, so you can copy the GUID of whichever one you want and paste it into `ActivePowerScheme`.

Standard GUIDs for reference:

- Balanced: `381b4222-f694-41f0-9685-ff5bb260df2e`
- High performance: `8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c`
- Power saver: `a1841308-3541-4fab-bc81-f71556f20b4a`

Two caveats worth knowing. First, editing that value directly doesn't reliably apply the change live — Windows caches the active scheme, so you'd typically need a reboot or a restart of the power service. The cleaner way is an elevated command prompt with `powercfg /setactive <GUID>`, which applies instantly (and `powercfg /list` shows every installed plan with its GUID, saving you the registry dig).

Second, if this is a modern standby laptop on Windows 11, the "power mode" slider in Settings isn't the power plan at all — it's an overlay stored in that same key as `ActiveOverlayAcPowerScheme` and `ActiveOverlayDcPowerScheme` (best efficiency is `961cc777-...`, best performance is `ded574b5-...`, and all zeros means the default balanced overlay). So if changing `ActivePowerScheme` doesn't seem to do what you expect, that's probably why.

What are you trying to switch to?

---

## 🧑 Papi  <sub>2026-07-22 04:39:38</sub>

im on a pc desktop. guide me to this. i want to change to the ultimate power plan if possible or whatever allows me to take advantage of my specs

The cleaner way is an elevated command prompt with `powercfg /setactive <GUID>`, which applies instantly (and `powercfg /list` shows every installed plan with its GUID, saving you the registry dig).

---

## 🤖 Claude  <sub>2026-07-22 04:40:02</sub>

The user wants to switch to Ultimate Performance mode on their desktop, so I need to walk them through using powercfg since that plan is typically hidden by default on Windows 11. I'll explain that they need to duplicate the Ultimate Performance scheme first using its GUID, then activate it.

The process involves opening an elevated command prompt, listing current power plans, duplicating the Ultimate Performance scheme (which generates a new GUID), and then setting that new GUID as active. I should mention they can verify the change afterward, and note that while Ultimate Performance sounds impressive, the real-world performance gain over High Performance on a desktop is pretty minimal since it mainly just disables some power-saving features. Writing the command steps...Ultimate Performance is hidden by default on Windows 11, but unlocking it takes one command. Here's the full sequence:

**1. Open an elevated terminal** — right-click the Start button → **Terminal (Admin)** → accept the UAC prompt.

**2. Check what's installed:**
```
powercfg /list
```
If "Ultimate Performance" already appears, copy its GUID and skip to step 4.

**3. Unlock the Ultimate Performance plan:**
```
powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61
```
This creates a visible copy of the hidden plan and prints its **new GUID** in the output. Copy that GUID (the duplicate gets its own — don't reuse the one above).

**4. Activate it:**
```
powercfg /setactive <paste-the-new-GUID-here>
```

**5. Confirm:**
```
powercfg /getactivescheme
```
It should report Ultimate Performance as active. It'll also now show up in Control Panel → Power Options if you ever want to switch back by clicking instead.

A quick honesty note on what you're actually getting: Ultimate Performance locks minimum processor state at 100%, disables core parking, and strips out the micro-latencies from power state transitions. On a desktop that's all upside except slightly higher idle power draw and heat. Just keep expectations calibrated — versus High Performance the difference is small, and on a modern CPU versus Balanced you're mostly buying snappier frequency response rather than raw FPS gains. It costs nothing to run, though, so for a gaming desktop it's a reasonable default.

One side effect: with this plan active, the power mode slider in Settings → System → Power goes inert — that slider only functions on Balanced. Everything lives in Control Panel → Power Options from here on.

---

## 🧑 Papi  <sub>2026-07-22 04:40:43</sub>

Power Scheme GUID: 01e7d7b7-f37c-4307-8406-e50b005b90be  (GameTurbo (High Performance)) *
Power Scheme GUID: 381b4222-f694-41f0-9685-ff5bb260df2e  (Balanced)
Power Scheme GUID: 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c  (High performance)
Power Scheme GUID: 9fb9c30d-9dab-496d-a421-56f015dfab66  (My Custom Plan 1)
Power Scheme GUID: a1841308-3541-4fab-bc81-f71556f20b4a  (Power saver)
Power Scheme GUID: f0c997af-a408-4fac-a903-50c1c66f573f  (Ultimate Performance)
Power Scheme GUID: fdeeafbd-16a3-4c28-b681-ae15203dda79  (Ultimate Performance)

---

## 🤖 Claude  <sub>2026-07-22 04:41:05</sub>

Looking at the user's power plan output, I can see they have GameTurbo (High Performance) currently active — that's an OEM plan, likely from MSI or a similar manufacturer that bundles custom power management tools with their systems.

The key issue is they've got two duplicate Ultimate Performance plans with different GUIDs, which probably happened from running the duplication command twice or having one pre-exist. I should recommend activating one of them with `powercfg /setactive` and then cleaning up the duplicate with `powercfg /delete`, followed by a verification check to confirm the switch worked.

But there's an important caveat: if MSI Center (or whatever OEM software created GameTurbo) is actively managing power plans through its user scenario feature, it might automatically switch back to GameTurbo regardless of what they set. They may need to disable that scenario management in MSI Center or switch it to a manual/customize mode to prevent the override. I should keep this concise and conversational, sticking with code blocks for the commands and a few short paragraphs to explain what's happening and note that OEM software like MSI Center might automatically revert the power plan.You ended up with two copies of Ultimate Performance (the duplicate command ran twice, or one was already there). They're identical, so just pick one and activate it:

```
powercfg /setactive f0c997af-a408-4fac-a903-50c1c66f573f
```

Then clean up the extra copy so the list stays tidy:

```
powercfg /delete fdeeafbd-16a3-4c28-b681-ae15203dda79
```

And confirm:

```
powercfg /getactivescheme
```

One thing worth flagging: the asterisk in your list shows you're currently on **GameTurbo (High Performance)**, which isn't a stock Windows plan — that's created by OEM gaming software, most likely MSI Center if this is an MSI board. That kind of software often actively manages the power plan and may silently switch you back to GameTurbo on reboot or when a game launches. If you run the verify command later and find GameTurbo active again, that's what happened — you'd need to open the MSI Center (or equivalent) settings and disable its user scenario / auto power plan feature so your choice sticks.

Also worth saying: GameTurbo is itself a high-performance profile the vendor tuned for this exact purpose, so the real-world difference between it and Ultimate Performance will be minimal. Nothing wrong with running Ultimate — just don't expect a dramatic jump.