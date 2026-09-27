# Study Guide 7: Bonds with Embedded Options: Callable, Putable and Convertible

*Fixed Income Study Guides*

[← All study guides](README.md)

Many bonds carry an option that lets the issuer or the investor change the cash flows. To value them you need two ideas: how an option works, and how interest rates move. This guide starts with the options review in Bodie Chapter 2, then applies it to callable, putable and convertible bonds.

## 1. Options review (Bodie Chapter 2.5, Derivative Markets)

An **option** gives its buyer the **right, but not the obligation**, to buy or sell an asset at a fixed price (the **strike** or exercise price) on or before a set date. The buyer pays a **premium** for that right; the seller (writer) collects it and must perform if the buyer exercises.

| | Call option | Put option |
| --- | --- | --- |
| Buyer's right | Buy the asset at the strike | Sell the asset at the strike |
| Buyer profits when | The asset price rises above the strike | The asset price falls below the strike |
| Payoff at expiration | max(S − K, 0) | max(K − S, 0) |

$$\text{Call payoff} = \max(S_T - K,\ 0) \qquad \text{Put payoff} = \max(K - S_T,\ 0) \qquad \text{Profit} = \text{Payoff} - \text{Premium}$$

Example: a call with strike 100 bought for a premium of 4. If the asset ends at 110, the payoff is 10 and the profit 6. At 95, the call expires worthless and the buyer loses the 4 premium. A put with strike 100 pays 10 if the asset ends at 90.

**Moneyness and value**

- **In the money:** exercising now would pay (call: S > K; put: S < K). **At the money:** S = K. **Out of the money:** exercising now would not pay.
- **Option value = intrinsic value + time value.** Intrinsic value is the payoff from exercising now; time value is what the chance of a better outcome is worth before expiration.
- **Value rises with volatility and time to expiration** for both calls and puts: more uncertainty means more chance of a large payoff, while losses are capped at the premium.

**Exercise styles**

| Style | Can exercise | Bond example |
| --- | --- | --- |
| European | Only at expiration | A bond callable on one date only |
| American | Any time up to expiration | A bond callable continuously after its protection period |
| Bermudan | On a set of dates | A bond callable on each coupon date (the most common case) |

**Options vs futures.** A futures contract **obligates** both sides to trade at the futures price on the delivery date, so gains and losses are symmetric and no premium is paid up front. An option's payoff is **asymmetric**: the buyer's loss is limited to the premium. That asymmetry is exactly what an embedded bond option adds.

**Bridge to bonds.** Replace the stock with a bond and its price with the level of interest rates:

- A **callable** bond: the issuer owns a **call on the bond**. It is in the money when rates fall and the bond's value rises above the call price.
- A **putable** bond: the investor owns a **put on the bond**. It is in the money when rates rise and the bond's value falls below the put price.
- A **convertible** bond: the investor owns a **call on the issuer's stock**, paid for with the bond.

## 2. Callable bonds

The issuer may redeem the bond before maturity at a set **call price**, usually par or a small premium that steps down over time.

**Key terms**

- **Call protection:** a period after issue when the bond cannot be called (for example, "10 non-call 5": 10-year maturity, callable after 5 years).
- **Call schedule:** the dates and prices at which the bond can be called; usually each coupon date after protection ends (Bermudan).
- **Make-whole call:** the call price is the present value of remaining payments at a Treasury yield plus a small spread. It is so expensive that it is used mainly for mergers or restructurings, not for refinancing.
- U.S. Treasuries issued today are not callable; callables are common among corporates, municipals and agency debt.

**Why issuers use them.** When rates fall, the issuer can call the bond and refinance at a lower coupon, like a homeowner refinancing a mortgage. The call also allows early retirement of debt after an asset sale or restructuring.

**What the investor gives up and gets**

- The investor is short the call, so the bond is worth less than an otherwise identical option-free (straight) bond and pays a **higher yield** in compensation.
- **Reinvestment risk:** calls happen when rates are low, so proceeds are reinvested at lower rates.
- **Price compression:** as rates fall, the price stops rising near the call price. This is **negative convexity** (Study Guide 5).

$$V_{callable} = V_{straight} - V_{call}$$

**Yield measures:** yield to maturity, yield to each call date, and **yield to worst**, the lowest of them.

$$P = \sum_{k=1}^{n_c} \frac{C/2}{\left(1 + \frac{y_c}{2}\right)^{k}} + \frac{CP}{\left(1 + \frac{y_c}{2}\right)^{n_c}}$$

Example (from Study Guide 4): a 10-year 5% bond at 105, callable in 5 years at 101. YTM = 4.377%, YTC = 4.067%, so YTW = **4.067%**. A premium callable is usually priced to its call; a discount callable to its maturity.

## 3. Putable bonds

The investor may sell the bond back to the issuer at a set **put price**, usually par, on one or more dates before maturity.

**Why they are used**

- **Investors** get protection against rising rates and, to a degree, against credit deterioration: if the bond's value falls below the put price, they hand it back and reinvest at the new higher rates.
- **Issuers** pay a **lower coupon** in return, and may attract buyers who would otherwise avoid long maturities.
- The issuer's risk: puts are exercised just when refinancing is most expensive, sometimes when the issuer is in trouble.

$$V_{putable} = V_{straight} + V_{put}$$

**Price floor:** as rates rise, the price stops falling near the put price, which shortens effective duration.

**Yield to put** uses the put date and put price in place of maturity and par. Example: a 10-year 5% bond at 97, putable at 100 in 3 years. YTM = 5.392%; yield to put = **6.110%**. The put only adds to the holder's options, so the YTM is the conservative figure; the yield to put shows the return if the investor exercises.

## 4. Convertible bonds

The investor may exchange the bond for a set number of the issuer's shares.

| Term | Definition | Example (\$1,000 par) |
| --- | --- | --- |
| Conversion ratio | Shares received per bond | 25 shares |
| Conversion price | Par ÷ conversion ratio | \$1,000 ÷ 25 = \$40 |
| Conversion value | Share price × conversion ratio | \$36 × 25 = \$900 |
| Straight value | Value as an option-free bond | \$850 |
| Minimum value | The larger of straight value and conversion value | \$900 |
| Market conversion premium | (Price − conversion value) ÷ conversion value | (\$1,000 − \$900) ÷ \$900 = 11.1% |

$$V_{convertible} = V_{straight} + V_{call\ on\ stock} \qquad \text{Floor} = \max(\text{straight value},\ \text{conversion value})$$

- **Why issuers use them:** a lower coupon than straight debt, and possible future equity issuance at a price above today's share price.
- **Why investors buy them:** bond-like downside (the straight value floor) with equity upside.
- **Behavior:** with the stock well below the conversion price the convertible trades like a bond ("busted"); well above it, like the stock. Most convertibles are also callable, which lets the issuer force conversion once the stock has risen.

$$V_{callable\ convertible} = V_{straight} + V_{call\ on\ stock} - V_{issuer\ call}$$

## 5. Pricing bonds with embedded options

A single yield cannot price an option, because the option's value depends on how rates **might** move. The standard tool is a **binomial interest rate tree**: rates branch up or down each period, the bond is valued backward from maturity, and at each exercise date the option holder's choice is applied.

**The rule at each exercise node**

$$V_{callable} = \min\left(V_{continue},\ CP\right) \qquad V_{putable} = \max\left(V_{continue},\ PP\right)$$

$$V_{continue} = \frac{\tfrac{1}{2}\left(V_{up} + C\right) + \tfrac{1}{2}\left(V_{down} + C\right)}{1 + r_{node}}$$

**Worked example.** A 3-year, 5% annual-coupon bond. It is callable (or putable) at 100 only at the end of year 2, after that year's coupon. Up and down moves each have probability ½. The tree is illustrative; in practice it is calibrated so it reprices on-the-run Treasuries exactly.

| Date | Rates at each node |
| --- | --- |
| Today | 3.0% |
| Year 1 | 4.5% (up), 2.5% (down) |
| Year 2 | 6.0% (up-up), 4.0% (up-down), 2.0% (down-down) |

**Year 2 (values before the option, ex-coupon):** 105 ÷ (1 + r) at each node.

| Year 2 node | Rate | Straight | Callable (min with 100) | Putable (max with 100) |
| --- | --- | --- | --- | --- |
| Up-up | 6.0% | 99.057 | 99.057 | **100.000** (put) |
| Up-down | 4.0% | 100.962 | **100.000** (called) | 100.962 |
| Down-down | 2.0% | 102.941 | **100.000** (called) | 102.941 |

**Year 1 (ex-coupon), then today:**

| Node | Straight | Callable | Putable |
| --- | --- | --- | --- |
| Year 1 up (4.5%) | 100.487 | 100.027 | 100.939 |
| Year 1 down (2.5%) | 104.343 | 102.439 | 104.343 |
| **Today (3.0%)** | **104.286** | **103.139** | **104.505** |

- Value of the issuer's call = 104.286 − 103.139 = **1.147**.
- Value of the investor's put = 104.505 − 104.286 = **0.219**. The put is worth less because only one node puts it in the money.

**Effective duration and convexity.** Shift every rate in the tree ±25 bp and reprice (formulas from Study Guide 5):

| Bond | Price | Effective duration | Effective convexity |
| --- | --- | --- | --- |
| Straight | 104.286 | 2.77 | 10.5 |
| Callable | 103.139 | 2.10 | 6.7 |
| Putable | 104.505 | 2.56 | 9.3 |

Both options shorten duration: the call caps the price when rates fall, the put floors it when rates rise. The callable's convexity drops; with more of the tree near the call price (lower rates or a finer tree) it turns negative.

**Volatility matters.** Higher rate volatility makes any option more valuable: a callable's price falls and a putable's price rises. A straight bond's value does not depend on volatility.

## 6. Spreads: Z-spread and OAS

- **Z-spread:** the constant spread over the spot (zero) curve that makes the discounted cash flows equal the price, ignoring the option.
- **Option-adjusted spread (OAS):** the constant spread added to every rate in the tree so the model price equals the market price. It is the spread for credit and liquidity with the option removed, which makes callable, putable and straight bonds comparable.

$$\text{Option cost} = Z\text{-spread} - OAS$$

For a callable the option cost is positive (OAS < Z-spread: part of the extra yield just pays for the call). For a putable it is negative (OAS > Z-spread).

## 7. Summary: what the option changes

| | Callable | Putable | Convertible |
| --- | --- | --- | --- |
| Who owns the option | Issuer | Investor | Investor (a call on the stock) |
| Price vs straight bond | Lower | Higher | Higher |
| Yield vs straight bond | Higher | Lower | Much lower |
| Yield to quote | Yield to worst | YTM and yield to put | YTM plus conversion premium |
| Effective duration | Shorter, especially when rates fall | Shorter, especially when rates rise | Depends on the stock; low when equity-like |
| Convexity | Can turn negative | Positive, enhanced | Positive equity convexity |
| More volatility | Price falls | Price rises | Price rises |
| Right valuation tool | Tree or OAS model | Tree or OAS model | Two-factor (rates and stock) or equity option model |

## 8. Tools

**TI BA II Plus Professional**

- Yield to call: `2nd` `BOND`; set RDT to the call date and RV to the call price (for example 101), enter PRI = 105, then `CPT` YLD → **4.067**.
- Yield to put: same steps with the put date and put price (RV = 100), PRI = 97 → **6.110**.
- Tree node values: 105 `÷` 1.06 `=` → 99.057, and so on backward through the tree.

**HP 12C**

- Yield to call (the bond functions assume redemption at 100, so use TVM): 10 `n` · 105 `CHS` `PV` · 2.5 `PMT` · 101 `FV` · `i` 2 `×` → **4.067**.
- Yield to put: 6 `n` · 97 `CHS` `PV` · 2.5 `PMT` · 100 `FV` · `i` 2 `×` → **6.110**.

**Excel**

| Task | Formula | Result |
| --- | --- | --- |
| Yield to call | `=YIELD(DATE(2026,11,15),DATE(2031,11,15),5%,105,101,2,1)` | 4.067% |
| Yield to put | `=YIELD(DATE(2026,11,15),DATE(2029,11,15),5%,97,100,2,1)` | 6.110% |
| Call payoff | `=MAX(S-K,0)` | |
| Conversion value | `=share_price*conversion_ratio` | \$900 |
| Conversion premium | `=(price-conv_value)/conv_value` | 11.1% |

A small tree fits in a worksheet: one column per date, each cell `=MIN((0.5*(up+C)+0.5*(down+C))/(1+r),CP)` for a callable node (MAX with the put price for a putable node).

**Python: binomial tree (tested; output 104.286, 103.139, 104.505 and durations 2.77, 2.10, 2.56)**

```python
def tree_price(rates, cpn=5.0, face=100.0, kind="straight", strike=100.0, exercise=(2,), shift=0.0):
    values = [face + cpn] * (len(rates) + 1)           # cash at maturity
    for t in reversed(range(len(rates))):
        step = []
        for i, r in enumerate(rates[t]):
            v = 0.5 * (values[i] + values[i + 1]) / (1 + r + shift)
            if t in exercise and kind == "callable": v = min(v, strike)
            if t in exercise and kind == "putable":  v = max(v, strike)
            step.append(v + (cpn if t > 0 else 0.0))    # add coupon paid at t
        values = step
    return values[0]

rates = [[0.03], [0.045, 0.025], [0.06, 0.04, 0.02]]
for kind in ("straight", "callable", "putable"):
    p = tree_price(rates, kind=kind)
    pm = tree_price(rates, kind=kind, shift=-0.0025)
    pp = tree_price(rates, kind=kind, shift=0.0025)
    print(kind, round(p, 3), round((pm - pp) / (2 * p * 0.0025), 2))
```

**Python: QuantLib callable bond (tested).** A 10-year 5% bond, callable at par on each coupon date after year 5, on a flat 4.5% curve with a Hull-White rate model (mean reversion 3%, volatility 1%). Output: straight 103.991, callable 99.868, so the call is worth about 4.12.

```python
import QuantLib as ql
today = ql.Date(15, ql.November, 2026)
ql.Settings.instance().evaluationDate = today
curve = ql.YieldTermStructureHandle(ql.FlatForward(today, 0.045, ql.ActualActual(ql.ActualActual.Bond),
                                                   ql.Compounded, ql.Semiannual))
sched = ql.Schedule(today, ql.Date(15, ql.November, 2036), ql.Period(ql.Semiannual), ql.NullCalendar(),
                    ql.Unadjusted, ql.Unadjusted, ql.DateGeneration.Backward, False)
dc = ql.ActualActual(ql.ActualActual.Bond, sched)
calls = ql.CallabilitySchedule()
for d in sched:
    if ql.Date(15, ql.November, 2031) <= d < ql.Date(15, ql.November, 2036):
        calls.append(ql.Callability(ql.BondPrice(100.0, ql.BondPrice.Clean), ql.Callability.Call, d))
callable_bond = ql.CallableFixedRateBond(0, 100.0, sched, [0.05], dc, ql.Following, 100.0, today, calls)
callable_bond.setPricingEngine(ql.TreeCallableFixedRateBondEngine(ql.HullWhite(curve, 0.03, 0.01), 200))
straight = ql.FixedRateBond(0, 100.0, sched, [0.05], dc)
straight.setPricingEngine(ql.DiscountingBondEngine(curve))
print(straight.cleanPrice(), callable_bond.cleanPrice())
```

Change the volatility from 0.01 to 0.02 and the callable's price falls: the call is worth more. Use `ql.Callability.Put` for a putable bond.

**Julia (same logic as the tested Python tree; not run here)**

```julia
function tree_price(rates; cpn = 5.0, face = 100.0, kind = :straight, strike = 100.0, exercise = (3,), shift = 0.0)
    values = fill(face + cpn, length(rates) + 1)
    for t in length(rates):-1:1
        step = Float64[]
        for (i, r) in enumerate(rates[t])
            v = 0.5 * (values[i] + values[i + 1]) / (1 + r + shift)
            t in exercise && kind == :callable && (v = min(v, strike))
            t in exercise && kind == :putable  && (v = max(v, strike))
            push!(step, v + (t > 1 ? cpn : 0.0))
        end
        values = step
    end
    values[1]
end

rates = [[0.03], [0.045, 0.025], [0.06, 0.04, 0.02]]
tree_price(rates; kind = :callable)    # 103.139
```

Julia arrays start at 1, so year 2 is index 3 in `exercise`.

## 9. Practice set

1. You buy a call with strike 50 for a premium of 3. The stock ends at 58. Payoff and profit? *Payoff 8, profit 5.*
2. A 10-year 6% semiannual bond trades at 103 and is callable at par in 5 years. Find YTM, YTC and YTW. *5.604%, 5.309%; YTW = 5.309%.*
3. Rework the tree example with a call price of 101. *Callable value 103.827; the higher call price makes the call less valuable.*
4. A straight bond is worth 102.50 and the otherwise identical callable 99.80. Value of the call? *2.70.*
5. A convertible has conversion ratio 20, the stock trades at \$55, the straight value is \$950 and the market price is \$1,150. Find conversion value, minimum value and conversion premium. *\$1,100; \$1,100; 4.5%.*
6. A bond's Z-spread is 150 bp and its OAS 110 bp. What is the option cost, and is the bond more likely callable or putable? *40 bp; callable.*

## 10. CFA-style review questions

Original questions in the CFA Level I format (three choices, one correct). Not CFA Institute material.

1. The investor in a callable bond is effectively:
   - A. long a call option on the bond
   - B. short a call option on the bond
   - C. long a put option on the bond
2. If interest rate volatility increases, the value of a callable bond most likely:
   - A. increases
   - B. decreases
   - C. is unchanged
3. A straight bond is worth 101.40 and the embedded put is worth 1.20. The putable bond's value is:
   - A. 100.20
   - B. 101.40
   - C. 102.60
4. As interest rates fall well below its coupon rate, a callable bond's price will most likely:
   - A. rise without limit, like a straight bond
   - B. rise more slowly and flatten near the call price
   - C. fall
5. A convertible bond has conversion ratio 40 and a straight value of \$820; the stock trades at \$22. Its minimum value is:
   - A. \$820
   - B. \$880
   - C. \$1,000
6. A bond has a Z-spread of 120 bp and an OAS of 90 bp. It is most likely:
   - A. callable
   - B. putable
   - C. option-free
7. When rates are low, a callable bond's effective duration compared with its modified duration is:
   - A. lower
   - B. the same
   - C. higher

**Answer key**

1. B. The issuer owns the call; the investor has sold it.
2. B. A more valuable call is subtracted from the straight value.
3. C. 101.40 + 1.20 = 102.60.
4. B. Negative convexity: the call caps the price.
5. B. Conversion value 40 × \$22 = \$880 exceeds the straight value.
6. A. A positive option cost (30 bp) means the investor is short an option.
7. A. Modified duration ignores the likely call, which shortens the bond's effective life.

## 11. Bloomberg Terminal exercises (draft: verify on the campus Terminal)

| Command | What to do | Check against this guide | Verified |
| --- | --- | --- | --- |
| `OMON <GO>`, `OV <GO>` | Equity option monitor and option valuation: view calls and puts, strikes, premiums | Section 1: payoffs, moneyness, volatility | ☐ |
| `SRCH <GO>` | Find corporate bonds that are callable, putable or convertible (use the call, put and convertible filters) | Sections 2–4 | ☐ |
| `DES <GO>` | Read the call or put schedule, call protection and make-whole terms | Sections 2 and 3 | ☐ |
| `YAS <GO>` | Read YTM, yield to call, yield to worst and the workout date | Section 2: YTW | ☐ |
| `OAS1 <GO>` | Read OAS, option value, effective duration and convexity; change the volatility input and watch the price | Sections 5 and 6 | ☐ |
| `OVCV <GO>` (confirm) | Convertible valuation: conversion value, premium, bond floor | Section 4 | ☐ |

Confirm Excel field names for yield to worst, OAS and conversion premium with `FLDS <GO>`.

**Exercise:** pick a callable corporate bond. In `OAS1`, record the OAS and option value at the default volatility, then at volatility 5 points higher. Explain the change in price using section 5.

## 12. Reading in Bodie, Kane & Marcus, *Investments*, 13th ed. (2024)

| Section | Topic in the book | Supports |
| --- | --- | --- |
| 2.5 Derivative Markets | Options; Futures Contracts | Section 1: the options review |
| 20.1 The Option Contract | Options trading; American and European options | Section 1 |
| 20.2 Values of Options at Expiration | Call and put payoffs | Section 1: payoff formulas |
| 20.5 Option-like Securities | Callable Bonds; Convertible Securities | Sections 2 and 4 |
| 14.1 Bond Characteristics | Corporate Bonds: call provisions, convertible bonds, puttable bonds | Sections 2–4 |
| 14.3 Bond Yields | Yield to Call | Section 2: YTC and YTW |
| 16.2 Convexity | Duration and Convexity of Callable Bonds | Sections 5 and 7: negative convexity |
| Chapter 21 Option Valuation | Binomial option pricing | Section 5: backward induction in a tree |
