# Research Watch: Codex Sub-Agent Prompt Encryption — Audit Trail vs. Confidentiality Tension

- Repo/Link: https://github.com/openai/codex/issues/28058
- Source: GeekNews (2026-07-16)

## Why this is worth watching
OpenAI's Codex MultiAgentV2 now encrypts inter-agent message payloads, making child-agent task assignments opaque to human operators reviewing audit logs. The community response articulates a design tension that will recur across all multi-agent systems: agent-to-agent confidentiality (preventing prompt injection via eavesdropping) directly conflicts with human oversight (compliance, debugging, accountability). This is the first concrete deployment-scale instance of the oversight tradeoff in a widely-used agent system.

## What stands out immediately
- `spawn_agent`, `send_message`, `followup_task` tool calls now store only ciphertext
- Plaintext `content` field is empty post-encryption — no audit trail for operators
- Proposed fix: maintain plaintext locally for admin review while delivering encrypted payload to recipient agent
- Directly affects compliance-grade deployments where audit trails are required
- Mirrors the "Own the Outer Loop" principle: encryption removes the human operator from the outer loop

## Why clawfit should care
This is a direct empirical signal for clawfit's `governance_need` scoring axis. Tools that encrypt inter-agent communications without preserving operator-accessible audit logs should score **lower** for `governance_need: hard` profiles (enterprise, regulated industries) — regardless of their security posture on other axes. The fix proposed in the issue (local plaintext audit copy) aligns with `hooks_enforcement: enforcing` — a separate enforcement layer that preserves human visibility. clawfit should add `audit_trail: [none | partial | full | encrypted-only]` to track this property.

## Preliminary interpretation
Current best reading:
- **Ecosystem signal** — governance/security design constraint surfacing at deployment scale
- Adjacent to L5 (evaluation/oversight layer): agent-to-agent auditability as an evaluation concern

## Status
- Tracking as governance signal; no registry entry change
- Schema watch: `audit_trail: [none | partial | full | encrypted-only]`; `inter_agent_confidentiality: [plaintext | encrypted | encrypted-with-local-copy]`
