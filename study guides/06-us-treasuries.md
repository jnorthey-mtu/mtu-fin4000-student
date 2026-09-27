# Study Guide 6: U.S. Treasuries

*Fixed Income Study Guides*

[← All study guides](README.md)

U.S. Treasury securities are the debt the federal government sells to fund itself. They are the world's benchmark risk-free asset, the collateral behind most repo lending, and the base of the curves used to price almost every other fixed income instrument. Outstanding marketable Treasuries passed \$31 trillion in June 2026.

## 1. The securities

| Type | Terms | Interest | How often auctioned | Strippable? |
| --- | --- | --- | --- | --- |
| Bills | 4, 6, 8, 13, 17, 26 and 52 weeks | None; sold at a discount, paid face value at maturity | Weekly; 52-week every four weeks | No |
| Cash management bills (CMBs) | Variable | Discount | As needed; banks and brokers only, not TreasuryDirect | No |
| Notes | 2, 3, 5, 7 and 10 years | Fixed coupon, semiannual | Monthly (new issues and reopenings) | Yes |
| Bonds | 20 and 30 years | Fixed coupon, semiannual | Monthly (new issues and reopenings) | Yes |
| TIPS | 5, 10 and 30 years | Fixed real coupon on CPI-adjusted principal | Several times a year per term | Yes |
| Floating rate notes (FRNs) | 2 years | Quarterly, indexed to the 13-week bill rate plus a spread | Monthly | No |

Common features:

- Minimum purchase \$100, in \$100 increments. All issued in electronic book-entry form only.
- Interest is taxed federally but exempt from state and local income tax.
- Non-callable (no current issues have call features), so there is no call risk.
- STRIPS are covered in Study Guide 1, TIPS in Study Guide 4.

## 2. Pricing Treasury bills

Bills are quoted on a **bank discount** basis: the discount as a percentage of face value, on a 360-day year.

```math
P = 100\left(1 - d \times \frac{t}{360}\right)
```

The discount rate understates the true return, because it divides by face value instead of price and uses 360 days. Treasury also publishes the **investment rate** (coupon-equivalent or bond-equivalent yield), for bills of six months or less:

```math
i = \frac{100 - P}{P} \times \frac{365}{t}
```

The **money market yield** uses price but a 360-day year, so it lines up with other money market rates:

```math
y_{MM} = \frac{100 - P}{P} \times \frac{360}{t}
```

Worked example: 26-week bill, 182 days, discount rate 4.00%.

| Measure | Calculation | Result |
| --- | --- | --- |
| Price per 100 | 100 × (1 − 0.04 × 182/360) | 97.9778 |
| Investment rate (BEY) | (2.0222 ÷ 97.9778) × 365/182 | 4.139% |
| Money market yield | (2.0222 ÷ 97.9778) × 360/182 | 4.083% |

For bills longer than six months Treasury uses a more involved investment-rate formula, because a coupon security of that term would pay a coupon before maturity.

## 3. Pricing notes and bonds

**Quoting in 32nds.** Coupon Treasuries trade in 32nds of a point, often split to 64ths or 256ths.

| Quote | Meaning | Decimal |
| --- | --- | --- |
| 98-16 | 98 and 16/32 | 98.500000 |
| 98-16+ | 98 and 16.5/32 (the + is 1/64) | 98.515625 |
| 98-162 | 98 and 16.25/32 (third digit in eighths of a 32nd) | 98.507813 |

**Clean price, accrued interest and dirty price.** Quotes are clean prices. The buyer also pays the seller the coupon interest earned since the last coupon date, counted Actual/Actual:

```math
AI = \frac{C}{2} \times \frac{\text{days since last coupon}}{\text{days in coupon period}} \qquad P_{dirty} = P_{clean} + AI
```

The dirty (invoice) price discounts every remaining cash flow, with a fractional first period $`w`$ = days to next coupon ÷ days in period:

```math
P_{dirty} = \sum_{k=1}^{n} \frac{CF_k}{\left(1 + \frac{y}{2}\right)^{k-1+w}}
```

Worked example: 4.25% note maturing May 15, 2036, yield 4.20%, settling Sep 30, 2026.

- Coupon period May 15 to Nov 15, 2026 has 184 days; 138 have passed, so $`w = 46/184 = 0.25`$.
- Accrued interest $`= 2.125 \times 138/184 = 1.5938`$.
- Dirty price = **101.9821**; clean price = **100.3884**, quoted about **100-12+**.
- On \$1 million face the buyer pays \$1,019,821.30.

Settlement for Treasuries is normally T+1.

## 4. Pricing tools

**TI BA II Plus Professional**

- Bill price: 100 `×` `(` 1 `−` .04 `×` 182 `÷` 360 `)` `=` → 97.9778. The Date worksheet (`2nd` `DATE`) counts days between dates.
- Note: `2nd` `BOND`; SDT = 9.3026, CPN = 4.25, RDT = 5.1536, RV = 100, ACT, 2/Y, YLD = 4.2, PRI `CPT` → **100.388**; ↓ AI → **1.594**.

**HP 12C**

- Bill price: 1 `ENTER` .04 `ENTER` 182 `×` 360 `÷` `−` 100 `×` → 97.9778. `g` `ΔDYS` counts days.
- Note: 4.2 `i` · 4.25 `PMT` · 9.302026 `ENTER` 5.152036 `f` `PRICE` → **100.388**; `x≷y` → **1.594**.

**Excel**

| Task | Formula | Result |
| --- | --- | --- |
| Bill price | `=TBILLPRICE(DATE(2026,10,1),DATE(2027,4,1),4%)` | 97.9778 |
| Bill bond-equivalent yield | `=TBILLEQ(DATE(2026,10,1),DATE(2027,4,1),4%)` | 4.139% |
| Bill yield from price | `=TBILLYIELD(DATE(2026,10,1),DATE(2027,4,1),97.9778)` | 4.083% |
| Note clean price | `=PRICE(DATE(2026,9,30),DATE(2036,5,15),4.25%,4.2%,100,2,1)` | 100.388 |
| Accrued interest | `=4.25/2*COUPDAYBS(DATE(2026,9,30),DATE(2036,5,15),2,1)/COUPDAYS(DATE(2026,9,30),DATE(2036,5,15),2,1)` | 1.594 |
| 32nds to decimal | `=DOLLARDE(98.165,32)` | 98.515625 |

`DOLLARDE` reads 98.165 as 98 and 16.5/32; `DOLLARFR` converts back.

**Python (QuantLib; tested, output 100.3884, 1.5938, 101.9821)**

```python
import QuantLib as ql
settle = ql.Date(30, ql.September, 2026)
ql.Settings.instance().evaluationDate = settle
sched = ql.Schedule(ql.Date(15, ql.May, 2026), ql.Date(15, ql.May, 2036), ql.Period(ql.Semiannual),
                    ql.NullCalendar(), ql.Unadjusted, ql.Unadjusted,
                    ql.DateGeneration.Backward, False)
dc = ql.ActualActual(ql.ActualActual.Bond, sched)
note = ql.FixedRateBond(0, 100.0, sched, [0.0425], dc, ql.Unadjusted, 100.0, ql.Date(15, ql.May, 2026))
ytm = ql.InterestRate(0.042, dc, ql.Compounded, ql.Semiannual)
clean = ql.BondFunctions.cleanPrice(note, ytm)
ai = note.accruedAmount()
dirty = clean + ai
```

**Julia:** the plain-Julia pricing loop from Study Guide 4 applies, with the exponent changed to `k - 1 + w`.

## 5. The primary market: Treasury auctions

Every marketable Treasury is first sold at a public auction run by the Bureau of the Fiscal Service. Treasury's Office of Debt Management decides what to issue, advised by the Treasury Borrowing Advisory Committee (TBAC), and announces coupon issuance plans at the **quarterly refunding** (early February, May, August and November).

**The four steps**

1. **Announcement:** security, offering amount, auction date, issue date and bidding deadlines, usually a few days to a week ahead.
2. **When-issued trading:** from announcement until issue, dealers trade the security forward. The when-issued yield is the market's estimate of the auction result.
3. **Auction:** bids close at set times (for notes and bonds, noncompetitive usually noon ET and competitive 1:00 p.m. ET). Results are released within minutes.
4. **Issue:** securities are delivered and paid for, typically a few days after the auction.

**Two kinds of bids**

| | Noncompetitive | Competitive |
| --- | --- | --- |
| Who | Individuals and smaller institutions | Dealers, banks, funds, foreign official accounts |
| What you specify | Amount only | Amount and the yield (or discount rate) you will accept |
| Size limit | \$100 to \$10 million per auction | 35% of the offering amount per bidder |
| Guarantee | Filled in full at the auction yield | Filled only if your yield is at or below the stop-out |
| Channel | TreasuryDirect, or a bank or broker | Through TAAPS directly or via a dealer; not allowed in TreasuryDirect |

**How the price is set: single-price auction**

1. Treasury accepts all noncompetitive bids first.
2. Competitive bids are ranked from lowest yield up and accepted until the offering is filled.
3. The last accepted yield is the **stop-out** (high) yield. Every winning bidder, competitive and noncompetitive, gets that same yield and price.
4. Bids exactly at the stop-out are prorated.

Treasury has used this uniform-price format for all auctions since November 1998. It encourages bidders to bid their true value, because no one pays more than the market-clearing price.

**Reading auction results**

| Statistic | Meaning | What analysts watch |
| --- | --- | --- |
| High yield | The stop-out yield; sets the coupon for new issues | Compared with the when-issued yield at 1:00 p.m. |
| Tail or stop-through | High yield minus the when-issued yield | Positive (a tail) signals weak demand; negative (stop-through) signals strong demand |
| Bid-to-cover ratio | Total bids ÷ amount accepted | Higher means more demand |
| Indirect bidders | Bids through dealers for others, including foreign central banks | Proxy for foreign and investor demand |
| Direct bidders | Non-dealer institutions bidding for their own account | Domestic institutional demand |
| Primary dealer takedown | Share left to primary dealers | High takedown means dealers absorbed weak demand |

**Primary dealers.** The New York Fed's trading counterparties, currently 26 firms after MUFG joined in January 2026. They must bid in every auction at reasonably competitive prices, make markets for the Fed's official accountholders, and participate in open market operations. Their obligation to bid is what guarantees each auction is fully covered.

**Reopenings.** Many issues are sold again in later auctions with the same CUSIP, coupon and maturity (for example, a 10-year note issued in February is reopened in March and April). Reopenings build issue size and liquidity.

**Buybacks.** Since May 2024 Treasury has run regular buybacks: **liquidity support** buybacks give holders a predictable place to sell off-the-run securities, and **cash management** buybacks smooth Treasury's cash balance and bill issuance. They are reverse auctions open to primary dealers and are not meant to respond to acute market stress.

## 6. The secondary market

After issue, Treasuries trade over the counter, not on an exchange. Trading is heaviest in on-the-run issues and very light for most off-the-run bonds.

| Segment | Who trades | How |
| --- | --- | --- |
| Interdealer (dealer-to-dealer) | Primary dealers and principal trading firms (PTFs) | Electronic central limit order books such as BrokerTec, Nasdaq Fixed Income and Fenics UST; voice brokers for off-the-runs |
| Dealer-to-client | Asset managers, banks, insurers, hedge funds, corporates | Request-for-quote platforms such as Tradeweb and Bloomberg, plus direct voice trading |
| Retail | Individuals | Brokerage accounts, which trade with dealers on the investor's behalf |
| Repo | Dealers, money funds, hedge funds, the Fed | Treasuries lent against cash overnight or for a term; the financing that supports most trading |
| Futures | All of the above | CME Treasury futures; used for hedging and cash-futures basis trades |

**Settlement and plumbing**

- Standard settlement is T+1 over the Fed's Fedwire Securities Service.
- The Fixed Income Clearing Corporation (FICC) is the central counterparty for dealer trades and much of repo.
- **Central clearing mandate:** SEC rules adopted in December 2023 require direct participants of covered clearing agencies to centrally clear eligible cash Treasury trades by **December 31, 2026** and eligible repo by **June 30, 2027**.

**Transparency**

- Since 2017, dealers report Treasury trades to FINRA's TRACE system.
- Since March 25, 2024, FINRA publishes end-of-day, trade-by-trade data for on-the-run nominal notes and bonds, with size caps (for example \$150 million for 7- and 10-year notes). The data is free on FINRA's website for personal use on a next-day basis.

**Liquidity episodes to know:** the 1998 LTCM crisis (on-the-run premium spike), the October 2014 flash rally, the September 2019 repo spike and the March 2020 "dash for cash," when even Treasuries became hard to sell. These drove the clearing mandate, TRACE transparency and the buyback program.

## 7. On-the-run and off-the-run Treasuries

- **On-the-run:** the most recently auctioned security of each maturity (the current 2-, 3-, 5-, 7-, 10-, 20- and 30-year). It stays on-the-run until the next new issue of that term is auctioned.
- **Off-the-run:** every earlier issue. The one just replaced is the "old" (first off-the-run), the one before that the "double old," and so on.
- An old 30-year bond with 10 years left and the current 10-year note have almost the same cash flow timing, but the 10-year note is on-the-run and the old bond is not.

**Why on-the-runs trade differently**

| Feature | On-the-run | Off-the-run |
| --- | --- | --- |
| Trading volume | Very high; the bulk of interdealer volume | Low; many issues rarely trade |
| Bid-ask spread | Tightest in the world's bond markets | Wider |
| Yield | Slightly lower (higher price): a liquidity premium | Slightly higher, typically a few basis points, more in stress |
| Repo | Often "special": borrowing it in repo costs extra, so its repo rate falls below general collateral | Usually trades at the general collateral rate |
| Use | Benchmarks for quoting spreads, hedging, futures pricing and the Treasury par curve | Fitted-curve analysis, relative value trades, buy-and-hold portfolios |

**Life cycle:** when-issued trading → auction → on-the-run (heavy trading, repo specialness) → next auction makes it the old issue → liquidity and premium fade → it settles into the off-the-run pool, where much of it is held to maturity.

**On-the-run/off-the-run trade.** Buy the cheaper off-the-run, short the richer on-the-run, and wait for the spread to converge as the on-the-run ages. It usually works, but the spread can widen sharply in a flight to liquidity. That is how LTCM lost heavily in 1998.

**Practical implications**

- **Curve building:** bootstrapping from on-the-runs mixes a liquidity premium into the spot curve; many analysts use off-the-runs or a fitted curve instead (Study Guide 2).
- **Buy-and-hold investors:** an off-the-run of similar maturity often yields a little more. If you will hold to maturity, you give up liquidity you will not use.
- **Transparency:** FINRA's public trade-by-trade TRACE data currently covers on-the-run nominal notes and bonds only.
- **Policy:** Treasury's liquidity support buybacks target off-the-runs, and measures of off-the-run pricing dispersion have improved since they began.

## 8. Buying Treasuries directly

Individuals have three routes: TreasuryDirect, a brokerage account or bank, and funds.

| | TreasuryDirect | Brokerage account |
| --- | --- | --- |
| New issues at auction | Yes, noncompetitive only | Yes, usually noncompetitive through the broker |
| Existing issues (secondary market) | No | Yes, at the dealer's offer price |
| Selling before maturity | Not in TreasuryDirect; transfer to a broker first | Any day, T+1 settlement |
| Hold in an IRA | No | Yes |
| Automatic reinvestment | Yes for bills; check TreasuryDirect's current rules for other terms | Varies by broker; some offer auto-roll |
| Cash management bills | No | Yes |
| Savings bonds (I and EE) | Only here, electronically | No |
| Costs | None | Usually none for auction purchases at major brokers; dealer spread on secondary trades |

**Using TreasuryDirect**

1. Open an account at treasurydirect.gov (needs a Social Security number, a U.S. address and a bank account).
2. Choose BuyDirect, the security and term, the amount (\$100 minimum, \$100 steps) and whether to reinvest at maturity.
3. Your bank account is debited on the issue date. You receive the auction yield like every other noncompetitive bidder.
4. Coupons and maturity proceeds go to your bank account. TreasuryDirect issues 1099 tax forms.

**TreasuryDirect limits to know**

- Securities bought in TreasuryDirect must be held **45 days** before they can be transferred out, so a 4-week bill bought there can never be transferred.
- Selling requires moving the security to a bank or broker with a transfer request (FS Form 5511) signed before a certifying official at a bank or credit union; a notary is not accepted. Transfers can take a long time to process.
- Rule of thumb: TreasuryDirect suits bills and savings bonds held to maturity. Buy notes, bonds and TIPS you might sell, or want in an IRA, through a broker.

**Funds** (Treasury mutual funds and ETFs) offer daily liquidity and diversification but no maturity date: their price moves with rates indefinitely, and they charge a fee.

## 9. Treasury ladders

A ladder spreads money evenly across a series of maturities. As each rung matures, the cash is either spent or reinvested at the long end, so the ladder keeps its shape.

**Why build one**

- **Predictable cash flow:** principal comes back on known dates, useful for tuition, retirement spending or planned expenses.
- **Rate diversification:** you never commit everything at one rate. If rates rise, maturing rungs reinvest higher; if rates fall, the longer rungs keep the old rates.
- **Liquidity without selling:** something always matures soon, so you rarely need to sell before maturity.
- **Simplicity and credit safety:** no credit risk, no call risk and no state income tax on the interest.

**Worked example: \$100,000, five annual rungs.** Yields are illustrative.

| Rung | Maturity | Amount | Yield (illustrative) | Annual interest |
| --- | --- | --- | --- | --- |
| 1 | 1 year | \$20,000 | 3.90% | \$780 |
| 2 | 2 years | \$20,000 | 3.80% | \$760 |
| 3 | 3 years | \$20,000 | 3.85% | \$770 |
| 4 | 4 years | \$20,000 | 3.95% | \$790 |
| 5 | 5 years | \$20,000 | 4.05% | \$810 |
| **Total** | | **\$100,000** | **3.91% average** | **\$3,910** |

- Each year the maturing \$20,000 buys a new 5-year note, so after year one the ladder always runs 1 to 5 years.
- Average maturity is 3 years at the start and stays there. Once fully rolled, the whole ladder earns 5-year rates while one-fifth of it comes due every year.

```math
\bar{T} = \sum_{i} w_i \, T_i = \frac{1 + 2 + 3 + 4 + 5}{5} = 3 \text{ years}
```

**Variations**

| Ladder | How | Suits |
| --- | --- | --- |
| Bill ladder | Buy a 13-week bill each week (13 rungs) and auto-reinvest | Cash reserves needing weekly access; easy in TreasuryDirect |
| Note ladder | Annual rungs over 5 or 10 years, as above | Balancing yield and access |
| TIPS ladder | Rungs sized to cover each year's real spending, principal plus interest | Inflation-protected retirement income; cash-flow matching (Study Guide 5) |

**Ladder, bullet or barbell**

| Structure | Shape | Trade-off |
| --- | --- | --- |
| Ladder | Equal amounts at every maturity | Steady reinvestment and cash flow; average curve exposure |
| Bullet | Concentrated near one maturity | Matches one known liability date |
| Barbell | Short and long ends, little in the middle | Same duration as a ladder but more convexity; bets on curve shape |

**Cautions:** a ladder does not remove interest rate risk, it spreads it. Selling a rung early can mean a loss. Nominal ladders fix dollars, not purchasing power (use TIPS for real needs). Keep ladders of notes and TIPS in a brokerage account if you might sell or want IRA tax treatment.

## 10. Web resources

**Buying, auctions and security details (TreasuryDirect)**

- [How Treasury auctions work](https://treasurydirect.gov/auctions/how-auctions-work/): the four steps, bid types and limits.
- [Auction rules and process FAQs](https://www.treasurydirect.gov/help-center/additional-auction-related-faqs/): stop-out yield, proration, TAAPS vs TreasuryDirect.
- [Treasury bills at a glance](https://www.treasurydirect.gov/marketable-securities/treasury-bills): terms, minimums, auction frequency, taxes.
- [Treasury bill FAQs](https://www.treasurydirect.gov/research-center/history-of-marketable-securities/bills/t-bills-faqs): auction days, pricing and rounding.
- [Transferring securities out of TreasuryDirect](https://treasurydirect.gov/indiv/help/treasurydirect-help/user-guide/261-270/): the 45-day hold and FS Form 5511.
- [Auction rules summary (PDF)](https://www.treasurydirect.gov/files/laws-and-regulations/auction-regulations-uoc/treasury-auction-rules.pdf): bid limits, award limits, proration math.

**Market structure and policy**

- [New York Fed: primary dealers](https://newyorkfed.org/markets/primarydealers): current list and obligations.
- [Treasury buyback program details (PDF)](https://home.treasury.gov/system/files/221/TreasurySupplementalQ22024.pdf): liquidity support vs cash management buybacks.
- [FINRA: Treasury trade dissemination (Regulatory Notice 24-06)](https://FINRA.org/rules-guidance/notices/24-06): end-of-day on-the-run trade data.
- [FINRA TRACE reporting and dissemination timeframes](https://www.finra.org/filing-reporting/trade-reporting-and-compliance-engine-trace/trace-reporting-timeframes): size caps by maturity.
- [ICMA: SEC mandatory clearing for U.S. Treasuries](https://www.icmagroup.org/market-practice-and-regulatory-policy/repo-and-collateral-markets/other-resources/sec-mandatory-clearing-for-u-s-treasuries/): the clearing mandate and its dates.
- [TBAC charge on central clearing, 2026 (PDF)](https://home.treasury.gov/system/files/221/TBACCharge1Q22026.pdf): implementation status.

**Data**

- Daily Treasury par yield curve rates and auction results: U.S. Treasury Resource Center and TreasuryDirect auction query pages.
- FRED (Federal Reserve Bank of St. Louis): constant-maturity yield series such as DGS10.
- FINRA's Treasury Daily Aggregate Statistics and end-of-day trade files.

## 11. Practice set

1. A 13-week (91-day) bill auctions at a 4.20% discount rate. Price and investment rate? *98.9383; 4.304%.*
2. Convert 99-24+ to decimal. *99 + 24.5/32 = 99.765625.*
3. A 3.875% note settles 60 days into a 181-day coupon period. Accrued interest per 100? *1.9375 × 60/181 = 0.6423.*
4. The when-issued yield at 1:00 p.m. was 4.300%; the auction's high yield is 4.325%. What happened? *A 2.5 bp tail: demand was weaker than the market expected.*
5. You bid noncompetitively for \$50,000 of a 10-year note. What yield do you get? *The stop-out (high) yield, the same as every winning bidder.*
6. Why does the old 10-year note usually yield a little more than the new one? *It is less liquid and not special in repo, so investors demand a small premium.*
7. Why buy a 10-year note through a broker rather than TreasuryDirect if you might need to sell? *TreasuryDirect cannot sell; you must first transfer the note, after a 45-day hold and a paper form.*
8. A ladder holds \$30,000 each in 2-, 4- and 6-year notes. Average maturity? *(2 + 4 + 6) ÷ 3 = 4 years.*
9. Why is a Treasury ladder attractive to a state taxpayer compared with a CD ladder at the same yield? *Treasury interest is exempt from state and local income tax.*

## 12. CFA-style review questions

Original questions in the CFA Level I format (three choices, one correct). Not CFA Institute material.

1. A 91-day Treasury bill is quoted at a 5.00% discount rate. Its price per 100 is closest to:
   - A. 98.736
   - B. 98.753
   - C. 95.000
2. Compared with a Treasury bill's bank discount yield, its bond-equivalent yield is:
   - A. higher
   - B. lower
   - C. the same
3. In a Treasury auction, a noncompetitive bidder receives:
   - A. the yield it specified in its bid
   - B. the stop-out (highest accepted) yield
   - C. the average of all accepted competitive yields
4. Compared with the first off-the-run issue of similar maturity, an on-the-run Treasury note typically has:
   - A. a lower yield and a narrower bid-ask spread
   - B. a higher yield and a narrower bid-ask spread
   - C. a higher yield and a wider bid-ask spread
5. A Treasury note is quoted at 101-08. Its price per 100 is:
   - A. 101.08
   - B. 101.25
   - C. 101.80
6. The main purpose of a Treasury ladder is to:
   - A. maximize yield by concentrating in the longest maturity
   - B. spread reinvestment dates evenly over time
   - C. eliminate interest rate risk
7. When a Treasury note is bought between coupon dates, the buyer pays:
   - A. the quoted clean price only
   - B. the clean price plus accrued interest
   - C. the clean price minus accrued interest

**Answer key**

1. A. $`100 \times (1 - 0.05 \times 91/360) = 98.736`$. B wrongly uses a 365-day year.
2. A. BEY divides by price (below face) and uses 365 days.
3. B. Treasury uses a single-price auction.
4. A. The liquidity premium lowers its yield; heavy trading tightens its spread.
5. B. 101 + 8/32 = 101.25.
6. B. A ladder spreads maturities and reinvestment timing; it does not eliminate rate risk.
7. B. The buyer compensates the seller for interest earned since the last coupon.

## 13. Bloomberg Terminal exercises (draft: verify on the campus Terminal)

| Command | What to do | Check against this guide | Verified |
| --- | --- | --- | --- |
| `CT2 Govt`, `CT10 Govt`, `CT30 Govt` | Current (on-the-run) issues; `DES <GO>` shows the specific CUSIP, coupon and issue date | Section 7: on-the-run | ☐ |
| `FIT <GO>` | Treasury monitor: actives, off-the-runs, bills | Sections 1 and 7 | ☐ |
| `ALLQ <GO>` | Dealer quotes for one security; compare bid-ask spreads of the on-the-run and first off-the-run 10-year | Section 7: liquidity differences | ☐ |
| `GC <GO>` | Plot the actives curve against an off-the-run curve | Section 7: liquidity premium | ☐ |
| Auction results | Find the Terminal's Treasury auction results and calendar screen (search "Treasury auction" in the command line) | Section 5: high yield, bid-to-cover, bidder shares, tail | ☐ |
| `ECO <GO>` | Economic calendar: auction dates and the quarterly refunding announcement | Section 5 | ☐ |
| `BTMM <GO>` | U.S. money market monitor: bill yields, repo, SOFR | Sections 2 and 6 | ☐ |
| `YAS <GO>` on a bill and a note | Check discount rate, investment rate, accrued interest and 32nds quote | Sections 2 and 3 | ☐ |

**Exercises:**

1. Record yield and bid-ask for the on-the-run and first off-the-run 10-year. Compute the yield spread in basis points. Repeat after the next 10-year auction.
2. After a note auction, record high yield, bid-to-cover and indirect, direct and dealer shares. Compare the high yield with the 1:00 p.m. when-issued yield: tail or stop-through?
3. Build a five-rung ladder in Excel with `BDP` yields for real CUSIPs maturing one to five years out; compute the average yield and maturity.

## 14. Reading in Bodie, Kane & Marcus, *Investments*, 13th ed. (2024)

| Section | Topic in the book | Supports |
| --- | --- | --- |
| 2.1 The Money Market | Treasury Bills; Yields on Money Market Instruments | Bank discount yield, bond-equivalent yield (sections 1–2) |
| 2.2 The Bond Market | Treasury Notes and Bonds; Inflation-Protected Treasury Bonds | Security types (section 1) |
| 3.1 How Firms Issue Securities | Primary vs secondary markets | Framework for sections 5–6 (the book's focus is corporate issuance) |
| 3.2 How Securities Are Traded | Types of Markets: direct search, brokered, dealer and auction markets | Treasuries as an auction primary market and dealer secondary market |
| 14.1 Bond Characteristics | Treasury Bonds and Notes; Accrued Interest and Quoted Bond Prices | 32nds, clean vs dirty price (section 3) |
| 14.2 Bond Pricing | Bond Pricing between Coupon Dates | Dirty price with fractional periods |
| 14.3 Bond Yields | Yield to Maturity | Auction yields and quotes |
| 15.1 The Yield Curve | Bond Pricing | Why on-the-run vs off-the-run matters for curve building (section 7) |
| 16.3 Passive Bond Management | Cash Flow Matching and Dedication | Ladders as cash-flow matching (section 9) |

The book covers Treasury auctions, primary dealers, TreasuryDirect and on-the-run liquidity only briefly; the links above fill that gap.
