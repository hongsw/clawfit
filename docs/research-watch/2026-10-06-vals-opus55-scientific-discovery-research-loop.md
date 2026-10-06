# Research Watch: Vals.ai Opus 5.5 — AI Agents in Scientific Discovery Research Loops

- Repo/Link: https://vals.ai
- Source: Hacker News front page (448 pts, 73 comments)

## Why this is worth watching
Vals.ai has published a series of experiments in which Claude Opus 5.5 agents complete substantive scientific and mathematical tasks previously requiring human domain expertise: identifying room-temperature magnetic semiconductor candidates, proving geometric optimality of a bipyramid electron placement (17,895-line Lean-verified proof), and developing a shortest-path algorithm (C-HD) with improved bounds over Dijkstra's in a specific density regime. The HN thread has 448 points, indicating broad practitioner attention. These are not benchmark scores; they are open-ended research outcomes with independent formal verification.

## What stands out immediately
- Magnetic semiconductor candidates: agents given an open-ended specification ("find a room-temperature magnet with zero net magnetism whose electrons are still sorted by spin") and identified a 1999 compound meeting the requirements — literature archaeology plus synthesis, not rote retrieval
- Mathematical proof: 17,895-line Lean proof accepted by formal verification — the output is machine-checked, not just model-claimed
- Algorithm discovery: C-HD beats published Dijkstra bounds in a specific density regime; 10 agents collaborated via message board for 15 hours
- Multi-agent collaborative research: 10 Opus 5.5 agents sharing state via a message board — an L5 research loop architecture, not a single-agent chain
- Vals.ai operates independent benchmarks (Vals Index, CyberBench, ProofBench, Terminal-Bench) — credibility above zero on independent evaluation claims
- 448 HN pts — highest community engagement of any signal in today's scan

## Why clawfit should care
This signal confirms that agent research loop architectures (L5) are now capable of producing verifiable scientific contributions, not just benchmark improvements. Clawfit's current scoring does not differentiate between agents deployed for iterative code generation vs. multi-agent research loops; the Vals experiments suggest that the `task: research` and `task: qa` dimensions may need further granularity for high-autonomy multi-day agent deployments. The multi-agent message-board architecture (10 agents, 15 hours) is also a new data point on statefulness costs: `statefulness: persistent` with inter-agent communication is now demonstrated at the scale of producing externally verifiable academic results.

## Preliminary interpretation
Current best reading:
- **L5 — Evaluation / Research Loop layer** (primary: multi-agent research loop producing formal-verification-eligible scientific outputs)
- **L3 — Team / SSOT Generator layer** (secondary: 10-agent collaborative structure with shared message state)

## Claims to verify
- Magnetic semiconductor claim — "two candidates" identified; independent domain chemist review not yet confirmed
- Lean proof — formal verification acceptance by the Lean checker is verifiable; semantic correctness of the underlying mathematical claim requires domain expert review
- C-HD algorithm — benchmark comparison against Dijkstra is in a specific density regime; does not claim general improvement
- Vals.ai's independence from Anthropic — confirm organizational separation for evaluation credibility

## Status
- New signal 2026-10-06 — not a GitHub repo (vals.ai platform); 448 HN pts; monitoring for peer-reviewed publication of the magnetic semiconductor and algorithm claims; no registry entry applicable (evaluation platform, not a deployable agent or LLM)
