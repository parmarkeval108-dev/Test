# Due Diligence Workflow

**Layer:** Execution  ·  **System:** Execution  ·  **Typical duration:** 4–8 weeks

## When to run

A transaction has moved past indicative terms and the thesis must now be verified.

## Inputs required

- The investment thesis with its underlying assumptions
- Data room access and adviser scopes
- The price and structure currently on the table

## Phases

### Phase 1 — Plan  *(3–5 days)*

| # | Action | Agent |
|---|---|---|
| 1.1 | Map each thesis assumption to the evidence that would confirm or disprove it | `diligence-analysis-agent` |
| 1.2 | Build the prioritised question list and delete anything answerable from documents | `diligence-analysis-agent` |
| 1.3 | Define workstream scopes and identify the gaps between them | `workstream-coordination-agent` |

### Phase 2 — Financial  *(2–3 weeks)*

| # | Action | Agent |
|---|---|---|
| 2.1 | Run the quality of earnings and build the underwritable EBITDA | `quality-of-earnings-agent` |
| 2.2 | Analyse working capital, seasonality and the normalised level | `working-capital-modeling-agent` |
| 2.3 | Test revenue quality, concentration and retention | `revenue-quality-agent` |
| 2.4 | Assess tax exposures and the structure | `tax-diligence-agent` |

### Phase 3 — Commercial and operational  *(2–3 weeks)*

| # | Action | Agent |
|---|---|---|
| 3.1 | Test the competitive position and the claimed advantage | `competitive-position-agent` |
| 3.2 | Review material contracts for change-of-control and value terms | `contract-review-agent` |
| 3.3 | Assess technology, technical debt and the investment gap | `technology-diligence-agent` |
| 3.4 | Assess organisation, key people and retention risk | `hr-and-culture-diligence-agent` |

### Phase 4 — Management sessions  *(1 week)*

| # | Action | Agent |
|---|---|---|
| 4.1 | Design the session and pre-write the follow-up trees | `management-presentation-agent` |
| 4.2 | Evaluate answers and run the cross-source consistency check | `diligence-analysis-agent` |
| 4.3 | Build the second-session list ordered by value impact | `diligence-analysis-agent` |

### Phase 5 — Synthesise  *(3–5 days)*

| # | Action | Agent |
|---|---|---|
| 5.1 | Consolidate all workstream findings and eliminate duplication | `diligence-findings-synthesis-agent` |
| 5.2 | Restate the synergy case against what diligence found | `synergy-analysis-agent` |
| 5.3 | Restate the thesis and produce the price and structure recommendation | `diligence-findings-synthesis-agent` |

## Gates

- **Thesis-mapping gate** — Diligence starts from the thesis assumptions, not from a standard checklist.
- **Quantification gate** — Every finding carries a dollar value impact before it reaches the synthesis.
- **Unverified gate** — Anything unverified is listed as unverified, never assumed resolved.

## Definition of done

- [ ] Every thesis assumption marked confirmed, disproved or unresolved
- [ ] Underwritable EBITDA established with the gap to the seller's figure
- [ ] Findings register with aggregate value impact against the price
- [ ] Price, structure, post-close and accepted-risk categories populated
- [ ] The three findings that change the deal stated plainly

## Common failure modes

- Working the data room in index order rather than in value order
- Accepting management's EBITDA adjustments without testing whether the activity continues
- A findings list ordered by workstream, burying the three that matter
