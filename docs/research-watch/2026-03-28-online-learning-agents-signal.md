# Research Watch: online-learning agents / deployed adaptation signal

## Source
- Title: **almost no agent in production is dynamic.**
- Author: **Pratik Bhavsar**
- Source URL: <https://www.linkedin.com/posts/bhavsarpratik_almost-no-agent-in-production-is-dynamic-share-7443292210860593153-2I80>

## Why this is worth watching
This is a strong trend signal because it highlights a practical weakness in most deployed agent systems:

> they are trained once, deployed, and then remain largely static.

That means when tasks shift, users change, or new failure modes emerge, the deployed agent often does not improve in place.

The post is useful because it frames the next step clearly:
- not just better agent design,
- but **agents that improve while deployed**.

## Core idea in the post
The post describes a two-speed learning structure:

### Fast path
- task failure happens
- an LLM evolver inspects the trajectory
- synthesizes a reusable skill
- the next request benefits immediately

### Slow path
- idle windows are used for larger learning loops
- LoRA fine-tuning + RL with process reward models
- adaptation becomes broader generalization

It also highlights an important systems detail:
- **skill versioning / stale trajectory flushing**

This suggests that online-improving agents are not just a model problem.
They are also a data/versioning/replay-buffer problem.

## Why this matters for clawfit
clawfit has already been tracking:
- harnesses
- team workflow layers
- methodology signals
- research/eval patterns

This new signal suggests another important question:

> are agents static artifacts, or improving systems? 

That distinction may become a major ecosystem split.

## What trend this points to
This looks like an early signal of a future category around:
- self-improving deployed agents
- online learning for agents
- runtime skill evolution
- failure-driven adaptation loops
- continuous agent training in production

## Why this is structurally important
If this trend matures, the ecosystem may need to distinguish between:

1. **static agent systems**
   - deployed once
   - manually updated
   - no meaningful online adaptation

2. **adaptive agent systems**
   - evolve skills from failures
   - improve during production use
   - maintain learning loops and version discipline

That is bigger than a feature difference.
It changes how we think about maintenance, evaluation, and system architecture.

## Suggested clawfit implications
This signal may later connect to:
- Level 5 — research / evaluation / autoresearch patterns
- methodology signals around feedback-loop design
- future taxonomy around static vs adaptive deployed agents

## Status
- Added as a research watch subject
- Useful as a trend signal for runtime adaptation and online-improving agents
