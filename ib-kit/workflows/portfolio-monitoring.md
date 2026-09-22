# Portfolio Monitoring Workflow

**Layer:** Execution  ·  **System:** Client Delivery  ·  **Typical duration:** Quarterly cycle

## When to run

A portfolio of investments must be monitored against the cases they were bought on.

## Inputs required

- Underwriting cases for each asset including exit assumptions
- Current trading, leverage and covenant positions
- Market conditions and sector trading levels

## Phases

### Phase 1 — Refresh  *(1–2 weeks)*

| # | Action | Agent |
|---|---|---|
| 1.1 | Update performance against the underwriting case for each asset | `portfolio-monitoring-agent` |
| 1.2 | Refresh valuations and attribute movement since entry | `valuation-monitoring-agent` |
| 1.3 | Update covenant headroom forecasts | `covenant-monitoring-agent` |

### Phase 2 — Assess  *(1 week)*

| # | Action | Agent |
|---|---|---|
| 2.1 | Flag assets where the exit assumption is no longer supported | `portfolio-monitoring-agent` |
| 2.2 | Rank by attention required using distance from the case | `portfolio-monitoring-agent` |
| 2.3 | Track synergy or value-creation plan delivery where applicable | `synergy-tracking-agent` |

### Phase 3 — Act  *(1 week)*

| # | Action | Agent |
|---|---|---|
| 3.1 | Define the intervention for each asset needing one | `integration-scorecard-agent` |
| 3.2 | Assess exit readiness and timing for assets approaching their window | `valuation-agent` |

### Phase 4 — Report  *(3–5 days)*

| # | Action | Agent |
|---|---|---|
| 4.1 | Prepare the quarterly review with the value bridge from entry for each asset | `board-materials-agent` |

## Gates

- **Case gate** — Performance is measured against the underwriting case, never against a budget that has been revised.
- **Exit gate** — An exit assumption unsupported by current sector trading is flagged, not carried forward.
- **Attention gate** — Ranking is by distance from the case, not by absolute performance.

## Definition of done

- [ ] Every asset measured against its underwriting case
- [ ] Valuations refreshed with movement attributed
- [ ] Exit assumptions validated or flagged
- [ ] Interventions defined for the assets that need them

## Common failure modes

- Measuring against a budget that has been revised down to meet
- Carrying an exit multiple the sector has not traded at for three years
- Attention going to the loudest asset rather than the one furthest from its case
