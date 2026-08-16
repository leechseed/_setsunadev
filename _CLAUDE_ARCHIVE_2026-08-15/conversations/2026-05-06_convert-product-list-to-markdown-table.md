---
title: "Convert product list to markdown table"
uuid: b663ea31-1dbe-478f-b82f-a54b5875d302
created: 2026-05-06
updated: 2026-05-06
trunk: OTHER
messages: 2
chars: 1228
artifacts: 0
generated_files: 0
tools: []
source: claude.ai-export-2026-08-15
---

# Convert product list to markdown table

> **Conversation Overview**

The person shared shopping cart data from what appears to be an adult novelty retailer and asked Claude to convert it into the simplest possible markdown-compatible table. Claude reformatted the raw product listing data — which included product names, sizes, firmness options, colors, add-ons, and prices — into a clean markdown table with abbreviated fields where appropriate (e.g., "Extra Large" → "XL") and added a calculated totals row at the bottom. The task was completed in a single exchange with no corrections or follow-up requests.

---
## 🧑 Papi  <sub>2026-05-06 01:47:54</sub>

Can you turn this into the simplest table possible? With the following data? I wanna be able to paste it into a markdown. Chance the Unflared Stallion®
Size: Extra Large / Firmness: Medium
Color: Chance's Natural
Suction cup added
$220.00
Quantity: 1
Remove
Taurion the Minotaur®
Size: Medium / Firmness: Soft Shaft, Firm Base
Color: Taurion's Signature
$160.00
Quantity: 1
Remove
Vector® the Cyber-Unicorn
Size: Extra Large / Firmness: Medium
Color: Vector's Natural
Dragon Mount™ added
$220.00
Quantity: 1
Remove
Ika® the Tentacle
Size: Extra Large / Firmness: Medium
Color: Ika's Signature
Suction cup added
$240.00
Quantity: 1

---

## 🤖 Claude  <sub>2026-05-06 01:47:59</sub>

| Product | Size | Firmness | Color | Add-On | Price | Qty |
|---|---|---|---|---|---|---|
| Chance the Unflared Stallion® | XL | Medium | Chance's Natural | Suction cup | $220.00 | 1 |
| Taurion the Minotaur® | Medium | Soft Shaft, Firm Base | Taurion's Signature | — | $160.00 | 1 |
| Vector® the Cyber-Unicorn | XL | Medium | Vector's Natural | Dragon Mount™ | $220.00 | 1 |
| Ika® the Tentacle | XL | Medium | Ika's Signature | Suction cup | $240.00 | 1 |
| **Total** | | | | | **$840.00** | **4** |