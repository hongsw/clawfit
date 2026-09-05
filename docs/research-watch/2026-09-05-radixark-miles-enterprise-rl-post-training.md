# Research Watch: radixark/miles — Enterprise RL Post-Training Framework at Trillion-Parameter Scale

- Repo: https://github.com/radixark/miles (⭐2,627)
- Source: GitHub Trending Python (158 stars today, 2026-09-05)

## Why this is worth watching

Miles is an enterprise-grade reinforcement learning framework for large-language and vision model post-training. It pairs SGLang (high-throughput rollout generation) with Megatron-LM (distributed training) or PyTorch FSDP2, targeting trillion-parameter models at production scale. Version 0.1 shipped in August 2026.

The significance is not that RL post-training is new — it is not. The significance is that miles is the first framework tracked by clawfit that explicitly targets production deployment (fault tolerance, asynchronous operation, RDMA weight sync) rather than research reproducibility. Prior RL training frameworks (GRPO, PPO, REINFORCE++) have been research-oriented; miles is engineered for the infrastructure teams that run them at scale.

## What stands out immediately

- **Asynchronous RL with decoupled rollout and training workers**: rollout generation and parameter updates run independently, eliminating the synchronization bottleneck that slows PPO at scale.
- **P2P RDMA weight sync**: updated weights reach inference engines in seconds via direct memory transfer — eliminates the checkpoint-and-reload cycle that adds latency between training steps.
- **Rollout Routing Replay (R3)**: maintains MoE routing consistency across rollout and training passes — addresses a correctness bug in MoE training that can produce gradient inconsistencies when routing decisions differ between forward passes.
- **Token-in-token-out (TITO)**: ensures exact token alignment across all models, preventing the subtle off-by-one errors that corrupt RL reward signals.
- **Low-precision training (MXFP8, NVFP4, FP8, INT4 QAT)**: reduces memory footprint and compute costs for trillion-parameter runs; explicitly supported rather than bolted on.
- **Fault tolerance with automatic SGLang engine recovery**: production-grade — a crashed rollout engine is restarted without aborting the training run.
- **Day-0 support for frontier models**: DeepSeek-V4, Kimi-K3, GLM-5.2, Inkling listed as supported on release.
- **Agentic environment support**: Harbor, HUD, NeMo Gym, OpenEnv listed as supported environments for agentic RL training — not just language task benchmarks.
- **AMD MI355X ROCm support in flight**: hardware-agnostic training is a stated priority, not an afterthought.

## Why clawfit should care

Miles operates in the model post-training layer (L5 in the clawfit taxonomy) — below the agent runtime but directly shaping what LLMs agents can do. The implications:

1. **Agentic RL as a first-class use case**: miles explicitly supports agentic training environments (Harbor, HUD, NeMo Gym). Prior RL training frameworks treated language tasks as the default; miles frames agentic task training as a supported production use case. This means models fine-tuned with miles may have qualitatively different agent behavior compared to supervised-only fine-tunes.

2. **Infrastructure prerequisite for custom model entries**: any organization considering deploying a custom-trained LLM agent (relevant to clawfit's `hardware: on-prem` and `hardware: edge` profiles) needs an RL post-training pipeline. Miles is now the clearest candidate for a framework recommendation in that space.

3. **R3 and TITO as correctness signals**: the fact that routing consistency (R3) and token alignment (TITO) are novel enough to warrant named features suggests these are systemic problems in prior RL training pipelines — worth tracking because they affect the quality of any agent trained using RL without these mitigations.

## Preliminary interpretation

Current best reading:
- **Level 5 — Memory / observability / learning layer (primary)**: miles produces post-trained models — it is the mechanism by which agent behavior is shaped via reward signals. It does not orchestrate agents; it trains the models that agents use.
- **No secondary layer**: miles does not expose APIs, build harnesses, or manage agent workflows at runtime — it is purely a training infrastructure tool.

## Claims to verify

- The "trillion-parameter scale" claim in the tagline — whether miles has been validated at that scale in production, or whether the architecture is designed for that scale but tested at smaller sizes
- Whether Day-0 frontier model support (DeepSeek-V4, Kimi-K3) is based on architecture compatibility alone or on validated training runs
- The RDMA requirement: whether P2P RDMA is a hard infrastructure dependency or falls back gracefully to slower weight sync on non-RDMA clusters
- Whether the agentic environment support (Harbor, HUD, NeMo Gym) is documented with example training configs or requires significant integration work

## Status

- 2,627 stars, 449 forks — above research-watch threshold (100★); below registry threshold (5k★)
- v0.1 released August 2026 — genuinely new, not a repackaging of prior work
- Not eligible for clawfit registry: miles does not produce agents; it trains models. No cost/latency schema applies.
- First tracked RL post-training framework in the clawfit research-watch log
- Watch for: star growth toward 5k (potential registry signal for future "training infrastructure" schema); production case studies; whether R3 and TITO become standard features in competing frameworks
