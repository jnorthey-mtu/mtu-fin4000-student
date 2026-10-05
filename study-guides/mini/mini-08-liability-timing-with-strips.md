# Mini Study Guide 8: Liability Timing

*Funding Future Cash Needs with STRIPS (BKM Ch. 14 & 16)*

[← All study guides](../../study-guide-index.md)

FIN 4000 Investments · Midterm prep · Sep 28, 2026 · Jim Northey

## Learning objectives

When you know exactly when cash is needed, you can buy a zero-coupon Treasury (a STRIP) maturing on each date. That locks in the funding today with no reinvestment or price risk.

After this guide you should be able to:

1. Explain what Treasury STRIPS are and how they are created.
2. Price the cost of funding a schedule of future liabilities with STRIPS.
3. Build a cash-flow-matched (dedicated) portfolio from a coupon bond plus zeros.
4. Compare cash-flow matching with duration-based immunization.
5. Explain the tax treatment (phantom income) and where STRIPS are best held.

## Core concept

### What STRIPS are

**STRIPS** (Separate Trading of Registered Interest and Principal of Securities) are zero-coupon securities made from Treasury notes and bonds. A dealer splits a Treasury into its separate coupon payments and principal payment. Each piece trades as its own zero-coupon bond.

- A 10-year Treasury with semiannual coupons becomes 21 zeros: 20 coupon STRIPS plus 1 principal STRIP.
- Each STRIP pays one amount on one date, so its price is set by the spot rate for that date: P = Face / (1 + yₜ)ᵗ.
- STRIPS carry U.S. Treasury credit quality.

### Matching liability timing

| Approach | How it works | Rebalancing? | Risks remaining |
| --- | --- | --- | --- |
| **Cash-flow matching (dedication)** | Buy zeros (or bonds) whose cash flows arrive on each liability date in each liability amount | None | Essentially none if Treasuries are used |
| **Immunization** | Match portfolio duration (and PV) to liability duration | Yes, as time passes and rates change | Non-parallel yield curve shifts; rebalancing costs |
| **Unhedged** | Hold any bond portfolio | — | Price risk and reinvestment risk |

A single zero maturing on the liability date is the simplest immunized position: its duration equals the horizon, and it pays exactly the face value no matter what rates do.

**Cost of a dedicated STRIPS portfolio:**

```math
\text{Cost today} = \sum_{t} \frac{L_t}{(1 + y_t)^{t}}
```

**Where:**

- Cost today = amount needed now to buy the dedicated STRIPS portfolio
- Lₜ = liability (cash needed) at time t
- yₜ = STRIP (spot) yield for maturity t, as a decimal
- t = years until each payment is due
- Σ = sum over all liability dates

where Lₜ is the liability due at time t and yₜ is the STRIP (spot) yield for that date.

**Why not always dedicate?** Exact matching can cost more than immunization, and the right maturities may be thin or unavailable for long or irregular liabilities. Many pension funds dedicate the near-term payments and immunize the rest.

### Tax treatment: phantom income

A STRIP pays no cash until maturity. The IRS still taxes its yearly accretion in value as interest (original issue discount). Taxable investors pay tax on income they have not received. STRIPS are therefore best held in tax-deferred accounts: pension funds, IRAs, 401(k)s, and 529 plans.

## Worked examples

### Example 1: Funding four years of tuition (Algorithmic)

A family needs \$50,000 at the end of each of the next 4 years for tuition. STRIP yields (annual compounding) are 4.0%, 4.3%, 4.5%, and 4.7%.

| Year | Liability | STRIP yield | Cost today = L / (1 + y)ᵗ |
| --- | --- | --- | --- |
| 1 | \$50,000 | 4.0% | \$48,076.92 |
| 2 | \$50,000 | 4.3% | \$45,962.26 |
| 3 | \$50,000 | 4.5% | \$43,814.83 |
| 4 | \$50,000 | 4.7% | \$41,608.62 |
| **Total** | **\$200,000** |  | **\$179,462.63** |

For \$179,463 today, all four payments are locked in. Nothing needs to be reinvested, and nothing needs to be sold before its date. A 529 plan avoids the phantom-income tax problem.

**BA II Plus (year 3):** `3` `N` · `4.5` `I/Y` · `0` `PMT` · `50000` `FV` · `CPT` `PV` → −43,814.83

### Example 2: A single liability, and why the zero is immune (Algorithmic)

A firm owes \$1,000,000 in 7 years. The 7-year STRIP yields 5%.

1. Cost = 1,000,000 / 1.05⁷ = **\$710,681.33**.
2. If rates jump to 6% tomorrow, the STRIP's market value falls to \$665,057. The liability's present value falls by the same proportion, and the STRIP still pays \$1,000,000 in year 7.
3. If rates drop to 4%, the market value rises to \$759,918. Again the STRIP still pays exactly \$1,000,000.

The firm is hedged no matter what rates do. With a 7-year-duration coupon bond instead, the firm would have to rebalance as time passes to keep durations matched.

### Example 3: Cash-flow matching with a coupon bond and a zero (Algorithmic)

A pension plan owes \$100,000 in 1 year and \$200,000 in 2 years. It can buy a 2-year, 6% annual-coupon bond at par and a 1-year zero yielding 5%. Work **backward from the last liability**:

1. **Year 2:** the 2-year bond pays face × 1.06 at year 2. Face = 200,000 / 1.06 = **\$188,679.25**.
2. **Year 1:** that bond also pays a coupon of 0.06 × 188,679.25 = \$11,320.75 in year 1. Remaining need = 100,000 − 11,320.75 = \$88,679.25. Buy a 1-year zero with that face value.
3. **Cost:** bond \$188,679.25 (at par) + zero 88,679.25 / 1.05 = \$84,456.43. Total = **\$273,135.68**.

Working backward matters: each longer bond's coupons cover part of the earlier liabilities, which reduces what you must buy for those dates.

## Common pitfalls

- **Discounting every liability at one rate.** Each date has its own spot (STRIP) yield.
- **Matching forward instead of backward.** Start from the last liability, so longer bonds' coupons offset earlier needs.
- **Confusing a STRIP's market value with its payoff.** Its price moves with rates, but the payoff on its maturity date is fixed. For a matched liability, interim price changes do not matter.
- **Forgetting semiannual conventions.** STRIP yields are usually quoted as bond-equivalent yields: price = 100 / (1 + y/2)^(2T).
- **Ignoring phantom income.** Taxable holders owe tax each year on accreted interest.

## Key terms and definitions

- [ ] **Treasury STRIPS:** zero-coupon securities created by separating a Treasury note's or bond's coupon payments and principal.
- [ ] **Coupon STRIPS vs. principal STRIPS:** zeros made from individual coupon payments vs. from the final principal payment.
- [ ] **Spot rate:** the yield on a zero-coupon bond for a given maturity.
- [ ] **Cash-flow matching:** buying securities whose cash flows arrive on each liability date in each liability amount.
- [ ] **Dedication strategy:** another name for cash-flow matching, often applied to the near-term part of a liability schedule.
- [ ] **Immunization:** matching the portfolio's duration and present value to the liability's so that rate changes do not affect funding.
- [ ] **Rebalancing:** adjusting an immunized portfolio as time passes and rates change, to keep durations matched.
- [ ] **Horizon (liability) duration:** the duration of the liabilities to be funded; for a single payment, the time until it is due.
- [ ] **Original issue discount (OID) / phantom income:** the yearly accretion of a zero's value, taxed as interest even though no cash is received.
- [ ] **Tax-deferred account:** an account (pension, IRA, 401(k), 529) in which income is not taxed until withdrawal, if at all.

## CFA-style practice questions

**Q1 [Algorithmic].** A liability of \$250,000 is due in 5 years. The 5-year STRIP yields 4.5% (annual). The cost to fund it today is *closest* to:

- A. \$193,750
- B. \$200,613
- C. \$239,234

**Q2 [Conceptual].** Compared with immunization, a cash-flow matching strategy:

- A. requires more frequent rebalancing.
- B. requires no rebalancing once set up.
- C. is exposed to non-parallel yield curve shifts.

**Q3 [Algorithmic].** Liabilities of \$40,000 are due at the end of years 1 and 2. Spot rates are 4% (1 year) and 5% (2 years). The cost of a dedicated STRIPS portfolio is *closest* to:

- A. \$74,380
- B. \$74,743
- C. \$76,190

**Q4 [Conceptual].** STRIPS are *most* suitable for tax-deferred accounts because:

- A. their interest is tax-exempt.
- B. holders owe tax each year on accreted interest they have not received.
- C. they cannot be held in taxable accounts.

**Q5 [Conceptual].** Buying a zero-coupon Treasury that matures on a liability's due date eliminates:

- A. price risk only.
- B. reinvestment risk only.
- C. both price risk and reinvestment risk for that liability.

**Q6 [Algorithmic].** A plan owes \$50,000 in 1 year and \$100,000 in 2 years. It matches the year-2 liability with a 2-year, 5% annual-coupon bond. The face value of the 1-year zero it also needs is *closest* to:

- A. \$45,238
- B. \$47,619
- C. \$50,000

**Q7 [Conceptual].** The *main* drawback of full cash-flow matching for a large pension plan is:

- A. it leaves the plan exposed to reinvestment risk.
- B. it can be costly or impossible when suitable maturities are scarce.
- C. its duration drifts away from the liabilities over time.

**Q8 [Algorithmic].** A 10-year principal STRIP is quoted at a 4.2% bond-equivalent yield. Its price per \$100 of face value is *closest* to:

- A. \$65.99
- B. \$66.27
- C. \$95.97

## Answer key

| Q | Answer | Explanation |
| --- | --- | --- |
| 1 | B | 250,000 / 1.045⁵ = \$200,613. A uses simple interest; C discounts for one year only. |
| 2 | B | Matched cash flows pay the liabilities directly, so nothing needs adjusting. A and C describe immunization. |
| 3 | B | 40,000 / 1.04 + 40,000 / 1.05² = 38,461.54 + 36,281.18 = \$74,742.72. A discounts both at 5%. |
| 4 | B | Accreted interest (OID) is taxed yearly even though no cash is paid, so tax-deferred accounts avoid phantom income. |
| 5 | C | The zero pays a known amount on the exact date: no coupons to reinvest and no need to sell early. |
| 6 | A | Bond face = 100,000 / 1.05 = \$95,238.10. Its year-1 coupon = \$4,761.90. Zero face = 50,000 − 4,761.90 = \$45,238.10. |
| 7 | B | Exact matching needs bonds at every liability date, which can be expensive or unavailable. A and C do not apply to a matched portfolio. |
| 8 | A | 100 / (1 + 0.042/2)²⁰ = 100 / 1.021²⁰ = \$65.99. B uses annual compounding; C discounts one year. |
