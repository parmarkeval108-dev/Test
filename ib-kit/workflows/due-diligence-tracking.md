# Diligence Tracking Workflow

**Layer:** Execution  ·  **System:** Execution  ·  **Typical duration:** Continuous through diligence

## When to run

Multiple diligence workstreams are running and their findings must be coordinated.

## Inputs required

- Workstream scopes and adviser contacts
- The diligence request list
- Decision points that depend on diligence deliverables

## Phases

### Phase 1 — Set up  *(2–3 days)*

| # | Action | Agent |
|---|---|---|
| 1.1 | Map workstream scopes and identify gaps and overlaps | `workstream-coordination-agent` |
| 1.2 | Build the coverage map of the data room against the request list | `data-room-navigation-agent` |
| 1.3 | Establish the shared findings register | `issues-log-agent` |

### Phase 2 — Run  *(Ongoing)*

| # | Action | Agent |
|---|---|---|
| 2.1 | Consolidate information requests to avoid duplicate approaches | `workstream-coordination-agent` |
| 2.2 | Log every finding with value impact, owner and required decision | `issues-log-agent` |
| 2.3 | Route findings to the other workstreams that need them | `workstream-coordination-agent` |
| 2.4 | Track deliverables against the decision points that depend on them | `timeline-management-agent` |

### Phase 3 — Escalate  *(Weekly)*

| # | Action | Agent |
|---|---|---|
| 3.1 | Rank open issues by value impact and by whether they block a decision | `issues-log-agent` |
| 3.2 | Identify issues with no owner or no resolution path | `issues-log-agent` |
| 3.3 | Report aggregate unresolved value impact against the price | `issues-log-agent` |

### Phase 4 — Close out  *(3–5 days)*

| # | Action | Agent |
|---|---|---|
| 4.1 | Confirm every request is answered or explicitly recorded as unanswered | `data-room-navigation-agent` |
| 4.2 | Synthesise findings into price and structure conclusions | `diligence-findings-synthesis-agent` |

## Gates

- **Ownership gate** — No issue stays on the log without an owner and a resolution path.
- **Routing gate** — A finding in one workstream reaches every workstream it affects, in the same week.
- **Unanswered gate** — An unanswered request is recorded as unanswered, never quietly dropped.

## Definition of done

- [ ] Coverage map complete with every gap listed
- [ ] Findings register consolidated with value impacts
- [ ] All blocking issues resolved or escalated with consequences stated
- [ ] Aggregate unresolved impact reported against the price

## Common failure modes

- Two advisers approaching the target with the same question, wasting credibility
- A commercial finding that never reaches the modelling team
- Requests quietly dropped because chasing them was awkward
