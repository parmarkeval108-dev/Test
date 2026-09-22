# Investment Committee Workflow

**Layer:** Execution  ·  **System:** Execution  ·  **Typical duration:** 2–3 weeks

## When to run

A transaction requires committee or board approval to proceed.

## Inputs required

- All completed analysis: valuation, diligence, financing, synergies
- The terms being approved and the authority sought
- The committee's standards and their questions on prior deals

## Phases

### Phase 1 — Assemble  *(3–5 days)*

| # | Action | Agent |
|---|---|---|
| 1.1 | Consolidate diligence findings into price and structure conclusions | `diligence-findings-synthesis-agent` |
| 1.2 | Finalise the valuation and reconcile the methods | `valuation-agent` |
| 1.3 | Finalise the returns or accretion analysis | `lbo-modeling-agent` |

### Phase 2 — Challenge  *(3–5 days)*

| # | Action | Agent |
|---|---|---|
| 2.1 | Run the pre-mortem and feed it into the risk register | `premortem-agent` |
| 2.2 | Build the quantified risk register with owners and a top three | `risk-register-agent` |
| 2.3 | Write the devil's advocate case from the team's own evidence | `devils-advocate-agent` |

### Phase 3 — Draft  *(3–5 days)*

| # | Action | Agent |
|---|---|---|
| 3.1 | Write the memo with the recommendation in the first hundred words | `investment-memo-agent` |
| 3.2 | Table our case against management's with every haircut justified | `investment-memo-agent` |
| 3.3 | Sweep for unsourced figures, unlabelled judgements and contradictions | `source-verification-agent` |

### Phase 4 — Prepare  *(2–3 days)*

| # | Action | Agent |
|---|---|---|
| 4.1 | Build the Q&A pack from the committee's actual prior behaviour | `committee-qa-agent` |
| 4.2 | Fix the memo wherever a question should not have needed asking | `investment-memo-agent` |
| 4.3 | Draft the approval conditions and delegated authority | `approval-conditions-agent` |

## Gates

- **Devil's advocate gate** — If the case against is persuasive on the team's own facts, the memo goes back before it goes to committee.
- **Quantification gate** — Every risk carries a dollar figure, an owner and a leading indicator.
- **Consistency gate** — Every figure appearing more than once, including in appendices, agrees.

## Definition of done

- [ ] Recommendation in the first hundred words
- [ ] Thesis in pillars, each with a disproving fact
- [ ] Risks quantified and reduced to a top three with a walk-away condition
- [ ] Pre-mortem and devil's advocate case included
- [ ] Approval conditions and delegated authority drafted

## Common failure modes

- A memo that builds to a conclusion rather than opening with one
- Thirty generic risks that dilute the three real ones
- Hedged language that avoids taking the position the committee is paying for
