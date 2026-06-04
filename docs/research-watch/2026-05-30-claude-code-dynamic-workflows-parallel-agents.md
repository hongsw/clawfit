# Research Watch: Claude Code Dynamic Workflows

- Repo/Link: https://claude.com/blog/introducing-dynamic-workflows-in-claude-code
- Source: GeekNews front page; Hacker News

## Why this is worth watching
Anthropic shipped a first-party, vendor-native mechanism for orchestrating tens to hundreds of parallel subagents inside a single Claude Code session — without requiring a third-party harness or user-authored orchestration script. This is a direct vertical integration into territory currently occupied by Level 2 harnesses (deepagents, ECC, multica, openai-agents-python). Because it activates from within Claude Code itself, it collapses the harness layer and the base runtime into a single product surface.

## What stands out immediately
- Activation via `ultracode` setting (sets effort to `xhigh`, auto-triggers workflow when appropriate) or explicit user request — no external setup
- Claude generates the orchestration script dynamically at runtime; users do not write fan-out logic themselves
- Parallel subagent results are independently verified before being merged — convergence is the termination criterion, not a fixed step count
- Some subagents are explicitly tasked with refuting the findings of others (adversarial verification pattern)
- Progress saves automatically; interrupted jobs resume rather than restart from scratch — resumability is stated as a feature, not a side effect
- Token consumption is materially higher; a confirmation gate fires before the first workflow launch
- Available on Max, Team, Enterprise plans; CLI, Desktop, VS Code extension, Bedrock, Vertex AI, Microsoft Foundry
- Stated use cases: codebase-wide bug hunts, security audits, large migrations across thousands of files

## Why clawfit should care
This signal puts pressure on the Level 2 layer from above. Orgs that previously needed a third-party harness (ECC, deepagents, multica) to run parallel agents can now do so through a first-party toggle inside Claude Code. For clawfit's recommendation engine, the relevant implication is that `agent: claude-code` with `statefulness: session` or `statefulness: persistent` and `task: code-gen` or `task: security-testing` or `task: qa` may now implicitly include multi-agent fan-out without a separate harness recommendation. The resumability feature directly maps to the `statefulness` filter — this is the first native, first-party answer to long-running, interruptible agent sessions at the vendor layer. clawfit currently has no registry field for `orchestration_mode: dynamic-parallel` vs. `single-agent`; this gap may need to surface as a scoring dimension.

## Preliminary interpretation
Current best reading:
- **Level 2 — Meta wrapper / harness / orchestration layer** (first-party, vendor-native, dynamically generated fan-out)
- **Level 3 secondary** — independent verification before delivery functions as a governance gate; adversarial subagents checking convergence is a behavioral constraint on the workflow, not just orchestration

The L2/L3 dual-layer reading mirrors the ECC pattern (harness + embedded governance), but here both layers are controlled entirely by Anthropic rather than a third-party distribution.

## Status
- High signal — first-party vendor entry that competes structurally with the Level 2 harness layer; assess whether `orchestration_mode` warrants addition to registry schema
- Monitor: does this cannibalize recommendation slots for ECC, deepagents, multica in `governance_need: medium` + `task: code-gen` profiles?
