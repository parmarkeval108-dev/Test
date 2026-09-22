# The Claude Origination System

**Layer:** Impact Engine  ·  **Purpose:** source, prioritise and qualify opportunities

A system is the layer above a workflow. A workflow runs once and finishes. A system runs continuously, keeps state between runs, and gets better because it remembers what happened last time.

The Origination System answers one question on a standing basis: *what should we be working on, and who do we call first?*

---

## What it assembles

| Component | Included |
|---|---|
| Workflows | `deal-screening`, `buyer-list`, `target-approach`, `carve-out-divestiture` |
| Core agents | `screening-and-targeting` family, `company-research-agent`, `market-intelligence-agent`, `buyer-universe-agent`, `ability-to-pay-agent`, `pipeline-management-agent` |
| Core skills | `screening-and-targeting`, `industry-analysis`, `buyer-universe-mapping`, `valuation-techniques` |
| Prompt libraries | `01-ma-screening`, `04-industry-market-analysis`, `09-buyer-list-generation` |

## Standing state

The system maintains four datasets between runs. Without persistent state it is a workflow, not a system.

1. **The universe** — every company in the covered sectors with its profile, last refresh date and tier.
2. **The pipeline** — live opportunities with stage, owner, next action, next action date and last contact.
3. **The trigger monitor** — observable signals per target: leadership changes, auditor changes, adviser hires, sponsor fund life, segment reporting changes, capex pauses, prior failed processes.
4. **The anti-target log** — names deliberately excluded, with the disqualifying fact, so the same rejected ideas stop recirculating each quarter.

## Operating cadence

| Cadence | Activity | Agent |
|---|---|---|
| Weekly | Refresh the trigger monitor; flag any signal that changes a target's priority | `pipeline-management-agent` |
| Weekly | Update pipeline stage and next actions; flag anything unmoved for 60 days | `pipeline-management-agent` |
| Monthly | Pipeline review pack: decisions required, not status narrative | `pipeline-management-agent` |
| Quarterly | Re-score the universe; test whether the criteria still match the client's strategy | `screening-and-targeting` |
| Quarterly | Refresh willingness-to-pay estimates against current sector trading | `ability-to-pay-agent` |
| On trigger | Run the approach workflow for any target whose trigger fires | `target-approach` workflow |
| Annually | Review conversion rates by stage and recalibrate what "qualified" means | `post-investment-review-agent` |

## What makes it compound

- **Trigger monitoring beats periodic screening.** A quarterly screen finds a target after it has come to market. A trigger monitor finds it before.
- **The anti-target log saves more time than the target list.** Most origination waste is re-analysing names that were already rejected for a reason nobody recorded.
- **Conversion tracking recalibrates the criteria.** If Tier 1 targets convert at the same rate as Tier 2, the scorecard is not working and should be rebuilt.
- **Willingness-to-pay estimates age.** Refreshed quarterly against sector trading, they tell you when a target has become affordable or a competitor has become able to outbid.

## Measures

| Measure | What it tells you |
|---|---|
| Trigger-to-contact time | Whether monitoring converts into action |
| Tier 1 conversion to conversation | Whether the scorecard predicts anything |
| Proportion of conversations sourced proactively | Whether origination is working or inbound is |
| Pipeline items unmoved over 60 days | Whether the pipeline is honest |
| Deals lost to a competitor who moved first | The cost of the monitoring gap |

## Setting it up

1. Agree criteria and weights with the client in writing, before any screening.
2. Run `deal-screening` once to build the initial universe and tier it.
3. Stand up the four datasets and assign an owner to each.
4. Define the trigger set per target and the monitoring source for each.
5. Set the weekly and monthly cadence with a named owner for each cycle.
6. After two quarters, review conversion by tier and recalibrate the scorecard.
