---
title: "APY calculator for $5000 at 3.5%"
uuid: bca6e5ad-cd35-43f8-8836-d9f42d9a822f
created: 2026-05-15
updated: 2026-05-15
trunk: BLACK
messages: 6
chars: 1990
artifacts: 0
generated_files: 0
tools: []
source: claude.ai-export-2026-08-15
---

# APY calculator for $5000 at 3.5%

> **Conversation Overview**

The person asked Claude to calculate compound growth using APY, starting with one principal amount and then requesting the same breakdown for a doubled amount. Claude provided multi-year projections (1, 2, 5, and 10 years) for both scenarios using the standard APY formula, and noted the linear scaling relationship between the two calculations. Claude also offered to build an interactive calculator artifact, though the person did not take up that offer.

The conversation concluded with the person asking a question about FDIC insurance coverage limits, referencing an incorrect threshold. Claude corrected the misunderstanding, clarifying the actual standard FDIC coverage limit per depositor per insured institution, and explained strategies for maintaining full coverage when balances grow — including spreading funds across multiple FDIC-insured banks or using different ownership categories at the same bank. Claude asked a clarifying follow-up to determine whether the person had a specific account type in mind or had simply misstated the coverage figure.

---
## 🧑 Papi  <sub>2026-05-15 04:14:33</sub>

apy calculator for $5000 at a 3.5% apy

---

## 🤖 Claude  <sub>2026-05-15 04:14:46</sub>

So the calculation is straightforward—$5,000 at 3.5% APY gives $175 in interest after a year. The user asked for a "calculator" though, which suggests they might want an interactive tool rather than just the math, so I should build a quick artifact they can use.At 3.5% APY on $5,000:

- 1 year: $5,175.00 (+$175)
- 2 years: $5,356.25 (+$356.25)
- 5 years: $5,938.43 (+$938.43)
- 10 years: $7,052.99 (+$2,052.99)

APY already bakes in compounding, so the math is just $5,000 × (1.035)ⁿ where n is years. Want me to build an interactive calculator artifact you can plug different numbers into?

---

## 🧑 Papi  <sub>2026-05-15 04:15:40</sub>

what about 10k

---

## 🤖 Claude  <sub>2026-05-15 04:15:42</sub>

At 3.5% APY on $10,000:

- 1 year: $10,350.00 (+$350)
- 2 years: $10,712.25 (+$712.25)
- 5 years: $11,876.86 (+$1,876.86)
- 10 years: $14,105.99 (+$4,105.99)

Double the principal, double the interest — scales linearly. Want me to spin up that interactive calculator?

---

## 🧑 Papi  <sub>2026-05-15 04:17:15</sub>

if i'm insured up to 10k by fdic, would i want to open up an account if i go over

---

## 🤖 Claude  <sub>2026-05-15 04:17:20</sub>

Quick correction — standard FDIC insurance is $250,000 per depositor, per insured bank, per ownership category, not $10,000. So unless you're working with a different number for a specific reason, you've got a lot more headroom than you think.

That said, the general principle holds: if you ever exceed your FDIC coverage limit at one bank, yes, opening an account at a *different* FDIC-insured bank is the standard move. Each bank gives you a fresh $250K of coverage. You can also get more coverage at the same bank by using different ownership categories (individual, joint, trust, retirement).

Were you thinking of a specific account type with a $10K cap, or did you have the FDIC number wrong?