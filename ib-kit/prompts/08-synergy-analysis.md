# Synergy Analysis Prompts

**Layer:** Insight · **Engagement contexts:** M&A Advisory, Strategic Alternatives
**Pairs with:** `skills/synergy-quantification`, `agents/synergy-analysis-agent`, `workflows/post-close-transition.md`

## A. Identification

1. **Full synergy inventory** — "Build the complete synergy inventory for `<Acquirer>` + `<Target>`. For each item: category, description, gross annual value, the driver it is calculated from, the year of full run-rate, the one-time cost to achieve, the owner, and a confidence rating of high/medium/low with the reason. No item without a driver."
2. **Cost synergies by function** — "Identify cost synergies by function: corporate/public-company costs, overlapping management, finance, HR, IT, legal, procurement, manufacturing footprint, distribution, sales overlap, marketing, R&D. Size each from headcount or spend data, not percentages."
3. **Procurement synergies** — "Quantify procurement savings from combined spend: overlapping categories, combined volume, current price differential between the two companies, and the achievable negotiated rate. Show the category-level build."
4. **Footprint rationalisation** — "Map both companies' facilities. Identify closure candidates, the capacity they represent, the receiving sites, the annual saving, and the closure cost including severance and lease exit."
5. **Headcount synergies** — "Build the headcount synergy from the combined org chart: duplicate roles by level and function, fully loaded cost per role, severance per role, and the retention risk in each affected team."
6. **Public-company cost elimination** — "Quantify elimination of `<Target>`'s public-company costs: listing fees, audit, investor relations, board compensation, D&O insurance, and listed-compliance costs (SOX, or SEBI LODR in India). This is the most credible synergy — size it precisely."
7. **Revenue synergies — cross-sell** — "Quantify cross-sell: `<Acquirer>`'s product into `<Target>`'s customer base. Show addressable accounts, realistic attach rate with the evidence for it, average deal size, gross margin and ramp period."
8. **Revenue synergies — channel** — "Quantify revenue from putting `<Target>`'s product through `<Acquirer>`'s distribution: reach gained, conversion assumption, margin, and the time to enable the channel."
9. **Revenue synergies — pricing** — "Assess pricing synergy from reduced competitive intensity. State the antitrust risk of relying on it and whether it can be disclosed."
10. **Geographic expansion** — "Quantify revenue from using `<Target>`'s footprint to enter `<markets>`: market size, share assumption, time to reach it, and the investment required."
11. **Capability and product synergies** — "Identify combined product or R&D opportunities. Quantify revenue, timing and the development cost, and be explicit that these are the least reliable class of synergy."
12. **Capital synergies** — "Quantify balance-sheet synergies: working capital from combined terms and inventory pooling, capex avoidance from shared facilities, and reduced cost of debt from scale and diversification."
13. **Tax synergies** — "Identify tax synergies: NOL utilisation, interest deductibility capacity, transfer pricing, and structural rate optimisation. State the substance requirement and the risk of challenge for each."
14. **Negative synergies** — "Identify dis-synergies: customer overlap loss, channel conflict, revenue attrition during integration, talent departure, contract renegotiation on change of control, and lost focus. Quantify each. A synergy case without dis-synergies is not credible."

## B. Quantification discipline

15. **Bottom-up rebuild** — "Rebuild every synergy from first-principles drivers — headcount, spend, volume, accounts — and delete any line expressed as a percentage of a cost base."
16. **Benchmark the total** — "Express total cost synergies as a percentage of target operating costs, target revenue, and combined overlapping cost base. Benchmark against comparable deals in `<sector>` and flag any metric above the 75th percentile."
17. **Evidence grading** — "Grade every synergy line: A = contractually verifiable, B = supported by data-room data, C = management assertion, D = analyst judgement. Report the total by grade and treat only A and B as underwritable."
18. **Phasing schedule** — "Build the quarterly phasing of run-rate synergy realisation over 3 years for each line, driven by the specific action required — notice periods, contract expiries, system migrations — not a smooth curve."
19. **Cost to achieve** — "Build the cost-to-achieve schedule by category: severance, retention, facility exit, IT integration, systems, advisers, rebranding, dual-running. Express the total as a multiple of run-rate synergies and benchmark it."
20. **Net present value** — "Compute the NPV of synergies net of costs to achieve, discounted at `<rate>`, with a terminal value only for the synergies that genuinely persist. Justify which ones do."
21. **Probability weighting** — "Apply a probability weighting to each synergy line based on its evidence grade. Report the gross figure, the risk-adjusted figure, and the figure you would be willing to announce."
22. **Announce vs underwrite** — "Split the synergy total into three numbers: what we underwrite internally, what we announce publicly, and what we tell the seller we can pay for. Explain the gap between them."

## C. Deliverability and integration

23. **Dependency mapping** — "For each synergy above `<$X>`m, map its dependencies: systems, approvals, contracts, consents, regulatory clearance. Identify which synergies cannot start until closing plus `<N>` months."
24. **Regulatory constraint** — "Identify synergies that antitrust review may prohibit or that gun-jumping rules prevent us from pursuing pre-close. Flag anything that cannot be discussed with the target before clearance."
25. **Owner assignment** — "Assign each synergy an accountable executive by name and role, with a delivery date and the measure that proves delivery. Unowned synergies do not get counted."
26. **Integration plan alignment** — "Reconcile the synergy plan to the integration workstream plan. Identify every synergy with no corresponding workstream — that is a gap."
27. **Retention risk** — "Identify the people whose departure would destroy specific synergies. Quantify the value at risk and design the retention package."
28. **Customer attrition model** — "Model customer attrition post-close by segment using comparable-deal evidence. Net this against revenue synergies before presenting any revenue synergy number."
29. **Timeline realism test** — "Compare this synergy phasing to actual realisation curves in `<N>` comparable deals. State where our plan is faster than any observed precedent and justify it."
30. **Systems integration dependency** — "Assess which synergies require ERP or CRM consolidation. Estimate that programme's duration and cost from comparable integrations, and re-phase the dependent synergies."

## D. Challenge and validation

31. **Red-team the case** — "Attack this synergy case as a sceptical board member. Identify double-counting across categories, savings already in the target's standalone plan, one-time savings presented as recurring, and revenue synergies without a named customer."
32. **Already-in-plan test** — "Cross-check every cost synergy against `<Target>`'s own standalone cost programme. Any saving already in their plan is not a deal synergy — quantify the overlap."
33. **Diligence verification plan** — "For each synergy above `<$X>`m, specify exactly what document or data request in diligence would verify it. Produce it as a numbered information request."
34. **Post-diligence restatement** — "Given these diligence findings `<findings>`, restate the synergy case. Show the original figure, the revised figure and the reason for every movement."
35. **Value split** — "Compute what percentage of synergy NPV is being paid to the seller through the premium. State the acquirer's retained share and compare to sector precedent."
36. **Premium justification** — "Test whether the premium is justified by synergies alone: premium paid versus risk-adjusted synergy NPV. If the premium exceeds it, state what else must be true for the deal to create value."
37. **Sensitivity** — "Show value creation across synergy realisation of 50%, 75%, 100% and 125% of target, crossed with costs-to-achieve at 1x, 1.5x and 2x run-rate."
38. **Comparable-deal outcome study** — "Study `<N>` comparable deals where synergy targets were publicly announced. Report actual delivery versus target, the time taken, and the common reason for shortfall."

## E. Communication and tracking

39. **Announcement figure** — "Recommend the synergy figure to announce: the amount, the phasing, the cost to achieve, and the language. Balance credibility against the risk of setting a target we miss."
40. **Synergy tracker design** — "Design the post-close synergy tracker: line items, owners, monthly targets, actuals, the validation rule that lets a saving be booked, and the escalation trigger for a line behind plan."
41. **Board page** — "Produce the synergy page for the board: the category summary, the phasing chart, the cost to achieve, the evidence grading, and an explicit statement of what we are not counting."
42. **Analyst defence pack** — "Prepare the answers to the ten hardest analyst questions on this synergy case, each backed by a specific driver and a specific piece of evidence."
