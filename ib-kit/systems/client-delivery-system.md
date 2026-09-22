# The Claude Client Delivery System

**Layer:** Impact Engine  ·  **Purpose:** deliver high-impact materials and track performance

The Client Delivery System governs everything the client actually sees, and everything that happens after a transaction closes. It exists so that materials make an argument rather than present information, and so that what was promised at signing is measured afterwards.

---

## What it assembles

| Component | Included |
|---|---|
| Workflows | `pitchbook`, `cim-update`, `post-close-transition`, `synergy-realisation`, `portfolio-monitoring`, `capital-allocation-review`, `ipo-readiness`, `activist-defence`, `hostile-defence`, `post-investment-review` |
| Core agents | Pitchbook Drafting family, CIM Drafting family, KPIs & Dashboards family, Committee Materials family |
| Core skills | `pitchbook-construction`, `investment-memo-writing`, `synergy-quantification`, `valuation-techniques`, `risk-assessment` |
| Prompt libraries | `11-investment-memo`, `12-pitchbook`, `08-synergy-analysis` |

## Standing state

1. **The materials register** — every document issued, its version, its date and the figures it contains, so a later document never contradicts an earlier one.
2. **The source log** — shared with the Execution System; every external figure with document, page and retrieval date.
3. **The KPI definitions** — each measure with its numerator, denominator, period, inclusions and exclusions, fixed so that definitions cannot drift between reports.
4. **The synergy tracker** — lines, owners, monthly targets, actuals, validation status and cost to achieve.
5. **The underwriting cases** — the case each asset was bought on, held unchanged as the benchmark for every later review.

## The delivery standard

Every client-facing document meets the same bar, whatever the deadline.

- The argument exists in ten sentences before any page is built.
- Every title is a conclusion under twelve words, and the titles alone make the argument.
- Every exhibit proves the title above it.
- Every page carries a source line; every figure has been verified against its source.
- Every figure appearing more than once, including in appendices, agrees.
- Something in the document could not be produced by a competitor with the same public data.

## Operating cadence

| Cadence | Activity | Agent |
|---|---|---|
| Before every issue | Fact verification and consistency sweep | `deck-quality-control-agent` |
| Before every issue | Reconcile against every document already in the market | `source-verification-agent` |
| Monthly post-close | Synergy tracking with validation rules enforced | `synergy-tracking-agent` |
| Monthly post-close | Business health monitoring: revenue, retention, attrition, service levels | `integration-scorecard-agent` |
| Quarterly | Portfolio review against underwriting cases, not against budgets | `portfolio-monitoring-agent` |
| Quarterly | Valuation refresh with movement attributed to performance, multiple and rates | `valuation-monitoring-agent` |
| At month 12 | Post-investment review with honest variance attribution | `post-investment-review-agent` |

## What makes it compound

- **The materials register prevents contradiction.** The most damaging error in a live process is a figure that contradicts one already given to a bidder. A register makes that checkable rather than remembered.
- **Fixed KPI definitions prevent drift.** A measure whose definition moves between reports is worse than no measure, because it produces confident wrong conclusions.
- **Underwriting cases held unchanged prevent goalpost movement.** Measuring against a revised budget always shows performance in line. Measuring against the case the asset was bought on shows the truth.
- **Validation rules prevent synergy inflation.** A saving is booked when a headcount closes, a contract is signed or a lease is exited — not when a budget line comes in low.

## Measures

| Measure | What it tells you |
|---|---|
| Figures failing verification at final review | Whether the standard is being applied early or late |
| Contradictions found against previously issued materials | Whether the register is working |
| Synergy run-rate realised against announced | Whether the case was honest |
| Business health through integration | Whether integration pace is sustainable |
| Variance attribution at month 12 | Whether the organisation learns from its own deals |

## Setting it up

1. Adopt the delivery standard explicitly, including the rule that it is not waived for deadlines.
2. Stand up the materials register at the start of the first mandate.
3. Fix KPI definitions in writing before the first report, not after the first disagreement.
4. Lock the underwriting case at closing as the permanent benchmark.
5. Stand up the synergy tracker with its validation rules before day one, not after the first quarter.
