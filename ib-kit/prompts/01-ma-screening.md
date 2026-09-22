# M&A Screening Prompts

**Layer:** Insight · **Engagement contexts:** M&A Advisory, Strategic Alternatives, Restructuring
**Pairs with:** `skills/screening-and-targeting`, `agents/target-screening-agent`, `workflows/deal-screening.md`

Replace `<>` placeholders before running. Every prompt assumes you will demand a source for each number.

## A. Universe construction

1. **Define the screening universe** — "Build the screening universe for `<Client>`'s acquisition program in `<sector>`. Start from SIC/NAICS `<codes>`, then add adjacency by product, channel and end-market. Output a table with company, country, ownership status, revenue, EBITDA, and the one-line reason it is in scope. Separately list what you deliberately excluded and why."
2. **Adjacency mapping** — "Map three rings of adjacency around `<Client>`'s core business: same customer/different product, same product/different customer, and same capability/different market. Name 10 candidates per ring."
3. **Value-chain sweep** — "Lay out the `<sector>` value chain from raw input to end customer. For each stage, name the top 5 independent players and mark which stages `<Client>` does not own today."
4. **Capability gap screen** — "List the 8 capabilities `<Client>` says it needs in its `<year>` strategic plan. For each, identify targets that would close the gap through acquisition rather than build, and estimate build-vs-buy timing."
5. **White-space geography screen** — "Identify countries where `<Client>` has under `<X>`% share but the market grows above `<Y>`%. Name the top 3 acquirable platforms in each."
6. **Sponsor-owned inventory** — "List `<sector>` assets held by financial sponsors with holding periods above 4 years. Include fund name, fund vintage, entry date, estimated entry multiple, and likelihood of a `<year>` exit."
7. **Founder/succession screen** — "Screen `<sector>` for founder- or family-owned businesses where the principal is over 60, there is no evident successor, and revenue exceeds `<$X>`m. Flag the succession signal you relied on."
8. **Carve-out screen** — "Identify divisions inside `<sector>` public companies that are sub-scale, margin-dilutive, or off-strategy relative to the parent's stated focus. Rank by carve-out feasibility and standalone-cost risk."
9. **Distress screen** — "Screen `<sector>` for companies with net leverage above `<X>`x, a maturity inside 18 months, or a covenant headroom below 15%. Separate operational distress from balance-sheet distress."
10. **Take-private screen** — "Screen listed `<sector>` companies trading below `<X>`x EBITDA with free float under `<Y>`%, stable cash conversion, and no controlling shareholder that would block a bid."
11. **Roll-up fragmentation test** — "Assess whether `<sub-sector>` supports a roll-up: measure top-5 share, count of sub-$50m-revenue operators, regional density, and multiple arbitrage between platform and tuck-in pricing."
12. **Reverse screen from the buyer** — "Work backwards: given `<Client>`'s balance sheet capacity of `<$X>`m and a maximum `<Y>`x pro forma leverage, define the size envelope of deals it can actually do, then screen only inside that envelope."

## B. Scoring and prioritisation

13. **Weighted screening scorecard** — "Score each target 1–5 on strategic fit, financial quality, integration difficulty, deliverability and valuation risk. Publish the weights first, then the scores, then a sensitivity showing which rankings flip if weights move ±10 points."
14. **Tier the list** — "Sort the universe into Tier 1 (pursue now), Tier 2 (monitor), Tier 3 (out). Write one sentence of justification per company and name the single fact that would promote a Tier 2 to Tier 1."
15. **Deliverability screen** — "For each Tier 1 target, assess shareholder willingness to sell, board composition, any standstill or lock-up, regulatory posture, and whether a competing bidder is likely. Score deliverability separately from desirability."
16. **Strategic-fit narrative** — "For `<Target>`, write the 150-word strategic rationale a CEO would give the board, then write the 150-word version a sceptical director would give in rebuttal."
17. **Screen hygiene check** — "Audit this screening list for survivorship bias, stale financials, double-counted subsidiaries, and companies already under exclusivity. Report what is wrong before you report what is good."
18. **Anti-target list** — "Name the targets `<Client>` should explicitly decide not to pursue, and the disqualifying fact for each, so the board stops re-asking about them."
19. **Cost of delay** — "For each Tier 1 target, estimate what changes if `<Client>` waits 12 months: likely acquirer, likely price movement, likely loss of optionality."
20. **Competitive tension map** — "For each Tier 1 target, name the other 3–5 credible acquirers and what each would pay for. Identify where `<Client>` has a genuine willingness-to-pay advantage."
21. **Scarcity ranking** — "Rank targets by scarcity: how many comparable assets of this quality exist, and how often do they come to market? Distinguish genuinely unique assets from ones with substitutes."
22. **Portfolio-fit test** — "Test each target against `<Client>`'s existing portfolio for channel conflict, customer overlap, brand cannibalisation and cultural distance."

## C. Target financial quick-cuts

23. **One-page target profile** — "Produce a one-page profile of `<Target>`: business description, ownership, 3-year financials, growth and margin trajectory, end markets, top customers, management, known transaction history, and three questions you cannot answer from public sources."
24. **Quality of growth** — "Decompose `<Target>`'s revenue growth into organic volume, price, mix, FX and acquisition. State which sources you used for each and where you had to estimate."
25. **Margin bridge** — "Build a gross-to-EBITDA margin bridge for `<Target>` across `<years>`. Attribute each move to a driver and flag which are structural versus cyclical."
26. **Cash conversion quick-cut** — "Compute `<Target>`'s EBITDA-to-FCF conversion for `<years>`. Identify the largest leakage — working capital, capex, tax, leases — and whether it is fixable by an acquirer."
27. **Normalised EBITDA** — "Build a normalised EBITDA bridge for `<Target>`: reported EBITDA, then each add-back with its amount, its evidence and a credibility rating. Total the add-backs you would refuse to underwrite."
28. **Customer concentration** — "Assess `<Target>`'s customer concentration, contract tenure, renewal mechanics and churn. State the revenue at risk if the top customer left and how long the exit would take."
29. **Balance-sheet screen** — "Summarise `<Target>`'s capital structure: gross and net debt, maturity wall, pricing, covenants, pensions, leases, off-balance-sheet items, and any change-of-control provision."
30. **Capex intensity** — "Compare `<Target>`'s maintenance versus growth capex to peers. Assess whether reported maintenance capex is credible against asset age and depreciation."
31. **Working-capital seasonality** — "Chart `<Target>`'s quarterly working capital. Identify peak-to-trough swing and the funding it implies for an acquirer at closing."
32. **Preliminary valuation range** — "Produce an indicative value range for `<Target>` on trading comps, precedent transactions and a rough DCF. Present as a football field with the driver of each end of the range."
33. **Affordability test** — "At a `<X>`% premium to `<Target>`'s current value, test whether `<Client>` can fund the deal within its leverage and rating constraints. Show the funding mix required."
34. **Accretion pre-screen** — "Before any modelling, tell me directionally whether acquiring `<Target>` is accretive to `<Client>`'s EPS, using only P/E differential, funding cost and estimated synergies. Show the arithmetic in four lines."

## D. Sourcing intelligence and monitoring

35. **Trigger-event monitor** — "Define the observable trigger events that would signal `<Target>` is coming to market — CFO change, auditor change, adviser hire, sponsor fund-life, segment reporting change, capex pause — and set out how to monitor each."
36. **Ownership unwind** — "Map `<Target>`'s full ownership: shareholders above 3%, management holdings, ESOP, any shareholder agreement, and who actually controls a sale decision."
37. **Prior-process history** — "Research whether `<Target>` has run a prior sale process. Identify when, who advised, who bid, why it failed and what would need to be different now."
38. **Relationship map** — "Map existing relationships between `<Client>`'s leadership and `<Target>`'s board, management and owners. Recommend the warmest credible path to a first conversation."
39. **Approach strategy** — "Draft the approach strategy for `<Target>`: who calls whom, in what sequence, what is said in the first 5 minutes, and what the fallback is if rebuffed."
40. **Inbound triage** — "Triage this inbound teaser against `<Client>`'s stated criteria. Give a pursue / pass / park recommendation in under 200 words with the three facts that drove it."
41. **Pipeline review pack** — "Summarise the current pipeline for the monthly corp-dev review: stage, owner, next action, date of next action, and the deals that have not moved in 60 days."
42. **Screening memo** — "Write the screening memo for `<Client>`'s investment committee: universe and method, screening criteria and weights, the resulting Tier 1 list, the three targets you recommend approaching, and a clear statement of what this screen cannot tell them."
