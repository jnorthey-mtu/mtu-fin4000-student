# Sharpe Ratio and Risk & Risk Premiums (BKM 13e §5.3)

**FIN 4000 Investments — General Study Guide gen-10 (Chapter 5)**

*Big picture: §5.3 turns "how did the investment do?" into "how much reward did I earn per unit of risk?" You compute expected return and standard deviation from scenarios, subtract the risk-free rate to get the risk premium, and divide by $\sigma$ to get the Sharpe ratio, the number used to compare portfolios on equal footing.*

---

## Learning Objectives

By the end of this guide you should be able to:

1. Compute a holding-period return (HPR) from prices and dividends.
2. Compute **expected return**, **variance**, and **standard deviation** from a scenario table.
3. Distinguish **risk premium** (expected) from **excess return** (realized).
4. Compute and interpret the **Sharpe ratio** (reward-to-volatility ratio) from scenario data or from historical excess returns.
5. Compare portfolios using the Sharpe ratio, and explain why mixing a portfolio with T-bills does not change it.
6. Annualize a monthly Sharpe ratio.

---

## Core Concept

### 1. Holding-period return

$$
HPR = \frac{P_1 - P_0 + D_1}{P_0}
$$
Return is uncertain, so we describe it with a **scenario analysis**: a list of states $s$, each with a probability $p(s)$ and a return $r(s)$.

### 2. Expected return, variance, standard deviation

$$
E(r) = \sum_s p(s)\, r(s)
$$
$$
\sigma^2 = \sum_s p(s)\,\big[r(s) - E(r)\big]^2
$$
$$
\sigma = \sqrt{\sigma^2}
$$
$\sigma$ is the standard measure of total risk in this chapter.

### 3. Risk-free rate, risk premium, excess return

- **Risk-free rate** ($r_f$): the return on T-bills, the benchmark safe asset.
- **Risk premium** (what you *expect* to earn for bearing risk):

$$
\text{Risk premium} = E(r) - r_f
$$
- **Excess return** (what you *actually* earned in a given period):

$$
\text{Excess return} = r - r_f
$$
The risk premium is the expected value of the excess return.

### 4. The Sharpe ratio

$$
\text{Sharpe ratio} = \frac{E(r_P) - r_f}{\sigma_P}
$$
- The numerator is the risk premium; the denominator is total risk.
- Interpretation: extra return earned per 1% of standard deviation. Higher is better.
- With historical data, let $R_t = r_t - r_{f,t}$ be the excess return in period $t$. Use the sample mean $\bar{R}$ and sample standard deviation $s_R$ of those excess returns:

$$
\text{Sharpe ratio} = \frac{\bar{R}}{s_R}
$$
- The Sharpe ratio is the **slope of the capital allocation line (CAL)** formed by combining the risk-free asset with portfolio $P$.
- Because every mix of $P$ and T-bills lies on the same line, **blending with T-bills (or borrowing at the risk-free rate) changes risk and return but not the Sharpe ratio.**

### 5. Annualizing

If the monthly Sharpe ratio is $S_m$, then

$$
S_{\text{annual}} \approx S_m \times \sqrt{12}
$$
The mean scales with 12, but $\sigma$ scales with $\sqrt{12}$.

---

## Worked Examples

### Example 1: Scenario analysis and Sharpe ratio

A stock has these scenarios. The T-bill rate is $r_f = 3\%$.

| State | Probability | Return |
|---|---|---|
| Boom | 0.30 | 30% |
| Normal | 0.50 | 12% |
| Recession | 0.20 | −18% |

**Expected return:**

$$
E(r) = 0.30(30) + 0.50(12) + 0.20(-18) = 9.0 + 6.0 - 3.6 = 11.4\%
$$
**Variance:**

$$
\sigma^2 = 0.30(30 - 11.4)^2 + 0.50(12 - 11.4)^2 + 0.20(-18 - 11.4)^2
$$
$$
\sigma^2 = 0.30(345.96) + 0.50(0.36) + 0.20(864.36) = 103.788 + 0.18 + 172.872 = 276.84
$$
**Standard deviation:**

$$
\sigma = \sqrt{276.84} = 16.64\%
$$
**Risk premium:**

$$
E(r) - r_f = 11.4 - 3 = 8.4\%
$$
**Sharpe ratio:**

$$
\text{Sharpe ratio} = \frac{8.4}{16.64} = 0.505
$$
**BA II Plus (statistics worksheet, probabilities entered as frequencies out of 100):**

1. `2nd` `DATA` (opens the data worksheet), then `2nd` `CLR WORK`
2. `X01` = 30 `ENTER` `↓`, `Y01` = 30 `ENTER` `↓`
3. `X02` = 12 `ENTER` `↓`, `Y02` = 50 `ENTER` `↓`
4. `X03` = 18 `+/-` `ENTER` `↓`, `Y03` = 20 `ENTER`
5. `2nd` `STAT`, press `2nd` `ENTER` until the mode reads `LIN`, then `↓` through the results:
   - $\bar{x}$ = 11.4 (this is $E(r)$)
   - $\sigma_x$ = 16.64 (**use the population value**, not the sample $S_x$, because the probabilities are the whole distribution)

Then compute the Sharpe ratio by hand: $(11.4 - 3) \div 16.64$.

---

### Example 2: Comparing two portfolios

$r_f = 3\%$.

| Portfolio | $E(r)$ | $\sigma$ |
|---|---|---|
| A | 12% | 20% |
| B | 9% | 11% |

$$
\text{Sharpe}_A = \frac{12 - 3}{20} = 0.450 \qquad \text{Sharpe}_B = \frac{9 - 3}{11} = 0.545
$$
**B is the better risk-adjusted performer** even though A has the higher expected return. Per unit of risk, B pays more.

---

### Example 3: Sharpe ratio from historical excess returns

Five years of a fund's **excess returns** $R_t = r_t - r_{f,t}$: 10%, −8%, 18%, 6%, 4%.

$$
\bar{R} = \frac{10 - 8 + 18 + 6 + 4}{5} = 6.0\%
$$
Deviations from the mean: 4, −14, 12, 0, −2. Squared: 16, 196, 144, 0, 4. Sum = 360.

$$
s^2 = \frac{360}{5 - 1} = 90 \qquad s = \sqrt{90} = 9.49\%
$$
$$
\text{Sharpe ratio} = \frac{6.0}{9.49} = 0.632
$$
**BA II Plus:**

1. `2nd` `DATA`, `2nd` `CLR WORK`
2. Enter `X01` = 10, `X02` = 8 `+/-`, `X03` = 18, `X04` = 6, `X05` = 4 (press `ENTER` `↓` after each)
3. `2nd` `STAT` (`LIN` mode), `↓` to read $\bar{x}$ = 6.0 and $S_x$ = 9.49 (**use the sample value** for historical data)
4. $6.0 \div 9.49 = 0.632$

---

### Example 4: Mixing a risky portfolio with T-bills

Portfolio $P$ has $E(r_P) = 14\%$, $\sigma_P = 22\%$, and $r_f = 4\%$.

$$
\text{Sharpe}_P = \frac{14 - 4}{22} = 0.4545
$$
**Target standard deviation of 11%** (invest weight $y$ in $P$, the rest in T-bills):

$$
y = \frac{11}{22} = 0.50 \qquad E(r) = r_f + y\,[E(r_P) - r_f] = 4 + 0.50(10) = 9\%
$$
$$
\text{Sharpe} = \frac{9 - 4}{11} = 0.4545 \quad \text{(unchanged)}
$$
**Target standard deviation of 33%** (borrow at $r_f$ to invest $y = 1.5$ in $P$):

$$
E(r) = 4 + 1.5(10) = 19\% \qquad \text{Sharpe} = \frac{19 - 4}{33} = 0.4545 \quad \text{(unchanged)}
$$
Leverage and de-leveraging slide you along the same CAL; the slope is the Sharpe ratio.

---

### Example 5: Annualizing a monthly Sharpe ratio

A fund has an average monthly excess return of 0.6% and a monthly standard deviation of 3.0%.

$$
S_m = \frac{0.6}{3.0} = 0.20 \qquad S_{\text{annual}} = 0.20 \times \sqrt{12} = 0.693
$$
Check: annual mean excess return $= 0.6 \times 12 = 7.2\%$; annual $\sigma = 3.0 \times \sqrt{12} = 10.39\%$; $7.2 \div 10.39 = 0.693$.

---

## Common Pitfalls

- **Forgetting to subtract the risk-free rate.** Return $\div\ \sigma$ is *not* the Sharpe ratio. The numerator must be the excess return or risk premium.
- **Population vs. sample standard deviation.** Scenario tables (the full probability distribution) use the population $\sigma_x$. A time series of historical returns uses the sample $S_x$ (divide by $n - 1$).
- **Mixing units.** Keep $E(r)$, $r_f$, and $\sigma$ all in percent (or all in decimals) before dividing.
- **Risk premium vs. excess return.** The risk premium is *expected*; the excess return is *realized*. Scenario problems use the premium; historical problems use average excess returns.
- **Comparing Sharpe ratios built on different risk-free rates or different periods.** Compare like with like.
- **Thinking leverage changes the Sharpe ratio.** Mixing with T-bills or borrowing at $r_f$ scales the premium and $\sigma$ by the same factor, so the ratio is unchanged.
- **Annualizing the standard deviation by 12.** $\sigma$ scales with $\sqrt{12}$, not 12, and so does the Sharpe ratio.
- **Misreading a negative Sharpe ratio.** A negative value means the portfolio earned less than T-bills. Interpret the sign before ranking.
- **Treating standard deviation as the only risk.** The Sharpe ratio uses *total* risk, which suits an investor's whole portfolio; it is not a beta-based measure.

---

## Key Terms Checklist

*Make sure you can define each in your own words.*

| | | |
|---|---|---|
| ☐ holding-period return (HPR) | ☐ scenario analysis | ☐ probability distribution |
| ☐ expected return $E(r)$ | ☐ variance $\sigma^2$ | ☐ standard deviation $\sigma$ |
| ☐ risk-free rate $r_f$ | ☐ risk premium | ☐ excess return |
| ☐ reward-to-volatility (Sharpe) ratio | ☐ capital allocation line (CAL) | ☐ risk aversion |
| ☐ population vs. sample standard deviation | ☐ annualizing ($\sqrt{12}$ rule) | ☐ total risk |

---

## Practice Questions (CFA-style, choose A, B, or C)

**Q1.** The Sharpe ratio measures:

- A. excess return per unit of total risk (standard deviation)
- B. excess return per unit of beta
- C. total return per unit of standard deviation

**Q2.** A portfolio has an expected return of 10%, a standard deviation of 15%, and the T-bill rate is 2.5%. The Sharpe ratio is closest to:

- A. 0.50
- B. 0.67
- C. 0.17

**Q3.** Fund X has $E(r) = 11\%$ and $\sigma = 18\%$. Fund Y has $E(r) = 8\%$ and $\sigma = 10\%$. The risk-free rate is 3%. Based on the Sharpe ratio:

- A. Fund X is better because its expected return is higher
- B. Fund Y is better
- C. The funds are equivalent

**Q4.** A stock has three scenarios: 25% probability of a 40% return, 50% probability of a 10% return, and 25% probability of a −20% return. The standard deviation of returns is closest to:

- A. 21.2%
- B. 15.0%
- C. 450%

**Q5.** An investor moves part of a risky portfolio $P$ into T-bills to reduce risk. The Sharpe ratio of the resulting mix will:

- A. increase
- B. stay the same
- C. decrease

**Q6.** A fund's monthly Sharpe ratio is 0.25. The annualized Sharpe ratio is closest to:

- A. 0.87
- B. 3.00
- C. 0.07

**Q7.** The slope of the capital allocation line combining the risk-free asset with risky portfolio $P$ equals:

- A. the beta of $P$
- B. the Sharpe ratio of $P$
- C. the expected return of $P$

**Q8.** Over three years, a fund's excess returns were 12%, −4%, and 10%. Using the sample standard deviation, the Sharpe ratio is closest to:

- A. 0.69
- B. 0.84
- C. 0.50

---

## Answer Key

**Q1. A.** $\text{Sharpe} = [E(r) - r_f] \div \sigma$. B describes a Treynor-style measure (per unit of beta), and C leaves out the subtraction of $r_f$.

**Q2. A.**

$$
\frac{10 - 2.5}{15} = \frac{7.5}{15} = 0.50
$$
B (0.67) divides by 11.25, which is not the standard deviation. C (0.17) divides by the wrong quantity.

**Q3. B.**

$$
\text{Sharpe}_X = \frac{11 - 3}{18} = 0.444 \qquad \text{Sharpe}_Y = \frac{8 - 3}{10} = 0.500
$$
Y earns more premium per unit of risk. A ignores risk.

**Q4. A.**

$$
E(r) = 0.25(40) + 0.50(10) + 0.25(-20) = 10\%
$$
$$
\sigma^2 = 0.25(30)^2 + 0.50(0)^2 + 0.25(-30)^2 = 225 + 0 + 225 = 450
$$
$$
\sigma = \sqrt{450} = 21.2\%
$$
C reports the variance, not the standard deviation. B is not supported by any calculation.

**Q5. B.** Mixing $P$ with T-bills moves you along the same CAL, scaling the premium and $\sigma$ by the same factor, so the slope (Sharpe ratio) does not change.

**Q6. A.**

$$
S_{\text{annual}} = 0.25 \times \sqrt{12} = 0.25 \times 3.464 = 0.866 \approx 0.87
$$
B multiplies by 12 (wrong scaling). C divides by $\sqrt{12}$ (wrong direction).

**Q7. B.** The CAL runs from $(0, r_f)$ through $P$; its slope is $[E(r_P) - r_f] \div \sigma_P$, the Sharpe ratio.

**Q8. A.**

$$
\bar{R} = \frac{12 - 4 + 10}{3} = 6.0\%
$$
Deviations: 6, −10, 4. Squared: 36, 100, 16. Sum = 152.

$$
s^2 = \frac{152}{2} = 76 \qquad s = 8.72\% \qquad \text{Sharpe ratio} = \frac{6.0}{8.72} = 0.69
$$
B uses the population $\sigma$ (7.12%), which is wrong for historical sample data.

---

*Study guide gen-10 for BKM (13th ed.), Chapter 5, §5.3 "Risk and Risk Premiums" (Sharpe ratio / reward-to-volatility ratio). All numeric answers were checked with Python.*
