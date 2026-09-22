# Engagement Contexts

The kit is organised around the situations a coverage or product team is actually in. Each context names the workflows that run, the skills that carry the most weight, and the thing that most often goes wrong.

---

## M&A Advisory

Buy-side and sell-side advisory on control transactions.

**Workflows:** `deal-screening` · `target-approach` · `buyer-list` · `process-management` · `valuation` · `diligence` · `merger-model` · `investment-committee` · `transaction-closing`
**Weighted skills:** `valuation-techniques` · `comparable-company-analysis` · `precedent-transaction-analysis` · `synergy-quantification` · `deal-structuring`
**Most common failure:** ranking bids on headline price when the structures differ materially. Net expected proceeds is the only comparable number.

## Capital Markets (ECM)

Equity raising, listings, secondary offerings and equity-linked issuance.

**Workflows:** `ipo-readiness` · `valuation` · `pitchbook` · `capital-allocation-review`
**Weighted skills:** `comparable-company-analysis` · `valuation-techniques` · `pitchbook-construction` · `accretion-dilution-modeling`
**Most common failure:** committing publicly to a KPI the company cannot produce accurately under a quarterly reporting deadline.

## Debt Capital Markets (DCM)

Bond issuance, private placements and rating advisory.

**Workflows:** `financing` · `refinancing` · `capital-allocation-review`
**Weighted skills:** `term-sheet-analysis` · `lbo-modeling` · `scenario-and-stress-testing` · `financial-statement-modeling`
**Most common failure:** counting the spread saving on a refinancing while ignoring the call premium and the unamortised fee write-off.

## Leveraged Finance

Acquisition financing, leveraged loans, high yield and private credit.

**Workflows:** `financing` · `refinancing` · `merger-model` · `diligence`
**Weighted skills:** `lbo-modeling` · `term-sheet-analysis` · `scenario-and-stress-testing` · `risk-assessment`
**Most common failure:** sizing leverage from a market benchmark with no downside test behind it, and accepting the drafted EBITDA definition without reading the add-back cap.

## Restructuring & Special Situations

Liability management, distressed M&A, recapitalisation and formal processes.

**Workflows:** `restructuring` · `refinancing` · `carve-out-divestiture` · `transaction-closing`
**Weighted skills:** `valuation-techniques` · `scenario-and-stress-testing` · `deal-structuring` · `risk-assessment`
**Most common failure:** negotiating before the fulcrum security has been identified and tested across a value range.

## Fairness Opinions & Valuations

Board opinions, valuations for transactions, disputes and reporting.

**Workflows:** `fairness-opinion` · `valuation`
**Weighted skills:** `valuation-techniques` · `comparable-company-analysis` · `precedent-transaction-analysis` · `dcf-and-sensitivity`
**Most common failure:** a selection criterion applied to the peer set but not to the subject company, and a file that cannot be reconstructed a year later.

## Strategic Alternatives

Portfolio review, separation analysis, activist response and defence.

**Workflows:** `capital-allocation-review` · `carve-out-divestiture` · `activist-defence` · `hostile-defence` · `joint-venture`
**Weighted skills:** `valuation-techniques` · `deal-structuring` · `risk-assessment` · `investment-memo-writing`
**Most common failure:** defending a value gap rather than addressing it, and mounting a defence on a standalone plan the board has never previously committed to.

---

# Jurisdictions

The method layer of this kit is jurisdiction-neutral. The **regime layer is not**, and applying a generic method to a company under an unfamiliar regime produces a confidently wrong answer rather than an incomplete one.

## India

**Skill:** `india-transaction-regime` — load it before `deal-structuring`, `buyer-universe-mapping`, `valuation-techniques` or any restructuring work on an Indian situation. Eighteen agents and eight skills carry a pointer to it.

The seven places a generic method breaks:

| Area | What changes |
|---|---|
| **Open offers** | SEBI (SAST) triggers a mandatory offer for a minimum 26% of voting capital on crossing 25%, on change of control, or on creeping past 5% in a year. Funding is the stake *plus* the offer. |
| **Cross-border price** | FEMA sets a fair-value floor for a non-resident buying and a ceiling for a non-resident selling. Price is bounded by rule, and the bound reverses with the direction of travel. |
| **Inbound FDI** | Press Note 3 requires prior government approval for land-border-country investors, tested on **beneficial ownership**, not incorporation. Approval is slow and often refused. |
| **Merger control** | CCI thresholds include a ₹2,000 crore deal value test catching loss-making targets; Green Channel clears no-overlap deals on filing; overall timeline cut to 150 days. |
| **Insolvency** | IBC is creditor-controlled through the CoC with a 330-day outer limit, and Section 29A can bar the existing promoter from bidding for their own asset. |
| **Control** | The promoter and promoter group, not the institutional register, decide whether a sale is deliverable. Pledged promoter shares are a distress signal. |
| **Tax** | The s.115BAA election moves the effective rate by roughly 1,000bps; Section 79 forfeits carried-forward losses outright on a change of control. |

**Most common failure:** sizing an acquisition envelope against the negotiated stake and discovering the open-offer obligation after signing.

## Adding another jurisdiction

Follow the same pattern rather than forking the kit:

1. Write one `<jurisdiction>-transaction-regime` skill holding every rule that changes an answer, each with its source and retrieval date.
2. Add a one-line `**Jurisdiction:**` pointer to the agents that would otherwise reason to a wrong answer, naming the specific reason.
3. Add a `> **<Jurisdiction>:**` note under the H1 of the skills whose method the regime bounds.
4. Add the jurisdiction's table to this file.
5. State the verification date and treat every threshold as requiring reconfirmation — securities and competition rules move.
