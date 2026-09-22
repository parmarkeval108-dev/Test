# The Claude Investment Banking Kit

**Prompts + Skills + Agents + Workflows + Systems**

A working toolkit for investment banking analysis, built as real Claude Code components rather than as a document about them. Open this repository in Claude Code and the skills and agents load automatically.

```
Prompts ──▶ Skills ──▶ Agents ──▶ Workflows ──▶ Systems
spark      build IB    generate   drive          create
insights   expertise   intelligence  structured   lasting
                                  execution      impact
```

---

## The five layers

| # | Layer | What it is | Count | Where |
|---|---|---|---|---|
| 1 | **[Prompts](prompts/README.md)** — the Insight Layer | Demanding, specific prompts that ask for the source, the driver and the disproving fact | **505** across 12 libraries | `ib-kit/prompts/` |
| 2 | **[Skills](skills/README.md)** — the Thinking Layer | Working Claude Code skills encoding named techniques with their methods and failure modes | **19** skills, **265** techniques | `.claude/skills/` |
| 3 | **[Agents](agents/README.md)** — the Intelligence Layer | Working Claude Code subagents with a mission, method, output and non-negotiables | **107** across 12 families | `.claude/agents/` |
| 4 | **[Workflows](workflows/README.md)** — the Execution Layer | Sequenced, gated procedures chaining agents into deliverables | **26** workflows | `ib-kit/workflows/` |
| 5 | **[Systems](systems/README.md)** — the Impact Engine | Standing operating models with their own state, cadence and measures | **3** systems | `ib-kit/systems/` |

**[Engagement contexts](CONTEXTS.md)** — M&A Advisory · ECM · DCM · Leveraged Finance · Restructuring & Special Situations · Fairness Opinions & Valuations · Strategic Alternatives

---

## Setting it up

The kit lives in `.claude/`, so it loads automatically for any Claude Code session opened on this repository. Pick whichever route suits you.

Claude Code requires a Pro, Max, Team, Enterprise or Console account — the free claude.ai plan does not include it.

### On the web — nothing to install

Go to [claude.ai/code](https://claude.ai/code), start a session on this repository, and ask it something. The skills and agents are already there.

### On your own machine

```bash
# macOS, Linux, WSL
curl -fsSL https://claude.ai/install.sh | bash

# Windows PowerShell
irm https://claude.ai/install.ps1 | iex
```

Then:

```bash
git clone https://github.com/parmarkeval108-dev/Test.git
cd Test
claude
```

Prefer a graphical interface? The [desktop app](https://code.claude.com/docs/en/desktop-quickstart) runs Claude Code without the terminal. Full options in the [setup docs](https://code.claude.com/docs/en/setup).

### In every project, not just this one

Copy the components into your home directory and they load everywhere on that machine:

```bash
mkdir -p ~/.claude/skills ~/.claude/agents
cp -r .claude/skills/* ~/.claude/skills/
cp -r .claude/agents/* ~/.claude/agents/
```

One caveat: personal skills in `~/.claude/` do **not** load in cloud or Cowork sessions. Only the project copy does, which is why the kit ships in the repository rather than as a personal install.

---

## Using it

**Just ask.** Skills load on their own when a task matches their description. "Build a trading comp set for Company X" pulls in `comparable-company-analysis` unprompted.

**Invoke a skill directly.** `/valuation-techniques`, `/india-transaction-regime` — the command name is the directory name.

**Run an agent.** `Use the dcf-modeling-agent to value this business`, or through the Agent tool with `subagent_type: "dcf-modeling-agent"`.

**Run a workflow.** Open `ib-kit/workflows/valuation.md` and work the phases. Each phase names the agent per step, and each gate must pass before the next phase starts.

**Adopt a system.** Start with `ib-kit/systems/execution-system.md`. Stand up its five registers on day one of a mandate — the registers are what turn a set of workflows into something that improves.

### A first thing to try

> Use the trading-comps-agent to build a comp set for an Indian specialty chemicals manufacturer with ₹1,200 crore revenue. Tell me what you'd need from me, and what you cannot determine without it.

A good response names the standalone-versus-consolidated decision before it builds anything, and tells you what it does not know. If it invents a peer set and hands you confident multiples, something is wrong.

---

## The standard this kit enforces

Every component carries the same non-negotiables, because analysis that cannot be defended is worse than no analysis.

- **Every figure carries a source and a retrieval date.** Vendor estimates are labelled as estimates.
- **Nothing unverified is presented as verified.** What could not be confirmed is listed as unconfirmed.
- **Every assumption that would change the conclusion is flagged.**
- **The finding that weakens the case is reported as prominently as the one that supports it.**
- **Judgements are labelled as judgements.** Unlabelled judgement is what committees catch.

These appear in every agent definition and every skill's quality bar. They are the point of the kit.

---

## Repository layout

```
.claude/
  skills/         19 working skills — load automatically by description
  agents/        107 working subagents — invoke by name
ib-kit/
  prompts/       505 prompts across 12 libraries
  workflows/      26 gated, phased procedures
  systems/         3 standing operating models
  CONTEXTS.md    engagement contexts and their common failure modes
  README.md      this file
```

---

## A note on what this is and is not

This kit encodes method: how to select a comp set you can defend, how to build a WACC someone can check, how to grade a synergy by its evidence, how to structure a memo so a committee can decide from it.

It does not contain market data, and it will not make an unsourced number true. Every component is written on the assumption that the output will be challenged by someone with an incentive to find the error — a counterparty, a committee, a regulator, or the market. That assumption is the whole design.
