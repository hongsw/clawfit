# Research Watch: Docker Agent

- Repo/Link: https://github.com/docker/docker-agent
- Source: Hacker News

## Why this is worth watching
Docker has shipped a declarative YAML-based agent runtime as a Docker CLI plugin, giving it first-class integration with the Docker container ecosystem. Shipping as a CLI plugin (now bundled in Docker Desktop) means it reaches the ~50M Docker users without a separate install step. The rapid release cadence (v1.90 → v1.131 in three months) signals active investment.

## What stands out immediately
- Declarative YAML config: agents, tools, and orchestration defined in files, not code
- Native MCP support: any local, remote, or Docker-based MCP server works as a tool
- Multi-agent orchestration built in: agent teams, handoffs, and routing from config
- Pluggable retrieval: BM25, embedding, hybrid search, reranking for RAG
- Runs on OpenAI, Anthropic, Gemini, AWS Bedrock, Mistral, xAI, Docker Model Runner, and more
- Agents are shareable as packages (like Docker images, but for agents)

## Why clawfit should care
Docker is L1 infrastructure (base runtime + execution environment). This collapses the Docker execution layer and the agent runtime into one product, meaning orgs that already standardize on Docker can adopt an agent harness at near-zero friction. This is a new hardware/deployment axis: **containerized agent** as a deployment target, separate from cloud-API or local. Clawfit's hardware registry may need a `docker-agent` environment type.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base Agent Runtime** (primary): runs and schedules agents as containers
- **Level 2 — Harness/Wrapper** (secondary): multi-agent orchestration, tool wiring, RAG

## Status
- Tracking: active development, bundled with Docker Desktop, ~2.9k stars on GitHub
