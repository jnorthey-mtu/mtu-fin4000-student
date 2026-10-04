# Mini Study Guide 10: The Two-Stage DDM and PVGO

*BKM Ch. 18*

[← All study guides](../../study-guide-index.md)

FIN 4000 Investments · Final exam prep · Sep 28, 2026 · Jim Northey

## Learning objectives

A stock's price has two parts: the value of the assets it already has (E₁ / k) and the present value of its growth opportunities (PVGO). Growth adds value only when reinvested earnings earn more than the required return (ROE > k).

After this guide you should be able to:

1. Value a stock with the constant-growth DDM and compute sustainable growth (g = ROE × b).
2. Split a stock's price into no-growth value and PVGO.
3. Explain why plowing back earnings can raise, lower, or leave price unchanged.
4. Value a stock with a two-stage DDM, discounting the terminal value correctly.
5. Connect the P/E ratio to growth opportunities.

## Core concept

### Constant growth and sustainable growth

```math
V_0 = \frac{D_1}{k - g} \qquad g = \text{ROE} \times b \qquad D_1 = E_1 (1 - b)
```

**Where:**

- V₀ = intrinsic value of the stock today
- D₁ = dividend expected next year
- k = required rate of return (market capitalization rate)
- g = constant dividend growth rate
- ROE = return on equity
- b = plowback (retention) ratio; 1 − b = payout ratio
- E₁ = earnings per share expected next year

b is the plowback (retention) ratio and 1 − b is the payout ratio. The formula needs k > g. Required return k often comes from the CAPM: k = rƒ + β[E(rₘ) − rƒ].

### PVGO

```math
P_0 = \underbrace{\frac{E_1}{k}}_{\text{no-growth value}} + \text{PVGO} \quad\Rightarrow\quad \text{PVGO} = P_0 - \frac{E_1}{k}
```

**Where:**

- P₀ = current stock price
- E₁ = earnings per share expected next year
- k = required rate of return
- E₁ / k = no-growth value (the price if all earnings were paid out forever)
- PVGO = present value of growth opportunities

| ROE vs. k | Effect of plowing back more earnings | PVGO |
| --- | --- | --- |
| ROE > k | Price rises: each reinvested dollar earns more than investors require | Positive |
| ROE = k | Price unchanged: growth appears, but it adds no value | Zero |
| ROE < k | Price falls: reinvestment destroys value | Negative |

**Growth is not the same as growth opportunities.** A firm can grow earnings by reinvesting at ROE < k and still lower its stock price.

### P/E and growth

```math
\frac{P_0}{E_1} = \frac{1}{k}\left(1 + \frac{\text{PVGO}}{E_1 / k}\right) = \frac{1 - b}{k - g}
```

**Where:**

- P₀ / E₁ = price-earnings ratio on next year's earnings
- k = required rate of return
- PVGO = present value of growth opportunities
- E₁ = earnings per share expected next year
- b = plowback ratio
- g = growth rate

A high P/E signals that the market expects large growth opportunities relative to current earnings.

### The two-stage DDM

Use it when a firm grows fast for T years, then settles into constant growth g₂ forever.

```math
V_0 = \sum_{t=1}^{T} \frac{D_t}{(1 + k)^t} + \frac{P_T}{(1 + k)^T}, \qquad P_T = \frac{D_{T+1}}{k - g_2}
```

**Where:**

- V₀ = intrinsic value today
- Dₜ = dividend in year t
- T = number of years of high growth
- Pₜ = terminal (horizon) price at the end of year T
- Dₜ₊₁ = first dividend of the constant-growth stage
- g₂ = long-run constant growth rate
- k = required rate of return

**Steps:**

1. Grow the dividend year by year at g₁ through year T.
2. Compute Dₜ₊₁ = Dₜ × (1 + g₂).
3. Compute the terminal price Pₜ = Dₜ₊₁ / (k − g₂). This is a value **at time T**.
4. Discount each dividend and Pₜ back to today. Pₜ is discounted T periods, not T + 1.

## Worked examples

### Example 1: PVGO when ROE is above, equal to, and below k (Algorithmic)

A firm expects E₁ = \$4.00, retains half its earnings (b = 0.5, so D₁ = \$2.00), and investors require k = 10%. No-growth value = E₁ / k = 4 / 0.10 = \$40.

| ROE | g = ROE × b | P₀ = D₁ / (k − g) | PVGO = P₀ − \$40 | P/E₁ |
| --- | --- | --- | --- | --- |
| 14% | 7% | 2 / 0.03 = \$66.67 | +\$26.67 | 16.7 |
| 10% | 5% | 2 / 0.05 = \$40.00 | \$0.00 | 10.0 |
| 8% | 4% | 2 / 0.06 = \$33.33 | −\$6.67 | 8.3 |

All three firms grow, but only the one earning more than k on new investment has positive PVGO. At ROE = 8%, the firm would be worth more (\$40) if it paid out every dollar.

### Example 2: Two-stage DDM (Algorithmic)

D₀ = \$1.50. Dividends grow 20% a year for 3 years, then 5% forever. k = 11%.

| Year | Dividend | Terminal value | PV at 11% |
| --- | --- | --- | --- |
| 1 | 1.50 × 1.20 = \$1.80 |  | \$1.62 |
| 2 | 1.80 × 1.20 = \$2.16 |  | \$1.75 |
| 3 | 2.16 × 1.20 = \$2.592 | P₃ = 2.592 × 1.05 / (0.11 − 0.05) = \$45.36 | (2.592 + 45.36) / 1.11³ = \$35.06 |
| **Value** |  |  | **\$38.44** |

**BA II Plus:** `CF` `2nd` `CLR WORK` · `0` `ENTER` `↓` · `1.8` `ENTER` `↓` `↓` · `2.16` `ENTER` `↓` `↓` · `47.952` `ENTER` · `NPV` · `11` `ENTER` `↓` `CPT` → 38.44

*Put P₃ in the same cash flow as D₃ (year 3), not in year 4.*

### Example 3: Required return from the CAPM (Algorithmic)

rƒ = 4%, β = 1.2, market risk premium = 6%. D₁ = \$2.24 and g = 5%.

1. k = 4% + 1.2 × 6% = **11.2%**.
2. V₀ = 2.24 / (0.112 − 0.05) = **\$36.13**.

If the stock trades at \$32, it is underpriced by this model: its implied return D₁ / P₀ + g = 7.0% + 5% = 12.0% exceeds the 11.2% required.

## Common pitfalls

- **Using D₀ in the numerator.** The DDM uses next year's dividend: D₁ = D₀(1 + g).
- **Discounting the terminal value one period too many.** Pₜ is already a time-T value; discount it T periods.
- **Computing Pₜ with Dₜ.** It uses Dₜ₊₁ = Dₜ(1 + g₂).
- **Equating growth with value creation.** Only ROE > k creates positive PVGO.
- **Using E₀ for PVGO.** No-growth value is E₁ / k.

## Key terms and definitions

- [ ] **Intrinsic value:** the present value of a firm's expected future cash payoffs, discounted at the required return.
- [ ] **Dividend discount model (DDM):** values a stock as the present value of all expected future dividends.
- [ ] **Constant-growth (Gordon) model:** V₀ = D₁ / (k − g), for dividends growing at a constant rate forever.
- [ ] **Plowback (retention) ratio and payout ratio:** the share of earnings reinvested (b) vs. paid out as dividends (1 − b).
- [ ] **Sustainable growth rate, g = ROE × b:** the growth rate a firm can support from reinvested earnings alone.
- [ ] **Present value of growth opportunities (PVGO):** the part of a stock's price that comes from future investments earning more than k.
- [ ] **No-growth value (E₁ / k):** a firm's value if it paid out all earnings and never grew.
- [ ] **Multistage (two-stage) DDM:** a DDM with a high-growth period followed by constant growth.
- [ ] **Terminal (horizon) value:** the value at the end of the forecast period of all dividends after that date.
- [ ] **Price-earnings ratio:** stock price ÷ earnings per share; reflects growth opportunities and risk.
- [ ] **Market capitalization rate (k):** the market's consensus required return on a stock, often estimated with the CAPM.

## CFA-style practice questions

**Q1 [Algorithmic].** A stock's next dividend is \$3.00, its required return is 11%, and its dividend growth rate is 5%. Its intrinsic value is *closest* to:

- A. \$27.27
- B. \$50.00
- C. \$52.50

**Q2 [Algorithmic].** A firm has a 12% ROE and retains 40% of its earnings. Its sustainable growth rate is:

- A. 4.8%
- B. 7.2%
- C. 12.0%

**Q3 [Algorithmic].** A stock sells for \$80. Next year's expected EPS is \$5.00, and the required return is 10%. Its PVGO is *closest* to:

- A. \$30
- B. \$50
- C. \$75

**Q4 [Conceptual].** A firm's ROE is 8% and its required return is 10%. If it increases its plowback ratio, its stock price will *most likely*:

- A. rise, because growth increases.
- B. stay the same.
- C. fall, because reinvestment earns less than investors require.

**Q5 [Algorithmic].** D₀ = \$2.00. Dividends grow 15% for 2 years, then 4% forever. k = 10%. The stock's value is *closest* to:

- A. \$34.67
- B. \$38.72
- C. \$42.17

**Q6 [Conceptual].** In a two-stage DDM whose high-growth phase lasts T years, the terminal value Pₜ should be:

- A. discounted back T years.
- B. discounted back T + 1 years.
- C. added to Dₜ₊₁ and discounted back T + 1 years.

**Q7 [Algorithmic].** A firm has a plowback ratio of 0.40, a required return of 10%, and a growth rate of 6%. Its P/E ratio (on next year's earnings) is:

- A. 10
- B. 15
- C. 25

**Q8 [Conceptual].** A stock with a much higher P/E than its industry *most likely* has:

- A. a higher required return than its peers.
- B. a large PVGO relative to the value of its existing assets.
- C. a lower ROE than its required return.

**Q9 [Algorithmic].** rƒ = 4%, β = 1.2, and the market risk premium is 6%. A stock's D₁ = \$2.24 and g = 5%. Its value is *closest* to:

- A. \$36.13
- B. \$37.33
- C. \$44.80

## Answer key

| Q | Answer | Explanation |
| --- | --- | --- |
| 1 | B | 3.00 / (0.11 − 0.05) = \$50.00. C wrongly grows the given D₁ again; A ignores growth. |
| 2 | A | g = 0.12 × 0.40 = 4.8%. B uses the payout ratio (0.60). |
| 3 | A | No-growth value = 5 / 0.10 = \$50. PVGO = 80 − 50 = \$30. |
| 4 | C | With ROE < k, each reinvested dollar is worth less than a dollar to shareholders, so PVGO falls. |
| 5 | C | D₁ = 2.30, D₂ = 2.645, P₂ = 2.645 × 1.04 / 0.06 = 45.85. V = 2.30 / 1.10 + (2.645 + 45.85) / 1.10² = \$42.17. B discounts P₂ one year too many; A ignores the high-growth stage. |
| 6 | A | Pₜ is the value at time T of all dividends from T + 1 on, so it is discounted T years. |
| 7 | B | P/E = (1 − b) / (k − g) = 0.60 / 0.04 = 15. C forgets the payout ratio. |
| 8 | B | A high P/E reflects large growth opportunities relative to earnings. A would lower the P/E; C implies negative PVGO. |
| 9 | A | k = 4% + 1.2 × 6% = 11.2%. V = 2.24 / (0.112 − 0.05) = \$36.13. C uses k = 10% (β of 1). |
