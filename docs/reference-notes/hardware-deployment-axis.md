# Hardware and Deployment Axis

*Companion note · Addresses GitHub issue #8*

---

## Problem

clawfit's README promises an **agent + LLM + hardware** recommendation engine. The `hardware` field in the registry currently carries three values (`laptop`, `workstation`, `cloud`) which are functional but coarse. Several important distinctions are collapsed:

- A developer's M3 MacBook and a $3,000 Linux workstation with an RTX 4090 are both `hardware: workstation` in different contexts
- `cloud` conflates managed APIs (Anthropic/OpenAI), self-hosted cloud VMs, and vendor-managed platforms (AWS Bedrock, Azure AI, Vertex AI)
- There is no axis for governance requirements (data residency, VPC, HIPAA, SOC 2)
- There is no axis for isolation model (process-level, container, microVM, k8s)

---

## Proposed hardware/deployment taxonomy

### Primary hardware categories (current + expanded)

| Category | Description | Inference substrate |
|----------|-------------|---------------------|
| `laptop` | Consumer notebook; ≤64 GB RAM; Apple Silicon or mid-range x86 | Ollama, llama.cpp, MLX |
| `workstation` | Desktop or tower; dedicated CUDA/AMD GPU; 24–80 GB VRAM | Ollama, vLLM (local), llama.cpp |
| `edge` | Mobile, embedded, IoT; ARM; ≤8 GB RAM | LiteRT-LM, MLC LLM (iOS/Android) |
| `cloud_api` | Managed API endpoint; no user-controlled infra | Anthropic, OpenAI, Mistral, DeepSeek |
| `cloud_vm` | Self-hosted on rented VM/GPU; user manages runtime | vLLM, TGI, TensorRT-LLM on EC2/GCP |
| `cloud_managed` | Fully managed platform with governance surface | AWS Bedrock, Azure AI, Vertex AI |
| `home_cluster` | Multiple consumer devices networked together | exo |

### Deployment context dimensions

These are independent of hardware and should be filterable:

| Dimension | Values | Relevance |
|-----------|--------|-----------|
| `governance_need` | `none` / `basic` / `hard` | HIPAA, SOC 2, data residency requirements |
| `isolation_model` | `process` / `container` / `microvm` / `k8s` | Security boundary required |
| `managed_platform` | `bedrock` / `azure_ai` / `vertex_ai` / `none` | Which managed surface hosts the model |
| `multi_tenancy` | `single` / `team` / `enterprise` | Concurrent user isolation requirements |

---

## How this maps to existing clawfit filters

The current `hardware` filter collapses the above into three choices. Proposed evolution:

```
Current:   hardware: [laptop | workstation | cloud]

Expanded:  hardware_type:  [laptop | workstation | edge | cloud_api | cloud_vm | cloud_managed | home_cluster]
           governance:     [none | basic | hard]
           isolation:      [process | container | microvm | k8s]
```

**Backward compatibility:** The three current values map directly:
- `laptop` → `hardware_type: laptop`
- `workstation` → `hardware_type: workstation`
- `cloud` → `hardware_type: cloud_api` (default assumption)

---

## Connection to inference runtime substrate (#9)

The hardware axis and the inference runtime substrate axis (issue #9) are complementary:

| Hardware context | Inference substrate default |
|------------------|-----------------------------|
| `laptop` (Apple Silicon) | MLX or Ollama (Metal backend) |
| `laptop` (x86) | Ollama or llama.cpp (CPU/CUDA) |
| `workstation` (CUDA) | Ollama + GPU, vLLM, or llama.cpp |
| `cloud_vm` | vLLM, TGI, TensorRT-LLM |
| `cloud_api` | Provider-managed; substrate is opaque |
| `cloud_managed` | Bedrock/Azure/Vertex — substrate is opaque + auditable |
| `home_cluster` | exo (multi-device sharding) |

---

## Discriminating criteria for hardware classification

**Use `cloud_api`** when: the agent calls a remote API endpoint; no user-controlled inference; latency is network-bound; `network: online` is required.

**Use `cloud_managed`** when: governance, data residency, or compliance (HIPAA/SOC 2) drive the platform choice; the managed surface (Bedrock/Azure AI/Vertex AI) provides audit trails and VPC isolation.

**Use `cloud_vm`** when: the user controls the inference stack on rented compute; vLLM or TGI is deployed on EC2/GCP/Azure VMs; cost is usage-based but infra is self-managed.

**Use `workstation`** when: dedicated local GPU (NVIDIA/AMD) is available; VRAM ≥ 16 GB; user can run 7B–70B models without quantization.

**Use `laptop`** when: consumer notebook; VRAM < 16 GB or no discrete GPU; quantized models (GGUF Q4/Q5) are the realistic inference path.

**Use `edge`** when: mobile or embedded target; ARM processor; battery / thermal constraints limit sustained inference.

**Use `home_cluster`** when: user has multiple consumer devices and wants to shard a model too large for any single device.

---

## Recommended v0.4 schema change

Add to `clawfit/registry/hardware.json` entries:

```json
{
  "id": "cloud-managed",
  "name": "Cloud Managed Platform",
  "type": "cloud_managed",
  "governance_profiles": ["hipaa", "soc2", "gdpr"],
  "managed_platforms": ["bedrock", "azure_ai", "vertex_ai"],
  "isolation_model": "k8s",
  "network": "online"
}
```

Current hardware.json has 5 entries. Suggested expansion to 7 (add `cloud_managed` and `edge`).
