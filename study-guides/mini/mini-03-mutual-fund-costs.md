# Mini Study Guide 3: Mutual Fund Costs

*Loads, 12b-1 Fees, and Turnover (BKM Ch. 4)*

[← All study guides](../../study-guide-index.md)

FIN 4000 Investments · Midterm prep · Sep 28, 2026 · Jim Northey

## Learning objectives

Fund costs compound. A 1% difference in annual fees can cost more than a 5% up-front load over a long holding period, and turnover costs never appear in the expense ratio.

After this guide you should be able to:

1. Name each fee a mutual fund investor can pay, and say when it is charged.
2. Compute NAV, offering price, and a fund's holding-period return, with and without a load.
3. Compare share classes over different horizons and find the break-even holding period.
4. Estimate the hidden cost of portfolio turnover.

## Core concept: the fee menu

| Cost | When charged | Typical size | In the expense ratio? |
| --- | --- | --- | --- |
| Front-end load | At purchase | Up to 8.5% by rule; usually 3–5% for stock funds | No |
| Back-end load (CDSC) | At redemption; declines each year held | Often starts at 5–6%, falls to 0 over about 6 years | No |
| Operating expenses (management fee, admin) | Continuously, deducted from assets | 0.03% (index) to 1%+ (active) per year | Yes |
| 12b-1 fee | Continuously, deducted from assets | Up to 1% per year (0.75% distribution + 0.25% service) | Yes |
| Trading costs from turnover | Whenever the fund trades | Depends on turnover and spreads | **No**, hidden |

**12b-1 fees** pay for marketing, distribution, and broker compensation. They are named for the SEC rule that allows them. They are part of the expense ratio.

**Share classes** give the same portfolio different fee structures:

- **Class A:** front-end load, low 12b-1 fee. Best for long horizons.
- **Class B:** back-end load (CDSC), higher 12b-1 fee; often converts to Class A after several years. Now rare.
- **Class C:** little or no load, high 12b-1 fee (often 1%) every year. Best for short horizons.

**Turnover** is the share of the portfolio replaced each year. Commissions and bid-ask spreads reduce returns but are not in the expense ratio. High turnover also realizes capital gains, which taxable investors pay tax on each year.

**Formulas**

```math
\text{NAV} = \frac{\text{Market value of assets} - \text{Liabilities}}{\text{Shares outstanding}}
```

**Where:**

- NAV = net asset value per share
- Market value of assets = current value of all securities and cash the fund holds
- Liabilities = what the fund owes (accrued fees, borrowings)
- Shares outstanding = number of fund shares held by investors

```math
\text{Offering price} = \frac{\text{NAV}}{1 - \text{Front-end load}}
```

**Where:**

- Offering price = price per share an investor pays, including the load
- NAV = net asset value per share
- Front-end load = sales charge, as a decimal of the offering price

```math
\text{Fund return} = \frac{\text{NAV}_1 - \text{NAV}_0 + \text{Income and capital gain distributions}}{\text{NAV}_0}
```

**Where:**

- NAV₀ = net asset value per share at the start of the period
- NAV₁ = net asset value per share at the end of the period
- Income and capital gain distributions = cash paid per share during the period

For an investor who paid a load, replace NAV₀ in both places with the offering price actually paid.

**Fee drag over T years**, with gross return r, expense ratio e, and front-end load L:

```math
\text{Ending value} = \text{Investment} \times (1 - L) \times (1 + r - e)^{T}
```

**Where:**

- Investment = dollar amount invested
- L = front-end load, as a decimal
- r = annual return on the portfolio before expenses
- e = annual expense ratio, as a decimal (includes any 12b-1 fee)
- T = number of years held

## Worked examples

### Example 1: Fund return with and without a load (Algorithmic)

A fund starts the year at a NAV of \$20.00 and ends at \$21.10. It distributes \$0.50 of income and \$0.40 of capital gains. It has a 4% front-end load.

1. Return at NAV (no-load investor) = (21.10 − 20.00 + 0.90) / 20.00 = **10.0%**.
2. Offering price = 20.00 / (1 − 0.04) = **\$20.83**.
3. Return to the load-paying investor = (21.10 + 0.90 − 20.83) / 20.83 = **5.6%**.

The 4% load cost this investor 4.4 percentage points of first-year return.

### Example 2: Share classes over time (Algorithmic)

You invest \$10,000. The portfolio earns 8% per year before expenses. Compare:

- **Class A:** 5% front-end load, 0.60% expense ratio. Grows at 7.40% on \$9,500.
- **Class C:** no load, 1.25% expense ratio (includes a 1.00% 12b-1 fee). Grows at 6.75% on \$10,000.
- **Index fund:** no load, 0.10% expense ratio. Grows at 7.90% on \$10,000.

| Years held | Class A | Class C | Index fund |
| --- | --- | --- | --- |
| 1 | \$10,203 | \$10,675 | \$10,790 |
| 5 | \$13,575 | \$13,862 | \$14,625 |
| 10 | \$19,398 | \$19,217 | \$21,390 |
| 20 | \$39,610 | \$36,928 | \$45,754 |

**Break-even holding period** (A vs. C): set 9,500 × 1.074^T = 10,000 × 1.0675^T.

```math
T = \frac{\ln(10{,}000 / 9{,}500)}{\ln(1.074 / 1.0675)} = \frac{0.05129}{0.00607} \approx 8.4 \text{ years}
```

**Where:**

- T = break-even holding period, in years
- 10,000 = amount invested in Class C (no load); 9,500 = amount invested in Class A after the 5% load
- 1.074 and 1.0675 = annual growth factors (1 + r − e) for Class A and Class C
- ln = natural logarithm

Hold less than about 8.4 years and Class C wins. Hold longer and Class A wins. The low-cost index fund wins at every horizon.

**BA II Plus (Class A, 10 years):** `10` `N` · `7.4` `I/Y` · `9500` `+/-` `PV` · `0` `PMT` · `CPT` `FV` → 19,398

### Example 3: The hidden cost of turnover (Algorithmic)

A \$500 million fund has 80% annual turnover. Each round trip (sell one stock, buy another) costs 0.50% of the value traded in commissions and spreads.

1. Value traded = 0.80 × \$500M = \$400M.
2. Trading cost = 0.0050 × \$400M = \$2M.
3. As a share of assets: \$2M / \$500M = **0.40% per year**.

If the fund's expense ratio is 0.90%, the investor's total annual cost is about 1.30%, but only 0.90% shows in the prospectus fee table.

## Common pitfalls

- **Offering price.** It is NAV / (1 − load), not NAV × (1 + load). The load is a percentage of the price you pay.
- **Leaving out distributions.** Fund return includes income and capital gain distributions, not just the NAV change.
- **"No-load" means "no fees."** No-load funds still charge expense ratios, and some charge 12b-1 fees up to 0.25%.
- **Assuming the expense ratio is the full cost.** Trading costs from turnover and the taxes on realized gains are extra.
- **Picking a share class without a horizon.** Class A vs. Class C depends on how long you will hold.

## Key terms and definitions

- [ ] **Net asset value (NAV):** a fund's assets minus liabilities, divided by shares outstanding.
- [ ] **Offering price:** the price an investor pays per share; NAV plus any front-end load.
- [ ] **Front-end load:** a sales charge paid when shares are bought.
- [ ] **Back-end load / contingent deferred sales charge (CDSC):** a sales charge paid when shares are sold, declining the longer they are held.
- [ ] **12b-1 fees:** annual fees, up to 1% of assets, that pay for marketing, distribution, and shareholder servicing.
- [ ] **Expense ratio:** total annual operating expenses (management fees, administration, 12b-1 fees) as a percentage of assets.
- [ ] **Share classes (A, B, C):** different fee structures on the same portfolio: A = front load and low annual fees; B = back load; C = little or no load and high annual 12b-1 fees.
- [ ] **No-load fund:** a fund with no sales charge on purchase or redemption.
- [ ] **Portfolio turnover:** the share of the portfolio replaced during a year; drives hidden trading costs.
- [ ] **Soft dollars:** brokerage commissions that a fund pays partly in research and services from the broker, which can hide costs.
- [ ] **Open-end vs. closed-end fund:** open-end funds issue and redeem shares at NAV; closed-end funds have a fixed number of shares that trade on an exchange at a premium or discount to NAV.
- [ ] **Pass-through (tax) treatment:** a fund that distributes nearly all its income is not taxed itself; shareholders pay the tax.

## CFA-style practice questions

**Q1 [Algorithmic].** A fund holds \$250 million of assets and has \$10 million of liabilities and 12 million shares outstanding. Its NAV is *closest* to:

- A. \$20.00
- B. \$20.83
- C. \$21.67

**Q2 [Algorithmic].** A fund has a NAV of \$19.00 and a 5% front-end load. Its offering price is *closest* to:

- A. \$18.05
- B. \$19.95
- C. \$20.00

**Q3 [Algorithmic].** An investor puts \$10,000 into a fund with a 4% front-end load. The portfolio earns 9% before expenses, and the expense ratio is 1%. After one year the investment is worth *closest* to:

- A. \$10,368
- B. \$10,464
- C. \$10,800

**Q4 [Conceptual].** 12b-1 fees are used *primarily* to pay for:

- A. the portfolio manager's performance bonus.
- B. marketing, distribution, and shareholder servicing.
- C. brokerage commissions on the fund's trades.

**Q5 [Conceptual].** Which statement about trading costs from portfolio turnover is *most* accurate? They:

- A. are included in the fund's expense ratio.
- B. reduce the fund's returns but are not in the expense ratio.
- C. are billed to shareholders when they redeem.

**Q6 [Algorithmic].** Fund X charges a 5% front-end load and a 0.50% expense ratio. Fund Y has no load and a 1.25% expense ratio. Both portfolios earn 8% before expenses. For a \$10,000 investment held 10 years:

- A. Fund X ends higher, at about \$19,580.
- B. Fund Y ends higher, at about \$19,217.
- C. Both end at about the same value.

**Q7 [Algorithmic].** A no-load fund's NAV rises from \$30.00 to \$31.50, and it distributes \$1.20 per share. The rate of return is *closest* to:

- A. 4.0%
- B. 5.0%
- C. 9.0%

**Q8 [Conceptual].** A contingent deferred sales charge (back-end load) typically:

- A. rises the longer shares are held.
- B. falls the longer shares are held.
- C. is charged when shares are bought.

**Q9 [Algorithmic].** A fund has 60% annual turnover, and each round-trip trade costs 0.60% of the value traded. The annual trading cost as a percentage of fund assets is *closest* to:

- A. 0.36%
- B. 0.60%
- C. 1.00%

## Answer key

| Q | Answer | Explanation |
| --- | --- | --- |
| 1 | A | NAV = (250 − 10) / 12 = \$20.00. C adds liabilities instead of subtracting them. |
| 2 | C | 19.00 / 0.95 = \$20.00. B uses 19 × 1.05; A subtracts the load from NAV. |
| 3 | A | \$9,600 invested × (1 + 0.09 − 0.01) = \$10,368. B ignores the expense ratio; C ignores both costs. |
| 4 | B | 12b-1 fees fund distribution and servicing. Commissions (C) are trading costs, not 12b-1 fees. |
| 5 | B | Trading costs reduce NAV but are not in the expense ratio. |
| 6 | A | X: 9,500 × 1.075¹⁰ = \$19,580. Y: 10,000 × 1.0675¹⁰ = \$19,217. The break-even is about 7.3 years, so X wins at 10 years. |
| 7 | C | (31.50 − 30.00 + 1.20) / 30.00 = 9.0%. B leaves out the distribution. |
| 8 | B | The CDSC declines each year the shares are held, often to zero after about 6 years. |
| 9 | A | 0.60 × 0.60% = 0.36% of assets per year. |
