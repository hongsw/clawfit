# Research Watch: Meta Muse Zero-Day — AI Agent Hijacking via Undocumented Config Endpoint

- Repo/Link: https://mouse.dev (disclosure) / https://www.malwarebytes.com/blog/bugs/2026/09/metas-muse-ai-assistant-has-a-zero-day-that-can-turn-it-into-a-mac-backdoor
- Source: Hacker News (item 1: 204 pts, 111 comments; item 2: 83 pts, 33 comments, arstechnica.com — 2026-09-22)

## Why this is worth watching
Meta Muse (already tracked 2026-09-09) had a zero-day vulnerability disclosed and hot-fixed on 2026-09-21. The core mechanism: an undocumented configuration setting (`endo_voyager_dictation_endpoint`) could be modified by any unprivileged local process, redirecting Muse's dictation traffic to an attacker-controlled server. This is the second confirmed commercial AI agent security incident this month after ZCode's silent git-history upload (2026-09-19). Two incidents in four days from different vendors confirms "commercial AI agent attack surface" is a real and active pattern, not an isolated event.

## What stands out immediately
- Vulnerability class is **configuration hijacking**, not prompt injection — the attack happens before the model sees any input, at the OS/config layer
- Unprivileged write access to the config key is the flaw — no root required, no exploit of a code vulnerability
- Once redirected, the agent's full capability surface (audio capture, connected-service auth, context window contents) becomes attacker-controlled
- Patrick Wardle (Objective-See / macOS security researcher) discovered and disclosed it; he released a proof-of-concept named "not-a-mused"
- Meta hot-fixed within hours of public disclosure — fast response, but the vulnerability existed in production
- Attack requires existing local code execution (not remote) — threat model is supply-chain compromise, malicious MCP server with local access, or parallel malware
- The `endo_voyager_dictation_endpoint` key name implies it was an internal debug/QA endpoint that was never locked down before shipping

## Why clawfit should care
This is the **second signal for "commercial AI agent with an exploitable configuration attack surface"** (ZCode 2026-09-19 was first). Two signals from two independent vendors in the same week confirm this is a structural weakness in how commercial AI agents are shipped, not a vendor-specific anomaly. Implications for clawfit:
- The `governance_need: hard` filter becomes load-bearing for commercial agent recommendations, especially desktop agents with persistent OS permissions
- `data_telemetry_disclosure` axis candidate (introduced by ZCode) now has a companion axis: `config_endpoint_exposure` — whether configuration keys that affect agent routing/behavior are accessible to unprivileged processes
- For `task: personal-assistant` + `hardware: local` + `data_sensitivity: confidential` profiles, clawfit has no filter for "agent config hardening" — this incident demonstrates the gap is real and exploitable
- Meta Muse is tracked (2026-09-09 doc) but its attack surface profile should be noted in registry governance fields when those are added

## Preliminary interpretation
- **Level 3 — SSOT / Governance layer (primary)**: config hardening failure; the attack exploits the agent's privilege-delegation model
- **Level 5 — Evaluation / Security research layer (secondary)**: Patrick Wardle's disclosure establishes a repeatable research methodology for testing commercial AI agent config surfaces

## Claims to verify
- Whether the `endo_voyager_dictation_endpoint` setting is unique to Muse or is a shared pattern in other Meta AI products
- Whether the hot-fix was a key permission enforcement or key removal
- Whether Wardle tested other commercial AI agents with the same methodology (follow-on disclosures would confirm the pattern is widespread)
- Whether this class of attack (config-layer hijacking, not prompt injection) is covered by any existing agent security benchmark

## Status
- **Second signal for "commercial AI agent configuration-layer attack surface"** (cross-date pattern: ZCode silent upload 2026-09-19 + Meta Muse config hijacking today)
- Two signals from different vendors, different attack vectors (outbound data exfiltration vs. inbound command injection), same structural root: shipping AI agents with under-hardened system-layer access
- Pattern is approaching canonical promotion threshold for a `config_hardening` or `attack_surface` axis candidate
- No registry action (Meta Muse is a service; config vulnerability does not change cost/latency data)
- Watch for: third commercial AI agent security incident that fits this pattern; Wardle follow-on disclosures on other agents
