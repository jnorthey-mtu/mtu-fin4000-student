# Current Events Study Guide 5: Treasury Buybacks and Bond Yields

*BKM Ch. 14–16 Extension*

[← All study guides](../../study-guide-index.md)

Oct 2, 2026 · Jim Northey

> **Why this current event is in the course.** The Aug–Sept 2026 Treasury buyback episode is a live case for introducing **duration and convexity** in BKM (13e) **Chapter 16, Managing Bond Portfolios**: Section 16.1 *Interest Rate Risk* (interest rate sensitivity, duration, and what determines duration) and Section 16.2 *Convexity*. A 5–10 bp yield move moves prices in proportion to duration, which is why long bonds matter far more than bills, and larger moves show the asymmetry that convexity captures. The pricing mechanics come from **Chapter 14, Bond Prices and Yields** (Section 14.2, bond pricing), and the question of whether maturity supply should move yields is the **Chapter 15, The Term Structure of Interest Rates** debate (Section 15.4, theories of the term structure: Expectations Hypothesis vs. liquidity preference and preferred habitat). Chapter titles are confirmed for the 13th edition; section numbers are from recent editions, so check them against your copy.

## Learning objectives

After this guide you should be able to:

1. Explain how a Treasury buyback works (who sells, who pays, where the cash comes from) and why it differs from Fed QE.
2. Separate the *supply-and-demand* effect of a buyback from the *liquidity*, *term-premium* and *signaling* channels.
3. Judge whether a yield decline from a buyback is likely to be transitory or lasting.
4. Explain why buybacks funded with bills shift the maturity mix, and what that implies for short-term rates and rollover risk.
5. Compute the price and yield effect of a buyback with duration and BA II Plus keystrokes (Ch. 14 and 16 tools).

## Core concept: why a buyback moves yields (it is more than supply and demand)

A buyback is Treasury paying cash to dealers for outstanding bonds, retiring them, and funding the cash mostly with newly issued bills. Supply and demand is only the first of four channels. The Aug 19, 2026 announcement doubled the cap per long-end operation from \$2 billion to at least \$4 billion, effective Sept 9 through Nov 4 ([Treasury press release](https://content.govdelivery.com/accounts/USTREAS/bulletins/425aba1)). Yields on the 30-year had just reached their highest level since 2007 and fell by as much as 10 bp on the news ([First Eagle](https://www.firsteagle.com/blog/can-buybacks-keep-yields-check)).

| Channel | Mechanism | Likely size and durability |
| --- | --- | --- |
| 1. Supply and demand | Treasury is a price-insensitive buyer, so long bonds held by the public shrink | Small: each operation is tiny relative to the market, and analysts argue the market is too large for buybacks of this size to matter ([Euronews](https://www.euronews.com/2026/09/10/us-treasury-yields-surge-as-6-billion-bond-buyback-disappoints-markets)) |
| 2. Liquidity premium | Retiring thin off-the-run bonds cleans up dealer balance sheets and lets the rest trade more easily, so investors demand less liquidity compensation | Real but fades; ING notes liquidity improved at first, then the benefit waned ([ING](https://think.ing.com/downloads/pdf/snap/us-treasury-ups-its-buying-of-long-dated-treasuries)) |
| 3. Term premium / duration extraction | If funded with bills, the public must hold less duration, which lowers the compensation required for bearing rate risk | Depends on net duration removed; limited because Treasury still issues new debt elsewhere |
| 4. Signaling | A surprise, unscheduled increase tells markets Treasury cares about the long end ([Robeco](https://www.robeco.com/it-it/approfondimenti/2026/08/us-treasuries-buyback-and-impact-on-the-fed-and-markets)) | Large on announcement day, but it erodes if follow-through disappoints |

**Not QE.** Buybacks draw on the Treasury General Account (TGA) and are a debt-management tool; they do not create bank reserves, and TGA balance rules limit how fast they can scale ([CME Group](https://www.cmegroup.com/insights/economic-research/2026/can-treasury-buyback-reverse-bearish-sentiment-in-bonds.html)). **Not Operation Twist** either: the Fed's Twist was a deliberate duration swap to cut long yields, whereas Treasury's stated framework is liquidity support and cash management that should not change the maturity profile ([Basis Point Insight](https://basispointinsight.com/Story/us-treasury-buybacks-bring-relief-but-are-no-hand-of-god-for-markets_ebe99fe64cd3.html)).

**What is the TGA?** The Treasury General Account is the federal government's checking account at the Federal Reserve. Tax receipts and proceeds from Treasury auctions flow in, and payments such as Social Security and debt service flow out. When the TGA rises (for example after bill auctions or tax dates), cash leaves bank reserves and tightens funding markets. When it falls, reserves rise. Because buybacks are paid from this balance, the TGA is both the funding source and the constraint, and the balance changes how much liquidity is in the system. Read more: [New York Fed, Treasury and Federal Reserve cash management](https://www.newyorkfed.org/medialibrary/media/research/current_issues/ci18-3.html) (primary source) and [BabyPips TGA explainer](https://www.babypips.com/learn/forex/treasury-general-account-tga-explained) (plain-language overview, with where to find the daily balance).

**What is QE?** Quantitative easing is a central bank buying large amounts of long-term securities, paid for by creating bank reserves, to push down long-term yields when short-term rates cannot be cut further. The purchases remove duration from private hands, which lowers the term premium (a portfolio-balance effect). A San Francisco Fed paper argues the reserve creation itself also matters. One Swiss National Bank study estimates Fed QE lowered 10-year Treasury yields by roughly 46–85 bp through liquidity effects between 2009 and 2011, plus about 20 bp from reduced bond supply. That contrast shows why a Treasury buyback, funded with existing cash and bills and creating no reserves, should be expected to have a much smaller effect than QE, in line with the 5–10 bp moves seen in August. Read more: [SF Fed, Transmission of Quantitative Easing](https://www.frbsf.org/economic-research/publications/working-papers/2014/18/) (primary source), [SNB, Liquidity Effects of QE](https://www.snb.ch/en/mmr/papers/id/working_paper_2012_02) (magnitudes), and [Plus500 QE explainer](https://us.plus500.com/en/newsandmarketinsights/quantitative-easing-guide) (plain-language overview).

**Textbook link (Ch. 15).** Under the pure Expectations Hypothesis only expected future short rates matter, so a change in maturity supply should do nothing. Liquidity preference and preferred-habitat theories say supply by maturity can move term premiums. The buyback debate is a live test of which theory applies. Duration (Ch. 16) converts any yield change into a price change:

```math
\frac{\Delta P}{P} \approx -D^{*}\,\Delta y + \tfrac{1}{2}\,C\,(\Delta y)^2
```

**Where:**

- **ΔP / P** = percentage change in the bond price, as a decimal (0.0125 means +1.25%). P is the starting price and ΔP is the new price minus the starting price.
- **D*** = modified duration, in years. It is the approximate % price change for a 1% (100 bp) change in yield.
- **Δy** = change in the bond's yield, as a decimal annual rate (−8 bp = −0.0008). The minus sign in front of D* means prices fall when yields rise.
- **C** = convexity (years squared), a measure of the curvature of the price-yield curve.
- **½ C (Δy)²** = the convexity adjustment. It is always positive, so it adds to the price gain from a yield drop and trims the loss from a yield rise.
- **≈** = approximation; accurate for small Δy and less so for large moves.

## Lasting impact and sustainability: relief is likely transitory unless the drivers change

Most analysts in the Aug–Sept 2026 coverage expect a dampening effect, not a reversal. ING calls buybacks essentially zero-sum, since Treasury still issues new debt, so they are unlikely to change the natural upward path of long yields ([ING](https://think.ing.com/downloads/pdf/snap/us-treasury-ups-its-buying-of-long-dated-treasuries)). Robeco agrees an activist Treasury can move yields in the short term but says the action does not address why long yields are high ([Robeco](https://www.robeco.com/it-it/approfondimenti/2026/08/us-treasuries-buyback-and-impact-on-the-fed-and-markets)).

**What the market has shown so far**

- Aug 19: yields fell sharply on the surprise announcement (up to 10 bp on the 30-year).
- Sept 9: a \$6 billion operation disappointed investors who expected more, and long yields rose again, helped by Brent crude above \$100 ([Euronews](https://www.euronews.com/2026/09/10/us-treasury-yields-surge-as-6-billion-bond-buyback-disappoints-markets)).
- Treasury will revisit sizes at the Nov 4 refunding, so the program size is not yet settled.

**What is pushing yields up (not touched by buybacks)**

- Higher term premiums from deficit spending, heavy debt issuance and persistent-inflation risk ([Trading Economics](https://tradingeconomics.com/united-states/government-bond-yield/news/576655)).
- Rising global yields (Japan, France, UK), so this is not only a US phenomenon ([CME Group](https://www.cmegroup.com/insights/economic-research/2026/can-treasury-buyback-reverse-bearish-sentiment-in-bonds.html)).
- Expectations of higher short rates; futures raised the odds of a Fed hike as oil and yields climbed.

**Are buybacks sustainable with rising spending?** As a liquidity tool, yes, because they are small and flexible. As a way to hold down yields against large deficits, doubtful. The cash must come from the TGA or new borrowing, so deficits and buybacks compete for the same funding, and TGA rules cap the pace ([CME Group](https://www.cmegroup.com/insights/economic-research/2026/can-treasury-buyback-reverse-bearish-sentiment-in-bonds.html)). First Eagle is skeptical the relief lasts and warns that funding with shorter debt adds rollover risk ([First Eagle](https://www.firsteagle.com/blog/can-buybacks-keep-yields-check)).

**Exam framing.** A lasting effect requires a lasting change in net duration supply or in term-premium drivers. A liquidity-and-signaling effect decays unless it is repeated or backed by credible fiscal change.

## Bills vs. bonds: yes, buybacks lean on bills, but the bigger effect is rollover risk, not higher short rates

Buybacks are funded from cash on hand, typically raised by issuing new bills, so the net effect is swapping old long-term debt for new short-term debt ([BIT Knowledge Hub](https://www.bit.com/knowledge-hub/treasury-buyback-program)). The "issue bills instead of bonds" idea is wider than buybacks: traders call it "T-bill and chill", where coupon auction sizes are held steady and bills absorb marginal borrowing, which eases long-end supply pressure but shifts risk to short rates ([TrendForce](https://datatrack.trendforce.com/blog/content/62282/u-s-keeps-coupon-treasury-issuance-steady-as-t-bill-and-chill-deepens-reliance-on-short-term-debt-and-refinancing-risks)).

**Will more bills raise short-term rates?** Only slightly, for three reasons:

1. Bill yields are anchored by the Fed's policy rate. More supply can cheapen bills a little relative to the policy rate, but it does not set the level.
2. Money market funds are the largest buyers and absorb bills readily ([Reuters via Zawya](https://www.zawya.com/en/web-section/insights/us-treasury-bill-issuance-grows-heightens-long-term-risk-407695)).
3. The buyback cash need is modest. One analyst estimates a \$2 billion operation drew only about \$1.3 billion from the TGA, so the added bill issuance is small ([Reverse Engineering Finance](https://johncomiskey.substack.com/p/august-treasury-model-update)). The Fed is also buying bills for reserve management, which offsets some supply.

**The real cost is exposure to the Fed.** Short-term supply pressure rises less than the sensitivity of interest costs to future Fed moves. Over 75% of tradable debt is fixed-rate paper issued at two years or longer, but bills roll in weeks, so a hike passes through almost immediately ([Weekly Market Brief, Aug 4](https://onrampbitcoin.com/newsletter/weekly-market-brief-2026-08-04)). That brief also reports bills near 22% of tradable debt, above the 15%–20% range Treasury's advisory committee (TBAC) recommends; Reuters reports the same TBAC range ([Reuters via Zawya](https://www.zawya.com/en/web-section/insights/us-treasury-bill-issuance-grows-heightens-long-term-risk-407695)). Goldman projected \$827 billion of net bill issuance for 2026.

**Trade-off in one line.** Bill funding lowers today's long-end supply and interest cost, but raises refinancing frequency and Fed-rate sensitivity. If short rates rise enough, the interest saving reverses (see the break-even in Worked example 3).

## Duration and convexity primer: how much a bond price moves when yields move

**Duration** measures a bond's sensitivity to yield changes, and it is the tool that turns "yields fell 8 bp" into "prices rose 1.2%." Macaulay duration is the present-value-weighted average time until you receive a bond's cash flows, in years. Modified duration (D*) divides it by (1 + y/2) for semiannual bonds and gives the approximate percentage price change for a 1% change in yield. The 30-year 4.75% bond used below has a Macaulay duration of about 15.9 years, far less than its maturity, because coupons arrive along the way. Duration rises with longer maturity, lower coupon and lower yield, and a zero-coupon bond's duration equals its maturity.

```math
\frac{\Delta P}{P} \approx -D^{*}\,\Delta y \qquad D^{*}=\frac{D_{\text{Macaulay}}}{1+y/2}
```

**Where:**

- **ΔP / P** = percentage change in the bond price, as a decimal (0.0124 means +1.24%).
- **D*** = modified duration, in years.
- **Δy** = change in yield, as a decimal annual rate (−8 bp = −0.0008).
- **D\_Macaulay** = Macaulay duration, in years: the present-value-weighted average time until the bond's cash flows are received.
- **y** = the bond's yield to maturity as a decimal annual rate (5.10% = 0.0510), the starting yield before the change.
- **1 + y/2** = the semiannual compounding adjustment, since y/2 is the yield per six-month period. For annual-pay bonds use 1 + y.
- **−** (minus sign) = prices and yields move in opposite directions.

**Convexity** corrects duration's main weakness. Duration is a straight-line (tangent) approximation, but the true price-yield relationship is curved. Because of that curvature, a yield decline raises price by more than an equal yield increase lowers it, and the gap grows with the size of the move and with the bond's duration. For our bond at 5.10%, a 100 bp move shows the effect (duration D* = 15.50, convexity C ≈ 354):

| Yield change | Duration only | Duration + convexity | Exact |
| --- | --- | --- | --- |
| −100 bp (to 4.10%) | +15.50% | +17.28% | +17.44% |
| +100 bp (to 6.10%) | −15.50% | −13.73% | −13.88% |

For small moves such as the 5–10 bp buyback reactions, duration alone is accurate (Example 2 below). For large moves, add the convexity term ½ × C × (Δy)², as in the Core concept formula.

**Why this matters for buybacks.** A bill has a duration under one year, while a 30-year bond has a duration around 15. Retiring long bonds and funding with bills therefore removes a lot of interest-rate risk from the public's hands, which is the duration-extraction (term-premium) channel. It also explains why a long-end operation has a much larger duration-weighted effect than the same dollar amount in a shorter bucket, as ING notes ([ING](https://think.ing.com/downloads/pdf/snap/us-treasury-ups-its-buying-of-long-dated-treasuries)). Duration and convexity are covered in BKM Ch. 16; use them whenever a question gives a yield change and asks for a price change.

## Worked examples (BA II Plus)

Setup once: `2nd` `P/Y` `1` `ENTER` `2nd` `QUIT`, then `2nd` `FORMAT` `2` `ENTER` for two decimals. We use semiannual periods directly, so P/Y = 1. Numbers are illustrative.

**Example 1: price effect of an 8 bp drop.** A 30-year, 4.75% semiannual coupon bond yields 5.10%. A buyback pushes its yield to 5.02%. Find the price change.

1. `2nd` `CLR TVM`
2. `60` `N`, `2.55` `I/Y`, `23.75` `PMT`, `1000` `FV`, `CPT` `PV` gives −946.52
3. Change `I/Y` to `2.51`, `CPT` `PV` gives −958.37
4. Change: 958.37 / 946.52 − 1 = **+1.25%**, about +\$11.85 per \$1,000 face.

**Example 2: check with modified duration.** Macaulay duration is about 15.90 years, so modified duration is 15.90 / 1.0255 = 15.50. Then ΔP/P ≈ −15.50 × (−0.0008) = **+1.24%**, close to the exact +1.25%. The small gap is convexity (Ch. 16).

**Example 3: bill-funded buyback and break-even.** Treasury retires \$4 billion par of a 3.0% bond priced at 70, so it pays \$2.8 billion in cash raised with bills at 3.76%.

| Item | Annual interest |
| --- | --- |
| Coupon retired (\$4B × 3.0%) | \$120.0M |
| New bill cost (\$2.8B × 3.76%) | \$105.3M |
| Saving at today's bill rate | \$14.7M |

Break-even bill rate = \$120.0M / \$2.8B = **4.29%**. If bills roll at a higher rate, the swap costs more than it saves, so a 100 bp rise to 4.76% costs \$133.3M. Face value of debt also falls by \$1.2 billion (\$4.0B − \$2.8B), which is the discount captured because the bond is below par.

The same calculation as a formula:

```math
r^{*} = \frac{\text{Par} \times c}{\text{Par} \times \text{Price}/100} = \frac{c}{\text{Price}/100}
```

**Where:**

- **r*** = the break-even bill rate (4.29% here). Above it, the bill-funded swap costs more interest than it saves.
- **Par** = face value of the bonds retired (\$4 billion). It cancels out of the ratio.
- **c** = coupon rate on the retired bond (3.0%), so Par × c = the annual coupon interest no longer paid (\$120.0M).
- **Price** = the bond's market price as a percent of par (70), so Par × Price/100 = the cash Treasury pays and must raise with bills (\$2.8B).

**Pattern to remember:** price change from a yield shift is a Ch. 16 problem; whether the funding is sustainable is a rollover-risk problem.

## Common pitfalls and key-terms checklist

The most common error is treating a buyback as Fed-style QE or as free money; it is neither.

**Pitfalls**

- Calling buybacks QE. Treasury funds them from the TGA and bill proceeds and creates no reserves; the Fed buys securities by creating reserves.
- Reading the announcement-day move as the permanent effect. Signaling and liquidity effects decay.
- Ignoring the funding side. A buyback retires long debt but adds bills, so net duration supply and rollover risk both change.
- Mixing up par and market value. Cash paid is market value; debt retired is par, so a below-par bond retires more face than cash paid (Example 3).
- Using the wrong keystroke setup: with P/Y = 1, enter N as periods (60) and I/Y as the semiannual rate (2.55), not 5.10.
- Assuming more bills means much higher short rates. Policy rate expectations dominate; the supply effect is small.

**Key terms**

- [ ] **Buyback (liquidity support vs. cash management):** Treasury repurchases outstanding securities from dealers for cash. Liquidity-support buybacks target thinly traded off-the-run bonds to improve trading. Cash-management buybacks smooth swings in the TGA around tax dates.
- [ ] **On-the-run / off-the-run:** The on-the-run security is the most recently auctioned issue of a given maturity and the most liquid. Off-the-run issues are older and trade less.
- [ ] **Treasury General Account (TGA):** The federal government's checking account at the Federal Reserve. Tax receipts and auction proceeds flow in, payments flow out, and buybacks are paid from it. A rising TGA drains bank reserves.
- [ ] **Bank reserves:** Balances commercial banks hold at the Fed. QE creates them, and a rising TGA drains them.
- [ ] **Quantitative easing (QE):** A central bank buys large amounts of long-term securities, paying with newly created reserves, to lower long-term yields when short-term rates cannot fall further.
- [ ] **Operation Twist:** The Fed sells short-term securities and buys long-term ones to lower long yields without enlarging its balance sheet.
- [ ] **Term premium:** The extra yield investors require for holding a long-term bond instead of rolling short-term ones; the part of a long yield not explained by expected short rates.
- [ ] **Duration extraction:** Reducing the interest-rate risk (duration) the public must hold, for example by retiring long bonds and issuing bills. This is the portfolio-balance channel behind lower term premiums.
- [ ] **Preferred habitat / market segmentation:** Investors favor certain maturities, so the supply of each maturity can move its yield. Under this view, buybacks can matter.
- [ ] **Expectations Hypothesis:** A long yield equals the average of expected future short rates, so maturity supply is irrelevant. Under this view, buybacks should not matter.
- [ ] **Rollover (refinancing) risk:** The risk that maturing debt must be refinanced at higher rates. It rises as the bill share of debt rises.
- [ ] **TBAC bill-share guideline:** The Treasury Borrowing Advisory Committee recommends keeping bills at about 15%–20% of marketable debt.
- [ ] **Modified duration and convexity:** Modified duration is Macaulay duration divided by (1 + y/2) for semiannual bonds; it gives the approximate % price change for a 1% yield change. Convexity captures the curvature that duration misses.

## Practice questions (CFA-style) and answer key

**Q1 (conceptual).** Which statement about a Treasury buyback is most accurate?

A. It is funded by creating new bank reserves, like QE.

B. It is funded from cash on hand, typically raised by issuing bills, and does not create reserves.

C. It permanently lengthens the average maturity of outstanding debt.

**Q2 (conceptual).** Under the pure Expectations Hypothesis, a bill-funded buyback of long bonds should:

A. lower long-term yields through a lower term premium.

B. leave yields unchanged, since only expected future short rates matter.

C. raise short-term yields only.

**Q3 (algorithmic).** A 30-year, 4.75% semiannual bond yields 5.10% and a buyback lowers the yield to 5.02%. The price change is closest to:

A. +0.80%

B. +1.25%

C. +2.50%

**Q4 (algorithmic).** Treasury buys back \$4 billion par of a 3.0% bond priced at 70 using bills. Annual interest cost falls only if the bill rate stays below:

A. 3.00%

B. 4.29%

C. 5.00%

**Q5 (conceptual).** Which best explains why a \$4 billion buyback operation is unlikely to durably offset rising long yields driven by deficits?

A. Treasury still issues new debt to fund deficits, so net supply to the market is not materially reduced.

B. Buybacks raise the policy rate.

C. Buybacks are exempt from TGA balance limits.

**Q6 (conceptual).** If the bill share of marketable debt rises above the 15%–20% guideline, the main risk that increases is:

A. call risk.

B. rollover (refinancing) risk.

C. reinvestment risk on zero-coupon bonds.

**Answer key**

1. **B.** Treasury raises cash with bills and pays dealers; no reserves are created. A describes QE. C is wrong because the stated framework is not to change the maturity profile, and bill funding if anything shortens it.
2. **B.** Under the Expectations Hypothesis the long rate is an average of expected short rates, so maturity supply is irrelevant. A is the preferred-habitat or portfolio-balance view.
3. **B.** Price at 5.10% is \$946.52 and at 5.02% is \$958.37, a +1.25% change. Duration check: 15.50 × 0.0008 = 1.24%.
4. **B.** Cash paid is \$2.8B, coupon retired is \$120M, so break-even = 120 / 2,800 = 4.29%. Above that, the swap increases interest cost.
5. **A.** The effect is largely zero-sum while deficits require new issuance. B is false, and TGA limits do constrain buybacks, so C is wrong.
6. **B.** Bills mature quickly, so more debt must be refinanced more often at prevailing rates.

## Recent articles reading list (Aug 19 – Sept 10, 2026)

Start with the Treasury release, then ING and First Eagle for the two sides of the debate. Newest first within each group; search snippets were used, so open each page before quoting it.

**Primary and institutional**

| Source | Date | Why read it |
| --- | --- | --- |
| [Euronews: \$6 billion buyback disappoints](https://www.euronews.com/2026/09/10/us-treasury-yields-surge-as-6-billion-bond-buyback-disappoints-markets) | Sept 10 | Shows the relief fading; size vs. expectations, oil, Fed-hike odds |
| [Basis Point Insight: no hand of God](https://basispointinsight.com/Story/us-treasury-buybacks-bring-relief-but-are-no-hand-of-god-for-markets_ebe99fe64cd3.html) | Aug 21 | Buybacks are liability management, not QE; limits vs. deficits |
| [CME Group: can buybacks reverse bearish sentiment](https://www.cmegroup.com/insights/economic-research/2026/can-treasury-buyback-reverse-bearish-sentiment-in-bonds.html) | Aug | TGA constraint, off-the-run liquidity, global yield trends |
| [Robeco: buybacks and the Fed](https://www.robeco.com/it-it/approfondimenti/2026/08/us-treasuries-buyback-and-impact-on-the-fed-and-markets) | Aug 20 | Why this is not Operation Twist; fiscal pressure persists |
| [First Eagle: can buybacks keep yields in check?](https://www.firsteagle.com/blog/can-buybacks-keep-yields-check) | Aug | Skeptical case; shorter-dated funding and rollover risk |
| [ING: Treasury ups its buying](https://think.ing.com/downloads/pdf/snap/us-treasury-ups-its-buying-of-long-dated-treasuries) | Aug 19 | Zero-sum argument; 5–10 bp move; liquidity benefit waning |
| [NY Life MacKay Shields: buyback announcement](https://www.nylim.com/assets/mackay-shields/documents/insights/treasurys-buyback-announcement.pdf) | Aug 19 | Signal that buyback objectives may be broadening |
| [Treasury press release](https://content.govdelivery.com/accounts/USTREAS/bulletins/425aba1) | Aug 19 | The official wording: \$2B cap to at least \$4B, Sept 9 to Nov 4 |

**On bills and issuance mix**

| Source | Date | Why read it |
| --- | --- | --- |
| [TrendForce: "T-bill and chill"](https://datatrack.trendforce.com/blog/content/62282/u-s-keeps-coupon-treasury-issuance-steady-as-t-bill-and-chill-deepens-reliance-on-short-term-debt-and-refinancing-risks) | Aug | Steady coupon sizes, bills absorb borrowing, refinancing risk |
| [Reuters via Zawya: bill issuance grows](https://www.zawya.com/en/web-section/insights/us-treasury-bill-issuance-grows-heightens-long-term-risk-407695) | 2026 | Goldman bill forecast, TBAC 15–20% guideline, money fund demand |

**Use with caution (secondary or commentary):** [Weekly Market Brief, Aug 4](https://onrampbitcoin.com/newsletter/weekly-market-brief-2026-08-04) (22% bill share, fixed-rate share of debt), [Reverse Engineering Finance](https://johncomiskey.substack.com/p/august-treasury-model-update) (TGA cash drawn per operation), [Vault Report](https://thevaultreport.com/treasury-buybacks) (cumulative buyback tally). Verify against Treasury Fiscal Data before using their figures on an exam.

*Open item: Treasury will revisit buyback sizes at the Nov 4, 2026 refunding. Update this guide then.*
