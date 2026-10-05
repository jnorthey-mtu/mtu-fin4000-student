# Mini Study Guide 11: Bond Issuance, Underwriting, and OID

*BKM Ch. 3, with Ch. 2 and 14*

[← All study guides](../../study-guide-index.md)

FIN 4000 Investments · Mini study guide · Oct 3, 2026 · Jim Northey

## Learning objectives and BKM map

Original issue discount (OID) is born in the **primary market**, when the coupon the issuer sets is below the yield the market demands on pricing day. After that, the bond trades in the **secondary market**, where any new discount is *market* discount, not OID.

After this guide you should be able to:

1. Distinguish the primary market (issuer sells, receives cash) from the secondary market (investors trade with each other or dealers; the issuer receives nothing).
2. Explain the underwriter's role: advising, pricing, distributing, and (in a firm commitment) bearing price risk.
3. Explain how a Treasury auction and a corporate bookbuilding both set the issue price, and why that price can sit below par.
4. Compute the OID on a new issue and test it against the de minimis threshold.
5. Separate OID from the underwriting spread and from market discount.
6. Describe how bonds trade after issuance (OTC dealer market, bid-ask spread, thin liquidity).

| BKM 13e section | What it covers | Link to this guide |
| --- | --- | --- |
| 3.1 How Firms Issue Securities | Primary vs. secondary markets, investment bankers/underwriters, firm commitment, prospectus, shelf registration (Rule 415), private placements (Rule 144A), IPOs | Where the issue price, and therefore OID, is set |
| 3.2 How Securities Are Traded | Types of markets: direct search, brokered, dealer, auction | Bonds trade mainly in dealer markets |
| 3.5 New Trading Strategies: Bond Trading | Bonds trade mostly OTC through dealers; thin, fragmented liquidity | The secondary market for bonds |
| 3.7 Trading Costs | Commissions and the bid-ask spread | The dealer's compensation after issuance |
| 3.10 Regulation of Securities Markets | Securities Act of 1933 (registration of new issues), Securities Exchange Act of 1934 (secondary trading) | 1933 Act = primary, 1934 Act = secondary |
| 2.1 The Money Market | T-bills sold at a discount at auction | Pure-discount instruments (short-term, outside OID accrual for most individuals) |
| 2.2 The Bond Market | Treasury notes/bonds, munis, corporates | The instruments being issued |
| 14.1 Bond Characteristics | Coupon, par, zero-coupon bonds, deep-discount bonds | Why a coupon below market yield means a price below par |
| 14.4 Bond Prices over Time | Zero-coupon bonds, STRIPS, after-tax returns: OID taxed as imputed interest | How OID accrues and is taxed |

Section numbers follow the 13e table of contents; check them against your copy before citing them on the exam review sheet.

## Core concept 1: Issuance (primary market)

The issuer chooses the coupon, and the market sets the price. If the coupon ends up below the yield investors require on pricing day, the bond sells below par, and the gap is OID.

```math
\text{OID} = \text{Stated redemption price at maturity} - \text{Issue price}
```

### Three ways bonds reach investors (BKM 3.1)

- **Public offering with an underwriter.** The issuer hires investment bankers, who form an *underwriting syndicate*. In a **firm commitment**, the syndicate buys the whole issue at an agreed price and resells it to the public at the *public offering price*. The difference is the **underwriting spread**, and the syndicate bears the risk of not selling at that price. In a **best-efforts** deal, the banker only agrees to try to sell, and the issuer keeps the risk.
- **Shelf registration (SEC Rule 415).** A large issuer registers securities with the SEC once, then sells them in tranches over up to two years whenever market conditions suit. Most investment-grade corporate bonds come to market this way, often priced and sold within hours.
- **Private placement (Rule 144A).** Bonds are sold directly to a small group of qualified institutional buyers, with no full SEC registration. Placements are cheaper and faster but less liquid afterward.

### How the issue price gets set

| Market | Who sets the coupon | Who sets the price | Why a discount appears |
| --- | --- | --- | --- |
| Treasury notes/bonds (BKM 2.2) | Treasury, *after* the auction | Single-price auction: everyone pays the high (stop-out) yield | The coupon is the high yield rounded **down** to the nearest 1/8 of 1%, so price is at or slightly below par |
| T-bills (BKM 2.1) | No coupon | Auction | Pure discount by design |
| Corporate bonds (BKM 3.1) | Issuer + underwriter, in round increments | Underwriter's **bookbuilding**: gathering investor orders at different yields | Final yield lands a few basis points above the chosen coupon, so the deal prices a little below par (e.g., 99.40) |
| Zero-coupon and deep-discount bonds (BKM 14.1) | Issuer sets a zero or low coupon on purpose | Market | Large, deliberate discount |

### Why underwriters matter for OID

- They advise on the coupon and price, so they decide where the issue lands relative to par.
- The **issue price for tax purposes is the first price at which a substantial amount is sold to the public**, not what the issuer nets. The underwriting spread is an issuance cost to the issuer, **not** OID.
- In a firm commitment, if rates rise between pricing and distribution, the *underwriter* absorbs the loss. The issue price, and the OID, are already fixed.

### De minimis rule

OID is treated as zero if it is less than 0.25% of the redemption price times the number of full years to maturity. For a \$1,000, 10-year bond, the threshold is 0.0025 × \$1,000 × 10 = **\$25** (2.5 points). Small discounts from coupon rounding or bookbuilding usually fall under it. Deep-discount and zero-coupon bonds never do.

## Core concept 2: Trading after issuance (secondary market)

Once the bonds are distributed, the issuer is out of the picture. Investors trade with each other through dealers, and the price moves with interest rates and credit quality.

### How bonds trade (BKM 3.2, 3.5, 3.7)

- **Dealer market.** Most bonds trade **over the counter**: dealers quote a *bid* (the price they pay) and an *ask* (the price they sell at) and hold inventory. The **bid-ask spread** is the dealer's compensation and the investor's main trading cost.
- **Thin, fragmented liquidity.** A single issuer may have dozens of bond issues outstanding, and many trade only a few times a month. Liquidity is concentrated right after issuance, then fades. Treasuries are the exception, with a deep and active dealer market.
- **Underwriters as dealers.** The banks that underwrite a deal usually *make a market* in it afterward, quoting prices to support trading. They are the bridge between the two markets.
- **Transparency.** Corporate and agency bond trades are reported to FINRA's TRACE system; muni trades go to the MSRB's EMMA site.
- **Regulation (BKM 3.10).** The Securities Act of 1933 governs new issues (registration, prospectus). The Securities Exchange Act of 1934 governs secondary trading and created the SEC.

### OID vs. market discount

OID is fixed at issuance and accrues on a schedule. A bond bought later below its **adjusted issue price** (issue price plus OID accrued so far) carries **market discount** on top of any OID.

|  | Original issue discount | Market discount |
| --- | --- | --- |
| Created in | Primary market, at issuance | Secondary market, after issuance |
| Usual cause | Coupon below market yield at pricing; zero or PIK structure | Rates rose or credit weakened after issuance |
| Measured from | Stated redemption price minus issue price | Adjusted issue price (or par, for a par bond) minus your purchase price |
| Tax timing | Accrued each year as interest (constant yield) | Ordinary income on sale or maturity, unless you elect to accrue it |
| De minimis test | 0.25% × redemption price × full years to maturity (from issue) | 0.25% × redemption price × full years remaining (from purchase) |

For a holder who buys at issue and keeps the bond, OID is all there is. Market discount arises only when a later buyer pays less than the bond's accreted value.

## Worked examples

All bonds have \$1,000 par and pay semiannual coupons; yields are bond-equivalent (BEY). Set the BA II Plus to P/Y = 1 and enter per-period rates.

**Calculator setup (do once):**

| Step | BA II Plus Professional keystrokes | Display |
| --- | --- | --- |
| Show 4 decimals | [2nd] [FORMAT] 4 [ENTER] [2nd] [QUIT] | 0.0000 |
| One payment per period | [2nd] [P/Y] 1 [ENTER] [2nd] [QUIT] | P/Y = 1.0000 |
| Clear TVM registers before each example | [2nd] [CLR TVM] | 0.0000 |

Sign convention: money you pay (the price) is negative, and money you receive (coupons, face value) is positive.

### Example 1: Treasury auction (BKM 2.2, 3.1)

A new 10-year Treasury note auction clears at a high yield of 4.237%. What are the coupon, the issue price and the OID?

**Formulas**

```math
\begin{aligned}
c &= \left\lfloor \frac{y^{*}}{0.125\%} \right\rfloor \times 0.125\% \\
P &= C \cdot \frac{1-(1+r)^{-n}}{r} + \frac{F}{(1+r)^{n}}, \quad C = \frac{c \cdot F}{2},\; r = \frac{y^{*}}{2},\; n = 2T \\
\text{OID} &= F - P \\
\text{DM} &= 0.0025 \times F \times N
\end{aligned}
```

| Symbol | Meaning | Example 1 value |
| --- | --- | --- |
| y* | High (stop-out) yield at which the auction clears, annual BEY | 4.237% |
| c | Annual coupon rate, y* rounded down to the nearest 1/8 of 1% | 4.125% |
| C | Coupon payment per six-month period (\$) | 20.625 |
| F | Face (par) value = stated redemption price at maturity (\$) | 1,000 |
| r | Yield per six-month period | 2.1185% |
| T | Years to maturity | 10 |
| n | Number of semiannual periods | 20 |
| P | Issue price (\$) | 990.95 |
| OID | Original issue discount (\$) | 9.05 |
| N | Full years to maturity, for the de minimis test | 10 |
| DM | De minimis threshold (\$); OID below DM is treated as zero | 25.00 |

1. Coupon = high yield rounded down to the nearest 1/8%: **4.125%** (semiannual payment \$20.625).
2. Price at the 4.237% clearing yield:
   - Keystrokes: 20 [N], 2.1185 [I/Y], 20.625 [PMT], 1000 [FV], [CPT] [PV] → **−990.95**
3. OID = 1,000 − 990.95 = **\$9.05** per bond.
4. De minimis threshold = 0.0025 × 1,000 × 10 = \$25. Since \$9.05 < \$25, OID is treated as **zero** for tax purposes.

The discount here comes from the auction mechanics, not a choice by Treasury.

**BA II Plus Professional: Example 1**

| Step | Keystrokes | Display |
| --- | --- | --- |
| Coupon rounding: y* in 1/8 steps | 4.237 [÷] 0.125 [=] | 33.8960 |
| Round down to 33 steps | 33 [×] 0.125 [=] | 4.1250 (c, %) |
| Coupon per period C | 4.125 [÷] 2 [×] 10 [=] | 20.6250 |
| Clear TVM | [2nd] [CLR TVM] | 0.0000 |
| Periods | 20 [N] | N = 20.0000 |
| Yield per period | 4.237 [÷] 2 [=] [I/Y] | I/Y = 2.1185 |
| Coupon | 20.625 [PMT] | PMT = 20.6250 |
| Face | 1000 [FV] | FV = 1,000.0000 |
| Price | [CPT] [PV] | PV = −990.9471 |
| OID | 1000 [−] 990.9471 [=] | 9.0529 |
| De minimis | 0.0025 [×] 1000 [×] 10 [=] | 25.0000 |

*Alternative, bond worksheet* (settlement on a coupon date, price per \$100): [2nd] [BOND]; SDT = 10.1526 [ENTER] [↓]; CPN = 4.125 [ENTER] [↓]; RDT = 10.1536 [ENTER] [↓]; RV = 100 [ENTER] [↓]; set ACT and 2/Y with [2nd] [SET] if needed [↓]; YLD = 4.237 [ENTER] [↓]; PRI [CPT] → **99.0947**.

### Example 2: Corporate deal with a firm-commitment underwriter (BKM 3.1)

An issuer sells \$500 million of 10-year, 5.25% bonds. The syndicate prices the deal to the public at 99.40 and takes an underwriting spread of 0.65 points.

**Formulas**

```math
\begin{aligned}
P_{net} &= POP - s \\
\text{Proceeds} &= \frac{P_{net}}{100} \times Q \\
\text{OID} &= F - \frac{POP}{100} \times F \\
\frac{POP}{100} \times F &= C \cdot \frac{1-(1+r)^{-n}}{r} + \frac{F}{(1+r)^{n}} \;\Rightarrow\; \text{solve for } r,\quad y = 2r
\end{aligned}
```

| Symbol | Meaning | Example 2 value |
| --- | --- | --- |
| POP | Public offering price, % of par (the issue price for OID) | 99.40 |
| s | Underwriting spread, points of par | 0.65 |
| P\_net | Price the issuer receives, % of par | 98.75 |
| Q | Total face amount of the issue (\$) | 500 million |
| Proceeds | Issuer's net cash from the deal (\$) | 493.75 million |
| F | Face value per bond (\$) | 1,000 |
| C | Coupon payment per six-month period (\$) | 26.25 |
| n | Number of semiannual periods | 20 |
| r | Yield per six-month period (solved) | 2.664% |
| y | Yield to maturity, annual BEY | 5.33% |

1. Issuer's net price = 99.40 − 0.65 = **98.75**, so proceeds = \$500M × 0.9875 = **\$493.75 million**.
2. Issue price for OID = public offering price = **99.40**, not 98.75.
3. OID = 1,000 − 994.00 = **\$6.00** per bond, below the \$25 de minimis threshold → treated as zero.
4. Yield to investors:
   - Keystrokes: 20 [N], −994 [PV], 26.25 [PMT], 1000 [FV], [CPT] [I/Y] → 2.664; × 2 = **5.33%**

The \$6.50 per bond the syndicate keeps is the issuer's cost of issuance, amortized separately. It is **not** OID.

**BA II Plus Professional: Example 2**

| Step | Keystrokes | Display |
| --- | --- | --- |
| Issuer's net price | 99.40 [−] 0.65 [=] | 98.7500 |
| Net proceeds | [÷] 100 [×] 500000000 [=] | 493,750,000.0000 |
| OID per bond | 1000 [−] 994 [=] | 6.0000 |
| Clear TVM | [2nd] [CLR TVM] | 0.0000 |
| Periods | 20 [N] | N = 20.0000 |
| Price paid by investors | 994 [+/−] [PV] | PV = −994.0000 |
| Coupon | 26.25 [PMT] | PMT = 26.2500 |
| Face | 1000 [FV] | FV = 1,000.0000 |
| Yield per period | [CPT] [I/Y] | I/Y = 2.6641 |
| Annual BEY | [×] 2 [=] | 5.3282 |

### Example 3: Zero-coupon bond, deliberate OID (BKM 14.1, 14.4)

A 5-year zero is issued to yield 4.80% BEY.

**Formulas**

```math
\begin{aligned}
P_0 &= \frac{F}{(1+r)^{n}}, \quad r = \frac{y}{2} \\
\text{OID} &= F - P_0 \\
\text{OID}_k &= \text{AIP}_{k-1} \times r \\
\text{AIP}_k &= \text{AIP}_{k-1} + \text{OID}_k = P_0 (1+r)^{k}, \quad \text{AIP}_0 = P_0
\end{aligned}
```

| Symbol | Meaning | Example 3 value |
| --- | --- | --- |
| P₀ | Issue price of the zero (\$) | 788.86 |
| F | Face value (\$) | 1,000 |
| y | Yield at issue, annual BEY | 4.80% |
| r | Yield per six-month period | 2.40% |
| n | Number of semiannual periods to maturity | 10 |
| k | Accrual period number (1, 2, 3, ...) | 1 to 4 |
| OIDₖ | OID accrued (taxable interest) in period k (\$) | 18.93 in period 1 |
| AIPₖ | Adjusted issue price at the end of period k (\$), also the holder's tax basis | 867.36 after period 4 |

1. Issue price: 10 [N], 2.4 [I/Y], 0 [PMT], 1000 [FV], [CPT] [PV] → **−788.86**
2. OID = 1,000 − 788.86 = **\$211.14** (far above the \$12.50 de minimis threshold for 5 years).
3. Accrue OID by the constant yield method: each period, adjusted issue price × 2.4%.

| Period (6 months) | Adjusted issue price, start (\$) | OID accrued (\$) | Adjusted issue price, end (\$) |
| --- | --- | --- | --- |
| 1 | 788.86 | 18.93 | 807.79 |
| 2 | 807.79 | 19.39 | 827.18 |
| 3 | 827.18 | 19.85 | 847.03 |
| 4 | 847.03 | 20.33 | 867.36 |

Taxable interest is \$38.32 in year 1 and \$40.18 in year 2, with no cash received. The holder's basis rises by the same amounts.

**BA II Plus Professional: Example 3**

| Step | Keystrokes | Display |
| --- | --- | --- |
| Clear TVM | [2nd] [CLR TVM] | 0.0000 |
| Periods | 10 [N] | N = 10.0000 |
| Yield per period | 2.4 [I/Y] | I/Y = 2.4000 |
| No coupon | 0 [PMT] | PMT = 0.0000 |
| Face | 1000 [FV] | FV = 1,000.0000 |
| Issue price P₀ | [CPT] [PV] | PV = −788.8609 |
| OID | 1000 [−] 788.8609 [=] | 211.1391 |
| AIP after 1 period (PV, I/Y, PMT stay) | 1 [N] [CPT] [FV] | FV = 807.7936 |
| OID₁ | [−] 788.8609 [=] | 18.9327 |
| AIP after 2 periods | 2 [N] [CPT] [FV] | FV = 827.1807 |
| Year 1 taxable OID | [−] 788.8609 [=] | 38.3198 |
| AIP after 4 periods | 4 [N] [CPT] [FV] | FV = 867.3617 |
| Year 2 taxable OID | [−] 827.1807 [=] | 40.1810 |

This works because the adjusted issue price after k periods is P₀ compounded at r for k periods.

### Example 4: Same zero in the secondary market (BKM 3.5)

Two years later (3 years left), market yields on similar bonds have risen to 6.00% BEY. An investor buys the zero from a dealer.

**Formulas**

```math
\begin{aligned}
P_m &= \frac{F}{(1+r_m)^{n_r}}, \quad r_m = \frac{y_m}{2} \\
\text{MD} &= \text{AIP}_k - P_m \\
\text{DM}_{MD} &= 0.0025 \times F \times N_r
\end{aligned}
```

| Symbol | Meaning | Example 4 value |
| --- | --- | --- |
| yₘ | Current market yield on similar bonds, annual BEY | 6.00% |
| rₘ | Market yield per six-month period | 3.00% |
| nᵣ | Semiannual periods remaining to maturity | 6 |
| Pₘ | Secondary-market purchase price (\$) | 837.48 |
| AIPₖ | Adjusted issue price on the purchase date, from Example 3 (\$) | 867.36 |
| MD | Market discount (\$) | 29.88 |
| Nᵣ | Full years remaining to maturity | 3 |
| DM\_MD | Market discount de minimis threshold (\$) | 7.50 |

1. Market price: 6 [N], 3 [I/Y], 0 [PMT], 1000 [FV], [CPT] [PV] → **−837.48**
2. Adjusted issue price after 4 periods (Example 3) = **\$867.36**.
3. Market discount = 867.36 − 837.48 = **\$29.88**. The de minimis threshold is 0.0025 × 1,000 × 3 = \$7.50, so it counts.
4. The buyer keeps accruing the remaining OID each year **and** has \$29.88 of market discount, taxed as ordinary income at maturity unless they elect to accrue it.

**BA II Plus Professional: Example 4**

| Step | Keystrokes | Display |
| --- | --- | --- |
| Clear TVM | [2nd] [CLR TVM] | 0.0000 |
| Periods remaining | 6 [N] | N = 6.0000 |
| Market yield per period | 6 [÷] 2 [=] [I/Y] | I/Y = 3.0000 |
| No coupon | 0 [PMT] | PMT = 0.0000 |
| Face | 1000 [FV] | FV = 1,000.0000 |
| Market price Pₘ | [CPT] [PV] | PV = −837.4843 |
| Market discount | 867.3617 [−] 837.4843 [=] | 29.8774 |
| De minimis | 0.0025 [×] 1000 [×] 3 [=] | 7.5000 |

### Example 5: The dealer's spread (BKM 3.7)

A dealer quotes a corporate bond at 98.50 bid / 98.75 ask. Buying and immediately selling \$100,000 face costs (98.75 − 98.50)% × \$100,000 = **\$250**. That is the dealer's compensation for holding inventory and providing liquidity. It has no effect on OID.

**Formula**

```math
\text{Round-trip cost} = \frac{P_{ask} - P_{bid}}{100} \times Q
```

| Symbol | Meaning | Example 5 value |
| --- | --- | --- |
| P\_ask | Dealer's ask price (investor buys), % of par | 98.75 |
| P\_bid | Dealer's bid price (investor sells), % of par | 98.50 |
| Q | Face amount traded (\$) | 100,000 |
| Round-trip cost | Cost of buying and immediately selling (\$) | 250 |

**BA II Plus Professional: Example 5**

| Step | Keystrokes | Display |
| --- | --- | --- |
| Spread in points | 98.75 [−] 98.50 [=] | 0.2500 |
| Dollar cost | [÷] 100 [×] 100000 [=] | 250.0000 |

## Common pitfalls

- **Using the issuer's net proceeds as the issue price.** The issue price is the public offering price. The underwriting spread is a cost of issuance, not OID.
- **Calling every below-par bond an OID bond.** A discount that appears after issuance because rates rose is market discount. OID is fixed when the bond is first sold.
- **Assuming the issuer picks the price.** The issuer (or Treasury) picks the coupon; the auction or the underwriter's book of orders sets the price.
- **Accruing OID in a straight line.** OID accrues by the constant yield method, so later accruals are larger than early ones.
- **Forgetting the de minimis test.** Small discounts from Treasury coupon rounding or corporate pricing are usually treated as zero OID.
- **Thinking the issuer benefits from secondary trading.** The issuer receives cash only in the primary market. Secondary prices matter to the issuer only for the cost of its *next* issue.
- **Mixing up firm commitment and best efforts.** In a firm commitment the underwriter bears the price risk; in best efforts the issuer does.

## Key-terms checklist

- [ ] **Primary market:** the market where new securities are sold by the issuer, which receives the proceeds (BKM 3.1).
- [ ] **Secondary market:** the market where existing securities trade between investors; the issuer receives nothing (BKM 3.1).
- [ ] **Investment banker:** a firm that advises issuers on structuring and pricing new securities and distributes them to investors.
- [ ] **Underwriter:** the investment banker that buys or markets a new issue; in a firm commitment it takes the price risk.
- [ ] **Underwriting syndicate:** a group of investment banks, led by one or more lead managers, that share the work and risk of distributing an issue.
- [ ] **Firm commitment:** an underwriting in which the syndicate buys the entire issue from the issuer at an agreed price and resells it to the public, bearing the risk of unsold securities.
- [ ] **Best efforts:** an underwriting in which the banker agrees only to try to sell the issue; the issuer bears the risk of unsold securities.
- [ ] **Public offering price:** the price at which the underwriters sell the new issue to the public; for bonds, this sets the issue price used to measure OID.
- [ ] **Underwriting spread:** the difference between the public offering price and the price the underwriter pays the issuer; the underwriters' compensation and the issuer's cost of issuance.
- [ ] **Prospectus:** the disclosure document filed with the SEC and given to investors, describing the issuer, the securities and the risks.
- [ ] **Shelf registration (Rule 415):** an SEC rule letting an issuer register securities once and sell them gradually over up to two years.
- [ ] **Private placement (Rule 144A):** a sale of securities directly to a small number of qualified institutional buyers without full SEC registration; Rule 144A allows those buyers to trade the securities among themselves.
- [ ] **Bookbuilding:** the underwriter's process of collecting investor orders at different prices or yields to set the final price of a new issue.
- [ ] **Single-price (uniform) auction:** the auction format the U.S. Treasury uses, in which all winning bidders pay the same price, set by the highest accepted yield.
- [ ] **High (stop-out) yield:** the highest yield accepted in a Treasury auction; every winning bidder receives this yield.
- [ ] **Competitive bid:** a Treasury auction bid that specifies the yield the bidder will accept; it may be rejected if the yield is above the stop-out.
- [ ] **Noncompetitive bid:** a Treasury auction bid that accepts whatever yield the auction sets; it is filled in full, up to a size limit.
- [ ] **Dealer market:** a market in which dealers buy and sell for their own inventory, quoting prices at which they will trade (BKM 3.2).
- [ ] **Over the counter (OTC):** trading arranged through a network of dealers rather than on an organized exchange; most bonds trade this way.
- [ ] **Bid price:** the price at which a dealer will buy a security; the price an investor receives when selling.
- [ ] **Ask price:** the price at which a dealer will sell a security; the price an investor pays when buying.
- [ ] **Bid-ask spread:** the ask price minus the bid price; the dealer's compensation and an implicit trading cost for investors (BKM 3.7).
- [ ] **Market maker:** a dealer that stands ready to quote bid and ask prices in a security, providing liquidity; underwriters often make markets in bonds they issue.
- [ ] **TRACE:** FINRA's Trade Reporting and Compliance Engine, which collects and publishes prices of corporate and agency bond trades.
- [ ] **Securities Act of 1933:** the U.S. law requiring registration and full disclosure for new securities issues (primary market) (BKM 3.10).
- [ ] **Securities Exchange Act of 1934:** the U.S. law that created the SEC and regulates secondary-market trading, exchanges and broker-dealers (BKM 3.10).
- [ ] **Original issue discount (OID):** the amount by which a debt instrument's stated redemption price at maturity exceeds its issue price.
- [ ] **Stated redemption price at maturity:** the total amount payable at maturity other than regular periodic interest; usually face (par) value.
- [ ] **Issue price:** the first price at which a substantial amount of a bond issue is sold to the public (not to underwriters or dealers).
- [ ] **Adjusted issue price:** the issue price plus all OID accrued to date; the bond's accreted value and the original holder's tax basis.
- [ ] **Constant yield method:** the method for accruing OID in which each period's accrual equals the adjusted issue price times the yield at issue, so accruals grow over time.
- [ ] **De minimis OID:** OID smaller than 0.25% of the stated redemption price times the full years to maturity; it is treated as zero.
- [ ] **Market discount:** the amount by which a bond's adjusted issue price (or par, for a bond issued at par) exceeds the price paid for it in the secondary market.
- [ ] **Zero-coupon bond:** a bond that pays no coupons and is sold at a discount to par; the entire return comes from price appreciation (BKM 14.1).
- [ ] **Deep-discount bond:** a bond issued with a coupon well below the market yield, so it sells far below par.
- [ ] **STRIPS:** Separate Trading of Registered Interest and Principal of Securities; the Treasury program that lets coupon and principal payments of Treasury securities trade as separate zero-coupon bonds (BKM 14.4).

## CFA-style practice questions

**1. (Conceptual)** A company sells newly issued bonds to investors through an underwriting syndicate. This transaction takes place in the:

- A. secondary market, because the underwriter resells the bonds.
- B. primary market, because the issuer receives the proceeds.
- C. money market, because the bonds are sold through dealers.

**2. (Conceptual)** In a firm-commitment underwriting, the risk that the bonds cannot be sold at the public offering price is borne by the:

- A. issuer.
- B. investors who buy in the offering.
- C. underwriting syndicate.

**3. (Algorithmic)** A 10-year Treasury note auction clears at a high yield of 3.96%. The note's coupon and the treatment of its discount are closest to:

- A. 4.000% coupon; issued at a premium, no OID.
- B. 3.875% coupon; OID of about \$6.96 per \$1,000, treated as zero under the de minimis rule.
- C. 3.875% coupon; OID of about \$6.96 per \$1,000, accrued each year as interest.

**4. (Algorithmic)** A 20-year corporate bond is sold to the public at 98.90. The underwriting spread is 0.75 points. For tax purposes, the OID per \$1,000 bond is:

- A. \$18.50, because the issuer nets 98.15.
- B. \$11.00, but it is treated as zero because it is below the \$50 de minimis threshold.
- C. \$11.00, accrued annually by the constant yield method.

**5. (Algorithmic)** A 7-year zero-coupon bond is issued to yield 5.00% (BEY, semiannual). The OID accrued in the first six-month period is closest to:

- A. \$17.69
- B. \$20.88
- C. \$35.39

**6. (Conceptual)** An investor buys a bond in the secondary market two years after issuance at a price below its adjusted issue price, because interest rates have risen. The difference between the adjusted issue price and the purchase price is:

- A. additional original issue discount.
- B. market discount.
- C. an underwriting spread.

**7. (Conceptual)** Which statement about the secondary market for corporate bonds is *most* accurate?

- A. Most corporate bonds trade on organized exchanges with continuous auction pricing.
- B. Most corporate bonds trade over the counter through dealers, and many issues trade infrequently.
- C. The issuer receives part of the proceeds each time its bonds trade.

**8. (Conceptual)** A large, frequent corporate issuer wants to register bonds once and sell them in tranches over the next two years as market conditions allow. It will most likely use:

- A. shelf registration under Rule 415.
- B. a private placement under Rule 144A.
- C. a best-efforts underwriting.

## Answer key

| # | Answer | Explanation |
| --- | --- | --- |
| 1 | B | The primary market is where the issuer sells new securities and receives cash. The underwriter's resale is part of the distribution (BKM 3.1). |
| 2 | C | In a firm commitment, the syndicate buys the issue outright and bears the price risk. In best efforts, the issuer bears it. |
| 3 | B | 3.96% rounded down to the nearest 1/8% is 3.875%. Price: 20 [N], 1.98 [I/Y], 19.375 [PMT], 1000 [FV], [CPT] [PV] → −993.04. OID = \$6.96, below the \$25 threshold (0.25% × 1,000 × 10), so it is treated as zero. A rounds the wrong way; C ignores de minimis. |
| 4 | B | The issue price is the public price, 98.90, so OID = \$11.00. The threshold is 0.0025 × 1,000 × 20 = \$50, so OID is treated as zero. A wrongly uses the issuer's net price; C ignores de minimis. |
| 5 | A | Price: 14 [N], 2.5 [I/Y], 0 [PMT], 1000 [FV], [CPT] [PV] → −707.73. First accrual = 707.73 × 2.5% = \$17.69. B is straight-line (\$292.27 / 14); C uses the annual rate on a semiannual period. |
| 6 | B | OID is set at issuance. A discount below the adjusted issue price that arises in later trading is market discount. |
| 7 | B | Bonds trade mainly in OTC dealer markets with thin, fragmented liquidity (BKM 3.5). The issuer receives nothing from secondary trades. |
| 8 | A | Shelf registration lets an issuer register once and sell over up to two years (BKM 3.1). |
