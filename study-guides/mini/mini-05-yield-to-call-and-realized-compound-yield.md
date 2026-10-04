# Mini Study Guide 5: Yield to Call and Realized Compound Yield

*BKM Ch. 14*

[← All study guides](../../study-guide-index.md)

FIN 4000 Investments · Midterm prep · Sep 28, 2026 · Jim Northey

## Learning objectives

YTM is a promise that holds only if the bond is not called and every coupon is reinvested at the YTM. Yield to call and realized compound yield show what happens when those assumptions fail.

After this guide you should be able to:

1. Compute yield to call (YTC) and identify the yield to worst.
2. Explain why premium callable bonds are priced off YTC.
3. Compute realized compound yield (RCY) for a given reinvestment rate.
4. Compute a horizon (holding-period) return when rates change before maturity.

## Core concept

### YTM, YTC, and yield to worst

| Measure | Final cash flow | Timing | Assumes |
| --- | --- | --- | --- |
| Yield to maturity | Par value | Maturity date | Bond is held to maturity; coupons reinvested at YTM |
| Yield to call | Call price (often par + a premium) | First call date | Bond is called at the first opportunity |
| Yield to worst | Whichever gives the lowest yield | Earliest harmful date | The issuer acts against you |

Issuers call bonds when rates have fallen, which is when the bond trades at a premium. So for a **premium** callable bond, YTC is usually below YTM and becomes the yield to worst. For a **discount** bond, a call is unlikely and YTM is the relevant yield.

Near the call price, a callable bond's price is capped. It cannot rise much above the call price, however far rates fall (price compression, or negative convexity).

### Reinvestment risk and realized compound yield

YTM assumes every coupon is reinvested at the YTM. If reinvestment rates differ, the investor's actual return differs.

```math
\text{RCY} = \left(\frac{\text{Future value of all coupons (reinvested)} + \text{Par}}{\text{Price paid}}\right)^{1/T} - 1
```

**Where:**

- RCY = realized compound yield, per year
- Future value of all coupons (reinvested) = value at maturity of every coupon, reinvested at the actual reinvestment rate
- Par = face value repaid at maturity
- Price paid = purchase price of the bond
- T = years to maturity

* Reinvestment rate > YTM → RCY > YTM.
* Reinvestment rate < YTM → RCY < YTM.
* A zero-coupon bond held to maturity has **no reinvestment risk**: its RCY always equals its YTM.

### Horizon analysis

If you sell before maturity, your return depends on the sale price, which depends on yields at the horizon:

```math
\text{Horizon return} = \left(\frac{\text{FV of coupons to horizon} + \text{Price at horizon}}{\text{Price paid}}\right)^{1/H} - 1
```

**Where:**

- Horizon return = annualized return over the holding period
- FV of coupons to horizon = value at the horizon date of all coupons received, with reinvestment
- Price at horizon = sale price at the horizon, set by market yields at that time
- Price paid = purchase price of the bond
- H = holding period (horizon), in years

Rising rates hurt the sale price but help reinvestment. Falling rates do the opposite. This trade-off is the basis of immunization in Ch. 16.

## Worked examples

### Example 1: YTM vs. YTC (Algorithmic)

A 20-year bond pays a 7% coupon semiannually and sells for \$1,120. It is callable in 5 years at \$1,050.

**YTM:** `40` `N` · `35` `PMT` · `1120` `+/-` `PV` · `1000` `FV` · `CPT` `I/Y` → 2.982 per half-year → × 2 = **5.96%**

**YTC:** `10` `N` · `35` `PMT` · `1120` `+/-` `PV` · `1050` `FV` · `CPT` `I/Y` → 2.569 → × 2 = **5.14%**

The bond sells at a premium and YTC < YTM, so the **yield to worst is 5.14%**. A buyer should expect the bond to be called if rates stay where they are.

### Example 2: Realized compound yield (Algorithmic)

You buy a 3-year, 8% annual-coupon bond at par (\$1,000). Its YTM is 8%. What is your RCY if coupons are reinvested at 6%? At 10%?

| Cash flow | FV at 6% | FV at 10% |
| --- | --- | --- |
| Year 1 coupon, reinvested 2 years | 80 × 1.06² = \$89.89 | 80 × 1.10² = \$96.80 |
| Year 2 coupon, reinvested 1 year | 80 × 1.06 = \$84.80 | 80 × 1.10 = \$88.00 |
| Year 3 coupon + par | \$1,080.00 | \$1,080.00 |
| **Total at year 3** | **\$1,254.69** | **\$1,264.80** |
| **RCY** | (1,254.69 / 1,000)^(1/3) − 1 = **7.86%** | (1,264.80 / 1,000)^(1/3) − 1 = **8.15%** |

**BA II Plus (RCY at 6%):** `3` `N` · `1000` `+/-` `PV` · `0` `PMT` · `1254.69` `FV` · `CPT` `I/Y` → 7.86

### Example 3: Horizon return when rates rise (Algorithmic)

You buy a 10-year, 6% annual-coupon bond at par and plan to sell in 2 years. Right after purchase, yields rise to 7% and stay there.

1. Price at year 2 (8 years left, 7% yield): `8` `N` · `7` `I/Y` · `60` `PMT` · `1000` `FV` · `CPT` `PV` → **\$940.29**.
2. Coupons with reinvestment: 60 × 1.07 + 60 = **\$124.20**.
3. Horizon value = 940.29 + 124.20 = \$1,064.49.
4. Annualized horizon return = (1,064.49 / 1,000)^(1/2) − 1 = **3.17%**.

The small reinvestment gain did not offset the \$59.71 price loss over a short horizon. Over a longer horizon it would matter more.

## Common pitfalls

- **Using par as the FV for YTC.** The final cash flow is the call price.
- **Using years to maturity for YTC.** N is the number of periods to the first call date.
- **Forgetting to annualize.** For semiannual bonds, double the periodic I/Y (bond-equivalent yield).
- **Assuming YTM is the return you will earn.** It is only if the bond is held to maturity, not called, and coupons are reinvested at the YTM.
- **Saying zeros have reinvestment risk.** A zero held to maturity has none. It still has price risk if sold early.

## Key terms and definitions

- [ ] **Yield to maturity (YTM):** the discount rate that sets the present value of a bond's promised payments equal to its price.
- [ ] **Yield to call (YTC):** the YTM calculated assuming the bond is called at the first call date for the call price.
- [ ] **Yield to worst:** the lowest of the YTM and all possible yields to call.
- [ ] **Call price / call premium:** the price the issuer pays to redeem a callable bond; the premium is the amount above par.
- [ ] **Deferred call (call protection):** an initial period during which the bond cannot be called.
- [ ] **Premium vs. discount bond:** a bond priced above par (coupon rate > YTM) vs. below par (coupon rate < YTM).
- [ ] **Reinvestment rate risk:** the risk that coupons are reinvested at rates below the YTM.
- [ ] **Realized compound yield (RCY):** the compound annual return actually earned, given the actual reinvestment rate.
- [ ] **Horizon analysis:** forecasting the realized return over a holding period from an assumed sale price and reinvestment rate.
- [ ] **Bond-equivalent yield vs. effective annual yield:** BEY = periodic yield × number of periods per year; EAY = (1 + periodic yield)^periods − 1, which includes compounding.
- [ ] **Price compression (negative convexity):** the cap on a callable bond's price near the call price as rates fall.

## CFA-style practice questions

**Q1 [Algorithmic].** A 10-year, 6% semiannual-coupon bond sells for \$1,080. It is callable in 3 years at \$1,030. Its yield to call is *closest* to:

- A. 4.09%
- B. 4.97%
- C. 5.56%

**Q2 [Conceptual].** A callable bond trades well above par. Investors will *most likely* price it using:

- A. its current yield.
- B. its yield to maturity.
- C. its yield to call.

**Q3 [Algorithmic].** An investor buys a 2-year, 9% annual-coupon bond at par and reinvests the first coupon at 5%. Her realized compound yield is *closest* to:

- A. 7.00%
- B. 8.83%
- C. 9.00%

**Q4 [Conceptual].** A bond is bought at its YTM of 7% and held to maturity. Coupons are reinvested at 8%. The realized compound yield will be:

- A. less than 7%.
- B. equal to 7%.
- C. greater than 7%.

**Q5 [Algorithmic].** An investor buys a 10-year, 5% annual-coupon bond at par. One year later, just after the first coupon, the market yield is 6% and she sells. Her one-year holding-period return is *closest* to:

- A. −6.80%
- B. −1.80%
- C. 5.00%

**Q6 [Conceptual].** Which bond held to maturity has the *least* reinvestment risk?

- A. A 20-year, 9% coupon bond
- B. A 20-year, 3% coupon bond
- C. A 20-year zero-coupon bond

**Q7 [Conceptual].** As market rates fall, the price of a callable bond rises *less* than an otherwise identical straight bond because:

- A. the issuer is more likely to call it at the call price.
- B. its coupon rate rises.
- C. its default risk increases.

**Q8 [Conceptual].** A premium bond has a YTM of 5.2%, a YTC (first call) of 4.6%, and a YTC (second call) of 4.9%. Its yield to worst is:

- A. 4.6%
- B. 4.9%
- C. 5.2%

## Answer key

| Q | Answer | Explanation |
| --- | --- | --- |
| 1 | A | N = 6, PMT = 30, PV = −1,080, FV = 1,030 → I/Y = 2.045% × 2 = 4.09%. B is the YTM (N = 20, FV = 1,000). C is the current yield (60 / 1,080). |
| 2 | C | A premium bond is likely to be called, so YTC is the yield to worst. |
| 3 | B | FV = 90 × 1.05 + 1,090 = \$1,184.50. RCY = (1.1845)^(1/2) − 1 = 8.83%. C is the YTM, which assumes reinvestment at 9%. |
| 4 | C | Reinvesting above the YTM raises the realized yield above the YTM. |
| 5 | B | Price with 9 years left at 6% = \$931.98. HPR = (50 + 931.98) / 1,000 − 1 = −1.80%. A leaves out the coupon; C ignores the price change. |
| 6 | C | A zero has no coupons to reinvest, so its return to maturity is locked in. |
| 7 | A | As rates fall, a call becomes more likely, capping the price near the call price. |
| 8 | A | Yield to worst is the lowest of all yields, 4.6%. |
