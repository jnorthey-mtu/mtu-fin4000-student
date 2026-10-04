# Study Guide 4: Measures of Yield

*Fixed Income Study Guides*

[← All study guides](../../study-guide-index.md)

Each yield measure answers a different question. Coupon yield answers what the bond promises per year on its face value. Current yield answers what it pays in cash on today's price. Yield to maturity answers what it returns if held to maturity. Real yield answers what that return is worth after inflation.

Worked bond used throughout: 10-year Treasury-style note, 5% coupon paid semiannually, price 95 (clean), settles Nov 15 2026, matures Nov 15 2036, face 100.

## 1. Nominal yield: two meanings

"Nominal" is used two ways, and exam questions exploit the ambiguity.

- **Nominal yield = coupon rate.** The annual coupon divided by face value. It never changes after issue. Example: 5.00%.
- **Nominal vs real.** Any yield stated in dollars, with no inflation adjustment. A 5.66% YTM is a nominal yield in this sense.
- A third use: an annual rate quoted with more frequent compounding (5.66% compounded semiannually) is a "nominal annual rate," as opposed to the effective annual rate.

```math
\text{Coupon (nominal) yield} = \frac{C}{F}
```

## 2. Current yield

Annual coupon divided by current price. It measures cash income only.

```math
CY = \frac{C}{P} = \frac{5}{95} = 5.263\%
```

- **Use:** income-focused investors comparing cash payout; quick screen.
- **Blind spots:** ignores the gain or loss as price pulls to par, ignores the timing of cash flows and reinvestment, and is meaningless for zeros (CY = 0).

## 3. Yield to maturity (YTM)

The single discount rate that sets the present value of all promised cash flows equal to the price. It is the bond's internal rate of return.

```math
P = \sum_{k=1}^{n} \frac{C/2}{\left(1 + \frac{y}{2}\right)^{k}} + \frac{F}{\left(1 + \frac{y}{2}\right)^{n}}
```

For the worked bond:

```math
95 = \sum_{k=1}^{20} \frac{2.5}{\left(1 + \frac{y}{2}\right)^{k}} + \frac{100}{\left(1 + \frac{y}{2}\right)^{20}} \quad\Rightarrow\quad y = 5.662\%
```

There is no closed form; it is solved by iteration.

Between coupon dates, use the dirty (full) price and a fractional first period, where $`w`$ = days to next coupon ÷ days in the coupon period:

```math
P_{dirty} = \sum_{k=1}^{n} \frac{CF_k}{\left(1 + \frac{y}{2}\right)^{k-1+w}}
```

**Assumptions built into YTM:**

1. The bond is held to maturity.
2. Every payment is made on time (no default).
3. Every coupon is reinvested at the YTM itself.

**Nuances:**

- YTM is a blend of spot rates weighted by the bond's cash flows. Two bonds with the same maturity but different coupons can have different YTMs (the coupon effect). Price off spot rates, not off another bond's YTM.
- It is a promised yield, not an expected one. For risky credit, expected return is lower.
- Ordering rule for all bonds: discount bond → coupon < CY < YTM (5.00 < 5.26 < 5.66). Premium bond → coupon > CY > YTM. Par bond → all three are equal.

## 4. Yield to call and yield to worst

Same equation, with the call date as maturity and the call price as the final payment.

```math
P = \sum_{k=1}^{n_c} \frac{C/2}{\left(1 + \frac{y_c}{2}\right)^{k}} + \frac{CP}{\left(1 + \frac{y_c}{2}\right)^{n_c}}
```

- **Yield to worst (YTW):** the lowest of YTM and the yield to every call date. It is the standard quote for callable bonds.
- Example: the 5% note at a premium price of 105, callable in 5 years at 101. YTM = 4.377%, YTC = 4.067%, so **YTW = 4.067%**. Premium callables usually yield to the call.
- Callable bonds are properly valued with option-adjusted spread (OAS) models. YTW is a quoting convention, not a valuation.

## 5. Realized (horizon) yield

The return actually earned, given an assumed reinvestment rate $`r`$ and holding period. It fixes the third YTM assumption.

```math
FV = \sum_{k=1}^{n} \frac{C}{2}\left(1 + \frac{r}{2}\right)^{n-k} + F \qquad y_{realized} = 2\left[\left(\frac{FV}{P}\right)^{1/n} - 1\right]
```

Example: the worked bond held to maturity with coupons reinvested at 3%. $`FV = 157.81`$, so **realized yield = 5.140%**, not 5.662%. The gap is reinvestment risk. A zero has none: its YTM is its realized yield.

## 6. Compounding conventions

| Measure | Definition | Worked bond | Used for |
| --- | --- | --- | --- |
| Bond-equivalent yield (BEY) | Semiannual rate × 2 | 5.662% | US Treasury and corporate quotes |
| Effective annual yield (EAY) | (1 + BEY/2)² − 1 | 5.742% | Comparing with annual-pay bonds (Bunds, most Eurobonds) and other investments |

```math
EAY = \left(1 + \frac{BEY}{2}\right)^{2} - 1 \qquad BEY = 2\left[(1 + EAY)^{1/2} - 1\right]
```

Never compare yields quoted on different compounding bases. T-bills add two more conventions: the bank discount yield (on face value, 360-day year) and the investment yield (on price, 365-day year).

## 7. Real yield

The return after inflation. The Fisher relation links nominal yield $`i`$, real yield $`r`$ and inflation $`\pi`$:

```math
(1 + i) = (1 + r)(1 + \pi) \qquad r = \frac{1 + i}{1 + \pi} - 1 \approx i - \pi
```

Example: nominal 4.5%, inflation 2.5%. Exact real yield $`= 1.045 / 1.025 - 1 = 1.951\%`$; the approximation gives 2.0%. The gap grows when rates are high.

- **Ex-ante vs ex-post:** real yield computed from expected inflation is a forecast; from realized inflation it is a result.
- **TIPS real yield:** the YTM of a TIPS computed from its real (quoted) price and real coupon. It is the market-observed real rate. Same formula as section 3.
- **Breakeven inflation:** the inflation rate that equalizes a nominal Treasury and a TIPS of the same maturity.

```math
\pi_{BE} = \frac{1 + i_{nominal}}{1 + r_{TIPS}} - 1 \approx i_{nominal} - r_{TIPS}
```

Example: nominal 4.30%, TIPS 2.00%, breakeven ≈ 2.30%. Breakeven is a rough, not pure, inflation forecast. It also contains an inflation risk premium, the TIPS liquidity discount, the 3-month CPI lag and the deflation floor's value.

## 8. Summary: which yield for which question

| Measure | Answers | Best use | Main blind spot |
| --- | --- | --- | --- |
| Coupon (nominal) yield | Promised cash per 100 face | Describing the bond | Ignores price |
| Current yield | Cash income on money invested | Income screening | Ignores pull to par and timing |
| YTM | IRR if held to maturity | Standard quote; comparing non-callable bonds | Assumes reinvestment at YTM |
| YTC / YTW | Return if called on the worst date | Quoting callable bonds | Not a valuation of the call option |
| Realized yield | Return under your reinvestment and horizon assumptions | Planning and scenario analysis | Depends on assumptions |
| EAY | Yield with annual compounding | Cross-market comparison | Not the US quoting convention |
| Real yield | Return in purchasing power | Long-horizon, inflation-linked goals | Expected inflation is uncertain |

One more adjustment for munis:

```math
\text{Tax-equivalent yield} = \frac{\text{Tax-exempt yield}}{1 - t_{marginal}}
```

## 9. Tools: the worked bond on every platform

Targets: CY 5.263% · YTM 5.662% · EAY 5.742% · YTC (premium case, price 105, call at 101 in 5 years) 4.067% · real yield 1.951%.

### TI BA II Plus Professional

**YTM with TVM** (P/Y = C/Y = 2 set via `2nd` `P/Y`)

1. `2nd` `CLR TVM`.
2. 20 `N` · 95 `+|-` `PV` · 2.5 `PMT` · 100 `FV`.
3. `CPT` `I/Y` → **5.662**.

**YTM with the Bond worksheet**

1. `2nd` `BOND`, `2nd` `CLR WORK`.
2. SDT = 11.1526 ↓ CPN = 5 ↓ RDT = 11.1536 ↓ RV = 100 ↓ ACT ↓ 2/Y ↓
3. ↓ to PRI, enter 95 `ENTER`, then ↑ to YLD and `CPT` → **5.662**. DUR shows modified duration.

**Yield to call:** in the Bond worksheet set RDT = 11.1531 and RV = 101, enter PRI = 105, `CPT` YLD → **4.067**.

**BEY to EAY with ICONV**

1. `2nd` `ICONV`.
2. NOM = 5.662 `ENTER` ↓ ↓ C/Y = 2 `ENTER`.
3. ↑ to EFF, `CPT` → **5.742**. Reverse the steps to go from EFF to NOM.

**Current and real yield (arithmetic):** 5 `÷` 95 `×` 100 `=` → 5.263. Real: 1.045 `÷` 1.025 `−` 1 `=` → 0.01951.

### HP 12C

**YTM with TVM**

1. `f` `CLEAR FIN`.
2. 20 `n` · 95 `CHS` `PV` · 2.5 `PMT` · 100 `FV`.
3. `i` → 2.831 per half-year, then 2 `×` → **5.662**.

**YTM with bond functions** (`g` `M.DY` for US dates)

1. 95 `PV` · 5 `PMT`.
2. 11.152026 `ENTER` 11.152036 `f` `YTM` → **5.662**.

**Yield to call:** the 12C bond functions assume redemption at 100, so use TVM: 10 `n` · 105 `CHS` `PV` · 2.5 `PMT` · 101 `FV` · `i` 2 `×` → **4.067**.

**BEY to EAY (RPN):** .05662 `ENTER` 2 `÷` 1 `+` 2 `yˣ` 1 `−` → 0.05742.

**Current and real yield:** 5 `ENTER` 95 `÷` → 0.05263. 1.045 `ENTER` 1.025 `÷` 1 `−` → 0.01951.

### Excel

| Measure | Formula | Result |
| --- | --- | --- |
| Current yield | `=5%*100/95` | 5.263% |
| YTM, date-based | `=YIELD(DATE(2026,11,15),DATE(2036,11,15),5%,95,100,2,1)` | 5.662% |
| YTM, period-based | `=2*RATE(20,2.5,-95,100)` | 5.662% |
| Yield to call | `=YIELD(DATE(2026,11,15),DATE(2031,11,15),5%,105,101,2,1)` | 4.067% |
| BEY to EAY | `=EFFECT(5.662%,2)` | 5.742% |
| EAY to BEY | `=NOMINAL(5.742%,2)` | 5.662% |
| Real yield (Fisher) | `=(1+4.5%)/(1+2.5%)-1` | 1.951% |
| Realized yield, 3% reinvestment | `=2*(((-FV(1.5%,20,2.5)+100)/95)^(1/20)-1)` | 5.140% |

`YIELD` arguments: settlement, maturity, coupon rate, price, redemption, frequency (2), basis (1 = Actual/Actual). For TIPS, use the real clean price and real coupon: the result is the real yield.

### Python

Plain Python with numpy-financial, then QuantLib with real dates and day counts (tested; both return 0.056617):

```python
import numpy_financial as npf
ytm = 2 * npf.rate(20, 2.5, -95, 100)          # 0.056617
cy  = 5 / 95                                    # 0.052632
eay = (1 + ytm / 2) ** 2 - 1                    # 0.057418
real = 1.045 / 1.025 - 1                        # 0.019512

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
eay = rate.equivalentRate(ql.Compounded, ql.Annual, 1.0).rate()   # 0.057418
```

- `scipy.optimize.brentq` solves any yield equation you write yourself, such as YTC or realized yield.
- QuantLib's `CPIBond` handles TIPS with an inflation index; `BondFunctions` adds duration and convexity.
- rateslib's bond objects also return YTM directly; check its licence before commercial use (Study Guide 3).

### Julia

Plain Julia, no packages (logic mirrors the tested Python; not run here). Bisection works because price falls as yield rises:

```julia
function ytm(price, cpn, n; freq = 2)
    f(y) = sum(cpn / freq / (1 + y / freq)^k for k in 1:n) + 100 / (1 + y / freq)^n - price
    lo, hi = 0.0, 1.0
    for _ in 1:100
        mid = (lo + hi) / 2
        f(mid) > 0 ? (lo = mid) : (hi = mid)
    end
    (lo + hi) / 2
end

y    = ytm(95.0, 5.0, 20)          # 0.056617
cy   = 5 / 95
eay  = (1 + y / 2)^2 - 1
real = 1.045 / 1.025 - 1
```

- In the JuliaActuary ecosystem, FinanceCore.jl rate types convert compounding directly, for example `convert(Periodic(1), Periodic(0.05662, 2))` for BEY to EAY. Its `irr` function solves yields from cash flows and times.
- Roots.jl `find_zero` is the general-purpose replacement for the bisection loop.

## 10. Practice set

1. An 8-year 7% semiannual bond trades at 108. Find CY, YTM and EAY. *6.481%, 5.739%, 5.821%.*
2. Check the ordering rule on question 1. *Premium bond: coupon 7% > CY 6.48% > YTM 5.74%.*
3. Nominal yield 6.0%, expected inflation 3.5%. Exact real yield? *Answer:* $`1.06 / 1.035 - 1 = 2.415\%`$.
4. A 10-year Treasury yields 4.30% and the 10-year TIPS 2.00%. Exact breakeven? *Answer:* $`1.043 / 1.02 - 1 = 2.255\%`$.
5. Why is the worked bond's realized yield at 3% reinvestment below its YTM? *Coupons earn 3%, not 5.66%, so the terminal value falls short.*
6. A callable premium bond has YTM 4.38% and YTC 4.07%. Which do you quote, and why? *YTC, the yield to worst: the issuer is likely to call a bond trading above its call price.*

## 11. CFA-style review questions

Original questions in the CFA Level I format (three choices, one correct). Not CFA Institute material.

1. A bond with a 6% annual coupon trades at 90. Its current yield is closest to:
   - A. 6.00%
   - B. 6.67%
   - C. 7.00%
2. For a bond trading at a discount, which ordering is correct?
   - A. coupon rate < current yield < yield to maturity
   - B. yield to maturity < current yield < coupon rate
   - C. current yield < coupon rate < yield to maturity
3. A Treasury note's bond-equivalent yield is 6.00%. Its effective annual yield is closest to:
   - A. 6.00%
   - B. 6.09%
   - C. 6.18%
4. The nominal yield is 5% and expected inflation is 3%. Using the exact Fisher relation, the real yield is closest to:
   - A. 1.94%
   - B. 2.00%
   - C. 2.06%
5. A callable bond trades well above its call price. The yield measure investors are most likely to quote is:
   - A. current yield
   - B. yield to maturity
   - C. yield to worst
6. An investor holds a bond to maturity and reinvests all coupons at a rate below the purchase yield to maturity. The realized yield will be:
   - A. below the yield to maturity
   - B. equal to the yield to maturity
   - C. above the yield to maturity

**Answer key**

1. B. $`6 / 90 = 6.67\%`$.
2. A. The discount amortizes up to par, which YTM captures and current yield does not.
3. B. $`1.03^{2} - 1 = 6.09\%`$.
4. A. $`1.05 / 1.03 - 1 = 1.94\%`$; B is the approximation.
5. C. For a premium callable, the yield to call is usually the lowest, so it is the yield to worst.
6. A. YTM assumes reinvestment at the YTM itself.

## 12. Bloomberg Terminal exercises (draft: verify on the campus Terminal)

| Command | What to do | Check against this guide | Verified |
| --- | --- | --- | --- |
| `CT10 Govt YAS <GO>` | Open the current 10-year note in the yield calculator; enter price 95 in place of the market price | Section 3: compare with the worked bond (coupon differs, so match the method, not the number) | ☐ |
| `YAS <GO>`, yield conventions | Find the list of yield conventions (street, true, annual equivalent) | Section 6: BEY vs EAY | ☐ |
| `YAS <GO>` on a bill | Open a Treasury bill; compare discount rate, bond-equivalent and money market yields | Study Guide 6 section 2 | ☐ |
| `SRCH <GO>` then `YAS` | Find a callable corporate bond trading above par; read yield to maturity, yield to call and yield to worst | Section 4: YTW | ☐ |
| `GC <GO>` | Plot the nominal Treasury curve and the TIPS real yield curve together | Section 7: real vs nominal | ☐ |
| Indices | `USGG10YR Index` (10-year nominal), `USGGT10Y Index` (10-year TIPS real), `USGGBE10 Index` (10-year breakeven): confirm tickers | Section 7: breakeven inflation | ☐ |

Excel: `=BDP("CT10 Govt","YLD_YTM_MID")`, `=BDP("CT10 Govt","CURRENT_YIELD")` (confirm field names with `FLDS`).

**Exercise:** pull the 10-year nominal and 10-year TIPS yields. Compute breakeven inflation both exactly and by subtraction, then compare with the Terminal's breakeven index. Explain any gap.

## 13. Reading in Bodie, Kane & Marcus, *Investments*, 13th ed. (2024)

| Section | Topic in the book | Supports |
| --- | --- | --- |
| 14.3 Bond Yields | Yield to Maturity; Yield to Call; Realized Compound Return versus Yield to Maturity | Core reading: sections 2–5 of this guide |
| 14.1 Bond Characteristics | Accrued Interest and Quoted Bond Prices; Call Provisions; Indexed Bonds | Clean vs dirty price, callables, TIPS |
| 14.2 Bond Pricing | Bond Pricing between Coupon Dates | YTM with fractional periods |
| 14.4 Bond Prices over Time | Yield to Maturity versus Holding-Period Return; After-Tax Returns | Yield vs actual return |
| 14.5 Default Risk and Bond Pricing | Yield to Maturity and Default Risk | Promised vs expected yield |
| 2.1 The Money Market | Treasury Bills; Yields on Money Market Instruments | Bank discount yield vs bond-equivalent yield |
| 2.2 The Bond Market | Inflation-Protected Treasury Bonds; Municipal Bonds | TIPS real yield; tax-equivalent yield |
| 5.1 Measuring Returns over Different Holding Periods | Annual Percentage Rates; Continuous Compounding | BEY vs effective annual yield |
| 5.2 Interest Rates and Inflation Rates | Real and Nominal Rates of Interest; Taxes and the Real Rate of Interest | Fisher equation, real yield |

Good end-of-chapter practice: Chapter 14 CFA Problem 2 (Zello Corporation) asks for current yield, YTM and realized compound yield, then one shortcoming of each. Problem Set 31 covers realized compound yield with OID taxes.

Source: [Investments, 13th ed., table of contents (McGraw Hill)](https://info.mheducation.com/rs/128-SJW-347/images/Bodie_Preface_Investments_13e.pdf)
