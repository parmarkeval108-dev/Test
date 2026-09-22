---
name: dcf-and-sensitivity
description: Discounted cash flow modelling - forecast construction, unlevered free cash flow, WACC build, terminal value, the equity bridge, sensitivity and reverse DCF. Use when building or auditing a DCF, deriving a discount rate, or testing what a valuation depends on.
---

# DCF and Sensitivity Analysis

A DCF is four assumptions wearing forty. Find the four, defend them, and show what happens when they move.

> **India:** load `india-transaction-regime` before applying this skill to an Indian company — discount-rate inputs are India-specific and Section 79 usually forfeits loss carryforwards on a change of control.

## Techniques

1. **Driver-based forecasting** — Every forecast line is the output of a driver: revenue from volume × price or customers × ARPU × retention; costs split fixed/variable; capex from asset base and growth capital intensity; working capital from DSO/DIO/DPO. A growth rate typed directly into a revenue row is not a forecast.
   *Fails when:* the forecast is a set of percentage assumptions that cannot be argued with because they cannot be decomposed.

2. **Horizon selection by convergence** — Forecast explicitly until the business reaches steady state: ROIC converging toward WACC, growth toward a sustainable rate, capex toward depreciation adjusted for growth. Then stop. If terminal value exceeds 75% of EV, the horizon is too short.

3. **History anchoring** — Place five years of history beside the forecast on the same page for growth, margin, capex intensity and working capital days. Every divergence gets one sentence of justification. Most forecast errors are visible in this single view.

4. **Unlevered FCF construction** — EBIT, less cash taxes on EBIT (not on EBT), plus D&A, less capex, less the increase in working capital, plus or minus other non-cash items. Financing flows never appear. Interest never appears.
   *Fails when:* tax is taken from the levered income statement, double-counting the interest shield already in the WACC.

5. **WACC build with cited inputs** — Risk-free rate with the instrument and date; ERP with its source and study; beta with its window, frequency and index; target capital structure with its basis; pre-tax cost of debt from actual or rating-comparable issuance; marginal tax rate. An uncited WACC is an unusable WACC.

6. **Beta triangulation** — Estimate raw regression beta, Blume-adjusted beta, and peer unlevered-relevered beta, then reconcile. Peer relevering is usually right for a subject whose current leverage is not its target; state the debt-beta and tax assumptions in the relevering formula.

7. **Country risk premium** — Where cash flows are earned in higher-risk jurisdictions, add a CRP weighted by revenue or asset exposure, sized by sovereign spread or relative equity volatility. Adding it to every cash flow regardless of source overstates the adjustment.

8. **Terminal value dual method** — Compute terminal value both by perpetuity growth and by exit multiple, then cross-check each against the other: the implied exit multiple from Gordon, the implied `g` from the multiple. When either is implausible, the explicit forecast is wrong — fix that, not the terminal assumption.
   *Fails when:* an implausible implied multiple is accepted because the perpetuity growth rate "looks reasonable."

9. **Terminal-year normalisation** — In the terminal year, set capex equal to depreciation grown at `g`, working capital investment consistent with `g`, margin at steady state and tax at the full effective rate. Capitalising an un-normalised final year is the single largest source of DCF error.

10. **Value-driver terminal formula** — TV = NOPAT × (1 − g/ROIC) / (WACC − g). This forces the reinvestment consistent with growth to be explicit, and exposes any perpetuity assumption that implies growth without capital.

11. **Equity bridge discipline** — EV less gross debt, preferred, minorities at fair value and pension deficit net of tax; plus cash, non-core assets and the discounted value of NOLs if not already in the cash flows. Every item sourced and dated at the valuation date.

12. **Circular share count** — Fully diluted shares depend on the price, which depends on the per-share value. Iterate to convergence and show the iteration rather than using the market price for dilution and the DCF price for value.

13. **Sensitivity design** — Two grids: WACC × terminal growth, and the two operating drivers that actually matter. Shade the base case. A grid on variables that do not move the answer is decoration.

14. **Value-driver ranking** — Rank the top ten assumptions by value impact per 1% change. Report the three that decide the valuation. Everything else belongs in the appendix.

15. **Reverse DCF** — Solve for the growth and margin path implied by the current market price. This is the most useful single output of the model: it converts "is it cheap" into "is the market's expectation achievable."

16. **Scenario construction** — Build upside and downside from internally consistent driver sets — a downside where volume falls should show working capital release and capex deferral — not by flexing one input.

## Quality bar

- [ ] No hardcoded values inside formulas
- [ ] Circularity resolved and documented
- [ ] Lease treatment consistent across FCF, WACC and the equity bridge
- [ ] Terminal value under 75% of EV, or the horizon extended
- [ ] Implied exit multiple and implied `g` both stated and both plausible
- [ ] Sensitivity run on drivers, not on the output

## Outputs

Forecast with drivers, FCF schedule, WACC build with sources, terminal value under both methods, equity bridge, sensitivity grids, value-driver ranking, reverse-DCF read.
