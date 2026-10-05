# Current Events Study Guide 2: Dividend Stocks, Inflation and Covered Calls

*BKM Ch. 2, with Ch. 5, 17, 18, 20 and 21*

[← All study guides](../../study-guide-index.md)

FIN 4000 Investments · Sep 30, 2026 · Jim Northey

## Why this matters

When inflation runs hot, a fixed dividend loses purchasing power, so income investors are turning to a familiar tool: selling call options against the dividend stocks they already own. A recent Barron's article (published Sept. 29–30, 2026) describes this call-overwriting approach as a way to enhance dividend income. It is a live case study for BKM Chapter 2, and it points ahead to Chapters 5, 17, 18, 20 and 21.

**Learning objectives.** After this guide you should be able to:

1. Explain how a covered call combines a dividend stock with a short call, and compute its income, breakeven and maximum profit.
2. Distinguish nominal from real income, and explain why a capped-upside strategy interacts with inflation.
3. Use put-call parity to show that a covered call has the same payoff shape as a written put.
4. Argue both sides of the question: are options valid investments or mere speculative trading?

**Open item for Jim.** I could not retrieve the Barron's piece itself (paywalled, and my search did not surface it). Paste the headline, author, link and any tickers or yields it cites, and I will fold them into the next section.

## The strategy: enhancing dividends with call options

The strategy is a covered call (call overwriting): own a dividend-paying stock and sell a call option on it, collecting the premium as extra income. Details of the Barron's article (author, tickers, yields quoted) still need to be added from the original.

**How it works.**

1. Buy or hold 100 shares of a dividend payer for each call contract sold.
2. Sell an out-of-the-money call, typically 1–3 months out, and collect the premium up front.
3. If the stock stays below the strike at expiration, the call expires worthless. You keep the premium, the dividends and the shares, then repeat.
4. If the stock finishes above the strike, the shares are called away at the strike price. You keep the premium and dividends, but give up gains above the strike.

**Why it appeals when inflation is high.**

- A stock's dividend is set in nominal dollars and adjusts slowly, so a 3.5% yield in a 4% inflation year is a negative real yield. Option premium adds a second cash stream on top of it.
- Higher and more volatile inflation tends to raise market volatility, and option premiums rise with volatility (BKM Ch. 21). Sellers are paid more for the same strike.
- Mature dividend payers often trade in a range, which is the situation where the capped upside costs the least.

**What you give up.** The premium is not free income. You pay for it with the right tail of the return distribution, and the premium is a fixed nominal amount that does not grow with inflation. In a strong rally, a covered call trails the plain stock. In a sell-off, the premium cushions only a small part of the loss.

## BKM connections

Chapter 2 is the anchor: its derivative-markets section defines calls and puts and shows the payoff of buying and writing each. Chapter numbers below follow BKM 13e; confirm against your edition.

| Chapter | Concept | Link to this story |
| --- | --- | --- |
| Ch. 2 Asset Classes and Financial Instruments | Equity, dividend yield, call and put options | A covered call packages a common stock with a short call. Dividend yield is only one part of total return. |
| Ch. 3 How Securities Are Traded | Exchange-listed options, margin, short positions | Calls are written on listed exchanges. A covered call is fully collateralized by the shares, unlike a naked short call, which needs margin. |
| Ch. 5 Risk and Return | Nominal vs. real return, Fisher relation, skewed returns | Judge the strategy by real income. Selling calls trades away positive skew for income. |
| Ch. 9 CAPM and Ch. 13 EMH | Risk-adjusted return; can premium be earned for free? | If option prices are fair, extra income comes with extra risk. Any excess return must come from a volatility risk premium. |
| Ch. 17 Macroeconomic Analysis | Inflation, interest rates, sector rotation | Inflation regimes favor some sectors, such as energy and staples, and pressure rate-sensitive dividend payers such as utilities and REITs. |
| Ch. 18 Equity Valuation | Dividend discount model, P0 = D1 / (k − g) | Inflation raises the required return k. Whether it also raises dividend growth g decides whether the stock's price holds up. |
| Ch. 20 Options Markets: Introduction | Covered calls, protective puts, collars, put-call parity | The core chapter for this guide: payoff diagrams and strategy comparisons. |
| Ch. 21 Option Valuation | Black-Scholes, delta, implied volatility | The premium you collect is set by implied volatility. Delta of the short call is roughly the chance the shares get called away. |

**Put-call parity connection.** With no dividends, parity gives C + PV(X) = P + S. Rearranging, S − C = PV(X) − P. Owning the stock and writing a call has the same payoff shape as holding a bond and writing a put. A covered call is therefore economically close to a short put, and it carries a short put's risk of large losses if the stock falls.

## Worked example: stock plus covered call

A hypothetical dividend stock (illustrative numbers, not from the article) trades at \$50 and pays \$0.50 per quarter (\$2.00 a year, a 4.0% yield). You sell a 3-month call with a \$52.50 strike for a \$0.75 premium. Assume the stock goes ex-dividend after you sell the call and the call is European style, so early exercise is ignored.

**Step 1: income.** Dividend yield per quarter = 0.50 / 50 = 1.00%. Premium yield per quarter = 0.75 / 50 = 1.50%. Total income = 2.50% per quarter.

**Step 2: breakeven.** Breakeven = 50 − 0.75 − 0.50 = \$48.75. The stock can fall 2.5% before the position loses money.

**Step 3: maximum profit.** The shares are called away at \$52.50, so the maximum is (52.50 − 50) + 0.50 + 0.75 = \$3.75, or 7.5% of the \$50 cost.

**Step 4: annualize.** Repeating 2.5% each quarter compounds to (1.025)^4 − 1 = 10.38%, against a 4.0% dividend alone. That is the appeal, but it holds only if the stock stays below the strike every quarter.

**BA II Plus keystrokes.** Premium yield: 0.75 ÷ 50 = 1.5%. Annualized: 1.025 [y^x] 4 [=] − 1 [=], then × 100 [=] gives 10.38.

Profit per share at expiration, including the dividend and premium:

| Stock price at expiration | Stock only | Covered call | Covered call minus stock only |
| --- | --- | --- | --- |
| \$45.00 | −\$4.50 | −\$3.75 | +\$0.75 |
| \$50.00 | +\$0.50 | +\$1.25 | +\$0.75 |
| \$52.50 | +\$3.00 | +\$3.75 | +\$0.75 |
| \$55.00 | +\$5.50 | +\$3.75 | −\$1.75 |
| \$60.00 | +\$10.50 | +\$3.75 | −\$6.75 |

The covered call wins by exactly the premium up to the strike, then loses one dollar for each dollar the stock rises above it. The formula behind the table:

```math
\text{Profit} = (S_T - S_0) + D + C_0 - \max(S_T - X,\, 0)
```

Here S\_T is the stock price at expiration, S\_0 the purchase price, D the dividends received, C\_0 the premium and X the strike.

**Inflation twist.** Suppose inflation is 4% a year. The 10.38% best-case nominal income is about a 6.1% real income, using the Fisher relation (1.1038 / 1.04 − 1). The stock-only investor has a 4.0% nominal yield, about zero real, but keeps the full price upside. In an inflationary rally, that upside is the part you sold.

## Discussion question: are options investments or speculative trading?

**The question.** Many investors call any option position gambling. Is that fair? The answer this guide defends: options are instruments, not a style. Used to hedge, to earn income on holdings or to reshape risk, they can be part of a strategic investment portfolio. Used as leveraged bets on short-term price moves, they are speculation.

**McMillan's argument.** Lawrence McMillan's *Options as a Strategic Investment* (first published 1980, updated through several editions) is the standard practitioner reference on this point. Paraphrasing his thesis: options are best understood as strategic tools that can be matched to a market view and a risk tolerance, ranging from conservative (covered writing, protective puts) to aggressive (naked writing, speculative buying). The book's long treatments of covered call writing and of using options to hedge stock holdings are why it is often cited against the view that options are inherently speculative. Verify page and edition references against your copy before quoting.

**BKM's definitions.** BKM Chapter 5 separates speculation from gambling. Speculation means taking considerable risk in return for a commensurate gain, meaning a positive risk premium. Gambling means bearing risk for enjoyment with no such premium. Apply the definitions to the position, not the instrument.

| Position | Risk relative to holding the stock alone | Typical purpose | Reads as |
| --- | --- | --- | --- |
| Covered call | Lower volatility, capped upside, small cushion on losses | Income on an existing holding | Investment |
| Protective put (BKM Ch. 20) | Floors the loss at the strike less the put cost | Insurance | Investment |
| Collar | Floor and cap, often near zero net cost | Protect a concentrated position | Investment |
| Long out-of-the-money call | New leveraged exposure that can expire worthless | Bet on a big move | Speculation |
| Naked short call | Unlimited loss if the stock rallies | Collect premium with no offsetting position | Speculation |

**A test you can apply.** Ask four questions about any option position. What existing risk or goal does it serve? Does it lower or raise total portfolio risk? Is the size small enough that a total loss of the premium, or the worst-case loss, is tolerable? Would you hold it through a full holding period rather than watching it tick by tick? Yes to the first, a lowered risk, a tolerable size and a planned holding period points to strategic use.

**The honest counterpoint.** If options are fairly priced, no strategy earns free money. The covered call's extra income is compensation for giving up upside (Ch. 9 and Ch. 13). The empirical case for the strategy rests on a volatility risk premium, which is the tendency of implied volatility to exceed realized volatility. That premium is real in many studies but varies and is not guaranteed. Options also carry costs a buy-and-hold owner avoids: bid-ask spreads, commissions, and less favorable tax treatment of premium income than of qualified dividends. Check the current tax rules before acting.

**Prompt for class.** Take the hypothetical stock above. Would you class the covered call as an investment, a speculation or a hedge? Would your answer change for an investor who sells calls on 100% of a concentrated position in a stock with a very low tax basis? Defend your view with BKM's definitions.

## Pitfalls, key terms and practice questions

**Common pitfalls.**

- Treating premium as yield without total return. Income is not return; a stock that falls 10% can wipe out a year of premiums.
- Annualizing the best case. The 10.38% figure above assumes the stock never rises above the strike and never falls.
- Forgetting early exercise. American calls on dividend payers are most likely to be exercised just before the ex-dividend date, so the dividend can be lost.
- Comparing the covered call to a bond. Its downside is that of the stock less a small cushion, not a bond's.
- Ignoring taxes and costs. Premium income, called-away gains and qualified dividends are taxed differently, and spreads and commissions reduce the net.

**Key terms checklist.**

- [ ] Covered call / call overwriting
- [ ] Strike (exercise) price, premium, expiration
- [ ] In, at and out of the money
- [ ] Called away / assignment
- [ ] Breakeven and maximum profit
- [ ] Put-call parity
- [ ] Implied vs. realized volatility; volatility risk premium
- [ ] Delta
- [ ] Protective put and collar
- [ ] Nominal vs. real return (Fisher relation)
- [ ] Speculation vs. gambling (BKM Ch. 5)

**Practice questions (CFA style).**

1. An investor buys a stock at \$40 and sells a 3-month call with a \$42 strike for a \$1.20 premium. Ignoring dividends, the breakeven price and maximum profit per share at expiration are:
   - A. \$38.80 and \$3.20
   - B. \$41.20 and \$3.20
   - C. \$38.80 and unlimited
2. By put-call parity, the payoff shape of a covered call is most similar to:
   - A. a long call
   - B. a written put combined with a bond
   - C. a protective put
3. A covered call strategy earns 9.0% nominal income in a year with 4.0% inflation. The real income, using the exact Fisher relation, is closest to:
   - A. 5.0%
   - B. 4.8%
   - C. 13.0%
4. Holding strike and maturity fixed, the premium received on a written call is most likely to rise if:
   - A. implied volatility falls
   - B. implied volatility rises
   - C. the stock price falls
5. The market view best matched to a covered call is:
   - A. strongly bullish
   - B. neutral to modestly bullish
   - C. bearish

**Answer key.**

1. **A.** Breakeven = 40 − 1.20 = \$38.80. Maximum profit = (42 − 40) + 1.20 = \$3.20, because the shares are called away at \$42. Choice C is wrong because the short call caps the upside.
2. **B.** From C + PV(X) = P + S we get S − C = PV(X) − P: stock minus a call equals a bond minus a put, so the covered call resembles a written put.
3. **B.** 1.09 / 1.04 − 1 = 4.81%. Choice A is the linear approximation 9 − 4, and choice C adds inflation instead of removing it.
4. **B.** Option value rises with volatility (BKM Ch. 21). Falling volatility or a falling stock price lowers a call's value.
5. **B.** A covered call profits from a flat or slowly rising stock and gives up large gains, so the seller is neutral to modestly bullish.

## Sources

- Barron's article on enhancing dividends with call options (published Sept. 29–30, 2026): link, headline and author still to be added. I could not retrieve it.
- Bodie, Kane and Marcus, *Investments* (BKM), Ch. 2, 3, 5, 9, 13, 17, 18, 20 and 21. Confirm chapter numbers against your edition.
- McMillan, Lawrence G., *Options as a Strategic Investment* (New York Institute of Finance; several editions). Page references not verified.
- Background reading on covered calls and dividend stocks from web search, not cited for specific figures: [Dividend.com](https://www.dividend.com/dividend-stocks-and-options/enhancing-your-income-play-with-covered-calls/), [U.S. News](https://money.usnews.com/financial-advisors/articles/best-covered-call-strategy-for-income).
- All example numbers are hypothetical and checked by hand: 0.75 / 50 = 1.5%; 1.025^4 − 1 = 10.38%; 1.1038 / 1.04 − 1 = 6.1%; 1.09 / 1.04 − 1 = 4.8%.
