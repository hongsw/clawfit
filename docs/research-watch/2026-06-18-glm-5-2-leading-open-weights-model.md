# Research Watch: GLM-5.2 — New Leading Open-Weights Model

- Repo/Link: https://artificialanalysis.ai/articles/glm-5-2-is-the-new-leading-open-weights-model-on-the-artificial-analysis-intelligence-index
- Source: Hacker News front page (760 points)

## Why this is worth watching
GLM-5.2 (ZhipuAI / z.ai) tops the Artificial Analysis Intelligence Index with a score of 51, surpassing both MiniMax-M3 (44) and DeepSeek V4 Pro (44). Its GDPval-AA v2 score of 1,524 is competitive with proprietary GPT-5.5 (1,514). This is a meaningful successor to GLM-5.1 (tracked 2026-04-08) and arrives with a 1M-token context window under MIT license.

## What stands out immediately
- 744B total parameters, 40B active — MoE architecture
- 1M token context window (5× GLM-5.1's 200K)
- MIT licensed; pricing at $1.4 / 1M input tokens, $4.4 / 1M output tokens
- HLE score 40% (+12 pts), CritPt 21% (+16 pts) vs GLM-5.1
- High reasoning token usage: ~37k reasoning tokens per task (cost-inefficient for short tasks)

## Why clawfit should care
The GLM-5 family's long-horizon framing aligns with clawfit's `task: research` + `frequency: daily` profile. GLM-5.2's 1M context window makes it viable for full-codebase research tasks where Claude Sonnet and GPT-4o hit limits. The MIT license opens deployment options not available for proprietary models. However, the $4.4/M output token pricing and high reasoning token consumption push it outside the `monthly_budget: low` tier. Worth adding to `clawfit/registry/llms.json` as an alternative LLM for research-heavy profiles.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base LLM (long-horizon, open-weights, APAC-origin, MIT license)**

## Status
- Update to GLM-5.1 signal (2026-04-08). GLM-5.2 is now best-in-class open weights. Recommend adding to llms.json for research profile coverage.
