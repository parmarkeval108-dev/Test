# Repository guidance

This repository contains **The Claude Investment Banking Kit** — see `ib-kit/README.md`.

## Structure

- `.claude/skills/` — 19 investment banking skills. They load automatically when a task matches their description.
- `.claude/agents/` — 107 subagent definitions, invocable by name via the Agent tool.
- `ib-kit/prompts/` — 505 prompts across 12 libraries.
- `ib-kit/workflows/` — 26 gated, phased procedures.
- `ib-kit/systems/` — 3 standing operating models.
- `index.html` — an unrelated pre-existing page; leave it alone.

## Working standard for any analysis in this repository

These apply to anything produced here, and are stated in every agent and skill:

- Every figure carries a source and a retrieval date. Vendor estimates are labelled as estimates.
- State what could not be verified. Never close a gap with a plausible-looking number.
- Flag every assumption that would change the conclusion if it were wrong.
- Report the finding that weakens the case as prominently as the one that supports it.
- Label judgements as judgements.

## Editing conventions

- Skills use YAML frontmatter with `name` and `description`; techniques are numbered with `N. **Name** — method`, and most carry a `*Fails when:*` line.
- Agents use YAML frontmatter with `name` and `description`, then Mission, Inputs required, Method, Output, Non-negotiables.
- Workflows carry phases as tables with the agent per step, plus Gates, Definition of done and Common failure modes.
- The index files (`ib-kit/*/README.md`) are generated from the component files — regenerate them rather than editing counts by hand.
