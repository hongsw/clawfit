# Research Watch: Claude Code VSX Compromise — Supply Chain Backdoor in Cursor Marketplace Extension

- Repo/Link: https://phorion.io/blog/offical-claude-code-vsx-compromise/
- Source: Hacker News front page (455 points, 2026-10-30)

## Why this is worth watching

A backdoored version of the Claude Code for VS Code extension (v2.1.313) was distributed through the Cursor Marketplace. The malicious code installed a persistent reverse SSH tunnel, added an attacker-controlled SSH key to `~/.ssh/authorized_keys`, and beaconed host reconnaissance — all before the user interacted with the extension. The attack vector is the extension distribution channel, not the model, the harness runtime, or the developer's own code. Cursor removed the release and the NPM and VS Code versions were also pulled, but uninstalling the extension does not remove the installed persistence artifacts.

This is the third supply chain attack on an AI coding agent distribution channel in 6 weeks (after `rubyhack` OpenAI Agents SDK on RubyGems, 2026-09-12; and ZCode silent git history upload, 2026-09-19). The pattern is no longer anecdotal.

## What stands out immediately

- **Attack vector is the IDE marketplace, not the agent runtime**: the injected prefix in `extension.js` runs before the extension's `activate` function — no user action required beyond installation
- **Persistence survives uninstall**: macOS LaunchAgent (`com.apple.sysmond`), SSH key injection, and tunnel process all remain after extension removal; developers may not detect this via normal dependency audits
- **Reconnaissance scope**: hostname, username, OS, Git committer email, public IP, and names (not values) of environment variables matching KEY, TOKEN, SECRET — sufficient to profile high-value targets before deeper exploitation
- **Reverse tunnel to 134.209.82.225**: outbound tunnel establishment means firewall ingress rules provide no protection; only egress filtering would catch this
- **Cross-platform**: backdoor targets macOS, Linux, and Windows; macOS SSH-enable bug limits inbound access if Remote Login is off, but keys and persistence are still planted
- **Indicators of compromise are specific and actionable**: Phorion published file hashes, the Ed25519 key fingerprint, and host artifacts — the signal has immediate operational value
- **Cursor, NPM, and VS Code Marketplace all pulled the version**: three separate distribution channels were affected simultaneously, indicating coordinated or compromised upload access

## Why clawfit should care

This signal extends the `platform_trust_risk` annotation cluster from 2026-10-18 (OpenCode credential breach + Codex daemon consent + Radware MCP attack vectors) with a new attack surface: the **IDE marketplace extension channel**. The OpenCode breach was a cloud platform compromise; this is a local execution compromise delivered through a trusted extension marketplace.

For clawfit recommendation profiles:
- Agents delivered via IDE extension — rather than CLI or self-hosted — now carry a distinct supply chain risk dimension that clawfit does not currently model
- A `distribution_channel` field distinguishing CLI (self-contained binary, pinned version), NPM/pip package, and IDE marketplace extension would allow clawfit to surface this risk differential
- Self-hosted agents (Goose, Aider, Roo Code) are unaffected by this attack vector; this increases their relative advantage under `governance_need: hard` + `data_sensitivity: confidential` profiles

Third supply chain attack signal: rubyhack (2026-09-12), zcode (2026-09-19), and this incident (2026-10-30) form a three-signal cluster for "supply chain attacks on AI coding agent distribution channels." The three-signal rule is met. Candidate for a new companion axis note on agent distribution channel security, distinct from runtime governance.

## Preliminary interpretation

Current best reading:
- **Level 2 — Harness / Wrapper** (primary): the affected artifact is a coded agent harness (the VS Code extension wrapping Claude Code agent capabilities)
- **Level 3 — Governance / SSOT** (secondary): the incident directly affects the trust model for agent harness distribution and the governance question of how teams verify extension provenance

## Claims to verify

- Whether the injected code was introduced by a compromised developer credential, a CI/CD pipeline compromise, or a malicious insider at the publisher
- Whether v2.1.313 was ever distributed via channels other than Cursor Marketplace (NPM + VS Code Marketplace also affected — scope of exposure is wider than one channel)
- Whether the reverse tunnel server at 134.209.82.225 was associated with prior campaigns or is opportunistic infrastructure
- Whether any credential exfiltration occurred beyond the reconnaissance beacon (the advisory does not confirm active credential theft, only the capability)

## Status

- Tracking: new supply chain incident signal, Hacker News front page 2026-10-30
- Registry eligibility: not a candidate (security incident, not a new agent/LLM/hardware tool); the affected tool (Claude Code VS Code extension) is already tracked
- Three-signal cluster: rubyhack (2026-09-12) + zcode (2026-09-19) + this = three supply chain attacks on AI coding agent distribution channels — candidate for companion axis note on agent extension supply chain security
