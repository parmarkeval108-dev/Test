# Valuation Workflow

**Layer:** Execution  ·  **System:** Execution  ·  **Typical duration:** 2–4 weeks

## When to run

A value range is needed for a bid, a defence, a fairness opinion or a board decision.

## Inputs required

- Company financials and a forecast or the drivers to build one
- A single agreed valuation date
- Peer universe and transaction history

## Phases

### Phase 1 — Set up  *(2–3 days)*

| # | Action | Agent |
|---|---|---|
| 1.1 | Fix the valuation date and pull all market data as at that date | `valuation-agent` |
| 1.2 | Select methods from what the asset is, and record why each excluded method was excluded | `valuation-agent` |

### Phase 2 — Build the model  *(1 week)*

| # | Action | Agent |
|---|---|---|
| 2.1 | Build or validate the operating model from drivers | `operating-model-agent` |
| 2.2 | Benchmark the forecast against history, peers and consensus | `forecast-benchmarking-agent` |
| 2.3 | Audit the model before anything is built on it | `model-audit-agent` |

### Phase 3 — Run the methods  *(1–1.5 weeks)*

| # | Action | Agent |
|---|---|---|
| 3.1 | Build the trading comparables with defended selection | `trading-comps-agent` |
| 3.2 | Build the precedent transactions with rebuilt deal values | `precedent-transactions-agent` |
| 3.3 | Build the DCF with a fully cited discount rate | `dcf-modeling-agent` |
| 3.4 | Build the LBO ability-to-pay where a sponsor bid is credible | `lbo-modeling-agent` |

### Phase 4 — Reconcile  *(3–5 days)*

| # | Action | Agent |
|---|---|---|
| 4.1 | Cross-check every output as an implied multiple and reconcile disagreements above 15% | `valuation-agent` |
| 4.2 | Build the football field with labelled endpoint drivers | `football-field-agent` |
| 4.3 | Run the reverse DCF against the current market price | `dcf-modeling-agent` |

### Phase 5 — Deliver  *(2–3 days)*

| # | Action | Agent |
|---|---|---|
| 5.1 | Verify every figure against its source | `source-verification-agent` |
| 5.2 | Build the valuation section for the board or committee | `board-materials-agent` |

## Gates

- **Single-date gate** — Every market input comes from one valuation date. Mixed dates fail the review.
- **Reconciliation gate** — Methods reconciled by finding the responsible assumption, never by averaging.
- **Terminal value gate** — Terminal value below 75% of enterprise value, or the explicit forecast is extended.

## Definition of done

- [ ] Football field with each endpoint traceable to a specific assumption
- [ ] Methodology reconciliation completed
- [ ] Every input sourced and dated
- [ ] The three assumptions that decide the valuation identified
- [ ] What would make this valuation wrong stated explicitly

## Common failure modes

- Averaging methods that disagree instead of diagnosing why
- A DCF whose implied exit multiple nobody checked against the comps
- Control premium stacked on precedent transactions that already reflect control
