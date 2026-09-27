# Fixed Income Study Guides

Study guides for an undergraduate fixed income unit, aligned with Bodie, Kane & Marcus, *Investments*, 13th edition (2024). Each guide covers concepts and formulas, worked examples, calculations on the TI BA II Plus Professional, HP 12C, Excel, Python (QuantLib) and Julia, a practice set, CFA-style review questions, Bloomberg Terminal exercises and readings from the textbook.

| # | Guide | Topics |
| --- | --- | --- |
| 1 | [Treasury STRIPS](01-treasury-strips.md) | What STRIPS are, why they are used, quoting, pricing, taxation, TIPS strips |
| 2 | [Bootstrapping the Spot Curve](02-bootstrapping-the-spot-curve.md) | Discount factors, spot and forward rates, par vs spot vs forward curves |
| 3 | [Quantitative Tools](03-quantitative-tools.md) | TI BA II Plus Professional, HP 12C, Excel, Python libraries, Julia |
| 4 | [Measures of Yield](04-measures-of-yield.md) | Current yield, YTM, YTC/YTW, realized yield, BEY vs EAY, real yield, breakeven |
| 5 | [Duration, Average Life and Convexity](05-duration-average-life-convexity.md) | Macaulay, modified and effective duration, DV01, WAL, convexity, immunization, hedging |
| 6 | [U.S. Treasuries](06-us-treasuries.md) | Securities, pricing, auctions, secondary market, on/off-the-run, TreasuryDirect, ladders |
| 7 | [Callable, Putable and Convertible Bonds](07-callable-putable-convertible-bonds.md) | Options review, embedded options, binomial tree pricing, OAS |

## Notes

- Equations use GitHub's protected math syntax: ```` ```math ```` blocks for display equations and `` $`...`$ `` for inline math, so the Markdown parser does not alter the LaTeX.
- Python examples were run and checked against the worked answers; Julia examples follow the same logic but were not run.
- Bloomberg Terminal sections are drafts to be verified on a Terminal; mnemonics and field names change over time.
- CFA-style questions are original and are not CFA Institute material.
- Yields in the ladder and tree examples are illustrative, not market data.
