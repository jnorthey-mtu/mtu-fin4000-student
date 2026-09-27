# Study Guide 5: Duration, Average Life and Convexity

*Fixed Income Study Guides*

[← All study guides](README.md)

These three measures describe when a bond's money comes back and how its price reacts to rate changes. Duration is the first-order rate sensitivity, convexity corrects for the curve in the price-yield relationship, and average life measures only when principal is repaid.

Worked bond (from Study Guide 4): 10-year, 5% semiannual coupon, price 95, YTM 5.6617%. Results: Macaulay duration **7.927**, modified duration **7.709**, convexity **72.41**, DV01 **0.0732** per 100 face.

## 1. Macaulay duration

The weighted-average time to receive the bond's cash flows, where each weight is that cash flow's share of the price. Measured in years.

```math
D_{mac} = \sum_{t} t \times w_t \qquad w_t = \frac{CF_t / (1 + y)^{t}}{P}
```

For semiannual bonds, compute with $`t`$ in half-years and $`y`$ per half-year, then divide the result by 2.

Closed form at a coupon date, with $`y`$ and $`c`$ per period and $`T`$ periods:

```math
D_{mac} = \frac{1 + y}{y} - \frac{(1 + y) + T(c - y)}{c\left[(1 + y)^{T} - 1\right] + y}
```

Worked bond: $`y = 2.8308\%`$, $`c = 2.5\%`$, $`T = 20`$, giving 15.855 half-years = **7.927 years**.

Check against the book: an 8% coupon, 2-year bond at a 10% yield has duration 1.8852 years; a 2-year zero has duration 2.0.

## 2. Modified duration

The percentage price change for a 1-unit change in yield. This is the number used for risk.

```math
D^{*} = \frac{D_{mac}}{1 + y/k} \qquad \frac{\Delta P}{P} \approx -D^{*} \, \Delta y
```

Here $`k`$ is payments per year. Worked bond: $`7.927 / 1.028308 = 7.709`$. A 100 bp rise predicts a 7.71% price fall.

## 3. Rules for duration

| Rule | Statement | Why |
| --- | --- | --- |
| 1 | A zero's duration equals its maturity | All value arrives at one date |
| 2 | Holding maturity fixed, lower coupon means higher duration | More value sits in the final payment |
| 3 | Holding coupon fixed, duration generally rises with maturity | Cash flows are further out; deep-discount long bonds are the exception |
| 4 | Holding coupon and maturity fixed, lower yield means higher duration | Distant cash flows are discounted less, so they weigh more |
| 5 | A level perpetuity has duration (1 + y) ÷ y | At 10%, duration = 11 years |

```math
D_{perpetuity} = \frac{1 + y}{y}
```

## 4. Dollar duration and DV01

Traders manage dollars, not percentages.

```math
\text{Dollar duration} = D^{*} \times P \qquad DV01 = D^{*} \times P \times 0.0001
```

- Worked bond: $`DV01 = 7.709 \times 95 \times 0.0001 = 0.0732`$ per 100 face. For \$10 million face, a 1 bp rise costs about **\$7,324**.
- DV01 is also called PVBP (price value of a basis point) or BPV. DV01s add across positions, which makes them the standard unit for limits and hedges.

## 5. Effective duration

For bonds whose cash flows change when rates change (callables, puttables, MBS), YTM-based duration is wrong. Reprice with a model at yields shifted up and down:

```math
D_{eff} = \frac{P_{-} - P_{+}}{2 \, P_{0} \, \Delta y}
```

Worked bond with $`\Delta y`$ = 50 bp: $`P_{-} = 98.749`$, $`P_{+} = 91.423`$, so

```math
D_{eff} = \frac{98.749 - 91.423}{2 \times 95 \times 0.005} = 7.712
```

matching modified duration for an option-free bond. For a callable, $`P_{-}`$ is capped near the call price, so effective duration falls well below modified duration.

## 6. Portfolio and key rate duration

- **Portfolio duration** is the value-weighted average of the holdings' durations. A strictly correct figure uses one common yield, but the weighted average is standard practice.
- **Key rate durations** measure sensitivity to one point on the curve (2, 5, 10, 30 years) at a time. They capture twists and steepening that a single duration, which assumes a parallel shift, misses.

```math
D_{portfolio} = \sum_{i} w_i \, D_i \qquad w_i = \frac{MV_i}{\sum_j MV_j}
```

## 7. Weighted average life (WAL)

The average time until each dollar of **principal** is repaid. It ignores interest and discounting, so it measures timing of principal, not price risk.

```math
WAL = \frac{\sum_{t} t \times \text{Principal}_t}{\sum_{t} \text{Principal}_t}
```

| Instrument | WAL | Note |
| --- | --- | --- |
| Worked bond (bullet) | 10.00 yr | All principal at maturity; compare duration 7.93 |
| Bond with sinking fund retiring 20% a year, years 1–5 | 3.00 yr | (1 + 2 + 3 + 4 + 5) × 20 ÷ 100 |
| 30-year 6% level-payment mortgage, no prepayment | 19.31 yr | Principal repaid slowly at first |
| Same mortgage, 8% CPR prepayments | 8.96 yr | Prepayments cut WAL by more than half |
| 15-year 6% level-payment mortgage | 8.65 yr | |

**Uses:**

- **MBS and ABS pricing:** spreads are quoted over the Treasury whose maturity is nearest the security's WAL.
- **Amortizing loans and sinking-fund bonds:** WAL gives a single "effective maturity" for comparing issues.
- **Bank asset-liability management:** WAL shows when principal returns for reinvestment.
- **Blind spot:** WAL depends on a prepayment assumption and says nothing about price sensitivity. Use effective duration for risk.

## 8. Convexity

The price-yield curve is convex, so duration alone underestimates price gains and overstates price losses. Convexity measures that curvature.

```math
C = \frac{1}{P\,(1 + y)^{2}} \sum_{t} \frac{CF_t}{(1 + y)^{t}}\left(t^{2} + t\right)
```

With $`t`$ in half-years and $`y`$ per half-year, divide the result by 4 to annualize. Worked bond: **C = 72.41**. For a zero:

```math
C_{zero} = \frac{T\,(T + 0.5)}{(1 + y/2)^{2}}
```

A 30-year strip at 4.5% has $`C = 875`$.

Price change with convexity:

```math
\frac{\Delta P}{P} \approx -D^{*}\,\Delta y + \tfrac{1}{2}\,C\,(\Delta y)^{2}
```

| Yield change | Actual price change | Duration only | Duration + convexity |
| --- | --- | --- | --- |
| +200 bp | −14.06% | −15.42% | −13.97% |
| +100 bp | −7.36% | −7.71% | −7.35% |
| −100 bp | +8.08% | +7.71% | +8.07% |
| −200 bp | +16.97% | +15.42% | +16.87% |

Duration alone is off by 1.4–1.6 points at ±200 bp; adding convexity cuts the error to about 0.1.

**Effective convexity** for bonds with options:

```math
C_{eff} = \frac{P_{-} + P_{+} - 2P_{0}}{P_{0}\,(\Delta y)^{2}}
```

Worked bond at ±50 bp:

```math
C_{eff} = \frac{98.749 + 91.423 - 190}{95 \times 0.005^{2}} = 72.4
```

**Why investors like convexity:** for two bonds with equal duration, the more convex one gains more when rates fall and loses less when rates rise. The market charges for it with a lower yield.

**Negative convexity:** callable bonds and mortgage-backed securities. As rates fall, the call or prepayments cap the price near par, so the price curve bends the wrong way. The holder gets small gains and full-sized losses. This is why MBS yield more than Treasuries of similar duration.

## 9. Using the measures to manage interest rate risk

**Immunization** protects a known future liability against rate changes. Conditions:

1. PV of assets = PV of liability.
2. Duration of assets = duration of liability.
3. Convexity of assets > convexity of liability (so any rate move leaves a surplus).

Example: a \$1,000,000 liability due in 7 years, with rates flat at 10% (annual). PV = \$513,158; duration = 7. Fund it with a 3-year zero (duration 3) and a perpetuity (duration 11):

```math
w \times 3 + (1 - w) \times 11 = 7 \quad\Rightarrow\quad w = 0.5
```

Buy \$256,579 of each. Durations drift at different speeds as time passes and rates move, so the portfolio must be **rebalanced**. Buying a 7-year zero (cash flow matching, dedication) avoids rebalancing entirely; that is the strip use case from Study Guide 1.

**DV01 hedging.** The hedge ratio is:

```math
\text{Hedge ratio} = \frac{DV01_{position}}{DV01_{hedge}}
```

- Position: \$10 million face of the worked bond, DV01 \$7,324.
- Hedge with a 30-year strip at 4.5%: $`DV01 = 29.34 \times 26.315 \times 0.0001 = 0.0772`$ per 100.
- Short about **\$9.49 million face** of the strip (market value about \$2.50 million).
- The hedge is exact only for a parallel shift. It leaves curve risk (10-year vs 30-year) and a convexity mismatch (72 vs 875). Key rate DV01s or a Treasury futures hedge in the 10-year sector reduce that residual risk.

**Other uses:**

- **Bank and insurer gap management:** match asset and liability durations to protect net worth, not just income.
- **Portfolio positioning:** active managers lengthen duration when they expect falling rates and shorten it when they expect rising rates.
- **Risk limits and reporting:** DV01 and key rate DV01 limits by desk, with convexity reported for large moves.

## 10. Tools: the worked bond on every platform

Targets: Macaulay 7.927 · modified 7.709 · convexity 72.41 · DV01 0.0732 · prices at ±50 bp 98.749 / 91.423 · mortgage WAL 19.31.

### TI BA II Plus Professional

**Modified and Macaulay duration (Bond worksheet)**

1. `2nd` `BOND`: SDT = 11.1526, CPN = 5, RDT = 11.1536, RV = 100, ACT, 2/Y.
2. PRI = 95 `ENTER`, then YLD `CPT` → 5.6617.
3. ↓ to DUR → **7.709** (modified).
4. Macaulay: 7.709 `×` `(` 1 `+` 5.6617 `÷` 200 `)` `=` → **7.927**.

**Effective duration and convexity (TVM, P/Y = 2)**

1. 20 `N` · 2.5 `PMT` · 100 `FV`.
2. 5.1617 `I/Y`, `CPT` `PV` → −98.749; `STO` 1 (after `+|-`).
3. 6.1617 `I/Y`, `CPT` `PV` → −91.423; `STO` 2 (after `+|-`).
4. Duration: `(` `RCL` 1 `−` `RCL` 2 `)` `÷` `(` 2 `×` 95 `×` .005 `)` `=` → **7.712**.
5. Convexity: `(` `RCL` 1 `+` `RCL` 2 `−` 190 `)` `÷` `(` 95 `×` .005 `x²` `)` `=` → **72.4**.

**DV01:** 7.709 `×` 95 `×` .0001 `=` → 0.0732.

**WAL of amortizing loans:** the `AMORT` worksheet gives principal paid over any range of payments (P1 to P2). Group payments by year and weight by year for an approximate WAL; use Excel for exact monthly results.

### HP 12C

The 12C has no duration or convexity keys, so use repricing.

1. `f` `CLEAR FIN`; 20 `n` · 2.5 `PMT` · 100 `FV`.
2. 5.1617 `ENTER` 2 `÷` `i`, `PV` → −98.749; `CHS` `STO` 1.
3. 6.1617 `ENTER` 2 `÷` `i`, `PV` → −91.423; `CHS` `STO` 2.
4. Effective duration: `RCL` 1 `RCL` 2 `−` .95 `÷` → **7.712** (dividing by 2 × 95 × 0.005 = 0.95).
5. Effective convexity: `RCL` 1 `RCL` 2 `+` 190 `−` .002375 `÷` → **72.4** (95 × 0.005² = 0.002375).
6. Modified to Macaulay: 7.709 `ENTER` 1.028308 `×` → 7.927.

**WAL:** `f` `AMORT` after n payments shows interest, then `x≷y` shows principal paid, year by year (12 `f` `AMORT` repeatedly).

### Excel

| Measure | Formula | Result |
| --- | --- | --- |
| Macaulay duration | `=DURATION(DATE(2026,11,15),DATE(2036,11,15),5%,5.6617%,2,1)` | 7.927 |
| Modified duration | `=MDURATION(DATE(2026,11,15),DATE(2036,11,15),5%,5.6617%,2,1)` | 7.709 |
| Price at −50 bp | `=PRICE(DATE(2026,11,15),DATE(2036,11,15),5%,5.1617%,100,2,1)` | 98.749 |
| Effective duration | `=(P_minus-P_plus)/(2*95*0.005)` | 7.712 |
| Effective convexity | `=(P_minus+P_plus-2*95)/(95*0.005^2)` | 72.4 |
| DV01 per 100 | `=MDURATION(…)*95*0.0001` | 0.0732 |
| Mortgage WAL (Excel 365) | `=SUMPRODUCT(SEQUENCE(360)/12*PPMT(6%/12,SEQUENCE(360),360,-100000))/100000` | 19.31 |

Excel has no convexity function. Build a cash flow table (periods in A2:A21, cash flows in B2:B21, yield in E1, price in E2):

```
=SUMPRODUCT(B2:B21/(1+E1/2)^A2:A21*A2:A21*(A2:A21+1))/(E2*(1+E1/2)^2)/4
```

This mirrors the book's Spreadsheet 16.1, which builds duration cash flow by cash flow.

### Python

QuantLib (tested; output 7.927, 7.709, 72.41, −0.0732):

```python
import QuantLib as ql
settle = ql.Date(15, ql.November, 2026)
ql.Settings.instance().evaluationDate = settle
sched = ql.Schedule(settle, ql.Date(15, ql.November, 2036), ql.Period(ql.Semiannual),
                    ql.NullCalendar(), ql.Unadjusted, ql.Unadjusted,
                    ql.DateGeneration.Backward, False)
dc = ql.ActualActual(ql.ActualActual.Bond, sched)
bond = ql.FixedRateBond(0, 100.0, sched, [0.05], dc)
ytm = bond.bondYield(ql.BondPrice(95.0, ql.BondPrice.Clean), dc, ql.Compounded, ql.Semiannual)
rate = ql.InterestRate(ytm, dc, ql.Compounded, ql.Semiannual)
mac  = ql.BondFunctions.duration(bond, rate, ql.Duration.Macaulay)
mod  = ql.BondFunctions.duration(bond, rate, ql.Duration.Modified)
conv = ql.BondFunctions.convexity(bond, rate)
dv01 = ql.BondFunctions.basisPointValue(bond, rate)   # sign: price change for +1 bp
```

Plain NumPy, plus mortgage WAL with numpy-financial (tested):

```python
import numpy as np, numpy_financial as npf
y, t = 0.0566169, np.arange(1, 21)
cf = np.full(20, 2.5); cf[-1] += 100
pv = cf / (1 + y / 2) ** t; P = pv.sum()
mac  = (t * pv).sum() / P / 2                           # 7.927
mod  = mac / (1 + y / 2)                                # 7.709
conv = (pv * t * (t + 1)).sum() / (P * (1 + y / 2) ** 2) / 4   # 72.41

k = np.arange(1, 361)
prin = npf.ppmt(0.06 / 12, k, 360, -100_000)
wal = (k / 12 * prin).sum() / prin.sum()                # 19.31
```

### Julia

Plain Julia (same logic as the tested NumPy code; not run here):

```julia
y = 0.0566169; t = 1:20
cf = fill(2.5, 20); cf[end] += 100
pv = cf ./ (1 + y / 2) .^ t; P = sum(pv)
mac  = sum(t .* pv) / P / 2
modd = mac / (1 + y / 2)
conv = sum(pv .* t .* (t .+ 1)) / (P * (1 + y / 2)^2) / 4
```

`mod` is a built-in Julia function, hence `modd`. ActuaryUtilities.jl provides duration (Macaulay, modified, key rate) and convexity functions that take a yield or a fitted FinanceModels.jl curve.

## 11. Practice set

1. A 5-year 6% semiannual bond trades at par. Find Macaulay and modified duration and convexity. *4.393, 4.265, 21.77.*
2. Duration of a perpetuity at 8%? *Answer:* $`1.08 / 0.08 = 13.5`$ years.
3. Estimate the worked bond's price change for +50 bp with duration and convexity. Compare with the actual change. *Answer:* $`-7.709 \times 0.005 + \tfrac{1}{2} \times 72.41 \times 0.005^{2} = -3.764\%`$; actual −3.765%.
4. Immunize a 5-year liability using 2-year and 10-year zeros. Weights? *Answer:* $`w \times 2 + (1 - w) \times 10 = 5`$, so 62.5% in the 2-year and 37.5% in the 10-year.
5. A 10-year bond retires 25% of principal in each of years 7–10. WAL? *(7 + 8 + 9 + 10) ÷ 4 = 8.5 years.*
6. Why does a 30-year strip need more rebalancing in a DV01 hedge than a 10-year note? *Its convexity (875 vs 72) makes its DV01 change much faster as rates move.*
7. Why do MBS show negative convexity? *Falling rates speed up prepayments, returning principal at par just when the bond would rise above it.*

## 12. CFA-style review questions

Original questions in the CFA Level I format (three choices, one correct). Not CFA Institute material.

1. A bond has modified duration 7.0 and convexity 60. For a 100 bp rise in yield, the estimated price change is closest to:
   - A. −7.30%
   - B. −7.00%
   - C. −6.70%
2. Which bond has the highest duration?
   - A. a 10-year 8% coupon bond
   - B. a 10-year zero-coupon bond
   - C. a 5-year zero-coupon bond
3. The Macaulay duration of a level perpetuity yielding 5% is closest to:
   - A. 20 years
   - B. 21 years
   - C. 22 years
4. A bond priced at 100 falls to 98.20 when yields rise 50 bp and rises to 102.00 when yields fall 50 bp. Its effective duration is closest to:
   - A. 1.9
   - B. 3.8
   - C. 7.6
5. A \$5 million face position has modified duration 6.0 and a price of 98. Its DV01 is closest to:
   - A. \$2,940
   - B. \$3,000
   - C. \$29,400
6. When interest rates fall sharply, a callable bond's price is most likely to:
   - A. rise more than an otherwise identical option-free bond
   - B. rise less than an otherwise identical option-free bond
   - C. fall, because the call is exercised

**Answer key**

1. C. $`-7.0 \times 0.01 + \tfrac{1}{2} \times 60 \times 0.01^{2} = -7.00\% + 0.30\% = -6.70\%`$.
2. B. A zero's duration equals its maturity, the longest here.
3. B. $`1.05 / 0.05 = 21`$.
4. B. $`(102.00 - 98.20) / (2 \times 100 \times 0.005) = 3.8`$.
5. A. $`6.0 \times 98 \times 0.0001 = 0.0588`$ per 100; × 50,000 = \$2,940.
6. B. Negative convexity: the call caps price appreciation near the call price.

## 13. Bloomberg Terminal exercises (draft: verify on the campus Terminal)

| Command | What to do | Check against this guide | Verified |
| --- | --- | --- | --- |
| `CT10 Govt YAS <GO>` | Read modified duration, convexity and risk (DV01 per 100) | Sections 2, 4 and 8 | ☐ |
| `YAS <GO>`, hedge area | Set a hedge instrument (for example the current 30-year or a Treasury future) and read the hedge ratio | Section 9: DV01 hedging | ☐ |
| `OAS1 <GO>` | Open a callable bond; compare option-adjusted (effective) duration and convexity with the yield-based figures | Sections 5 and 8: effective duration, negative convexity | ☐ |
| `KRR <GO>` (confirm) | Key rate risk for a bond or portfolio | Section 6: key rate duration | ☐ |
| `PRTU <GO>`, then `PORT <GO>` | Build a small test portfolio (say 2-, 10- and 30-year Treasuries); read portfolio duration and key rate exposures | Section 6: portfolio duration | ☐ |
| `DES <GO>` on an agency MBS pool | Read weighted average life and prepayment speed (CPR); change the prepayment assumption and watch WAL | Section 7: WAL | ☐ |

Excel (confirm with `FLDS`): `=BDP("CT10 Govt","DUR_ADJ_MID")`, `=BDP("CT10 Govt","CONVEXITY_MID")`, `=BDP("CT10 Govt","RISK_MID")`.

**Exercise:** for \$10 million face of the current 10-year, compute DV01 from `RISK_MID`. Size a hedge in the current 30-year using the ratio of their DV01s, then compare your answer with the YAS hedge area.

## 14. Reading in Bodie, Kane & Marcus, *Investments*, 13th ed. (2024)

| Section | Topic in the book | Supports |
| --- | --- | --- |
| 16.1 Interest Rate Risk | Interest Rate Sensitivity; Duration; What Determines Duration? (Rules 1–5); Spreadsheet 16.1 | Sections 1–4 and the duration rules |
| 16.2 Convexity | Why Do Investors Like Convexity?; Duration and Convexity of Callable Bonds; Duration and Convexity of Mortgage-Backed Securities | Sections 5 and 8: convexity, effective duration, negative convexity |
| 16.3 Passive Bond Management | Bond-Index Funds; Immunization; Cash Flow Matching and Dedication; Other Problems with Conventional Immunization | Section 9: immunization and rebalancing |
| 16.4 Active Bond Management | Sources of Potential Profit; Horizon Analysis | Duration positioning |
| 14.5 Default Risk and Bond Pricing | Bond Indentures: Sinking Funds | WAL of sinking-fund bonds |
| 2.2 The Bond Market | Mortgage and Asset-Backed Securities | WAL and prepayment background |
| 20.5 Option-like Securities | Callable Bonds | Why callables have negative convexity |
| 23.3 Interest Rate Futures | Hedging Interest Rate Risk | DV01 hedging with futures |
| 23.4 Swaps | Swaps and Balance Sheet Restructuring | Changing portfolio duration with swaps |

Chapter 16's end-of-chapter problems and CFA problems give extensive duration, convexity and immunization practice. Weighted average life is not a named topic in the book; it comes up through sinking funds and mortgage-backed securities.
