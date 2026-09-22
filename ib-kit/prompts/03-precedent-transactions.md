# Precedent Transaction Prompts

**Layer:** Insight · **Engagement contexts:** M&A Advisory, Fairness Opinions & Valuations, Restructuring
**Pairs with:** `skills/precedent-transaction-analysis`, `agents/precedent-transactions-agent`, `workflows/valuation.md`

## A. Building the transaction set

1. **Assemble the set** — "Build a precedent transaction set for a sale of `<Company>`. Cover `<years>` years in `<sectors>` and `<geographies>`. Per deal: date announced, date closed, target, acquirer, acquirer type, consideration mix, deal value, EV/Revenue, EV/EBITDA, premium paid, and source. Mark every estimated figure."
2. **Justify the window** — "State why the lookback window is `<X>` years. Identify what changed at the boundary — rates, regulation, sector cycle — and show medians for the period inside and outside."
3. **Strategic vs sponsor split** — "Split the set by acquirer type. Report medians for each and quantify the strategic premium. Explain what it buys."
4. **Size banding** — "Band the set by deal value. Test whether multiples rise with size and state the implied read for a `<$X>`m transaction."
5. **Control-transaction filter** — "Retain only transactions conveying control (above 50% or effective control). List minority-stake deals separately and explain why they are not directly comparable."
6. **Process-type tagging** — "Tag each deal as broad auction, targeted process, bilateral negotiation, or hostile/unsolicited. Compare multiples across process types."
7. **Distressed carve-out** — "Separate distressed and insolvency transactions (US 363 sales, UK administrations, India IBC resolutions) from the main set. Report both medians and explain when the distressed set is the relevant benchmark."
8. **Failed deals** — "List announced transactions in the set that did not close. Give the reason each failed — financing, regulatory, shareholder vote, MAC — and what it implies for deliverability here."
9. **Cross-border subset** — "Identify cross-border deals in the set. Assess whether foreign acquirers paid a premium and whether FDI screening lengthened timelines."
10. **Data availability audit** — "For each deal, state whether the multiple is disclosed, derived from filings, or a press estimate. Compute the medians using disclosed-only, then all. Report both."

## B. Normalising the multiples

11. **Rebuild deal EV** — "For each transaction, rebuild enterprise value from the offer terms: equity consideration, assumed debt, cash acquired, earn-out at expected value, rollover equity, preferred, minorities, transaction fees. Do not trust the press number."
12. **LTM basis** — "Confirm whether each multiple uses LTM-at-announcement, LTM-at-close, or forward EBITDA. Restate all to LTM-at-announcement and show the effect."
13. **Synergy-inclusive multiples** — "Identify deals where the disclosed multiple is post-synergy. Restate to pre-synergy and show both."
14. **Earn-out treatment** — "For deals with earn-outs, show the multiple at minimum, expected and maximum consideration. State which you use in the median and why."
15. **Contingent and deferred consideration** — "Discount deferred consideration to announcement-date present value at `<rate>` and restate the multiple."
16. **Equity consideration valuation** — "For stock or mixed deals, value the equity component at the announcement-date price, then at the closing-date price, and report the difference."
17. **Adjusted-EBITDA scrutiny** — "Where the target's EBITDA in the announcement was adjusted, list the add-backs and recompute on reported EBITDA. Report the multiple gap."
18. **Currency and inflation** — "Convert all deal values to `<currency>` at announcement-date spot. Separately show values indexed to `<year>` money and comment on whether it changes the read."

## C. Premium analysis

19. **Premium reference dates** — "For public targets, compute premia to the 1-day, 5-day, 30-day and 90-day VWAP prior to announcement, and to the 52-week high. Report all four — a single premium figure is an incomplete answer."
20. **Leak adjustment** — "Identify deals with evidence of pre-announcement leakage — abnormal volume or price run-up. Compute the premium to the unaffected price and state how you determined the unaffected date."
21. **Premium drivers regression** — "Regress premium against target size, acquirer type, consideration mix, competing bidders and deal-year rate environment. Report what actually explains premia in this sector."
22. **Competing-bid effect** — "Isolate transactions with a confirmed competing bidder. Quantify the incremental premium tension delivered."
23. **Bump analysis** — "For deals where the price was raised after the initial offer, chart initial versus final premium and the average number of raises."
24. **Minority squeeze-out premia** — "Build a separate premium set for minority buy-ins and controlling-shareholder transactions, where premia follow different norms."

## D. Deal-terms intelligence

25. **Consideration mix trend** — "Chart cash/stock/mixed consideration across the window. Explain the shift by reference to acquirer currency strength and financing conditions."
26. **Financing conditionality** — "Report how many deals carried a financing condition, and how this varies by acquirer type and year."
27. **Break fees** — "Compute target and reverse break fees as a percentage of equity value across the set. Report median by deal size and by regulatory risk level."
28. **Regulatory conditions** — "Catalogue the antitrust, FDI and sector-regulator conditions in each deal, the remedies offered, and the time from signing to closing."
29. **MAC definitions** — "Compare material adverse change clauses across the set. Identify the carve-outs that became market standard and any deal where MAC was invoked."
30. **Timeline benchmark** — "Compute median days from announcement to closing, split by whether an in-depth review occurred (US second request, EU/UK Phase 2, India CCI Phase II). Use it to set expectations for `<Company>`."
31. **Rollover and management terms** — "For sponsor deals, summarise management rollover percentages, option pool sizes and vesting terms."
32. **Escrow and W&I** — "Report typical escrow size and tenor, and the shift toward warranty and indemnity insurance across the window."

## E. Application and review

33. **Apply to the target** — "Apply the precedent median and quartiles to `<Company>`'s LTM metrics. Output implied EV, equity value and per-share value, showing net debt and share count."
34. **Select the most relevant deals** — "From the full set, identify the 5 most relevant transactions and write 100 words per deal on why it is the closest read for `<Company>`."
35. **Adjust for market conditions** — "Deals in `<period>` were struck at `<X>`x with `<benchmark rate>` at `<Y>`%. Adjust the implied multiple for today's rate and credit environment and show the arithmetic."
36. **Cycle positioning** — "Place each deal on the sector cycle at its announcement date. State where we are now and which subset of deals is the right benchmark."
37. **Precedents vs trading comps** — "Explain the gap between the precedent median and the trading-comp median for `<Company>`. Decompose it into control premium, synergy capitalisation and market drift."
38. **Buy-side counter-brief** — "You are advising the buyer. Identify the three precedents we cited that they will attack, and the attack on each. Then prepare our response."
39. **Fairness-opinion documentation** — "Document the transaction set to fairness-opinion standard: selection criteria, exclusions with reasons, sources, calculation conventions, and every judgement call."
40. **Source audit** — "Produce a source log for each deal: value, metric, source, document date, and whether disclosed or estimated. Flag any deal resting on a single press report."
41. **Football field input** — "Produce the precedent-transactions bar: low, median, high, with the deal driving each endpoint named."
42. **Board page** — "Write the precedent transactions page for the board deck: the table, the implied range, three observations on what the market is paying, and an explicit statement of the set's limitations."
