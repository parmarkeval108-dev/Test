# Fairness Opinion Workflow

**Layer:** Execution  ·  **System:** Execution  ·  **Typical duration:** 3–5 weeks

## When to run

A board requires an opinion on the fairness of consideration in a transaction.

## Inputs required

- The transaction terms and the consideration being assessed
- The board's mandate and the opinion's scope
- All company and market data required

## Phases

### Phase 1 — Scope  *(3–5 days)*

| # | Action | Agent |
|---|---|---|
| 1.1 | Define precisely what is opined on, as at what date, to whom, and what is excluded | `fairness-opinion-agent` |
| 1.2 | Confirm independence and document any relationship requiring disclosure | `fairness-opinion-agent` |

### Phase 2 — Analyse  *(2 weeks)*

| # | Action | Agent |
|---|---|---|
| 2.1 | Build the trading comparables to documentation standard | `trading-comps-agent` |
| 2.2 | Build the precedent transactions with documented selection criteria | `precedent-transactions-agent` |
| 2.3 | Build the DCF with every input cited and dated | `dcf-modeling-agent` |
| 2.4 | Run the premium analysis against unaffected prices | `precedent-transactions-agent` |

### Phase 3 — Test  *(3–5 days)*

| # | Action | Agent |
|---|---|---|
| 3.1 | Re-run the analyses under alternative defensible assumptions | `fairness-opinion-agent` |
| 3.2 | Record where the conclusion holds and where it does not | `fairness-opinion-agent` |

### Phase 4 — Document  *(3–5 days)*

| # | Action | Agent |
|---|---|---|
| 4.1 | Assemble the source log with document, page and retrieval date for every input | `source-verification-agent` |
| 4.2 | Record every judgement call with its reason, including each exclusion | `fairness-opinion-agent` |

### Phase 5 — Deliver  *(2–3 days)*

| # | Action | Agent |
|---|---|---|
| 5.1 | Present to the board with limitations stated as prominently as the conclusion | `board-materials-agent` |

## Gates

- **Scope gate** — The opinion's scope is fixed in writing before analysis begins.
- **Documentation gate** — Every judgement call is recorded with its reason, because the file may be read years later.
- **Robustness gate** — The conclusion is tested under alternative defensible assumptions before it is given.

## Definition of done

- [ ] Scope, date and addressee documented
- [ ] Every analysis documented to a standard that stands without its author
- [ ] Source log complete
- [ ] Alternative-assumption testing recorded
- [ ] Board presentation delivered with limitations stated

## Common failure modes

- A selection criterion applied to peers but not to the subject company
- An opinion whose supporting file cannot be reconstructed a year later
- Limitations buried in a footnote rather than stated to the board
