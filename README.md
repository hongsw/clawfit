# clawfit

AI agent + LLM + hardware recommendation engine.

Given a task description and constraints (latency, budget, network, statefulness),
clawfit recommends the best agent pattern, LLM, and hardware combination.

## Install

```bash
pip install -e .
```

## CLI Usage

### Get a recommendation

```bash
clawfit recommend --task qa --latency low --budget 0.01
```

With all options:

```bash
clawfit recommend \
  --task code-gen \
  --latency medium \
  --budget 0.01 \
  --hardware cloud \
  --network online \
  --statefulness session \
  --top 5
```

### List registry entries

```bash
clawfit list agents
clawfit list llms
clawfit list hardware
```

### Show registry summary

```bash
clawfit profile
```

## Output

`recommend` returns JSON:

```json
[
  {
    "agent": "react-agent",
    "llm": "claude-sonnet",
    "hardware": "aws-cpu-medium",
    "architecture": "cloud-api",
    "fit_score": 0.85,
    "why": ["ReAct Agent supports 'qa' with medium latency", ...],
    "risk": ["High per-token cost — monitor usage"]
  }
]
```

## Python API

```python
from clawfit.recommend import recommend

results = recommend(task="research", latency="high", network="online")
```

## Tasks

Supported task categories: `classification`, `code-gen`, `data-analysis`, `qa`, `research`, `summarization`.

## Architecture

1. **Registry** — JSON files define available agents, LLMs, and hardware.
2. **Filters** — Hard constraints eliminate incompatible options.
3. **Scoring** — Remaining candidates are scored on latency fit, cost, and preference alignment.
4. **Recommendation** — Top-N results returned with architecture label, rationale, and risks.

## Ecosystem research

clawfit is evolving beyond a simple recommender into a comparison and evidence hub for AI coding tools.

Reference classification document:
- `docs/reference-levels.md`

Initial structured registry:
- `data/tools_registry.json`

Initial feature verification dataset:
- `data/feature_matrix.json`
- `data/feature_matrix.schema.json`

### Reference levels overview

| Level | Focus | Representative tools |
|---|---|---|
| 1 | Core comparison targets | <a href="https://github.com/openclaw/openclaw"><img src="https://github.com/openclaw.png" alt="OpenClaw" width="20" /></a> <a href="https://github.com/openclaw/openclaw">OpenClaw</a>, <a href="https://github.com/zeroclaw-labs/zeroclaw"><img src="https://github.com/zeroclaw-labs.png" alt="ZeroClaw" width="20" /></a> <a href="https://github.com/zeroclaw-labs/zeroclaw">ZeroClaw</a>, <a href="https://github.com/anthropics/claude-code"><img src="https://github.com/anthropics.png" alt="Claude Code" width="20" /></a> <a href="https://github.com/anthropics/claude-code">Claude Code</a>, <a href="https://github.com/anomalyco/opencode"><img src="https://github.com/anomalyco.png" alt="OpenCode" width="20" /></a> <a href="https://github.com/anomalyco/opencode">OpenCode</a>, <a href="https://github.com/block/goose"><img src="https://github.com/block.png" alt="Goose" width="20" /></a> <a href="https://github.com/block/goose">Goose</a>, <a href="https://github.com/charmbracelet/crush"><img src="https://github.com/charmbracelet.png" alt="Crush" width="20" /></a> <a href="https://github.com/charmbracelet/crush">Crush</a>, <a href="https://github.com/paul-gauthier/aider"><img src="https://github.com/paul-gauthier.png" alt="Aider" width="20" /></a> <a href="https://github.com/paul-gauthier/aider">Aider</a>, <a href="https://github.com/All-Hands-AI/OpenHands"><img src="https://github.com/All-Hands-AI.png" alt="OpenHands" width="20" /></a> <a href="https://github.com/All-Hands-AI/OpenHands">OpenHands</a>, <a href="https://github.com/cline/cline"><img src="https://github.com/cline.png" alt="Cline" width="20" /></a> <a href="https://github.com/cline/cline">Cline</a>, <a href="https://github.com/continuedev/continue"><img src="https://github.com/continuedev.png" alt="Continue" width="20" /></a> <a href="https://github.com/continuedev/continue">Continue</a>, <a href="https://cursor.com/"><img src="https://www.google.com/s2/favicons?domain=cursor.com&sz=64" alt="Cursor" width="20" /></a> <a href="https://cursor.com/">Cursor</a>, <a href="https://superwhisper.com/"><img src="https://www.google.com/s2/favicons?domain=superwhisper.com&sz=64" alt="Superwhisper" width="20" /></a> <a href="https://superwhisper.com/">Superwhisper</a> |
| 2 | Workflow wrappers and orchestration tools | <a href="https://github.com/code-yeongyu/oh-my-openagent"><img src="https://github.com/code-yeongyu.png" alt="oh-my-openagent" width="20" /></a> <a href="https://github.com/code-yeongyu/oh-my-openagent">oh-my-openagent</a>, <a href="https://github.com/Yeachan-Heo/oh-my-claudecode"><img src="https://github.com/Yeachan-Heo.png" alt="oh-my-claudecode" width="20" /></a> <a href="https://github.com/Yeachan-Heo/oh-my-claudecode">oh-my-claudecode</a>, <a href="https://github.com/AndyMik90/Aperant"><img src="https://github.com/AndyMik90.png" alt="Aperant" width="20" /></a> <a href="https://github.com/AndyMik90/Aperant">Aperant</a>, <a href="https://github.com/frankbria/ralph-claude-code"><img src="https://github.com/frankbria.png" alt="ralph-claude-code" width="20" /></a> <a href="https://github.com/frankbria/ralph-claude-code">ralph-claude-code</a>, <a href="https://github.com/Th0rgal/open-ralph-wiggum"><img src="https://github.com/Th0rgal.png" alt="open-ralph-wiggum" width="20" /></a> <a href="https://github.com/Th0rgal/open-ralph-wiggum">open-ralph-wiggum</a>, <a href="https://github.com/SuperClaude-Org/SuperClaude_Framework"><img src="https://github.com/SuperClaude-Org.png" alt="SuperClaude Framework" width="20" /></a> <a href="https://github.com/SuperClaude-Org/SuperClaude_Framework">SuperClaude Framework</a>, <a href="https://github.com/siteboon/claudecodeui"><img src="https://github.com/siteboon.png" alt="claudecodeui" width="20" /></a> <a href="https://github.com/siteboon/claudecodeui">claudecodeui</a>, <a href="https://github.com/coder/agentapi"><img src="https://github.com/coder.png" alt="agentapi" width="20" /></a> <a href="https://github.com/coder/agentapi">agentapi</a> |
| 3 | Architecture and benchmark references | <a href="https://github.com/mozilla-ai/any-agent"><img src="https://github.com/mozilla-ai.png" alt="any-agent" width="20" /></a> <a href="https://github.com/mozilla-ai/any-agent">any-agent</a>, <a href="https://github.com/mozilla-ai/any-llm"><img src="https://github.com/mozilla-ai.png" alt="any-llm" width="20" /></a> <a href="https://github.com/mozilla-ai/any-llm">any-llm</a>, <a href="https://github.com/anomalyco/opencode-bench"><img src="https://github.com/anomalyco.png" alt="opencode-bench" width="20" /></a> <a href="https://github.com/anomalyco/opencode-bench">opencode-bench</a>, <a href="https://github.com/EleutherAI/lm-evaluation-harness"><img src="https://github.com/EleutherAI.png" alt="lm-evaluation-harness" width="20" /></a> <a href="https://github.com/EleutherAI/lm-evaluation-harness">lm-evaluation-harness</a>, <a href="https://github.com/prometheus-eval/prometheus"><img src="https://github.com/prometheus-eval.png" alt="Prometheus" width="20" /></a> <a href="https://github.com/prometheus-eval/prometheus">Prometheus</a>, <a href="https://github.com/Hugging-Face-KREW/Ko-AgentBench"><img src="https://github.com/Hugging-Face-KREW.png" alt="Ko-AgentBench" width="20" /></a> <a href="https://github.com/Hugging-Face-KREW/Ko-AgentBench">Ko-AgentBench</a>, <a href="https://github.com/microsoft/agent-lightning"><img src="https://github.com/microsoft.png" alt="agent-lightning" width="20" /></a> <a href="https://github.com/microsoft/agent-lightning">agent-lightning</a>, <a href="https://github.com/team-attention/hoyeon"><img src="https://github.com/team-attention.png" alt="hoyeon" width="20" /></a> <a href="https://github.com/team-attention/hoyeon">hoyeon</a> |
| 4 | Memory, context, MCP, and plugin ecosystem | <a href="https://github.com/CaviraOSS/OpenMemory"><img src="https://github.com/CaviraOSS.png" alt="OpenMemory" width="20" /></a> <a href="https://github.com/CaviraOSS/OpenMemory">OpenMemory</a>, <a href="https://github.com/campfirein/cipher"><img src="https://github.com/campfirein.png" alt="cipher" width="20" /></a> <a href="https://github.com/campfirein/cipher">cipher</a>, <a href="https://github.com/zilliztech/claude-context"><img src="https://github.com/zilliztech.png" alt="claude-context" width="20" /></a> <a href="https://github.com/zilliztech/claude-context">claude-context</a>, <a href="https://github.com/oraios/serena"><img src="https://github.com/oraios.png" alt="serena" width="20" /></a> <a href="https://github.com/oraios/serena">serena</a>, <a href="https://github.com/anthropics/claude-plugins-official"><img src="https://github.com/anthropics.png" alt="claude-plugins-official" width="20" /></a> <a href="https://github.com/anthropics/claude-plugins-official">claude-plugins-official</a>, <a href="https://github.com/team-attention/plugins-for-claude-natives"><img src="https://github.com/team-attention.png" alt="plugins-for-claude-natives" width="20" /></a> <a href="https://github.com/team-attention/plugins-for-claude-natives">plugins-for-claude-natives</a>, <a href="https://github.com/microsoft/mcp-for-beginners"><img src="https://github.com/microsoft.png" alt="mcp-for-beginners" width="20" /></a> <a href="https://github.com/microsoft/mcp-for-beginners">mcp-for-beginners</a>, <a href="https://github.com/IBM/mcp-context-forge"><img src="https://github.com/IBM.png" alt="mcp-context-forge" width="20" /></a> <a href="https://github.com/IBM/mcp-context-forge">mcp-context-forge</a> |
| 5 | Data hub, RAG, and evidence infrastructure | <a href="https://github.com/HKUDS/LightRAG"><img src="https://github.com/HKUDS.png" alt="LightRAG" width="20" /></a> <a href="https://github.com/HKUDS/LightRAG">LightRAG</a>, <a href="https://github.com/HKUDS/RAG-Anything"><img src="https://github.com/HKUDS.png" alt="RAG-Anything" width="20" /></a> <a href="https://github.com/HKUDS/RAG-Anything">RAG-Anything</a>, <a href="https://github.com/airweave-ai/airweave"><img src="https://github.com/airweave-ai.png" alt="airweave" width="20" /></a> <a href="https://github.com/airweave-ai/airweave">airweave</a>, <a href="https://github.com/agentset-ai/agentset"><img src="https://github.com/agentset-ai.png" alt="agentset" width="20" /></a> <a href="https://github.com/agentset-ai/agentset">agentset</a>, <a href="https://github.com/VectifyAI/PageIndex"><img src="https://github.com/VectifyAI.png" alt="PageIndex" width="20" /></a> <a href="https://github.com/VectifyAI/PageIndex">PageIndex</a>, <a href="https://github.com/opendatalab/MinerU"><img src="https://github.com/opendatalab.png" alt="MinerU" width="20" /></a> <a href="https://github.com/opendatalab/MinerU">MinerU</a> |
| 6 | Productivity, input, and human-agent interface tools | <a href="https://superwhisper.com/"><img src="https://www.google.com/s2/favicons?domain=superwhisper.com&sz=64" alt="Superwhisper" width="20" /></a> <a href="https://superwhisper.com/">Superwhisper</a>, <a href="https://github.com/channprj/claude-code-voice"><img src="https://github.com/channprj.png" alt="claude-code-voice" width="20" /></a> <a href="https://github.com/channprj/claude-code-voice">claude-code-voice</a>, <a href="https://github.com/hada0127/cc-telegram"><img src="https://github.com/hada0127.png" alt="cc-telegram" width="20" /></a> <a href="https://github.com/hada0127/cc-telegram">cc-telegram</a>, <a href="https://github.com/Q00/ouroboros"><img src="https://github.com/Q00.png" alt="ouroboros" width="20" /></a> <a href="https://github.com/Q00/ouroboros">ouroboros</a>, <a href="https://github.com/openclaw/openclaw/pull/53553#issuecomment-4124082023"><img src="https://github.com/openclaw.png" alt="OpenClaw talkmode" width="20" /></a> <a href="https://github.com/openclaw/openclaw/pull/53553#issuecomment-4124082023">OpenClaw talkmode improvement</a> |

**상세보기:** [docs/reference-levels.md](https://github.com/hongsw/clawfit/blob/main/docs/reference-levels.md)

See full details in [`docs/reference-levels.md`](docs/reference-levels.md).

## Tests

```bash
python -m pytest tests/ -v
```
