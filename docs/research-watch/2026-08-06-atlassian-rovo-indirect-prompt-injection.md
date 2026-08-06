# Research Watch: Atlassian Rovo Indirect Prompt Injection

- Repo/Link: https://www.promptarmor.com/resources/atlassian-rovo-exfiltrates-data
- Source: Hacker News (155 pts, 2026-08-06)

## Why this is worth watching
PromptArmor disclosed a zero-click indirect prompt injection vulnerability in Atlassian Rovo that bypasses organization-level web search controls, exfiltrating any data the agent can access via Atlassian connectors (Jira tickets, Confluence docs, and beyond). The attack succeeds without requiring any human-in-the-loop approval and exploits Rovo's URL retrieval tool even when web search has been disabled organization-wide. Atlassian was notified May 23, 2026. A separate one-click variant via a crafted `rovoChatPrompt` URL parameter was also found and remediated server-side.

## What stands out immediately
- Zero-click attack: no user action required for data exfiltration
- Bypasses org-level web search disable — the control doesn't protect against this attack vector
- Scope: any data accessible via Rovo's connectors (Jira, Confluence, potentially more)
- Two distinct vulnerability classes: indirect prompt injection + one-click URL injection
- Bugcrowd disclosure confirms the one-click variant was officially acknowledged
- Enterprise AI agents with connector access are a systematic prompt injection target

## Why clawfit should care
This is the first documented zero-click data exfiltration via prompt injection in a major enterprise AI agent product in the corpus. It validates the threat model behind Strix (2026-04-12), claw-patrol (2026-06-01), and uber/ADR (2026-08-04) — all of which were defensive tools without a documented real-world enterprise breach to point to. Clawfit's governance scoring should weight `governance_need: hard` more heavily against tools with broad connector access and no sandboxed execution model. The pattern (agent with external data access + URL retrieval = exfiltration vector) is not Rovo-specific.

## Preliminary interpretation
Current best reading:
- **Level 3 — Governance / Security** (vulnerability signal, not a tool)
- Corroborating signal for the gatekeeper-mediated capability security pattern first identified in cloudflare/cloudflare-os (2026-08-05)

## Status
- Ecosystem security signal, not a trackable tool.
- Atlassian patched the one-click URL variant; indirect injection via URL retrieval tool remains an architectural concern.
- Cross-reference: banking-agent-prompt-injection (2026-06-11), uber/ADR (2026-08-04), prismata (2026-07-11)
