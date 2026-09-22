# Agents — The Intelligence Layer

Every agent below is a working Claude Code subagent defined in `.claude/agents/`. Invoke one with the Agent tool (`subagent_type: "<name>"`) or by name in conversation.

Each definition carries a mission, the inputs it requires, a method, the output it produces, and a fixed set of non-negotiables: every figure sourced and dated, nothing unverified presented as verified, and the finding that weakens the case reported as prominently as the one that supports it.

**107 agents across 12 families.** 18 carry a jurisdiction pointer to `india-transaction-regime` — see [CONTEXTS.md](../CONTEXTS.md#jurisdictions).


## Company Research  *(10)*

| Agent | Purpose | Skills loaded |
|---|---|---|
| `business-model-analysis-agent` | Decomposes how a company actually makes money, unit by unit. | `financial-statement-modeling`, `industry-analysis` |
| `company-research-agent` | Builds a complete, sourced company profile from public and provided materials. | `screening-and-targeting`, `industry-analysis` |
| `competitive-position-agent` | Establishes where a company actually stands against its competitors. | `industry-analysis`, `risk-assessment` |
| `corporate-history-agent` | Reconstructs a company's corporate and transaction history and what it reveals. | `precedent-transaction-analysis`, `buyer-universe-mapping` |
| `customer-analysis-agent` | Analyses the customer base: concentration, economics, retention and risk. | `diligence-questioning`, `risk-assessment` |
| `management-assessment-agent` | Assesses a management team against the plan they are asking to be funded. | `risk-assessment`, `diligence-questioning` |
| `ownership-structure-agent` | Maps ownership, control and who can actually approve a transaction. | `buyer-universe-mapping`, `deal-structuring`  ·  **India-sensitive** |
| `public-filings-extraction-agent` | Extracts and reconciles structured financial data from filings with full traceability. | `financial-statement-modeling`  ·  **India-sensitive** |
| `revenue-quality-agent` | Tests the durability and composition of reported revenue. | `diligence-questioning`, `financial-statement-modeling` |
| `target-screening-agent` | Screens a sector for acquisition targets and tiers them by desirability and deliverability. | `screening-and-targeting`, `industry-analysis` |

## Financial Modeling  *(10)*

| Agent | Purpose | Skills loaded |
|---|---|---|
| `cash-flow-forecasting-agent` | Builds short-term and medium-term cash flow forecasts including a 13-week model. | `financial-statement-modeling`, `scenario-and-stress-testing` |
| `dcf-modeling-agent` | Builds a discounted cash flow valuation with a fully sourced discount rate. | `dcf-and-sensitivity`, `valuation-techniques`  ·  **India-sensitive** |
| `debt-schedule-agent` | Builds and audits multi-tranche debt schedules and cash sweep mechanics. | `lbo-modeling`, `financial-statement-modeling` |
| `forecast-benchmarking-agent` | Tests a forecast against history, peers and consensus to find where it is not credible. | `financial-statement-modeling`, `industry-analysis` |
| `lbo-modeling-agent` | Builds a leveraged buyout model with full debt mechanics and downside testing. | `lbo-modeling`, `scenario-and-stress-testing` |
| `merger-model-agent` | Builds a merger model and accretion/dilution analysis with full purchase accounting. | `accretion-dilution-modeling`, `synergy-quantification`  ·  **India-sensitive** |
| `model-audit-agent` | Audits a financial model for structural and logical errors before it is relied on. | `financial-statement-modeling`, `dcf-and-sensitivity` |
| `operating-model-agent` | Builds an integrated three-statement operating model from drivers. | `financial-statement-modeling`, `scenario-and-stress-testing` |
| `scenario-modeling-agent` | Designs and runs internally consistent scenarios and stress tests. | `scenario-and-stress-testing`, `financial-statement-modeling` |
| `working-capital-modeling-agent` | Models working capital from days assumptions, including seasonality and normalisation. | `financial-statement-modeling`, `deal-structuring` |

## Market Intelligence  *(9)*

| Agent | Purpose | Skills loaded |
|---|---|---|
| `competitive-landscape-agent` | Maps the competitive structure of an industry and how it is changing. | `industry-analysis`, `risk-assessment` |
| `esg-assessment-agent` | Assesses financially material ESG factors and quantifies what is at stake. | `industry-analysis`, `risk-assessment` |
| `macro-scenario-agent` | Translates macroeconomic scenarios into company-level forecast effects. | `scenario-and-stress-testing`, `industry-analysis` |
| `market-intelligence-agent` | Builds a sourced industry and market view with implications for the forecast. | `industry-analysis` |
| `market-sizing-agent` | Sizes a market two ways and reconciles the difference. | `industry-analysis` |
| `regulatory-landscape-agent` | Maps the regulatory regime governing a business and what changes are coming. | `industry-analysis`, `risk-assessment` |
| `sector-cycle-agent` | Places a sector on its cycle and states what the forecast assumes about it. | `industry-analysis`, `valuation-techniques` |
| `supply-chain-analysis-agent` | Maps supply chain structure, concentration and disruption exposure. | `industry-analysis`, `risk-assessment` |
| `technology-disruption-agent` | Assesses technology and business-model disruption with an evidence threshold. | `industry-analysis`, `scenario-and-stress-testing` |

## Valuation  *(9)*

| Agent | Purpose | Skills loaded |
|---|---|---|
| `ability-to-pay-agent` | Determines what each buyer type can actually pay for an asset. | `lbo-modeling`, `accretion-dilution-modeling`, `buyer-universe-mapping`  ·  **India-sensitive** |
| `fairness-opinion-agent` | Assembles the analytical support for a fairness opinion to documentation standard. | `valuation-techniques`, `comparable-company-analysis`, `precedent-transaction-analysis` |
| `football-field-agent` | Builds and quality-controls the valuation summary exhibit. | `valuation-techniques`, `pitchbook-construction` |
| `precedent-transactions-agent` | Builds a precedent transaction analysis with rebuilt deal values and premia. | `precedent-transaction-analysis` |
| `sum-of-parts-agent` | Values a multi-segment business by parts with segment-specific methods. | `valuation-techniques`, `comparable-company-analysis` |
| `trading-comps-agent` | Builds and defends a trading comparable company analysis. | `comparable-company-analysis`  ·  **India-sensitive** |
| `valuation-agent` | Runs a complete multi-method valuation and reconciles the methods. | `valuation-techniques`, `dcf-and-sensitivity`, `comparable-company-analysis`, `precedent-transaction-analysis` |
| `valuation-gap-agent` | Bridges traded value to intrinsic value and identifies what closes the gap. | `valuation-techniques`, `risk-assessment` |
| `wacc-agent` | Builds a defensible discount rate with every input cited. | `dcf-and-sensitivity`  ·  **India-sensitive** |

## Diligence Analysis  *(11)*

| Agent | Purpose | Skills loaded |
|---|---|---|
| `antitrust-screening-agent` | Assesses competition clearance risk, remedies and timeline for a combination. | `risk-assessment`, `deal-structuring`  ·  **India-sensitive** |
| `contract-review-agent` | Reviews material contracts for the terms that affect value and deal execution. | `diligence-questioning`, `deal-structuring` |
| `data-room-navigation-agent` | Indexes a data room and extracts what matters against a defined request list. | `diligence-questioning` |
| `diligence-analysis-agent` | Runs and synthesises due diligence findings across workstreams. | `diligence-questioning`, `risk-assessment` |
| `diligence-findings-synthesis-agent` | Consolidates findings from all workstreams into price and structure conclusions. | `diligence-questioning`, `risk-assessment`, `investment-memo-writing` |
| `hr-and-culture-diligence-agent` | Assesses organisation, talent, compensation and integration culture risk. | `risk-assessment`, `diligence-questioning` |
| `litigation-and-claims-agent` | Assesses litigation, claims and contingent liabilities and quantifies exposure. | `risk-assessment`, `deal-structuring` |
| `quality-of-earnings-agent` | Tests reported EBITDA and builds the earnings figure you would underwrite. | `diligence-questioning`, `financial-statement-modeling`  ·  **India-sensitive** |
| `synergy-analysis-agent` | Builds, grades and phases a synergy case including dis-synergies and costs to achieve. | `synergy-quantification`, `risk-assessment` |
| `tax-diligence-agent` | Identifies historic tax exposures and assesses the transaction's tax structure. | `deal-structuring`, `risk-assessment`  ·  **India-sensitive** |
| `technology-diligence-agent` | Assesses the technology estate, technical debt and the investment it requires. | `diligence-questioning`, `risk-assessment` |

## Buyer Outreach  *(8)*

| Agent | Purpose | Skills loaded |
|---|---|---|
| `bid-evaluation-agent` | Evaluates and ranks bids on certainty-adjusted value rather than headline price. | `term-sheet-analysis`, `buyer-universe-mapping` |
| `buyer-outreach-agent` | Drafts buyer-specific outreach materials and approach strategy. | `buyer-universe-mapping`, `pitchbook-construction` |
| `buyer-universe-agent` | Builds and tiers the complete universe of potential acquirers. | `buyer-universe-mapping`  ·  **India-sensitive** |
| `management-presentation-agent` | Designs and rehearses the management presentation for a sale process. | `pitchbook-construction`, `diligence-questioning` |
| `negotiation-strategy-agent` | Builds the negotiation strategy for each counterparty. | `term-sheet-analysis`, `deal-structuring` |
| `process-communication-agent` | Manages process communications with bidders, the seller and internal stakeholders. | `buyer-universe-mapping`, `investment-memo-writing` |
| `process-design-agent` | Designs the sale process: type, waves, timetable and tension mechanics. | `buyer-universe-mapping`, `deal-structuring`  ·  **India-sensitive** |
| `teaser-drafting-agent` | Drafts the anonymous one-page teaser for a sale process. | `pitchbook-construction`, `buyer-universe-mapping` |

## Pitchbook Drafting  *(8)*

| Agent | Purpose | Skills loaded |
|---|---|---|
| `action-title-agent` | Rewrites page titles as conclusions and tests deck flow. | `pitchbook-construction` |
| `benchmarking-page-agent` | Builds company and peer benchmarking exhibits. | `pitchbook-construction`, `comparable-company-analysis` |
| `board-materials-agent` | Builds board presentations for transaction decisions. | `pitchbook-construction`, `investment-memo-writing`, `valuation-techniques` |
| `credentials-agent` | Assembles relevant transaction credentials and team pages. | `pitchbook-construction` |
| `deck-quality-control-agent` | Runs the fact-verification and consistency review before a deck goes out. | `pitchbook-construction` |
| `exhibit-design-agent` | Designs exhibits that prove their page's message. | `pitchbook-construction` |
| `pitchbook-drafting-agent` | Builds a complete client pitchbook from storyline through to delivery brief. | `pitchbook-construction` |
| `storyline-agent` | Develops the argument structure before any page is built. | `pitchbook-construction`, `investment-memo-writing` |

## CIM Drafting  *(7)*

| Agent | Purpose | Skills loaded |
|---|---|---|
| `cim-drafting-agent` | Drafts the confidential information memorandum for a sale process. | `pitchbook-construction`, `investment-memo-writing` |
| `disclosure-review-agent` | Reviews process materials for claims that diligence will contradict. | `diligence-questioning`, `investment-memo-writing` |
| `equity-story-agent` | Develops the equity story that a sale or listing process is built on. | `pitchbook-construction`, `investment-memo-writing` |
| `financial-section-agent` | Drafts the financial section of a CIM or offering document. | `financial-statement-modeling`, `pitchbook-construction` |
| `growth-plan-agent` | Articulates the growth plan that supports the asking price. | `industry-analysis`, `investment-memo-writing` |
| `ipo-materials-agent` | Prepares equity story, prospectus input and analyst materials for a listing. | `pitchbook-construction`, `comparable-company-analysis` |
| `offering-memo-agent` | Drafts debt offering memoranda and lender presentations. | `lbo-modeling`, `term-sheet-analysis` |

## Deal Tracking  *(7)*

| Agent | Purpose | Skills loaded |
|---|---|---|
| `conditions-precedent-agent` | Tracks conditions precedent and closing mechanics to completion. | `deal-structuring`, `risk-assessment` |
| `deal-tracking-agent` | Maintains live deal status across workstreams and surfaces what is slipping. | `risk-assessment` |
| `issues-log-agent` | Maintains the transaction issues log and drives items to resolution. | `risk-assessment` |
| `pipeline-management-agent` | Maintains the origination pipeline and prepares pipeline reviews. | `screening-and-targeting` |
| `post-signing-tracker-agent` | Tracks the period between signing and closing including integration readiness. | `synergy-quantification`, `risk-assessment` |
| `timeline-management-agent` | Builds and reforecasts transaction timetables against actual progress. | `precedent-transaction-analysis`  ·  **India-sensitive** |
| `workstream-coordination-agent` | Coordinates advisers and workstreams across a transaction. | `diligence-questioning` |

## KPIs & Dashboards  *(7)*

| Agent | Purpose | Skills loaded |
|---|---|---|
| `covenant-monitoring-agent` | Monitors covenant compliance and forecasts headroom forward. | `lbo-modeling`, `scenario-and-stress-testing` |
| `integration-scorecard-agent` | Builds the post-close integration scorecard across workstreams. | `synergy-quantification`, `risk-assessment` |
| `kpi-dashboard-agent` | Designs and maintains the KPI dashboard for a business or a portfolio. | `financial-statement-modeling` |
| `market-monitoring-agent` | Monitors market conditions relevant to live transactions and mandates. | `industry-analysis`, `term-sheet-analysis` |
| `portfolio-monitoring-agent` | Monitors a portfolio of investments against their underwriting cases. | `scenario-and-stress-testing`, `valuation-techniques` |
| `synergy-tracking-agent` | Tracks realised synergies against the deal case after closing. | `synergy-quantification` |
| `valuation-monitoring-agent` | Tracks how a valuation moves with market and performance changes. | `valuation-techniques`, `comparable-company-analysis` |

## Committee Materials  *(7)*

| Agent | Purpose | Skills loaded |
|---|---|---|
| `approval-conditions-agent` | Drafts approval conditions, delegated authority and the path to signing. | `investment-memo-writing`, `deal-structuring` |
| `committee-qa-agent` | Prepares the question-and-answer pack for a committee session. | `investment-memo-writing` |
| `devils-advocate-agent` | Argues against a transaction using only the facts already assembled. | `investment-memo-writing`, `risk-assessment` |
| `investment-memo-agent` | Drafts the investment committee memo end to end. | `investment-memo-writing`, `risk-assessment` |
| `post-investment-review-agent` | Reviews a completed transaction against what was underwritten. | `investment-memo-writing`, `risk-assessment` |
| `premortem-agent` | Runs a structured pre-mortem on a transaction before approval. | `risk-assessment`, `investment-memo-writing` |
| `risk-register-agent` | Builds the quantified risk register for a transaction. | `risk-assessment` |

## Specialist  *(14)*

| Agent | Purpose | Skills loaded |
|---|---|---|
| `activist-defence-agent` | Prepares a company's defence against activist shareholder campaigns. | `valuation-techniques`, `buyer-universe-mapping` |
| `capital-structure-agent` | Advises on optimal capital structure and capital allocation. | `lbo-modeling`, `valuation-techniques` |
| `carve-out-analysis-agent` | Analyses a divestment carve-out including standalone costs and separation. | `financial-statement-modeling`, `deal-structuring` |
| `creditor-recovery-agent` | Models recoveries by creditor class through the waterfall. | `lbo-modeling`, `valuation-techniques`  ·  **India-sensitive** |
| `cross-border-agent` | Assesses cross-border transaction considerations beyond the commercial terms. | `deal-structuring`, `risk-assessment`  ·  **India-sensitive** |
| `financing-markets-agent` | Assesses current financing market conditions and available structures. | `term-sheet-analysis`, `lbo-modeling` |
| `hostile-bid-agent` | Analyses and prepares for unsolicited and hostile takeover situations. | `valuation-techniques`, `buyer-universe-mapping`, `risk-assessment`  ·  **India-sensitive** |
| `integration-planning-agent` | Builds the post-close integration plan aligned to the synergy case. | `synergy-quantification`, `risk-assessment` |
| `joint-venture-agent` | Structures and evaluates joint ventures and partnerships. | `deal-structuring`, `valuation-techniques` |
| `minority-stake-agent` | Evaluates minority investments and the protections they require. | `valuation-techniques`, `deal-structuring`  ·  **India-sensitive** |
| `rating-agency-agent` | Assesses rating implications and prepares rating agency materials. | `lbo-modeling`, `term-sheet-analysis` |
| `restructuring-analysis-agent` | Analyses a distressed capital structure and the restructuring options. | `valuation-techniques`, `scenario-and-stress-testing`, `deal-structuring`  ·  **India-sensitive** |
| `sector-specialist-agent` | Applies sector-specific valuation metrics, drivers and conventions. | `industry-analysis`, `valuation-techniques` |
| `source-verification-agent` | Verifies every figure in a deliverable against its primary source. | `financial-statement-modeling`, `pitchbook-construction` |
