# Research Watch: METATRON — AI Penetration Testing Assistant with Zero-Exfiltration Local LLM

- Repo: https://github.com/sooryathejas/METATRON (⭐~3.9k)
- Source: GitHub Trending Python (2026-09-06); cybersecuritynews.com, medevel.com coverage

## Why this is worth watching

METATRON is a CLI-based penetration testing assistant that runs entirely offline on Linux (Parrot OS primary target). It executes real reconnaissance tools — nmap, whois, whatweb, curl, dig, nikto — feeds the aggregated output to a locally-running Ollama model (`metatron-qwen`, a custom Qwen-family build with 16,384-token context), and returns vulnerability analysis, exploit suggestions, and remediation recommendations. The tool requires 8.4 GB RAM for the 9B model variant.

The architectural choice that makes this notable is the zero-exfiltration guarantee: the local LLM receives sensitive target data (internal IP ranges, open ports, banner strings, discovered credentials) that cannot be transmitted to any cloud endpoint. This is not a performance optimization — it is a compliance and operational-security requirement for red teams working under non-disclosure agreements or testing internal infrastructure that cannot touch the public internet. This positions METATRON at the intersection of two patterns now confirmed in this log: local-inference-for-compliance and domain-specialized agent harness.

Created ~April 2026 (5 months ago); MIT license.

## What stands out immediately

- **Zero-exfiltration by design**: all LLM inference runs through Ollama locally; the `metatron-qwen` custom model is specifically tuned for security reconnaissance output — target data (IPs, ports, banners, credentials) never leaves the host
- **16,384-token context window**: sized to accommodate full nmap scan output, multi-tool result aggregation, and CVE lookup context in a single inference pass
- **MariaDB backend with full scan history**: reconnaissance results are persisted across sessions; the LLM can reference historical scans for the same target when analyzing new findings
- **DuckDuckGo + CVE lookup integration**: the local LLM can request external searches for CVE details while the target's internal data remains local — a deliberate split between public research (external) and sensitive target data (local)
- **Real tool execution, not simulation**: METATRON calls the actual binaries (nmap, nikto, dig) and parses their real output; the LLM layer is an analysis layer over live reconnaissance data, not a simulated environment
- **Custom Qwen model via Ollama Modelfile**: `metatron-qwen` is defined in a Modelfile with security-domain system prompt and tuning — this establishes the pattern of domain-customized Ollama models for specialist applications

## Why clawfit should care

1. **Security domain gap in current task taxonomy**: current task categories (code-gen, qa, documentation, planning, research) do not include security assessment, vulnerability analysis, or penetration testing. METATRON confirms there is a meaningful community of security professionals deploying local AI agents for tasks with hard data-exfiltration constraints.

2. **`data_sensitivity: air-gapped` use case materially different from `data_sensitivity: confidential`**: the previous collusion.wiki signal (2026-09-04) flagged `containment_level` as a future schema dimension for multi-agent coordination. METATRON adds a different constraint: the agent must not transmit target data over any network, even encrypted. This `network: offline` requirement is not the same as `network: local` (a local LAN service) — it is a hard air-gap requirement. The current `network` filter does not express this.

3. **Custom Ollama Modelfile as a configuration pattern**: METATRON's domain customization via a Modelfile (system prompt + base model) is an L1 configuration artifact distinct from a registry agent entry. This pattern — domain-tuned local model configured via Modelfile — is the third signal in this log (after FreeToken 2026-08-31 and waste-nvme 2026-08-01) for the "local-model domain specialization" sub-type.

4. **Two-signal building pattern (same scan)**: METATRON + OpenMed (both today) are two same-day signals for compliance-justified local inference — both explicitly cite regulatory/security constraints as the design driver for local LLM deployment. See OpenMed research-watch doc for pattern note.

## Preliminary interpretation

Current best reading:
- **Level 1 — Base Runtime / Inference Layer (primary)**: METATRON's Ollama + metatron-qwen pairing is a locally-deployed inference runtime with domain-customized model; the 9B model at 8.4GB RAM maps cleanly to the `hardware: local` tier in clawfit's registry
- **Level 2 — Harness / Wrapper Layer (secondary)**: METATRON orchestrates multiple recon tools, sequences their execution, aggregates output, and routes it through the LLM — this is a domain-specific agent harness, not a base runtime

## Claims to verify

- Whether the `metatron-qwen` Modelfile is included in the public repo or requires a separate download; the base Qwen variant (7B vs. 9B vs. 14B) and exact version used
- Whether METATRON has been tested against modern anti-fingerprinting and IDS systems, or whether nmap/nikto defaults are used without evasion settings
- Whether the 3.9k stars reflect genuine security-practitioner adoption or primarily hobbyist interest — the test is whether red teams at professional firms have deployed it under NDA constraints
- Whether MariaDB as a dependency (vs. SQLite) is an intentional design choice for multi-user deployments or an implementation artifact

## Status

- ~3.9k stars, above research-watch threshold (100★); below registry threshold (5k★)
- Not eligible for current registry: no schema slot for security-domain tools; `task: pentest` not in current taxonomy; Ollama-based local inference has hardware-dependent cost, not deterministic API pricing
- First "offline security agent" signal in this research-watch log
- Watch: whether METATRON adds MCP server exposure (similar to OpenMed's pattern); whether a second tool confirms the "local LLM security agent with zero-exfiltration" pattern; whether stars grow past 5k
