# Study Guide 3: Quantitative Tools

*Fixed Income Study Guides*

[← All study guides](README.md)

The same three tasks run through every tool: price a strip, compute its yield and duration, and do one bootstrap step. Calculators handle single bonds; spreadsheets and code build whole curves.

Common inputs used below:

- **Strip:** 20-year zero, settles Nov 15 2026, matures Nov 15 2046, yield 4.5%. Answer: price 41.065, modified duration 29.34 (30-year) or 19.56 (20-year).
- **Bootstrap step:** the 2.0-year bond from Study Guide 2. Coupon 4.6%, price 100, earlier coupons worth 6.6157. Answer: spot rate 4.6117%.

The calculations each tool performs:

$$P = \frac{100}{(1 + y/2)^{n}} \qquad D^{*} = \frac{T}{1 + y/2} \qquad s = 2\left[\left(\frac{100 + c/2}{P - PV_{known}}\right)^{1/n} - 1\right]$$

## 1. TI BA II Plus Professional

**Strip price with TVM**

1. `2nd` `CLR TVM` to clear.
2. `2nd` `P/Y` 2 `ENTER` (C/Y follows to 2), then `2nd` `QUIT`.
3. 40 `N` · 4.5 `I/Y` · 0 `PMT` · 100 `FV`.
4. `CPT` `PV` → **−41.065**.

With P/Y = 2, `I/Y` is the annual rate and `N` is the number of half-years. `20` `2nd` `xP/Y` `N` also enters 40.

**Strip price, yield and duration with the Bond worksheet**

1. `2nd` `BOND`, then `2nd` `CLR WORK`.
2. SDT = 11.1526 `ENTER` (dates are MM.DDYY) ↓
3. CPN = 0 `ENTER` ↓ RDT = 11.1546 `ENTER` ↓ RV = 100 `ENTER` ↓
4. ACT (toggle with `2nd` `SET` if it shows 360) ↓ 2/Y ↓
5. YLD = 4.5 `ENTER` ↓ PRI `CPT` → **41.065** ↓ AI → 0 ↓ DUR → **19.56** (modified duration, Professional model only).

To solve for yield instead, enter PRI and `CPT` at YLD.

**Bootstrap step**

1. Value the earlier coupons: 2.3 × (0.980392 + 0.959267 + 0.936719) = 6.6157. Keep discount factors in memory with `STO` 1–9 and `RCL`.
2. With P/Y = 2: 4 `N` · 93.3843 `+|-` `PV` · 0 `PMT` · 102.3 `FV`.
3. `CPT` `I/Y` → **4.6117**.

## 2. HP 12C (RPN)

**Strip price with TVM**

1. `f` `CLEAR FIN`.
2. 40 `n` · 4.5 `ENTER` 2 `÷` `i` (the 12C uses the rate per period) · 0 `PMT` · 100 `FV`.
3. `PV` → **−41.065**.

**Bond functions** (semiannual, Actual/Actual only)

1. `g` `M.DY` once to set US date format (MM.DDYYYY).
2. 4.5 `i` (annual yield) · 0 `PMT` (annual coupon %).
3. 11.152026 `ENTER` 11.152046 `f` `PRICE` → **41.065**; `x≷y` shows accrued interest.
4. For yield: price in `PV`, coupon in `PMT`, the two dates, then `f` `YTM`.

The 12C has no duration key. Compute modified duration for a zero by hand: 20 `ENTER` 1.0225 `÷` → 19.56.

**Bootstrap step**

1. 4 `n` · 93.3843 `CHS` `PV` · 0 `PMT` · 102.3 `FV`.
2. `i` → 2.3059 (per half-year), then 2 `×` → **4.6117**.
3. Or directly: 102.3 `ENTER` 93.3843 `÷` 4 `1/x` `yˣ` 1 `−` 2 `×` → 0.046117.

Forward rate from 1.0 to 1.5 years: 0.959267 `ENTER` 0.936719 `÷` 1 `−` 2 `×` → 0.0481.

## 3. Excel

| Task | Formula | Result |
| --- | --- | --- |
| Strip price | `=PRICE("2026-11-15","2046-11-15",0,4.5%,100,2,1)` | 41.065 |
| Strip price, direct | `=100/(1+4.5%/2)^40` | 41.065 |
| Yield from price | `=YIELD("2026-11-15","2046-11-15",0,41.065,100,2,1)` | 4.50% |
| Modified duration | `=MDURATION("2026-11-15","2046-11-15",0,4.5%,2,1)` | 19.56 |

Arguments: frequency 2 = semiannual, basis 1 = Actual/Actual. Use cell references or `DATE()` in real models.

**Bootstrap layout** (one row per half-year; row 2 is the first bond). Columns: A = period n, C = coupon in percent units (4.2, not 4.2%), D = price, E = discount factor, F = spot, G = forward.

| Cell | Formula (fill down from row 3) |
| --- | --- |
| E2 | `=D2/(100+C2/2)` |
| E3 | `=(D3-(C3/2)*SUM(E$2:E2))/(100+C3/2)` |
| F2 | `=2*(E2^(-1/A2)-1)` |
| G3 | `=2*(E2/E3-1)` |

For a smooth fitted curve, put Nelson-Siegel parameters in cells and let Solver minimize squared pricing errors.

## 4. Python

| Library | Role | License |
| --- | --- | --- |
| QuantLib (`pip install QuantLib`) | Industry standard. Wraps the C++ library; full day counts, calendars, bond helpers, curve bootstrapping and interpolation | Open source, BSD-style; free for commercial use |
| rateslib | Modern, Pythonic curve building and bond/swap analytics with automatic differentiation | Source-available: free for personal and educational use; commercial use needs a paid licence |
| FinancePy | Readable pure-Python library, good for teaching | Open source |
| numpy-financial, SciPy, pandas | Basic TVM, root-finding and curve fitting for hand-built models | Open source |

QuantLib bootstrap of Example B (tested; matches the hand results):

```python
import QuantLib as ql
today = ql.Date(15, ql.January, 2026)
ql.Settings.instance().evaluationDate = today
cal, dc = ql.NullCalendar(), ql.Thirty360(ql.Thirty360.BondBasis)
helpers = []
for months, cpn in [(6, 4.0), (12, 4.2), (18, 4.4), (24, 4.6)]:
    sched = ql.Schedule(today, today + ql.Period(months, ql.Months), ql.Period(ql.Semiannual),
                        cal, ql.Unadjusted, ql.Unadjusted, ql.DateGeneration.Backward, False)
    helpers.append(ql.FixedRateBondHelper(ql.QuoteHandle(ql.SimpleQuote(100.0)),
                                          0, 100.0, sched, [cpn / 100], dc))
curve = ql.PiecewiseLogLinearDiscount(today, helpers, dc)
print(curve.zeroRate(2.0, ql.Compounded, ql.Semiannual).rate())  # 0.046117
```

30/360 makes every period exactly half a year so the output matches the hand example. Real Treasury work uses `ql.ActualActual(ql.ActualActual.Bond)` and a US government calendar.

## 5. Julia

- **FinanceModels.jl** (JuliaActuary, formerly Yields.jl) is the main maintained package. It takes market quotes such as `ZCBYield`, `ParYield` or `CMTYield` and fits curves with `fit(model, quotes, Fit.Bootstrap())`.
- Models include bootstrapped splines, Nelson-Siegel, Nelson-Siegel-Svensson and Smith-Wilson. Functions `discount`, `zero`, `forward` and `par` read rates off the fitted curve.
- **ActuaryUtilities.jl** adds duration, convexity and present-value helpers.

Plain-Julia bootstrap (same logic as the tested Python; not run here):

```julia
coupons = [4.0, 4.2, 4.4, 4.6]; prices = fill(100.0, 4)
spots = Float64[]
for n in eachindex(coupons)
    cpn = coupons[n] / 2
    pv_known = sum((cpn / (1 + spots[k] / 2)^k for k in 1:n-1); init = 0.0)
    push!(spots, 2 * (((100 + cpn) / (prices[n] - pv_known))^(1 / n) - 1))
end
println(spots)   # 0.04, 0.042021, 0.044059, 0.046117
```

## 6. Choosing a tool

| Tool | Best for | Bootstrap a whole curve? | Duration built in? |
| --- | --- | --- | --- |
| TI BA II Plus Professional | Exams, single-bond checks | One step at a time, by hand | Yes (modified) |
| HP 12C | Exams, quick RPN checks | One step at a time, by hand | No |
| Excel | Transparent teaching models, small curves | Yes, with fill-down formulas | Yes (`DURATION`, `MDURATION`) |
| Python + QuantLib | Production-grade curves and pricing | Yes, with interpolation choices | Yes (`BondFunctions`) |
| Julia + FinanceModels.jl | Fast actuarial and curve modeling | Yes, including fitted models | Yes (ActuaryUtilities.jl) |

The CFA exams allow only the TI BA II Plus (including Professional) and HP 12C families, which is why both appear here.

## 7. Practice set

1. On either calculator, price a 10-year strip at 4.0%. *67.297.*
2. On the TI Bond worksheet, find the yield of a strip settling 11/15/2026, maturing 11/15/2041, priced at 50. *4.67%.*
3. In Excel, extend the bootstrap table with a 2.5-year 4.8% par bond. *Spot ≈ 4.82%.*
4. In Python, change the QuantLib day count to Actual/Actual and explain why the rates move slightly. *Periods are no longer exactly 0.5 years.*

## 8. CFA-style review questions

Original questions in the CFA Level I format (three choices, one correct). Not CFA Institute material. Solve each on the TI BA II Plus or HP 12C.

1. A 10-year Treasury note pays a 4% coupon semiannually and yields 5%. Its price per 100 is closest to:
   - A. 92.21
   - B. 92.28
   - C. 107.79
2. A 5-year bond pays a 6% coupon semiannually and yields 5%. Its price per 100 is closest to:
   - A. 104.33
   - B. 104.38
   - C. 105.00
3. The HP 12C's bond functions (`f PRICE`, `f YTM`) assume:
   - A. semiannual coupons and an Actual/Actual day count
   - B. annual coupons and a 30/360 day count
   - C. quarterly coupons and an Actual/360 day count
4. To compute a bond's yield to maturity from settlement and maturity dates in Excel, the most appropriate function is:
   - A. YIELD
   - B. RATE
   - C. IRR
5. On the TI BA II Plus, a student solves a semiannual bond with P/Y left at 12. The computed I/Y will most likely be:
   - A. correct, because P/Y affects only the display
   - B. wrong, because the calculator assumes monthly periods
   - C. correct only if the bond trades at par

**Answer key**

1. A. N = 20, I/Y = 2.5 per period, PMT = 2, FV = 100 → PV = 92.21. B uses annual compounding; C is a premium price, impossible when the yield exceeds the coupon.
2. B. N = 10, I/Y = 2.5, PMT = 3, FV = 100 → 104.38. A uses annual compounding.
3. A. The 12C bond functions are fixed to U.S. Treasury conventions.
4. A. YIELD takes dates, coupon, price, redemption, frequency and basis. RATE needs whole periods; IRR needs a cash flow list.
5. B. P/Y and C/Y must match the bond's payment frequency (2).

## 9. Bloomberg Terminal (draft: verify on the campus Terminal)

The Terminal is a sixth tool alongside the ones above, and it connects to Excel and Python.

| Command | What to do | Check against this guide | Verified |
| --- | --- | --- | --- |
| `YAS <GO>` | The Terminal's bond calculator: enter a price or yield, read price, yield, duration and convexity | Use it to check TI and HP 12C answers | ☐ |
| Excel add-in | Bloomberg tab → Spreadsheet Builder; functions `BDP` (current value), `BDH` (history), `BDS` (lists) | Rebuild the section 3 Excel table with live data | ☐ |
| `FLDS <GO>` | Field search: find the exact field names for price, yield, duration, accrued interest | Field names used in these guides | ☐ |
| `BQL` | Bloomberg Query Language in Excel, e.g. `=BQL("CT10 Govt","yield")` (confirm syntax) | Bulk pulls for curves and ladders | ☐ |
| `BQNT <GO>` | BQuant: Python notebooks on the Terminal | Run the section 4 Python examples against live data | ☐ |
| `BMC <GO>` | Bloomberg Market Concepts course, including a fixed income module | Student onboarding before these exercises | ☐ |

The `blpapi` Python package (Desktop API) works only on a machine logged in to the Terminal; licensing limits redistributing the data.

**Exercise:** pull the current 10-year note's price, yield and modified duration with `BDP`, then reproduce each value with `PRICE`, `YIELD` and `MDURATION` in the same workbook.

## 10. Reading in Bodie, Kane & Marcus, *Investments*, 13th ed. (2024)

| Section | Topic in the book | Supports |
| --- | --- | --- |
| 14.2 Bond Pricing | Bond Pricing between Coupon Dates; Excel `PRICE` spreadsheet | Excel bond pricing |
| 14.3 Bond Yields | Yield to Maturity; Yield to Call | Excel `YIELD` and calculator yield solving |
| 16.1 Interest Rate Risk | Duration; Spreadsheet 16.1 | Duration built cash flow by cash flow in Excel |
| 5.1 Measuring Returns over Different Holding Periods | Annual Percentage Rates; Continuous Compounding | Compounding conversions (ICONV, `EFFECT`) |

The book's tool coverage is Excel only, through its Excel Applications and the spreadsheet templates on its student site (mhhe.com/Bodie13e). The calculator keystrokes, Python and Julia material in this guide go beyond the text.

Sources: [rateslib licence](https://rateslib.readthedocs.io/en/latest/i_licence.html) · [FinanceModels.jl documentation](https://docs.juliahub.com/FinanceModels/euyfJ/4.8.0) · [FinanceModels.jl on GitHub](https://github.com/JuliaActuary/FinanceModels.jl)
