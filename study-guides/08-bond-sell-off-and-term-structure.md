# Why Bond Yields Are Rising

**FIN 4000 · Investments · Study Guide**
Ten market forces, credit risk, and the term structure of interest rates (BKM Ch. 14–15)

Prepared October 1, 2026 · Market data as of Sept 30 – Oct 1, 2026 · Instructor: Jim Northey

---

## 1. Learning Objectives

After working through this guide you should be able to:

- Explain the inverse price–yield relationship using the "bond as someone else's savings deposit" analogy.
- Distinguish what holding to maturity protects (nominal principal) from what it does not (purchasing power and opportunity cost).
- Classify each of the ten drivers of the 2026 bond selloff as expected inflation (E), short-rate path (R), supply and term premium (S), or forced selling and market structure (F).
- Explain how credit risk enters a bond's yield as a spread over the risk-free rate.
- Compute implied forward rates from a yield curve and connect the curve to the expectations, liquidity preference, and market segmentation theories.

## 2. Key Terms and Definitions

Check each term off when you can define it in your own words and use it in a sentence.

| Term | Definition |
|------|------------|
| ☐ **Coupon rate** | The fixed annual interest the issuer pays, stated as a percentage of face value. It is set at issuance and does not change when market rates move. |
| ☐ **Yield to maturity** | The single discount rate that makes the present value of all promised cash flows equal to the bond’s price. It is the return earned if the bond is held to maturity and coupons are reinvested at that same rate. |
| ☐ **Price–yield inverse relationship** | When market yields rise, existing bond prices fall, and when yields fall, prices rise. Fixed cash flows are discounted at a higher or lower rate, and the relationship is convex rather than a straight line. |
| ☐ **Duration** | A measure of a bond’s price sensitivity to yield changes, and the weighted-average time until its cash flows arrive. Modified duration approximates the percentage price change for a one-percentage-point change in yield. Longer maturities and lower coupons mean higher duration. |
| ☐ **Nominal vs. real yield** | Nominal yield is the stated return in current dollars. Real yield adjusts for inflation: approximately nominal yield minus inflation, or exactly (1 + nominal) ÷ (1 + inflation) − 1. |
| ☐ **TIPS** | Treasury Inflation-Protected Securities. Principal adjusts with the CPI and coupons are paid on the adjusted principal, so a holder to maturity locks in a real yield. |
| ☐ **Breakeven inflation** | The nominal Treasury yield minus the TIPS yield of the same maturity. It is the inflation rate at which the two investments earn the same return. |
| ☐ **Term premium** | The extra yield investors require to hold a long-term bond instead of rolling short-term bonds, compensating for interest-rate, inflation, and supply uncertainty. |
| ☐ **Expectations hypothesis** | Long-term rates reflect expected future short rates. Forward rates equal expected future spot rates, and the pure version has no term premium. |
| ☐ **Liquidity preference theory** | Investors prefer shorter maturities, so long bonds must pay a premium. Forward rates equal expected short rates plus a liquidity (term) premium, which is why the curve tends to slope upward. |
| ☐ **Market segmentation / preferred habitat** | Segmentation holds that investors are tied to particular maturities, so each maturity’s yield is set by supply and demand within it. Preferred habitat is the softer version: investors will leave their habitat if compensated. |
| ☐ **Forward rate** | The rate implied today for borrowing or lending over a future period, derived from the spot curve: (1 + s_n)ⁿ = (1 + s_(n−1))ⁿ⁻¹ × (1 + f_n). |
| ☐ **Normal, flat, and inverted curves** | A normal curve slopes upward (long yields above short), a flat curve has similar yields across maturities, and an inverted curve has short yields above long. Inversions have historically preceded recessions. |
| ☐ **Credit spread** | The extra yield on a bond over a comparable-maturity Treasury, compensating for default, downgrade, and liquidity risk. |
| ☐ **Carry trade** | Borrowing in a low-rate currency (such as yen) to invest in higher-yielding assets and earning the difference. It is vulnerable to unwinding when funding costs rise or exchange rates move. |
| ☐ **Price-sensitive vs. price-insensitive buyers** | Price-insensitive buyers (central banks, policy-driven holders) buy regardless of price. Price-sensitive buyers (hedge funds, asset managers) buy only at attractive yields, so they amplify price swings. |
| ☐ **Spot rate** | The yield on a zero-coupon bond for a given maturity: the rate for a single cash flow at that date. Spot rates are the building blocks for pricing and for forward rates. |
| ☐ **Par yield and bootstrapping** | A par yield is the coupon rate at which a bond prices at 100. Bootstrapping extracts spot rates from par yields one maturity at a time, using the earlier spot rates to price each bond. |

## 3. An Analogy of sorts: A Bond as a Savings Account

Instead of opening a savings account, you buy another investor's original *deposit*, made when the bond was issued. The word *deposit* here is an analogy: in reality the investor made a loan, but the result is much the same as depositing money in a bank account, where the money is borrowed by the bank, which seeks to earn income from using it. That *deposit* carries a fixed rate (the coupon). Similar to "time deposits" in a bank (such as a Certificate of Deposit), access to your "*deposit*" (principal) is set for a specific date in the future. However, unlike deposits, you cannot withdraw your principal from the bond issuer; you can only sell it to someone else.[^1] And that is where the bond price comes into the picture. The price you are able to sell the bond at is set by supply and demand and economic factors. If newly issued bonds pay more than the coupon of your bond, nobody will pay full price for yours, so its price falls until the buyer's return matches the going rate. If new bonds pay less, yours trades at a premium, meaning you can sell it for more than the initial "*deposit*" (bond price when purchased). Price and yield are the same quantity viewed from two sides, and longer maturities (higher duration) move more.

[^1]: Most people may not be aware that banks buy and sell deposits from one another.

### What holding to maturity does and does not protect

- **Protected:** you receive face value at maturity (barring default), so a price decline is only realized if you must sell early.
- **Not protected, purchasing power:** if inflation exceeds your yield, the real return is negative. Real yield is roughly nominal yield minus inflation.
- **Not protected, opportunity cost:** you are locked into the old rate while new deposits pay more.
- **The TIPS fix:** TIPS lock in a real yield, but they remain exposed to changes in real rates.

## 4. The Four Buckets: E, R, S, and F

These letters are this guide's own classification, not Bloomberg's. Each bucket answers a different question about why a yield moved, and the bucket tells you what would have to change for the move to reverse. A single reason can belong to more than one bucket.

| Bucket | Question it answers | What changes | Typical evidence | Reasons |
|--------|---------------------|--------------|------------------|---------|
| **E** | What will inflation do to my purchasing power? | Expected inflation | Breakeven inflation, CPI, oil and food prices | 1, 2, 8 |
| **R** | Where will the central bank set short rates? | Expected path of short rates | Fed signals, payrolls reports, futures pricing | 1, 3 |
| **S** | How much debt must investors absorb, and what do they want for the risk? | Bond supply and the term premium | Auction results, deficits, issuance volume | 4, 5, 6, 8, 10 |
| **F** | Who is being forced to sell, or who now owns the bonds? | Constraints, hedging, and the buyer base | Reserve data, positioning, mortgage duration | 3, 7, 9 |

### E: expected inflation

Coupons and principal are fixed in dollars, so higher expected inflation erodes what bondholders will be able to buy. Investors respond by demanding a higher nominal yield, which means the price must fall. The Fisher relationship summarizes it: nominal yield ≈ real yield + expected inflation. If expected inflation rises one percentage point with the real yield unchanged, the nominal yield rises about one point.

- **Bloomberg reasons:** 1 (growth fans inflation), 2 (oil and food prices), and 8 (tariffs raising import costs).
- **Reversal:** an end to the oil shock, easing tariffs, or slowing growth.
- **Hedge:** TIPS neutralize this bucket for a holder to maturity, but not the real-yield effects in R, S, and F.

### R: the short-rate path

Under the expectations hypothesis, a long yield is roughly the average of the short rates expected over the bond's life. A 10-year yield rises when markets expect the central bank to hike or to hold rates high for longer, even if inflation expectations are unchanged. For example, if the one-year rate is 4.55% and the expected rate for the next year moves from 5.0% to 5.5%, the two-year yield rises about 0.25 percentage points.

- **Bloomberg reasons:** 3 (Fed, Australia, and Japan hikes), with 1 (strong growth raising hike odds). The cited paper attributes about 90% of the rise in 10-year yields since August 2020 to events that move short-rate expectations.
- **Reversal:** weaker data or a central bank signaling cuts.
- **Distinguish from E:** E concerns inflation expectations, while R concerns the policy response, and the two usually move together.

### S: supply and term premium

Even if expected inflation and expected short rates are unchanged, yields rise when investors must absorb more bonds, or when they demand more compensation for tying up money for years. The term premium is that compensation for duration risk and uncertainty. More supply from deficits, defense spending, and corporate borrowing means buyers must be enticed with higher yields, and a weak auction shows up directly as a higher yield. Structural forces matter too: if the global savings pool that once soaked up bonds shrinks, borrowers compete harder for capital.

- **Bloomberg reasons:** 4 (AI borrowing), 5 (deficits and debt), 6 (defense), 8 (uncertainty from fragmentation), and 10 (savings glut erasure).
- **Reversal:** slower issuance, fiscal consolidation, or a return of price-insensitive buyers. Most of these are slow-moving.
- **Why it matters:** these drivers tend to lift the long end more than the short end, steepening the curve.

### F: forced selling and market structure

Some selling has nothing to do with views on inflation or rates. It comes from constraints, mandates, or a change in who owns the bonds. Because the sellers are not choosing the price, yields can overshoot what fundamentals justify, and they can reverse quickly once the pressure ends.

- **Policy-driven:** Japan selling Treasuries to support the yen (reason 7).
- **Leverage-driven:** carry traders unwinding yen-funded positions as Japanese rates rise (reason 7).
- **Hedging-driven:** mortgage investors selling Treasuries to offset longer mortgage-bond duration when refinancing slows (reason 3).
- **Buyer-base shift:** price-sensitive private investors replacing central banks, which makes yields more reactive (reason 9).
- **Reversal:** when intervention ends, positions are closed out, or hedging needs change.

**Using the buckets:** to judge whether a yield move is likely to persist, ask which bucket is driving it. E and R reverse when the economic outlook changes, S reverses slowly, and F can reverse quickly when the constraint disappears.

## 5. The Ten Reasons Yields Are Rising

*Source: "10 Reasons Investors Are Driving Government Bond Yields Higher," Ruth Carson, Masaki Kondo, and Alice Gledhill, Bloomberg, Oct 1, 2026. Summaries below are paraphrased for instruction; consult the original for full text. The buckets (E, R, S, F) are this guide's own classification, not Bloomberg's.*

**Bucket key:** E = expected inflation · R = short-rate path · S = supply and term premium · F = forced selling and market structure

| # | Reason | Summary (paraphrased) | Bucket | Teaching point |
|---|--------|-----------------------|--------|----------------|
| 1 | Resilient growth | Strong US and global activity, with PMIs pointing to the strongest manufacturing growth in years. This fuels inflation and the risk of further hikes, and it makes equities more attractive than bonds. Inflation erodes the coupons and principal bondholders will receive. | E, R | Bonds are not hedging equity risk when growth, not recession, is the threat. |
| 2 | Higher commodity prices | Goldman Sachs calls the Iran war the largest oil supply shock ever. Brent peaked above $126 as flows through the Strait of Hormuz were choked, lifting fuel prices. Food prices are also climbing, partly on heatwaves. | E | Energy shocks feed headline inflation and raise the yield investors demand. |
| 3 | Interest rate hikes | The Fed hiked in September and signals more may come. Australia and Japan have also hiked, and markets price increases in the UK, Canada, and Europe. A cited paper attributes about 90% of the rise in 10-year yields since Aug 2020 to payrolls reports and Fed speeches. Fewer refinancings also extend mortgage-bond duration, forcing some investors to sell Treasuries. | R, F | The short-rate outlook is the dominant driver of the long yield (expectations hypothesis). |
| 4 | Hyperscaler borrowing and building | The AI infrastructure race has triggered a borrowing binge: over $400 billion of bonds sold globally this year, much of it in the US. Governments, M&A borrowers, and tech firms compete harder for investor cash, and T. Rowe Price expects the extra supply to lift high-quality government yields. | S | A bond's price depends on how many other bonds compete for the same buyers. |
| 5 | Fiscal deficits and debts | Governments keep running deficits without tackling them. US debt recently passed $40 trillion, and OECD countries are expected to borrow about $18 trillion gross this year. Heavy supply pushes investors to demand higher yields. | S | Yields embed a premium for the issuer's fiscal path, not just expected short rates. |
| 6 | Defense spending | Global military spending is at a record, driven by the Iran war, Ukraine, and re-armament in NATO, the Middle East, and Asia. The US defense budget crossed $1 trillion in fiscal 2026. Larger financing needs mean more bond sales. | S | A second channel from the war to yields, through borrowing rather than oil. |
| 7 | The Japan effect | Japan's foreign securities holdings fell by a record $87.8 billion in August, likely from Treasury sales to support the yen. Separately, rising Japanese rates are forcing carry traders to sell government bonds they bought worldwide with cheap yen loans. | F | Yields can rise because of who must sell, not because expectations changed. |
| 8 | Trade wars | Tariffs raise import costs and threaten to keep inflation elevated, reinforcing higher-for-longer rate expectations. Geopolitical fragmentation also leads investors to demand extra yield for uncertainty. | E, S | Required yield has two parts: expectations and a premium for not knowing. |
| 9 | Changing ownership | The buyer base has shifted from the Fed and foreign central banks toward private investors such as hedge funds. Bloomberg Economics estimates official holdings fell about 12 points (Fed) and 8 points (foreign official) of GDP since 2020. NY Fed researchers say the market has become more price sensitive, explaining much of historical yield changes. | F | Price-insensitive holders are patient depositors; price-sensitive ones reprice immediately and amplify swings. |
| 10 | Savings glut erasure | Oxford Economics argues that the forces behind excess global savings (fiscal austerity, US deleveraging, Chinese exports) have unwound or been constrained by protectionism. Borrowers now compete harder for capital just as governments and companies need a great deal of it. | S | Lower structural savings supply raises the long-run real rate. |

## 6. Credit Risk and Bond Pricing

A corporate bond's yield decomposes into the risk-free rate, plus a credit spread, plus a liquidity premium. The spread compensates for default and downgrade risk. The bond's price is the present value of its promised cash flows discounted at that full yield, so a wider spread means a lower price.

- A Treasury selloff raises the risk-free base, so corporate yields rise even if credit quality has not changed.
- Heavy corporate issuance (reason 4) can widen spreads, because issuers must entice buyers away from Treasuries.
- Higher rates can also strain borrowers that must refinance, a second-round credit effect.
- Treasuries differ: fiscal worries (reason 5) show up mainly as term premium rather than default risk.

## 7. Tie-In to Chapter 15: The Term Structure of Interest Rates

### The curve on Sept 30, 2026

| Maturity | 1-year | 2-year | 5-year | 10-year | 30-year |
|----------|--------|--------|--------|---------|---------|
| Yield | 4.55% | 4.90% | 5.10% | 5.29% | 5.63% |

*Source: streetstats.finance, as of Sept 30, 2026. The curve slopes upward, and the September selloff lifted all maturities with the long end moving most. On Oct 1 the 10-year touched 5.31%, the highest since 2007 (Reuters).*

### From par yields to spot rates

The quoted Treasury yields are par yields, which are flat-rate yields to maturity on coupon bonds. Forward rates must be built from spot rates, so the curve is bootstrapped: each maturity's spot rate is the rate that, together with the earlier spot rates, prices that par bond at 100. Because the curve slopes upward, spot rates sit above par yields, and the gap widens at longer maturities.

| Maturity | 1-year | 2-year | 5-year | 10-year | 30-year |
|----------|--------|--------|--------|---------|---------|
| Par yield | 4.55% | 4.90% | 5.10% | 5.29% | 5.63% |
| Spot rate | 4.55% | 4.91% | 5.12% | 5.33% | 5.88% |

*Spot rates are bootstrapped using annual-coupon par bonds. Par yields for maturities between the quoted points were interpolated linearly, so spot rates beyond 2 years are approximations.*

### How bootstrapping works

A par yield is a blend, because a coupon bond pays cash at several dates. A spot rate is the yield on a single cash flow at one date. Bootstrapping finds spot rates one maturity at a time, using the earlier answers to solve for the next one:

1. **1-year:** a single payment, so the par yield is the spot rate: s₁ = 4.55%.
2. **2-year:** the bond pays 4.90 after year 1 and 104.90 after year 2, and it prices at 100. Discount the first payment at s₁, then solve for s₂:

$$
100 = \frac{4.90}{1.0455} + \frac{104.90}{(1+s_2)^2} \Rightarrow s_2 \approx 4.91\%
$$

3. **3-year and beyond:** repeat, using the earlier spot rates to discount the early payments and solving for the next unknown.

At two years the gap is small (4.90% par vs. 4.91% spot), but it widens at longer maturities, so forwards computed directly from par yields are slightly off.

### Implied forward rates

The general form: locking in an n-year deposit must earn the same as an (n-1)-year deposit rolled into a one-year deposit.

$$
(1+y_n)^n = (1+y_{n-1})^{n-1}(1+f_n)
$$

$$
f_n = \frac{(1+y_n)^n}{(1+y_{n-1})^{n-1}} - 1
$$

Here yₙ is the n-year spot rate, fₙ is the one-year forward rate for year n, and n is the number of years. For a forward covering years a to b:

$$
f_{a,b} = \left(\frac{(1+y_b)^b}{(1+y_a)^a}\right)^{1/(b-a)} - 1
$$

The forward rate is the rate that makes you indifferent between a long deposit and rolling shorter ones, and it is computed from spot rates. For year two: the 2-year spot rate is 4.91%, so the forward is:

$$
f_{1,2} = \frac{(1.0491)^2}{1.0455} - 1 \approx 5.27\%
$$

Rough figures, using annual compounding:

| Forward period | Implied rate | Reading |
|----------------|--------------|---------|
| Year 2 (1y1y) | ≈ 5.27% | Market expects 1-year rates to rise from 4.55% |
| Years 6–10 (5y5y) | ≈ 5.55% | Long-run rates priced above today's 5-year yield |
| Years 11–30 (10y20y) | ≈ 6.15% | Highest forward rate on the curve |

### Which theory explains which driver?

| Theory | Core claim | Drivers that fit |
|--------|------------|------------------|
| Expectations hypothesis | Forward rates equal expected future short rates | Reasons 1, 2, 3, 8: expected inflation and the short-rate path (E, R) |
| Liquidity preference | Forward rates equal expected short rates plus a term premium | Reasons 4, 5, 6, 8, 10: supply and uncertainty raise the premium (S) |
| Market segmentation / preferred habitat | Maturity-specific demand and supply set yields | Reasons 3, 7, 9: mortgage hedging, carry-trade unwinds, and a shifting buyer base (F) |

### Reading the slope

An upward slope can reflect higher expected short rates, a higher term premium, or both, and the curve alone cannot separate them. Inverted curves have historically signaled recession; this curve's upward slope is consistent with reasons 1 and 3, where growth is still strong. Comparing nominal and TIPS yields gives breakeven inflation, and the gap between expected and demanded inflation compensation is part of the premium.

## 8. Worked Examples

### Example A: Price of a deposit when rates move

The price of a bond when its yield to maturity is known, with m coupon periods per annum, is the present value of the coupons plus the present value of the face value, all discounted at the periodic yield y/m:

$$
P_0 = \frac{C}{m} \cdot \frac{1-\left(1+\frac{y}{m}\right)^{-mT}}{\frac{y}{m}} + \frac{F}{\left(1+\frac{y}{m}\right)^{mT}}
$$

Where:

- P₀ = current (clean) price per 100 of face value
- C = annual coupon payment (C = c × F, with c the annual coupon rate)
- F = face (par) value
- m = coupon periods per annum (2 = semiannual, 1 = annual)
- T = years to maturity, so mT is the total number of periods
- y = annual yield to maturity (bond-equivalent when m = 2)
- y/m = periodic yield, the discount rate per coupon period

A 10-year Treasury has a 4.625% semiannual coupon. Its yield is now 5.26%, so the price is about 95.11, and a buyer who paid par is down about 4.9% on paper with no loss if held to maturity. Using n = 20, coupon = 2.3125, and y/m = 2.63% per half-year:

$$
P = 2.3125 \times \frac{1 - 1.0263^{-20}}{0.0263} + 100 \times 1.0263^{-20} \approx 35.61 + 59.50 \approx 95.11
$$

### Example B: Real return from holding to maturity

Buy at a 5.29% yield. If inflation averages 3.0%, the real return is about 2.2%. If inflation averages 5.5%, it is about −0.2%: no default and no price loss, yet purchasing power is lost.

$$
r = \frac{1 + R}{1 + i} - 1 = \frac{1.0529}{1 + i} - 1
$$

Here R is the nominal yield (0.0529), r is the real return, and i is the average annual inflation rate, following BKM Section 5.2.

**Note on notation:** BKM uses i for the inflation rate. Many economics and finance texts instead write inflation as the Greek letter π (pi), as in the Fisher equation (1 + R) = (1 + r)(1 + π). That is a symbol for inflation, not the constant 3.14159. Both notations mean the same thing.

## 9. Review Questions

| # | Type | Question |
|---|------|----------|
| 1 | Conceptual | Which of the ten reasons would a TIPS buyer worry about most, and which least? Explain using the distinction between inflation expectations and real rates. |
| 2 | Conceptual | Why does reason 7 (the Japan effect) fit none of the E, R, or S buckets? Describe the mechanism that makes it a forced-selling story. |
| 3 | Conceptual | If the Iran war ended tomorrow, which of the ten reasons would likely fade and which would persist? Justify each. |
| 4 | Conceptual | Treasuries carry almost no default risk, yet corporate bonds trade at a spread over them. Explain how credit risk affects a bond's price and yield. Then explain what happens to a corporate bond's total yield and spread when Treasury yields spike and companies issue record debt (reason 4). |
| 5 | Algorithmic | The Sept 30 yields are par yields (1-year 4.55%, 2-year 4.90%, annual coupons). (a) Bootstrap the 2-year spot rate, treating the 1-year yield as the 1-year spot rate. (b) Compute the implied one-year forward rate for year two. (c) What does it say about market expectations? Hint: bootstrap as shown in Section 7. |
| 6 | Conceptual | Which of the ten reasons would raise the term premium without changing expected short rates? Which would do the reverse? |
| 7 | Conceptual | If a recession shock hit, what would you expect to happen to the slope of the curve? Explain using all three theories. |
| 8 | Algorithmic | A 10-year note with a 4.625% semiannual coupon yields 5.26%. (a) Compute its price. (b) If an investor buys at a 5.29% yield and inflation averages 4%, compute the approximate real return. (c) Explain why holding to maturity does not eliminate the loss in (b), if any. |

### CFA exam style multiple choice

**9.** An investor buys a 10-year Treasury at a 5.29% yield and holds it to maturity. Which risk best describes the exposure that remains?

- A. Price risk, because the bond must be marked to market at maturity.
- B. Inflation risk, because the real value of fixed payments can fall short of expectations.
- C. Credit risk equal to that of a BBB corporate bond.

**10.** Under the pure expectations hypothesis, an upward-sloping yield curve implies that:

- A. Investors expect short-term rates to rise.
- B. Investors require a positive liquidity premium.
- C. Markets for different maturities are segmented.

**11.** Carry-trade unwinding by yen borrowers selling global government bonds is best explained by:

- A. The expectations hypothesis.
- B. A change in the term premium caused by deficits.
- C. Forced selling tied to market structure and maturity-specific demand.

## 10. Answer Key Outline

| Q | Key points |
|---|------------|
| 1 | TIPS compensate for the inflation channel (reasons 1, 2, 8) but not for rising real yields. Least worried about 2 and 8 as inflation drivers; most worried about 4, 5, 6, 10 (supply and term premium) and 3 (short-rate path), because real yields can still rise and cut TIPS prices. |
| 2 | Neither expectations of inflation or short rates nor aggregate supply changed; sales are driven by yen defense and the deleveraging of leveraged carry positions. F bucket. |
| 3 | Likely to fade: 2 (oil), part of 1 and 3 (inflation and hike pressure), and some of 6. Likely to persist: 4, 5, 9, 10 (structural supply and buyer-base changes) and much of 8. |
| 4 | Yield = risk-free + credit spread + liquidity premium; price is the PV of cash flows at that yield. Treasury spike lifts corporate yields via the base; record issuance can widen spreads; refinancing strain adds a second-round effect. Treasury fiscal worries show up as term premium. |
| 5 | (a) 100 = 4.90 ÷ 1.0455 + 104.90 ÷ (1 + s₂)², so (1 + s₂)² ≈ 1.1006 and s₂ ≈ 4.91%. (b) Forward = 1.1006 ÷ 1.0455 − 1 ≈ 5.27%. Using the par yield as if it were spot (1.049² ÷ 1.0455 − 1 ≈ 5.25%) understates the forward. (c) The forward exceeds the 4.55% one-year rate, so markets expect higher short rates or demand a premium. |
| 6 | Premium without expectations change: 4, 5, 6, 10, and the uncertainty part of 8. Expectations without premium change: 1, 2, and 3. |
| 7 | Expectations: expected cuts flatten or invert the curve. Liquidity preference: premium cushions the long end, so the slope flattens less. Segmentation: flight-to-quality demand for long Treasuries pushes long yields down. |
| 8 | (a) ≈ 95.11. (b) 1.0529 ÷ 1.04 − 1 ≈ 1.2%. (c) Principal is repaid in nominal dollars, and the real return depends on realized inflation; opportunity cost also applies if rates rise. |
| 9–11 | 9: B. 10: A. 11: C. |

## 11. Sources and Data Notes

- Carson, Kondo, and Gledhill, "10 Reasons Investors Are Driving Government Bond Yields Higher," Bloomberg, Oct 1, 2026 (subscription).
- Reuters, "Bonds teeter after US Treasuries' worst quarter since 1994," Oct 1, 2026: 10-year touched 5.31%, 30-year topped 5.65%; the 10-year rose about 87 bp in the September quarter.
- Treasury yield curve as of Sept 30, 2026: streetstats.finance. Treasury note price and yield as of Sept 29, 2026: F/m Investments.
- Yields were moving as this guide was prepared; confirm against a live source before using exact levels in class.
- Spot rates are bootstrapped from par yields with annual compounding; yields between the quoted maturities were interpolated linearly, so forwards beyond year 2 are approximations. Textbook conventions may differ slightly.
