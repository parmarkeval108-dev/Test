# Carve-Out Divestiture Workflow

**Layer:** Execution  ·  **System:** Origination  ·  **Typical duration:** 4–7 months

## When to run

A division is being separated and sold, and its standalone economics are not what the segment accounts show.

## Inputs required

- Segment financials and the allocation methodology behind them
- Shared services, systems, contracts and facilities
- The parent's retained business and its cost base

## Phases

### Phase 1 — Establish standalone  *(4–6 weeks)*

| # | Action | Agent |
|---|---|---|
| 1.1 | Rebuild segment financials into standalone form with real function costs | `carve-out-analysis-agent` |
| 1.2 | Quantify stranded costs left in the parent | `carve-out-analysis-agent` |
| 1.3 | Define the TSA scope, duration and cost | `carve-out-analysis-agent` |
| 1.4 | Estimate one-time separation costs | `carve-out-analysis-agent` |

### Phase 2 — Prepare  *(6–8 weeks)*

| # | Action | Agent |
|---|---|---|
| 2.1 | Build the equity story for the business as a standalone | `equity-story-agent` |
| 2.2 | Draft the CIM on standalone financials, not segment disclosure | `cim-drafting-agent` |
| 2.3 | Map contracts and licences requiring consent to transfer | `contract-review-agent` |

### Phase 3 — Market  *(8–12 weeks)*

| # | Action | Agent |
|---|---|---|
| 3.1 | Build the buyer universe including sponsors who back carve-outs | `buyer-universe-agent` |
| 3.2 | Run the process with separation complexity disclosed early | `process-design-agent` |
| 3.3 | Evaluate bids including each buyer's separation capability | `bid-evaluation-agent` |

### Phase 4 — Separate  *(3–9 months)*

| # | Action | Agent |
|---|---|---|
| 4.1 | Track consents, separation milestones and TSA readiness | `conditions-precedent-agent` |
| 4.2 | Manage stranded cost removal in the parent | `integration-planning-agent` |

## Gates

- **Standalone gate** — No materials go out on segment allocations; standalone financials are built first.
- **Consent gate** — Contracts requiring consent are identified before marketing, not during diligence.
- **Stranded-cost gate** — The parent has a plan for stranded costs before signing, not after.

## Definition of done

- [ ] Standalone financials built and reconciled to segment reporting
- [ ] TSA scope, duration and cost agreed
- [ ] Consents mapped and the critical ones secured
- [ ] Stranded cost removal plan in place

## Common failure modes

- Marketing on segment allocations that understate the true cost of running the business alone
- Discovering during diligence that key contracts cannot be assigned
- A parent left with stranded costs nobody planned to remove
