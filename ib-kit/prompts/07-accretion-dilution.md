# Accretion / Dilution Prompts

**Layer:** Insight · **Engagement contexts:** M&A Advisory, ECM, Strategic Alternatives
**Pairs with:** `skills/accretion-dilution-modeling`, `agents/merger-model-agent`, `workflows/valuation.md`

## A. Model setup

1. **Build the merger model** — "Build a merger model for `<Acquirer>` acquiring `<Target>` at `<$X>` per share. Structure it with separate standalone forecasts, a purchase-price allocation, pro forma adjustments and an EPS bridge. Every pro forma number must trace to a standalone number plus a named adjustment."
2. **Standalone forecasts** — "Build 3-year standalone forecasts for both companies from consensus, then state every place you deviated from consensus and why."
3. **Transaction assumptions sheet** — "Create the assumptions sheet: offer price, premium, consideration mix, exchange ratio mechanics, financing sources and costs, fees, synergy phasing, integration costs, closing date and tax rate. One input cell each, referenced everywhere."
4. **Fiscal-year alignment** — "`<Acquirer>` has a `<month>` year-end and `<Target>` a `<month>` year-end. Align the forecasts, show the stub adjustment, and state the effect on first-year EPS."
5. **Mid-year close** — "Model a closing date of `<date>`. Include only the post-close portion of the target's earnings and the corresponding financing cost. Show the partial-year arithmetic."

## B. Purchase price and accounting

6. **Purchase price allocation** — "Build the PPA: equity purchase price, plus assumed debt, less cash, equals enterprise value. Allocate to identified intangibles by class with useful lives, write up inventory and PP&E, book deferred tax on the write-ups, and plug goodwill. Show the balancing."
7. **Intangible amortisation** — "Estimate intangible values by class — customer relationships, technology, trade names, backlog — using sector-typical allocation percentages. Build the amortisation schedule and show the annual EPS drag."
8. **Goodwill calculation** — "Compute goodwill and state whether it is tax-deductible under this structure. Quantify the value of the tax step-up if it is."
9. **Deferred tax liabilities** — "Compute the DTL arising on intangible and asset write-ups at `<rate>`. Show its unwinding and the effect on cash versus book tax."
10. **Inventory step-up** — "Model the inventory fair-value step-up and its one-time COGS impact in the first year post-close. Present EPS with and without it."
11. **Deferred revenue haircut** — "Model the fair-value haircut to `<Target>`'s deferred revenue. Show the first-year revenue reduction and the multi-year normalisation."
12. **Stock compensation replacement** — "Value the replacement awards for `<Target>`'s unvested equity. Split between purchase consideration and post-close expense, and show both effects."
13. **Debt refinancing** — "Model the refinancing of `<Target>`'s existing debt: make-whole or call premium, write-off of unamortised issuance costs, and new debt cost."
14. **Transaction and financing fees** — "Separate expensed transaction fees from capitalised financing fees. Amortise the latter over tenor and show both hitting the right lines."

## C. Accretion / dilution mechanics

15. **Core EPS bridge** — "Build the EPS bridge: acquirer standalone net income, plus target net income, plus after-tax synergies, less after-tax incremental interest, less foregone interest on cash used, less after-tax intangible amortisation, less other adjustments, divided by pro forma shares. Show every line in dollars and in cents per share."
16. **Accretion/dilution summary** — "Report accretion/dilution in dollars per share and in percent for years 1, 2 and 3, on GAAP EPS and on cash EPS. State which measure you consider decisive and why."
17. **Cash EPS** — "Compute cash EPS excluding intangible amortisation and one-time items. Explain the case for and against presenting it as the headline."
18. **Pro forma share count** — "Build the pro forma diluted share count: acquirer shares, plus new shares issued at the exchange ratio, plus dilution from converted target awards, less any buyback. Show the treasury-method calculation."
19. **Exchange ratio mechanics** — "Model a fixed exchange ratio and a fixed-value exchange ratio with a `<X>`% collar. Show how consideration value and accretion move as `<Acquirer>`'s share price moves ±20%."
20. **Break-even synergies** — "Solve for the annual synergy amount required for the deal to be EPS-neutral in year 1 and in year 2. Compare to the announced synergy target."
21. **Break-even price** — "Solve for the maximum price per share that keeps the deal accretive in year `<X>`. This is the EPS-constrained ceiling; state it next to the value-based ceiling."
22. **Contribution analysis** — "Compare each party's contribution to pro forma revenue, EBITDA, net income and cash flow against its share of the pro forma equity. Identify who is over- or under-paying on a contribution basis."
23. **Accretion is not value** — "Show a case where this deal is EPS-accretive but value-destructive, and one where it is dilutive but value-creative. Explain the mechanism in plain language for the board."

## D. Financing and structure comparison

24. **Consideration mix comparison** — "Compare 100% cash, 100% stock and `<X>`/`<Y>` mixed consideration: accretion, pro forma leverage, credit rating impact, ownership dilution and shareholder-vote requirement. Recommend one and say what would change your mind."
25. **Cash vs debt funding** — "Compare funding with balance-sheet cash against new debt. Include foregone interest income, incremental interest expense, rating implications and the liquidity cushion retained."
26. **Optimal funding mix** — "Solve for the funding mix that maximises year-2 accretion subject to pro forma net leverage staying under `<X>`x and the rating staying at `<rating>`."
27. **Equity issuance dilution** — "Model the equity raise required: size, discount to market, new shares, ownership dilution to existing holders, and the effect on the exchange ratio if done concurrently."
28. **Rating agency test** — "Assess the pro forma credit metrics against `<agency>`'s published thresholds for `<rating>`. Identify the metric closest to a downgrade and the headroom in dollars."
29. **Pro forma capital structure** — "Build the pro forma capital structure: every tranche, maturity, pricing and covenant. Show the maturity wall and identify refinancing risk in the first 3 years."

## E. Analysis, stress and delivery

30. **Sensitivity grid** — "Build an accretion grid across offer price `<range>` and synergy realisation `<range>`. Mark the boundary between accretive and dilutive."
31. **Synergy phasing sensitivity** — "Show accretion under three synergy phasings — 25/75/100, 40/80/100 and 15/50/85 percent of run-rate in years 1–3 — holding the run-rate constant."
32. **Integration cost impact** — "Model integration costs of `<X>`x run-rate synergies spread over `<Y>` years. Show accretion including and excluding them and state which the market will focus on."
33. **Downside case** — "Run a case with target EBITDA `<X>`% below plan, synergies at 60% of target and interest rates `<Y>`bps higher. Report year-2 accretion and pro forma leverage."
34. **Share-price sensitivity** — "For a stock deal, show how accretion changes if `<Acquirer>` trades down 20% before closing. Identify the price at which the deal stops making sense."
35. **ROIC test** — "Compute the deal's return on invested capital in years 1–5 against `<Acquirer>`'s WACC. State the year ROIC exceeds WACC. If it never does, say so plainly."
36. **Value creation test** — "Compute value created: the present value of synergies less the premium paid less integration costs. Report it in dollars and as a percentage of the acquirer's market cap."
37. **EPS vs value reconciliation** — "Reconcile the accretion conclusion to the DCF value conclusion. Where they disagree, explain which one the board should weight and why."
38. **Peer deal benchmarking** — "Benchmark this deal's accretion profile and premium against comparable transactions in `<sector>`. Identify where we are an outlier."
39. **Market reaction model** — "Estimate the likely announcement-day share-price reaction for `<Acquirer>` using event-study evidence from comparable deals. Identify which deal characteristics drove negative reactions."
40. **Model audit** — "Audit the merger model: double-counted synergies, interest calculated on the wrong debt balance, tax applied to pre-tax synergies twice, share count omitting target awards, amortisation on non-amortising intangibles, stub period mismatches. Report by severity with cell references."
41. **Board page** — "Produce the accretion/dilution page for the board: the EPS bridge, the 3-year accretion summary, the break-even synergy figure, and three sentences a director can repeat."
42. **Analyst Q&A prep** — "Write the 15 questions equity analysts will ask on the announcement call about this deal's financial impact, with the answer and the supporting number for each."
