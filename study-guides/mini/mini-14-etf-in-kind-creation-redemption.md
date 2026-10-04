# Mini Study Guide 14: ETF In-Kind Creation/Redemption and Tax Avoidance

*BKM Ch. 4*

[← All study guides](../../study-guide-index.md)

Sep 29, 2026 · Jim Northey

## Learning objectives

ETFs avoid most capital gains distributions because Authorized Participants (APs) create and redeem shares in kind, and Treasury announced on Monday, Sept. 28, 2026 that it is targeting abuses of that mechanism. After this guide you should be able to:

1. Explain the creation/redemption process and why in-kind exchanges are not taxable events for the fund.
2. Contrast an ETF with an open-end mutual fund on capital gains distributions (Ch. 4).
3. Describe how heartbeat trades, low-basis lot redemptions and 351 conversions push that mechanism further.
4. Summarize what Treasury and the IRS announced and which tactics are named.
5. Compute an investor's tax drag from a distribution and after-tax return.

## Core concept: the in-kind loophole

When an AP exchanges a basket of stocks for ETF shares (creation) or ETF shares for a basket of stocks (redemption), the swap is treated as an in-kind transaction, so the fund realizes no capital gain on the securities it hands over. Most ETFs are registered investment companies, and the tax code (IRC §852(b)(6)) says a RIC does not recognize gain when it distributes appreciated property to redeem its own shares. An ordinary corporation would owe tax on the same distribution under §311(b).

**How the cycle works**

1. **Creation.** The AP buys the ETF's basket in the market, delivers it to the fund, and receives a Creation Unit (commonly 25,000-50,000 shares) of new ETF shares.
2. **Trading.** The AP sells those shares on the exchange; arbitrage keeps price close to NAV.
3. **Redemption.** The AP hands back a Creation Unit and receives the underlying basket instead of cash.
4. **Tax effect.** The fund gives away its lowest-basis (most appreciated) shares in the basket, so the gain leaves with them and is never distributed to remaining shareholders. This is often called "purging" low-basis lots.

**Why a mutual fund differs.** A mutual fund meets redemptions with cash. It sells securities, realizes gains, and by law must pass them on to all remaining shareholders, who owe tax even if they never sold a share. An ETF's investors generally owe tax only when they sell their own shares.

**Caveat.** Cash-heavy ETFs (bond ETFs, some international or leveraged funds) redeem partly in cash and can still distribute gains, as ETF prospectuses themselves disclose. The advantage is deferral, not elimination: your basis stays low until you sell or, in the best case, until a step-up at death.

## Worked example: same portfolio, same redemption

A fund holds \$100M of stock with a \$60M cost basis (a \$40M unrealized gain, 40% of value). Shareholders redeem \$20M. Assume a 23.8% tax rate on gains (20% long-term rate + 3.8% NIIT) and a remaining investor holding \$100,000 of the fund.

|  | Mutual fund (cash) | ETF (in kind) |
| --- | --- | --- |
| Stock delivered or sold | \$20M sold | \$20M handed to AP |
| Gain realized by fund | \$20M × 40% = \$8M | \$0 (§852(b)(6)) |
| Distribution to remaining holders | \$8M / \$80M = 10% of NAV | \$0 |
| Distribution on a \$100,000 holding | \$10,000 | \$0 |
| Tax due this year | \$10,000 × 23.8% = \$2,380 | \$0 |

**Deferral value.** Suppose the \$2,380 stays invested at 7% for 20 years. On the BA II Plus: 2nd CLR TVM, N = 20, I/Y = 7, PV = -2,380, CPT FV = about \$9,210. The ETF investor still owes tax on the gain at sale, so the benefit is the deferral (and a possible step-up in basis at death), not permanent exemption.

**Exam angle.** Expect a conceptual question asking why the ETF shareholder faces a smaller tax bill from fund activity, and an algorithmic one computing after-tax return net of a distribution.

## Strategies built on the in-kind mechanism

The basic in-kind exchange is uncontroversial; the strategies below stack other tactics on top of it. Definitions follow [Bloomberg's Sept. 29 report](https://www.wealthmanagement.com/etfs/-black-holes-for-capital-gains-tax-come-under-treasury-fire) and [AdvisorHub's Sept. 28 report](https://www.advisorhub.com/irs-threatens-crackdown-on-array-of-wall-street-tax-dodges/) unless noted.

| Strategy | How it works | Tax result sought | Status after Sept. 28 |
| --- | --- | --- | --- |
| Routine low-basis purge | ETF gives APs its lowest-basis lots at each redemption | Fund never realizes or distributes the gain | Treasury officials said in July that creation-redemption itself is not at issue |
| Heartbeat trades | Artificial creation/redemption flows generate a large in-kind redemption on demand | Removes large embedded gains from the fund | Used in the Twin Oak example; the notice's first category covers in-kind use "inconsistent" with the mechanism's purpose, and heartbeats are not named as such |
| §351 ETF conversion | Investors contribute appreciated stock to a new ETF, then the ETF swaps it out through in-kind redemptions | Investor reshapes a concentrated portfolio without a taxable sale | Rev. Rul. 2026-20 says a prearranged, materially different result is a taxable exchange |
| §351 + exchange fund | Exchange-fund shares are contributed to an ETF seed | Solves exchange-fund liquidity and meets the diversification test | Described in the notice; more information requested |
| Box spread ETFs | Options positions convert interest income into capital gains | Lower rate on what is economically interest | Listed in the notice; more information requested |
| Swap-based tax-aware funds | Notional principal contracts generate ordinary losses that offset income | Deductions against ordinary income | Listed in the notice; more information requested |

**§351 conversion, step by step (the 2026 focus).** IRC §351 lets investors transfer property to a corporation tax-free if they control it afterward. Investors seed a new ETF with appreciated stock (the transfer must be diversified). The ETF then redeems an AP in kind, handing out the seed stock and holding a new portfolio matching its stated strategy. The investor owns ETF shares with the old low basis, and no gain was recognized.

**Why it matters for Ch. 4.** BKM presents the ETF tax advantage as a byproduct of the creation/redemption design. These strategies show the same design being used deliberately as a tax-planning tool, which is the policy question regulators are now weighing.

## Latest: Treasury and IRS action, Monday, Sept. 28, 2026

On Sept. 28, 2026 Treasury and the IRS issued a notice seeking information on "tax-aware" strategies and a revenue ruling, [Rev. Rul. 2026-20](https://www.irs.gov/pub/irs-drop/rr-26-20.pdf), that treats prearranged §351 ETF conversions as taxable. Secretary Bessent said on X that Treasury is serious about cracking down on transactions designed to dodge taxes. Details come from the [IRS ruling text](https://www.irs.gov/pub/irs-drop/rr-26-20.pdf), [AdvisorHub/Bloomberg](https://www.advisorhub.com/irs-threatens-crackdown-on-array-of-wall-street-tax-dodges/), and [Bloomberg via Wealth Management](https://www.wealthmanagement.com/etfs/-black-holes-for-capital-gains-tax-come-under-treasury-fire).

**The ruling (Rev. Rul. 2026-20)**

- **Fact pattern.** An investor transfers an appreciated, diversified portfolio to a new ETF. Under the same plan, the ETF issues shares to an AP for securities that fit its strategy, then shortly afterward redeems the AP with the investor's contributed securities. The ETF ends up holding a portfolio "materially different" from what the investor contributed.
- **Holding.** The ETF is treated as a mere conduit. The investor is treated as making a taxable exchange under §1001 with the AP, and the result is the same with multiple investors.
- **Legal basis.** Substance-over-form and step-transaction doctrines, in a line of cases including *Court Holding* and *Kuper*, plus Rev. Rul. 71-336, which is amplified.
- **What the ruling leaves alone.** §852(b)(6) itself is untouched: the ruling covers a prearranged plan that swaps out contributed securities, not ordinary redemptions.

**The notice**

- It requests information on two groups of tactics: ETFs using in-kind redemption for tax benefits "inconsistent" with its purpose, and strategies used by tax-optimized funds (box spread ETFs; swap-based funds such as AQR's Delphi Plus).
- Treasury is considering more guidance or other action, including designating some strategies "transactions of interest", which triggers extra disclosure. The notice named no specific products or issuers.
- One reported example: Twin Oak Active Opportunities ETF (TSPX) launched in February 2025 with about \$450M, including roughly \$200M of embedded gains in two tech stocks, and within a week those holdings were replaced with an S&P 500 fund via heartbeat trades.

**Market reaction and open questions**

- Bloomberg reports 351-conversion ETFs have grown into a roughly \$23B business, and Affiliated Managers Group (a stake-holder in AQR) fell about 1.5% on the news.
- Practitioners disagree on scope. Sullivan & Cromwell's Jeffrey Hochberg noted uncertainty over how long an ETF must hold contributed securities; Practus's Raymond Holst said routine seeding "in an appropriate manner" is not chilled; Alpha Architect's Wes Gray said conversions remain possible when the ETF genuinely intends to hold the seed securities.
- The Investment Company Institute said it is assessing the guidance and plans to respond. Sources describing the notice also say later guidance could apply retroactively (Traders Union summary; unverified against the notice itself).

**Bottom line for students.** The regulators are not challenging the AP in-kind exchange itself. They are challenging plans where a contribution and an in-kind redemption are linked so that one appreciated portfolio becomes a different one with no tax.

## Common pitfalls and key-terms checklist

**Pitfalls**

- Saying ETFs "avoid taxes." They defer gains inside the fund; the investor still pays when selling shares.
- Assuming every ETF is tax-free on redemptions. Cash redemptions force sales and can create distributions.
- Mixing up the fund and the investor. Fund-level recognition is what §852(b)(6) removes; investor-level tax on sale remains.
- Treating the Sept. 28 ruling as a ban on in-kind redemptions. It targets a prearranged contribution-and-redemption plan, and the notice only asks for information on other tactics.
- Confusing the tactics: box spread ETFs convert interest into capital gains; §351 conversions defer gains on a contributed stock portfolio.
- Using the wrong denominator when spreading a mutual fund's distribution: it goes to remaining shareholders, not the pre-redemption total.

**Key terms (tick when you can define each)**

- [ ] Authorized Participant (AP)
- [ ] Creation Unit
- [ ] Creation and redemption in kind
- [ ] Regulated investment company (RIC)
- [ ] IRC §852(b)(6) and §311(b)
- [ ] Cost basis and low-basis lots
- [ ] Heartbeat trade
- [ ] §351 conversion (ETF seed)
- [ ] Substance over form and step-transaction doctrines
- [ ] Box spread ETF
- [ ] Transaction of interest
- [ ] Tax deferral vs. tax elimination

## Practice questions (CFA-style)

**1.** Why can a typical equity ETF avoid distributing the capital gains that a comparable mutual fund would?

A. ETFs only hold securities with no unrealized gains.

B. Authorized Participants redeem shares for a basket of securities, and the fund does not recognize gain on that in-kind distribution.

C. ETF shareholders are exempt from capital gains tax.

**2.** A mutual fund has \$200M in assets with a \$120M cost basis. It sells \$30M of stock, in proportion to its holdings, to pay redemptions. An investor holds \$50,000 of the fund after the redemption, and the tax rate on gains is 23.8%. The investor's tax on the resulting distribution is closest to:

A. \$714

B. \$840

C. \$0

**3.** Under Rev. Rul. 2026-20, which transaction is most likely to be recharacterized as a taxable exchange?

A. An AP redeems a Creation Unit of an established ETF for its underlying basket in the ordinary course.

B. Investors contribute an appreciated, diversified portfolio to a new ETF, and under the same plan the ETF soon redeems an AP with those securities, leaving a materially different portfolio.

C. An ETF investor sells shares after holding them for ten years.

**4.** The main tax benefit an ETF investor gets from in-kind redemptions is best described as:

A. permanent elimination of tax on the gain.

B. deferral of tax until the investor sells, because basis stays low.

C. conversion of ordinary income into capital gains.

**5.** Which ETF is most likely to still distribute capital gains?

A. A large-cap index ETF that redeems entirely in kind.

B. An ETF that meets a large share of its redemptions in cash.

C. An ETF with no redemptions during the year.

**6.** If Treasury designates a strategy a "transaction of interest," this most likely means participants must:

A. stop using the strategy immediately.

B. provide additional disclosure about the transaction to the IRS.

C. pay a fixed penalty tax on the position.

## Answer key

| Q | Answer | Explanation |
| --- | --- | --- |
| 1 | B | Under §852(b)(6) a RIC does not recognize gain when it distributes property to redeem shares on demand. A is false (ETFs hold gains), and C is false (shareholders are taxed when they sell). |
| 2 | B | Gain fraction = 1 - 120/200 = 40%. Gain realized = \$30M × 40% = \$12M. Remaining assets = \$170M, so distribution = 12/170 = 7.06% of NAV. On \$50,000: \$3,529 × 23.8% = \$840. Choice A uses \$200M as the denominator. |
| 3 | B | It matches the ruling's fact pattern: a planned contribution, an AP exchange, and a prompt redemption leaving a materially different portfolio. The investor is treated as making a taxable §1001 exchange with the AP. A and C are ordinary transactions. |
| 4 | B | The gain is deferred, not eliminated. Choice C describes box spread ETFs, not in-kind redemptions. |
| 5 | B | Cash redemptions force the fund to sell securities and realize gains, a risk ETF prospectuses themselves disclose. |
| 6 | B | The designation, per Bloomberg's report, requires additional disclosure; it does not itself ban the strategy or impose a penalty. |

## Reading list and sources

Facts about the Sept. 28 action come from the first three pages, which I opened in full. The others were read only as search excerpts or are linked from those pages, so check them before citing.

**Opened**

1. [Rev. Rul. 2026-20](https://www.irs.gov/pub/irs-drop/rr-26-20.pdf), IRS, Sept. 28, 2026: primary source for the §351 / §852(b)(6) holding.
2. [IRS Threatens Crackdown on Array of Wall Street Tax Dodges](https://www.advisorhub.com/irs-threatens-crackdown-on-array-of-wall-street-tax-dodges/), Bloomberg News via AdvisorHub, Sept. 28, 2026: the notice, box spread ETFs, swap-based funds, "transactions of interest."
3. ["Black Holes" for Capital-Gains Tax Come Under Treasury Fire](https://www.wealthmanagement.com/etfs/-black-holes-for-capital-gains-tax-come-under-treasury-fire), Tsekova and Lee, Bloomberg via Wealth Management, Sept. 29, 2026: the latest article; Twin Oak example, heartbeat trades, practitioner reactions.

**Seen as search excerpts only**

- [US Treasury threatens crackdown on Wall Street tax-avoidance strategies](https://news.google.com/read/CBMihAFBVV95cUxPRk1mMy1xVVdVazZ4NXJ6cDhYYV9acXNTSjVuTkw0bnIwbVQyS1l0WkZhQ1Jud2laTHpzMkJiNXVuVDFSdEdvVzl6U0RmbjViV0xDLThfc3Z3eTBXYzEyRnNiREdnWXczVWdkUHlWMFR1a01nUUFpRDR5dnZGQkFJTlVVTUo?hl=en-US&gl=US&ceid=US%3Aen), Financial Times, Sept. 28, 2026 (Brent Sullivan quotes).
- [Traders Union summary](https://tradersunion.com/news/financial-news/show/3550603-us-treasury-etf-tax-crackdown/): the source for possible retroactive action; its summary also cites a June 24, 2024 date that conflicts with other reports, so treat that report with caution.
- [Franklin Templeton ETF Trust prospectus](https://www.sec.gov/Archives/edgar/data/1655589/000174177322004316/c497.htm) and [First Trust prospectus](https://www.sec.gov/Archives/edgar/data/1667919/000144554625005566/etf8_497k.htm): show ETFs' own disclosure that cash redemptions can create taxable gains.

**Background linked from the Bloomberg pieces (not opened)**

- Bloomberg, Feb. 27, 2026: Treasury first signals interest in 351 conversions.
- Bloomberg, July 21, 2026: Treasury flags "potentially abusive" strategies at an industry seminar.
- Bloomberg, July 21, 2025: "Capital Gains Vanish Into 'Black Holes' in Latest ETF Tax Trick."

**Course link.** BKM 13e, Ch. 4 (mutual funds and ETFs). Ties to the existing [Mutual Fund Costs guide](https://claude.ai/code/artifact/5509b8b5-42ae-4904-98cf-cee769824935) in the midterm study set.
