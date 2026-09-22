# Pitchbook Workflow

**Layer:** Execution  ·  **System:** Client Delivery  ·  **Typical duration:** 1–3 weeks

## When to run

A client presentation, pitch or board deck is required.

## Inputs required

- The objective and the decision being sought
- The audience and who actually decides
- Available analysis and the time to produce more

## Phases

### Phase 1 — Argue  *(2–3 days)*

| # | Action | Agent |
|---|---|---|
| 1.1 | Answer the four framing questions before outlining anything | `storyline-agent` |
| 1.2 | Write the argument as ten sentences and test each for available evidence | `storyline-agent` |
| 1.3 | Map audience objections to the sentence that pre-empts each | `storyline-agent` |

### Phase 2 — Plan  *(1–2 days)*

| # | Action | Agent |
|---|---|---|
| 2.1 | Build the page inventory with title, message, exhibit, source and owner | `pitchbook-drafting-agent` |
| 2.2 | Delete every page that would appear in a pitch to any other client | `pitchbook-drafting-agent` |
| 2.3 | Get the inventory approved before anyone opens a template | `pitchbook-drafting-agent` |

### Phase 3 — Analyse and build  *(1–2 weeks)*

| # | Action | Agent |
|---|---|---|
| 3.1 | Run the analysis each page requires | `valuation-agent` |
| 3.2 | Build benchmarking and market exhibits | `benchmarking-page-agent` |
| 3.3 | Design each exhibit to prove its page's message | `exhibit-design-agent` |
| 3.4 | Assemble relevant credentials only | `credentials-agent` |

### Phase 4 — Sharpen  *(2–3 days)*

| # | Action | Agent |
|---|---|---|
| 4.1 | Rewrite every title as a conclusion under twelve words | `action-title-agent` |
| 4.2 | Run the title-only flow test and reorder where it breaks | `action-title-agent` |

### Phase 5 — Verify and deliver  *(1–2 days)*

| # | Action | Agent |
|---|---|---|
| 5.1 | Verify every figure against its source | `deck-quality-control-agent` |
| 5.2 | Run the consistency sweep and produce the defect list | `deck-quality-control-agent` |
| 5.3 | Write the delivery brief and the leave-behind version | `pitchbook-drafting-agent` |

## Gates

- **Storyline gate** — No page is built before the ten-sentence argument is agreed.
- **Differentiation gate** — Something in the deck must be impossible for a competitor with the same public data to replicate.
- **Verification gate** — Any figure not verified against its source comes off the page.

## Definition of done

- [ ] Titles alone make a complete argument
- [ ] Every exhibit proves its title
- [ ] Every page carries a source line
- [ ] Fact verification table complete
- [ ] Delivery brief written with the three pages that must land

## Common failure modes

- Building pages before agreeing the argument, then rebuilding them
- Fifteen pages of market context the client knows better than the bank
- A chart that is interesting but does not prove the title above it
