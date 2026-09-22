# IPO Readiness Workflow

**Layer:** Execution  ·  **System:** Client Delivery  ·  **Typical duration:** 6–18 months

## When to run

A company is preparing to list and must be ready for public market scrutiny.

## Inputs required

- Company financials and the reporting capability behind them
- Governance structure and board composition
- Listed comparable companies and their disclosure practice

## Phases

### Phase 1 — Diagnose  *(4–8 weeks)*

| # | Action | Agent |
|---|---|---|
| 1.1 | Assess reporting capability against public-company timetables | `ipo-materials-agent` |
| 1.2 | Identify the comparable set the market will value the company against | `trading-comps-agent` |
| 1.3 | Assess governance against listing requirements and investor expectations | `ownership-structure-agent` |

### Phase 2 — Build the story  *(8–12 weeks)*

| # | Action | Agent |
|---|---|---|
| 2.1 | Define the equity story and the KPIs the company will commit to | `ipo-materials-agent` |
| 2.2 | Confirm each KPI can be produced reliably every quarter | `kpi-dashboard-agent` |
| 2.3 | Build the financial track record and identify required restatements | `financial-section-agent` |

### Phase 3 — Prepare  *(3–9 months)*

| # | Action | Agent |
|---|---|---|
| 3.1 | Build the analyst presentation with the drivers analysts need | `ipo-materials-agent` |
| 3.2 | Stress-test guidance against a first-quarter miss | `scenario-modeling-agent` |
| 3.3 | Establish the valuation range against the comparable set | `valuation-agent` |

### Phase 4 — Execute  *(8–12 weeks)*

| # | Action | Agent |
|---|---|---|
| 4.1 | Manage the market window assessment | `market-monitoring-agent` |
| 4.2 | Run analyst education and investor engagement | `process-communication-agent` |

## Gates

- **Reliability gate** — No KPI is committed to publicly unless it can be produced accurately every quarter.
- **Guidance gate** — Guidance is stress-tested against a miss before it is given.
- **Readiness gate** — Public-company reporting capability is demonstrated before listing, not promised.

## Definition of done

- [ ] Equity story and comparable set established
- [ ] KPIs committed to and reliably producible
- [ ] Financial track record complete with restatements done
- [ ] Guidance stress-tested

## Common failure modes

- Committing to a KPI the company cannot produce accurately under a reporting deadline
- Guidance set at the plan rather than at a level that can be beaten
- Discovering reporting capability gaps after listing
