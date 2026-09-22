# Post-Close Transition Workflow

**Layer:** Execution  ·  **System:** Client Delivery  ·  **Typical duration:** Day one to month 12

## When to run

A transaction has closed and value now depends entirely on execution.

## Inputs required

- The synergy case with owners and phasing
- The integration plan and target operating model
- Baseline business performance at closing

## Phases

### Phase 1 — Day one  *(1 day)*

| # | Action | Agent |
|---|---|---|
| 1.1 | Execute the day-one checklist across legal, systems, payroll and banking | `integration-planning-agent` |
| 1.2 | Release communications to employees, customers, suppliers and regulators | `post-signing-tracker-agent` |

### Phase 2 — First hundred days  *(100 days)*

| # | Action | Agent |
|---|---|---|
| 2.1 | Run the workstream plan with accountable owners and decision rights | `integration-planning-agent` |
| 2.2 | Stand up the synergy tracker with validation rules before anything is booked | `synergy-tracking-agent` |
| 2.3 | Monitor business health: revenue, retention, attrition and service levels | `integration-scorecard-agent` |
| 2.4 | Execute the retention plan for the people the synergies depend on | `hr-and-culture-diligence-agent` |

### Phase 3 — Deliver  *(Months 4–12)*

| # | Action | Agent |
|---|---|---|
| 3.1 | Track synergy realisation and cost to achieve against plan | `synergy-tracking-agent` |
| 3.2 | Intervene on the workstreams that early indicators flag | `integration-scorecard-agent` |
| 3.3 | Compare against integration curves observed in comparable deals | `integration-scorecard-agent` |

### Phase 4 — Review  *(Month 12)*

| # | Action | Agent |
|---|---|---|
| 4.1 | Compare actual performance to the underwriting case and attribute the variance | `post-investment-review-agent` |
| 4.2 | Extract transferable lessons and recommend changes to the underwriting standard | `post-investment-review-agent` |

## Gates

- **Validation gate** — A synergy is booked only when its validation rule is met — a closed headcount, a signed contract, an exited lease.
- **Business-health gate** — If retention or attrition breaches its threshold, integration pace is reconsidered before the next milestone.
- **Honesty gate** — The month-12 review attributes variance honestly, including to the price paid.

## Definition of done

- [ ] Day-one executed with no service interruption
- [ ] Synergy tracker live with validated bookings only
- [ ] Business health within thresholds through the integration
- [ ] Month-12 review completed with transferable lessons recorded

## Common failure modes

- Counting a favourable variance as a synergy
- Losing the key people whose knowledge the synergies depended on
- Integrating so fast that customers notice
