# Activist Defence Workflow

**Layer:** Execution  ·  **System:** Client Delivery  ·  **Typical duration:** Ongoing, intensive 8–16 weeks

## When to run

An activist has arrived or the company's profile makes one likely.

## Inputs required

- Shareholder register and recent movements
- Company performance versus peers
- The activist's history and playbook where identified

## Phases

### Phase 1 — Self-assess  *(2–3 weeks)*

| # | Action | Agent |
|---|---|---|
| 1.1 | Build the activist's case from the company's own data | `activist-defence-agent` |
| 1.2 | Quantify and decompose the value gap | `valuation-gap-agent` |
| 1.3 | Separate what management can address from what it cannot | `valuation-gap-agent` |

### Phase 2 — Analyse the register  *(1–2 weeks)*

| # | Action | Agent |
|---|---|---|
| 2.1 | Assess who would support an activist and the vote arithmetic | `activist-defence-agent` |
| 2.2 | Review structural defences and whether they remain available | `activist-defence-agent` |

### Phase 3 — Decide  *(2–4 weeks)*

| # | Action | Agent |
|---|---|---|
| 3.1 | Identify what the company should do anyway, regardless of the activist | `capital-structure-agent` |
| 3.2 | Compare portfolio and capital allocation alternatives on value | `valuation-gap-agent` |
| 3.3 | Prepare the response: what to announce, what to refuse | `activist-defence-agent` |

### Phase 4 — Engage  *(Ongoing)*

| # | Action | Agent |
|---|---|---|
| 4.1 | Execute the shareholder engagement plan by holder category | `activist-defence-agent` |
| 4.2 | Monitor register movements and sentiment continuously | `market-monitoring-agent` |

## Gates

- **Honesty gate** — The value gap is assessed honestly; a defence built on denying it fails.
- **Do-anyway gate** — Actions that are right regardless of the activist are separated from actions taken only in response.
- **Vote gate** — No position is taken without understanding the vote arithmetic.

## Definition of done

- [ ] Activist case reconstructed from the company's own data
- [ ] Value gap decomposed with actions and their value release quantified
- [ ] Vote arithmetic understood
- [ ] Engagement plan running with each holder category addressed

## Common failure modes

- Defending a value gap instead of addressing it
- Announcing a response that the register does not support
- Discovering the vote arithmetic after taking a public position
