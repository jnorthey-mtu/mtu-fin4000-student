# Mini Study Guide 12: Flat Rate vs. Term Structure

*Pricing a Bond and Backing Out Its YTM (BKM Ch. 14 & 15)*

[← All study guides](../../study-guide-index.md)

## Learning objectives

By the end of this guide, students can explain which direction a bond calculation runs, and so decide whether the annuity form or cash-flow-by-cash-flow discounting applies.

1. Explain that with a flat rate the YTM produces the price, while with a term structure the spot rates produce the price and the YTM is backed out afterward.
2. Price a bond from spot rates, then solve for its YTM and show that no cash flow was actually discounted at that YTM.
3. Explain the coupon effect and why STRIPS arbitrage tests must use spot rates, not YTM.
4. State the conditions under which the annuity form matches discounting every cash flow, and price such a bond with the BA II Plus TVM keys.

## The main idea: two directions of calculation

With a flat rate, the calculation runs from YTM to price. With a term structure it runs the other way: spot rates set the price, and the YTM is a summary number backed out afterward.

| | Flat-rate world | Term-structure world |
| --- | --- | --- |
| Starting point | One YTM | One spot rate per maturity |
| Discounting | Every cash flow at the same y | Each cash flow at its own spot rate |
| Price | Output (annuity form or TVM keys) | Output (sum of separately discounted cash flows) |
| YTM | Input | Output: the single rate that gives the same price |
| BA II Plus | TVM keys (N, I/Y, PMT, FV) | Discount each term by hand; use TVM only to back out the YTM |

```math
\text{Flat rate: } y \rightarrow P \qquad\qquad \text{Term structure: } s_1, s_2, \dots \rightarrow P \rightarrow y
```

**Example.** A 2-year, 5% annual-coupon bond, par \$1,000, with spot rates of 4% (1-year) and 6% (2-year). Discounting each cash flow at its own spot rate gives a price of \$982.57. Solving for the single rate that reproduces that price gives a YTM of about 5.95%. No cash flow was discounted at 5.95%: it is a blend of 4% and 6%, and it sits close to 6% because about 95% of the bond's present value arrives in year 2. The full steps are in Examples 2 and 3 below.

**Why this matters for students:**

- **The YTM depends on the bond, not just the curve.** A 2-year zero on this curve has a YTM of 6.00%, while the 5% coupon bond has about 5.95%. The coupon bond puts more weight on the 4% year-1 rate. This is the coupon effect.
- **Spot rates are the true discount rates.** They are zero-coupon yields and do not depend on any coupon. That is why an arbitrage test, such as a coupon bond versus its STRIPS, must use spot rates: if the bond's price differs from the sum of its cash flows discounted at spot rates, an arbitrage exists.
- **YTM is a shorthand, not a discount rate.** It is the internal rate of return from buying and holding to maturity, and it implicitly assumes coupons are reinvested at that same rate. Spot-rate pricing makes no reinvestment assumption: it is a present value. If coupons are instead reinvested at the implied forward rates, the bond earns exactly the spot rate (6.00%, not 5.95%, in this example; see Example 6).

**One-line takeaway:** with a flat curve, YTM → price; with a curve, spot rates → price → YTM.

## When the annuity form applies

The annuity form is only a shortcut: it is the algebraic sum of the discounted coupons, so it returns exactly the same price as discounting each cash flow whenever it applies.

```math
P = C \cdot \frac{1 - (1+y)^{-n}}{y} + \frac{F}{(1+y)^{n}}
```

**Use the annuity form when all five conditions hold:**

- Every coupon is the same amount (fixed-rate, non-amortizing).
- Coupons are evenly spaced, and the first is a full period away.
- One constant discount rate (the YTM) applies to every cash flow.
- Rate and period match: semiannual coupons use y/2 and n = 2 × years.
- Par is repaid once at maturity and is discounted separately, outside the annuity.

**Discount each cash flow separately when any one of these holds:**

| Situation | Why the annuity form fails | Typical exam context |
| --- | --- | --- |
| Different discount rate for each maturity | No single y to factor out | Spot rates, yield curve, STRIPS arbitrage (Ch. 15) |
| Coupons change over time | Payment is not a constant C | Step-up, floating, amortizing bonds |
| Irregular timing | First cash flow is not one full period away | Settlement between coupon dates |
| Embedded options or extra cash flows | Cash flows are not fixed | Callable bonds, sinking funds |

**BA II Plus link.** The TVM keys (N, I/Y, PMT, FV) are the annuity formula, so they work only when the five conditions hold. For uneven cash flows or different rates, use the CF worksheet and discount each flow by hand.

## Worked examples

**Example 1: annuity form applies.** A 10-year, 8% semiannual-coupon bond, par \$1,000, YTM 6% (BEY). Price it.

All five conditions hold, so use the TVM keys. Semiannual: n = 20, y/2 = 3%, C = \$40.

```math
P = 40 \cdot \frac{1 - 1.03^{-20}}{0.03} + \frac{1000}{1.03^{20}} = \$1{,}148.77
```

- BA II Plus: 2nd [CLR TVM], N = 20, I/Y = 3, PMT = 40, FV = 1000, CPT PV = −1,148.77.

**Example 2: spot rates, so discount each cash flow.** A 2-year, 5% annual-coupon bond, par \$1,000. Spot rates: 1-year 4%, 2-year 6%.

Each cash flow gets its own rate, so there is no single y and the annuity form does not apply.

```math
P = \frac{50}{1.04} + \frac{1050}{1.06^{2}} = 48.08 + 934.50 = \$982.57
```

- BA II Plus: do not use the TVM keys or the NPV function, because both apply one rate to every cash flow. Compute each term directly: 50 ÷ 1.04, then 1050 ÷ 1.06 ÷ 1.06 (or 1.06 [y^x] 2 [1/x] × 1050), and add them.

**Example 3: back out the YTM.** Using the price from Example 2, find the single rate that equates it to the cash flows.

```math
982.57 = \frac{50}{1+y} + \frac{1050}{(1+y)^{2}} \;\Rightarrow\; y \approx 5.95\%
```

- BA II Plus: 2nd [CLR TVM], N = 2, PMT = 50, FV = 1000, PV = −982.57, CPT I/Y = 5.95.
- No cash flow was discounted at 5.95%. It is a blend of 4% and 6%, and it sits close to 6% because about 95% of the bond's present value arrives in year 2.

**Example 4: the coupon effect.** Both securities below are priced off the same curve, yet their YTMs differ.

| Security | Price | YTM |
| --- | --- | --- |
| 2-year zero, par \$1,000 | \$890.00 | 6.00% |
| 2-year 5% coupon bond (Example 2) | \$982.57 | 5.95% |

The coupon bond pays part of its value in year 1, where the spot rate is only 4%, so its blended YTM is pulled below the zero's. Spot rates do not depend on the coupon; YTM does.

**Example 5: STRIPS arbitrage.** The bond from Example 2 trades at \$970. Its stripped value is the sum of its cash flows discounted at spot rates, \$982.57.

1. Buy the bond at \$970.
2. Strip it, selling a \$50 one-year zero and a \$1,050 two-year zero at spot-rate prices, which brings in \$982.57.
3. Profit: \$982.57 − \$970.00 = \$12.57 per bond, with no risk.

The test must use spot rates. Comparing the bond's YTM to some other bond's YTM would not reveal this.

**Example 6: the reinvestment assumption.** Same 2-year, 5% bond: price \$982.57, YTM 5.95%, spot rates 4% and 6%. The implied forward rate for year 2 is 1.06² ÷ 1.04 − 1 = 8.04%. Suppose you buy the bond and hold it to maturity, reinvesting the \$50 year-1 coupon at different rates.

| Reinvest year-1 coupon at | Value at year 2 | Annualized realized return |
| --- | --- | --- |
| 5.95% (the YTM) | \$1,102.97 | 5.95% |
| 8.04% (the forward rate) | \$1,104.02 | 6.00% |
| 5.00% | \$1,102.50 | 5.93% |

```math
\text{Realized return} = \left(\frac{\text{Value at year 2}}{982.57}\right)^{1/2} - 1
```

- BA II Plus: 2nd [CLR TVM], N = 2, PV = −982.57, PMT = 0, FV = 1104.02, CPT I/Y = 6.00.
- Pricing with spot rates assumed no reinvestment at all. The YTM equals the realized return only if the coupon is reinvested at the YTM itself.
- Reinvesting at the forward rate makes the bond earn exactly the 2-year spot rate. That is why forward rates (Ch. 15) are the market-implied reinvestment rates.

## Common pitfalls

- **Treating YTM as the discount rate for every cash flow** when the curve is not flat. With a term structure, spot rates discount; YTM is only a summary.
- **Using the TVM keys with spot rates.** I/Y is one rate, so the keys cannot price a bond off a yield curve.
- **Forgetting to discount par separately.** The annuity factor covers coupons only; add F ÷ (1+y)^n.
- **Mismatching rate and period.** For semiannual coupons use y/2 and n = 2 × years. A 4-year 6% semiannual bond at 8% BEY is N = 8, I/Y = 4, PMT = 30, not N = 4, I/Y = 8.
- **Applying the annuity factor to a stub period.** If the first coupon is less than a full period away, the standard formula no longer fits.
- **Using YTM to test for arbitrage.** Compare the bond's price to the sum of its cash flows discounted at spot rates, as in the STRIPS example.
- **Assuming two bonds on the same curve share a YTM.** The coupon effect gives them different YTMs.

## Key-terms checklist

- [ ] Annuity form (present value of a level coupon stream plus discounted par)
- [ ] Level-coupon, non-amortizing bond
- [ ] Yield to maturity (single rate that equates price to discounted cash flows)
- [ ] Spot rate (yield on a zero-coupon bond of that maturity)
- [ ] Term structure / yield curve
- [ ] Coupon effect
- [ ] STRIPS and stripping a coupon bond
- [ ] Arbitrage (price differs from sum of discounted cash flows)
- [ ] Bond-equivalent yield and rate-period matching
- [ ] Reinvestment-rate assumption behind YTM

## Practice questions

Eight CFA-style questions: five algorithmic (Q2, Q3, Q5, Q6, Q8) and three conceptual (Q1, Q4, Q7). Par value is \$1,000 throughout.

**Q1.** Which bond can be priced exactly with the annuity form using a single YTM?

- A. A 7-year, 5% annual-coupon bond with a stated YTM
- B. A bond whose cash flows are discounted at spot rates of 3%, 4% and 5%
- C. A 5-year bond whose coupon steps up every year

**Q2.** A 5-year bond pays a 6% annual coupon and has a YTM of 7%. Its price is closest to:

- A. \$1,041.00
- B. \$959.00
- C. \$1,000.00

**Q3.** A 3-year bond pays a 4% annual coupon. The spot rates are 3% (1-year), 4% (2-year) and 5% (3-year). The bond's price is closest to:

- A. \$863.84
- B. \$1,000.00
- C. \$974.21

**Q4.** With the same spot rates as Q3, the YTM of the 3-year 4% coupon bond is most likely:

- A. Below 5.00%
- B. Above 5.00%
- C. Equal to 5.00%

**Q5.** A 2-year, 5% annual-coupon bond trades at \$970. The 1-year and 2-year spot rates are 4% and 6%. Buying the bond and selling its cash flows as STRIPS earns a riskless profit per bond closest to:

- A. \$17.43
- B. \$12.57
- C. \$0.00

**Q6.** A 4-year bond pays a 6% coupon semiannually and has a bond-equivalent yield of 8%. Its price is closest to:

- A. \$933.76
- B. \$712.67
- C. \$932.67

**Q7.** Which statement is correct?

- A. A coupon bond's YTM always equals the spot rate for its maturity.
- B. Two bonds priced from the same spot curve can have different YTMs.
- C. The TVM keys can price a bond when each cash flow has its own spot rate.

**Q8.** A 2-year, 5% annual-coupon bond is priced at \$982.57 from spot rates of 4% (1-year) and 6% (2-year). An investor holds it to maturity and reinvests the year-1 coupon at the implied 1-year forward rate for year 2 (8.04%). The annualized realized return is closest to:

- A. 5.95%
- B. 6.00%
- C. 8.04%

## Answer key

| Q | Answer | Explanation |
| --- | ------ | ------------------------------------------------------ |
| 1 | A | Level coupon, even spacing, one YTM: all five conditions hold. B needs a separate spot rate per cash flow. C has a changing coupon, so there is no constant C. |
| 2 | B | Coupon (6%) is below YTM (7%), so the bond sells at a discount. BA II Plus: N = 5, I/Y = 7, PMT = 60, FV = 1000, CPT PV = −959.00. |
| 3 | C | 40/1.03 + 40/1.04² + 1040/1.05³ = 38.83 + 36.98 + 898.39 = \$974.21. Each cash flow uses its own spot rate. \$863.84 is the price of a 3-year zero, which ignores the coupons. |
| 4 | A | The 3-year zero has a YTM of 5.00%. The coupon bond pays part of its value earlier, at lower spot rates, so its YTM is pulled below 5%. Solving gives about 4.95%. This is the coupon effect. |
| 5 | B | Stripped value = 50/1.04 + 1050/1.06² = \$982.57. Profit = 982.57 − 970 = \$12.57. \$17.43 is par minus stripped value, which is not a cash flow in this trade. |
| 6 | C | Semiannual: N = 8, I/Y = 4, PMT = 30, FV = 1000, CPT PV = −932.67. A uses annual periods (N = 4, I/Y = 8, PMT = 60), which gives \$933.76. B uses N = 8 with I/Y = 8, which gives \$712.67. |
| 7 | B | A zero and a coupon bond on the same curve have different YTMs (6.00% vs. 5.95% in Example 4). A is false for coupon bonds. C is false: I/Y is one rate, so the keys cannot discount at different spot rates. |
| 8 | B | Value at year 2 = 50 × 1.0804 + 1,050 = \$1,104.02. Realized return = (1,104.02 ÷ 982.57)^(1/2) − 1 = 6.00%, the 2-year spot rate. A (5.95%) is the YTM, which would require reinvesting at 5.95%. C (8.04%) is the forward rate for year 2 alone, not the return on the whole investment. |
