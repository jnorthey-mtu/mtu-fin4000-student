# Current Events Study Guide 1: Treasury Supply and Rising Yields

*BKM Ch. 14–16*

[← All study guides](../../study-guide-index.md)

Sep 29, 2026 · Jim Northey

## Learning objectives

This study guide uses the September 2026 bond selloff (10-year at 5.24%, 30-year at 5.56% on Sept 28) as a live case for BKM Ch. 14-16. After working it, a student can:

- Decompose a long yield into expected short rates plus a term premium, and say which piece is moving (Ch. 15).
- Estimate the price effect of a yield move with duration and duration-convexity, and explain why long bonds lose most (Ch. 16).
- Compute implied forward rates from the current curve and say what they do and do not predict (Ch. 15).
- Separate nominal, real and breakeven-inflation yields (Ch. 5, Ch. 14).
- Explain how Treasury debt management (buybacks, bill share, auction sizes) and the Fed (policy rate, balance sheet) try to influence yields, and why the effect can be small or backfire.
- Read credit spreads to tell a rates-driven selloff from a credit-driven one (Ch. 14).

## What is happening

Long Treasury yields hit two-decade highs on Sept 24, 2026: the 30-year reached about 5.5%, the highest since 2004, and the 10-year about 5.2%, the highest since 2007 ([CNBC](https://www.cnbc.com/2026/09/24/us-treasury-yields-bonds-fed-inflation.html)). The move is global; German 10-year yields reached 3.59% and Japan's 3.09%, and the average sovereign yield worldwide is near 4% ([Advisor Perspectives/Bloomberg](https://www.advisorperspectives.com/articles/2026/09/24/global-bond-rout-highest-30-year-yield)).

**Treasury par yield curve, Sept 28, 2026** (sources differ by 1-2 bp; figures rounded for teaching)

| Maturity | Yield (%) |
| --- | --- |
| 3-month | 4.28 |
| 1-year | 4.53 |
| 2-year | 4.92 |
| 5-year | 5.07 |
| 10-year | 5.24 |
| 30-year | 5.56 |

Source: [Spot the Money](https://spotthemoney.com/rates/treasury-yields/) and [StreetStats](https://streetstats.finance/rates/treasuries), from Treasury's daily par curve.

The selloff reaches other fixed income too. The broad investment-grade corporate index yields 5.88% (spread 0.81 points over Treasuries) and high yield 7.87% (spread 2.93 points), and 30-year mortgage rates are about 7% ([StreetStats](https://streetstats.finance/rates/corporates), [ETF Trends](https://www.etftrends.com/fixed-income-content-hub/treasury-yields-snapshot-september-25-2026/)). Spreads are still modest, so this is mostly a rates move, not a credit scare.

**A caution on "more notes and bonds."** Treasury has not raised nominal coupon auction sizes. Its August refunding kept them flat and said it expects to hold them for at least the next several quarters; the refunding was \$58 billion of 3-year, \$42 billion of 10-year and \$25 billion of 30-year ([Treasury, Aug 5, 2026](https://home.treasury.gov/news/press-releases/sb0590)). The supply pressure comes from the accumulated stock of debt (now above \$40 trillion), deficits that must be rolled, a cash balance built to about \$950 billion, and heavy corporate issuance competing for the same investors. Demand looks weaker too: the 5-year auction this week drew the highest yield since 2006 and ranked second-worst by one measure since 2018 ([Advisor Perspectives/Bloomberg](https://www.advisorperspectives.com/articles/2026/09/24/global-bond-rout-highest-30-year-yield)).

## What rising yields signal

The yield on a long bond has three parts, and this selloff touches all of them:

```math
y_{10} \approx \underbrace{\bar{r}_{\text{real, expected}}}_{\text{Fed path}} + \underbrace{\bar{\pi}_{\text{expected}}}_{\text{inflation}} + \underbrace{TP}_{\text{term premium}}
```

1. **Expected short rates.** The Fed raised the funds rate 25 bp to 3.75-4.00% on Sept 16, its first hike since 2023, and 16 of 18 projections show at least one more this year ([CNBC](https://www.cnbc.com/2026/09/16/fed-rate-decision-september-2026.html), [Schwab](https://www.schwab.com/learn/story/fomc-meeting)).
2. **Inflation.** Oil prices tied to the US-Iran war have lifted inflation fears; the 2-year yield is up more than 150 bp since the war began, while the 30-year is up over 80 bp ([Advisor Perspectives/Bloomberg](https://www.advisorperspectives.com/articles/2026/09/24/global-bond-rout-highest-30-year-yield)). The Fed's core PCE forecast for 2026 is 3.4% ([J.P. Morgan](https://am.jpmorgan.com/us/en/asset-management/adv/insights/portfolio-insights/fixed-income/fixed-income-perspectives/fomc-statement-september-2026/)).
3. **Term premium.** The long end also reflects what investors demand to finance government borrowing years ahead. Analysts argue that heavy government and corporate supply and weaker traditional demand make this part structural, so long yields may stay high even if cyclical pressures fade ([TD Economics](https://economics.td.com/ca-bond-yields)).

Two readings of the same curve. Chair Warsh said part of the rise in long yields reflects a stronger economy, which is a growth signal, not a distress signal ([Fox Business](https://www.foxbusiness.com/economy/federal-reserve-interest-rate-decision-september-16-2026)). The bearish reading is a fiscal feedback loop: higher yields raise interest expense, which widens the deficit, which raises supply, which pushes yields up again ([LPL Research](https://www.lpl.com/content/dam/edam/research/publications/rate-and-credit-view/rate-and-credit-view-09-2026.pdf)).

The curve itself is upward sloping but not steep: 10-year minus 2-year is about 32 bp and 30-year minus 10-year about 32 bp. It is not inverted, so the usual recession warning is not flashing. Students should be able to say why an upward slope here is consistent with both the Expectations Hypothesis (more hikes expected) and Liquidity Preference (a positive term premium).

## How the government and the Fed are responding

Treasury has leaned on debt management (buybacks, cash balance, issuance mix) rather than cutting long-bond supply, while the Fed is tightening, not easing. So far the results are mixed.

| Tool | What was done | Effect so far |
| --- | --- | --- |
| Larger buybacks | On Aug 19 Treasury doubled the maximum size of long-end liquidity-support buybacks from \$2 billion to at least \$4 billion, effective Sept 9 through Nov 4 ([Treasury](https://home.treasury.gov/news/press-releases/sb0607)). The quarterly plan allows up to \$38 billion of liquidity-support and \$25 billion of cash-management buybacks ([Treasury refunding](https://home.treasury.gov/news/press-releases/sb0590)). | Yields fell briefly, then rose. A \$6 billion operation on Sept 10 was followed by higher yields ([NBC News](https://www.nbcnews.com/business/economy/bessent-treasury-bonds-repurchase-rcna596819)). Bessent calls it successful versus the counterfactual ([Yahoo Finance](https://finance.yahoo.com/economy/policy/article/bessent-calls-treasury-bond-buyback-successful-reiterates-he-has-tools-to-stabilize-bond-market-190005670.html)). |
| Cash balance (TGA) | Treasury has built its cash balance to about \$950 billion and expects it to peak near \$1.05 trillion in late October ([Treasury refunding](https://home.treasury.gov/news/press-releases/sb0590)); sources say it could fund more buybacks ([CNBC](https://www.cnbc.com/2026/08/24/bessent-1-trillion-treasury-general-account-bond-buybacks.html)). | Investors doubt the firepower is large enough to matter ([CNBC](https://www.cnbc.com/2026/08/24/bessent-1-trillion-treasury-general-account-bond-buybacks.html)). |
| Auction sizes and mix | Nominal coupon sizes held flat; shifting issuance toward bills is discussed as an option but has not been done ([CNBC](https://www.cnbc.com/2026/08/20/bessents-efforts-in-the-treasury-market-so-far-havent-worked-heres-what-else-he-can-try.html)). | Bessent criticized that approach when his predecessor used it, so it is a politically costly option. |
| New demand sources | Bessent expects stablecoin rules under the GENIUS Act to raise demand for Treasury bills ([Yahoo Finance](https://finance.yahoo.com/economy/policy/article/bessent-calls-treasury-bond-buyback-successful-reiterates-he-has-tools-to-stabilize-bond-market-190005670.html)). | Helps the short end mainly; effect on 10- to 30-year yields is indirect. |
| Fiscal consolidation | Bessent has promised a deficit-reduction plan with OMB but has given no details ([NBC News](https://www.nbcnews.com/business/economy/bessent-treasury-bonds-repurchase-rcna596819)). | Not yet in the market; the largest lever on term premium if it arrives. |
| Fed policy | Rate hike to 3.75-4.00% on Sept 16; another expected this year ([Schwab](https://www.schwab.com/learn/story/fomc-meeting)). Chair Warsh has also suggested higher long yields could stand in for some policy tightening ([Goldman Sachs](https://www.goldmansachs.com/insights/the-markets/how-inflation-and-fiscal-policy-are-driving-us-treasury-markets)). | Raises short rates directly; puts the Fed and Treasury at odds on long yields. |

Because investors see Treasury as trying to hold yields down, some call this the "Bessent put," and critics warn it can become a trap if the market tests it ([W1M](https://www.w1m.com/insights/the-bessent-put-can-policymakers-stop-bond-yields-rising/)). Treasury also acted abroad, helping stabilize the yen partly to avoid heavy Japanese selling of Treasuries ([NBC News](https://www.nbcnews.com/business/economy/bessent-treasury-bonds-repurchase-rcna596819)). The next checkpoint is the quarterly refunding on Nov 4, 2026.

## Background reading and how to access WSJ and Barron's

Start with the open sources below, then add WSJ and Barron's coverage through the campus subscription. Several Bloomberg and CNBC pages are metered or paywalled, so students may need the library.

| Reading | Why assign it |
| --- | --- |
| [Treasury quarterly refunding statement, Aug 5, 2026](https://home.treasury.gov/news/press-releases/sb0590) | Primary source for auction sizes, cash balance and buyback plans; shows coupon sizes are flat. |
| [Treasury: increased long-end buybacks, Aug 19, 2026](https://home.treasury.gov/news/press-releases/sb0607) | Primary source for the main policy response. |
| [CNBC: 30-year yield highest since 2004, Sept 24](https://www.cnbc.com/2026/09/24/us-treasury-yields-bonds-fed-inflation.html) | Clear news account of the day yields peaked; good for the yield-price arithmetic. |
| [TD Economics: higher for longer](https://economics.td.com/ca-bond-yields) | Separates cyclical from structural (term premium) drivers. |
| [Fidelity: what is causing the bond selloff](https://www.fidelity.com/learning-center/trading-investing/market-commentary) | Accessible view that rising yields need not signal a crisis. |
| [FOMC press conference, Sept 16 (PDF)](https://www.federalreserve.gov/mediacenter/files/FOMCpresconf20260916.pdf) | Chair Warsh on why the Fed hiked and why long yields rose. |

**Activate the campus WSJ subscription.** Michigan Tech students, faculty and staff can activate the school-sponsored subscription at [WSJ.com/MTU](http://WSJ.com/MTU) ([College of Business announcement](https://blogs.mtu.edu/business/2024/08/27/free-wsj-subscription/)).

1. Go to WSJ.com/MTU and create or link a WSJ account using your Michigan Tech email address.
2. If you already pay for WSJ, call 1-800-JOURNAL and say you are switching to the school-sponsored subscription; partial refunds are made.
3. After activation, sign in at WSJ.com or in the WSJ app. The announcement says access covers WSJ.com, the app, newsletters and podcasts.

**Barron's.** The Michigan Tech announcement describes WSJ access only and does not mention Barron's, so I could not confirm that the campus deal includes it. Three ways to check, in order:

1. While signed in to your activated WSJ account, open Barron's and see whether articles are unlocked. Barron's is a Dow Jones title, and at some other universities it is activated separately after the WSJ account exists ([Rollins College library FAQ](https://rollins.libanswers.com/faq/420005)).
2. Search the Van Pelt and Opie Library databases. The library has offered ABI/INFORM (ProQuest), which it has described as including the WSJ; at the University of Michigan the same database carries Barron's from 1988 ([Kresge Library](https://kresgeguides.bus.umich.edu/newsstand/barrons)). At Michigan Tech, search the database's publication list for "Barron's" to confirm coverage. Off campus, sign in with your Michigan Tech email credentials ([library remote access](https://www.mtu.edu/library/services/off-campus/remote-access/)).
3. If neither works, ask the library (reflib@mtu.edu, per an older library post; check the current contact on the library page) or Dow Jones academic support whether the Michigan Tech agreement covers Barron's.

I did not find specific WSJ or Barron's articles to link because both are paywalled to my search. Useful search terms once you are signed in: "Treasury buyback", "term premium", "30-year yield 2004", "Bessent bond market".

## Worked examples

All figures are illustrative and were checked in Python. Yields are the rounded Sept 28, 2026 values above, treated as annual effective rates for the forward-rate example.

**Example 1. Price of a 30-year bond after the selloff (Ch. 14, 16).** A 30-year, 4.75% semiannual-coupon bond was issued at par when the 30-year yield was 4.75%. The yield is now 5.56% (up 81 bp). Find the new price and compare with the duration-convexity estimate.

BA II Plus keystrokes (set 2 payments per year once, then clear):

1. `2nd` `P/Y` `2` `ENTER` `2nd` `QUIT`
2. `60` `N` (30 years × 2)
3. `5.56` `I/Y`
4. `2.375` `PMT` (4.75% ÷ 2 × 100)
5. `100` `FV`
6. `CPT` `PV` → −88.24 (the sign is cash flow direction; the price is 88.24)

Actual change: 88.24 / 100 − 1 = −11.76%. Estimate with modified duration 15.90 and convexity 367.9: −15.90 × 0.0081 = −12.88% from duration alone, plus ½ × 367.9 × 0.0081² = +1.21% from convexity, total −11.68%. Duration overstates the loss on a large move; convexity corrects most of the gap.

**Example 2. Implied forward rate (Ch. 15).** With a 1-year rate of 4.53% and a 2-year rate of 4.92%, the one-year rate implied for the year starting one year from now is:

```math
(1 + f_{1,2}) = \frac{(1.0492)^2}{1.0453} \Rightarrow f_{1,2} = 5.31\%
```

Keystrokes: `1.0492` `y^x` `2` `=` `÷` `1.0453` `=` `−` `1` `=` → 0.0531. Under the Expectations Hypothesis the market expects a 1-year rate near 5.31% next year. If a positive term premium is embedded, the true expectation is lower, which is exactly why forward rates are not forecasts (Ch. 15).

**Example 3. Real yield from a nominal yield (Ch. 5).** If the 10-year yields 5.24% and expected inflation is 2.60% (an assumed breakeven, not a market quote), the real yield is (1.0524 / 1.0260) − 1 = 2.57%. Keystrokes: `1.0524` `÷` `1.026` `−` `1` `=` → 0.0257. The simple subtraction gives 2.64%; use the exact form for large rates or inflation.

## Conceptual questions (choose A, B or C)

**Q1.** Treasury's August 2026 refunding kept nominal coupon auction sizes unchanged, yet long yields kept rising. Which statement best explains this?

- A. Unchanged auction sizes mean supply is not a factor in long yields.
- B. Long yields reflect expected short rates, expected inflation and a term premium, and the term premium can rise with the total stock of debt and weaker demand even when new-issue sizes are flat.
- C. Yields rise only when the Treasury increases the size of its 10-year and 30-year auctions.

**Q2.** The 30-year yield rises 30 bp while the Fed's expected path for the funds rate and expected inflation are unchanged. The best interpretation is:

- A. The Expectations Hypothesis fully explains the move.
- B. The term premium rose.
- C. The yield curve inverted.

**Q3.** Treasury announced larger buybacks of 10- to 30-year bonds, and yields rose after a \$6 billion operation. Which is the most plausible reason the buyback did not lower yields?

- A. Buybacks remove old bonds but do not change the deficit, so the government must issue new debt again, and the market may read the intervention as a sign of stress.
- B. Buybacks always raise yields by increasing the money supply.
- C. Buybacks only affect bills, which are not part of the yield curve.

**Q4.** Under Liquidity Preference Theory, a forward rate is typically:

- A. Equal to the expected future short rate.
- B. Greater than the expected future short rate by a liquidity premium.
- C. Less than the expected future short rate by a default premium.

**Q5.** From Sept 4 to late September 2026 the high-yield spread widened from about 259 bp to 294 bp while Treasury yields rose sharply, and the investment-grade spread stayed near 81 bp. This pattern most likely indicates:

- A. A broad credit crisis in corporate bonds.
- B. A selloff driven mainly by higher Treasury yields, with only modest added credit risk pricing.
- C. A flight to quality into corporate bonds.

**Q6.** Which best describes the fiscal feedback loop some analysts fear?

- A. Higher yields lower interest expense, which narrows the deficit and reduces supply.
- B. Higher yields raise interest expense, which widens the deficit, which raises supply and pressures yields further.
- C. Higher deficits reduce supply, which lowers yields.

**Q7.** After a parallel +50 bp shift in the yield curve, which Treasury holding will most likely lose the largest percentage of its price?

- A. A 2-year note.
- B. A 10-year note.
- C. A 30-year bond with the same coupon.

## Algorithmic questions (choose A, B or C)

**Q8.** The 10-year yield rose from 4.75% at the end of August to 5.24% on Sept 28 (+49 bp). A 10-year note has modified duration 8.0 and convexity 80. The duration-convexity estimate of its percentage price change is closest to:

- A. −3.92%
- B. −3.82%
- C. −4.02%

**Q9.** A 30-year bond with a 4.75% semiannual coupon and \$100 par is priced when the 30-year yield is 5.56% (semiannual compounding). Its price is closest to:

- A. \$91.83
- B. \$88.24
- C. \$100.00

**Q10.** The 5-year yield is 5.07% and the 10-year yield is 5.24% (annual effective rates, treated as spot rates). The implied 5-year forward rate starting five years from now is closest to:

- A. 5.16%
- B. 5.24%
- C. 5.41%

**Q11.** The 10-year nominal yield is 5.24% and expected inflation over the period is 2.60%. The exact real yield is closest to:

- A. 2.64%
- B. 2.57%
- C. 7.84%

**Q12.** An investor buys an investment-grade bond fund with a yield of 5.88% and average modified duration of 6.5. Over one year the yield rises 50 bp. Ignoring convexity and reinvestment, the approximate one-year total return is closest to:

- A. 5.88%
- B. 2.63%
- C. 9.13%

**Q13.** In August 2026 Treasury offered \$125 billion of 3-, 10- and 30-year securities to refund \$96.3 billion of privately held notes and bonds maturing August 15. New cash raised from private investors is:

- A. \$96.3 billion
- B. \$28.7 billion
- C. \$221.3 billion

## Key terms, pitfalls and answer key

**Key terms checklist**

- [ ] Term premium; Expectations Hypothesis; Liquidity Preference Theory
- [ ] Forward rate versus expected future spot rate
- [ ] Modified duration, convexity, duration-convexity estimate
- [ ] Nominal, real and breakeven inflation yield; Fisher equation
- [ ] Credit spread (IG and high yield); rates-driven versus credit-driven selloff
- [ ] Quarterly refunding; Treasury buyback (liquidity support versus cash management); Treasury General Account
- [ ] Bear steepener versus bear flattener

**Common pitfalls**

- Treating higher yields as "more supply this quarter." Here, coupon auction sizes are flat; the pressure is the stock of debt, deficits, weaker demand and a higher term premium.
- Reading forward rates as forecasts. They embed a term premium under Liquidity Preference.
- Forgetting to set P/Y = 2 and N = 60 for a 30-year semiannual bond on the BA II Plus.
- Using the duration-only estimate for a large yield move; add the convexity term.
- Subtracting inflation from the nominal yield instead of dividing (1 + nominal) by (1 + inflation).

**Answer key**

| Q | Answer | Why |
| --- | --- | --- |
| 1 | B | The long yield has three components; total debt and demand affect the term premium even with flat new-issue sizes. |
| 2 | B | With expected short rates and inflation unchanged, a higher long yield must come from a higher term premium. |
| 3 | A | Buybacks do not change the deficit, so supply returns, and heavy intervention can be read as a sign of stress. |
| 4 | B | Under Liquidity Preference, forward rate = expected future spot rate + liquidity premium. |
| 5 | B | IG spreads barely moved and HY widened modestly, so the selloff is mostly a higher Treasury yield, not credit stress. |
| 6 | B | Higher yields raise interest cost, widening the deficit and supply, which pressures yields again. |
| 7 | C | Longer maturity means higher duration, so the 30-year bond has the largest percentage price loss. |
| 8 | B | −8.0 × 0.0049 = −3.92%; convexity adds ½ × 80 × 0.0049² = +0.10%; total −3.82%. Choice C subtracts the convexity term by mistake. |
| 9 | B | 60 `N`, 5.56 `I/Y`, 2.375 `PMT`, 100 `FV`, `CPT` `PV` = −88.24. Choice A uses N = 30; C is correct only when yield equals coupon. |
| 10 | C | (1.0524^10 / 1.0507^5)^(1/5) − 1 = 5.41%. Use STO/RCL or parentheses for the two powers. Choice A is the simple average; B is the 10-year yield. |
| 11 | B | 1.0524 / 1.0260 − 1 = 2.57%. Choice A is the approximate subtraction; C adds instead of subtracting. |
| 12 | B | Return ≈ yield − duration × change in yield = 5.88 − 6.5 × 0.50 = 2.63%. Choice C adds the price loss instead of subtracting it. |
| 13 | B | \$125 billion − \$96.3 billion = \$28.7 billion of new cash, as stated in the refunding. |

Figures are as of Sept 28-29, 2026 and will date quickly; refresh the yield table after the Nov 4, 2026 refunding.
