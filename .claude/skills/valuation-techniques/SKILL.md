---
name: valuation-techniques
description: Core valuation methods for investment banking - selecting an approach, reconciling methodologies, building a football field, and defending a value range. Use when valuing a company or asset, building a valuation section, reconciling a value gap, or reviewing someone else's valuation work.
---

# Valuation Techniques

Valuation is an argument about the future supported by evidence, not a calculation. Every number carries a source; every judgement is stated as a judgement.

## Method selection

Pick methods from what the asset is, not from habit.

| Situation | Primary | Support | Avoid |
|---|---|---|---|
| Stable cash generative | DCF | Trading comps, precedents | Asset-based |
| High growth, pre-profit | DCF with fade, revenue multiples | Growth-comp regression | LTM EBITDA multiples |
| Cyclical | Mid-cycle EBITDA multiple | Through-cycle DCF | Peak or trough LTM |
| Asset-heavy / real assets | NAV, replacement cost | DCF, yield comps | Earnings multiples alone |
| Financial institution | Dividend discount, P/TBV vs ROTE | Regulatory capital-adjusted | EV/EBITDA (meaningless) |
| Distressed | Liquidation and going-concern recovery | Distressed precedents | Standard comps |
| Control transaction | Precedents with control premium | DCF with synergies | Unadjusted trading comps |
| LBO candidate | LBO ability-to-pay | DCF, precedents | — |

## Techniques

1. **Football field construction** — Present each methodology as a horizontal bar with an explicit low and high. Label what drives each endpoint in six words. State in the header what range you actually recommend and why it sits where it does inside the overlap.
   *Fails when:* bars are drawn wide enough to overlap comfortably. Width must come from the analysis, not from a desire for a tidy picture.

2. **Methodology reconciliation** — Where two methods disagree by more than 15%, find the assumption responsible rather than averaging. Compare the DCF's implied exit multiple against the comp median; compare the comp median's implied perpetuity growth against your terminal `g`.
   *Fails when:* the reconciliation stops at "different methods give different answers."

3. **Implied-multiple cross-check** — Convert every output back to a multiple of the same metric. A DCF that implies 22x when peers trade at 11x is making a claim you must be able to state in words.

4. **Control premium application** — Apply control premia only to minority-basis values, sized from the specific synergies and control benefits available to the named buyer. Sector-average premia are a sanity check, not a method.
   *Fails when:* a control premium is stacked on top of precedent transactions that already reflect control.

5. **Minority and marketability discounts** — Size DLOM from restricted-stock and pre-IPO studies with the study named; size minority discounts as the inverse of the control premium. State both separately — never as one combined haircut.

6. **Sum-of-the-parts** — Value each segment on its own appropriate method and peer set, then subtract the present value of unallocated corporate costs and consolidated debt. Show the implied conglomerate discount against the traded value.
   *Fails when:* central costs are ignored, inflating value by the capitalised value of the head office.

7. **Mid-cycle normalisation** — For cyclical assets, value off mid-cycle earnings with the cycle defined by a stated historical window, not off LTM. Show where in the cycle LTM sits.

8. **Liquidation and recovery valuation** — Build orderly and forced-sale values by asset class with recovery percentages sourced from comparable insolvencies, net of wind-down costs and priority claims. Waterfall to each creditor class.

9. **Real-options valuation** — Where value depends on a decision that can be deferred (a development pipeline, an undeveloped reserve, an expansion right), value the option separately with stated volatility and time to expiry. Use it to supplement a DCF, never to rescue one.

10. **Value-gap bridge** — Bridge the traded value to the intrinsic value in named increments: operational improvement, capital structure, portfolio actions, multiple re-rating. This is the page that gives an activist or a bidder their argument — and the page that defends against one.

11. **Cross-check against market evidence** — Test every output against what has actually been paid: recent transactions, the current share price, any prior offer. A valuation that no buyer would pay and no seller would accept needs its assumptions revisited.

12. **Valuation date discipline** — Fix a single valuation date. Market data, net debt, share count, FX and estimates all come from that date. Mixed-date inputs are the most common and most embarrassing defect in a valuation.

## Quality bar

- [ ] Every input has a source and a retrieval date
- [ ] One valuation date used consistently throughout
- [ ] Enterprise and equity metrics never mismatched
- [ ] Share count fully diluted and stated
- [ ] Methods reconciled, not averaged
- [ ] The recommended range is narrower than the union of all bars, and the narrowing is justified
- [ ] What would make this valuation wrong is stated explicitly

## Outputs

Football field, valuation summary table, methodology reconciliation, source log, and a one-page statement of the recommended range with its three supporting arguments.
