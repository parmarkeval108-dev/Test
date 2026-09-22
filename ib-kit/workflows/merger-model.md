# Merger Model Workflow

**Layer:** Execution  ·  **System:** Execution  ·  **Typical duration:** 2–3 weeks

## When to run

The earnings and value impact of a combination must be established.

## Inputs required

- Standalone forecasts for both companies
- Offer terms and financing assumptions
- Synergy estimates and integration costs

## Phases

### Phase 1 — Standalone  *(3–5 days)*

| # | Action | Agent |
|---|---|---|
| 1.1 | Build both standalone forecasts and note every deviation from consensus | `operating-model-agent` |
| 1.2 | Benchmark each forecast against history and peers | `forecast-benchmarking-agent` |

### Phase 2 — Transaction  *(3–5 days)*

| # | Action | Agent |
|---|---|---|
| 2.1 | Build the purchase price allocation with intangibles by class | `merger-model-agent` |
| 2.2 | Model the financing including refinancing costs and fee treatment | `debt-schedule-agent` |
| 2.3 | Grade and phase the synergy case | `synergy-analysis-agent` |

### Phase 3 — Analyse  *(3–5 days)*

| # | Action | Agent |
|---|---|---|
| 3.1 | Build the EPS bridge with every line on a consistent tax basis | `merger-model-agent` |
| 3.2 | Solve for break-even synergies and the break-even price | `merger-model-agent` |
| 3.3 | Run the contribution analysis and the consideration mix comparison | `merger-model-agent` |
| 3.4 | Test pro forma metrics against rating thresholds | `rating-agency-agent` |

### Phase 4 — Reconcile  *(2–3 days)*

| # | Action | Agent |
|---|---|---|
| 4.1 | Compute deal ROIC against WACC and value created | `merger-model-agent` |
| 4.2 | Reconcile the accretion conclusion to the valuation conclusion | `valuation-agent` |
| 4.3 | Audit the model for the standard merger-model errors | `model-audit-agent` |

### Phase 5 — Deliver  *(2–3 days)*

| # | Action | Agent |
|---|---|---|
| 5.1 | Build the board page and the analyst Q&A | `board-materials-agent` |

## Gates

- **Tax-basis gate** — Synergies, interest and amortisation all on a consistent tax basis, or the bridge is wrong.
- **Share-count gate** — Pro forma shares reconcile from acquirer standalone including converted target awards.
- **Value gate** — The accretion conclusion is presented alongside the value conclusion, never instead of it.

## Definition of done

- [ ] EPS bridge complete in dollars and cents per share
- [ ] Break-even synergies and break-even price solved
- [ ] ROIC-versus-WACC and value created computed
- [ ] Model audited and outputs reconciled to the deck

## Common failure modes

- Adding synergies pre-tax while deducting interest post-tax
- Omitting target equity awards converting into acquirer stock
- Presenting accretion as evidence of value creation
