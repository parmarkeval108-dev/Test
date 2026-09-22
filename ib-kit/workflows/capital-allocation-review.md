# Capital Allocation Review Workflow

**Layer:** Execution  ·  **System:** Client Delivery  ·  **Typical duration:** 6–10 weeks

## When to run

A board needs to decide between reinvestment, acquisition, distribution and debt reduction.

## Inputs required

- Current capital structure and cash generation forecast
- The investment opportunity set with returns
- Peer capital structures and shareholder expectations

## Phases

### Phase 1 — Establish capacity  *(2 weeks)*

| # | Action | Agent |
|---|---|---|
| 1.1 | Assess the current structure against cash flow volatility and plan requirements | `capital-structure-agent` |
| 1.2 | Model WACC across leverage levels and identify where distress cost dominates | `capital-structure-agent` |
| 1.3 | Map the maturity profile and refinancing risk | `capital-structure-agent` |

### Phase 2 — Compare uses  *(2–3 weeks)*

| # | Action | Agent |
|---|---|---|
| 2.1 | Compare reinvestment, acquisition, dividend, buyback and debt reduction on returns | `capital-structure-agent` |
| 2.2 | Value the acquisition pipeline's contribution | `ability-to-pay-agent` |
| 2.3 | Assess what the market currently rewards in this sector | `market-intelligence-agent` |

### Phase 3 — Test  *(1–2 weeks)*

| # | Action | Agent |
|---|---|---|
| 3.1 | Stress the plan against a downturn and a closed financing market | `scenario-modeling-agent` |
| 3.2 | Assess rating implications of each path | `rating-agency-agent` |

### Phase 4 — Recommend  *(1–2 weeks)*

| # | Action | Agent |
|---|---|---|
| 4.1 | Recommend the target structure and the path with triggers for each step | `board-materials-agent` |

## Gates

- **Returns gate** — Every use of capital is compared on the same returns basis, including buybacks.
- **Downside gate** — The allocation plan survives a downturn with the financing market closed.
- **Policy gate** — The recommendation includes the financial policy the board commits to, not just the next action.

## Definition of done

- [ ] Capacity established with the WACC-by-leverage analysis
- [ ] All uses compared on a consistent returns basis
- [ ] Downside and rating implications tested
- [ ] Target structure and path recommended with triggers

## Common failure modes

- Comparing acquisitions on IRR and buybacks on sentiment
- A plan that assumes financing will be available when it is most needed
- Announcing a policy the balance sheet cannot sustain through a cycle
