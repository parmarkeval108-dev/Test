---
name: india-transaction-regime
description: India-specific transaction rules that change the answer - SEBI SAST open offers, FEMA pricing floors and ceilings, Press Note 3, CCI merger control and the deal value threshold, IBC insolvency and Section 29A, delisting, promoter structures, Ind AS reporting and Indian valuation inputs. Use whenever a target, acquirer, listing or asset is Indian, before applying any generic valuation, structuring, buyer-list or restructuring method.
---

# India Transaction Regime

The method layer of this kit is jurisdiction-neutral and transfers to India unchanged: discounting, the EV bridge, treasury-method dilution, synergy grading, memo structure. This skill covers the places where applying the generic method to an Indian company produces a **wrong answer, not merely an incomplete one**.

Load this before `deal-structuring`, `buyer-universe-mapping`, `valuation-techniques` or any restructuring work on an Indian situation.

> **Verification status.** Every figure below was checked against the sources listed at the end on **22 September 2026**. Indian securities, competition and exchange-control rules are amended frequently — SEBI and CCI both moved in the last two years. Treat every threshold as requiring confirmation against the current instrument before it reaches a deal. Where this skill states market practice rather than a rule, it is labelled as judgement.

## Techniques

1. **Open-offer funding — size the bid before you size the stake** — Under SEBI (SAST) Regulations 2011, acquiring 25% or more of voting rights, acquiring control, or creeping beyond 5% in a financial year while holding 25–75%, triggers a mandatory open offer to public shareholders for a minimum of **26% of total voting share capital** (Reg. 7(1)). The acquirer must therefore fund the negotiated stake *plus* up to 26% more at the open-offer price, with escrow posted up front.
   *Fails when:* `ability-to-pay-agent` sizes an envelope against the stake being negotiated. An acquirer who can afford 51% of an Indian listed company frequently cannot afford 51% plus a 26% open offer, and discovers it after signing.

2. **Open-offer price as a valuation floor** — The offer price is set by a formula referencing negotiated price and historical market prices, not by negotiation. It puts a statutory floor under what minorities receive, which compresses the premium a buyer can pay the seller without raising the cost of the whole transaction.
   *Fails when:* a premium analysis treats the negotiated per-share price as the only price being paid.

3. **FEMA pricing — price is not freely negotiable cross-border** — Under the FEMA Non-Debt Instruments Rules, a non-resident acquiring from a resident may not pay **below** fair value (a floor), and a non-resident selling to a resident may not receive **above** fair value (a ceiling). Unlisted-share fair value must be determined by a Chartered Accountant or SEBI-registered merchant banker using DCF, NAV or a comparable-transaction method.
   *Fails when:* `deal-structuring` treats price as the output of negotiation. In a cross-border Indian deal it is bounded on one side by rule, and the bound runs in opposite directions depending on the direction of travel. A distressed sale to a foreign buyer below fair value is not available.

4. **Deferred consideration is capped, not barred** — Up to **25% of total consideration may be deferred for up to 18 months** from execution of the transfer agreement. Earn-outs, escrows and working-capital true-ups must be built inside that envelope.
   *Fails when:* an earn-out is designed over three years at 40% of consideration, as it would be elsewhere, and the structure is not permissible.

5. **Press Note 3 — the inbound FDI screen** — Since 17 April 2020, any investment by an entity of a country sharing a land border with India (Afghanistan, Bangladesh, Bhutan, China, Myanmar, Nepal, Pakistan), **or where the beneficial owner is situated in or a citizen of such a country**, requires prior government approval regardless of sector. Approval is slow and frequently refused: of 526 proposals received, 124 were approved, 201 rejected and 200 still pending as of the reported figures.
   *Fails when:* `buyer-universe-agent` tiers a Chinese strategic or a fund with Chinese LP beneficial ownership as a Tier 1 buyer. The beneficial-owner test reaches through intermediate holding structures, so a Singapore or Mauritius vehicle does not cure it. Such a buyer is a stalking horse, not a closer.

6. **CCI merger control and the deal value threshold** — Notification is required on asset/turnover thresholds, and since the Competition (Amendment) Act 2023 also where **deal value exceeds ₹2,000 crore and the target has substantial business operations in India** — which catches digital and loss-making targets that escape asset tests. The CCI's overall approval timeline was reduced from 210 to 150 days. Transactions with no horizontal, vertical or complementary overlap may file under the **Green Channel** and are deemed approved on filing.
   *Fails when:* `antitrust-screening-agent` reasons toward a second-request or Phase 2 framing. Green Channel means a clean deal clears on the day it is filed; the deal value threshold means a no-revenue target can still be notifiable.

7. **Delisting — reverse book building or fixed price** — SEBI's September 2024 amendments cut the RBB success threshold from 90% to **75% post-offer acquirer shareholding, provided at least 50% of public shareholding is tendered** to the counter-offer, and introduced an alternative **fixed-price route at a minimum 15% premium to floor price**, available only where shares are frequently traded.
   *Fails when:* a take-private screen is run on Western assumptions, or on the pre-2024 90% threshold, and dismisses candidates that are now deliverable. Take-privates in India became materially easier in 2024.

8. **Promoter structure — who actually controls the outcome** — Indian listed companies disclose "promoter and promoter group" holdings, a concept with no Western equivalent. Promoter share **pledging** is separately disclosed and is a live distress signal. Control frequently sits with a family or founder group well below a majority stake.
   *Fails when:* `ownership-structure-agent` maps institutional holders and concludes a board can deliver a sale. Identify the promoter group, its aggregate holding, its pledge position and any inter-se agreement before assessing deliverability.

9. **Related-party transactions with promoter entities** — Promoter-affiliated supply, property, lending and service arrangements are common and material. They affect normalised EBITDA directly, and they may not survive a change of control.
   *Fails when:* `quality-of-earnings-agent` runs a generic add-back review. In India, weight related-party pricing and promoter-entity dependency far above the default; ask whether each arrangement is arm's length and what replaces it post-close.

10. **Standalone versus consolidated — pick one and enforce it** — Indian listed companies report both standalone and consolidated financials. Multiples computed on standalone earnings against an EV that reflects consolidated debt are wrong, and the two bases circulate interchangeably in market commentary. *Judgement: consolidated is the appropriate basis for most comp work, but state the choice and apply it to every company including the subject.*
    *Fails when:* a comp set silently mixes bases. Add this to the `comparable-company-analysis` error sweep for any Indian peer group.

11. **Indian discount-rate inputs** — Risk-free from the 10-year Indian government security, not a US Treasury. Equity risk premium must incorporate an India country risk premium. Betas measured against the Nifty 50 or BSE Sensex; low-float and promoter-dominated names produce unreliable regression betas, so peer unlevered-relevered beta is usually the better estimate.
    *Fails when:* `wacc-agent` builds a rate from developed-market inputs and adds a country premium as an afterthought, or trusts a regression beta on a stock with 70% promoter holding and thin float.

12. **Tax rate and regime election** — A domestic company may elect the concessional regime under **s.115BAA at 22% plus surcharge and cess, an effective 25.17%**, forfeiting most deductions and any carried-forward losses attached to them; the election is irrevocable. Companies that have not elected sit near an effective 34.94%.
    *Fails when:* a cash tax build applies one statutory rate without establishing which regime the target has elected. The two differ by roughly 1,000 basis points of effective rate.

13. **Loss carryforward on a change of control — Section 79** — For a company in which the public are not substantially interested, carried-forward losses are **forfeited unless shareholders holding at least 51% of voting power on the last day of the loss year still hold 51% on the last day of the set-off year**. This is India's analogue to the US Section 382 limitation, and it is harsher: the losses are lost outright rather than rate-limited.
    *Fails when:* an NOL asset is valued in an acquisition of an unlisted Indian company. In most control transactions it goes to zero — check before ascribing value.

14. **IBC — the process is creditor-controlled and time-bound** — Corporate insolvency resolution runs through a Committee of Creditors, with an outer limit of **330 days including litigation and stays**. The CoC, not the debtor or the court, selects the resolution plan.
    *Fails when:* `restructuring-analysis-agent` reasons toward a debtor-in-possession, Chapter 11-shaped negotiation. In India the promoter loses control on admission, and the question "who controls the outcome" resolves to the CoC.

15. **IBC Section 29A — the promoter may be barred from bidding** — Section 29A disqualifies defaulting promoters and connected persons from submitting a resolution plan, including anyone whose account was classified as an NPA for at least a year before CIRP commencement, undischarged insolvents and disqualified directors. The Supreme Court has held the bar does not apply to MSMEs.
    *Fails when:* a buyer universe for a distressed Indian asset includes the existing promoter as the natural acquirer. Check eligibility before building the list — this reshapes the entire bidder set.

16. **Scheme of arrangement and NCLT timelines** — Mergers, demergers and many restructurings proceed by scheme under the Companies Act 2013 with National Company Law Tribunal sanction. Timelines run to many months and are outside the parties' control.
    *Fails when:* `timeline-management-agent` benchmarks against a Western statutory-merger timetable. Build the NCLT step into the critical path from day one and treat it as the long pole.

17. **Indian data sources** — Listed filings from BSE and NSE and the SEBI portal. **Private company financials are filed and publicly obtainable through MCA21** — better availability than many jurisdictions, and often overlooked. Sector and company databases: Prowess (CMIE), Capitaline, AceEquity.
    *Fails when:* `public-filings-extraction-agent` treats an unlisted Indian target as an information void. Check MCA21 before concluding a figure is unobtainable.

## Quality bar

- [ ] Open-offer trigger tested, and its funding included in the affordability envelope
- [ ] FEMA pricing floor or ceiling identified and the direction of travel stated
- [ ] Deferred consideration inside the 25% / 18-month envelope
- [ ] Every buyer screened for Press Note 3 beneficial ownership, not just place of incorporation
- [ ] CCI thresholds tested including the deal value threshold; Green Channel eligibility assessed
- [ ] Promoter group, aggregate holding and pledge position mapped before deliverability is scored
- [ ] Standalone versus consolidated basis chosen, stated and applied to every company
- [ ] Tax regime election established before any cash tax build
- [ ] Section 79 tested before any value is ascribed to carried-forward losses
- [ ] For distressed situations: Section 29A eligibility tested before the bidder list is built
- [ ] Every threshold in this skill reconfirmed against the current instrument

## Outputs

India regulatory pathway with approvals and timelines, open-offer funding analysis, FEMA pricing assessment, Press Note 3 screen, CCI notifiability and route assessment, promoter and pledge map, India-based discount rate build, tax regime and Section 79 findings.

## Sources

Checked 22 September 2026. Secondary sources are labelled as such; confirm against the primary instrument before relying on any threshold.

- SEBI (SAST) Regulations 2011 — [SEBI FAQ (primary, PDF)](https://www.sebi.gov.in/sebi_data/faqfiles/aug-2017/1503313163982.pdf) · [open offer triggers and Reg. 7(1) minimum 26%](https://taxguru.in/sebi/sebi-sast-open-offer-triggers-25-percent-creeping-acquisition-control.html) *(secondary)*
- Press Note 3 (2020) — [PIB, Investment from Land Border Sharing Countries (primary)](https://www.pib.gov.in/PressReleasePage.aspx?PRID=1808806) · [PwC news alert, 18 April 2020 (PDF)](https://www.pwc.in/assets/pdfs/news-alert-tax/2020/pwc_news_flash_18_april_2020_fdi_press_note_3_amendment.pdf) · [approval statistics](https://www.india-briefing.com/news/india-approves-124-fdi-proposals-from-neighboring-countries-32287.html/) *(secondary)*
- Competition (Amendment) Act 2023 — [CCI, Salient Features (primary, PDF)](https://www.cci.gov.in/images/publications_booklet/en/competition-amendment-act-2023-salient-features1684831868.pdf) · [deal value threshold notified](https://www.business-standard.com/companies/news/mca-notifies-deal-value-threshold-for-mergers-under-competition-act-124090901074_1.html) · [Green Channel route](https://www.snrlaw.in/one-year-of-the-ccis-green-channel-route-for-deemed-approval-of-combinations/) *(secondary)*
- FEMA pricing and deferred consideration — [Rule 21 FDI pricing compliance](https://harchandani.in/articles/mastering-fema-fdi-pricing-rules-ultimate-guide-to-rule-21-compliance) · [25% / 18-month deferred consideration](https://www.mondaq.com/india/inward-foreign-investment/1792292/acquisition-by-an-focc-of-an-indian-company-pricing-conditions-for-resident-and-non-resident-shareholders) *(both secondary — confirm against FEMA NDI Rules)*
- SEBI (Delisting) Regulations 2021, 2024 amendments — [SEBI Delisting (Amendment) Regulations 2024](https://taxguru.in/sebi/securities-exchange-board-india-delisting-equity-shares-amendment-regulations-2024.html) · [new delisting regime, key highlights](https://corporate.cyrilamarchandblogs.com/2024/09/new-delisting-regime-key-highlights/) · [fixed price method](https://indiacorplaw.in/2024/07/22/striking-a-balance-sebis-fixed-price-method-in-voluntary-delisting/) *(secondary)*
- IBC 2016 — [Section 29A ineligibility](https://www.ijllr.com/post/persons-not-eligible-to-be-resolution-applicant-section-29a-ibc) · [CIRP 330-day outer limit](https://www.taxmann.com/post/blog/conducting-corporate-insolvency-resolution-process) · [MSME exemption, Supreme Court](https://www.scconline.com/blog/post/2023/12/09/section-29a-ibc-disqualification-promotors-applying-resolution-plan-not-applicable-to-msme-supreme-court/) *(secondary)*
- Income-tax Act 1961 — [Section 79 (primary, incometaxindia.gov.in)](https://www.incometaxindia.gov.in/w/section-79-22) · [Section 115BAA rate and conditions](https://cleartax.in/s/section-115-baa-tax-rate-domestic-companies) *(secondary)*
