# Transaction Closing Workflow

**Layer:** Execution  ·  **System:** Execution  ·  **Typical duration:** 6 weeks–9 months

## When to run

A transaction is signed and must be brought to completion.

## Inputs required

- The signed agreement and its conditions schedule
- Regulatory filing requirements by jurisdiction
- Third-party consent requirements

## Phases

### Phase 1 — Extract  *(1 week)*

| # | Action | Agent |
|---|---|---|
| 1.1 | Extract every condition with its responsible party and evidence requirement | `conditions-precedent-agent` |
| 1.2 | Map approvals required in every jurisdiction | `cross-border-agent` |
| 1.3 | Identify the long-pole condition and what can run in parallel | `timeline-management-agent` |

### Phase 2 — Regulatory  *(4 weeks–9 months)*

| # | Action | Agent |
|---|---|---|
| 2.1 | Manage filings and respond to information requests | `antitrust-screening-agent` |
| 2.2 | Track decision dates and prepare for remedy discussions | `antitrust-screening-agent` |
| 2.3 | Reforecast closing from actual progress, not the original plan | `timeline-management-agent` |

### Phase 3 — Consents and covenants  *(Ongoing)*

| # | Action | Agent |
|---|---|---|
| 3.1 | Track third-party consents with counterparty and response | `conditions-precedent-agent` |
| 3.2 | Monitor interim operating covenant compliance | `post-signing-tracker-agent` |
| 3.3 | Monitor the target's trading against the basis the price was struck on | `post-signing-tracker-agent` |

### Phase 4 — Readiness  *(4–8 weeks before closing)*

| # | Action | Agent |
|---|---|---|
| 4.1 | Build day-one readiness across systems, payroll, banking and communications | `post-signing-tracker-agent` |
| 4.2 | Maintain the clean-team protocol so planning does not breach gun-jumping rules | `post-signing-tracker-agent` |
| 4.3 | Prepare the day-one communications pack | `post-signing-tracker-agent` |

### Phase 5 — Complete  *(1–2 weeks)*

| # | Action | Agent |
|---|---|---|
| 5.1 | Run the closing checklist, signatories and funds flow | `conditions-precedent-agent` |
| 5.2 | Confirm every condition satisfied with its evidence on file | `conditions-precedent-agent` |

## Gates

- **Gun-jumping gate** — No pre-close integration activity proceeds outside the clean-team protocol.
- **MAC gate** — Any deterioration in the target's trading is assessed against the agreement before it becomes a surprise.
- **Evidence gate** — Every condition is satisfied with documented evidence, not with an assurance.

## Definition of done

- [ ] All conditions satisfied with evidence on file
- [ ] All approvals obtained and documented
- [ ] Day-one readiness confirmed across every function
- [ ] Funds flow executed and completion documented

## Common failure modes

- Discovering a required third-party consent weeks before closing
- Pre-close integration planning that breaches gun-jumping rules
- A closing date repeatedly reforecast from optimism rather than observed progress
