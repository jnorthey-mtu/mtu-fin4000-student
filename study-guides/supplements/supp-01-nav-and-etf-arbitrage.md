# Supplement 1: NAV and ETF Arbitrage

*Worked Examples from SEC Filings (BKM Ch. 4)*

[← All study guides](../../study-guide-index.md)

*Big picture: this supplement pairs BKM's conceptual coverage of mutual funds, ETFs, and fund structures with real numbers pulled from SEC EDGAR filings and a from-scratch derivation of why in-kind redemptions escape capital gains tax — so you leave with the formula, a worked example, and the actual statute behind it.*

**Source context:** Companion to the slide deck "NAV and ETF Arbitrage — Ch4 Supplement" (Michigan Tech template). Slide references below are to that deck, not the publisher's chapter lecture slides. BKM section references are to *Investments*, 13th Edition, Chapter 4 (*Mutual Funds and Other Investment Companies*).

---

## What This Supplement Adds

No official numbered learning objectives exist for this material — it is enrichment built on top of BKM Chapter 4, not a textbook section in its own right. By the end of it you should be able to:

- Apply the NAV formula to real fund filings, not textbook placeholders.
- Explain why ETF prices track NAV as tightly as they do, and work the arbitrage math on both sides — creation and redemption.
- Identify which market participants can actually run that arbitrage, and which can't.
- Trace the tax treatment of in-kind redemptions back to its actual statutory source.

---

## 1. Fund Structures & Fees *(Supplement Slide 4)* — BKM §4.2, §4.4

- **Open-end funds** continuously issue/redeem shares at NAV; **closed-end funds** have a fixed share count and trade at a market price that can drift from NAV, with no redemption channel to correct it.
- Three sales-load structures: **no-load** (no sales charge), **front-end load** (charged at purchase), **back-end load / CDSC** (charged at redemption, typically shrinking the longer you hold).

## 2. Finding Fund Data: SEC EDGAR *(Supplement Slide 5)* — supports BKM §4.1, §4.8

- EDGAR is the SEC's free public filing system — the primary source every other data provider (Morningstar, Bloomberg) ultimately draws from.
- Four-step path: sec.gov/edgar → search by company/fund/ticker → pick the filing type (10-K, N-CSR, N-CSRS) → open it. Every number in the detail sections below came from exactly this path.

## 3. The Mutual Fund Industry's Growth & Morningstar *(Supplement Slide 6)* — BKM §4.8

- Industry assets grew from under \$1 billion (1945) to over \$200 billion (1984, Morningstar's founding year) to **\$31 trillion+** in mutual funds alone today.
- Morningstar's 1985 star rating and 1992 Style Box gave investors their first standardized way to compare funds — still the industry's standard reference, which is why BKM itself lists morningstar.com in §4.8.

## 4. Calculating NAV — Formula & Real Filings *(Supplement Slides 7–10)* — BKM §4.1

- NAV = (Total Assets − Total Liabilities) ÷ Shares Outstanding — see Key Equations. Published "net assets" figures are already assets minus liabilities; the full gross breakdown only shows up in a fund's SEC shareholder report.
- Summary comparison across three real funds — **VFIAX, FCNTX, AGTHX** — net assets, NAV, and implied shares outstanding.
- Full Statement of Assets and Liabilities pulled directly from **AGTHX's** and **VFIAX's** actual N-CSR filings, with every line item reconciling to the published NAV.

## 5. How ETFs Trade *(Supplement Slides 12–14)* — BKM §4.6

- Mutual funds price once a day at NAV ("forward pricing"); ETFs trade continuously all day like a stock — which is also why they carry intraday volatility and bid-ask spread costs mutual fund investors don't.
- **Secondary market** (investors trading existing shares) vs. **primary market** (Authorized Participants creating/redeeming "creation units" directly with the fund) — only the primary market can actually force price back to NAV.
- The full arbitrage mechanism, step by step: secondary-market price drift → AP steps in → creation or redemption → fund issues/cancels creation units.

## 6. The Arbitrage Mechanism in Numbers *(Supplement Slides 15–16)* — BKM §4.6

- **Worked creation example:** ETF at a \$100.40 premium to \$100 NAV — AP buys the \$5,000,000 basket, delivers it for 50,000 new shares, sells them at market for a **\$20,000 gross profit**; new supply pushes price back down.
- **Worked redemption example:** same ETF at a \$99.60 discount — AP buys 50,000 shares, redeems for the basket, sells the basket for the same **\$20,000 gross profit**; reduced supply pushes price back up.

## 7. Who Can Arbitrage? APs vs. Non-APs *(Supplement Slide 17)* — BKM §4.6, extension

- Direct creation/redemption is legally restricted to registered **Authorized Participants** — a firm granted that access is an AP by definition.
- Non-AP firms can still arbitrage the secondary market (trade the ETF against the basket, bet on convergence) or route through an actual AP as agent — just with more risk, since nothing forces convergence.

## 8. Tax Treatment of In-Kind Redemptions *(Supplement Slides 18–19)* — BKM §4.5

- In-kind redemption is why ETFs avoid distributing capital gains the way mutual funds can be forced to when meeting net redemptions.
- The actual mechanism: **IRC §311(b)** is the default rule (distributing appreciated property triggers gain as if sold); **IRC §852(b)(6)** is the specific override for regulated investment companies redeeming stock that's redeemable on demand — which is also exactly why this protection doesn't extend to closed-end funds.

---

## Key Terms

*Make sure you can define each of these in your own words.*

- [ ] net asset value (NAV)
- [ ] open-end fund
- [ ] closed-end fund
- [ ] no-load fund
- [ ] front-end load
- [ ] back-end load (CDSC)
- [ ] SEC EDGAR
- [ ] Form N-CSR / N-CSRS
- [ ] Statement of Assets and Liabilities
- [ ] forward pricing
- [ ] Authorized Participant (AP)
- [ ] creation unit
- [ ] primary market
- [ ] secondary market
- [ ] creation
- [ ] redemption
- [ ] in-kind redemption
- [ ] carryover basis
- [ ] regulated investment company (RIC)
- [ ] IRC §311(b)
- [ ] IRC §852(b)(6)

---

## Key Equations

**Net asset value (NAV)**

```math
\text{NAV} = \frac{\text{Total Assets} - \text{Total Liabilities}}{\text{Shares Outstanding}}
```

Fact sheets report "net assets" — that's already Assets − Liabilities. The full gross breakdown only appears in a fund's SEC shareholder report (Form N-CSR / N-CSRS).

**Gross arbitrage profit (creation / redemption)**

```math
\text{Gross Profit} = \left|\,\text{Market Price} - \text{NAV}\,\right| \times \text{Creation Unit Shares}
```

Profit scales with both the size of the mispricing and the creation unit size. In the worked examples, a \$0.40 (0.4%) gap on a 50,000-share unit produced \$20,000 gross profit before trading costs and the fund's own transaction fee.

---

*Study guide for the "NAV and ETF Arbitrage — Ch4 Supplement" slide deck. Slide references are to that deck, not the standard chapter lecture slides. BKM section references are to Investments, 13th Edition, Chapter 4 (Mutual Funds and Other Investment Companies).*
