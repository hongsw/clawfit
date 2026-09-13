# Research Watch: ssiat llm — Korean LLM for Raspberry Pi Zero 2W

- Repo/Link: https://huggingface.co/ssiat (Korean LLM project)
- Source: GeekNews

## Why this is worth watching
ssiat llm is a Korean-language model capable of running on a Raspberry Pi Zero 2W — a sub-1W, $15 microcontroller with 512MB RAM. This pushes the edge inference floor to consumer IoT-class hardware, beyond the current "phone-class" benchmark. If this level of capability becomes repeatable for other languages, it redefines what "local AI" means in the hardware recommendation dimension.

## What stands out immediately
- Runs on Raspberry Pi Zero 2W — dramatically cheaper than any current recommended edge hardware
- Korean language focus — signals that multilingual sub-1B models are now viable for edge
- Companion to the broader micro-LLM trend (Needle2 at 14MB, opsa/bonsai 2.7B signals)
- Demonstrated rather than claimed — working on actual hardware

## Why clawfit should care
Clawfit's hardware registry currently bottom-floors at phone/embedded-class GPUs. If Pi Zero 2W-class inference is production-capable (even for simple tasks), it should appear as a new hardware tier — call it "microcontroller" below "embedded." This would affect the `network: offline` and `monthly_budget: low` arms of the recommendation tree, opening options for zero-cloud, zero-GPU deployments. The org-fit axis for `data_sensitivity: confidential` + `governance_need: hard` would benefit from this tier.

## Preliminary interpretation
Current best reading:
- **Level 1 — Base LLM / Edge Inference (Microcontroller Tier)**

## Status
- Tracking: new signal 2026-09-13; verify quantization method and task quality before hardware tier update
