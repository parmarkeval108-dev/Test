# Synergy Realisation Workflow

**Layer:** Execution  ·  **System:** Client Delivery  ·  **Typical duration:** Months 1–36 post-close

## When to run

Announced synergies must be delivered and evidenced.

## Inputs required

- The synergy case with lines, owners, phasing and evidence grades
- Actual financial performance
- The integration workstream plan

## Phases

### Phase 1 — Establish  *(2–4 weeks)*

| # | Action | Agent |
|---|---|---|
| 1.1 | Load the case line by line with owner, monthly target and evidence requirement | `synergy-tracking-agent` |
| 1.2 | Define the validation rule that permits a saving to be booked | `synergy-tracking-agent` |
| 1.3 | Reconcile every synergy to an integration workstream and close any gap | `integration-planning-agent` |

### Phase 2 — Track  *(Monthly)*

| # | Action | Agent |
|---|---|---|
| 2.1 | Track actual against target and compute run-rate achieved | `synergy-tracking-agent` |
| 2.2 | Separate genuine synergies from favourable variances | `synergy-tracking-agent` |
| 2.3 | Track cost to achieve alongside the benefit | `synergy-tracking-agent` |

### Phase 3 — Intervene  *(As required)*

| # | Action | Agent |
|---|---|---|
| 3.1 | Escalate every line behind plan with a recovery action and a revised date | `issues-log-agent` |
| 3.2 | Re-phase where a dependency has slipped and state the value effect | `synergy-analysis-agent` |

### Phase 4 — Report  *(Quarterly)*

| # | Action | Agent |
|---|---|---|
| 4.1 | Report realised run-rate against the announced figure with the gap explained | `board-materials-agent` |

## Gates

- **Validation gate** — No saving is booked without meeting its validation rule.
- **Attribution gate** — Favourable variances that would have happened anyway are not counted.
- **Honesty gate** — A gap to the announced figure is reported, not absorbed into other variances.

## Definition of done

- [ ] Every line tracked with validated bookings only
- [ ] Cost to achieve tracked against budget
- [ ] Behind-plan lines escalated with recovery actions
- [ ] Realised run-rate reported against the announced figure

## Common failure modes

- Booking a saving because a budget line came in low
- Tracking benefits without tracking the cost of achieving them
- Quietly absorbing a synergy shortfall into general variance
