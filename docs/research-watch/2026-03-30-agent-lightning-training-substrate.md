# Research Watch: Agent Lightning as an agent training substrate

- Repo: <https://github.com/microsoft/agent-lightning>

## Why this is worth watching
`microsoft/agent-lightning` is worth tracking because it is not primarily another runtime, wrapper, or orchestration UI.
It is much better understood as an **agent training substrate**.

Its core claim is strong and very clear:

> train almost any AI agent with minimal code changes.

That makes it a different category from most of the repos currently clustered around runtime, harness, or workflow discussions.

## What stands out immediately
From the README:
- “The absolute trainer to light up AI agents.”
- train **ANY** agent framework (LangChain, OpenAI Agent SDK, AutoGen, CrewAI, Microsoft Agent Framework, or even bare Python OpenAI)
- selectively optimize one or more agents in a multi-agent system
- supports RL, prompt optimization, SFT, and more
- architecture centers on traces/spans, LightningStore, algorithms, trainers, and resource updates
- emphasizes continuous improvement loops after deployment rather than one-shot static setup

This is not just orchestration.
It is optimization infrastructure.

## Why clawfit should care
clawfit has been tracking the difference between:
- base runtimes
- harness layers
- team workflow layers
- methodology signals
- static vs adaptive deployed agents

Agent Lightning matters because it provides a strong signal for a different axis:

> **agent systems that can be trained and improved systematically after they already exist.**

That connects directly to the emerging distinction between:
- static agents
- adaptive / continuously improving agents

## Preliminary interpretation
Current best reading:
- strongly relevant to **Level 5 — Research / evaluation / benchmark / autoresearch patterns**
- adjacent to a future category like:
  - **agent training substrate**
  - **optimization infrastructure for deployed agents**
  - **post-runtime improvement layer**

This is not best understood as a primary runtime.
It is a layer that improves runtimes and agent systems.

## Why it is structurally important
Agent Lightning suggests the ecosystem may split into another important distinction:

1. **agent creation / deployment layers**
2. **agent improvement / training layers**

That is significant because many discussions still stop at:
- how to run agents
- how to orchestrate them
- how to extend them

Agent Lightning pushes the next question:
- how do you **systematically train and optimize** them?

## Relationship to other clawfit signals
This connects strongly to:
- online-learning agent signals
- feedback-loop methodologies
- evaluation and reward infrastructure
- adaptive agent system design

It also complements the harness/orchestration discussion by adding a different concern:
- harnesses help agents operate
- training substrates help agents improve

## Status
- Added as a research watch subject
- Strong candidate for future promotion into the main map under a clearer “agent training / optimization substrate” subtype
