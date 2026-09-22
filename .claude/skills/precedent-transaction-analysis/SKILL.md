---
name: precedent-transaction-analysis
description: Building precedent transaction analysis - transaction selection, rebuilding deal enterprise value from terms, premium analysis against unaffected prices, and deal-terms benchmarking. Use when analysing comparable M&A transactions, computing premia, or benchmarking deal terms.
---

# Precedent Transaction Analysis

Press-reported deal multiples are unreliable. Rebuild each one from the announced terms or mark it as an estimate.

## Techniques

1. **Window justification** — State why the lookback period is what it is by naming what changed at its boundary: a rate regime, a regulatory change, a sector cycle turn. Show medians inside and outside the window so the reviewer can see the effect of the choice.

2. **Deal EV reconstruction** — Rebuild enterprise value from the terms: equity consideration at announcement-date value, plus assumed debt, plus the expected value of earn-outs, plus rollover, plus preferred and minorities, less cash acquired. Do not take the press figure.
   *Fails when:* an earn-out-heavy deal is recorded at maximum consideration, inflating the multiple.

3. **Multiple basis alignment** — Confirm whether each multiple is LTM-at-announcement, LTM-at-close or forward, and restate all to one basis. Announcement-date LTM is the default because it matches the information the buyer had.

4. **Synergy-inclusive detection** — Identify deals where the disclosed multiple is struck on post-synergy EBITDA and restate to pre-synergy. Mixing the two understates what buyers actually paid.

5. **Unaffected-price premium** — Compute premia to the 1-day, 5-day, 30-day and 90-day VWAP and to the 52-week high. Where price ran up on leakage, determine the unaffected date from abnormal volume and compute the premium from there, stating how you set the date.
   *Fails when:* a single one-day premium is presented as "the premium."

6. **Premium driver regression** — Regress premium against size, acquirer type, consideration mix, competing bidders and rate environment. This tells you which of your deal's characteristics actually predict what it should clear at.

7. **Competing-bid isolation** — Separate deals with a confirmed second bidder and quantify the incremental premium tension produced. This is the number that justifies running a process.

8. **Process-type tagging** — Tag each deal as broad auction, targeted, bilateral or hostile, and compare multiples by type. Bilateral deals are not evidence for what an auction achieves.

9. **Deal-terms benchmarking** — Catalogue break fees as a percentage of equity value, reverse break fees, financing conditionality, MAC carve-outs, escrow size and tenor, W&I usage, and regulatory conditions. Benchmark the proposed terms against the distribution.

10. **Timeline benchmarking** — Compute median days from announcement to close, split by whether a second request or Phase 2 review occurred, and by acquirer nationality. Use it to set the client's expectations before they set their own.

11. **Cycle placement** — Locate each deal on the sector cycle and in its rate environment at announcement. Adjust the implied multiple for today's conditions explicitly, showing the arithmetic rather than asserting a judgement.

12. **Precedent-versus-trading gap** — Decompose the difference between precedent and trading medians into control premium, capitalised synergies and market drift since the deals were struck. An unexplained gap is a finding, not a footnote.

## Quality bar

- [ ] Disclosed and estimated multiples distinguished, with medians shown both ways
- [ ] Every deal traceable to a primary source — announcement, filing, or circular
- [ ] Failed deals listed with the reason each failed
- [ ] Distressed transactions separated from the main set
- [ ] All values in one currency at announcement-date spot

## Outputs

Transaction table with multiples and premia, the five most relevant deals with rationale, deal-terms benchmark, implied range, source log.
