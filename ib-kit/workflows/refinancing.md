# Refinancing Workflow

**Layer:** Execution  ·  **System:** Execution  ·  **Typical duration:** 8–16 weeks

## When to run

A maturity is approaching or better terms are available.

## Inputs required

- Existing facilities with terms, maturities and call protection
- Current financials and forecast
- Rating position and market conditions

## Phases

### Phase 1 — Assess  *(2–3 weeks)*

| # | Action | Agent |
|---|---|---|
| 1.1 | Map the maturity wall and identify the refinancing requirement by date | `capital-structure-agent` |
| 1.2 | Compute the economics including call premium and unamortised fee write-off | `debt-schedule-agent` |
| 1.3 | Read the current market for this credit | `financing-markets-agent` |

### Phase 2 — Structure  *(2–3 weeks)*

| # | Action | Agent |
|---|---|---|
| 2.1 | Design the new structure and test it in the downside | `lbo-modeling-agent` |
| 2.2 | Assess rating implications against published methodology | `rating-agency-agent` |
| 2.3 | Compare structures on pricing, terms, flexibility and certainty | `financing-markets-agent` |

### Phase 3 — Market  *(3–6 weeks)*

| # | Action | Agent |
|---|---|---|
| 3.1 | Prepare lender materials and the credit story | `offering-memo-agent` |
| 3.2 | Run the process and benchmark every term received | `bid-evaluation-agent` |

### Phase 4 — Close  *(2–4 weeks)*

| # | Action | Agent |
|---|---|---|
| 4.1 | Negotiate documentation, particularly the EBITDA definition and baskets | `term-sheet-analysis` |
| 4.2 | Track conditions and set up covenant monitoring before the first test | `covenant-monitoring-agent` |

## Gates

- **Window gate** — The execution window is assessed continuously; a closing window overrides an optimal structure.
- **Economics gate** — The refinancing economics include every cost, not just the spread saving.
- **Documentation gate** — Baskets and the EBITDA definition are negotiated, not accepted as drafted.

## Definition of done

- [ ] Refinancing completed ahead of the maturity with margin to spare
- [ ] Full economics documented including premiums and write-offs
- [ ] Covenant monitoring live before the first test date

## Common failure modes

- Leaving a refinancing until the window has closed
- Counting the spread saving while ignoring the call premium
- Accepting tighter baskets in exchange for a headline pricing improvement
