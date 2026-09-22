# Post-Investment Review Workflow

**Layer:** Execution  ·  **System:** Client Delivery  ·  **Typical duration:** 3–4 weeks

## When to run

An investment has run long enough to judge and the lessons would otherwise be lost.

## Inputs required

- The original investment case and committee memo
- Actual performance since closing
- The diligence file including findings that were set aside

## Phases

### Phase 1 — Compare  *(1 week)*

| # | Action | Agent |
|---|---|---|
| 1.1 | Compare actual performance against the underwriting case line by line | `post-investment-review-agent` |
| 1.2 | Attribute the variance to market, execution, price, synergies or a wrong assumption | `post-investment-review-agent` |

### Phase 2 — Interrogate  *(1 week)*

| # | Action | Agent |
|---|---|---|
| 2.1 | Identify what diligence found and the team discounted, and whether it mattered | `post-investment-review-agent` |
| 2.2 | Assess whether the process was sound independently of the outcome | `post-investment-review-agent` |
| 2.3 | Re-read the pre-mortem against what actually happened | `premortem-agent` |

### Phase 3 — Extract  *(3–5 days)*

| # | Action | Agent |
|---|---|---|
| 3.1 | Extract specific transferable lessons rather than general observations | `post-investment-review-agent` |
| 3.2 | Recommend changes to the underwriting standard | `post-investment-review-agent` |

### Phase 4 — Embed  *(3–5 days)*

| # | Action | Agent |
|---|---|---|
| 4.1 | Update the screening criteria, diligence checklists and memo standards | `screening-and-targeting` |

## Gates

- **Process gate** — A good outcome from a poor process is recorded as a poor process.
- **Honesty gate** — Variance attributable to the price paid is stated, not attributed to the market.
- **Embedding gate** — Lessons change a standard, a checklist or a template, or they are not lessons.

## Definition of done

- [ ] Case-versus-actual comparison complete with attribution
- [ ] Diligence retrospective completed including what was discounted
- [ ] Process assessed independently of outcome
- [ ] Lessons embedded in standards, not just circulated

## Common failure modes

- Reviewing only the deals that went badly
- Attributing to the market what was a price decision
- Lessons that are circulated and never change a template
