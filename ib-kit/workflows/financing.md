# Financing Workflow

**Layer:** Execution  ·  **System:** Execution  ·  **Typical duration:** 6–12 weeks

## When to run

An acquisition, recapitalisation or refinancing requires debt to be raised.

## Inputs required

- The transaction and its funding requirement
- Target or company financials and forecast
- Rating objectives and any structural constraints

## Phases

### Phase 1 — Assess capacity  *(1 week)*

| # | Action | Agent |
|---|---|---|
| 1.1 | Size leverage by all three tests and name the binding constraint | `lbo-modeling-agent` |
| 1.2 | Read the current market for this credit profile | `financing-markets-agent` |
| 1.3 | Assess the rating implications against published methodology | `rating-agency-agent` |

### Phase 2 — Design the structure  *(1–2 weeks)*

| # | Action | Agent |
|---|---|---|
| 2.1 | Design the tranche structure with terms and pricing | `lbo-modeling-agent` |
| 2.2 | Build the debt schedule with sweep and covenant mechanics | `debt-schedule-agent` |
| 2.3 | Compare syndicated against private credit on all dimensions | `financing-markets-agent` |
| 2.4 | Model the downside and the first breach period | `scenario-modeling-agent` |

### Phase 3 — Prepare materials  *(2 weeks)*

| # | Action | Agent |
|---|---|---|
| 3.1 | Build the lender presentation and offering materials | `offering-memo-agent` |
| 3.2 | Reconcile credit-agreement EBITDA and disclose the add-back caps | `quality-of-earnings-agent` |
| 3.3 | Prepare the rating agency presentation | `rating-agency-agent` |

### Phase 4 — Execute  *(3–6 weeks)*

| # | Action | Agent |
|---|---|---|
| 4.1 | Run the market process and track indications | `market-monitoring-agent` |
| 4.2 | Analyse term sheets and benchmark every material term | `bid-evaluation-agent` |
| 4.3 | Negotiate documentation with the ask-and-concede map prepared | `negotiation-strategy-agent` |

### Phase 5 — Close  *(1 week)*

| # | Action | Agent |
|---|---|---|
| 5.1 | Track conditions precedent and the funds flow | `conditions-precedent-agent` |
| 5.2 | Set up covenant monitoring before the first test date | `covenant-monitoring-agent` |

## Gates

- **Downside gate** — The structure must survive the downside case without a sponsor cheque, or the leverage is reduced.
- **Documentation gate** — The EBITDA definition and add-back caps are negotiated explicitly, not accepted as drafted.
- **Monitoring gate** — Covenant monitoring is live before the first test date, not after it.

## Definition of done

- [ ] Structure sized by the binding constraint, with that constraint named
- [ ] Downside case run with the first breach period identified
- [ ] Every material term benchmarked against recent comparable issuance
- [ ] Conditions precedent tracked to satisfaction
- [ ] Covenant monitoring operational

## Common failure modes

- Sizing leverage from a market benchmark with no downside test behind it
- Accepting the drafted EBITDA definition without reading the add-back cap
- Modelling interest at a flat rate instead of the forward curve
