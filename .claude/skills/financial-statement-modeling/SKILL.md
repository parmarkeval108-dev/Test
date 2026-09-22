---
name: financial-statement-modeling
description: Building integrated three-statement operating models - structure, linkages, working capital, debt schedules, circularity handling and model audit. Use when building an operating model, integrating statements, or auditing a model for structural errors.
---

# Financial Statement Modeling

An integrated model that balances is the minimum, not the achievement. The achievement is a model someone else can pick up and change safely.

## Techniques

1. **Architecture before build** — Fix the tab structure (inputs, drivers, statements, schedules, outputs), the periodicity, the sign convention and the colour convention before the first formula. Retrofitting structure costs more than building it.

2. **Single-input principle** — Each assumption is entered once, in one cell, on the inputs tab, and referenced everywhere else. A number typed twice will eventually disagree with itself.

3. **Row consistency** — One formula per row, copied across all periods without exception. A broken row is the defect that survives every review because it looks identical to a working one.
   *Fails when:* a one-off adjustment is typed into a single cell rather than added as its own line.

4. **Statement linkage** — Net income flows to retained earnings and to the top of the cash flow statement; every balance sheet movement appears in cash flow; closing cash flows back to the balance sheet. Build the check row — assets less liabilities less equity — before anything else and keep it visible.

5. **Working capital schedule** — Drive receivables from DSO, inventory from DIO on COGS, payables from DPO on COGS. Show the cash impact as a separate line. Flag any forecast year where days improve without a named operational reason.

6. **Rolling fixed-asset schedule** — Opening PP&E, plus capex, less depreciation on a stated useful life, less disposals at net book value, equals closing. Depreciation forecast as a percentage of revenue disconnects the asset base from the investment that creates it.

7. **Debt and interest schedule** — Per tranche: opening balance, drawdown, mandatory amortisation, optional prepayment, sweep, PIK accretion, closing balance. Interest on average balances. State whether the sweep applies before or after mandatory amortisation — the two give different answers.

8. **Circularity management** — Interest depends on debt, debt depends on cash flow, cash flow depends on interest. Resolve with an iterative-calculation switch plus a circuit breaker that zeroes the loop, or with an explicit iteration block. Document which you used and where the breaker is.

9. **Tax modelling** — Build current and deferred tax separately, with NOL carryforwards, utilisation limits and expiry. Cash tax and book tax differ, and the difference is a cash flow line, not a rounding item.

10. **Scenario switching** — Drive scenarios from a single named case selector with all case inputs held in a labelled block. Never overwrite base-case inputs to run a scenario.

11. **Check row discipline** — Balance check, cash flow tie, debt schedule tie, share count tie, and a consolidated error flag on the cover. Green means safe to use; the model is not finished until it is green in every scenario, including the downside.

12. **Sensitivity and data tables** — Build outputs as a clean, single-cell reference so data tables work. Structure the output block so that the two variables the reader cares about are the two axes.

13. **Model audit protocol** — Sweep for: hardcodes inside formulas, inconsistent rows, broken external links, sign errors, off-by-one period references, tax on the wrong base, double-counted items, and scenarios that break the balance check. Report by severity with cell references, not as a narrative.

14. **Documentation** — Cover sheet with purpose, author, date, version, key assumptions, and a change log. A model without provenance cannot be relied on six months later, including by the person who built it.

## Quality bar

- [ ] Balance check green in every scenario
- [ ] No hardcodes inside formulas
- [ ] Every row internally consistent across periods
- [ ] No external links, or all documented
- [ ] Circularity resolved with a working circuit breaker
- [ ] Cover sheet complete with version and change log

## Outputs

Integrated three-statement model, supporting schedules, scenario switch, check panel, audit report, documentation cover.
