# Pricing a Coupon Bond from the Zero-Coupon Yield Curve

**FIN 4000 · Investments · Assignment Introduction**
BKM Ch. 14–15 · October 3, 2026 · Instructor: Jim Northey

---

## Overview

This assignment prices a new 2-year Treasury coupon bond from the zero-coupon yield curve, then asks what the market expects that bond to be worth in one year. It uses the same forward-rate and term-structure ideas as the study guide "Why Bond Yields Are Rising" (Section 7).

You will look at one bond three ways: as a package of zero-coupon bonds, as a single yield to maturity, and as a forecast of next year's price under two theories of the yield curve.

**The setup.** One-year zero-coupon bonds yield 7%, and two-year zeros yield 8%. The Treasury plans to issue a 2-year bond with a 9% coupon paid once a year and a face value of $100.

**What you will practice:**

- Discounting each cash flow at the zero-coupon yield for its own maturity.
- Telling a spot rate apart from a bond's yield to maturity.
- Extracting a forward rate from the zero-coupon curve.
- Contrasting the expectations hypothesis with liquidity preference theory.

## Notation and Given Inputs

The symbols follow BKM, with one convention to note: i is reserved for inflation elsewhere in the course, so it does not appear here.

| Symbol | Meaning | Given value |
|--------|---------|-------------|
| y₁ | Yield to maturity on a 1-year zero-coupon bond | 7% |
| y₂ | Yield to maturity on a 2-year zero-coupon bond | 8% |
| c | Annual coupon rate of the new 2-year bond | 9% |
| F | Face value | $100 |
| C | Annual coupon payment, C = c × F | Computed from c and F |
| P₀ | Flat (clean) price of the new bond today | Part 1 |
| y | Yield to maturity of the new coupon bond | Part 2 |
| f₂ | One-year forward rate for year 2 | Part 3 |
| E(r₂) | Expected 1-year rate next year | Parts 3 and 4 |
| L | Liquidity premium | 1% (Part 4) |
| E(P₁) | Expected price of the bond one year from now | Parts 3 and 4 |

**What you submit.** Do not round intermediate calculations; round only the final answer.

| Part | You find | Round to |
|------|----------|----------|
| 1 | Price of the bond today | 2 decimal places |
| 2 | Yield to maturity of the bond | 3 decimal places |
| 3 | Expected price next year, expectations theory | 2 decimal places |
| 4 | Expected price next year, liquidity preference with L = 1% | 2 decimal places |

## Part 1: Price of the Bond Today

Price the bond as a package of zero-coupon bonds, discounting each cash flow at the zero-coupon yield for its own maturity. The year-1 payment is the coupon, and the year-2 payment is the coupon plus the face value.

$$
C = c \times F
$$

$$
P_0 = \frac{C}{1+y_1} + \frac{C+F}{(1+y_2)^2}
$$

With the given inputs, the setup is:

$$
P_0 = \frac{9}{1.07} + \frac{109}{(1.08)^2}
$$

## Part 2: Yield to Maturity of the Bond

The bond's yield to maturity is the single rate that discounts both cash flows back to the price you found in Part 1. Solve for y:

$$
P_0 = \frac{C}{1+y} + \frac{C+F}{(1+y)^2}
$$

This is a quadratic in 1/(1+y), so use a financial calculator (see the calculator section below). As a check, y should fall between y₁ and y₂, because the bond's cash flows span both maturities.

## Part 3: Expected Price Next Year Under the Expectations Hypothesis

The zero-coupon curve implies a forward rate for year 2: the 1-year rate that, rolled over after year 1, matches the 2-year zero. Rolling over the 1-year zero and then the forward rate must earn the same as holding the 2-year zero.

$$
(1+y_2)^2 = (1+y_1)(1+f_2)
$$

$$
f_2 = \frac{(1+y_2)^2}{1+y_1} - 1 = \frac{(1.08)^2}{1.07} - 1
$$

Under the expectations hypothesis, the forward rate is the market's expectation of next year's 1-year rate.

$$
E(r_2) = f_2
$$

One year from now the bond has a single payment left, the final coupon plus the face value, one year away. The expected price is that payment discounted at the expected 1-year rate:

$$
E(P_1) = \frac{C+F}{1+E(r_2)}
$$

## Part 4: Expected Price Under Liquidity Preference

Liquidity preference theory says the forward rate includes a premium L for lending long. The expected future short rate is therefore lower than the forward rate.

$$
f_2 = E(r_2) + L \quad\Rightarrow\quad E(r_2) = f_2 - L
$$

The expected price uses the same final payment, now discounted at the lower expected rate:

$$
E(P_1) = \frac{C+F}{1+E(r_2)} = \frac{C+F}{1+f_2-L}
$$

With L = 1%, compare your answer with Part 3: a smaller expected rate gives a different expected price, and you should be able to say which way it moves and why.

## Reference Equations: Annuity Factor and Holding-Period Return

Two tools help with coupon bonds: the annuity factor, which values the stream of coupons, and the holding-period return, which measures the gain over one year.

The annuity factor for T years at yield y is the present value of $1 paid at the end of each year, and the present-value factor discounts a single $1 payment.

$$
A(y,T) = \frac{1}{y}\left[1 - \frac{1}{(1+y)^T}\right]
$$

$$
\mathrm{PVF}(y,T) = \frac{1}{(1+y)^T}
$$

A coupon bond with annual coupon C, face value F, and T years left is then priced in one step:

$$
P = C \times A(y,T) + F \times \mathrm{PVF}(y,T)
$$

The holding-period return (HPR) is the coupon received plus the change in price, divided by the starting price. Here P₀ is the price paid and P₁ is the price at the end of the year.

$$
\mathrm{HPR} = \frac{P_1 - P_0 + C}{P_0}
$$

At the end of the year the bond has T − 1 years left, so P₁ is the same formula evaluated at y′, the yield prevailing then:

$$
P_1 = C \times A(y',T-1) + F \times \mathrm{PVF}(y',T-1)
$$

In Parts 3 and 4, the expected price E(P₁) plays the role of P₁, so the expected holding-period return is:

$$
E(\mathrm{HPR}) = \frac{E(P_1) - P_0 + C}{P_0}
$$

**Flat price and accrued interest.** The flat (clean) price is the quoted bond price without accrued interest. The buyer pays the full (invoice or dirty) price, which adds the share of the next coupon the seller has earned:

$$
\text{Accrued interest} = C \times \frac{\text{days since last coupon}}{\text{days in coupon period}}
$$

$$
P_{full} = P_{flat} + \text{Accrued interest}
$$

For example, a 4% semiannual note has C = $20. With 60 days elapsed in a 182-day coupon period and a flat price of $976, accrued interest is 20 × 60 ÷ 182 = $6.59, and the full price is 976 + 6.59 = $982.59.

The present-value formulas in this assignment give the flat price when computed at a coupon date, because no interest has accrued. In Part 1 the bond is newly issued, so the price you compute is both the flat price and the full price.

## Background: Yield to Maturity and Realized Compound Yield (Problem 14-9)

An 8% annual-coupon bond with $1,000 face value matures in three years and sells for $953.10. Interest rates for the next three years are known with certainty: r₁ = 8%, r₂ = 10%, and r₃ = 12%. The problem asks for the bond's yield to maturity and its realized compound yield. The two measures differ in what they assume about reinvesting the coupons.

**Yield to maturity.** The yield to maturity is the single rate y that discounts all of the bond's cash flows to its price, with C = 0.08 × 1000 = $80 per year:

$$
953.10 = \frac{80}{1+y} + \frac{80}{(1+y)^2} + \frac{1080}{(1+y)^3}
$$

Equivalently, with the annuity factor and present-value factor from the reference equations:

$$
953.10 = 80 \times A(y,3) + 1000 \times \mathrm{PVF}(y,3)
$$

There is no closed-form solution, so use the calculator: N = 3, PMT = 80, FV = 1000, PV = −953.10, CPT I/Y. The yield to maturity implicitly assumes every coupon is reinvested at y itself.

**Realized compound yield.** This measure uses the interest rates that actually prevail. Grow each cash flow to the end of year 3, reinvesting each coupon at the one-year rates for the remaining years:

$$
FV = C(1+r_2)(1+r_3) + C(1+r_3) + (C+F) = 80(1.10)(1.12) + 80(1.12) + 1080
$$

The first coupon arrives at the end of year 1, so it earns r₂ and r₃. The rate r₁ applies before any coupon is received and does not enter the future value. Then find the single annual rate that grows the purchase price to that future value:

$$
953.10\,(1+y_{realized})^3 = FV \;\Rightarrow\; y_{realized} = \left(\frac{FV}{953.10}\right)^{1/3} - 1
$$

On the calculator: N = 3, PV = −953.10, PMT = 0, FV = the future value above, CPT I/Y.

The two yields differ whenever the reinvestment rates differ from the yield to maturity. The realized compound yield is the measure that reflects the actual rates, which makes it the same idea as the expected realized compound yield in the study guide's Example C.

## Worked Example: Coupon Bond from Zero-Coupon Prices, YTM, and Holding-Period Return

This example uses different numbers from the assignment, so you can see each tool in action. Zero-coupon bonds with $1,000 par currently trade at these prices:

| Maturity (years) | Price of $1,000 par zero-coupon bond |
|------------------|--------------------------------------|
| 1 | $988.00 |
| 2 | $888.50 |
| 3 | $842.30 |

A 4.5% annual-coupon bond with $1,000 par matures in 3 years. What is its yield to maturity? If the yield curve flattens at 7.0% at the end of year 1, what is the 1-year holding-period return?

**Step 1: Price today.** Each zero-coupon price divided by $1,000 is the present-value factor for that year, so the coupon bond is priced as a package of zeros:

$$
P_0 = 45(0.98800) + 45(0.88850) + 1045(0.84230) = 964.65
$$

**Step 2: Yield to maturity.** Find the single y that discounts the bond's cash flows to that price. On the BA II Plus: N = 3, PMT = 45, FV = 1000, PV = −964.65, CPT I/Y.

$$
964.65 = 45 \times A(y,3) + 1000 \times \mathrm{PVF}(y,3) \;\Rightarrow\; y = 5.82\%
$$

**Step 3: Price after one year.** Two years remain, and the yield is now 7.0%, so the annuity and present-value factors are evaluated at 7.0% for 2 years:

$$
P_1 = 45 \times A(7.0\%,2) + 1000 \times \mathrm{PVF}(7.0\%,2) = 954.80
$$

**Step 4: Holding-period return.** Add the $45 coupon to the price change and divide by the starting price:

$$
\mathrm{HPR} = \frac{45 + (954.80 - 964.65)}{964.65} = 0.0364 = 3.64\%
$$

The return has two parts: a coupon yield of about 4.67% (45 ÷ 964.65) and a capital loss of about 1.02%, because yields rose from 5.82% to 7.0% and the price fell. The loss offsets part of the coupon.

## Worked Example: Arbitrage from Discounting at Spot Rates

A 4% Treasury note with $1,000 face value has 2.5 years to maturity and pays coupons semiannually. The spot rates are quoted as annual rates with semiannual compounding:

| Maturity | 6 months | 1 year | 1.5 years | 2 years | 2.5 years |
|----------|----------|--------|-----------|---------|-----------|
| Spot rate | 2% | 2.5% | 3% | 4% | 6% |

The note currently sells for $976. Is there an arbitrage profit?

**Step 1: Cash flows.** The semiannual coupon is C = 0.04 × 1000 ÷ 2 = $20 for five half-year periods, and the final payment adds the $1,000 face value ($1,020).

**Step 2: No-arbitrage price.** Discount each cash flow at the spot rate for its own maturity. Each spot rate s_t is annualized, so the rate per half-year is s_t ÷ 2, and t counts half-years:

$$
P^{*} = \sum_{t=1}^{5} \frac{C}{\left(1+\frac{s_t}{2}\right)^{t}} + \frac{F}{\left(1+\frac{s_5}{2}\right)^{5}}
$$

$$
P^{*} = \frac{20}{1.01} + \frac{20}{(1.0125)^2} + \frac{20}{(1.015)^3} + \frac{20}{(1.02)^4} + \frac{1020}{(1.03)^5} = 19.80 + 19.51 + 19.13 + 18.48 + 879.86 = 956.78
$$

**Step 3: Arbitrage profit.** Any gap between the market price and the no-arbitrage price is a potential profit:

$$
\text{Arbitrage profit} = P_{market} - P^{*} = 976 - 956.78 = 19.22
$$

The note is overpriced, so the strategy is to sell it at $976 and buy the same cash flows as zero-coupon bonds (strips) for $956.78, keeping the $19.22 difference with no risk. If the market price were below the no-arbitrage price, you would reverse the trade: buy the note and sell the strips.

## Calculator Setup (BA II Plus)

Because nothing may be rounded until the end, set the display to show more decimals and store each result instead of retyping it.

- **Show more decimals:** press 2nd, then FORMAT (the . key), type 9, press ENTER, then 2nd and QUIT.
- **Part 2, yield to maturity:** set N = 2, PMT = 9, FV = 100, and PV = the Part 1 price entered as a negative number, then press CPT and I/Y. The answer is an annual percentage.
- **Carry results forward:** press STO and a digit (1 to 9) to store a value, and RCL and that digit to recall it. Use this for P₀ and f₂ rather than typing rounded values.

## Keystroke Guide: BA II Plus Professional

This guide shows the keys for every calculation in this introduction. Keys are in [brackets]; a second function is written [2nd] [KEY]. The guide lists inputs only, so you can follow along without seeing the assignment answers. Where a worked example appears, a check value is given.

### Before you start (once)

1. **Set payments per year to 1.** Press [2nd] [P/Y] (above the I/Y key), type 1, press [ENTER], then [↓] to confirm C/Y also shows 1, and press [2nd] [QUIT]. The calculator starts at 12, which would treat every rate as monthly. For semiannual bonds, keep P/Y = 1 and enter the rate per half-year (the annual rate ÷ 2).
2. **Check the payment mode.** The display should not show BGN. If it does, press [2nd] [BGN], [2nd] [SET], then [2nd] [QUIT].
3. **Clear before each time-value calculation:** [2nd] [CLR TVM] (above the FV key).
4. **Use the sign convention.** Cash you pay out is negative and cash you receive is positive, so PV is opposite in sign to PMT and FV.
5. **Enter rates as percentages.** Type 7 for 7%, not 0.07.
6. **Store full-precision results.** [STO] and a digit saves a value, and [RCL] and that digit recalls it. The display setting from the setup section above changes only what you see, not the stored value.

### 1. Discount one cash flow at its own rate (Part 1 and the arbitrage example)

For each cash flow: [2nd] [CLR TVM], enter N, I/Y, and FV, then press [CPT] [PV]. The answer appears negative, because it is the cash you would pay. Press [+/−] to make it positive, then add it to a running total.

**Part 1.** Discount the year-1 and year-2 payments at the zero-coupon yields:

| Cash flow | N | I/Y | FV |
|-----------|---|-----|----|
| Year 1 payment | 1 | 7 | 9 |
| Year 2 payment | 2 | 8 | 109 |

After the first row, press [+/−] [STO] 1. After the second row, press [+/−] [+] [RCL] 1 [=], then [STO] 1. The total in memory 1 is P₀.

**Arbitrage example.** The same method works with the spot rate per half-year (annual rate ÷ 2):

| Cash flow | N | I/Y | FV |
|-----------|---|-----|----|
| Period 1 | 1 | 1 | 20 |
| Period 2 | 2 | 1.25 | 20 |
| Period 3 | 3 | 1.5 | 20 |
| Period 4 | 4 | 2 | 20 |
| Period 5 | 5 | 3 | 1020 |

Add the five results with [STO] and [RCL] as above. The total should be 956.78. The arbitrage profit is then 976 [−] [RCL] 1 [=], which gives 19.22.

### 2. Yield to maturity (Part 2, the holding-period-return example, and Problem 14-9)

Press [2nd] [CLR TVM], then enter N, PMT, and FV. Enter the price and press [+/−] [PV], then press [CPT] [I/Y]. The result is already a percentage.

| Problem | N | PMT | FV | PV | Then |
|---------|---|-----|----|----|------|
| Part 2 | 2 | 9 | 100 | [RCL] 1 [+/−] | [CPT] [I/Y] |
| Holding-period-return example | 3 | 45 | 1000 | 964.65 [+/−] | [CPT] [I/Y] |
| Problem 14-9, part (a) | 3 | 80 | 1000 | 953.10 [+/−] | [CPT] [I/Y] |

Check: the holding-period-return example gives 5.82%.

### 3. Forward rate and expected price (Parts 3 and 4)

**Forward rate f₂.** The calculator evaluates keys from left to right, so a division after a power works on the power:

1. Press 1.08 [yˣ] 2 [÷] 1.07 [−] 1 [=]. The display is f₂ as a decimal.
2. Press [STO] 2. Multiply by 100 if you want to see it as a percentage.

**Expected price, Part 3 (expectations hypothesis).** The expected rate is f₂, in percent:

1. Press [2nd] [CLR TVM], then 1 [N].
2. Press [RCL] 2 [×] 100 [=] [I/Y].
3. Press 109 [FV], then [CPT] [PV]. Ignore the sign.

**Expected price, Part 4 (liquidity premium L = 1%).** The expected rate is f₂ − L:

1. Press [2nd] [CLR TVM], then 1 [N].
2. Press [RCL] 2 [−] 0.01 [=] [×] 100 [=] [I/Y].
3. Press 109 [FV], then [CPT] [PV]. Ignore the sign.

Store the results with [+/−] [STO] 3 if you want to reuse them.

### 4. Annuity factor and present-value factor (reference equations)

The time-value keys produce both factors directly. Use PMT = 1 for the annuity factor and FV = 1 for the present-value factor:

| Factor | Keys |
|--------|------|
| A(y,T) | [2nd] [CLR TVM], T [N], y [I/Y], 1 [PMT], [CPT] [PV] |
| PVF(y,T) | [2nd] [CLR TVM], T [N], y [I/Y], 1 [FV], [CPT] [PV] |

Both answers appear negative; ignore the sign. Check: with T = 2 and y = 7, the annuity factor is 1.8080 and the present-value factor is 0.8734.

### 5. Price after one year and holding-period return

**Price at the end of the year, P₁.** The bond has T − 1 years left, discounted at the new yield y′:

1. Press [2nd] [CLR TVM].
2. Enter T − 1 [N], y′ [I/Y], C [PMT], and F [FV].
3. Press [CPT] [PV], then [+/−] [STO] 3.

**Holding-period return.** With P₀ in memory 1 and P₁ in memory 3, press [RCL] 3 [−] [RCL] 1 [+] C [=] [÷] [RCL] 1 [=]. The display is the return as a decimal; multiply by 100 for a percentage.

Check: in the holding-period-return example, T − 1 = 2, y′ = 7, C = 45, and F = 1000 give P₁ = 954.80, and the return is 0.0364 (3.64%).

### 6. Realized compound yield (Problem 14-9, part b)

The chain of operations evaluates strictly left to right, so compute each term separately and store the partial results.

1. Press 80 [×] 1.10 [×] 1.12 [=] [STO] 4. This is the first coupon grown through years 2 and 3.
2. Press 80 [×] 1.12 [=] [+] [RCL] 4 [+] 1080 [=] [STO] 5. This adds the second coupon and the final payment, so memory 5 holds the future value.
3. Press [2nd] [CLR TVM], then 3 [N], 953.10 [+/−] [PV], 0 [PMT], [RCL] 5 [FV].
4. Press [CPT] [I/Y]. The result is the realized compound yield as a percentage.

To check it with the formula instead, press [RCL] 5 [÷] 953.10 [=] [yˣ] 3 [1/x] [=] [−] 1 [=] and multiply by 100.

### 7. Accrued interest and flat versus full price

Accrued interest is the coupon times the fraction of the coupon period elapsed. For the $20 coupon with 60 days elapsed in a 182-day period, press 20 [×] 60 [÷] 182 [=], which gives 6.59. Then press [+] 976 [=] for the full price of 982.59.

When dates are given, the Bond worksheet ([2nd] [BOND]) returns the clean price (PRI) and accrued interest (AI) from the settlement date, coupon rate, redemption date, and yield. Use it for date-based problems and the keys above for the arithmetic in this introduction.

### 8. Common keystroke errors

- **P/Y left at 12.** The I/Y answer or input is treated as monthly. Set P/Y = 1 once, as above.
- **Same sign on PV and FV or PMT.** The calculator returns an error or a nonsense rate. Enter the price as a negative number.
- **No [2nd] [CLR TVM].** Old values stay in N, I/Y, PV, PMT, or FV and silently change the answer.
- **Rates as decimals.** Enter 7 for 7%, but keep decimals when you use rates in arithmetic, such as 1.07.
- **Sums of products.** The calculator does not apply multiplication before addition, so store each product with [STO] and combine the results with [RCL].
- **Rounding too early.** Store and recall results instead of retyping rounded values, and let the display setting control only what you see.

## Common Pitfalls

- **Part 1:** discount each cash flow at its own zero-coupon yield. Using a single rate for both is the Part 2 method, not Part 1.
- **The year-2 cash flow:** it is the coupon plus the face value, not the coupon alone.
- **Part 2:** enter PV as a negative number. A positive PV with a positive PMT and FV makes the calculation fail or give a nonsense rate.
- **Part 3:** the expected 1-year rate for next year is the forward rate, not the 2-year zero yield.
- **Part 4:** the liquidity premium is subtracted from the forward rate to get the expected rate. Check that your sign matches the idea that lenders demand a premium.
- **Rounding:** rounding f₂ or P₀ before the next step shifts the final answer in the third or fourth decimal place.
