# The Claude Execution System

**Layer:** Impact Engine  ·  **Purpose:** run deals, manage diligence, deliver materials

The Execution System is what runs between a mandate being won and a transaction closing. It exists to make sure nothing is discovered late, every finding reaches the people it affects, and every number that leaves the building can be defended.

---

## What it assembles

| Component | Included |
|---|---|
| Workflows | `valuation`, `diligence`, `due-diligence-tracking`, `process-management`, `merger-model`, `financing`, `investment-committee`, `transaction-closing`, `fairness-opinion`, `restructuring`, `refinancing`, `joint-venture` |
| Core agents | Financial Modeling family, Valuation family, Diligence Analysis family, Deal Tracking family, Committee Materials family |
| Core skills | `financial-statement-modeling`, `dcf-and-sensitivity`, `lbo-modeling`, `accretion-dilution-modeling`, `diligence-questioning`, `risk-assessment`, `deal-structuring`, `term-sheet-analysis` |
| Prompt libraries | `02`, `03`, `05`, `06`, `07`, `08`, `10`, `11` |

## Standing state

1. **The model register** — every model with its version, owner, last audit date and what depends on it.
2. **The findings register** — every diligence finding with value impact, owner, required decision and status, shared across all workstreams.
3. **The issues log** — open items with value impact, blocking status and resolution date.
4. **The conditions register** — every condition precedent with its responsible party, evidence requirement and status.
5. **The source log** — every external figure used in any deliverable, with document, page and retrieval date.

## Operating cadence

| Cadence | Activity | Agent |
|---|---|---|
| Daily during diligence | Route new findings to every workstream they affect | `workstream-coordination-agent` |
| Twice weekly | Update the issues log and flag items without an owner or a path | `issues-log-agent` |
| Weekly | Critical path review and closing-date reforecast from actual progress | `timeline-management-agent` |
| Weekly | Client update: stage, issues, decisions required this week | `process-communication-agent` |
| Before every deliverable | Source verification and consistency sweep | `source-verification-agent` |
| Before every model is relied on | Model audit including the balance check in every scenario | `model-audit-agent` |
| At each decision point | Findings synthesis into price and structure conclusions | `diligence-findings-synthesis-agent` |

## The three controls that prevent most failures

**The routing control.** A finding in one workstream reaches every workstream it affects within the same week. Most diligence failures are not failures to find something — they are failures to tell the right person.

**The verification control.** No figure leaves the building without a source, a page and a date. This is the cheapest control in the system and the one most often skipped under time pressure.

**The reforecast control.** The closing date is reforecast from observed progress, never from the original plan. A timetable that has slipped three times will slip a fourth, and the client would rather be told now.

## Quality gates

These apply across every workflow in the system and are not waived for time.

- Balance check green in every scenario, including the downside, before a model is used.
- Every diligence finding quantified in dollars before it reaches the synthesis.
- Every risk in a committee paper carries a dollar figure, an owner and a leading indicator.
- Valuation methods reconciled by finding the responsible assumption, never by averaging.
- Anything unverified is listed as unverified, never assumed resolved.

## Measures

| Measure | What it tells you |
|---|---|
| Findings routed within one week | Whether the coordination control is working |
| Figures failing verification at final review | Whether the verification control is working early enough |
| Closing-date slippage per reforecast | Whether timelines are built on dependencies or on optimism |
| Issues open past their resolution date | Whether escalation is functioning |
| Model audit findings after a model has been used | Where the process let an error through |

## Setting it up

1. Stand up the five registers on day one of the mandate, with an owner for each.
2. Map workstream scopes and identify the gaps between them before diligence starts.
3. Set the verification gate: nothing leaves without a source log entry.
4. Run the weekly reforecast from the first week, not from the first slip.
5. At close, run the post-process review while it is still fresh.
