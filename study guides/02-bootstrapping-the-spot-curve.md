# Study Guide 2: Bootstrapping the Spot Curve

*Fixed Income Study Guides*

[← All study guides](README.md)

Bootstrapping extracts zero-coupon (spot) rates from coupon bond prices, one maturity at a time. Each step prices the earlier cash flows with rates already found, leaving a single unknown to solve.

## 1. The idea

- A coupon bond is a bundle of zeros. Its price equals the sum of each cash flow times the discount factor for its date.
- The shortest bond has one cash flow, so it gives the first rate directly.
- Each longer bond adds exactly one new date. Subtract the value of its known earlier cash flows and solve for the new date's discount factor.

## 2. Core formulas

Price as a sum of discounted cash flows, with $DF_k$ the discount factor for period $k$:

$$P_n = \frac{c}{2}\sum_{k=1}^{n} DF_k + 100\,DF_n$$

Solved for the new discount factor (the bootstrap step):

$$DF_n = \frac{P_n - \frac{c}{2}\sum_{k=1}^{n-1} DF_k}{100 + \frac{c}{2}}$$

Spot rate from a discount factor (semiannual compounding):

$$s_n = 2\left[DF_n^{-1/n} - 1\right]$$

Forward rate for the period from $n-1$ to $n$:

$$f_{n-1,n} = 2\left[\frac{DF_{n-1}}{DF_n} - 1\right]$$

Working in discount factors is simpler than working in spot rates: every step is linear until the final conversion.

## 3. Example A: annual coupons

Three par bonds (price 100), annual coupons, used only to show the logic.

| Maturity | Coupon | Known cash flows valued at | Remaining value | Spot rate |
| --- | --- | --- | --- | --- |
| 1 yr | 3% | none | 100 | 3.00% |
| 2 yr | 4% | 4 ÷ 1.03 = 3.883 | 96.117 | 4.02% |
| 3 yr | 5% | 4.854 + 4.621 = 9.475 | 90.525 | 5.07% |

The 3-year step:

$$(1 + s_3)^{3} = \frac{105}{90.525} = 1.1599 \quad\Rightarrow\quad s_3 = 5.07\%$$

## 4. Example B: semiannual coupons (Treasury convention)

Four par bonds, coupons paid twice a year, rates annualized with semiannual compounding.

| Maturity | Coupon (annual) | Paid per period | Earlier coupons valued at | Discount factor | Spot rate | Forward rate for that period |
| --- | --- | --- | --- | --- | --- | --- |
| 0.5 yr | 4.0% | 2.00 | none | 0.980392 | 4.0000% | 4.0000% |
| 1.0 yr | 4.2% | 2.10 | 2.0588 | 0.959267 | 4.2021% | 4.4044% |
| 1.5 yr | 4.4% | 2.20 | 4.2673 | 0.936719 | 4.4059% | 4.8143% |
| 2.0 yr | 4.6% | 2.30 | 6.6157 | 0.912848 | 4.6117% | 5.2302% |

Step for 2.0 years: remaining value = 100 − 6.6157 = 93.3843. Then

$$\left(1 + \frac{s}{2}\right)^{4} = \frac{102.30}{93.3843} = 1.095473 \quad\Rightarrow\quad s = 4.6117\%$$

Check: the 2-year discount factors reprice the 4.6% bond at exactly 100.

## 5. Par, spot and forward curves

- **Par curve:** the coupon at which a bond of each maturity prices at 100. This is what most people mean by "the yield curve."
- **Spot curve:** the zero-coupon rate for each date. A par yield is a weighted blend of spot rates.
- **Forward curve:** the rate implied for each future period. Spot rates are geometric averages of forwards.
- Upward-sloping curve: forward > spot > par at longer maturities, as in Example B (5.23% > 4.61% > 4.60% at 2 years). Inverted curve: the order flips. Flat curve: all three coincide.

## 6. In practice

- **Inputs:** Treasury bills at the short end, then notes and bonds. Many desks prefer off-the-run issues, because on-the-run issues carry a liquidity premium.
- **Gaps:** bonds rarely mature on every date needed. Fill them by interpolation (linear on spot rates, or log-linear on discount factors), or fit a smooth curve.
- **Fitted models:** Nelson-Siegel and Svensson describe the whole curve with 4–6 parameters. They are smoother but no longer reprice every bond exactly.
- **Day counts:** real Treasury periods follow Actual/Actual, so periods are not exactly 0.5 years. Settlement between coupon dates requires accrued interest and fractional periods.
- **Error propagation:** a bad short-end price flows into every longer rate.
- **Other inputs:** swap and SOFR curves are bootstrapped the same way from deposits, futures and swaps.

## 7. Review questions

1. Why does the bootstrap start at the shortest maturity? *Its bond has a single cash flow, so its rate is known directly.*
2. Using Example B's discount factors, price a 1.5-year 5% bond. *Answer:* $2.5 \times (0.980392 + 0.959267 + 0.936719) + 100 \times 0.936719 = 7.192 + 93.672 = 100.86$.
3. From Example B, what is the forward rate from 1.0 to 1.5 years? *Answer:* $2 \times (0.959267 / 0.936719 - 1) = 4.81\%$.
4. When would the spot curve lie below the par curve? *When the curve is inverted.*
5. Why does a fitted Nelson-Siegel curve not reprice every bond exactly? *It trades exact fit for smoothness, which filters out noise from individual bonds.*

## 8. CFA-style review questions

Original questions in the CFA Level I format (three choices, one correct). Not CFA Institute material. Assume annual compounding.

1. The 1-year spot rate is 3.00%. A 2-year, 4% annual-coupon bond trades at par. The 2-year spot rate is closest to:
   - A. 4.00%
   - B. 4.02%
   - C. 4.04%
2. The 1-year spot rate is 3% and the 2-year spot rate is 4%. The 1-year forward rate one year from now is closest to:
   - A. 4.50%
   - B. 5.01%
   - C. 6.00%
3. Using spot rates of 3% (1 year) and 4% (2 years), the price of a 2-year 5% annual-coupon bond is closest to:
   - A. 101.93
   - B. 101.89
   - C. 102.00
4. When the par yield curve slopes upward, the spot curve at longer maturities is:
   - A. below the par curve
   - B. above the par curve
   - C. identical to the par curve
5. Valuing a bond with spot rates rather than its own yield to maturity is preferred because:
   - A. it gives an arbitrage-free value consistent with stripping and reconstitution
   - B. spot rates are always lower than yields to maturity
   - C. it removes interest rate risk from the valuation

**Answer key**

1. B. $100 = 4/1.03 + 104/(1 + s_2)^{2}$, so $s_2 = 4.02\%$.
2. B. $1.04^{2} / 1.03 - 1 = 5.01\%$.
3. A. $5/1.03 + 105/1.04^{2} = 4.854 + 97.078 = 101.93$.
4. B. A par yield blends lower short-term spot rates, so it sits below the long spot rate.
5. A. Each cash flow is priced at its own date's rate, so no stripping profit is possible.

## 9. Bloomberg Terminal exercises (draft: verify on the campus Terminal)

| Command | What to do | Check against this guide | Verified |
| --- | --- | --- | --- |
| `CRVF <GO>` | Curve finder: locate the U.S. Treasury actives curve and its zero (spot) version | Section 5: par vs spot curves | ☐ |
| `GC <GO>` | Plot par, zero and forward versions of the Treasury curve on one chart | Upward-sloping curve: forward > spot > par | ☐ |
| `ICVS <GO>` | Curve builder: view the instruments behind the curve and its zero rates and discount factors | Sections 2 and 6: inputs, interpolation | ☐ |
| `FWCV <GO>` | Forward curve analysis | Section 2: forward rate formula | ☐ |
| `BDS` in Excel | Pull the curve's members, e.g. `=BDS("YCGT0025 Index","CURVE_TENOR_RATES")` (confirm the curve ticker in `CRVF`) | Inputs for the Excel bootstrap in Study Guide 3 | ☐ |

**Exercise:** take the 6-month, 1-year, 1.5-year and 2-year Treasury yields from the Terminal, bootstrap them with the Excel layout from Study Guide 3, and compare your spot rates with the Terminal's zero curve. Differences should be small; explain them (interpolation method, day counts, bills vs coupon securities at the short end).

## 10. Reading in Bodie, Kane & Marcus, *Investments*, 13th ed. (2024)

| Section | Topic in the book | Supports |
| --- | --- | --- |
| 15.1 The Yield Curve | Bond Pricing | Spot rates and pricing coupon bonds off the zero curve; the foundation for bootstrapping |
| 15.2 The Yield Curve and Future Interest Rates | The Yield Curve under Certainty; Holding-Period Returns; Forward Rates | Deriving forward rates from spot rates |
| 15.3 Interest Rate Uncertainty and Forward Rates | | Forwards vs expected future rates; term premium |
| 15.4 Theories of the Term Structure | Expectations Hypothesis; Liquidity Preference; Market Segmentation | Why the curve slopes as it does |
| 15.5 Interpreting the Term Structure | | Reading the curve's shape |
| 15.6 Forward Rates as Forward Contracts | | Locking in forward rates with zeros |
| 14.2 Bond Pricing | Bond Pricing between Coupon Dates | Fractional periods and accrued interest |

The book builds the zero curve and forwards but gives the step-by-step bootstrap only lightly; this guide's worked examples fill that gap.
