# Study Guide 9: The IPO Process and the Underwriter's Role

*BKM Ch. 2–3*

[← All study guides](../../study-guide-index.md)

FIN 4000 Investments · Oct 3, 2026 · Jim Northey

## Learning objectives and BKM map

When a firm sells new shares to investors for the first time, that sale happens in the **primary market** — the one and only time the issuer itself receives cash for those shares. Every later trade between investors happens in the **secondary market**, where the issuer receives nothing. An **underwriter** (investment banker) stands between the two: in a **firm commitment** offering it buys the whole issue from the company and resells it to the public, bearing the risk that shares go unsold; in a **best efforts** deal, the issuer bears that risk instead. The underwriter's compensation is the **underwriting spread** — the gap between what the public pays and what the issuer receives. A well-documented regularity called **IPO underpricing** means the public offering price is typically set below where the stock opens trading, so the stock “pops” on day one; insiders are usually barred from selling into that pop by a **lockup period**.

After this section, you will be able to:

1. Distinguish the primary market from the secondary market, and explain why an IPO raises cash for the firm only once.
2. Describe the SEC registration process for a public offering: the S-1, the preliminary (“red herring”) prospectus, and the roadshow.
3. Contrast firm-commitment and best-efforts underwriting, and explain who bears the price risk in each.
4. Explain how bookbuilding sets the final offer price, and compute the underwriting spread in dollars and percent.
5. Explain IPO underpricing — why first-day returns are usually positive — and compute “money left on the table.”
6. Compute a greenshoe (overallotment) allocation and an investor's annualized return from the offer price to today.

| BKM 13e section | What it covers | Link to this guide |
| --- | --- | --- |
| 2 (Asset Classes and Financial Instruments) | Common stock as an asset class: residual claims, limited liability, voting rights | Background — what is actually being sold in an IPO |
| 3.1 How Firms Issue Securities | Primary vs. secondary markets, investment bankers/underwriters, firm commitment, prospectus, shelf registration (Rule 415), private placements (Rule 144A), IPOs | The core of this guide |
| 3.2 How Securities Are Traded | Types of markets: direct search, brokered, dealer, auction | Where the stock trades once the IPO is complete |

## Core concept 1: How a firm goes public

Going public is a regulated, multi-month process, not a single event. The firm hires an investment bank (or a syndicate of them), decides on an underwriting arrangement, files disclosure documents with the SEC, markets the deal to investors, and only then sets a final price.

### From private company to public filing

- **Engagement**: the issuer selects a lead underwriter (often after a competitive pitch) and negotiates the underwriting arrangement and fee.
- **Registration statement (Form S-1)**: filed with the SEC, describing the company's business, financials, risk factors, and how proceeds will be used.
- **Preliminary prospectus (“red herring”)**: the portion of the S-1 given to prospective investors; it carries a filing range (e.g., “\$28–\$35”) but no final price — the name comes from the red-ink legend warning that the registration is not yet effective.
- **SEC review / cooling-off period**: the SEC reviews the filing for adequate disclosure (it does not evaluate investment merit) while the underwriters cannot yet sell shares.
- **Roadshow**: company management and the underwriters present to institutional investors over one to two weeks, gauging demand and collecting non-binding indications of interest.
- **Pricing and effectiveness**: once the SEC declares the registration effective, the underwriters and issuer set the final offer price, typically the evening before the stock begins trading.

### Firm commitment vs. best efforts

|  | Firm commitment | Best efforts |
| --- | --- | --- |
| Who bears the risk of unsold shares | The underwriting syndicate | The issuer |
| Underwriter's role | Buys the entire issue from the issuer, then resells to the public | Acts as an agent, trying to sell on the issuer's behalf |
| Underwriter's compensation | The spread between the price paid to the issuer and the public offering price | A commission on shares actually sold |
| Typical use | Most U.S. IPOs of any size, including every company in this guide's companion case studies | Smaller or higher-risk offerings |

### Pricing the offer: bookbuilding

Rather than fixing a price up front, U.S. underwriters typically use **bookbuilding**: during the roadshow they collect indications of interest from institutional investors at various prices, building a “book” of demand. If the book is oversubscribed — as it was for every IPO in the companion deck — the underwriters can raise the filing range, raise the share count, or both, before setting the final price. A deal priced right at the top of a heavily oversubscribed book (Facebook, 5x oversubscribed) leaves little room for a first-day gain; a deal priced below where demand clearly was (Snowflake, range raised twice and still priced under the opening trade) leaves a great deal.

## Core concept 2: The underwriter's role, compensation, and the aftermarket

Once a deal is priced, the underwriters' job shifts from marketing to distribution, risk-bearing, and (briefly) propping up the price.

### The underwriting syndicate

A single bank rarely underwrites a large IPO alone. Instead, a **syndicate** forms:

- **Lead manager (lead-left / lead bookrunner)**: the bank whose name appears first on the prospectus; it runs the roadshow, allocates shares among the syndicate, and controls pricing. Facebook's was Morgan Stanley; Snowflake's and SpaceX's were co-led by Goldman Sachs and Morgan Stanley.
- **Co-managers**: additional banks that help distribute shares and lend their name (and research coverage) to the deal, for a smaller cut of the fee.
- **Selling group**: brokerages that sell shares to their own clients without taking on underwriting risk themselves.

### The underwriting spread

The **gross spread** is the difference between the public offering price and the price the issuer receives:

```math
\text{Gross spread (\$)} = (\text{Offer price} - \text{Price to issuer}) \times \text{Shares sold}
```

For a U.S. IPO this typically runs 5–7% of proceeds, though very large, highly sought-after deals can negotiate it far lower — Facebook's \$16 billion offering carried a blended underwriting fee of roughly 1.1%, reflecting its size and the intensity of bank competition for lead-left status.

### The greenshoe (overallotment option)

Underwriters are typically granted an **overallotment option** (“greenshoe”), letting them sell up to 15% more shares than the base offering. If the stock trades up, they exercise it, buying those extra shares from the company at the offer price. If the stock trades down, they can instead buy shares in the open market to cover their short position — a form of **price stabilization** that cushions the stock just after listing.

### IPO underpricing: money left on the table

Across decades of U.S. IPOs, the average first-day return is reliably positive — a pattern researcher Jay Ritter and others have documented extensively. Two explanations dominate: **information asymmetry** (issuers and underwriters deliberately price conservatively to compensate uninformed investors for the risk of being sold an overpriced “lemon,” a dynamic related to the **winner's curse**), and underwriters' own incentive to reward their best institutional clients with an easy first-day gain. The dollar cost of this to the issuer is called **money left on the table**:

```math
\text{Money left on the table} = (\text{Closing price} - \text{Offer price}) \times \text{Shares offered}
```

This is not a cost the issuer pays to anyone — it is proceeds the issuer simply never received, because it sold its shares for less than the market was immediately willing to pay. To limit how quickly that gain can be cashed in by insiders, companies agree to a **lockup period** (commonly 180 days, sometimes staggered) during which pre-IPO shareholders cannot sell.

## Worked examples

All five examples use real, sourced figures from the companion case-study deck and slides (*IPO Case Studies: Facebook, Snowflake, SpaceX & Dell*). Examples 1–4 are simple arithmetic; Example 5 uses the BA II Plus in TVM mode.

**Calculator setup.** For Example 5, clear the TVM worksheet first (`[2nd] [CLR TVM]`) and set P/Y = 1 (`[2nd] [P/Y]`, `1 [ENTER]`) since we are compounding once per year. Sign convention: an amount paid out (the price you “pay” to buy at the offer price) is entered as negative; an amount received back (today's value) is entered as positive.

### Example 1: Underwriting spread — Facebook

Facebook's 2012 IPO offered 421 million shares at \$38.00, raising roughly \$16.0 billion, with total underwriting fees of about \$175 million.

**Formula**

```math
\text{Gross spread \%} = \frac{\text{Total underwriting fees}}{\text{Total proceeds}} \times 100
```

| Symbol | Meaning | Value |
| --- | --- | --- |
| P | Offer price | \$38.00 |
| n | Shares offered | 421,000,000 |
| Proceeds | P × n | \$15,998,000,000 |
| Fees | Total underwriting fees | \$175,000,000 |

1. Divide total fees by total proceeds: \$175{,}000{,}000 / \$15{,}998{,}000{,}000\$.
2. Convert to a percent: multiply by 100.
3. Divide the dollar fee by the share count to get the spread per share.

**Calculator**

| Step | Keystrokes | Display |
| --- | --- | --- |
| Spread % | 175000000 [÷] 15998000000 [=] [×] 100 [=] | 1.0939 |
| Spread per share | 175000000 [÷] 421000000 [=] | 0.4157 |

The blended spread was about **1.09%** of proceeds — roughly \$0.42 per share, far below the 5–7% typically quoted for a standard-sized IPO. A deal this large gave Facebook unusual leverage to negotiate the fee down, and banks competed hard for lead-left status on the highest-profile offering of the year regardless.

### Example 2: Money left on the table — Snowflake

Snowflake priced at \$120.00 and closed its first day at \$253.93, on 32.2 million shares offered.

**Formula**

```math
\text{Money left on the table} = (\text{Close} - \text{Offer}) \times \text{Shares offered}
```

| Symbol | Meaning | Value |
| --- | --- | --- |
| Offer | IPO offer price | \$120.00 |
| Close | Day-one closing price | \$253.93 |
| n | Shares offered | 32,200,000 |

1. Find the per-share gap: \$253.93 - \$120.00 = \$133.93\$.
2. Multiply by shares offered.

**Calculator**

| Step | Keystrokes | Display |
| --- | --- | --- |
| Per-share gap | 253.93 [−] 120 [=] | 133.93 |
| Money left on the table | 133.93 [×] 32200000 [=] | 4,312,546,000 |

Snowflake left about **\$4.31 billion** on the table — more than the roughly \$3.4 billion it actually raised in the offering. That is the clearest possible illustration of underpricing: the company could have raised more by pricing closer to where the market was clearly willing to pay.

### Example 3: Comparing first-day underpricing — Facebook vs. Snowflake

**Formula**

```math
\text{First-day return} = \frac{\text{Close} - \text{Offer}}{\text{Offer}} \times 100
```

| Symbol | Meaning | Facebook | Snowflake |
| --- | --- | --- | --- |
| Offer | IPO offer price | \$38.00 | \$120.00 |
| Close | Day-one close | \$38.23 | \$253.93 |

**Calculator**

| Step | Keystrokes | Display |
| --- | --- | --- |
| Facebook return | 38.23 [−] 38 [=] [÷] 38 [=] [×] 100 [=] | 0.605 |
| Snowflake return | 253.93 [−] 120 [=] [÷] 120 [=] [×] 100 [=] | 111.608 |

Facebook's first-day return was about **0.6%** — essentially flat, and often called a “failed” IPO for it. Snowflake's was about **111.6%**. Both outcomes trace back to the same mechanism (bookbuilding and the final pricing decision); they sit at opposite ends of the same underpricing spectrum, not in different categories.

### Example 4: Sizing a greenshoe — SpaceX

SpaceX's June 2026 IPO offered a base of 555,555,555 shares at \$135.00, with a 15% overallotment option.

**Formula**

```math
\text{Greenshoe shares} = \text{Base shares} \times 15\%
```

| Symbol | Meaning | Value |
| --- | --- | --- |
| Base | Base shares offered | 555,555,555 |
| Rate | Overallotment rate | 15% |
| P | Offer price | \$135.00 |

1. Multiply base shares by 15% to get the greenshoe share count.
2. Multiply by the offer price for its dollar value.

**Calculator**

| Step | Keystrokes | Display |
| --- | --- | --- |
| Greenshoe shares | 555555555 [×] .15 [=] | 83,333,333 |
| Dollar value | 83333333 [×] 135 [=] | 11,249,999,955 |

If fully exercised, the greenshoe alone was worth about **\$11.25 billion** — on top of the \$75 billion base offering, for roughly \$86 billion in total if every option share was sold.

### Example 5: Annualized return since relisting — Dell (BA II Plus, TVM)

Dell's Class C shares opened at \$46.00 on December 28, 2018. By September 2026 (about 7.7 years later), shares traded near \$524. Treating this as a single investment held to today (ignoring the modest dividend for simplicity):

**Formulas**

```math
\text{FV} = \text{PV} \times (1 + i)^{N} \quad\Longrightarrow\quad i = \left(\frac{\text{FV}}{\text{PV}}\right)^{1/N} - 1
```

| Symbol | Meaning | Value |
| --- | --- | --- |
| PV | Price at relisting (2018) | \$46.00 |
| FV | Recent price (Sept. 2026) | \$524.00 |
| N | Years held | 7.7 |
| i (I/Y) | Annualized return (solve for) | ? |

**BA II Plus keystrokes**

| Step | Keystrokes | Display |
| --- | --- | --- |
| Clear TVM | [2nd] [CLR TVM] | 0.0000 |
| Periods | 7.7 [N] | N = 7.7000 |
| Price paid | 46 [+/−] [PV] | PV = −46.0000 |
| Value today | 524 [FV] | FV = 524.0000 |
| No periodic payment | 0 [PMT] | PMT = 0.0000 |
| Annual return | [CPT] [I/Y] | I/Y ≈ 37.15 |

Held from the 2018 relisting to today, Dell shares compounded at roughly **37.1% per year** — a reminder that a single multi-year holding period can look very different from, and tell you nothing about, how a stock performed on its first day of trading.

## Common pitfalls

- **Confusing the offer price with the opening trade price.** The offer price is what the issuer and underwriters set the evening before trading; the opening trade is the first price the stock actually trades at on the exchange once public orders meet — they can differ sharply (Snowflake: \$120 vs. \$245).
- **Treating the underwriting spread as an extra fee layered on top of the offer price.** It is not added on; it is embedded. Investors still pay the public offering price, but the issuer receives offer price minus the spread.
- **Assuming a big first-day pop is good news for the issuer.** A large pop means the company sold shares for less than the market would immediately pay — money left on the table, not a win.
- **Assuming the greenshoe always adds shares to the market.** If the stock trades below the offer price, underwriters typically use the option to buy shares back (stabilizing the price) rather than sell more.
- **Mixing up firm commitment and best efforts.** In a firm commitment the underwriter bears the risk of unsold shares; in best efforts, the issuer does.
- **Assuming lockup expiration always crashes the stock.** It often increases selling pressure and volatility, but the outcome depends on demand at the time; it is not a guaranteed decline.
- **Treating IPO underpricing and long-run performance as the same phenomenon.** Day-one underpricing is a short-run pricing-and-demand effect; how the stock performs over the following years depends on the business, not on how it was priced at the open.

## Key-terms checklist

- [ ] **Primary market:** the market where new securities are sold by the issuer, which receives the proceeds (BKM 3.1).
- [ ] **Secondary market:** the market where existing securities trade between investors; the issuer receives nothing (BKM 3.1).
- [ ] **Initial public offering (IPO):** a company's first sale of common stock to the public.
- [ ] **Seasoned equity offering (SEO):** a sale of additional stock by a company whose shares already trade publicly.
- [ ] **Investment banker:** a firm that advises issuers on structuring and pricing new securities and distributes them to investors.
- [ ] **Underwriter:** the investment banker that buys or markets a new issue; in a firm commitment it takes the price risk.
- [ ] **Underwriting syndicate:** a group of investment banks, led by one or more lead managers, that share the work and risk of distributing an issue.
- [ ] **Lead manager (lead-left / lead bookrunner):** the bank with ultimate control of the offering; its name appears first on the prospectus.
- [ ] **Co-manager:** an additional underwriter that helps distribute shares for a smaller share of the fee.
- [ ] **Selling group:** brokerages that sell shares to clients without bearing underwriting risk.
- [ ] **Firm commitment:** an underwriting in which the syndicate buys the entire issue from the issuer and bears the risk of unsold shares.
- [ ] **Best efforts:** an underwriting in which the banker agrees only to try to sell the issue; the issuer bears the risk of unsold shares.
- [ ] **Registration statement (Form S-1):** the disclosure document filed with the SEC describing the issuer, its financials, and the planned offering.
- [ ] **Prospectus:** the portion of the registration statement given to investors, describing the issuer, the securities, and the risks.
- [ ] **Preliminary prospectus (“red herring”):** the prospectus circulated before the SEC declares the registration effective; it carries a price range but no final price.
- [ ] **Roadshow:** the period in which company management and underwriters market the offering to institutional investors before pricing.
- [ ] **Bookbuilding:** the underwriter's process of collecting investor orders at different prices to help set the final offer price.
- [ ] **Offer price (IPO price):** the price at which the underwriters sell the new issue to the public.
- [ ] **Underwriting spread (gross spread):** the difference between the public offering price and the price the underwriter pays the issuer; the underwriters' compensation.
- [ ] **Overallotment option (greenshoe):** an option letting underwriters sell up to 15% more shares than the base offering, exercised depending on aftermarket demand.
- [ ] **Price stabilization:** underwriters' purchases of shares in the aftermarket to support a weak stock price, often financed through the greenshoe.
- [ ] **IPO underpricing:** the well-documented tendency for an IPO's offer price to sit below its first trading prices.
- [ ] **Money left on the table:** the dollar value of underpricing — (closing price − offer price) × shares offered — proceeds the issuer did not receive.
- [ ] **First-day return:** the percentage change from the offer price to the first closing price.
- [ ] **Winner's curse:** the risk that uninformed investors disproportionately win allocations in overpriced IPOs, used to help explain why issuers price conservatively.
- [ ] **Lockup period:** a contractual window (often 180 days) during which pre-IPO shareholders cannot sell their shares.
- [ ] **Shelf registration (Rule 415):** an SEC rule letting an issuer register securities once and sell them gradually over up to two years.
- [ ] **Private placement (Rule 144A):** a sale of securities directly to qualified institutional buyers without full SEC registration.
- [ ] **Dual-class share structure:** a capital structure with two or more share classes carrying different voting rights, often used by founders to retain control after an IPO.
- [ ] **Direct listing:** a method of going public by listing existing shares directly on an exchange, without new shares sold or an underwriting syndicate.
- [ ] **Aftermarket:** trading in a security in the days and weeks immediately following its IPO.

## CFA-style questions

**1. (Conceptual)** A company sells 10 million new shares directly to the public for the first time, receiving the proceeds itself. This transaction takes place in the:

- A. Secondary market, because the shares will trade on an exchange afterward.
- B. Primary market, because the issuer receives the proceeds.
- C. Dealer market, because an underwriter is involved.

**2. (Conceptual)** In a firm-commitment underwriting, if the underwriters are unable to sell all the shares at the offer price, who bears that loss?

- A. The issuer, since it is the issuer's stock.
- B. The underwriting syndicate, which already bought the shares from the issuer.
- C. The SEC, through its investor-protection fund.

**3. (Algorithmic)** A firm sells 50 million shares at an offer price of \$20.00, receiving net proceeds of \$940 million from the underwriters. The gross underwriting spread, in percent, is closest to:

- A. 3.0%
- B. 6.0%
- C. 9.4%

**4. (Algorithmic)** An IPO is priced at \$25.00 and closes its first day at \$31.00, on 40 million shares offered. The money left on the table is closest to:

- A. \$24 million
- B. \$240 million
- C. \$1,240 million

**5. (Algorithmic)** A company's base IPO offering is 100 million shares. Underwriters hold a standard 15% overallotment option. If fully exercised, the total shares sold (base plus greenshoe) equal:

- A. 105 million
- B. 115 million
- C. 150 million

**6. (Conceptual)** Which of the following best explains why IPOs are, on average, underpriced?

- A. The SEC sets a maximum legal offer price below fair value.
- B. Issuers and underwriters price conservatively partly to compensate less-informed investors for the risk of winning allocations in overpriced deals.
- C. Underwriters are legally required to guarantee a first-day gain to all investors.

**7. (Conceptual)** The main purpose of a lockup period is to:

- A. Guarantee the underwriters a minimum resale price.
- B. Prevent pre-IPO shareholders from selling into the new public market immediately after listing.
- C. Delay the payment of underwriting fees until the stock proves stable.

**8. (Algorithmic)** An investor buys shares at an IPO's \$40.00 offer price and sells five years later at \$97.00, with no dividends paid. The approximate annualized return is closest to:

- A. 14.5%
- B. 19.5%
- C. 24.0%

## Answer key

| # | Answer | Explanation |
| --- | --- | --- |
| 1 | B | The primary market is where the issuer sells new securities and receives the proceeds (BKM 3.1); the shares' later exchange trading is a separate, secondary-market event. |
| 2 | B | In a firm commitment, the syndicate buys the entire issue from the issuer up front and resells it, so any shortfall in demand is the underwriters' loss, not the issuer's. |
| 3 | B | Total offer value = 50M × \$20.00 = \$1,000M. Spread = \$1,000M − \$940M = \$60M. Spread % = \$60M / \$1,000M = 6.0%. |
| 4 | B | Money left on the table = (\$31.00 − \$25.00) × 40,000,000 = \$6.00 × 40,000,000 = \$240,000,000. |
| 5 | B | Greenshoe shares = 100M × 15% = 15M. Total = 100M + 15M = 115M. |
| 6 | B | Conservative pricing partly compensates uninformed investors for the winner's-curse risk of being allocated overpriced deals; the SEC does not set prices, and no first-day gain is legally guaranteed. |
| 7 | B | A lockup restricts pre-IPO shareholders (founders, employees, early investors) from selling for a set period after listing, limiting a flood of supply right after the IPO. |
| 8 | B | PV = 40 [+/−] [PV], FV = 97 [FV], N = 5 [N], PMT = 0, [CPT] [I/Y] → 19.38%, closest to 19.5%. |
