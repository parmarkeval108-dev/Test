# Comparable Companies Prompts

**Layer:** Insight · **Engagement contexts:** M&A Advisory, ECM, Fairness Opinions & Valuations
**Pairs with:** `skills/comparable-company-analysis`, `agents/trading-comps-agent`, `workflows/valuation.md`

## A. Building the comp set

1. **Select the comp set** — "Build a trading comp set for `<Company>`. For each candidate give business-model similarity, size, growth, margin, geography and capital intensity, then state include/exclude with a reason. Comparability is a claim you must defend, not an assertion."
2. **Defend the exclusions** — "List every company a reviewer might expect in this comp set that you excluded, and the specific reason each was excluded. Assume the reviewer is hostile."
3. **Tiered comp set** — "Split the set into core comps (direct), secondary comps (partial overlap) and reference comps (read-across only). Compute medians separately for each tier."
4. **Business-mix weighting** — "`<Company>` is `<X>`% `<segment A>` and `<Y>`% `<segment B>`. Build a sum-of-the-parts comp set with a distinct peer group per segment and a blended implied multiple."
5. **Geographic comparability** — "Assess whether `<region>` peers are valid comps for `<Company>` given differences in growth, tax, cost of capital, disclosure standards and index membership. Quantify the discount if one is warranted."
6. **Size-effect check** — "Test whether valuation multiples in this set correlate with market cap. If they do, state the implied size adjustment for `<Company>` and show the regression."
7. **Liquidity screen** — "Screen the comp set for thin trading: average daily volume, free float, analyst coverage. Flag any name whose multiple should not be trusted."
8. **Index-inclusion effect** — "Identify which comps are in major indices and assess whether index membership is inflating multiples relative to `<Company>`, which is not a member."

## B. Data integrity and normalisation

9. **Calendarise** — "Calendarise all comps to a December year-end. Show the interpolation method and flag any company where stub-period estimates make the result unreliable."
10. **Reconcile to filings** — "For every comp, tie revenue, EBITDA, net debt and share count back to the primary filing. Produce a reconciliation table with page or note references. List any figure you could not tie."
11. **Diluted share count** — "Compute fully diluted shares for each comp using the treasury stock method. Include options, RSUs, PSUs at expected achievement, convertibles (if-converted where dilutive) and warrants."
12. **Net debt bridge** — "Build the enterprise value bridge for each comp: market cap, plus gross debt, plus preferred, plus minorities at fair value, plus pension deficit net of tax, plus capitalised leases where not already in debt, less cash and equivalents, less non-core assets. Show every line."
13. **Lease treatment consistency** — "Confirm every comp treats leases the same way post-IFRS 16/ASC 842/Ind AS 116. Where filers under different standards sit in the same set, restate to a common basis and show the effect on EV/EBITDA."
14. **Pension and OPEB** — "Quantify each comp's net pension deficit, the tax rate applied, and whether the deficit is debt-like. Show the multiple with and without."
15. **Minorities and associates** — "For comps with material minorities or equity-method stakes, adjust EV and the earnings measure consistently. State the value you assigned to each stake and your method."
16. **Adjusted vs reported** — "For each comp, compare management-adjusted EBITDA to reported. Tabulate the add-backs, and recompute multiples on a consistent definition of your own choosing."
17. **Non-recurring items** — "Identify non-recurring items in each comp's last three years. Decide which to normalise and apply the same rule to `<Company>`. Inconsistency here is the most common review finding."
18. **Capitalised costs** — "Compare R&D and software capitalisation policies across the set. Restate to a common policy and show the multiple impact."
19. **SBC treatment** — "Show each comp's multiple with stock-based compensation expensed and excluded. State which convention the sector uses and which you have adopted."
20. **Currency consistency** — "Convert all comps to `<currency>` using period-average rates for flows and spot for balances. Disclose the rates used."
20a. **Reporting basis (India and similar markets)** — "Where issuers report both standalone and consolidated financials, state which basis you have used, apply it to every company including the subject, and flag any peer where the two differ materially."
21. **Consensus estimate hygiene** — "For forward multiples, state the estimate source, the number of contributing analysts, the estimate date, and whether any estimate predates the last earnings release. Exclude stale consensus."

## C. Analysis and presentation

22. **Core multiple table** — "Build the comp table: EV/Revenue, EV/EBITDA, EV/EBIT, P/E and EV/FCF for LTM, FY+1 and FY+2, plus growth, margin, leverage and ROIC. Include mean, median, 25th and 75th percentile."
23. **Sector-specific multiples** — "Add the metrics this sector actually trades on: `<e.g. EV/ARR, EV/EBITDAR, P/TBV, EV/Subscriber, EV/kW, FFO multiple>`. Explain why each matters here."
24. **Growth-adjusted multiples** — "Compute EV/EBITDA divided by forward EBITDA growth, and PEG, for the set. Assess whether `<Company>`'s discount survives the growth adjustment."
25. **Regression valuation** — "Regress EV/EBITDA against EBITDA margin and forward growth across the set. Report R², coefficients and the implied multiple for `<Company>`. State plainly whether the R² justifies using it."
26. **Outlier treatment** — "Identify outliers using the interquartile rule. For each, decide to keep, exclude or winsorise — and show the medians under all three treatments."
27. **Mean vs median** — "Show the implied value using mean and median. Where they diverge by more than 10%, explain what is driving the skew and which you recommend."
28. **Trading history** — "Chart `<Company>`'s EV/EBITDA against the peer median over 5 years. Quantify the average premium/discount and identify when and why the relationship broke."
29. **Re-rating diagnosis** — "`<Company>` traded at a `<X>`x premium in `<year>` and a discount now. Decompose the de-rating into earnings revisions, multiple compression and peer-set drift."
30. **Implied valuation** — "Apply the peer median and quartile multiples to `<Company>`'s metrics and output implied enterprise value, equity value and per-share value. Show the net debt and share count used."
31. **Football field input** — "Produce the trading-comps bar for the football field: low, median, high, with the driver of each end labelled in six words or fewer."
32. **Sensitivity grid** — "Build a grid of implied share price across EV/EBITDA multiples `<range>` and EBITDA outcomes `<range>`. Shade the cells consistent with the base case."
33. **Cross-check against DCF** — "Compare the comps range to the DCF output. Where they disagree by more than 15%, identify which assumption in the DCF is inconsistent with what the market is paying."
34. **Implied perpetuity growth** — "Back out the perpetuity growth rate implied by the peer median multiple at `<Company>`'s WACC. Comment on whether the market's implied growth is plausible."

## D. Review, challenge and delivery

35. **Premium/discount rationale** — "Argue, in 200 words, why `<Company>` deserves a premium to the peer median. Then argue the opposite with equal force. Then tell me which argument the evidence supports."
36. **Comp-set stress test** — "Recompute the implied value under three alternative comp sets: narrowest defensible, broadest defensible, and the one the counterparty will propose. Report the spread."
37. **Counterparty's comps** — "The other side used this comp set `<list>`. Identify every methodological difference from ours, quantify the effect of each, and reconcile the two outputs line by line."
38. **Fairness-opinion support** — "Document this comp analysis to fairness-opinion standard: selection criteria, sources, dates, calculation conventions, adjustments and the reason for every judgement call."
39. **Audit trail** — "Produce a source log for every input: company, metric, value, source document, page, retrieval date. Flag anything from a secondary source."
40. **Common-error sweep** — "Check this comp analysis for the standard errors: mismatched period alignment, EV/equity metric mismatch, share counts on different dates, double-counted leases, stale consensus, currency mixing, minority inconsistency. Report findings with severity."
41. **Client page** — "Turn this analysis into a single client-ready page: the comp table, the implied range, three observations, and one footnote per methodological choice. No unexplained figure on the page."
42. **Committee Q&A** — "Write the ten questions the investment committee will ask about this comp set and the answer to each, with the supporting number."
