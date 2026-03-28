# Research Watch: Harness as a meta-skill / team architect plugin

- Repo: <https://github.com/revfactory/harness>

## Why this is worth watching
`revfactory/harness` is worth tracking because it makes a stronger and more explicit claim than many wrapper-style repos.

It is not just a wrapper or workflow note.
It is a **meta-skill** that:
- designs domain-specific agent teams
- chooses orchestration patterns
- generates specialized agent definitions
- generates the skills those agents use

That makes it a very clear signal in the emerging harness layer.

## What stands out immediately
From the README:
- it is framed as **Agent Team & Skill Architect**
- packaged as a **Claude Code Plugin**
- outputs `.claude/agents/` and `.claude/skills/`
- defines a 6-phase workflow from domain analysis to validation
- includes 6 explicit architecture patterns:
  - Pipeline
  - Fan-out/Fan-in
  - Expert Pool
  - Producer-Reviewer
  - Supervisor
  - Hierarchical Delegation
- includes built-with-Harness evidence (`harness-100`) and an A/B-style effectiveness claim

This is more concrete than many vague “agent wrapper” repos.

## Why clawfit should care
clawfit has already been tracking the harness layer as a major trend.
This repo matters because it sharpens what “harness” can mean:

> not only a wrapper around a runtime,
> but a system that **architects the team itself** and generates the reusable skills that team runs on.

That makes it useful for distinguishing:
- simple wrappers
- workflow packs
- orchestration substrates
- **meta-skill / team architect systems**

## Preliminary interpretation
Current best reading:
- strongly relevant to **Level 2 — Meta wrappers / harnesses / orchestration layers**
- with overlap into **Level 3 — Team harness / executable SSOT / governance layer**

More specifically, it appears to represent a subtype like:
- **meta-skill harness generator**
- **agent-team architect plugin**

## Why it is structurally interesting
This repo suggests the harness layer is splitting into finer subcategories.
At least these are becoming visible:

1. **wrapper / enhancement layer**
2. **workflow / methodology pack**
3. **orchestration testbed**
4. **company orchestration system**
5. **meta-skill / team architect generator**

`revfactory/harness` is closest to the fifth type.

## Notable claims to revisit later
The README includes a strong effectiveness claim tied to:
- `revfactory/claude-code-harness`
- 15 software engineering tasks
- quality improvement with structured pre-configuration

This is very relevant to clawfit, but should be treated as a claim to inspect rather than immediately accepted as settled evidence.

## Status
- Added as a research watch subject
- Strong candidate for future promotion into the main reference map under a more specific harness subtype
