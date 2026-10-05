# Mini Study Guide 2: Short Sales and Margin Calls

*FIN 4000 Investments · Midterm prep · BKM Ch. 3*

[← All study guides](../../study-guide-index.md)

## Learning objectives

A short seller gets a margin call when the stock price *rises* far enough that equity falls below the maintenance margin. Most exam errors come from reusing the long-position formula.

After this guide you should be able to:

1. Set up a short-sale margin account: assets, liability, and equity.
2. Compute the margin percentage at any price.
3. Solve for the price that triggers a margin call.
4. Compute the cash needed to meet a margin call.
5. Compute the return on a short sale, including dividends the short seller must pay.

## Core concept: the short-sale account

To sell short, you borrow shares from your broker, sell them, and must later buy them back to return them. The sale proceeds stay in your account; you cannot withdraw them. You also post initial margin (cash or T-bills).

| Account item | Amount | Changes when price moves? |
| --- | --- | --- |
| Asset: sale proceeds | n × P₀ | No (fixed) |
| Asset: margin deposit | IM × n × P₀ | No (unless you add cash or pay dividends) |
| Liability: shares owed | n × P | Yes (rises when P rises) |
| Equity | Total assets − n × P | Falls when P rises |

**Margin percentage** on a short position:

```math
\text{Margin} = \frac{\text{Equity}}{\text{Value of shares owed}} = \frac{(\text{Proceeds} + \text{Deposit}) - nP}{nP}
```

**Where:**

- Equity = account assets minus the current value of the shares owed
- Proceeds = n × P₀, the cash received from the short sale
- Deposit = the initial margin posted, IM × n × P₀
- n = number of shares sold short
- P = current share price

**Margin call price.** Set margin equal to the maintenance margin (MM) and solve for P:

```math
P^{*} = \frac{\text{Proceeds} + \text{Deposit}}{n\,(1 + MM)} = \frac{P_0\,(1 + IM)}{1 + MM}
```

**Where:**

- P* = the share price that triggers a margin call
- Proceeds, Deposit, n = as defined above
- MM = maintenance margin, as a decimal
- P₀ = price at which the shares were sold short
- IM = initial margin, as a decimal
- Loan (long position, table below) = amount borrowed from the broker

**Long vs. short margin: side by side.**

| | Buying on margin (long) | Short sale |
| --- | --- | --- |
| You lose when | Price falls | Price rises |
| Liability | Broker loan (fixed dollars) | Shares owed (n × P, moves with price) |
| Equity | nP − Loan | (Proceeds + Deposit) − nP |
| Margin ratio | Equity / nP | Equity / nP |
| Margin call when | P falls to Loan / [n(1 − MM)] | P rises to (Proceeds + Deposit) / [n(1 + MM)] |
| Maximum loss | Initial equity plus the loan (price goes to 0) | Unlimited in theory |
| Dividends | You receive them | You pay them to the share lender |

## Worked examples

### Example 1: Margin call price (Algorithmic)

You short 1,000 shares at \$100. Initial margin is 50% and maintenance margin is 30%.

1. Proceeds = 1,000 × \$100 = \$100,000.
2. Deposit = 0.50 × \$100,000 = \$50,000.
3. Total assets = \$150,000 (fixed).
4. Margin call price: P* = \$150,000 / [1,000 × (1 + 0.30)] = **\$115.38**.

**Check:** at \$115.38, shares owed = \$115,385 and equity = \$150,000 − \$115,385 = \$34,615. Margin = 34,615 / 115,385 = 30%.

**BA II Plus:** `150000` `÷` `1.3` `÷` `1000` `=` → 115.38

### Example 2: Meeting the margin call (Algorithmic)

The stock in Example 1 rises to \$120.

1. Shares owed = \$120,000. Equity = \$150,000 − \$120,000 = \$30,000.
2. Margin = 30,000 / 120,000 = **25%**, which is below 30%: margin call.
3. Equity required at 30% maintenance = 0.30 × \$120,000 = \$36,000.
4. Cash to deposit = \$36,000 − \$30,000 = **\$6,000**.

*Brokers sometimes require you to restore margin to the initial level instead. At 50%, you would need 0.50 × \$120,000 − \$30,000 = \$30,000. Read the question for which level applies.*

### Example 3: Dividends and the return on a short sale (Algorithmic)

You short 500 shares at \$40 with 50% initial margin (\$10,000 deposit) and 25% maintenance margin. The stock pays a \$1.00 dividend while you are short.

1. Margin call price with no dividend: \$30,000 / (500 × 1.25) = **\$48.00**.
2. The \$500 dividend is paid out of your account, so total assets fall to \$29,500. New margin call price: \$29,500 / 625 = **\$47.20**. The dividend brings the margin call closer.
3. You cover at \$44. Loss on shares = (44 − 40) × 500 = \$2,000. Plus dividend = \$500. Total loss = \$2,500.
4. Return on initial margin = −\$2,500 / \$10,000 = **−25%**.

**If instead you cover at \$34:** gain = (40 − 34) × 500 − \$500 = \$2,500, a return of **+25%**.

```math
r_{\text{short}} = \frac{n\,(P_0 - P_1) - n \times D}{\text{Initial margin deposit}}
```

**Where:**

- r(short) = return on the short position, measured on the margin deposit
- n = number of shares sold short
- P₀ = price at which the shares were sold
- P₁ = price at which the position is covered
- D = dividend per share paid while the position is open
- Initial margin deposit = cash posted when the position was opened

### Example 4: Compare with a long margin purchase

You buy 1,000 shares at \$100 with 50% initial margin (a \$50,000 loan) and 30% maintenance margin.

- Margin call price = Loan / [n(1 − MM)] = \$50,000 / (1,000 × 0.70) = **\$71.43**.
- The long position is called on a 28.6% price *drop*. The short in Example 1 is called on a 15.4% price *rise*.

## Common pitfalls

- **Using the long formula.** A short's margin call comes on a price *rise*. If your answer is below P₀, recheck.
- **Forgetting the proceeds.** Total assets = proceeds + deposit, not the deposit alone.
- **Dividing by the wrong base.** Margin = equity / *current* value of shares owed (n × P), not initial value.
- **Dropping dividends.** The short seller pays them. They lower the return and the margin call price.
- **Return base.** Return is measured on the initial margin deposit, not on the proceeds.

## Key terms and definitions

- [ ] **Short sale:** selling borrowed shares in the hope of buying them back later at a lower price.
- [ ] **Covering (closing) a short position:** buying shares to return to the lender, which ends the short position.
- [ ] **Initial margin:** the minimum equity, as a percentage of position value, required to open the position.
- [ ] **Maintenance margin:** the minimum equity percentage that must be kept; falling below it triggers a margin call.
- [ ] **Margin call:** the broker's demand for more cash or securities, or a closed position, when margin falls below maintenance.
- [ ] **Short interest:** the number of shares of a stock currently sold short.
- [ ] **Short squeeze:** a rapid price rise that forces short sellers to cover, which pushes the price higher still.
- [ ] **Stop-buy order:** an order to buy if the price rises to a stated level; used to cap losses on a short sale.
- [ ] **Uptick rule / alternative uptick rule (SEC Rule 201):** once a stock falls 10% or more in a day, short sales are allowed only above the current national best bid for the rest of that day and the next.

## CFA-style practice questions

**Q1 [Algorithmic].** An investor shorts 2,000 shares at \$60 with 50% initial margin and 30% maintenance margin. The price at which she receives a margin call is *closest* to:

- A. \$42.86
- B. \$69.23
- C. \$78.00

**Q2 [Algorithmic].** Using the position in Q1, the stock rises to \$72. Her margin percentage is *closest* to:

- A. 20.0%
- B. 25.0%
- C. 33.3%

**Q3 [Algorithmic].** At \$72, how much cash must she deposit to restore the account to the 30% maintenance margin?

- A. \$7,200
- B. \$36,000
- C. \$43,200

**Q4 [Algorithmic].** An investor shorts 1,000 shares at \$50 with 50% initial margin. The stock pays a \$0.50 dividend and she covers at \$42. Her return on the margin deposit is *closest* to:

- A. 15%
- B. 30%
- C. 32%

**Q5 [Conceptual].** The potential loss on a short sale is theoretically unlimited because:

- A. the stock price has no upper limit.
- B. the broker can charge unlimited interest on borrowed shares.
- C. the short seller must pay all future dividends.

**Q6 [Algorithmic].** A short sale is opened at \$100 with 50% initial margin. If maintenance margin is 40% instead of 30%, the margin call price is *closest* to:

- A. \$107.14
- B. \$115.38
- C. \$125.00

**Q7 [Conceptual].** The proceeds from a short sale:

- A. may be withdrawn to buy other securities.
- B. must stay in the investor's margin account.
- C. are paid to the investor whose shares were borrowed.

**Q8 [Conceptual].** When a stock that has been sold short pays a cash dividend:

- A. the short seller receives the dividend.
- B. the short seller must pay the dividend to the lender of the shares.
- C. no one receives the dividend on the borrowed shares.

## Answer key

| Q | Answer | Explanation |
| --- | ------ | ------------------------------------------------------ |
| 1 | B | Proceeds \$120,000 + deposit \$60,000 = \$180,000. P* = 180,000 / (2,000 × 1.30) = \$69.23. A applies the long formula; C is 60 × 1.30. |
| 2 | B | Shares owed = \$144,000. Equity = 180,000 − 144,000 = \$36,000. Margin = 36,000 / 144,000 = 25%. |
| 3 | A | Required equity = 0.30 × 144,000 = \$43,200. Deposit = 43,200 − 36,000 = \$7,200. C is the total required equity, not the shortfall. B restores to 50%. |
| 4 | B | Gain = (50 − 42) × 1,000 − \$500 dividend = \$7,500. Deposit = \$25,000. Return = 30%. C ignores the dividend (32%); A divides by the \$50,000 proceeds. |
| 5 | A | A stock price can rise without limit, so the cost to cover has no ceiling. |
| 6 | A | P* = 100 × 1.50 / 1.40 = \$107.14. A higher maintenance margin triggers the call sooner (at a lower price). B uses 30%. |
| 7 | B | Proceeds stay with the broker as collateral for the borrowed shares. |
| 8 | B | The lender of the shares is entitled to the dividend, so the short seller must pay it. |
