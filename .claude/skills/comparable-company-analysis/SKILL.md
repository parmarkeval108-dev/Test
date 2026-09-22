---
name: comparable-company-analysis
description: Building and defending trading comparable company analysis - peer selection, enterprise value bridges, multiple normalisation, calendarisation and regression-based valuation. Use when building a comp set, computing trading multiples, or reviewing a comps page for errors.
---

# Comparable Company Analysis

The comp set is the analysis. Selection decides the answer, so selection carries the burden of proof.

> **India:** load `india-transaction-regime` before applying this skill to an Indian company — Indian issuers report standalone and consolidated, and mixing the bases is a live error.

## Techniques

1. **Criteria-first peer selection** — Write the selection criteria before looking at any candidate: business model, size band, growth band, margin band, geography, capital intensity. Then apply them mechanically and record every include/exclude decision with its reason.
   *Fails when:* the set is assembled first and the criteria are reverse-engineered to fit.

2. **Tiered comp sets** — Separate core (direct), secondary (partial overlap) and reference (read-across) comps, with medians computed per tier. This shows the reviewer how the answer moves with comparability rather than hiding the judgement inside one median.

3. **Enterprise value bridge** — Build EV explicitly for every comp: market cap on fully diluted shares, plus gross debt, plus preferred at redemption value, plus minorities at fair value, plus net pension deficit after tax, plus capitalised leases where not in debt, less cash and equivalents, less the value of non-core assets and associates. Every line visible.
   *Fails when:* net debt is taken from a data vendor without checking what it includes.

4. **Treasury stock method dilution** — Options and warrants in the money at the current price convert, with proceeds used to repurchase shares at that price; RSUs count in full; PSUs at expected achievement; convertibles under if-converted where dilutive. Recompute at each valuation price, not once.

5. **Calendarisation** — Restate every comp to a common year-end by interpolating quarterly data. Flag any company where the interpolation spans a period of known disruption — the estimate is then not reliable.

6. **Definitional normalisation** — Force one definition of EBITDA, one lease treatment, one SBC convention and one capitalisation policy across the set, restating any filer that differs. Consistency matters more than which convention you pick, but state which you picked.
   *Fails when:* an IFRS 16 filer and a US GAAP filer sit in the same EV/EBITDA column untouched.

7. **Consensus hygiene** — For forward multiples record the estimate source, contributor count and estimate date. Drop any estimate that predates the company's most recent earnings release. Stale consensus produces multiples that are simply wrong.

8. **Growth and return adjustment** — Compute multiple-to-growth ratios and compare multiples against ROIC. A discount that disappears once adjusted for growth is not a discount.

9. **Regression valuation** — Regress EV/EBITDA on forward growth and margin across the set, report R² and coefficients, and read `<Company>`'s implied multiple off the line. State plainly whether the R² justifies using the regression — below roughly 0.5 it does not.

10. **Outlier protocol** — Identify outliers by the interquartile rule, then decide keep / exclude / winsorise and show the median under all three. The decision is disclosed, not silent.

11. **Historical relative trading** — Chart the subject's multiple against the peer median over three to five years. Quantify the mean premium or discount and identify what broke the relationship and when. This converts a static snapshot into evidence about a re-rating.

12. **Error sweep** — Run the standard defect list before publishing: period mismatch, EV-versus-equity metric mismatch, share counts on different dates, double-counted leases, stale estimates, mixed currencies, inconsistent minority treatment, and a subject company held to a different standard than its peers.

## Quality bar

- [ ] Every metric ties to a primary filing with a page reference
- [ ] Exclusions documented with reasons a hostile reviewer would accept
- [ ] One EBITDA definition, one lease treatment, one SBC convention
- [ ] Mean and median both shown where they diverge materially
- [ ] Implied range stated with the net debt and share count used

## Outputs

Comp table with quartiles, EV bridge per company, implied valuation range, source log, exclusion log.
