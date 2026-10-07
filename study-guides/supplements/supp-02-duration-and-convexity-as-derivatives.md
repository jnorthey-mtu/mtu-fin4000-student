# Supplement 2: Duration and Convexity as Derivatives

*Calculus Derivations, Taylor Series and Redington Immunization (BKM Ch. 16)*

[← All study guides](../../study-guide-index.md)

*Big picture: duration and convexity are not definitions to memorize. They are the first and second derivatives of the bond price function, divided by the price. Once you see that, the price-change formula is a Taylor series, and the classic actuarial immunization conditions are the first- and second-derivative tests for a minimum.*

**Source context:** Companion to the slide deck "Duration, Convexity & Weighted Average Life" (Michigan Tech template) and to the notebook [`FIN4000_Supp02_Notebook.ipynb`](../../notebooks/python/FIN4000_Supp02_Notebook.ipynb), which runs every calculation below in SymPy and QuantLib. For the finance-side treatment (duration rules, calculator and spreadsheet steps, practice questions) see [Study Guide 5](../general/gen-05-duration-average-life-convexity.md). BKM references are to *Investments*, 13th Edition, Chapter 16.

**Prerequisites:** the chain and power rules, Taylor series, and (for Section 6) the mean and variance of a discrete distribution.

---

## What This Supplement Adds

This is enrichment for students in mathematics and actuarial science. It is not a numbered learning objective in BKM. By the end of it you should be able to:

- Derive modified duration and convexity by differentiating the price function.
- Extend the derivation to $`k`$ payments per year and to continuous compounding.
- Show that the duration-convexity formula is a second-order Taylor expansion, and estimate its error with the third derivative.
- Show that, under continuous compounding, convexity equals duration squared plus the variance of the payment times.
- Prove Redington's immunization conditions with the second-derivative test.
- Check each result symbolically and numerically in Python.

---

## 1. Setup

For an option-free bond with fixed cash flows $`CF_t`$ at times $`t`$ (in years), the price is a function of the yield $`y`$ (effective annual):

```math
P(y) = \sum_{t} CF_t\,(1+y)^{-t}
```

Write $`PV_t = CF_t(1+y)^{-t}`$ for the present value of each payment and $`w_t = PV_t / P`$ for its weight. The weights are positive and sum to 1. Only $`y`$ varies; the cash flows do not.

**Running example:** a 10-year bond with a 6% annual coupon and \$1,000 face value, priced at $`y = 6\%`$, so $`P = \$1{,}000`$.

## 2. Duration is the first derivative

Differentiate one term:

```math
\frac{d}{dy}(1+y)^{-t} = -t\,(1+y)^{-t-1}
```

Sum over all payments and factor out one power of $`1/(1+y)`$:

```math
\frac{dP}{dy} = -\sum_{t} t\,CF_t\,(1+y)^{-t-1} = -\frac{1}{1+y}\sum_{t} t\,PV_t
```

Divide by $`P`$ and change sign:

```math
-\frac{1}{P}\frac{dP}{dy} = \frac{1}{1+y}\sum_{t} t\,\frac{PV_t}{P} = \frac{D_{mac}}{1+y} = D^{*}
```

Here $`D_{mac} = \sum_t t\,w_t`$ is the Macaulay duration, a weighted average of the payment times (actuarial texts call it the discounted mean term, and call $`D^{*}`$ the volatility). By the chain rule the same result reads:

```math
D^{*} = -\frac{d\,\ln P}{dy}
```

so $`D^{*}`$ is the percentage change in price per unit change in yield. The dollar version is the DV01:

```math
\text{DV01} = -\frac{dP}{dy}\times 0.0001 = P\,D^{*}\times 0.0001
```

**Running example:** $`D_{mac} = 7.8017`$ years, $`D^{*} = 7.3601`$, DV01 = \$0.7360 per \$1,000 face per basis point. A 1-point rise in yield gives a first-order estimate of $`-7.36\%`$.

**Two checks.**

- Zero-coupon bond, $`P = F(1+y)^{-T}`$: $`D^{*} = T/(1+y)`$ and $`D_{mac} = T`$.
- Perpetuity, $`P = c/y`$, so $`P' = -c/y^{2}`$: $`D^{*} = 1/y`$ and $`D_{mac} = (1+y)/y`$. At $`y = 5\%`$, $`D^{*} = 20`$ and $`D_{mac} = 21`$.

## 3. Other compounding conventions

With $`k`$ payments per year, $`P(y) = \sum_t CF_t\,(1+y/k)^{-kt}`$ and

```math
\frac{d}{dy}(1+y/k)^{-kt} = -t\,(1+y/k)^{-kt-1}
\quad\Rightarrow\quad
D^{*} = \frac{D_{mac}}{1+y/k}
```

with $`t`$ measured in years. Under continuous compounding with force of interest $`\delta`$, $`P(\delta) = \sum_t CF_t\,e^{-\delta t}`$ and

```math
-\frac{1}{P}\frac{dP}{d\delta} = \sum_{t} t\,w_t = D_{mac}
```

exactly. So Macaulay duration is the derivative with respect to the force of interest. The two results agree because $`\delta = \ln(1+y)`$ and $`d\delta/dy = 1/(1+y)`$:

```math
\frac{dP}{dy} = \frac{dP}{d\delta}\cdot\frac{d\delta}{dy} = \frac{1}{1+y}\,\frac{dP}{d\delta}
```

## 4. Convexity is the second derivative

Differentiate $`dP/dy`$ once more, using $`\frac{d}{dy}\left[-t(1+y)^{-t-1}\right] = t(t+1)(1+y)^{-t-2}`$:

```math
\frac{d^{2}P}{dy^{2}} = \sum_{t} t(t+1)\,CF_t\,(1+y)^{-t-2}
```

Convexity is this second derivative divided by the price:

```math
C = \frac{1}{P}\frac{d^{2}P}{dy^{2}} = \frac{1}{P\,(1+y)^{2}}\sum_{t} t(t+1)\,PV_t
```

**Running example:** $`C = 69.7404`$.

Every term in the sum is positive, so $`P''(y) > 0`$: the price-yield curve is convex for any bond with non-negative cash flows.

**With $`k`$ payments per year**, the second derivative of $`(1+y/k)^{-kt}`$ is $`\frac{t(kt+1)}{k}(1+y/k)^{-kt-2}`$, so

```math
C = \frac{1}{P\,(1+y/k)^{2}}\sum_{t} \frac{t(kt+1)}{k}\,PV_t
```

If you count time in periods, $`n = kt`$, this becomes $`\sum n(n+1)\,PV_n / \left[P\,(1+y/k)^{2}k^{2}\right]`$. That is why [Study Guide 5](../general/gen-05-duration-average-life-convexity.md) divides by 4 for semiannual bonds.

**Two checks.**

- Zero-coupon bond: $`C = T(T+1)/(1+y)^{2}`$. For $`T = 10`$ and $`y = 6\%`$: $`D^{*} = 9.434`$ and $`C = 97.90`$.
- Perpetuity: $`P'' = 2c/y^{3}`$, so $`C = 2/y^{2}`$. At 5%: $`C = 800`$.

## 5. The price-change formula is a Taylor series

Expand $`P`$ around today's yield:

```math
P(y+\Delta y) = P + P'\,\Delta y + \tfrac{1}{2}P''\,(\Delta y)^{2} + \tfrac{1}{6}P'''\,(\Delta y)^{3} + \cdots
```

Divide by $`P`$ and substitute $`P'/P = -D^{*}`$ and $`P''/P = C`$:

```math
\frac{\Delta P}{P} \approx -D^{*}\,\Delta y + \tfrac{1}{2}\,C\,(\Delta y)^{2}
```

The next term uses the third derivative:

```math
\frac{P'''}{P} = -\frac{1}{P\,(1+y)^{3}}\sum_{t} t(t+1)(t+2)\,PV_t
```

By the Lagrange remainder, truncating after the second-order term leaves an error of $`\tfrac{1}{6}P'''(\xi)(\Delta y)^{3}`$ for some $`\xi`$ between $`y`$ and $`y+\Delta y`$. For the running example $`P'''/P = -753.69`$.

| Yield change | Exact | Duration only | + convexity | + third order |
| --- | --- | --- | --- | --- |
| +2 points | −13.4202% | −14.7202% | −13.3254% | −13.4259% |
| +1 point | −7.0236% | −7.3601% | −7.0114% | −7.0239% |
| −1 point | +7.7217% | +7.3601% | +7.7088% | +7.7214% |
| −2 points | +16.2218% | +14.7202% | +16.1150% | +16.2155% |

- The first-order error is of order $`(\Delta y)^{2}`$ and has the same sign for rises and falls. The convex curve lies above its tangent line, so duration alone understates the price in both directions.
- The second-order error is of order $`(\Delta y)^{3}`$ and changes sign with $`\Delta y`$, because $`P''' < 0`$.

## 6. Convexity is duration squared plus variance

Treat the payment time $`T`$ as a random variable that takes the value $`t`$ with probability $`w_t`$. Then $`D_{mac} = E[T]`$. Under continuous compounding, differentiate twice with respect to $`\delta`$:

```math
\frac{1}{P}\frac{d^{2}P}{d\delta^{2}} = \sum_{t} t^{2}\,w_t = E[T^{2}] = D_{mac}^{2} + \operatorname{Var}(T)
```

At equal duration, a bond whose payments are more spread out in time has more convexity. That is why a barbell is more convex than a bullet.

**Running example:** $`D_{mac} = 7.8017`$, $`\operatorname{Var}(T) = 9.6922`$, and $`E[T^{2}] = 70.5586 = 7.8017^{2} + 9.6922`$.

To return to the effective-yield convexity of Section 4, differentiate $`dP/dy = P_\delta/(1+y)`$ once more:

```math
\frac{d^{2}P}{dy^{2}} = \frac{P_{\delta\delta} - P_{\delta}}{(1+y)^{2}}
\quad\Rightarrow\quad
C = \frac{D_{mac}^{2} + \operatorname{Var}(T) + D_{mac}}{(1+y)^{2}}
```

**Check:** $`(70.5586 + 7.8017)/1.06^{2} = 69.7404`$, the same value as Section 4.

## 7. Redington immunization from derivatives

Let $`A(y)`$ and $`L(y)`$ be the present values of the asset and liability cash flows, and let $`S(y) = A(y) - L(y)`$ be the surplus. Assume a single parallel shift in yield. Redington (1952) showed that the surplus is protected at $`y_0`$ if:

1. $`S(y_0) = 0`$, so $`A(y_0) = L(y_0)`$.
2. $`S'(y_0) = 0`$, so $`A'(y_0) = L'(y_0)`$. With equal present values this means equal duration.
3. $`S''(y_0) > 0`$, so $`A''(y_0) > L''(y_0)`$. The assets must be more convex than the liabilities.

Then $`y_0`$ is a strict local minimum of $`S`$ with $`S(y_0) = 0`$. By the second-derivative test and the Taylor expansion:

```math
\Delta S \approx \tfrac{1}{2}\,S''(y_0)\,(\Delta y)^{2} > 0
```

so any small move in yield, up or down, raises the surplus. When both sides have the same Macaulay duration, the second derivative reduces to a difference of variances:

```math
S''(y_0) = \frac{L(y_0)}{(1+y_0)^{2}}\left[\operatorname{Var}_A(T) - \operatorname{Var}_L(T)\right]
```

**Worked example.** A liability of \$1,000 is due in 8 years and $`y = 6\%`$, so $`L = \$627.41`$. The assets are zero-coupon bonds maturing in years 5 and 12.

- Match duration: $`5w + 12(1-w) = 8`$, so $`w = 4/7`$. Buy \$358.52 of the 5-year zero and \$268.89 of the 12-year zero.
- Convexity condition: $`E[T^{2}]`$ is $`0.5714\times 25 + 0.4286\times 144 = 76`$ for the assets and $`64`$ for the liability, so the variance difference is 12.
- Result: $`S''(6\%) = 627.41/1.06^{2}\times 12 = 6{,}701`$.

| Yield | 4.0% | 5.0% | 5.5% | 6.0% | 6.5% | 7.0% | 8.0% |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Surplus $`S`$ (\$) | 1.60 | 0.37 | 0.09 | 0.00 | 0.08 | 0.31 | 1.13 |

At a 1-point move, $`\tfrac{1}{2}(6701)(0.01)^{2} = \$0.34`$, close to the table's \$0.37 and \$0.31.

**Limits.** The result holds for small, instantaneous, parallel shifts. Duration drifts as time passes, so the portfolio must be rebalanced. See BKM Section 16.3.

## 8. Checking with software

The notebook [`FIN4000_Supp02_Notebook.ipynb`](../../notebooks/python/FIN4000_Supp02_Notebook.ipynb) runs these checks. SymPy differentiates the price formula:

```python
import sympy as sp
y = sp.symbols('y')
P = sum(60/(1+y)**t for t in range(1, 11)) + 1000/(1+y)**10
Dstar = -sp.diff(P, y) / P         # D* = -(1/P) dP/dy
C = sp.diff(P, y, 2) / P           # C = (1/P) d2P/dy2
Dstar.subs(y, 0.06), C.subs(y, 0.06)   # 7.3601, 69.7404
```

QuantLib returns the same numbers from the bond object:

```python
ql.BondFunctions.duration(bond, rate, ql.Duration.Modified)   # 7.3601
ql.BondFunctions.convexity(bond, rate)                        # 69.7404
```

A central finite difference shows the derivative as a limit. With step $`h`$ in the yield:

| Step $`h`$ | $`D^{*}`$ (central difference) | $`C`$ (second difference) |
| --- | --- | --- |
| 0.01 | 7.3727 | 69.8153 |
| 0.001 | 7.3602 | 69.7411 |
| 0.0001 | 7.3601 | 69.7404 |

## 9. Looking ahead: random rates

Everything above treats $`y`$ as one number that is shifted deterministically. In derivatives and risk-management courses, the short rate $`r`$ is a random process, for example the Vasicek model:

```math
dr = a\,(b - r)\,dt + \sigma\,dW
```

Itô's lemma gives the price dynamics of a bond $`P(t, r)`$, where $`\mu = a(b - r)`$ is the drift of $`r`$:

```math
dP = \left(P_t + \mu P_r + \tfrac{1}{2}\,\sigma^{2}P_{rr}\right)dt + \sigma P_r\,dW
```

The term $`\tfrac{1}{2}\sigma^{2}P_{rr}`$ is the convexity term again, now multiplied by the variance of the rate. For a zero-coupon bond under Vasicek, $`-\partial\ln P/\partial r = (1 - e^{-a\tau})/a`$, which is less than the maturity $`\tau`$: with $`a = 0.1`$ and $`\tau = 10`$ it is 6.32 years. Mean reversion shortens effective duration. As $`a \to 0`$ it approaches $`\tau`$, which recovers "a zero's duration equals its maturity."

## 10. Practice set

1. Derive $`D^{*}`$ and $`C`$ for a zero-coupon bond from $`P(y) = F(1+y)^{-T}`$. *Answer:* $`D^{*} = T/(1+y)`$ and $`C = T(T+1)/(1+y)^{2}`$.
2. For a perpetuity paying $`c`$ a year, show that $`D^{*} = 1/y`$, $`C = 2/y^{2}`$ and $`D_{mac} = (1+y)/y`$. Evaluate at $`y = 5\%`$. *Answer:* 20, 800 and 21.
3. For the running example, use the third-order term to estimate the price change when yield rises 1 point. *Answer:* $`-7.0114\% + \tfrac{1}{6}(-753.69)(0.01)^{3} = -7.0239\%`$; the exact change is $`-7.0236\%`$.
4. Use $`D^{*} = -d\ln P/dy`$ to explain why $`D^{*}`$ is the percentage price change per unit of yield. *Answer:* $`d\ln P = dP/P`$, so $`d\ln P/dy`$ is the relative price change per unit change in $`y`$.
5. A bullet pays \$1 at year 8. A barbell pays \$0.50 (in present value terms) at each of years 4 and 12. Both have $`D_{mac} = 8`$. Find $`E[T^{2}]`$ for each and the effective-yield convexity at $`y = 6\%`$. *Answer:* 64 and 80; $`(64+8)/1.06^{2} = 64.08`$ and $`(80+8)/1.06^{2} = 78.32`$. The variance difference is 16.
6. A liability of \$1,000 is due in 10 years at $`y = 5\%`$. Immunize it with zero-coupon bonds maturing in years 6 and 14. Find the weights and check the convexity condition. *Answer:* $`6w + 14(1-w) = 10`$, so $`w = 0.5`$: \$306.96 of each, since $`L = \$613.91`$. $`E[T^{2}] = 0.5(36) + 0.5(196) = 116 > 100`$, so the third condition holds.

## 11. Reading and open-source resources

- Bodie, Kane & Marcus, *Investments*, 13th ed., Chapter 16, especially Sections 16.1 (duration), 16.2 (convexity) and 16.3 (immunization).
- [Society of Actuaries, *Using Duration and Convexity to Approximate Change in Present Value*](https://www.soa.org/Files/Edu/2017/fm-duration-convexity-present-value.pdf) (free PDF with derivation appendices).
- F. M. Redington, "Review of the Principles of Life-Office Valuations," *Journal of the Institute of Actuaries* 78 (1952), 286–340.
- [QuantLib](https://www.quantlib.org): `BondFunctions.duration`, `convexity` and `basisPointValue`, and the Vasicek and Hull-White short-rate models.
- [SymPy](https://www.sympy.org) for symbolic derivatives.
- [JuliaActuary](https://github.com/JuliaActuary): ActuaryUtilities.jl has `duration` and `convexity`, and is in this course's Julia environment.
- R package FinancialMath: `cf.analysis()` computes the same sums.
- [MIT OpenCourseWare 18.S096](https://ocw.mit.edu/courses/18-s096-topics-in-mathematics-with-applications-in-finance-fall-2013/pages/calendar/): Lecture 18 (Itô calculus), Lecture 21 (stochastic differential equations) and Lecture 24 (the HJM interest-rate model).

---

## Key Terms

*Make sure you can define each of these in your own words.*

- [ ] price function $`P(y)`$
- [ ] modified duration $`D^{*}`$
- [ ] Macaulay duration
- [ ] volatility (actuarial)
- [ ] discounted mean term
- [ ] payment-time weights
- [ ] DV01
- [ ] convexity $`C`$
- [ ] Taylor series
- [ ] Lagrange remainder
- [ ] force of interest $`\delta`$
- [ ] variance of payment times
- [ ] barbell and bullet
- [ ] surplus function $`S(y)`$
- [ ] Redington immunization
- [ ] second-derivative test
- [ ] short-rate model

---

## Key Equations

**Modified duration**

```math
D^{*} = -\frac{1}{P}\frac{dP}{dy} = -\frac{d\ln P}{dy} = \frac{D_{mac}}{1+y}
```

**Convexity**

```math
C = \frac{1}{P}\frac{d^{2}P}{dy^{2}} = \frac{1}{P\,(1+y)^{2}}\sum_{t} t(t+1)\,PV_t
```

**Price change**

```math
\frac{\Delta P}{P} \approx -D^{*}\,\Delta y + \tfrac{1}{2}\,C\,(\Delta y)^{2}
```

**Convexity and dispersion (continuous compounding)**

```math
\frac{1}{P}\frac{d^{2}P}{d\delta^{2}} = D_{mac}^{2} + \operatorname{Var}(T)
```

**Redington conditions**

```math
S(y_0) = 0 \qquad S'(y_0) = 0 \qquad S''(y_0) > 0
```

---

*Study guide supplement for the "Duration, Convexity & Weighted Average Life" slide deck. BKM section references are to Investments, 13th Edition, Chapter 16 (Managing Bond Portfolios). Numerical results were checked with SymPy and QuantLib.*
