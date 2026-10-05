# Spot Rates vs. Forward Rates: Mini Study Guide

FIN 4000 Investments, BKM Ch. 15 · October 5, 2026

A spot rate is the annual return from today to year n; a forward rate is the rate for one future year that today's curve implies. This guide shows how to get each from zero-coupon prices, why they differ, and what today's US curve says.

## Learning objectives

- Define a spot rate and a forward rate, and say which period each one covers.
- Compute spot rates and forward rates from zero-coupon prices.
- Explain how to lock in a forward rate with a synthetic forward loan.
- Predict whether forwards sit above or below spots from the slope of the curve.
- Price a bond with spot rates or forward rates and get the same answer.

## Core concept: a spot rate is an average, a forward rate is one leg

A spot rate yₙ is the average annual return from today to year n, like the average speed for a whole trip. A forward rate fₙ is the rate for the single year from n−1 to n, like the speed on one leg of that trip.

The spot rate is the geometric average of the forward rates up to year n:

$$
(1+y_n)^n = (1+f_1)(1+f_2)\cdots(1+f_n)
$$

Solving for one forward rate gives the formula to use when you are handed spot rates:

$$
f_n = \frac{(1+y_n)^n}{(1+y_{n-1})^{n-1}} - 1
$$

With zero-coupon bonds of the same face value, a shortcut avoids the yields entirely. Divide the price of the shorter bond by the price of the longer one:

$$
1 + f_n = \frac{P_{n-1}}{P_n}
$$

For a forward covering several years, from year a to year b:

$$
f_{a,b} = \left[\frac{(1+y_b)^b}{(1+y_a)^a}\right]^{1/(b-a)} - 1
$$

| | Spot rate yₙ | Forward rate fₙ |
|---|---|---|
| Period covered | Today to year n | One year, from n−1 to n |
| Where it comes from | The yield on an n-year zero-coupon bond | Two spot rates, or two zero-coupon prices |
| Year 1 | y₁ | f₁ = y₁, the only year with no earlier leg |
| Pricing use | Discount factor 1 ÷ (1+yₙ)ⁿ | Discount factor 1 ÷ [(1+f₁)(1+f₂)…(1+fₙ)] |

The slope of the spot curve fixes the slope of the forwards. If spot rates rise with maturity, forward rates sit above them; if the curve is inverted, forwards sit below; if it is flat, they are equal.

## Worked example 1: spot and forward rates from zero-coupon prices

Zero-coupon bonds with $1,000 face value trade at the prices below. The spot rate for each maturity comes from its price, and each forward rate from the ratio of adjacent prices.

| Maturity (years) | Price | Spot rate yₙ | Forward rate fₙ |
|---|---|---|---|
| 1 | $925.93 | 8.00% | 8.00% |
| 2 | $853.39 | 8.25% | 8.50% |
| 3 | $782.92 | 8.50% | 9.00% |
| 4 | $715.00 | 8.75% | 9.50% |
| 5 | $650.00 | 9.00% | 10.00% |

**Spot rate.** Solve the price of a zero for its yield. For the 3-year bond:

$$
y_3 = \left(\frac{1000}{782.92}\right)^{1/3} - 1 = 8.50\%
$$

**Forward rate, two ways.** The price ratio gives the year-4 forward rate directly, and the spot-rate formula agrees:

$$
1 + f_4 = \frac{782.92}{715.00} = 1.095 \quad\Rightarrow\quad f_4 = 9.50\%
$$

$$
f_4 = \frac{(1.0875)^4}{(1.085)^3} - 1 = 9.50\%
$$

The forward rate rises every year because the spot curve slopes upward, and each forward is above the spot rate for its own maturity.

## Worked example 2: lock in a forward rate with a synthetic loan

You can lock in a forward rate today by issuing one zero and buying a longer one. To lend for one year beginning at the end of year 3, which is the year-4 forward rate, issue a 3-year zero and buy 4-year zeros with the proceeds.

The number of 4-year zeros per 3-year zero issued is the price ratio:

$$
\frac{782.92}{715.00} = 1.095 \text{ four-year zeros}
$$

| Time | Cash flow | What happens |
|---|---|---|
| 0 | $0 | Proceeds from the 3-year zero pay for the 4-year zeros |
| 3 | −$1,000 | The 3-year zero matures; you pay its face value |
| 4 | +$1,095 | The 4-year zeros mature; you receive their face value |

You receive nothing at time 0, pay $1,000 at time 3, and receive $1,095 at time 4. The 9.5% return on that one-year loan is exactly f₄.

For a forward loan beginning at the end of year 4, which is the year-5 rate, repeat with the 4-year and 5-year zeros:

$$
\frac{715.00}{650.00} = 1.100 \text{ five-year zeros} \quad\Rightarrow\quad f_5 = 10.0\%
$$

The cash flows are −$1,000 at time 4 and +$1,100 at time 5.

## Today's US curve: par, spot, and forward rates

On Oct 5, 2026, quoted Treasury strip yields implied a 1-year spot rate of 4.43%, a 10-year spot rate of 5.48%, and a one-year forward rate for year 10 of about 5.76%.

The spot rates are market quotes: ask yields on Treasury STRIPS, which are zero-coupon bonds, from a Schwab account export dated Oct 5, 2026. The par yields are Treasury's official curve for Oct 2, the latest published, so the two columns are three days apart.

| Year | Par yield (Treasury, Oct 2) | Spot rate (Treasury strips, Oct 5) | One-year forward rate for that year |
|---|---|---|---|
| 1 | 4.46% | 4.43% | 4.43% |
| 2 | 4.83% | 4.79% | 5.16% |
| 3 | 4.96% | 5.00% | 5.43% |
| 4 | 5.01%* | 5.12% | 5.45% |
| 5 | 5.06% | 5.19% | 5.47% |
| 6 | 5.12%* | 5.26% | 5.63% |
| 7 | 5.17% | 5.32% | 5.69% |
| 8 | 5.21%* | 5.39% | 5.84% |
| 9 | 5.24%* | 5.45% | 5.94% |
| 10 | 5.28% | 5.48% | 5.76% |

*Interpolated between the quoted 3-, 5-, 7-, and 10-year par yields. Strip yields are ask yields on interest (coupon) strips, converted to annual compounding and interpolated to whole-year maturities. Forwards are computed from unrounded spot rates.

Four readings of the table:

- **Forwards sit above spots.** The curve slopes upward, so the implied 1-year rate for year 2 is 5.16%, 73 basis points above the 1-year spot rate of 4.43%.
- **The gap is expectations plus a premium.** Under the expectations hypothesis the whole rise is expected rate hikes; under liquidity preference part of it is a term premium.
- **A multi-year forward.** The implied average rate for years 6 to 10, the 5y5y forward, is about 5.77%.
- **Spot rates run above par yields at long maturities.** The 10-year spot rate is 5.48% against a 5.28% par yield. Part of that gap is the upward slope, which pushes spot rates above par yields, and part is the three-day difference in dates.

Principal strips quoted lower yields than the interest strips used here, about a quarter of a percentage point lower at 10 years. The table uses interest strips because every payment date has a quote, while many principal strips had none.

Schwab's ask yields include the dealer's markup and move during the day; these were pulled on Oct 5, 2026. The list ends at Nov 2036, so the 10-year point rests on the last few strips.

### Cross-check: quoted STRIPS yields at the long end

Beyond the 10-year strips in the Schwab list, the only free, dated STRIPS yield found covers 25+ year maturities. The [iShares 25+ Year Treasury STRIPS ETF](https://www.ishares.com/us/products/315911/ishares-25%20-year-treasury-strips-bond-etf) held principal STRIPS with an average yield to maturity of 5.71% on Oct 2, 2026, at an average maturity of 27.4 years.

A 27-year spot rate bootstrapped from the Oct 2 par curve is about 5.77% compounded annually, or about 5.68% on the semiannual basis that STRIPS yields use. That is within 3 basis points of the fund's 5.71%. Shorter strips are the Schwab quotes above.

Sources: Treasury par yields for Oct 2, 2026, as published at [Slickcharts](https://www.slickcharts.com/treasury) from Treasury.gov [Daily Treasury Par Yield Curve Rates](https://home.treasury.gov/resource-center/data-chart-center/interest-rates/TextView?type=daily_treasury_yield_curve). Treasury strip ask prices from a Schwab online account export of US Treasury Zeros dated Oct 5, 2026; spot and forward rates are calculated from those prices.

## BA II Plus keystrokes

Set P/Y to 1 first: [2nd] [P/Y], type 1, [ENTER], [2nd] [QUIT]. Keys are in brackets, and a second function is written [2nd] [KEY].

| Task | Keys | Check (Example 1) |
|---|---|---|
| Forward rate from two zero prices | P(n−1) [÷] P(n) [−] 1 [=] | 782.92 [÷] 715 [−] 1 [=] gives 0.0950 |
| Spot rate from a zero price | [2nd] [CLR TVM], n [N], price [+/−] [PV], 1000 [FV], [CPT] [I/Y] | n = 3, price 782.92 gives 8.50 |
| Forward from two spot rates | 1.085 [yˣ] 3 [=] [STO] 1, then 1.0875 [yˣ] 4 [÷] [RCL] 1 [−] 1 [=] | gives 0.0950 |
| Several-year forward from prices | P(a) [÷] P(b) [=] [yˣ] (b−a) [1/x] [=] [−] 1 [=] | 5y5y: use the 5- and 10-year prices |

The calculator evaluates keys from left to right, so in the third row the denominator is stored first and the division comes last. In the fourth row, type b−a as one number (5 for the 5y5y forward), then press [1/x].

## Common pitfalls

- **Calling f₃ the 3-year rate.** f₃ covers year 3 only. The 3-year rate is the spot rate y₃.
- **Discounting a cash flow at a single forward rate.** Chain every forward from year 1: the year-3 factor is 1 ÷ [(1+f₁)(1+f₂)(1+f₃)].
- **Using the par yield as a spot rate.** Par yields blend several cash flows; bootstrap them first when precision matters.
- **Expecting forwards to be forecasts.** A forward is the rate you can lock in today, and it can include a term premium.
- **Mixing up the price ratio.** Use the shorter bond's price on top: P(n−1) ÷ P(n), not the reverse.
- **Forgetting that f₁ = y₁.** The first year has no earlier leg, so spot and forward are the same.

## Key terms checklist

Check each term off when you can define it in your own words.

- [ ] **Spot rate:** the annual yield on a zero-coupon bond from today to a given maturity.
- [ ] **Forward rate:** the rate for one future year implied by today's spot curve.
- [ ] **Zero-coupon bond:** a bond that pays only its face value at maturity.
- [ ] **Par yield:** the coupon rate at which a bond prices at its face value.
- [ ] **Bootstrapping:** extracting spot rates from par yields one maturity at a time.
- [ ] **Geometric average:** the average rate that compounds to the same total growth.
- [ ] **Synthetic forward loan:** a loan locked in today by issuing one zero and buying a longer one.
- [ ] **Expectations hypothesis:** forward rates equal the expected future short rates.
- [ ] **Liquidity (term) premium:** extra yield for lending long, which makes forwards exceed expected rates.
- [ ] **Upward-sloping curve:** spot rates rise with maturity, so forwards lie above spots.

## CFA-style questions

**1.** The 1-year spot rate is 5% and the 2-year spot rate is 6%. The one-year forward rate for year 2 is closest to:

- A. 5.5%
- B. 6.0%
- C. 7.0%

**2.** Which statement about forward rates is correct?

- A. The year-3 forward rate is the annual return from today to year 3.
- B. Under the expectations hypothesis, forward rates equal expected future short rates.
- C. The year-1 forward rate is always higher than the 1-year spot rate.

**3.** Zero-coupon bonds with $1,000 face value trade at $782.92 for 3 years and $715.00 for 4 years. The forward rate for year 4 is closest to:

- A. 8.75%
- B. 9.50%
- C. 10.00%

**4.** If the spot curve slopes upward, the forward curve lies:

- A. above the spot curve.
- B. below the spot curve.
- C. on top of the spot curve.

**5.** A 3-year bond is priced once with the spot rates and once with the matching forward rates. The two prices are:

- A. higher with the forward rates.
- B. the same.
- C. lower with the forward rates.

**6.** On Oct 5, 2026, the 1-year spot rate was 4.43% and the implied forward rate for year 2 was 5.16%. This most likely means the market expects, or demands compensation for:

- A. falling short-term rates.
- B. rising short-term rates.
- C. an unchanged short-term rate.

## Answer key

| Q | Answer | Explanation |
|---|---|---|
| 1 | C | f₂ = (1.06)² ÷ 1.05 − 1 = 1.1236 ÷ 1.05 − 1 = 7.01%. Averaging 5% and 6% (A or B) ignores compounding. |
| 2 | B | The expectations hypothesis sets forwards equal to expected future short rates. A describes a spot rate, and f₁ always equals y₁, so C is false. |
| 3 | B | 1 + f₄ = 782.92 ÷ 715.00 = 1.095, so f₄ = 9.50%. A is the 4-year spot rate, and C is the year-5 forward rate. |
| 4 | A | Each forward is the marginal rate for one year. When the average (spot) rate is rising, the marginal rate must exceed it. |
| 5 | B | The spot rate is the geometric average of the forwards, so each discount factor is identical and so is the price. |
| 6 | B | A forward above the spot rate says the 1-year rate is expected to rise, or that lenders demand a term premium. Both reflect a rising path. |
