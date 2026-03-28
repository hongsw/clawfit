# Research Watch: llmfit as a fit-navigator pattern

- Repo: <https://github.com/AlexsJones/llmfit>

## Why this is worth watching
`llmfit` is worth tracking because it is not just a model directory or benchmark browser.
It is a **fit navigator**:

> a tool that helps users determine what is actually suitable for their hardware and use case.

That makes it highly relevant to the long-term direction of `clawfit`.

## What stands out immediately
From the README and product framing:
- "Hundreds of models & providers. One command to find what runs on your hardware."
- hardware-aware fit scoring
- quality / speed / fit / context dimensions
- interactive **TUI by default**
- classic CLI mode also available
- web dashboard auto-start option
- support for multiple providers and runtimes
- explicit plan mode for estimating what hardware a model would require

This is not merely a data browser.
It is a recommendation interface grounded in operational constraints.

## Why this matters for clawfit
This is especially important because it resembles a possible end-state for clawfit itself.

The broader `clawfit` vision is not only:
- mapping the ecosystem,
- tracking layers,
- watching research,

but eventually helping users answer questions like:
- which agent/runtime fits my device?
- which stack fits my purpose?
- which setup fits my organization or team maturity?
- which choice is right for my context, not in the abstract?

In that sense, `llmfit` is a very useful reference pattern.

## Key design lesson
`llmfit` suggests that a strong terminal tool can succeed by combining:
- detection of the current environment
- a normalized comparison model
- practical recommendation logic
- an interactive TUI that feels exploratory rather than rigid

That is valuable because `clawfit` may need a similar final form, except applied more broadly to:
- agents
- harnesses
- workflows
- devices
- purposes
- organizational contexts

## Preliminary interpretation
Current best reading:
- not primarily a direct competitor in the same domain,
- but a **design reference** for how recommendation + fit analysis + TUI can work.

This makes it useful as both:
- a research watch subject,
- and a product-shape reference.

## Why this is structurally important
The important pattern here is not only “model fit.”
It is:

> **context-aware recommendation through a native terminal experience.**

That pattern could be generalized beyond models into a broader agent/harness/workflow navigator.

## Suggested future relevance for clawfit
Potential future inspiration points:
- TUI-first exploration flow
- filter/search/sort/compare affordances
- plan mode / reverse recommendation mode
- fit scoring based on real constraints
- recommendation engine that is not purely static documentation

## Status
- Added as a research watch subject
- Strong design-reference candidate for clawfit's future CLI/TUI product direction
