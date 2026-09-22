# LBO Analysis Prompts

**Layer:** Insight · **Engagement contexts:** Leveraged Finance, M&A Advisory, Strategic Alternatives
**Pairs with:** `skills/lbo-modeling`, `agents/lbo-modeling-agent`, `workflows/financing.md`

## A. Structuring the transaction

1. **Sources and uses** — "Build sources and uses for an LBO of `<Target>` at `<$X>`m enterprise value. Sources: each debt tranche with size, pricing and terms; sponsor equity; management rollover; any preferred. Uses: equity purchase price, refinanced debt, transaction fees, financing fees, minimum cash. It must balance to the cent."
2. **Capital structure design** — "Design the capital structure for `<Target>` at `<X>`x total leverage: allocate across revolver, TLA, TLB, second lien, senior notes, subordinated notes and preferred. Justify each tranche's size against current market appetite."
3. **Leverage capacity test** — "Determine maximum sustainable leverage for `<Target>` from three tests: what lenders will provide, what cash flow services with adequate cushion, and what the business survives in a downturn. The binding constraint is the answer."
4. **Pricing the debt** — "Price each tranche using current market comparables for `<sector>` credits at `<rating>`. Give base rate, spread, OID, floors, call protection and total effective cost."
5. **Covenant package** — "Specify the covenant package: which tranches are cov-lite, the springing leverage test and its trigger, any maintenance covenants with their levels and step-downs, and the EBITDA definition including add-back caps."
6. **Fee schedule** — "Build the full fee schedule: M&A advisory, financing/underwriting, arrangement, legal, accounting, consulting, insurance, and sponsor transaction fee. State each as a percentage and in dollars."
7. **Rollover structuring** — "Structure management rollover at `<X>`% of proceeds. Show the tax treatment, the vesting, and the effect on sponsor equity requirement and returns."
8. **Equity ticket sizing** — "Given a fund size of `<$X>`bn and a maximum single-investment concentration of `<Y>`%, test whether this equity cheque fits. If not, size the co-invest required."

## B. Operating model and debt schedule

9. **Operating case** — "Build the management case, a sponsor base case and a downside case for `<Target>`. For each, show revenue, EBITDA, capex and working capital, and state the specific haircuts applied to management's numbers."
10. **EBITDA definition** — "Define credit-agreement EBITDA for `<Target>`: reported EBITDA plus permitted add-backs, run-rate synergies with their cap and their look-forward period. Show the gap between credit EBITDA and cash EBITDA."
11. **Debt schedule** — "Build the full debt schedule: opening balance, mandatory amortisation, cash sweep, optional prepayment, PIK accretion, and closing balance per tranche per period, with interest on average balances."
12. **Cash sweep mechanics** — "Model the excess-cash-flow sweep with leverage-based step-downs at `<levels>`. Show the sweep percentage and dollars applied per year, and the payment waterfall across tranches."
13. **Revolver mechanics** — "Model the revolver: commitment size, drawn balance driven by minimum cash, undrawn commitment fee, and the springing covenant trigger at `<X>`% drawn."
14. **Interest rate assumptions** — "Model interest using the current `<SOFR/EURIBOR>` forward curve rather than a flat rate. Show the value and coverage difference versus a flat-rate assumption."
15. **Hedging** — "Model a `<X>`% interest-rate hedge via `<swap/cap>` at `<rate>`. Show the cost, the P&L effect and the downside-case protection delivered."
16. **PIK toggle** — "Model a PIK toggle on the `<tranche>`: the cash-vs-PIK decision rule, accreted balance, and the returns effect of toggling in the downside case."
17. **Credit statistics** — "Report per period: total and net leverage, senior leverage, EBITDA/interest, (EBITDA − capex)/interest, fixed-charge coverage and FCF/debt. Chart deleveraging."
18. **Covenant headroom** — "Compute headroom against each covenant per period in percentage and dollar EBITDA terms. Identify the first period of breach in the downside case and the cure options available."

## C. Returns

19. **Returns waterfall** — "Build the returns waterfall at exit: enterprise value at exit multiple, less net debt, distributed across preferred, sponsor common, rollover and the management incentive plan. Show gross and net of carry."
20. **IRR and MOIC** — "Compute IRR and MOIC for the sponsor across exit years 3 through 7 and exit multiples `<range>`. Present as a grid."
21. **Returns attribution** — "Decompose the sponsor's MOIC into EBITDA growth, multiple expansion/contraction, debt paydown and free-cash-flow generation. State what percentage of return comes from leverage alone."
22. **Entry multiple solve** — "Solve for the maximum entry multiple that delivers a `<X>`% IRR at a `<Y>`x exit multiple in year `<Z>`. This is the floor price the sponsor can bid."
23. **Exit multiple required** — "Solve for the exit multiple required to hit `<X>`% IRR at the current entry price. Assess whether that multiple is plausible given where the sector trades."
24. **Management incentive plan** — "Model a `<X>`% MIP with a `<Y>`x hurdle and `<Z>`-year vesting. Show the dilution to sponsor returns across exit scenarios."
25. **Preferred structure** — "Model structured preferred at `<X>`% PIK with a `<Y>`x cap. Show the returns split between preferred and common at each exit multiple."
26. **Dividend recap** — "Model a dividend recapitalisation in year `<X>` re-levering to `<Y>`x. Show the IRR uplift, the residual equity value, and the incremental default risk."
27. **Add-on acquisitions** — "Model `<N>` add-ons at `<X>`x entry against a platform at `<Y>`x. Show the multiple-arbitrage contribution to returns and the incremental leverage capacity consumed."
28. **Exit route comparison** — "Compare exit via strategic sale, sponsor-to-sponsor sale and IPO: achievable multiple, timing, proceeds, certainty and residual exposure."

## D. Stress and structure testing

29. **Downside case** — "Run a downside case: revenue down `<X>`%, EBITDA margin down `<Y>`bps, working capital outflow. Report the first covenant breach, the liquidity trough and whether the structure survives without a sponsor cheque."
30. **Break-even analysis** — "Solve for the EBITDA decline at which (a) covenants breach, (b) cash interest is not covered, (c) sponsor equity is worthless. Present all three thresholds."
31. **Rate shock** — "Increase base rates by `<X>`bps sustained. Report the effect on coverage, sweep, deleveraging and IRR."
32. **Liquidity runway** — "In the downside case, compute months of liquidity from cash plus revolver availability. Identify the first period of funding shortfall."
33. **Recovery analysis** — "In a default scenario at `<X>`x distressed EBITDA multiple, compute recovery per tranche through the waterfall. Report each tranche's recovery percentage."
34. **Amend-and-extend** — "Structure an amend-and-extend for a `<year>` maturity: fee, spread increase, tenor extension, covenant reset. Show the effect on returns."
35. **Ratings assessment** — "Assess the likely corporate family rating and facility ratings for this structure using published agency methodology. Identify which metric is the constraint."

## E. Advice and delivery

36. **Financing market read** — "Describe the current `<sector>` leveraged finance market: available leverage, pricing, terms, and whether the deal clears syndication or needs a private-credit solution."
37. **Bank vs private credit** — "Compare a broadly syndicated structure to a private-credit unitranche for this deal: leverage, pricing, terms, execution certainty, flexibility. Recommend one."
38. **Sponsor bid strength** — "Given this LBO, estimate the maximum a financial sponsor can pay for `<Target>` and compare it to what a strategic can pay with synergies. Identify who wins the asset and by how much."
39. **Staple financing** — "Construct a staple financing package for the sell-side process: structure, terms, and the message it sends the buyer universe."
40. **Model audit** — "Audit this LBO model: circularity resolution, interest on average vs closing balances, sweep applied before or after mandatory amortisation, fee capitalisation and amortisation, tax shield on the right interest base, balance-sheet balancing. Report by severity."
41. **IC memo returns section** — "Write the returns section of the investment committee memo: base, upside and downside IRR/MOIC, the attribution, the three assumptions the return depends on, and what kills the deal."
42. **One-page LBO summary** — "Produce the one-page LBO summary for the client: sources and uses, key credit stats at entry and exit, the returns grid, and the single sentence that says whether this deal works."
