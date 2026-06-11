# Research Watch: €0.01 Bank Transfer Agent Attack — Prompt Injection via Transaction Data

- Repo/Link: https://blue41.com/a-0-01-bank-transfer-could-compromise-a-banking-ai-agent
- Source: Hacker News (#30, 159 pts)

## Why this is worth watching
Security researchers demonstrated that a €0.01 bank transfer with a malicious memo field can inject prompt instructions into a banking AI agent via structured financial transaction data. This is a concrete indirect prompt injection at a financial services domain boundary: the attack surface is data the agent is already authorized to read.

## What stands out immediately
- Attack vector: transaction reference/memo field — legitimate structured data the agent processes
- No authentication bypass required; attacker controls only one field in a record the agent reads
- Injection cost: €0.01 per attempt — essentially zero barrier
- Target: any banking/fintech AI agent with transaction read access
- Demonstrates that structured financial data (not just web scraping or email) is a prompt injection surface

## Why clawfit should care
Fifth signal in the agent security cluster: Shannon (L1 pentester), Strix (L1 CI security testing), Claw Patrol (L3 firewall), HexStrike AI (L4 tool bridge), and now this attack demonstration. Unlike the others, this is an *attack proof-of-concept*, not a defensive tool. It motivates the `governance_need: hard` + `data_sensitivity: confidential` scoring path for agents that process structured external data. Also advances the case for a `data_input_trust` schema axis: agents that consume untrusted structured records (financial transactions, email, scraped content) need different governance classification than interactive chat agents.

## Preliminary interpretation
Current best reading:
- **Security research signal** — no deployable tool; not a registry candidate
- Motivates **L3 governance layer** enhancements: `data_input_trust: [user, structured-internal, structured-external, untrusted-web]`
- Relevant reference for: Claw Patrol (L3 agent firewall), `governance_need` scoring dimension

## Status
- No map mutation; no registry candidate
- Agent security cluster advances to 5 signals across 3 architectural levels (L1/L3/L4)
- Schema motivation recorded: `data_input_trust` field deferred — requires schema-analyst endorsement
