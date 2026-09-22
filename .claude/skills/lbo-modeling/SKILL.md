---
name: lbo-modeling
description: Leveraged buyout modelling - sources and uses, capital structure design, debt schedules and sweeps, returns attribution, covenant headroom and downside testing. Use when modelling an LBO, sizing leverage, testing sponsor ability-to-pay, or structuring acquisition financing.
---

# LBO Modeling

An LBO model answers two questions: what can be paid, and what survives the downside. Everything else is supporting detail.

## Techniques

1. **Sources and uses discipline** — Uses: equity purchase price, refinanced debt, transaction fees, financing fees, minimum cash at close. Sources: each tranche at its committed size, sponsor equity as the plug, rollover, and any preferred. It balances to the cent or the model is wrong somewhere else too.

2. **Three-test leverage sizing** — Maximum leverage is the lowest of what the market will lend at this rating and sector, what cash flow services with adequate coverage cushion, and what the business survives in a downside. The binding test is the answer; name which one it is.
   *Fails when:* leverage is set from a market benchmark alone, with no downside test behind it.

3. **Tranche design** — Allocate across revolver, TLA, TLB, second lien, senior notes, subordinated and preferred according to current appetite for this credit. Each tranche gets size, base rate, spread, floor, OID, call protection, amortisation and tenor.

4. **Credit-agreement EBITDA** — Define EBITDA as the credit agreement will: reported, plus permitted add-backs, plus run-rate synergies subject to a cap and a look-forward period. Track the gap between credit EBITDA and cash EBITDA — that gap is the real covenant headroom question.

5. **Debt schedule and waterfall** — Per tranche per period: opening, mandatory amortisation, sweep, optional prepay, PIK accretion, closing. Sweep applies through the waterfall in priority order with leverage-based step-downs. Interest on average balances.

6. **Revolver and minimum cash** — The revolver is drawn to hold cash at the minimum, repaid from surplus, charged an undrawn commitment fee, and carries the springing covenant above a stated utilisation. Model it as mechanics, not as a plug.

7. **Forward-curve interest** — Use the forward curve for the base rate rather than a flat assumption, and show the difference. Flat-rate assumptions have understated interest cost through every rate cycle.

8. **Returns attribution** — Decompose MOIC into EBITDA growth, multiple expansion or contraction, debt paydown and cash generation. State what share of the return comes from leverage alone. A return that is 70% leverage is a different investment from one that is 70% operational.
   *Fails when:* the deal is justified by an exit multiple above entry with no argument for the re-rating.

9. **Ability-to-pay solve** — Solve for the entry multiple delivering the sponsor's hurdle at a conservative exit. This is the floor of a financial bidder's range and the number that tells a seller whether sponsors can compete with strategics.

10. **Waterfall and MIP** — Model the exit waterfall through preferred, sponsor common, rollover and the management incentive plan with its hurdle and vesting. Report returns gross and net of carry.

11. **Covenant headroom tracking** — Compute headroom per covenant per period in both percentage and dollar-EBITDA terms. The dollar figure is what the credit committee reacts to.

12. **Downside and break-even** — Solve for the EBITDA decline at which covenants breach, at which cash interest is not covered, and at which equity is worthless. Report all three. The gap between the first and third is the margin for error.

13. **Liquidity runway** — In the downside, compute months of liquidity from cash plus revolver availability and identify the first funding shortfall. Covenant breach is survivable; running out of cash is not.

14. **Recovery analysis** — At a distressed exit multiple, run the waterfall to each tranche and report recovery percentages. This is what prices the debt and what a restructuring negotiation starts from.

15. **Add-on and multiple arbitrage** — Model add-ons at their own entry multiple against the platform's exit multiple, showing the arbitrage contribution to returns and the incremental leverage capacity consumed.

16. **Dividend recap** — Model a re-levering in a stated year with the IRR uplift, the residual equity value and the incremental default probability shown together. The uplift is never free.

## Quality bar

- [ ] Sources and uses balances exactly
- [ ] Circularity resolved with a working circuit breaker
- [ ] Interest computed on average balances
- [ ] Sweep priority and step-downs explicit
- [ ] Downside case run and the first breach period identified
- [ ] Returns attributed, not just reported

## Outputs

Sources and uses, capital structure summary, operating cases, debt schedule, credit statistics, covenant headroom, returns grid and attribution, downside and recovery analysis.
