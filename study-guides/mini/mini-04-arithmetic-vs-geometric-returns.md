# Mini Study Guide 4: Arithmetic vs. Geometric Returns; Real vs. Nominal Rates

*BKM Ch. 5*

[← All study guides](../../study-guide-index.md)

FIN 4000 Investments · Midterm prep · Sep 28, 2026 · Jim Northey

## Learning objectives

The geometric average is what an investor actually earned. The arithmetic average is the better estimate of next year's expected return. The real rate is what that return buys after inflation.

After this guide you should be able to:

1. Compute arithmetic, geometric, and dollar-weighted average returns.
2. Explain why the geometric average is never above the arithmetic average, and approximate the gap.
3. Choose the right average for measuring past performance or forecasting.
4. Convert between nominal and real rates with the exact Fisher equation and the approximation.
5. Compute an after-tax real rate of return.

## Core concept

### Three ways to average returns

```math
\text{Arithmetic: } \bar{r}_A = \frac{1}{n}\sum_{t=1}^{n} r_t
```

**Where:**

- r̄(A) = arithmetic average return
- n = number of periods
- rₜ = return in period t
- Σ = sum over periods t = 1 to n

```math
\text{Geometric: } \bar{r}_G = \left[\prod_{t=1}^{n}(1 + r_t)\right]^{1/n} - 1
```

**Where:**

- r̄(G) = geometric (time-weighted) average return
- Π = product over periods t = 1 to n
- rₜ = return in period t
- n = number of periods

```math
\text{Approximation: } \bar{r}_G \approx \bar{r}_A - \tfrac{1}{2}\sigma^2
```

**Where:**

- r̄(G), r̄(A) = geometric and arithmetic average returns
- σ² = variance of the returns (σ = standard deviation), in decimals

| Measure | Answers the question | Use it for |
| --- | --- | --- |
| Arithmetic average | What is a typical single-period return? | Unbiased estimate of next period's expected return |
| Geometric (time-weighted) average | What constant annual rate gives the same ending wealth? | Past performance of a manager or asset |
| Dollar-weighted average (IRR) | What did *this investor* earn, given when money went in and out? | An investor's own experience, including timing |

The geometric average equals the arithmetic only when every period's return is the same. The more volatile the returns, the bigger the gap.

### Nominal vs. real rates

The nominal rate R is growth in dollars. The real rate r is growth in purchasing power. With inflation i, the **Fisher equation** is:

```math
(1 + R) = (1 + r)(1 + i) \quad\Rightarrow\quad r = \frac{R - i}{1 + i} \approx R - i
```

**Where:**

- R = nominal interest rate
- r = real interest rate
- i = inflation rate

The approximation is close when inflation is low and poor when it is high.

**Taxes** apply to the *nominal* return, including the part that only makes up for inflation:

```math
r_{\text{after-tax}} = \frac{1 + R(1 - t)}{1 + i} - 1 \approx R(1 - t) - i
```

**Where:**

- r(after-tax) = after-tax real rate of return
- R = nominal rate of return
- t = investor's tax rate
- i = inflation rate

## Worked examples

### Example 1: The +50% / −50% trap (Conceptual)

A stock rises 50% one year and falls 50% the next. \$100 becomes \$150, then \$75.

- Arithmetic average = (50% − 50%) / 2 = **0%**.
- Geometric average = (1.50 × 0.50)^(1/2) − 1 = **−13.4%**.

The investor lost 25% of their money. Only the geometric average reflects that.

### Example 2: Four-year averages (Algorithmic)

Annual returns: 10%, −5%, 20%, 3%.

1. Arithmetic = (10 − 5 + 20 + 3) / 4 = **7.00%**.
2. Wealth relative = 1.10 × 0.95 × 1.20 × 1.03 = 1.2917.
3. Geometric = 1.2917^(1/4) − 1 = **6.61%**.
4. Check with the approximation: sample σ = 10.6%, so 7.00% − ½(0.106)² ≈ 6.44%. The approximation is rough with only four years of data.

**BA II Plus (geometric):** `1.1` `×` `.95` `×` `1.2` `×` `1.03` `=` → 1.2917 · `y^x` `.25` `=` → 1.0661 · `−` `1` `=`

Or with TVM: `4` `N` · `1` `+/-` `PV` · `0` `PMT` · `1.2917` `FV` · `CPT` `I/Y` → 6.61

### Example 3: Dollar-weighted vs. time-weighted (Algorithmic)

You buy one share at \$50. A year later it is \$53 and pays a \$2 dividend, and you buy a second share. At the end of year 2 it is \$54, pays another \$2 per share, and you sell both.

| Time | Cash flow | Detail |
| --- | --- | --- |
| 0 | −\$50 | Buy one share |
| 1 | −\$51 | Buy second share \$53, receive \$2 dividend |
| 2 | +\$112 | Sell two shares at \$54, receive \$4 of dividends |

- **Dollar-weighted return** (IRR) = **7.12%**.
- **Time-weighted returns**: year 1 = (53 + 2 − 50) / 50 = 10.00%; year 2 = (54 + 2 − 53) / 53 = 5.66%. Arithmetic average = 7.83%; geometric = 7.81%.

The dollar-weighted return is lower because more money was invested in the weaker year.

**BA II Plus (IRR):** `CF` `2nd` `CLR WORK` · `50` `+/-` `ENTER` `↓` · `51` `+/-` `ENTER` `↓` `↓` · `112` `ENTER` · `IRR` `CPT` → 7.12

### Example 4: Real and after-tax real rates (Algorithmic)

A bond yields 6% nominal. Inflation is 2.5%. Your tax rate is 30%.

1. Exact real rate = 1.06 / 1.025 − 1 = **3.41%** (approximation: 3.5%).
2. After-tax nominal = 6% × (1 − 0.30) = 4.20%.
3. After-tax real = 1.042 / 1.025 − 1 = **1.66%** (approximation: 1.7%).

Tax took 1.8 percentage points of nominal return but more than half of the real return. Taxes fall on the inflation part of the return too.

## Common pitfalls

- **Averaging percentages for past performance.** Use the geometric average for what was actually earned.
- **Using the geometric average to forecast one year.** The arithmetic average is the unbiased one-period forecast.
- **Subtracting inflation when the question says "exact."** Use r = (R − i) / (1 + i).
- **Taxing only the real return.** Tax falls on the full nominal return, so after-tax real returns can be very low or negative.
- **Treating dollar- and time-weighted returns as the same.** They differ whenever the investor adds or withdraws money.

## Key terms and definitions

- [ ] **Holding-period return (HPR):** (ending price − beginning price + cash income) ÷ beginning price.
- [ ] **Arithmetic average:** the simple average of periodic returns; the unbiased estimate of next period's expected return.
- [ ] **Geometric (time-weighted) average:** the constant per-period return that produces the same ending wealth; the right measure of past performance.
- [ ] **Dollar-weighted return (IRR):** the internal rate of return on an investor's actual cash flows; it reflects the timing and size of contributions and withdrawals.
- [ ] **Nominal interest rate:** the growth rate of money in dollar terms.
- [ ] **Real interest rate:** the growth rate of purchasing power, net of inflation.
- [ ] **Fisher equation:** (1 + R) = (1 + r)(1 + i), linking nominal rates, real rates, and inflation.
- [ ] **Inflation:** the rate at which the general price level rises, usually measured by the CPI.
- [ ] **After-tax real rate:** the real return left after taxes, which fall on the full nominal return.
- [ ] **T-bills as an inflation hedge:** T-bill yields track inflation fairly closely, so their real returns have stayed near zero.

## CFA-style practice questions

**Q1 [Algorithmic].** A fund returned 15%, −10%, and 8% over three years. Its geometric average annual return is *closest* to:

- A. 3.78%
- B. 4.33%
- C. 13.00%

**Q2 [Conceptual].** Which statement about the geometric and arithmetic averages of the same return series is *most* accurate?

- A. The geometric average is always greater than the arithmetic average.
- B. The geometric average is less than or equal to the arithmetic average, and equal only when every return is the same.
- C. The two averages are equal when returns average to zero.

**Q3 [Algorithmic].** The nominal rate is 8% and expected inflation is 3%. The exact real rate is *closest* to:

- A. 4.85%
- B. 5.00%
- C. 11.24%

**Q4 [Algorithmic].** An investor in the 25% tax bracket earns 5% nominal. Inflation is 2%. Her after-tax real return is *closest* to:

- A. 1.72%
- B. 2.21%
- C. 2.94%

**Q5 [Conceptual].** To estimate next year's expected return from 50 years of annual data, an analyst should *most* appropriately use the:

- A. arithmetic average.
- B. geometric average.
- C. dollar-weighted average.

**Q6 [Algorithmic].** \$10,000 grows to \$16,105 over five years. The geometric average annual return is *closest* to:

- A. 9.0%
- B. 10.0%
- C. 12.2%

**Q7 [Conceptual].** An investor adds a large sum to a fund just before its worst year. Compared with the fund's time-weighted return, the investor's dollar-weighted return will be:

- A. higher.
- B. lower.
- C. the same.

**Q8 [Algorithmic].** An asset's arithmetic average return is 10% and its standard deviation is 20%. The approximate geometric average return is:

- A. 6%
- B. 8%
- C. 9%

**Q9 [Conceptual].** Inflation turns out higher than expected. The holder of a fixed-rate bond bought at issue will see:

- A. a lower realized real return than expected.
- B. a higher realized real return than expected.
- C. no change in real return, because the coupon is fixed.

## Answer key

| Q | Answer | Explanation |
| --- | --- | --- |
| 1 | A | (1.15 × 0.90 × 1.08)^(1/3) − 1 = 1.1178^(1/3) − 1 = 3.78%. B is the arithmetic average; C sums the returns. |
| 2 | B | Volatility pulls the geometric average below the arithmetic. They are equal only with zero variability. |
| 3 | A | 1.08 / 1.03 − 1 = 4.85%. B is the approximation; C multiplies instead of divides. |
| 4 | A | After-tax nominal = 5% × 0.75 = 3.75%. Real = 1.0375 / 1.02 − 1 = 1.72%. B taxes only the real return (0.75 × 2.94%); C ignores tax. |
| 5 | A | The arithmetic average is the unbiased estimate of a one-period expected return. |
| 6 | B | (16,105 / 10,000)^(1/5) − 1 = 10.0%. C is the simple 61.05% gain ÷ 5. |
| 7 | B | More dollars were exposed to the worst year, so the dollar-weighted return is lower. |
| 8 | B | 10% − ½(0.20)² = 10% − 2% = 8%. |
| 9 | A | The nominal coupon is fixed, so higher inflation lowers its real value. |
