# Reference Note: 15 production agent patterns

## Source
- Title: **I've taught AI Agents to 2,300+ engineers.**
- Author: **Maryam Miradi, PhD**
- Source URL: <https://www.linkedin.com/posts/maryammiradi_ive-taught-ai-agents-to-2300-engineers-share-7440079802906099712-2Qh0>

## Why this is useful
This is a strong **reference subject** because it compresses a large amount of agent-system design knowledge into a pattern list.

Even if the post is simplified for broad sharing, it is useful as:
- a quick taxonomy reference
- a talk-preparation reference
- a checklist for explaining agent design patterns to others

## Pattern structure captured in the post
The post groups 15 patterns into 3 tiers:

### Tier 1 — Single-agent patterns
1. ReAct
2. Plan-and-Execute
3. Reflection / Self-Critique
4. Tool Use / Function Calling

### Tier 2 — Multi-agent orchestration
5. Orchestrator-Subagent
6. Supervisor
7. Hierarchical Agents
8. Sequential Pipeline
9. Parallel Fan-Out / Fan-In
10. MapReduce
11. Debate / Adversarial

### Tier 3 — Iterative & feedback loop
12. Evaluator-Optimizer
13. Critic-Actor
14. Self-Healing / Retry Loop
15. HITL

## Why clawfit should care
clawfit is increasingly trying to map not just products, but the structural layers and operating patterns behind agent systems.

This reference helps because it makes explicit that:
- the **pattern is the decision**
- the implementation code is downstream of that choice

That aligns well with clawfit's broader direction:
- base runtime
- harness layer
- team workflow layer
- capability layer
- interface layer

## Suggested use
This note is useful as:
- a presentation support artifact
- a taxonomy input for future pattern mapping
- a bridge between ecosystem scanning and educational framing

## Caution
This is a helpful high-level taxonomy, but not a canonical scientific classification.
It should be treated as a practical framing tool, not final ground truth.
