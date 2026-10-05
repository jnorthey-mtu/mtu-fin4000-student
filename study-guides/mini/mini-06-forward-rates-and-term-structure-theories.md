# Mini Study Guide 6: Forward Rates and Term Structure Theories

*BKM Ch. 15*

[← All study guides](../../study-guide-index.md)

FIN 4000 Investments · Midterm prep · Sep 28, 2026 · Jim Northey

## Learning objectives

A forward rate is the rate that makes a long-term investment and a series of short-term investments break even. The term structure theories disagree only on whether that rate equals the market's expected future short rate.

After this guide you should be able to:

1. Compute spot rates from zero-coupon prices.
2. Compute one-year and multi-year forward rates from spot rates.
3. Price a coupon bond with spot rates, not a single YTM.
4. Explain what an upward- or downward-sloping yield curve implies under the expectations and liquidity preference theories.

## Core concept

### Spot rates and forward rates

The **spot rate** yₙ is the YTM on an n-year zero-coupon bond. The **forward rate** fₙ is the one-year rate for year n implied by today's spot rates.

```math
(1 + y_n)^n = (1 + y_{n-1})^{n-1}(1 + f_n) \quad\Rightarrow\quad f_n = \frac{(1 + y_n)^n}{(1 + y_{n-1})^{n-1}} - 1
```

More generally, the annualized forward rate from year a to year b:

```math
f_{a,b} = \left[\frac{(1 + y_b)^b}{(1 + y_a)^a}\right]^{1/(b - a)} - 1
```

When the yield curve rises, forward rates are above spot rates. When it falls, forward rates are below spot rates.

**Other forms of the forward rate.** In zero-coupon price notation, where Pₙ is the price of a \$1 face-value zero maturing at time n:

```math
1+f_n = \frac{P_{n-1}}{P_n}
```

With m compounding periods per annum (m = 2 for semiannual), n counts periods and fₙ is the annualized forward rate for period n:

```math
(1+\frac{y_n}{m})^n = (1+\frac{y_{n-1}}{m})^{n-1}(1+\frac{f_n}{m})
```

```math
f_n = m(\frac{(1+\frac{y_n}{m})^n}{(1+\frac{y_{n-1}}{m})^{n-1}} - 1)
```

```math
f_{a,b} = ((1+y_b)^b / (1+y_a)^a)^{1/(b-a)} - 1
```

**Definitions of terms** (type as a normal bulleted list in Canvas; use the equation editor only for the symbols):

- yₙ = spot rate (YTM on a zero-coupon bond) for maturity n
- fₙ = one-period forward rate for period n, implied by yₙ₋₁ and yₙ
- f(a,b) = annualized forward rate from time a to time b, a < b
- Pₙ = price of a \$1 face-value zero-coupon bond maturing at time n
- m = number of compounding periods per annum
- n = number of years (or periods, in the m-period form)

### The theories

| Theory | What the forward rate equals | An upward-sloping curve means |
| --- | --- | --- |
| Expectations hypothesis | The expected future short rate: fₙ = E(rₙ) | Short rates are expected to rise |
| Liquidity preference | Expected short rate plus a liquidity premium: fₙ = E(rₙ) + LP | Rates may be expected to rise, *or* the premium alone may cause the slope |
| Market segmentation (preferred habitat) | Set by supply and demand within each maturity segment | Relative demand for short vs. long bonds, not rate forecasts |

**Why a liquidity premium?** Short-horizon investors see price risk in long bonds, so they demand extra return to hold them. Under liquidity preference, the curve slopes up even when no change in rates is expected. A *downward* slope therefore signals an expected fall in rates large enough to outweigh the premium.

**Pricing coupon bonds with spot rates.** Each cash flow is discounted at the spot rate for its own date:

```math
P = \sum_{t=1}^{T} \frac{CF_t}{(1 + y_t)^t}
```

**Where:**

- P = price of the coupon bond
- CFₜ = cash flow (coupon, plus principal at maturity) paid at time t
- yₜ = spot rate for maturity t
- T = years to maturity

## Worked examples

### Example 1: Spot rates, zero prices, and forward rates (Algorithmic)

| Maturity | Spot rate yₙ | Zero price (\$1,000 face) | Forward rate fₙ |
| --- | --- | --- | --- |
| 1 year | 5.00% | 1,000 / 1.05 = \$952.38 | — |
| 2 years | 6.00% | 1,000 / 1.06² = \$890.00 | 1.06² / 1.05 − 1 = **7.01%** |
| 3 years | 6.50% | 1,000 / 1.065³ = \$827.85 | 1.065³ / 1.06² − 1 = **7.51%** |

**Two-year forward rate starting in year 1** (covers years 2 and 3):

```math
f_{1,3} = \left(\frac{1.065^3}{1.05}\right)^{1/2} - 1 = 7.26\%
```

This is roughly the geometric average of f₂ and f₃, as it should be.

**Calculator:** `1.06` `x²` `÷` `1.05` `−` `1` `=` → 0.0701 · `1.065` `y^x` `3` `÷` `1.06` `x²` `−` `1` `=` → 0.0751

### Example 2: Backing out expected rates (Algorithmic)

Using f₂ = 7.01% from Example 1:

- **Expectations hypothesis:** the market expects next year's one-year rate to be **7.01%**.
- **Liquidity preference, with a 1% premium:** E(r₂) = 7.01% − 1.00% = **6.01%**. Rates are still expected to rise from 5%, but by less.
- With a 2% premium, E(r₂) = 5.01%. The whole upward slope could be the premium, with no expected rise in rates.

### Example 3: Pricing a coupon bond with spot rates (Algorithmic)

Price a 3-year, 6% annual-coupon bond using the Example 1 spot rates.

```math
P = \frac{60}{1.05} + \frac{60}{1.06^2} + \frac{1{,}060}{1.065^3} = 57.14 + 53.40 + 877.52 = \$988.06
```

Its YTM is 6.45%. That is a blend of the three spot rates, weighted toward the 3-year rate because most of the value arrives at year 3.

**BA II Plus (YTM):** `3` `N` · `988.06` `+/-` `PV` · `60` `PMT` · `1000` `FV` · `CPT` `I/Y` → 6.45

### Example 4: The break-even interpretation (Conceptual)

You have a 2-year horizon. You can buy a 2-year zero at 6%, or buy a 1-year zero at 5% and roll it into a new 1-year zero next year.

- 2-year zero: \$1 grows to 1.06² = \$1.1236.
- Roll-over: \$1 grows to 1.05 × (1 + r₂).
- They break even when r₂ = 7.01%, which is the forward rate f₂.

If you expect next year's rate to be above 7.01%, rolling over is better. If below, lock in the 2-year zero.

## Common pitfalls

- **Subtracting spot rates.** f₂ is not 2 × 6% − 5% = 7%. Compound: 1.06² / 1.05 − 1 = 7.01%. The shortcut is close at low rates but not exact.
- **Treating forward rates as forecasts under every theory.** Only the expectations hypothesis says f = E(r).
- **Reading an upward slope as proof that rates will rise.** Under liquidity preference, the premium alone can create it.
- **Discounting all coupons at the YTM when spot rates are given.** Use each date's own spot rate.

## Key terms and definitions

- [ ] **Yield curve:** a plot of yield to maturity against time to maturity.
- [ ] **Spot rate / pure yield curve:** the YTM on a zero-coupon bond; the pure yield curve plots spot rates against maturity.
- [ ] **On-the-run yield curve:** a yield curve built from recently issued, highly liquid Treasuries that trade near par.
- [ ] **Short rate:** the one-period interest rate prevailing for a given period.
- [ ] **Forward rate:** the future short rate implied by today's spot rates; the break-even rate between long and rolled-over short investments.
- [ ] **Expectations hypothesis:** the theory that forward rates equal the market's expected future short rates.
- [ ] **Liquidity preference theory:** the theory that investors demand a premium to hold longer bonds, so forward rates exceed expected short rates.
- [ ] **Liquidity premium:** the extra expected return demanded for holding a longer-term bond; forward rate minus expected short rate.
- [ ] **Market segmentation / preferred habitat:** the theory that supply and demand within each maturity segment set its rates; preferred habitat adds that investors will shift segments for enough extra yield.
- [ ] **Bootstrapping:** deriving spot rates one maturity at a time from coupon bond prices.
- [ ] **Inverted yield curve:** a curve on which long-term yields are below short-term yields.

## CFA-style practice questions

**Q1 [Algorithmic].** The 1-year spot rate is 4% and the 2-year spot rate is 5%. The 1-year forward rate for year 2 is *closest* to:

- A. 4.50%
- B. 5.00%
- C. 6.01%

**Q2 [Algorithmic].** The 2-year spot rate is 5.0% and the 3-year spot rate is 5.5%. The 1-year forward rate for year 3 is *closest* to:

- A. 5.75%
- B. 6.00%
- C. 6.50%

**Q3 [Conceptual].** Under the pure expectations hypothesis, an upward-sloping yield curve indicates that:

- A. short-term rates are expected to rise.
- B. investors demand a premium to hold long bonds.
- C. demand for long bonds is weak relative to supply.

**Q4 [Conceptual].** Under the liquidity preference theory, forward rates are:

- A. equal to expected future short rates.
- B. greater than expected future short rates.
- C. less than expected future short rates.

**Q5 [Algorithmic].** The forward rate for year 2 is 7.0%. The liquidity premium is 0.75%. Under liquidity preference, the expected 1-year rate in year 2 is:

- A. 6.25%
- B. 7.00%
- C. 7.75%

**Q6 [Algorithmic].** The 3-year spot rate is 6.5%. The price of a 3-year zero-coupon bond with \$1,000 face value is *closest* to:

- A. \$827.85
- B. \$835.00
- C. \$938.97

**Q7 [Conceptual].** Under the liquidity preference theory, an inverted yield curve *most likely* indicates that:

- A. short rates are expected to stay the same.
- B. short rates are expected to fall.
- C. the liquidity premium is negative.

**Q8 [Algorithmic].** Spot rates are 4% (1 year), 5% (2 years), and 5.5% (3 years). The price of a 3-year, 5% annual-coupon bond (\$1,000 face) is *closest* to:

- A. \$986.51
- B. \$987.62
- C. \$1,000.00

**Q9 [Conceptual].** Which theory holds that short- and long-maturity bonds trade in separate markets, each with its own equilibrium rate?

- A. Expectations hypothesis
- B. Liquidity preference
- C. Market segmentation

## Answer key

| Q | Answer | Explanation |
| --- | --- | --- |
| 1 | C | 1.05² / 1.04 − 1 = 6.01%. A averages the spot rates. |
| 2 | C | 1.055³ / 1.05² − 1 = 6.50%. |
| 3 | A | Under the expectations hypothesis, forward rates equal expected short rates, so an upward slope means rising expected rates. B is liquidity preference; C is segmentation. |
| 4 | B | f = E(r) + liquidity premium, and the premium is positive. |
| 5 | A | E(r₂) = 7.00% − 0.75% = 6.25%. C adds the premium instead of subtracting it. |
| 6 | A | 1,000 / 1.065³ = \$827.85. C discounts for only one year. |
| 7 | B | A positive premium pushes long rates up, so an inverted curve requires expected short rates to fall by more than the premium. |
| 8 | B | 50 / 1.04 + 50 / 1.05² + 1,050 / 1.055³ = 48.08 + 45.35 + 894.19 = \$987.62. A discounts every flow at 5.5%. |
| 9 | C | Market segmentation treats each maturity as its own market. |
