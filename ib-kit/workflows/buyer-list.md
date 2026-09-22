# Buyer List Workflow

**Layer:** Execution  ·  **System:** Origination  ·  **Typical duration:** 2–3 weeks

## When to run

A sale process is being prepared and the buyer universe determines the price it achieves.

## Inputs required

- Target profile and the seller's objectives including non-price ones
- Sector transaction history and sponsor activity
- Confidentiality constraints and any do-not-contact instructions

## Phases

### Phase 1 — Build  *(1 week)*

| # | Action | Agent |
|---|---|---|
| 1.1 | Construct the strategic and financial segments methodically | `buyer-universe-agent` |
| 1.2 | Identify sponsor-owned platforms for which the target is an add-on | `buyer-universe-agent` |
| 1.3 | Research each buyer's transaction history and process behaviour | `corporate-history-agent` |

### Phase 2 — Assess  *(1 week)*

| # | Action | Agent |
|---|---|---|
| 2.1 | Filter by genuine financial capacity | `buyer-universe-agent` |
| 2.2 | Estimate buyer-specific synergies and derive willingness to pay | `ability-to-pay-agent` |
| 2.3 | Screen antitrust and FDI risk for every strategic buyer | `antitrust-screening-agent` |
| 2.4 | Grade confidentiality risk per buyer | `buyer-universe-agent` |

### Phase 3 — Prioritise and design  *(3–5 days)*

| # | Action | Agent |
|---|---|---|
| 3.1 | Tier into contact waves with a documented do-not-contact list | `buyer-universe-agent` |
| 3.2 | Recommend the process type with the trade-off stated | `process-design-agent` |
| 3.3 | Design the tension plan and the pre-emption protocol | `process-design-agent` |

### Phase 4 — Prepare outreach  *(3–5 days)*

| # | Action | Agent |
|---|---|---|
| 4.1 | Draft the anonymous teaser and run the anonymity test | `teaser-drafting-agent` |
| 4.2 | Write buyer-specific positioning and approach routes | `buyer-outreach-agent` |
| 4.3 | Set up the buyer tracker | `deal-tracking-agent` |

## Gates

- **Capacity gate** — No buyer reaches Tier 1 without demonstrated ability to fund the transaction.
- **Confidentiality gate** — Every Tier 1 contact is cleared against the seller's confidentiality constraints.
- **Anonymity gate** — The teaser fails if a sector insider could identify the company from it.

## Definition of done

- [ ] Tiered list with rationale, capacity and willingness-to-pay per buyer
- [ ] Regulatory risk ranked separately from price
- [ ] Wave plan with contact sequence and triggers
- [ ] Buyer-specific positioning for every Tier 1 name
- [ ] Do-not-contact list documented with reasons

## Common failure modes

- Ranking buyers by size or reputation rather than by what the asset is worth to them
- Contacting a buyer whose diligence access would damage the client competitively
- A teaser so cautious it interests nobody, or so specific it identifies the seller
