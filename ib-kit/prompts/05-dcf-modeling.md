# DCF Modeling Prompts

**Layer:** Insight · **Engagement contexts:** M&A Advisory, Fairness Opinions & Valuations, Strategic Alternatives
**Pairs with:** `skills/dcf-and-sensitivity`, `agents/dcf-modeling-agent`, `workflows/valuation.md`

## A. Model architecture

1. **Design the model** — "Specify the structure for `<Company>`'s DCF: tab layout, the single-input principle, colour convention for inputs vs formulas, forecast horizon and periodicity. Lay out the architecture before building anything."
2. **Choose the horizon** — "Recommend an explicit forecast horizon for `<Company>` and justify it by reference to when the business reaches steady state — returns converging to cost of capital, growth to a sustainable rate, capex to depreciation."
3. **Mid-year convention** — "State whether to use mid-year discounting for `<Company>` and quantify the value difference against year-end. Justify the choice from cash-flow timing, not convention."
4. **Stub period** — "Build the stub-period mechanics for a valuation date of `<date>`: partial-year cash flow, fractional discount period, and treatment of the next dividend or interest payment."
5. **Currency structure** — "`<Company>` earns in `<currencies>`. Recommend whether to model by currency and discount at currency-specific rates, or to model in `<base>` with forward FX. Show the value difference."
6. **Segment-level DCF** — "Structure a sum-of-the-parts DCF with separate forecasts and discount rates per segment, plus central costs allocated or valued separately. State your treatment of central costs explicitly."

## B. Operating forecast

7. **Revenue build** — "Build `<Company>`'s revenue forecast bottom-up from `<volume × price>` or `<customers × ARPU × retention>`. Every growth rate must be the output of a driver, never a hardcoded assumption."
8. **Anchor to history** — "Show 5 years of historical growth, margin, capex and working capital next to the forecast. Where the forecast diverges from history, justify each divergence in one sentence."
9. **Benchmark the forecast** — "Compare the forecast's growth and margin path to peer history and consensus. Identify every year where we are above the peer 75th percentile and defend it."
10. **Cost build** — "Split costs into fixed, variable and semi-variable. Forecast each on its own driver and show the implied operating leverage."
11. **Margin convergence** — "Model `<Company>`'s EBITDA margin converging from `<X>`% to a terminal `<Y>`%. Justify the terminal margin from industry structure and competitive position, not extrapolation."
12. **Capex forecast** — "Split capex into maintenance and growth. Tie maintenance capex to asset base and depreciation, and growth capex to the revenue it supports, with a stated capital-to-revenue ratio."
13. **Depreciation schedule** — "Build a rolling depreciation schedule from opening PP&E and forecast capex using `<useful life>`. Do not forecast depreciation as a percentage of revenue."
14. **Working capital** — "Forecast working capital from DSO, DIO and DPO with explicit day assumptions. Show the cash flow impact per year and flag any year where the assumption improves without a stated reason."
15. **Tax build** — "Build the cash tax forecast: statutory rate by jurisdiction, mix, permanent differences, NOL utilisation with expiry, and the year cash tax converges to the effective rate."
16. **NOL valuation** — "Value `<Company>`'s `<$X>`m of NOLs separately: utilisation schedule under the forecast, any Section 382 or local limitation, and discounted value."
17. **Unlevered FCF bridge** — "Build the unlevered free cash flow line from EBIT: less cash taxes on EBIT, plus D&A, less capex, less change in working capital, plus/minus other non-cash items. Show every line for every year."
18. **Lease treatment** — "State whether leases are treated as debt or as operating cost, and enforce that choice consistently in FCF, WACC and the net-debt bridge. Show both treatments once to prove consistency."
19. **Pension cash flow** — "Model the pension deficit-recovery payments separately from operating cash flow, and deduct the deficit in the equity bridge — not both."

## C. Discount rate

20. **Build the WACC** — "Build `<Company>`'s WACC: risk-free rate with its instrument and date, equity risk premium with its source, levered beta with its estimation window and index, target capital structure with its basis, pre-tax cost of debt with its evidence, and marginal tax rate. Cite every input."
21. **Beta estimation** — "Estimate `<Company>`'s beta three ways — raw regression, Blume-adjusted, and peer unlevered-relevered — and reconcile them. State which you use and why."
22. **Unlever and relever** — "Unlever peer betas at their actual capital structures and relever at `<Company>`'s target. Show the formula, the tax assumption, and the debt beta treatment."
23. **Target capital structure** — "Justify the target capital structure from peer medians, management's stated policy and rating-agency thresholds. Explain why it differs from today's actual."
24. **Country risk premium** — "Add a country risk premium for `<Company>`'s `<region>` exposure. Show the method — sovereign spread, relative volatility, or a weighted lambda approach — and the revenue-weighting applied."
25. **Small-company premium** — "Assess whether a size premium is warranted for `<Company>`. State the empirical basis, the magnitude, and the argument against using one."
26. **Cost of debt** — "Derive the pre-tax cost of debt from `<Company>`'s actual issuance, its rating, and comparable secondary spreads. Justify the marginal rate against the current blended rate."
27. **WACC sensitivity** — "Show enterprise value across a WACC range of ±`<X>`bps in 25bps steps, and state which single WACC input moves value the most."

## D. Terminal value

28. **Gordon growth TV** — "Compute terminal value using perpetuity growth of `<g>`. Justify `g` against long-run GDP and inflation, and state why it is not higher."
29. **Exit multiple TV** — "Compute terminal value on an exit multiple of `<X>`x. Justify the multiple from where the business will trade at steady state, not where it trades today."
30. **Cross-check the two** — "Show the implied exit multiple from the perpetuity method and the implied perpetuity growth from the exit-multiple method. If either is implausible, fix the forecast, not the terminal assumption."
31. **Terminal-year normalisation** — "Normalise the terminal year: capex equal to depreciation adjusted for growth, working capital investment consistent with `g`, margin at steady state, tax at the full effective rate. Show the normalised free cash flow."
32. **TV proportion test** — "Report terminal value as a percentage of total enterprise value. If it exceeds 75%, extend the explicit forecast until it does not, and show the revised output."
33. **Fade period** — "Insert a fade period between the explicit forecast and terminal value where returns decline toward WACC. Show the value impact versus an abrupt terminal assumption."
34. **Value-driver TV** — "Compute terminal value using the value-driver formula NOPAT × (1 − g/ROIC) / (WACC − g). Reconcile to the Gordon result and explain any difference."

## E. Bridge, sensitivity and challenge

35. **Equity bridge** — "Bridge enterprise value to equity value: less gross debt, less preferred, less minorities at fair value, less pension deficit net of tax, less other debt-like items, plus cash and equivalents, plus non-core assets, plus the value of NOLs if not already in FCF. Show every item with its source."
36. **Per-share value** — "Convert equity value to a per-share figure using fully diluted shares under the treasury method at the implied price. Iterate to convergence and show the iteration."
37. **Sensitivity grid** — "Build a WACC × terminal growth grid for implied share price. Add a second grid on EBITDA margin × revenue CAGR. Shade the base case."
38. **Scenario DCF** — "Run base, upside and downside DCFs with internally consistent driver sets — not just flexed growth. Report value, implied multiple and the probability you assign to each."
39. **Value driver ranking** — "Rank the top 10 assumptions by value impact per 1% change. Tell me which three actually decide this valuation."
40. **Reverse DCF** — "Solve for the revenue growth and margin the current market price implies. State whether the market's implied expectations are achievable."
41. **Model audit** — "Audit the model for circularity, hardcodes inside formulas, broken links, sign errors in the FCF bridge, inconsistent lease treatment, tax applied to the wrong base, and share-count mismatches. Report by severity with cell references."
42. **Defend the output** — "Write the DCF page for the board: the output range, the four assumptions that drive it, the sensitivity grid, and an honest statement of what would have to be true for this valuation to be wrong."
