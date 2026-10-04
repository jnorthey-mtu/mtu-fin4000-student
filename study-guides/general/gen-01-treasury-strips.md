# Study Guide 1: Treasury STRIPS

*Fixed Income Study Guides*

[← All study guides](../../study-guide-index.md)

A STRIPS is a single Treasury cash flow sold on its own: one known dollar amount, paid on one known date, with nothing in between. They exist so investors can lock in today's spot rate for a specific date with no reinvestment risk.

## 1. What they are

- STRIPS stands for Separate Trading of Registered Interest and Principal of Securities. The program began in 1985; reconstitution was added in 1986.
- A dealer asks the Fed to split an eligible Treasury note, bond or TIPS into its cash flows. A 10-year note becomes 21 zeros: 20 coupon pieces and 1 principal piece, each with its own CUSIP.
- Treasury does not auction STRIPS. They are created by dealers and exist only in the commercial book-entry system, not in TreasuryDirect.
- Minimum to strip a fixed-principal note or bond: \$100 par, in multiples of \$100. Floating rate notes cannot be stripped.
- Reconstitution is the reverse: a dealer holding every remaining piece can reassemble the original bond. Stripping and reconstitution together keep STRIPS prices tied to coupon Treasury prices by arbitrage.

| Piece | Wall Street code | Fungible? |
| --- | --- | --- |
| Coupon (interest) strip | ci | Yes: every coupon strip with the same payment date shares one CUSIP, whatever bond it came from |
| Principal strip from a note | np | No: tied to its parent issue |
| Principal strip from a bond | bp | No: tied to its parent issue |

Because only the matching principal strip can reconstitute a given bond, principal strips sometimes trade at slightly different prices than coupon strips of the same date.

## 2. Why they are used

The core use is matching a known future payment. A zero delivers an exact amount on an exact date, so the payment is locked in today.

- **Liability matching (immunization):** pensions and insurers buy strips maturing on the dates benefits or annuity payments fall due.
- **No reinvestment risk:** a coupon bond's coupons must be reinvested at unknown future rates. A zero has no coupons, so its return to maturity is fixed at purchase.
- **Target-date saving:** an individual funds a tuition bill or retirement date, usually inside an IRA.
- **Duration and rate views:** a zero's Macaulay duration equals its maturity, the longest available for its date. At 4.5%, a 30-year strip falls about 25.4% for a 100 bp rise; a 30-year 4.5% par bond falls about 14.6%.
- **Reading the spot curve:** strip prices show the market's discount rate for each date directly, without bootstrapping.

What a strip does **not** do: it does not beat the market rate. You earn exactly the spot yield at purchase if held to maturity. Nominal strips fix dollars, not purchasing power; TIPS principal strips cover real needs.

## 3. How they are quoted

- **Price:** per 100 of face value, usually in decimals (for example 41.065), unlike coupon Treasuries, which trade in 32nds.
- **Yield:** annualized with semiannual compounding (bond-equivalent yield), so strips line up with the coupon Treasury curve.
- **Day count:** Actual/Actual on the semiannual schedule, so the number of periods can be fractional between coupon dates.
- **Tables:** a listing shows maturity date, type (ci, np, bp), bid, ask, change and ask yield.

## 4. How they are priced

Price per 100 face, where $`y`$ is the bond-equivalent yield and $`n`$ the number of semiannual periods to maturity:

```math
P = \frac{100}{\left(1 + \frac{y}{2}\right)^{n}}
```

Between coupon dates, $`n`$ = whole periods remaining + (days to next coupon date ÷ days in the current period).

Yield from price:

```math
y = 2\left[\left(\frac{100}{P}\right)^{1/n} - 1\right]
```

Worked example: 20-year strip, 4.5% yield. $`n = 40`$, so $`P = 100 / 1.0225^{40} = 41.065`$. \$10,000 face costs \$4,106.46.

Risk measures:

```math
D_{mac} = T \qquad D_{mod} = \frac{T}{1 + y/2} \qquad C = \frac{T\,(T + 0.5)}{(1 + y/2)^{2}}
```

For the 30-year strip at 4.5%, modified duration $`= 30 / 1.0225 = 29.3`$.

## 5. Tax: phantom income

- The discount accretes as original issue discount (OID). The holder reports it as interest income each year, though no cash arrives.
- Example: the 20-year strip above accretes $`41.065 \times (1.0225^{2} - 1) = 1.87`$ per 100 of taxable income in year one.
- That is why strips mostly sit in IRAs, pensions and other tax-deferred or tax-exempt accounts.

## 6. TIPS strips

- TIPS can be stripped into coupon and principal pieces.
- The principal strip pays the inflation-adjusted principal or par, whichever is greater, at maturity. It locks in a real yield rather than a nominal one.
- TIPS coupon strips are adjusted for inflation but carry no deflation floor. Liquidity is thinner than for nominal strips.

## 7. Review questions

1. Why does a strip have no reinvestment risk? *No cash flows before maturity, so nothing has to be reinvested.*
2. Why are coupon strips fungible but principal strips not? *Coupon strips for a date share a CUSIP; a principal strip is tied to one parent bond for reconstitution.*
3. Price a 10-year strip at 4.0%. *Answer:* $`100 / 1.02^{20} = 67.297`$.
4. A 15-year strip trades at 50.00. Its yield? *Answer:* $`2\left[(100/50)^{1/30} - 1\right] = 4.67\%`$.
5. What does reconstitution do to pricing? *It caps how far a coupon bond can drift from the sum of its strip prices.*
6. Why hold strips in an IRA? *To avoid tax on accreted income that pays no cash.*

## 8. CFA-style review questions

Original questions in the CFA Level I format (three choices, one correct). Not CFA Institute material.

1. A 10-year Treasury principal STRIP has a bond-equivalent yield of 4.00%. Its price per 100 of face value is closest to:
   - A. 67.30
   - B. 67.56
   - C. 68.06
2. Held to maturity, which security has no reinvestment risk?
   - A. A 10-year 4% Treasury note
   - B. A Treasury principal STRIP
   - C. A 2-year Treasury floating rate note
3. The Macaulay duration of a 12-year zero-coupon bond is:
   - A. less than 12 years
   - B. equal to 12 years
   - C. greater than 12 years
4. Reconstitution of a Treasury security refers to:
   - A. combining all of its STRIPS back into the original bond
   - B. Treasury reopening an existing issue at auction
   - C. exchanging a STRIP for a TIPS of the same maturity
5. A taxable U.S. investor holding a STRIPS in a regular brokerage account:
   - A. owes no tax until the STRIP matures
   - B. owes federal tax each year on the accreted discount
   - C. owes only capital gains tax at maturity

**Answer key**

1. A. $`100 / 1.02^{20} = 67.30`$. B uses annual compounding.
2. B. A zero has no interim cash flows to reinvest.
3. B. A zero's duration equals its maturity.
4. A. Dealers reassemble the coupon and principal pieces.
5. B. The accretion is original issue discount, taxed annually as interest (phantom income).

## 9. Bloomberg Terminal exercises (draft: verify on the campus Terminal)

These are drafts. Confirm each command, ticker and field on the Terminal and tick the last column. Use `FLDS <GO>` to confirm Excel field names and `HELP HELP` for the analyst desk.

| Command | What to do | Check against this guide | Verified |
| --- | --- | --- | --- |
| `SRCH <GO>` | Search fixed income: issuer U.S. Treasury, security type STRIPS; list coupon (ci) and principal (np, bp) strips by maturity | Section 1: coupon vs principal strips | ☐ |
| `<strip ticker> Govt DES <GO>` | Open one strip's description; note CUSIP, type and maturity. Confirm the ticker convention for coupon and principal strips | Sections 1 and 3 | ☐ |
| `YAS <GO>` | Price the strip maturing nearest Nov 15, 2046; enter 4.5% as the yield | Section 4: price ≈ 41.065, modified duration ≈ 19.56 | ☐ |
| `CSHF <GO>` | Show the strip's cash flows | One payment at maturity | ☐ |
| `GC <GO>` | Plot the strips curve against the Treasury actives (par) curve | Strip yields vs coupon yields; spot vs par (Study Guide 2) | ☐ |
| `FIT <GO>` | Open the Treasury monitor and look for a STRIPS view | Section 3: decimal prices, yields | ☐ |

Excel add-in (Bloomberg tab): `=BDP("<strip ticker> Govt","PX_MID")`, `=BDP("<strip ticker> Govt","YLD_YTM_MID")`, `=BDP("<strip ticker> Govt","DUR_ADJ_MID")`.

**Exercise:** pick three principal strips (5, 10 and 20 years). Record the Terminal price and yield, then recompute the price with the formula in section 4. Explain any difference (day count, settlement date).

## 10. Reading in Bodie, Kane & Marcus, *Investments*, 13th ed. (2024)

| Section | Topic in the book | Supports |
| --- | --- | --- |
| 14.4 Bond Prices over Time | Zero-Coupon Bonds and Treasury Strips; After-Tax Returns | Core reading: strip pricing, pull to par, OID taxation |
| 14.1 Bond Characteristics | Treasury Bonds and Notes; Accrued Interest and Quoted Bond Prices; Indexed Bonds | Quoting conventions, TIPS mechanics |
| 2.2 The Bond Market | Treasury Notes and Bonds; Inflation-Protected Treasury Bonds | Institutional background, TIPS |
| 15.1 The Yield Curve | Bond Pricing | Valuing coupon bonds as bundles of zeros |
| 16.1 Interest Rate Risk | Duration; Rules for Duration | Why a zero's duration equals its maturity |
| 16.2 Convexity | Why Do Investors Like Convexity? | Convexity of long zeros |
| 16.3 Passive Bond Management | Immunization; Cash Flow Matching and Dedication | The main use of strips: liability matching |

Sections are from the 13th edition; recent editions use the same chapter structure.

Sources: [TreasuryDirect, STRIPS](https://maint.treasurydirect.gov/marketable-securities/strips) · [31 CFR 356.31](https://www.law.cornell.edu/cfr/text/31/356.31) · [TreasuryDirect STRIPS timeline](https://www.treasurydirect.gov/research-center/timeline/strips)
