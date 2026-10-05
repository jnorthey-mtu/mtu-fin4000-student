# Current Events Study Guide 4: Yen Carry Trade in the Bond Market

*BoJ and U.S. Treasury Roles (BKM Ch. 14–16)*

[← All study guides](../../study-guide-index.md)

Oct 2, 2026 · Jim Northey

## Learning objectives

After this guide you should be able to explain how a yen carry trade earns money, why it fails when the yen rises, and who moves the levers: the Bank of Japan (BoJ), Japan's Ministry of Finance (MOF), the U.S. Treasury, the New York Fed and the Federal Reserve.

1. Define a carry trade, and identify the funding currency, the investment asset and the two sources of return (interest differential and currency change).
2. Compute the all-in return on a yen-funded position in U.S. Treasuries, with and without a currency move, and find the break-even yen appreciation.
3. Explain how BoJ policy (the policy rate, yield curve control, JGB purchases and tapering) sets the cost of the funding leg and shapes Japanese government bond (JGB) yields.
4. Describe the tools the U.S. side used in 2026: Exchange Stabilization Fund (ESF) yen purchases, the NY Fed as agent, and the Fed's FIMA repo facility.
5. Separate what the record shows (the U.S. bought yen and pressed the BoJ to hike) from what analysts infer (that this indirectly protects Treasury demand and the carry trade), and say why those are different claims.
6. Describe how a carry-trade unwind spreads to bond markets, using August 2024 and the 2026 episodes.

## Core concept: borrow cheap yen, hold higher-yielding bonds

A yen carry trade borrows in yen at a low rate, converts to dollars, buys a higher-yielding asset such as a U.S. Treasury, and earns the rate gap as long as the yen does not rise enough to erase it. The yen is the funding currency; the Treasury (or any dollar asset) is the investment asset.

Per yen borrowed, the one-period return is:

```math
R = (1 + r_{US}) \frac{S_1}{S_0} - (1 + r_{JP}), \qquad S = \text{yen per dollar}
```

The trade has two sources of return. The first is the interest gap, r\_US minus r\_JP, which is known today. The second is the currency move, which is not. When S falls (the yen strengthens), the yen cost of repaying the loan stays fixed while the yen value of the dollar bond shrinks.

**Break-even.** Setting R = 0 gives S\_1 = S\_0 × (1 + r\_JP) / (1 + r\_US). This is exactly the one-period forward rate under covered interest parity. A carry trade is therefore a bet that the forward rate is too pessimistic about the dollar: the yen will not rise as far as the forward market implies. This links directly to the Ch. 15 forward-rate material.

**Where the bond market comes in.**

- **Foreign investors and hedge funds** borrow yen, often through short-term loans or FX swaps, to buy Treasuries or other dollar assets. They are unhedged on currency, so they carry the full exchange-rate risk.
- **Japanese institutions** (life insurers, banks, pension funds) buy foreign bonds with yen savings. Many hedge the currency, which converts the trade into a hedged-yield comparison.
- **Japan's official sector** holds about \$1.14 trillion of Treasuries, the largest foreign government position, per a 2026 summary of Treasury data ([Wright Research](https://www.wrightresearch.in/blog/why-washington-bought-japanese-yen-for-tokyo-a-rare-currency-intervention-in-2026/)). That stack is why U.S. officials care about how Japan defends its currency.
- **Japanese government bond (JGB) yields** are the other end. The 10-year JGB yield was near 2.95% after the Bank of Japan's September 2026 hike ([CNBC](https://www.cnbc.com/2026/09/18/japan-raises-rates-30-year-high-yen-jgb.html)), so the funding side is no longer free.

The risk is asymmetric and leveraged. Small, steady carry gains are earned for months, then a fast yen rally forces many holders to sell at once. Selling dollar assets to buy back yen is what spreads a currency move into bond and equity markets.

## The Bank of Japan: it sets the cost of the funding leg

The Bank of Japan controls the price of yen funding and the pace of JGB buying, so its decisions move the carry trade more durably than any intervention does. The Ministry of Finance (MOF), not the BoJ, decides when to intervene in currency markets. The BoJ executes those trades as the MOF's agent, which is why BoJ data can reveal the size of an operation after the fact.

| BoJ lever | What it does | Effect on the carry trade |
| --- | --- | --- |
| Policy rate | Sets short-term yen borrowing cost | Higher rate raises funding cost and narrows the gap to U.S. rates |
| Yield curve control (YCC), ended in 2024 | Capped the 10-year JGB yield near zero | Kept long funding and JGB yields artificially low; its removal let yields float |
| JGB purchases and tapering | Buying holds JGB prices up; tapering lets yields rise | Less buying pushes JGB yields higher, which can draw Japanese savers home |
| Forward guidance | Signals the path of rates | A faster expected path strengthens the yen and raises unwind risk |

**The 2026 record.** The BoJ raised its policy rate 25 basis points to 1.25% on September 18, 2026, the highest since 1995, in a 7-2 vote ([CNBC](https://www.cnbc.com/2026/09/18/japan-raises-rates-30-year-high-yen-jgb.html)). The previous hike, to 1.0%, came in June ([Al Jazeera](https://www.aljazeera.com/economy/2026/8/3/japan-and-us-confirm-rare-joint-intervention-to-prop-up-yen)). Despite the hike, the yen weakened past 157 per dollar and the 10-year JGB yield slipped, because two dissents signaled a less hawkish path ([CNBC](https://www.cnbc.com/2026/09/18/japan-rate-hike-stocks-rise-bond-yields-yen-fall.html)).

The gap that funds the trade is still wide. The Fed raised its target range to 3.75%-4.00% on September 16, 2026, according to one market summary ([Admiral Markets](https://admiralmarkets.com/analytics/traders-blog/fed-raised-interest-rates)). That leaves the policy-rate gap at roughly 2.5 to 2.75 percentage points, so the carry remains positive unless the yen rallies.

JGB yields add a second pressure. MUFG Research expected the 10-year JGB yield in a 2.92%-3.08% range and the 30-year in a 4.00%-4.19% range for late September ([MUFG Research](https://www.mufgresearch.com/rates/japan-economic-financial-weekly-18-september-2026)). Higher domestic yields make Japanese investors less eager to buy Treasuries, which is the BoJ-to-Treasury-market link.

**Why the BoJ is the key to the whole story.** Analysts quoted in 2026 coverage argue that intervention alone does not last, and that a durable stronger yen needs BoJ tightening that narrows the U.S.-Japan yield gap ([CNBC](https://www.cnbc.com/2026/08/20/us-japan-yen-intervention-bank-of-japan-carry-trade.html)).

## The U.S. Treasury: it bought yen, which is not the same as supporting carry trades

The record shows the Treasury joined Japan in buying yen on July 31, 2026, and pressed the Bank of Japan to raise rates. The idea that it was trying to support carry trades is an analyst inference about Treasury-market motives, not something the Treasury has said. Buying yen strengthens the funding currency, which works against an unhedged carry position in the short run, so the two readings need to be kept apart.

**What is documented**

- On July 30 Japan intervened alone, and on July 31 the Treasury, acting through the New York Fed, sold euros from its Exchange Stabilization Fund (ESF) to buy yen ([CNBC](https://www.cnbc.com/2026/08/01/us-treasury-intervenes-to-support-yen-after-japan-steps-in-ft.html), [Al Jazeera](https://www.aljazeera.com/economy/2026/8/3/japan-and-us-confirm-rare-joint-intervention-to-prop-up-yen)). Reuters coverage called it the first joint U.S.-Japan yen action since 2011.
- A photo of Secretary Bessent's notepad read "Buy Japanese Yen (JPY) \$5-10 bil." Washington has not disclosed the exact amount ([CNBC](https://www.cnbc.com/2026/09/03/yen-japan-intervention-boj.html)). Third-party estimates differ, so treat any single figure as approximate.
- Bessent said the U.S. "will not hesitate to participate in further joint intervention" and backed Japan's steps to correct the "substantial undervaluation of the yen," repeating calls for BoJ rate hikes ([Al Jazeera](https://www.aljazeera.com/economy/2026/8/3/japan-and-us-confirm-rare-joint-intervention-to-prop-up-yen)).
- Japan's finance minister said Japan plans to use the Fed's FIMA repo facility in future operations ([Sovereign Magazine](https://www.sovereignmagazine.com/article/us-sold-euros-yen-intervention-treasury)). FIMA lets approved foreign central banks borrow dollars against Treasuries held at the New York Fed instead of selling them, with a \$60 billion per-counterparty limit.
- Bessent said it would be reasonable for the Fed to consider upsizing FIMA, adding that its purpose was to protect the U.S. bond market ([Reuters via FBC](https://www.fbcnews.com.fj/world/us-will-do-whatever-it-takes-to-support-japan-after-yen-intervention-bessent-says/)).
- On September 1 he said he had information the market lacked and believed Japan and the BoJ would act to produce a stronger yen ([Japan Times](https://www.japantimes.co.jp/business/2026/09/01/economy/bessent-japan-yen-boj-rate-hike/)).

**What is inferred, and by whom**

| Claim | Who makes it | Status |
| --- | --- | --- |
| Selling euros instead of dollars, and steering Japan to FIMA, was meant to stop Japan becoming a forced seller of Treasuries | CNBC analysis, other commentators ([CNBC](https://www.cnbc.com/2026/08/03/bessent-fed-japan-yen-fima-repo-facility.html), [Axios](https://www.axios.com/2026/08/03/yen-japan-treasury-bessent)) | Plausible reading; Treasury says it responded to disorderly moves |
| Stopping the yen's slide could protect the carry trade and keep Treasury demand up | CNBC analysis; a one-line aside in a market note ([FXStreet](https://www.fxstreet.com/analysis/the-intervention-to-halt-the-slide-of-the-yen-202608041203)) | Inference only; Bessent has not said this |
| Intervention "turbo-charged" carry trades by letting investors rebuild positions on dips | Jesper Koll, Monex, quoted by CNBC ([CNBC](https://www.cnbc.com/2026/08/20/us-japan-yen-intervention-bank-of-japan-carry-trade.html)) | One strategist's view |
| Intervention made the trade less one-sided without ending it | Marquette Associates ([Marquette](https://www.marquetteassociates.com/yen-wayward-investors-carry-on/)) | Analysis; cites a 1.3% drop in the Bloomberg FX Carry Index over ten trading days |

**How to reason about it.** The stated official aim is stopping disorderly yen weakness, with a clear second interest in not letting Treasury yields spike. Bessent also said he does not think the carry trade will ever go away entirely ([CNBC](https://www.cnbc.com/2026/08/03/bessent-fed-japan-yen-fima-repo-facility.html)). The yen gave back roughly half its post-intervention gains within a week ([Wright Research](https://www.wrightresearch.in/blog/why-washington-bought-japanese-yen-for-tokyo-a-rare-currency-intervention-in-2026/)), which shows why durable change needs the BoJ and the rate gap, not intervention alone.

**A limit of the FIMA backstop.** FIMA covers only official holders. Private yen-funded positions can still be closed in the open market, so a carry unwind could still pressure Treasuries ([NISM](https://www.nism.ac.in/blog/a-yen-rescue-dressed-in-euros)).

## Worked examples (BA II Plus)

All inputs are illustrative round numbers, chosen to resemble the 2026 setting (BoJ policy rate 1.25%, Fed range top 4.00%, USD/JPY near 157). Answers were checked in Python.

**Example 1: break-even yen move.** You borrow ¥1,000,000,000 for one year at 1.25%, convert at S0 = 157.00 yen per dollar, and buy a one-year Treasury yielding 4.00%. How far must the yen strengthen to wipe out the profit?

1. Dollars bought: ¥1,000,000,000 ÷ 157 = \$6,369,427.
2. Break-even: S1 = 157 × 1.0125 ÷ 1.04.
3. Keystrokes: `157` `×` `1.0125` `÷` `1.04` `=` shows 152.8486.
4. Yen appreciation needed: 157 ÷ 152.8486 − 1 = 2.72% (USD/JPY falls 2.64%).
5. If the yen does not move, profit is ¥27.5 million, or 2.75% of the amount borrowed.

**Example 2: the yen rallies.** Same trade, but the yen ends the year at 150.00.

1. Year-end dollars: \$6,369,427 × 1.04 = \$6,624,204.
2. Converted back: \$6,624,204 × 150 = ¥993,630,573.
3. Loan repayment: ¥1,000,000,000 × 1.0125 = ¥1,012,500,000.
4. Result: a loss of ¥18,869,427, or -1.89% of the amount borrowed, even though the Treasury paid in full.
5. Leverage: with a 5% yen rise the loss is 1.04 ÷ 1.05 - 1.0125 = -2.20% of the borrowed amount; at 10 times leverage on equity that is about -22%. This is why a fast yen rally forces selling.

**Example 3: a JGB yield rise (ties to Ch. 14 and 16).** A 10-year JGB with a 2.95% annual coupon is priced at par (annual coupons for simplicity). The yield rises 50 basis points to 3.45%. What happens to the price?

1. Clear the worksheet: `2nd` `CLR TVM`. Confirm payments per year: `2nd` `P/Y` `1` `ENTER`, then `2nd` `QUIT`.
2. Enter `10` `N`, `2.95` `I/Y`, `2.95` `PMT`, `100` `FV`, then `CPT` `PV`. The display shows -100.00.
3. Change the yield: `3.45` `I/Y`, then `CPT` `PV`. The display shows -95.83.
4. Price change: 95.83 ÷ 100 - 1 = -4.17%.
5. Check with duration: modified duration is about 8.55, so the estimate is -8.55 × 0.50% = -4.28%. The actual loss is slightly smaller because of convexity.

Higher JGB yields cut the value of Japanese institutions' domestic bond holdings and raise the return they can earn at home, which is how BoJ tightening can pull savings out of Treasuries.

## Common pitfalls and key-terms checklist

Most lost points come from getting the direction of the currency quote wrong or from blending claims about motives with claims about actions.

**Pitfalls**

- **Quote direction.** USD/JPY is yen per dollar. A falling number means a stronger yen, which hurts the unhedged carry trade.
- **Buying yen is not buying the carry trade.** The Treasury's yen purchases raise the yen. Any link to supporting carry trades runs through Treasury-market demand and is an inference.
- **MOF versus BoJ.** The MOF decides on intervention and the BoJ executes it. The BoJ separately sets the policy rate and JGB purchases.
- **FIMA is a repo, not a swap line.** FIMA lets a central bank borrow dollars against Treasuries it holds at the New York Fed. Fed swap lines exchange currencies and are normally used for dollar liquidity, not intervention.
- **Hedged is not the same as carry.** With the currency fully hedged, covered interest parity pushes the yen return back toward the yen rate. Any leftover gap comes from the cross-currency basis.
- **Policy rate is not the funding cost.** Real borrowers pay a spread over the BoJ rate, so use it only as a proxy.
- **Single-source figures.** Intervention sizes differ across reports (for example, the Treasury's yen purchase is cited as \$5-10 billion from the notepad, with other outlets giving different estimates). Cite the source and say "approximately."
- **Leverage.** A 2% unlevered loss becomes a 20% equity loss at 10 times leverage.

**Key terms and definitions**

- [ ] **Carry trade, funding currency, investment asset:** a carry trade borrows in a low-interest currency and invests in a higher-yielding asset, earning the interest gap as long as the exchange rate does not move against the position. The funding currency is the one borrowed (here, the yen). The investment asset is what the borrowed money buys (here, a U.S. Treasury).
- [ ] **Covered interest parity and the forward rate:** the no-arbitrage link between two countries' interest rates and the forward exchange rate. The forward rate is the exchange rate fixed today for a trade at a future date. With S in yen per dollar, F = S₀ × (1 + r\_JP) / (1 + r\_US), which is also the break-even rate of an unhedged carry trade.
- [ ] **Break-even currency move:** the exchange-rate change at which the carry trade earns exactly zero, because the yen cost of repaying the loan equals the yen value of the dollar investment. In Example 1 the yen must strengthen about 2.72% before the profit disappears.
- [ ] **Unhedged versus hedged carry:** an unhedged position bears the full exchange-rate risk and keeps the interest gap only if the currency holds. A hedged position locks in the exchange rate with a forward or swap, so under covered interest parity the return falls back toward the funding-currency rate. Any leftover gap comes from the cross-currency basis.
- [ ] **Ministry of Finance versus Bank of Japan roles:** the Ministry of Finance (MOF) decides when Japan intervenes in the currency market. The Bank of Japan (BoJ) carries out those trades as the MOF's agent, and separately sets the policy rate and the pace of JGB purchases.
- [ ] **Exchange Stabilization Fund (ESF) and the New York Fed as agent:** the ESF is the U.S. Treasury's fund for foreign-exchange operations. The New York Fed executes the trades on the Treasury's behalf. In July 2026 the Treasury used the ESF, through the New York Fed, to sell euros and buy yen.
- [ ] **Disorderly yen movements:** fast, one-directional yen moves that officials judge to be out of step with economic fundamentals. It is the stated official reason for intervention, not a precise measurable threshold.
- [ ] **FIMA repo facility versus a swap line:** the FIMA repo facility lets approved foreign central banks borrow dollars from the Fed against Treasuries they hold at the New York Fed, so they need not sell those bonds (limit of \$60 billion per counterparty). A swap line instead exchanges currencies between central banks and is normally used for dollar liquidity, not intervention.
- [ ] **Yield curve control (YCC) and JGB tapering:** YCC was the Bank of Japan policy of capping the 10-year JGB yield near zero; it ended in 2024. Tapering is the BoJ reducing its JGB purchases, which lets JGB yields rise.
- [ ] **Bear steepening:** a yield-curve move in which long-term yields rise by more than short-term yields, so the curve gets steeper and bond prices fall.
- [ ] **Carry-trade unwind and forced selling:** when the funding currency rises, carry positions lose money and leveraged holders must close them by selling their dollar assets and buying back yen. Many holders doing this at once spreads a currency move into bond and equity markets, as in August 2024.

## Practice questions (CFA-style, choose A, B or C)

**Algorithmic**

**1.** An investor borrows ¥500 million for one year at 1.00%, converts at 155.00 yen per dollar, and buys a one-year Treasury yielding 3.90%, with no currency hedge. The break-even exchange rate at the end of the year is closest to:

- A. 159.45
- B. 150.67
- C. 150.51

**2.** Using the trade in the worked examples (borrow at 1.25%, Treasury yield 4.00%, spot 157.00), the yen ends the year at 152.00. The return per yen borrowed is closest to:

- A. +2.75%
- B. -3.18%
- C. -0.56%

**3.** A 10-year JGB has a modified duration of 8.55. If its yield rises 40 basis points, the duration-based estimate of the price change is closest to:

- A. -3.42%
- B. +3.42%
- C. -0.34%

**Conceptual**

**4.** Which statement best describes what is documented about the U.S. Treasury's role on July 31, 2026?

- A. It sold euros through the New York Fed to buy yen, and Secretary Bessent said it would not hesitate to join further joint intervention.
- B. It sold dollars from the Federal Reserve's balance sheet to buy yen.
- C. It bought Japanese government bonds to lower Japanese yields.

**5.** Why did U.S. officials point Japan toward the Fed's FIMA repo facility?

- A. It lets private hedge funds borrow dollars to expand yen carry positions.
- B. It exchanges yen for dollars at a fixed rate, like a swap line.
- C. It lets a central bank raise dollars against Treasuries it holds, so it need not sell them and push up U.S. yields.

**6.** Which statement is best supported by the 2026 coverage on whether the Treasury was "supporting" yen carry trades?

- A. The Treasury has stated that its goal was to protect carry-trade profits.
- B. Officials framed the action as countering disorderly yen moves, while some analysts infer it may also protect Treasury demand and the carry trade.
- C. Intervention ended the carry trade within a week.

**7.** Who decides on yen intervention in Japan, and what does the Bank of Japan do?

- A. The BoJ decides, and the MOF executes the trades.
- B. The BoJ both decides and executes, with no role for the MOF.
- C. The MOF decides, and the BoJ executes as its agent, while separately setting policy rates.

## Answer key with explanations

| Q | Answer | Why |
| --- | --- | --- |
| 1 | B | S1 = 155 × 1.01 ÷ 1.039 = 150.67. A inverts the ratio (155 × 1.039 ÷ 1.01). C subtracts the 2.9-point rate gap from the exchange rate instead of using the ratio. |
| 2 | C | R = 1.04 × (152 ÷ 157) - 1.0125 = -0.56%. A counts only the interest gap. B counts only the 3.18% fall in USD/JPY and ignores the 2.75% rate gap. |
| 3 | A | Price change ≈ -modified duration × yield change = -8.55 × 0.40% = -3.42%. B has the wrong sign. C misplaces the decimal. |
| 4 | A | Reuters-based coverage reports the Treasury sold euros through the New York Fed to buy yen, and Bessent said it would not hesitate to join further joint intervention. B is wrong because euros, not dollars, were sold. C is wrong because no JGB purchases were involved. |
| 5 | C | FIMA is a repo against Treasuries held at the New York Fed, so Japan can raise dollars for intervention without selling bonds into the market. A is wrong because only foreign official institutions qualify. B describes a swap line. |
| 6 | B | The documented framing is countering disorderly moves, and Bessent said the carry trade will not go away entirely. Treating carry protection as a motive is an analyst inference. A overstates the evidence. C contradicts the Bloomberg FX Carry Index drop of only 1.3% over ten trading days reported by Marquette. |
| 7 | C | The Ministry of Finance decides on intervention, and the BoJ acts as its agent. The BoJ separately sets the policy rate and JGB purchases. |

## Sources and what could not be verified

I could not open any Wall Street Journal, Barron's or Bloomberg article, and I did not find a Barron's piece on this topic, so none is cited as a primary source here. Everything below was read from search excerpts as of October 2, 2026, because CNBC and several other pages blocked a full fetch. Check each figure against the original before relying on it for an exam or a lecture.

**WSJ, Barron's, Bloomberg: what I can and cannot say**

- **WSJ.** One aggregator reports that the WSJ described the Treasury's use of euros instead of dollars as unusual, and that Bessent called on the Fed to expand FIMA ([Longport summary](https://longportapp.cn/news/294751040)). That is a secondhand report. To read the original, search the WSJ site for "Treasury sold euros to buy yen" and "FIMA repo Japan."
- **Barron's.** No article found. Try searching barrons.com for "yen carry trade" and "Bessent yen."
- **Bloomberg (paywalled).** Facts attributed to Bloomberg here come secondhand: a Bloomberg survey in which all 52 economists expected the September BoJ hike ([FinanceCalendar](https://www.financecalendar.com/event/bank-of-japan-rate-decision-september-2026/)), and the Bloomberg FX Carry Index, down 1.3% over ten trading days ([Marquette Associates](https://www.marquetteassociates.com/yen-wayward-investors-carry-on/)). Search Bloomberg for "yen carry trade" and "Bessent yen intervention." Your library or Bloomberg terminal access would be the way past the paywall.

**Sources used**

| Source | Used for |
| --- | --- |
| [CNBC, Sep 18, 2026](https://www.cnbc.com/2026/09/18/japan-raises-rates-30-year-high-yen-jgb.html) | BoJ hike to 1.25%, 7-2 vote, 10-year JGB yield |
| [CNBC, Sep 18, 2026 (market reaction)](https://www.cnbc.com/2026/09/18/japan-rate-hike-stocks-rise-bond-yields-yen-fall.html) | Yen and JGB reaction to the hike |
| [Al Jazeera, Aug 3, 2026](https://www.aljazeera.com/economy/2026/8/3/japan-and-us-confirm-rare-joint-intervention-to-prop-up-yen) | Joint intervention, Bessent statements, June hike |
| [CNBC, Aug 1, 2026](https://www.cnbc.com/2026/08/01/us-treasury-intervenes-to-support-yen-after-japan-steps-in-ft.html) | Treasury yen purchase, notepad photo |
| [CNBC, Aug 3, 2026](https://www.cnbc.com/2026/08/03/bessent-fed-japan-yen-fima-repo-facility.html) | Treasury-market motive, FIMA, carry-trade comment |
| [Axios, Aug 3, 2026](https://www.axios.com/2026/08/03/yen-japan-treasury-bessent) | Treasury's stated rationale |
| [CNBC, Aug 20, 2026](https://www.cnbc.com/2026/08/20/us-japan-yen-intervention-bank-of-japan-carry-trade.html) | Carry trade "turbo-charged" view |
| [CNBC, Sep 3, 2026](https://www.cnbc.com/2026/09/03/yen-japan-intervention-boj.html) | Undisclosed U.S. amount |
| [Japan Times, Sep 1, 2026](https://www.japantimes.co.jp/business/2026/09/01/economy/bessent-japan-yen-boj-rate-hike/) | Bessent on BoJ and a stronger yen |
| [Reuters via FBC News](https://www.fbcnews.com.fj/world/us-will-do-whatever-it-takes-to-support-japan-after-yen-intervention-bessent-says/) | FIMA upsizing comments |
| [Sovereign Magazine](https://www.sovereignmagazine.com/article/us-sold-euros-yen-intervention-treasury) | MOF plan to use FIMA, FIMA terms |
| [MUFG Research](https://www.mufgresearch.com/rates/japan-economic-financial-weekly-18-september-2026) | JGB yield ranges |
| [Admiral Markets](https://admiralmarkets.com/analytics/traders-blog/fed-raised-interest-rates) | Fed range after September 16 hike (secondary source) |
| [Marquette Associates](https://www.marquetteassociates.com/yen-wayward-investors-carry-on/) | Carry-trade effect of intervention |
| [Wright Research](https://www.wrightresearch.in/blog/why-washington-bought-japanese-yen-for-tokyo-a-rare-currency-intervention-in-2026/) | Japan's Treasury holdings, yen retracement |
| [NISM](https://www.nism.ac.in/blog/a-yen-rescue-dressed-in-euros) | FIMA limits to official holders |

**Data conflicts to be aware of.** One calendar site listed the BoJ overnight rate at 0.75% as of June, while CNBC and Al Jazeera put it at 1.0% after a June hike; I used the CNBC and Al Jazeera figures. Estimates of the U.S. yen purchase range from the notepad's \$5-10 billion to other outlets' higher figures, and the amount has not been officially disclosed. YCC's end in 2024 and the BoJ's JGB tapering are background knowledge, not taken from the sources above.
