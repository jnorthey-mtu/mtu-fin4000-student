# Mini Study Guide 15: Sovereign Bond Yield Correlations

[← All study guides](../../study-guide-index.md)

Oct 4, 2026 · Jim Northey

## Why it matters

Government bond yields in different countries tend to move together, and the strength of that comovement changes over time. For a portfolio manager it determines how much diversification a multi-country sovereign portfolio really delivers, especially in a crisis.

**Key terms**

- **Comovement / correlation:** how closely yield changes in two countries move together. Always measure on yield changes, not levels, because levels trend and produce spurious correlation.
- **Excess comovement (Sutton's puzzle):** long-term yields in different countries move together more than local fundamentals and the expectations theory of the term structure would predict.
- **Term premium:** the extra yield investors demand for holding long bonds. If term premia are correlated across countries, long yields comove even when short-rate expectations differ.
- **Real rate, expected inflation, inflation risk premium:** the components of a nominal yield. The split tells you what is driving correlation.
- **Contagion:** a rise in correlation or spreads during stress that is not explained by fundamentals alone.
- **Spread:** a country's yield minus a benchmark (usually the German Bund in Europe). Widening spreads mean falling correlation with the core.
- **GIIPS:** Greece, Italy, Ireland, Portugal, Spain, the euro-area countries most affected by the sovereign debt crisis.

## Reading list

**1. Bekaert & Ermolov, [International Yield Co-movements](https://papers.ssrn.com/abstract=3402785) (2021, SSRN / CEPR DP16365)**

The authors split long-term nominal yields into real and inflation components using inflation-linked and nominal bonds across countries. Real-rate variation, not inflation, dominates yield variation, and real rates are the main source of correlation between countries' nominal yields. Cross-country correlations have declined since the Great Recession, a result robust to liquidity-premium and inflation-expectation adjustments.

*Discuss:* If real rates drive correlation, what would a global shift in saving or growth expectations do to diversification across sovereigns?

**2. Asgharian, Liu & Larsson, [Cross-Border Asset Holdings and Comovements in Sovereign Bond Markets](https://ehl.lu.se/hossein-asgharian/publication/79b27502-3084-4da1-ab3b-c1e2792fc51a) (Journal of International Money and Finance, vol. 86, 2018)**

Using a spatial VAR on Euro-area yield curves, the paper shows that cross-border holdings of long-term debt and bank lending help explain interdependence. Comovement fell after 2008, largely because the GIIPS countries segmented from the rest. Differences in sovereign creditworthiness, seen in the CDS term structure, are a main driver of the post-2008 divergence. A [2015 working-paper version](https://swopec.hhs.se/lunewp/abs/lunewp2015_030.htm) is free to read.

*Discuss:* Why would banks' holdings of other countries' debt transmit shocks? Who bears the loss?

**3. BIS Working Paper No. 44, [Is there excess comovement of bond yields between countries?](https://www.bis.org/publ/work44.htm) (July 1997)**

The classic reference. Ten-year yields in the US, Japan, Germany, the UK and Canada showed both excess volatility and excess comovement relative to the expectations theory. The implication is that term premia at the long end are time-varying and positively correlated across markets.

*Discuss:* How does a correlated term premium differ from correlated expectations of future short rates, and why does it matter for hedging?

**4. Smets, [Convergence and Divergence in Government Bond Markets](https://kansascityfed.org:443/documents/4568/2013Smetshandout.pdf) (Kansas City Fed symposium handout, 2013)**

A policy-maker's view of two opposite episodes: rising comovement of advanced-economy yields, and a dramatic breakdown of comovement inside the euro area. It revisits the excess-comovement puzzle and argues that time-varying pricing of sovereign risk matters for understanding the divergence.

*Discuss:* What can a central bank do to a long-term yield, and what can it not do?

**5. Supplementary (from the search results):** a [wavelet study of sovereign yields and stock returns in ten Eurozone countries](https://inzeko.ktu.lt/index.php/EE/article/view/6416/6754) shows that bond-stock comovement differs by country and time horizon, and a [PhD dissertation summary on emerging-market sovereign spreads](https://dea.lib.unideb.hu/bitstreams/b2865d1b-1eff-4fef-bd8f-842cff8297d1/download) examines how global factors and country fundamentals jointly drive spreads.

## The Wall Street Journal on European contagion

The WSJ framed the 2010-2011 euro-area crisis as a contagion story, and the academic evidence is more nuanced than the headlines. Note: the WSJ is paywalled and I could not open the articles themselves. The points below come from secondary sources that cite them, so pull the originals through the library (Factiva, ProQuest or the WSJ archive) before assigning them.

**Coverage to read**

- **"Who's Next? Spain? Italy?" (Neil Shah, WSJ, 4 Feb 2010).** Cited in [Bhanot, Burns, Hunter & Williams](https://interim.business.utsa.edu/wps/fin/0006FIN-073-2012.pdf) as the press source for the contagion narrative. The same authors note that, at the time, insuring Greek debt against default cost two to three times as much as insuring Portugal or Spain.
- **Barroso letter in the WSJ (4 Aug 2011).** The European Commission president wrote that the crisis was no longer confined to the periphery. [Calculated Risk](https://www.calculatedriskblog.com/2011/08/european-commission-president-crisis-no.html) reproduced the letter's context along with Bloomberg data showing record 10-year spreads to Germany of about 389.5 basis points for Italy and 398.5 for Spain.
- **WSJ coverage of fading appetite for Spanish and Italian bonds (Aug 2011).** Summarised by [ETF Trends](https://www.etftrends.com/2011/08/italy-etf-feeling-heat-of-debt-crisis/amp/): weaker risk appetite threatened these countries' ability to finance their deficits.
- **Earlier framing (Apr 2010).** [A CNBC commentary](https://www.cnbc.com/2010/04/29/farr-european-contagion-spreads.html) cites the WSJ's point that Greece and Portugal were small parts of the EU economy, but Spain, the fourth largest, ran a deficit of 11.2% of GDP.

**Does the evidence support the headline?**

[Bhanot et al.](https://interim.business.utsa.edu/wps/fin/0006FIN-073-2012.pdf) tested it with daily Bloomberg data on 5-year yield spreads to Germany (2003 to April 2011). The press was right on the raw numbers: correlations of Greek spread changes with the other PIIGS rose from an average of about 0.31 before the crisis to about 0.65 during it. But yield-spread volatility also exploded, and correlation rises mechanically with volatility. After controlling for volatility, global risk measures, CDS spreads and bank-stock returns, conditional correlations fell, so the authors find no evidence of contagion. Banking-sector stress and news announcements were the transmission channels that did matter.

Two other studies pull the other way or add nuance. A [copula study of five peripheral countries](https://research.monash.edu/en/publications/determinants-of-sovereign-bond-yield-spreads-and-contagion-in-the/) finds strong contagion, with Ireland, Greece and Portugal as exporters, while Spain and Italy appear to operate independently of each other. A [column on Eurozone CDS spreads (drawing on Manasse and Trigilia, 2011)](https://creditwritedowns.com/2011/07/contagion-fear-greece.html) argues that fear of contagion from Greece to Italy was exaggerated.

**Link to the course papers**

- Asgharian et al. explain the post-2008 divergence through banks' cross-border holdings and sovereign creditworthiness, which matches the banking channel above.
- Smets describes the same episode from the policy side: euro-area comovement broke down while global comovement stayed high.
- BIS WP 44 is the benchmark: before asking whether contagion exists, ask what comovement fundamentals alone would predict.

*Discuss:* Is a jump in correlation during a crisis evidence of contagion or just of higher volatility? What would you control for?

## Synthesis and review questions

**What the readings add up to**

1. Long yields comove across countries more than fundamentals alone would predict (BIS WP 44), and real rates are the main driver (Bekaert & Ermolov).
2. Comovement is not constant: it fell after the Great Recession globally, and fell sharply inside the euro area after 2008 as credit risk and bank balance sheets segmented the periphery from the core (Asgharian et al., Smets).
3. Crisis correlations overstate contagion unless you control for volatility and fundamentals (Bhanot et al.). The press narrative and the econometric evidence can disagree.

**Review questions**

1. Why measure correlation on yield changes rather than yield levels?
2. Decompose a 10-year nominal yield. Which component does Bekaert & Ermolov say drives cross-country correlation?
3. A portfolio holds German, French and Italian 10-year bonds. How should the diversification benefit differ in 2006, 2011 and today?
4. Define contagion in Bhanot et al.'s terms. Why can unconditional correlation rise while conditional correlation falls?
5. Which transmission channels does the euro-area evidence identify, and which asset class would you watch to detect them early?
6. Compute a rolling 12-month correlation of US and German yield changes. What would you expect a structural break to look like?

**Running the analysis (companion files)**

- **Jupyter notebook:** a reusable correlation function that pulls free FRED data, computes static and rolling correlations on yield changes, and can optionally pull Bloomberg data.
- **Excel workbook:** the same logic with live formulas, so students can change the window or the country pair.
- **Bloomberg terminal:** `CORR <GO>` or `HRH <GO>` for quick views, or `BDH` in Excel for the data. Tickers such as `USGG10YR Index`, `GDBR10 Index`, `GUKG10 Index` and `GJGB10 Index`. Confirm menus with `HELP HELP`.

## Sources

Summaries are based on abstracts and search excerpts, except Bhanot et al., which I read in full. WSJ articles were not opened directly. Check each against the original before assigning it.

- [Bekaert & Ermolov, International Yield Co-movements (SSRN)](https://papers.ssrn.com/abstract=3402785); [CEPR DP16365](https://causalclaims.trfetzer.com/paper/DP16365.html)
- [Asgharian, Liu & Larsson, J. Intl Money & Finance 2018](https://ehl.lu.se/hossein-asgharian/publication/79b27502-3084-4da1-ab3b-c1e2792fc51a); [2015 working paper](https://swopec.hhs.se/lunewp/abs/lunewp2015_030.htm)
- [BIS Working Paper No. 44 (1997)](https://www.bis.org/publ/work44.htm)
- [Smets, Kansas City Fed handout (2013)](https://kansascityfed.org:443/documents/4568/2013Smetshandout.pdf)
- [Bhanot, Burns, Hunter & Williams, Was there Contagion in Eurozone Sovereign Bond Markets during the Greek Debt Crisis? (UTSA working paper, 2012)](https://interim.business.utsa.edu/wps/fin/0006FIN-073-2012.pdf)
- [Determinants of sovereign bond yield spreads and contagion in the peripheral EU countries (Monash)](https://research.monash.edu/en/publications/determinants-of-sovereign-bond-yield-spreads-and-contagion-in-the/)
- [Contagion Fear in Europe (Manasse and Trigilia, 2011)](https://creditwritedowns.com/2011/07/contagion-fear-greece.html)
- WSJ via secondary sources: [Calculated Risk (Barroso letter, Aug 2011)](https://www.calculatedriskblog.com/2011/08/european-commission-president-crisis-no.html), [ETF Trends (Aug 2011)](https://www.etftrends.com/2011/08/italy-etf-feeling-heat-of-debt-crisis/amp/), [CNBC (Apr 2010)](https://www.cnbc.com/2010/04/29/farr-european-contagion-spreads.html)
- Supplementary: [Eurozone bond-stock wavelet study](https://inzeko.ktu.lt/index.php/EE/article/view/6416/6754); [EM sovereign spreads dissertation summary](https://dea.lib.unideb.hu/bitstreams/b2865d1b-1eff-4fef-bd8f-842cff8297d1/download)
