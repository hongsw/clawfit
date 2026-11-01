# Research Watch: AiSOC — AI-Native Security Operations Center with LLM Triage and MCP Server

- Repo: https://github.com/beenuar/AiSOC (⭐6,036)
- Source: GitHub Trending Python (daily, 2026-11-01)

## Why this is worth watching

AiSOC is a self-hostable Security Operations Center where alert triage is performed by LLM agents rather than analysts running manual queries. It ships an MCP server alongside the core platform, so Claude, Cursor, and Continue can be used as the human-facing interface for interactive investigation. The project is currently v21.0.0 with 1,783 commits — the version number suggests rapid iteration from a much earlier start, not a fresh experiment.

The combination is unusual: most AI-augmented security tools either wrap an existing SIEM with an LLM chat interface or build a standalone agent pipeline. AiSOC integrates detection rule execution, multi-agent investigation, and human-approval playbooks into one open-source stack. The "earned executability" policy — a rule only counts as runnable after a vendor-shaped event actually fires it in replay — is an honesty mechanism that constrains false-confidence from rule flags.

## What stands out immediately

- **LLM agents do not write SQL**: agents call typed tools for lake queries, graph lookups, and enrichment; the restriction prevents SQL injection and confines agent scope to an approved API surface
- **MCP server integration**: exposes SOC capabilities to Claude, Cursor, and Continue; users can drive incident investigation directly from their coding environment or a Claude client
- **87 data connectors**: Splunk, Sentinel, Elastic, CrowdStrike, Okta, CloudTrail, GCP, and Azure; normalizes events before agents process them
- **MITRE ATT&CK investigation**: agents can traverse the ATT&CK matrix to contextualize alerts, though the README gives no detail on how ATT&CK lookups are called
- **Earned executability**: a detection rule becomes "executable" only after a replayed event fires it — prevents the false-executable status that comes from flags or directory listings alone
- **Investigation Ledger**: every agent step is recorded; investigations can be exported as signed evidence bundles — important for legal hold and compliance workflows
- **Human-gated response**: playbooks preview by default, approval steps are durable, and response defaults are all off
- **Local model support**: runs via Ollama with no external API keys; air-gapped SOC deployments are possible
- **Honest self-labeling**: the README explicitly marks synthetic data, unmeasured results, and self-consistency benchmarks — an unusual level of epistemic honesty for a security product README

## Why clawfit should care

AiSOC is the first signal for "AI-native SOC platform with MCP layer" in the tracker. Prior security-adjacent signals covered: red-teaming agents (Metatron 2026-09-06, pentagi 2026-10-15), security audit skills (Cloudflare security audit skill 2026-09-17), agent security scanning (Tencent AI Infra Guard 2026-08-20), and supply chain attacks on agent distribution channels (rubyhack/ZCode/phorion cluster). AiSOC is a defensive operations tool, not a test tool or a skills pack — a distinct category.

For clawfit scoring, AiSOC's structure suggests two registry implications:
1. The MCP server makes it a capability-layer tool (L4) even though its primary value is operational (L5). Tools with "MCP server + observability + agent pipeline" in one package may need a multi-layer registry flag.
2. The `statefulness: persistent` requirement is strong: investigations span multiple agent turns, evidence bundles are durable, and playbook approvals can wait across restarts. Current registry entries with `statefulness: session` would be insufficient for SOC investigation workflows.

## Preliminary interpretation

Current best reading:
- **Level 5 — Memory / Observability / Evaluation** (primary): LLM-agent triage, investigation ledger, and earned executability are observability and evaluation primitives for security workflows
- **Level 4 — Capabilities / Skills / MCP** (secondary): the MCP server integrates the SOC into external agent harnesses, making SOC investigation a callable capability

## Claims to verify

- Whether the LLM agents genuinely use typed tools rather than generating queries — the claim is architectural but the code would confirm it
- Whether the Investigation Ledger uses a cryptographic signature scheme or calls itself "signed" informally
- Whether "87 data connectors" are maintained integrations or community-contributed stubs with varying quality
- Creation date of the repository — v21.0.0 with 1,783 commits implies a long active history, but the start date is not stated

## Status

- New signal; not previously tracked
- Registry eligibility: at 6,036 stars, above the 5k threshold; however, AiSOC is a domain-specific operational platform rather than a general-purpose agent, LLM, or hardware entry; no registry addition at this time
- Watch for: whether the MCP server pattern (SOC investigation as a callable tool) spreads to other security platforms — would be a two-signal candidate for "domain operations as MCP-callable capability"
