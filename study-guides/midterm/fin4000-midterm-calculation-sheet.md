---
title: "FIN 4000 Midterm Calculation Sheet"
subtitle: "Formulas, variable definitions and worked examples for Chapters 2, 3, 4, 14, 15 and 16"
---

# FIN 4000 Investments: Midterm Calculation Sheet

This sheet collects every calculation used in the midterm and practice questions. Notation follows Bodie, Kane and Marcus (BKM). Each formula is followed by a definition of every symbol and a worked example. The examples use their own numbers, so they are not midterm or practice questions. Chapters 1 and 5 contain no calculations (they are conceptual questions), so they do not appear here.

**Conventions used throughout**

- Rates are written as decimals inside formulas (for example, 5% is $0.05$) and as percentages in the worked examples.
- Unless a question says otherwise, interest compounds once a year, and coupon bonds have a face value (par value) of \$1,000.
- Round only at the end of a calculation; intermediate rounding can change the last digit of your answer.


## Calculator setup: TI BA II Plus

Do these once before the exam, and check them whenever a result looks odd.

| Setting | Keys | Why |
|---|---|---|
| Show more decimals | `2ND` `FORMAT` `9` `ENTER` `2ND` `QUIT` | Shows 9 decimal places so you can round only at the end |
| One payment per year | `2ND` `P/Y` `1` `ENTER` `2ND` `QUIT` | Makes `I/Y` an annual rate and `N` a count of years. For semiannual problems, either keep $P/Y = 1$ and use $N = 2T$ with the per-period rate, or set $P/Y = 2$. |
| Clear the time value of money registers | `2ND` `CLR TVM` | Run before every new TVM problem |
| Payments at period end | `2ND` `BGN` shows `END` (if it shows `BGN`, press `2ND` `SET`, then `2ND` `QUIT`) | Bond coupons are paid at the end of each period |
| Clear the memories | `2ND` `MEM` `2ND` `CLR WORK` | Memories `STO 1`–`STO 9` are used below to hold intermediate results |

**Reading the key notation.** A key written in backticks is pressed once. `CPT` followed by a TVM key (`N`, `I/Y`, `PV`, `PMT`, `FV`) solves for that register. In the TVM registers, money you pay out is negative and money you receive is positive, so a bond's `PV` is entered with `+/-` and the other cash flows are positive. `I/Y` is entered as a percent (type `5` for 5%). `y^x` is the power key, and `1/x` is the reciprocal key. Results shown in the **Display** lines are rounded.

---

## Chapter 2: Asset Classes and Financial Instruments

### 2.1 Tax-equivalent yield

Restate a tax-free municipal yield as the taxable yield that leaves the investor with the same amount after tax:

$$
r_{TEY} = \frac{r_{muni}}{1 - t}
$$

The after-tax yield of a taxable bond, and the tax rate at which the two bonds are equally attractive, are:

$$
r_{AT} = r_{taxable}\,(1 - t) \qquad\qquad t^{*} = 1 - \frac{r_{muni}}{r_{taxable}}
$$

| Symbol | Definition |
|---|---|
| $r_{TEY}$ | Tax-equivalent yield: the taxable yield that matches the municipal bond after tax |
| $r_{muni}$ | Yield of the municipal bond (free of federal income tax), as a decimal |
| $r_{taxable}$ | Yield of the taxable bond, as a decimal |
| $r_{AT}$ | After-tax yield of the taxable bond |
| $t$ | Investor's marginal federal income tax rate, as a decimal |
| $t^{*}$ | Break-even tax rate: above it the municipal bond is better, below it the taxable bond is better |

**Example.** A municipal bond yields 4.20% and the investor's tax rate is 22%. Then $r_{TEY} = 4.20\% / (1 - 0.22) = 5.38\%$. A taxable bond yielding 5.50% at a 30% tax rate leaves $r_{AT} = 5.50\% \times (1 - 0.30) = 3.85\%$ after tax. The break-even tax rate between the two bonds is $t^{*} = 1 - 4.20/5.50 = 23.64\%$.

**TI BA II Plus.** (Plain arithmetic; no TVM keys.)

| Step | Keys | Display |
|---|---|---|
| Tax-equivalent yield | `4.20` `÷` `(` `1` `−` `0.22` `)` `=` | 5.3846 |
| After-tax yield | `5.50` `×` `(` `1` `−` `0.3` `)` `=` | 3.8500 |
| Break-even tax rate (as a percent) | `1` `−` `4.20` `÷` `5.50` `=` `×` `100` `=` | 23.6364 |

---

## Chapter 3: How Securities Are Traded

### 3.1 Rate of return on a margin purchase

The investor puts up equity, borrows the rest, and measures the return on the equity:

$$
E = m_0\,N\,P_0 \qquad L = N\,P_0 - E \qquad I = i\,L
$$

$$
r_{margin} = \frac{N\,(P_1 - P_0) + N\,D - I}{E}
$$

| Symbol | Definition |
|---|---|
| $r_{margin}$ | Rate of return on the investor's own money for the holding period |
| $N$ | Number of shares purchased |
| $P_0$ | Purchase price per share |
| $P_1$ | Selling price per share at the end of the period |
| $D$ | Dividend per share received during the period |
| $m_0$ | Initial margin requirement: the fraction of the purchase paid with the investor's own money |
| $E$ | Equity: the investor's own money invested |
| $L$ | Loan from the broker |
| $i$ | Interest rate on the loan |
| $I$ | Dollar interest paid on the loan for the period |

**Example.** An investor buys $300 shares at \$20.00 with 50% initial margin, borrowing at 7%. The stock pays a \$0.40 dividend and is sold at \$24.00 after one year. Cost = \$6,000, equity $E$ = \$3,000, loan $L$ = \$3,000, interest $I$ = \$210. Price gain = \$1,200, dividends = \$120. Net profit = \$1,110, so $r_{margin} = 1,110 / 3,000 = 37.00\%$.

**TI BA II Plus.** (Plain arithmetic. The parentheses keys `(` and `)` are above the number pad.)

| Step | Keys | Display |
|---|---|---|
| Equity $E$ | `0.5` `×` `300` `×` `20` `=` `STO` `1` | 3,000 |
| Loan $L$ | `300` `×` `20` `−` `RCL` `1` `=` `STO` `2` | 3,000 |
| Interest $I$ | `RCL` `2` `×` `0.07` `=` `STO` `3` | 210 |
| Net profit | `300` `×` `(` `24` `−` `20` `)` `+` `300` `×` `0.4` `−` `RCL` `3` `=` | 1,110 |
| Return $r_{margin}$ (as a percent) | `÷` `RCL` `1` `=` `×` `100` `=` | 37.00 |

### 3.2 Stock price that triggers a margin call

The loan does not change while the price falls, so only the equity shrinks. A margin call occurs when equity as a fraction of the stock's current value falls to the maintenance margin:

$$
\frac{P\,N - L}{P\,N} = m \quad\Longrightarrow\quad P_{call} = \frac{L / N}{1 - m}
$$

| Symbol | Definition |
|---|---|
| $P_{call}$ | Stock price at or below which the broker issues a margin call |
| $P$ | Current stock price per share |
| $N$ | Number of shares |
| $L$ | Amount borrowed from the broker (constant while the price moves) |
| $L/N$ | Loan per share, equal to $P_0\,(1 - m_0)$ |
| $m$ | Maintenance margin: the minimum equity as a fraction of the stock's market value |
| $m_0$ | Initial margin requirement |
| $P_0$ | Purchase price per share |

**Example.** A stock is bought at \$60.00 with 55% initial margin and a 30% maintenance margin (ignore interest and dividends). The loan per share is $L/N = 60 \times (1 - 0.55) = \$27.00$, so $P_{call} = 27.00 / (1 - 0.30) = \$38.57$.

**TI BA II Plus.**

| Step | Keys | Display |
|---|---|---|
| Loan per share $L/N$ | `60` `×` `(` `1` `−` `0.55` `)` `=` | 27.00 |
| Margin call price $P_{call}$ | `÷` `(` `1` `−` `0.3` `)` `=` | 38.57 |

The second step continues from the first display, so do not press `CE|C` in between.

### 3.3 Rate of return on a short sale

The short seller sells borrowed shares, buys them back later, owes any dividends to the lender, and posts margin as equity:

$$
E = m_0\,N\,P_0 \qquad\qquad r_{short} = \frac{N\,(P_0 - P_1) - N\,D}{E}
$$

The most a short seller can gain is $N\,P_0$ (the price cannot fall below zero). The loss has no upper limit because the price can rise without limit.

| Symbol | Definition |
|---|---|
| $r_{short}$ | Rate of return on the margin posted for the holding period |
| $N$ | Number of shares sold short |
| $P_0$ | Price at which the shares are sold short |
| $P_1$ | Price at which the shares are bought back |
| $D$ | Dividend per share paid to the lender while the position is open |
| $m_0$ | Initial margin as a fraction of the value of the short position |
| $E$ | Equity posted as margin |

**Example.** 300 shares are sold short at \$25.00 with 50% margin. During the year a \$0.30 dividend is paid, and the shares are bought back at \$20.00. Equity $E$ = \$3,750. Gain on price = \$1,500, dividends owed = \$90, net profit = \$1,410, so $r_{short} = 1,410 / 3,750 = 37.60\%$.

**TI BA II Plus.**

| Step | Keys | Display |
|---|---|---|
| Equity $E$ | `0.5` `×` `300` `×` `25` `=` `STO` `1` | 3,750 |
| Net profit | `300` `×` `(` `25` `−` `20` `)` `−` `300` `×` `0.3` `=` | 1,410 |
| Return $r_{short}$ (as a percent) | `÷` `RCL` `1` `=` `×` `100` `=` | 37.60 |
| Maximum possible gain | `300` `×` `25` `=` | 7,500 |

There is no key sequence for the maximum loss because it has no upper limit.

---

## Chapter 4: Mutual Funds

### 4.1 Ending value of a fund investment after loads and expenses

A fund's annual expense ratio reduces the return every year. A front-end load is deducted once at purchase. A back-end load is deducted once at sale (and is often zero after a number of years). The questions use the approximation that net annual return equals gross return minus the expense ratio:

$$
V_T = V_0\,(1 - \ell)\,(1 + g - e)^{T}\,(1 - c_T)
$$

Set $\ell = 0$ and $c_T = 0$ for a no-load fund. The fund with the larger ending value had the smaller total fee drag.

| Symbol | Definition |
|---|---|
| $V_T$ | Value of the investment after $T$ years |
| $V_0$ | Amount invested |
| $\ell$ | Front-end load, as a fraction of the amount invested (0 if none) |
| $c_T$ | Back-end load charged at sale after $T$ years, as a fraction of the value (0 if none or if the schedule has expired) |
| $g$ | Annual gross return before expenses |
| $e$ | Annual expense ratio (including any 12b-1 fee) |
| $T$ | Number of years held |

**Example.** \$10,000 is invested for 5 years with a gross return of 6%. A no-load fund with expenses of 1.50% ends at $V_T = 10,000 \times (1 + 0.06 - 0.015)^{5} = \$12,461.82$. A fund with a 4% front-end load and 0.80% expenses ends at $V_T = 10,000 \times (1 - 0.04) \times (1 + 0.06 - 0.008)^{5} = \$12,369.44$. Over this horizon the front-end load fund has the larger fee drag.

**TI BA II Plus (time value of money).** Treat the net annual return $g - e$ as the interest rate. Use a negative `PV` for the amount that goes into the fund after any front-end load. Press `2ND` `CLR TVM` before each fund.

| Step | Keys | Display |
|---|---|---|
| No-load fund | `5` `N`  `4.5` `I/Y`  `-10000` `PV`  `0` `PMT`  `CPT` `FV` | 12,461.82 |
| Front-end load fund: amount invested after load | `10000` `×` `(` `1` `−` `0.04` `)` `=` | 9,600.00 |
| Front-end load fund: ending value | `2ND` `CLR TVM`  `5` `N`  `5.2` `I/Y`  `+/-` `PV` (uses the display above)  `0` `PMT`  `CPT` `FV` | 12,369.44 |

For a back-end load, take `FV` and then multiply by $(1 - c_T)$: `×` `(` `1` `−` `c` `)` `=`.

---

## Chapter 14: Bond Prices and Yields

### 14.1 Coupon interest

$$
\text{Annual interest} = F \times c \qquad\qquad C = \frac{F \times c}{n}
$$

| Symbol | Definition |
|---|---|
| $F$ | Face (par) value of the bond |
| $c$ | Annual coupon rate, as a decimal |
| $n$ | Number of coupon payments per year (1 annual, 2 semiannual, 4 quarterly) |
| $C$ | Dollar amount of one coupon payment |

**Example.** A bond has face value \$2,000 and a 5.5% coupon paid semiannually. Annual interest = \$2,000 $\times$ 0.055 = \$110, and each payment is $C$ = \$55.

**TI BA II Plus.**

| Step | Keys | Display |
|---|---|---|
| Annual interest | `2000` `×` `0.055` `=` | 110.00 |
| Payment per period | `÷` `2` `=` | 55.00 |

### 14.2 Free cash flow

$$
FCF = CFO - CapEx
$$

| Symbol | Definition |
|---|---|
| $FCF$ | Free cash flow: cash left after the investment needed to maintain and grow the business |
| $CFO$ | Cash flow from operations |
| $CapEx$ | Capital expenditures (spending on equipment, buildings and other long-lived assets) |

**Example.** Cash from operations is \$8.0 billion and capital spending is \$5.5 billion, so $FCF = 8.0 - 5.5 = \$2.5$ billion. A negative result means investment exceeded the cash the operations produced.

**TI BA II Plus.**

| Step | Keys | Display |
|---|---|---|
| Free cash flow | `8.0` `−` `5.5` `=` | 2.50 |

### 14.3 Day count and accrued interest

$$
AI = C \times \frac{d}{D}
$$

The convention decides how the days $d$ and $D$ are counted:

- **30/360** (U.S. corporate and municipal bonds): every month has 30 days and every year has 360 days.

$$
d = 360\,(Y_2 - Y_1) + 30\,(M_2 - M_1) + (D_2 - D_1)
$$

  If a date falls on the 31st, treat it as the 30th. Under 30/360 a six-month coupon period always has $D = 180$.
- **Actual/actual** (U.S. Treasury notes and bonds): $d$ is the real number of days since the last coupon and $D$ is the real number of days in the coupon period.
- **Actual/360** (money market instruments): $d$ is the real number of days elapsed and the year is taken as 360 days.

| Symbol | Definition |
|---|---|
| $AI$ | Accrued interest: the part of the next coupon already earned by the seller |
| $C$ | Dollar amount of one coupon payment |
| $d$ | Days from the last coupon date to the settlement date (counted by the convention) |
| $D$ | Days in the full coupon period (counted by the convention) |
| $Y_1, M_1, D_1$ | Year, month and day of the earlier date (last coupon) |
| $Y_2, M_2, D_2$ | Year, month and day of the later date (settlement) |

**Example (30/360).** A 6% semiannual bond with \$1,000 face has $C$ = \$30. The last coupon was paid on February 10 and the trade settles on July 25 of the same year. Then $d = 30\,(7 - 2) + (25 - 10) = 165$, and $AI = 30 \times 165/180 = \$27.50$.

**Example (actual/actual).** The last coupon was paid on January 15, the trade settles on April 10, and the next coupon is due July 15 of the same year. Real days: $d = 85$ and $D = 181$, so $AI = 30 \times 85/181 = \$14.09$.

**TI BA II Plus (date worksheet).** The calculator counts days between two dates, and you choose the convention.

1. Open the worksheet: `2ND` `DATE`. Dates are typed as month.dayyear (month and day, then the two-digit year), so February 10, 2027 is `2.1027`.
2. `DT1` = first date, then `ENTER` `↓`. `DT2` = second date, then `ENTER` `↓`.
3. At `ACT`/`360`, press `2ND` `SET` to toggle between **ACT** (actual days) and **360** (30/360). Leave it on the one you need.
4. At `DBD` press `CPT` to get the number of days.
5. Multiply: coupon `×` days `÷` days in the period `=` to get $AI$.

| Case | Entries | `DBD` shows | Then |
|---|---|---|---|
| 30/360 days since the last coupon ($d$) | `DT1` = `2.1027`, `DT2` = `7.2527`, set to `360`, `CPT` | 165 | `30` `×` `165` `÷` `180` `=` shows 27.50 |
| Actual days since the last coupon ($d$) | `DT1` = `1.1527`, `DT2` = `4.1027`, set to `ACT`, `CPT` | 85 | (keep this number) |
| Actual days in the coupon period ($D$) | `DT1` = `1.1527`, `DT2` = `7.1527`, `CPT` | 181 | `30` `×` `85` `÷` `181` `=` shows 14.09 |

Under 30/360 a semiannual coupon period is always 180 days, so you can type `180` directly.

### 14.4 Bond price from a yield

$$
P = \sum_{t=1}^{T} \frac{C}{(1 + y)^{t}} + \frac{F}{(1 + y)^{T}} = C\,\frac{1 - (1 + y)^{-T}}{y} + \frac{F}{(1 + y)^{T}}
$$

| Symbol | Definition |
|---|---|
| $P$ | Bond price (the present value of its cash flows) |
| $C$ | Coupon payment per period |
| $F$ | Face (par) value, paid at maturity |
| $y$ | Yield to maturity per period, as a decimal |
| $T$ | Number of periods until maturity |
| $t$ | Period in which a cash flow is received |

**Example.** A 4-year bond pays a 5% annual coupon (\$50) on \$1,000 face and the yield is 6%. $P = 50/1.06 + 50/1.06^2 + 50/1.06^3 + 1{,}050/1.06^4 = \$965.35$.

**TI BA II Plus (time value of money).** Solve for `PV` and ignore its sign.

| Step | Keys | Display |
|---|---|---|
| Clear | `2ND` `CLR TVM` | |
| Enter the bond | `4` `N`  `6` `I/Y`  `50` `PMT`  `1000` `FV` | |
| Solve for price | `CPT` `PV` | -965.35 (the price is 965.35; the sign only shows it is a cash outflow) |

For a semiannual bond, use $N = 2T$, $I/Y = y/2$ and the semiannual coupon, or set $P/Y = 2$ and enter $N$ in years times 2.

### 14.5 Flat (clean) price and full (invoice) price

$$
P_{full} = P_{flat} + AI
$$

| Symbol | Definition |
|---|---|
| $P_{flat}$ | Quoted (clean) price, without accrued interest |
| $P_{full}$ | Invoice (dirty) price the buyer actually pays |
| $AI$ | Accrued interest from section 14.3 |

**Example.** If the quoted price is \$965.35 and accrued interest is \$27.50, the buyer pays \$992.85.

**TI BA II Plus.**

| Step | Keys | Display |
|---|---|---|
| Full price | `965.35` `+` `27.50` `=` | 992.85 |

To find the flat price from a full price, subtract: full price `−` accrued interest `=`.

### 14.6 Yield to maturity (YTM)

The yield to maturity is the single discount rate $y$ that makes the present value of the bond's promised cash flows equal its price:

$$
P = \sum_{t=1}^{T} \frac{CF_t}{(1 + y)^{t}}
$$

It has no closed form for more than one period, so solve it with a calculator or by trial and error.

| Symbol | Definition |
|---|---|
| $P$ | Current price of the bond |
| $CF_t$ | Cash flow in period $t$ (coupon, plus face value in the last period) |
| $y$ | Yield to maturity per period |
| $T$ | Number of periods to maturity |

**TI BA II Plus (time value of money keys).** Set one payment per year (annual coupons): `2ND` `P/Y` `1` `ENTER` `2ND` `QUIT`. Clear with `2ND` `CLR TVM`. Enter `N` = number of periods, `PV` = price entered as a negative number (`+/-`), `PMT` = coupon, `FV` = face value, then press `CPT` `I/Y`. For semiannual coupons use $N = 2T$, the semiannual coupon, and double the answer to quote an annual rate.

**Example.** A 3-year bond with a 7% annual coupon sells for \$1,024.00. Keys: `N` = 3, `PV` = −1,024.00, `PMT` = 70, `FV` = 1000, `CPT` `I/Y` gives YTM = 6.10%.

**Compare with a yield you were given.** To check a YTM answer, enter `N`, `PMT`, `FV` and the YTM in `I/Y`, then `CPT` `PV`. If the result equals the price (ignoring the sign), the YTM is right.

---

## Chapter 15: The Term Structure of Interest Rates

### 15.1 Spot rates from a Treasury bill and a coupon bond (bootstrapping)

A 6-month Treasury bill pays only $F$ at month 6, so its price gives the first spot rate directly. The one-year bond's first coupon is then discounted at that rate, and what remains of the price is the present value of the final payment:

$$
1 + z_1 = \frac{F}{P_{bill}} \qquad y_1 = 2\,z_1
$$

$$
(1 + z_2)^2 = \frac{C + F}{P_{bond} - \dfrac{C}{1 + z_1}} \qquad y_2 = 2\,z_2
$$

| Symbol | Definition |
|---|---|
| $P_{bill}$ | Price of the 6-month Treasury bill |
| $P_{bond}$ | Price of the 1-year coupon bond |
| $F$ | Face value (\$1,000) |
| $C$ | Semiannual coupon payment of the bond |
| $z_1$ | 6-month spot rate for one 6-month period |
| $z_2$ | 12-month spot rate per 6-month period (the rate earned each half year over the full year) |
| $y_1,\;y_2$ | Annual spot rates on a bond-equivalent basis (the 6-month rate times 2) |

**Example.** A 6-month bill sells for \$965.00. A 1-year bond with a 7% coupon, paid semiannually (\$35 each), sells for \$1,010.00. Then $z_1 = 1000/965.00 - 1 = 3.627\%$ and $y_1 = 7.25\%$. The first coupon is worth $35/1.03627 = \$33.78$, leaving \$976.23. So $(1 + z_2)^2 = 1,035/976.23 = 1.06021$, $z_2 = 2.966\%$ and $y_2 = 5.93\%$.

**TI BA II Plus.** Use TVM for each spot rate. The answers are per 6-month period, so multiply by 2 for the bond-equivalent annual rate.

| Step | Keys | Display |
|---|---|---|
| $z_1$: clear, then enter the bill | `2ND` `CLR TVM`  `1` `N`  `-965.00` `PV` (type `965.00` then `+/-`)  `0` `PMT`  `1000` `FV`  `CPT` `I/Y` | 3.6269 |
| $y_1 = 2 z_1$ | `×` `2` `=` | 7.2539 |
| Present value of the first coupon | `35` `÷` `(` `1` `+` `0.036269` `)` `=` (use the unrounded $z_1$: `RCL` it from memory if you stored it) | 33.7750 |
| What remains of the bond price | `1010` `−` (the value above) `=` | 976.2250 |
| $z_2$: clear, then enter the final payment | `2ND` `CLR TVM`  `2` `N`  `976.2250` `+/-` `PV`  `0` `PMT`  `1035` `FV`  `CPT` `I/Y` | 2.9663 |
| $y_2 = 2 z_2$ | `×` `2` `=` | 5.9326 |

Tip: after the first `CPT` `I/Y`, press `STO` `1` to keep $z_1$ (in percent). Later, `RCL` `1` `÷` `100` `+` `1` gives $1 + z_1$.

### 15.2 Forward rates and discount factors

The forward rate for year $n$ is the rate that, applied to year $n$, links the $(n-1)$-year and $n$-year spot rates:

$$
(1 + y_n)^n = (1 + y_{n-1})^{n-1}\,(1 + f_n) \quad\Longrightarrow\quad f_n = \frac{(1 + y_n)^n}{(1 + y_{n-1})^{n-1}} - 1
$$

Discount factors are built by chaining the forward rates:

$$
DF_1 = \frac{1}{1 + f_1} \qquad DF_n = \frac{DF_{n-1}}{1 + f_n} = \frac{1}{(1 + y_n)^n}
$$

| Symbol | Definition |
|---|---|
| $y_n$ | Spot rate (yield on an $n$-year zero-coupon bond), as an annual rate |
| $f_n$ | One-year forward rate for year $n$ (the rate for the period from year $n-1$ to year $n$); $f_1 = y_1$ |
| $DF_n$ | Discount factor: the present value of \$1 received at the end of year $n$ |
| $n$ | Number of years |

**Example.** Spot rates are $y_1 = 4.0\%$, $y_2 = 4.8\%$ and $y_3 = 5.2\%$. Then $f_2 = 1.048^2/1.040 - 1 = 5.61\%$ and $f_3 = 1.052^3/1.048^2 - 1 = 6.00\%$. Discount factors: $DF_1 = 0.96154$, $DF_2 = 0.96154/(1 + 0.05606) = 0.91049$, $DF_3 = 0.91049/(1 + 0.06005) = 0.85892$.

**TI BA II Plus.** Spot rates are given in percent, so type them as decimals (for example, 4.8% is `0.048`).

| Step | Keys | Display |
|---|---|---|
| $f_2$ | `(` `1.048` `y^x` `2` `)` `÷` `1.04` `−` `1` `=` | 0.056062 |
| $f_3$ | `(` `1.052` `y^x` `3` `)` `÷` `(` `1.048` `y^x` `2` `)` `−` `1` `=` | 0.060046 |
| $DF_1$ | `1.04` `1/x` `STO` `1` | 0.96154 |
| $DF_2$ (chained) | `RCL` `1` `÷` `(` `1` `+` `0.056062` `)` `=` `STO` `2` | 0.91049 |
| $DF_3$ (chained) | `RCL` `2` `÷` `(` `1` `+` `0.060046` `)` `=` `STO` `3` | 0.85892 |
| Check $DF_3$ from the spot rate | `1.052` `y^x` `3` `=` `1/x` | 0.85892 |

### 15.3 Bond price from discount factors, then its YTM

$$
P = \sum_{t=1}^{T} CF_t \times DF_t
$$

Then solve the yield to maturity from section 14.6 using that price.

| Symbol | Definition |
|---|---|
| $P$ | Bond price |
| $CF_t$ | Cash flow in year $t$ (coupon, plus face value in the last year) |
| $DF_t$ | Discount factor for year $t$ from section 15.2 |
| $T$ | Years to maturity |

**Example.** Using the discount factors above, a 3-year bond with a 5% annual coupon (\$50) has $P = 50 \times 0.96154 + 50 \times 0.91049 + 1050 \times 0.85892 = \$995.47$. Keys: `N` = 3, `PV` = −995.47, `PMT` = 50, `FV` = 1000, `CPT` `I/Y` gives YTM = 5.17%.

**TI BA II Plus.** First the price from the stored discount factors, then the YTM from TVM.

| Step | Keys | Display |
|---|---|---|
| Price | `50` `×` `RCL` `1` `+` `50` `×` `RCL` `2` `+` `1050` `×` `RCL` `3` `=` `STO` `4` | 995.47 |
| YTM: clear, then enter the bond | `2ND` `CLR TVM`  `3` `N`  `RCL` `4` `+/-` `PV`  `50` `PMT`  `1000` `FV`  `CPT` `I/Y` | 5.1669 |

If your memories were cleared, recompute the discount factors from section 15.2 first.

---

## Chapter 16: Managing Bond Portfolios

### 16.1 Macaulay duration, modified duration and price change

$$
w_t = \frac{CF_t/(1 + y)^t}{P} \qquad D = \sum_{t=1}^{T} t\,w_t \qquad D^{*} = \frac{D}{1 + y}
$$

$$
\frac{\Delta P}{P} \approx -D^{*}\,\Delta y
$$

A zero-coupon bond's duration equals its maturity. The larger the duration, the more sensitive the price is to interest rate changes.

| Symbol | Definition |
|---|---|
| $w_t$ | Weight of period $t$: the present value of the cash flow in period $t$ as a fraction of the price |
| $CF_t$ | Cash flow in period $t$ |
| $y$ | Yield to maturity (annual) |
| $P$ | Price (present value) of the bond or liability |
| $D$ | Macaulay duration, in years |
| $D^{*}$ | Modified duration |
| $\Delta y$ | Change in yield, as a decimal |
| $\Delta P / P$ | Percentage change in price |

**Example.** A 3-year bond with a 6% annual coupon at a 5% yield has present values \$57.14, \$54.42 and \$915.67, so $P$ = \$1,027.23. The weights are 0.0556, 0.0530 and 0.8914, giving $D = 2.8358$ years and $D^{*} = 2.8358/1.05 = 2.7007$. If the yield rises 0.5 percentage points, $\Delta P/P \approx -2.7007 \times 0.005 = -1.35\%$.

**TI BA II Plus.** Get each present value with TVM, store them, then combine. (A cash-flow worksheet gives the price directly: `CF` `2ND` `CLR WORK`, `CF0` = `0`, `C01` = `60` with `F01` = `1`, `C02` = `60` with `F02` = `1`, `C03` = `1060` with `F03` = `1`, then `NPV`, `I` = `5`, `↓`, `CPT`, which shows 1,027.23.)

| Step | Keys | Display |
|---|---|---|
| PV of cash flow 1 | `2ND` `CLR TVM`  `1` `N`  `5` `I/Y`  `0` `PMT`  `60` `FV`  `CPT` `PV` `+/-` `STO` `1` | 57.1429 |
| PV of cash flow 2 | change `N` to `2`  `60` `FV`  `CPT` `PV` `+/-` `STO` `2` | 54.4218 |
| PV of cash flow 3 | change `N` to `3`  `1060` `FV`  `CPT` `PV` `+/-` `STO` `3` | 915.6679 |
| Price $P$ | `RCL` `1` `+` `RCL` `2` `+` `RCL` `3` `=` `STO` `4` | 1,027.2325 |
| Macaulay duration $D$ | `(` `1` `×` `RCL` `1` `+` `2` `×` `RCL` `2` `+` `3` `×` `RCL` `3` `)` `÷` `RCL` `4` `=` `STO` `5` | 2.8358 |
| Modified duration $D^{*}$ | `RCL` `5` `÷` `(` `1` `+` `0.05` `)` `=` `STO` `6` | 2.7007 |
| Price change for $\Delta y = +0.005$ (as a percent) | `RCL` `6` `×` `0.005` `=` `×` `100` `+/-` `=` | -1.3504 |

### 16.2 Convexity

Convexity corrects the duration estimate for large yield changes:

$$
Cx = \frac{1}{P\,(1 + y)^2}\sum_{t=1}^{T} \frac{CF_t}{(1 + y)^t}\,(t^2 + t)
\qquad
\frac{\Delta P}{P} \approx -D^{*}\,\Delta y + \tfrac{1}{2}\,Cx\,(\Delta y)^2
$$

| Symbol | Definition |
|---|---|
| $Cx$ | Convexity of the bond |
| $CF_t,\;y,\;P,\;t$ | As defined in section 16.1 |
| $D^{*}$ | Modified duration |
| $\Delta y$ | Change in yield, as a decimal |

**Example.** For the bond above, $Cx = 10.09$. For $\Delta y = +0.5$ percentage points, the duration-plus-convexity estimate is $\Delta P/P \approx -1.35\% + \tfrac{1}{2}(10.09)(0.005)^2 = -1.338\%$. The exact price change is -1.338%.

**TI BA II Plus.** This continues from section 16.1 and uses its stored present values (`STO` 1, 2, 3 and 4).

| Step | Keys | Display |
|---|---|---|
| Sum of $PV_t \times (t^2 + t)$ | `RCL` `1` `×` `2` `+` `RCL` `2` `×` `6` `+` `RCL` `3` `×` `12` `=` `STO` `7` | 11,428.8306 |
| Convexity $Cx$ | `RCL` `7` `÷` `(` `RCL` `4` `×` `1.1025` `)` `=` `STO` `8` | 10.0915 |
| Convexity term $\tfrac{1}{2}\,Cx\,(\Delta y)^2$ (as a percent) | `0.5` `×` `RCL` `8` `×` `0.005` `x²` `×` `100` `=` | 0.0126 |
| Duration plus convexity estimate (as a percent) | `RCL` `6` `×` `0.005` `×` `100` `+/-` `+` (the convexity term) `=` | -1.3377 |

Here $1.05^2 = 1.1025$ comes from $(1 + y)^2$. The multipliers 2, 6 and 12 are $t^2 + t$ for $t = 1, 2, 3$.

### 16.3 Immunizing a liability with two zero-coupon bonds

To protect a stream of payments against interest rate changes, choose a portfolio whose present value and duration equal those of the liability. For two zero-coupon bonds with maturities $T_1 < T_2$ (a zero's duration is its maturity):

$$
PV_L = \sum_{t} \frac{L_t}{(1 + y)^t} \qquad D_L = \sum_{t} t\,\frac{L_t/(1 + y)^t}{PV_L}
$$

$$
w_1\,T_1 + (1 - w_1)\,T_2 = D_L \quad\Longrightarrow\quad w_1 = \frac{T_2 - D_L}{T_2 - T_1}, \qquad w_2 = 1 - w_1
$$

$$
\text{Dollars in bond } j = w_j \times PV_L \qquad \text{Bonds of \$1 face} = \text{Dollars} \times (1 + y)^{T_j}
$$

| Symbol | Definition |
|---|---|
| $L_t$ | Liability (payment due) in year $t$ |
| $y$ | Flat market yield, compounded annually |
| $PV_L$ | Present value of the liability; the amount to invest today |
| $D_L$ | Duration of the liability |
| $T_1,\;T_2$ | Maturities of the two zero-coupon bonds, in years |
| $w_1,\;w_2$ | Fraction of $PV_L$ invested in each zero-coupon bond |
| $(1 + y)^{T_j}$ | Growth factor that converts dollars invested into the face value that bond $j$ pays at maturity |

A negative weight means selling that bond short. Compare the liability's duration with a zero-coupon bond's maturity to answer sensitivity questions: if $D_L$ is less than the bond's maturity, the liability is less sensitive to rate changes than that bond; if greater, it is more sensitive.

**Example.** Payments of \$5,000 are due in years 2 and 4 at a flat 6% yield. Present values are \$4449.98 and \$3960.47, so $PV_L$ = \$8,410.45, and $D_L = 2.9418$ years. Using zeros maturing in 1 and 6 years: $w_1 = (6 - 2.9418)/(6 - 1) = 0.6116$ and $w_2 = 0.3884$. Dollars invested: \$5,144.17 and \$3,266.28. Bonds of \$1 face: $5,144.17 \times 1.06^{1} = 5,453$ one-year zeros and $3,266.28 \times 1.06^{6} = 4,633$ six-year zeros. Check: $w_1 T_1 + w_2 T_2 = 2.9418$, equal to $D_L$.

**TI BA II Plus.** Each step builds on the one before.

| Step | Keys | Display |
|---|---|---|
| PV of the year 2 payment | `2ND` `CLR TVM`  `2` `N`  `6` `I/Y`  `0` `PMT`  `5000` `FV`  `CPT` `PV` `+/-` `STO` `1` | 4449.9822 |
| PV of the year 4 payment | change `N` to `4`  `CPT` `PV` `+/-` `STO` `2` | 3960.4683 |
| Present value of the liability $PV_L$ | `RCL` `1` `+` `RCL` `2` `=` `STO` `3` | 8,410.4505 |
| Duration of the liability $D_L$ | `(` `2` `×` `RCL` `1` `+` `4` `×` `RCL` `2` `)` `÷` `RCL` `3` `=` `STO` `4` | 2.9418 |
| Weight $w_1$ | `(` `6` `−` `RCL` `4` `)` `÷` `5` `=` `STO` `5` | 0.6116 |
| Weight $w_2$ | `1` `−` `RCL` `5` `=` `STO` `6` | 0.3884 |
| Dollars in bond 1 | `RCL` `5` `×` `RCL` `3` `=` `STO` `7` | 5,144.17 |
| Dollars in bond 2 | `RCL` `6` `×` `RCL` `3` `=` `STO` `8` | 3,266.28 |
| Number of \$1-face bonds, bond 1 | `2ND` `CLR TVM`  `1` `N`  `6` `I/Y`  `0` `PMT`  `RCL` `7` `+/-` `PV`  `CPT` `FV` | 5,452.82 |
| Number of \$1-face bonds, bond 2 | change `N` to `6`  `RCL` `8` `+/-` `PV`  `CPT` `FV` | 4,633.28 |
| Check the duration match | `RCL` `5` `×` `1` `+` `RCL` `6` `×` `6` `=` | 2.9418 |

If $w_1$ comes out negative or above 1, one of the two bonds must be sold short. That is not an error.

### 16.4 Why immunization is difficult, and the simpler alternative: cash-flow matching

Difficulties with duration matching:

- **Rebalancing.** Duration changes as time passes and as rates change, and not at the same pace for the assets and the liability, so the portfolio must be rebalanced.
- **Limited protection.** It protects only against small, parallel shifts of the yield curve.
- **Convexity.** Differences in convexity leave the match imperfect for larger moves.

Cash-flow matching (dedication) buys a zero-coupon bond maturing on each payment date, with face value equal to the payment:

$$
\text{Cost today} = \sum_{t} \frac{L_t}{(1 + y)^t} = PV_L
$$

| Symbol | Definition |
|---|---|
| $L_t$ | Payment due in year $t$ (also the face value of the zero maturing in year $t$) |
| $y$ | Yield, compounded annually |
| $PV_L$ | Present value of the liability, which equals the cost of the matching zeros |

**Example.** For the liability above, buy two zeros with \$5,000 face maturing in years 2 and 4. The cost is $PV_L$ = \$8,410.45. Each bond pays the tuition exactly when it is due, so there is no rebalancing and no exposure to yield-curve shifts.

**TI BA II Plus.** The cost of the matching zeros is the same present value you found in 16.3. The year 2 and year 4 face values are the payments themselves, so no bond-count calculation is needed.

| Step | Keys | Display |
|---|---|---|
| Cost of the year 2 zero | `2ND` `CLR TVM`  `2` `N`  `6` `I/Y`  `0` `PMT`  `5000` `FV`  `CPT` `PV` | -4,449.98 |
| Cost of the year 4 zero | change `N` to `4`  `CPT` `PV` | -3,960.47 |
| Total cost | add the two present values (ignore the signs) | 8,410.45 |

---

## Quick reference: when to use which formula

| Question type | Formula |
|---|---|
| Compare a municipal bond with a taxable bond | 2.1 |
| Return on a stock bought on margin | 3.1 |
| Price at which a margin call occurs | 3.2 |
| Return from selling a stock short; maximum loss or gain | 3.3 |
| Compare funds with different loads and expense ratios | 4.1 |
| Interest paid by a bond; free cash flow | 14.1, 14.2 |
| Accrued interest, day counts | 14.3 |
| Bond price from a yield; flat and full price; YTM | 14.4, 14.5, 14.6 |
| Spot rates from a bill and a coupon bond | 15.1 |
| Forward rates, discount factors, price from forwards, then YTM | 15.2, 15.3, 14.6 |
| Duration, price change, convexity | 16.1, 16.2 |
| Immunization and cash-flow matching | 16.3, 16.4 |
