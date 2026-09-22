---
name: scenario-and-stress-testing
description: Scenario design, stress testing, sensitivity analysis and Monte Carlo for transaction models - building internally consistent cases, finding break points, and reverse stress testing. Use when testing what a deal depends on, building downside cases, or preparing risk sections.
---

# Scenario and Stress Testing

A sensitivity flexes one input. A scenario tells a coherent story about the world. Boards make decisions on scenarios and get comfortable with sensitivities.

## Techniques

1. **Internally consistent case construction** — In a downside, volume falls, so working capital releases, capex is deferred, variable costs fall and the sweep slows. Flexing revenue alone while holding everything else produces a case no operator recognises.
   *Fails when:* the downside case shows a margin the business has never achieved at that volume.

2. **Driver-level scenario definition** — Define each case by its drivers — volume, price, input cost, rates, FX — not by its outputs. State the narrative in three sentences before touching a number.

3. **Probability assignment** — Assign explicit probabilities to each case and compute the probability-weighted outcome. Forcing the assignment exposes cases nobody actually believes and cases that should be the base.

4. **Break-point solving** — Rather than testing chosen scenarios, solve for the level at which something breaks: covenant breach, negative FCF, liquidity exhaustion, equity wipeout, rating downgrade. The break point is more useful than any scenario because it is a fact about the structure.

5. **Reverse stress testing** — Start from failure and work back: what combination of conditions destroys this investment, and how plausible is that combination? Regulators require this of banks for good reason — it surfaces risks that forward scenarios miss.

6. **Single-variable sensitivity with ranking** — Flex each material assumption by ±10% and rank by output impact. The tornado chart tells you where to spend diligence money.

7. **Two-way grids on the variables that matter** — Grid only the two drivers with the largest impact. Grids on immaterial variables give false comfort through apparent thoroughness.

8. **Correlated shock design** — Real downturns move variables together: demand falls while input costs rise and credit tightens. Build correlation into the downside explicitly, with the historical episode you are drawing on named.

9. **Historical analogue stress** — Run the model through an actual past episode using that period's observed moves in this sector. This is more defensible than an invented percentage decline because it happened.

10. **Monte Carlo where distributions are knowable** — Where inputs have genuine empirical distributions, simulate and report the outcome distribution, the probability of loss and the fifth-percentile outcome. Where distributions are guessed, the simulation manufactures false precision — say so and use scenarios instead.

11. **Liquidity-first stress** — Test cash before earnings. Businesses fail when they run out of cash, often while still profitable. Report the minimum liquidity month and the headroom at that point.

12. **Duration stress** — Test not just depth but length: a 15% decline for one year and the same decline for three years are different investments. Most models are only ever tested on the first.

## Quality bar

- [ ] Scenarios defined by drivers with a stated narrative
- [ ] Probabilities assigned and summing to one
- [ ] Break points solved and reported, not just scenarios run
- [ ] Downside internally consistent across P&L, balance sheet and cash flow
- [ ] Liquidity tested separately from earnings
- [ ] Balance check green in every case

## Outputs

Scenario definitions with narratives and probabilities, tornado chart, two-way grids, break-point table, reverse stress test, liquidity runway.
