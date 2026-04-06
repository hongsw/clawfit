# Maturity × Layer Map

> **2축 추천 매트릭스:** 사용자 성숙도(수요 축) × 도구 레이어(공급 축)

이 문서는 ai-maturity-diagnosis의 11단계와 clawfit의 7-레이어 분류체계를 통합합니다.

---

## 핵심 개념

| 시스템 | 축 | 질문 |
|--------|------|------|
| [ai-maturity-diagnosis](https://ai-maturity-diagnosis.site) | 수요 축 / 사용자 성숙도 (1–11단계) | 사용자가 지금 어느 단계인가? |
| clawfit | 공급 축 / 도구 아키텍처 (L1–L7) | 도구 생태계가 어떻게 구조화되어 있는가? |

둘을 합치면 **"지금 나는 여기 있고, 이 도구를 써야 하며, 다음에 이쪽으로 간다"** 가 가능해진다.

---

## 성숙도 단계 정의 (11단계)

| 단계 | 레이블 | 설명 |
|------|--------|------|
| 1 | 챗봇 사용 | ChatGPT/Claude.ai를 대화형으로만 사용 |
| 2 | 다중 챗봇 | 여러 LLM을 목적별로 병행 사용 |
| 3 | 자동화 입문 | Zapier/n8n 수준의 AI 자동화 경험 |
| 4 | 툴 사용형 | MCP, Composio 등 도구 연동 에이전트 활용 |
| 5 | 서브에이전트 | 멀티에이전트 오케스트레이션 직접 운영 |
| 6 | 에이전트 하네스 | 팀/조직 수준의 하네스 설계 및 운영 |
| 7 | 자기개선 루프 | 에이전트가 스스로 평가·개선하는 루프 구축 |
| 8 | 공개/배포 | 자체 에이전트 런타임 또는 하네스를 외부 배포 |
| 9 | sLLM/ML 응용 | 소형 모델 파인튜닝, 도메인 특화 ML 파이프라인 |
| 10 | 시스템 정의형 | 조직 전체의 AI 운영체제를 SSOT로 정의 |
| 11 | 프론티어 | 벤치마크·연구 생산, 생태계 자체를 형성 |

---

## 성숙도 → 적합 clawfit 레이어

```
사용자 단계          적합한 clawfit 공급 레이어
────────────────────────────────────────────────────
1단계  챗봇 사용   →  L1 Base Runtime (Claude.ai, ChatGPT UI)
2단계  다중 챗봇   →  L1 복수 + L7 Human Interface (음성/UI)
3단계  자동화 입문  →  L4c Tool infra (Zapier급 MCP, simple flows)
4단계  툴 사용형   →  L4c MCP / Composio / Serena
5단계  서브에이전트 →  L2 Meta Wrapper (oh-my-claudecode, SuperClaude)
6단계  하네스       →  L2 + L3 Team Harness / SSOT
7단계  자기개선 루프 →  L5 Eval / cq / autoresearch
8단계  공개/배포    →  L1→L2 (자기가 Level 1/2를 만드는 측)
9단계  sLLM/ML     →  L6 Data / Knowledge Infrastructure
10단계 시스템 정의  →  L3 Executable SSOT (gitagent, AGENTS.md)
11단계 프론티어     →  L5 + L6 (벤치마크·연구 생산자)
────────────────────────────────────────────────────
```

---

## 2축 추천 매트릭스

```
          clawfit 공급 레이어 (가로축)
          L1    L2    L3    L4a  L4b  L4c  L5    L6    L7
         ──────────────────────────────────────────────────
1~2단계 │  ●                                          ●
3~4단계 │  ●                         ●    ●
5~6단계 │         ●     ●            ●    ●
7~8단계 │         ●     ●                      ●
9단계   │                                      ●    ●
10~11단계│               ●                     ●    ●
         ──────────────────────────────────────────────────

● = 이 성숙도 단계 사용자에게 이 레이어의 도구가 적합
```

---

## clawfit 에이전트 패턴의 적합 성숙도

| 에이전트 | 적합 단계 | 최적 단계 | 설명 |
|---------|-----------|-----------|------|
| `simple-router` | 1–4 | 3 | 단일 분류·라우팅. 자동화 입문자에게 적합 |
| `react-agent` | 4–7 | 5 | ReAct 루프. 서브에이전트 운영 시작 단계 |
| `local-rag` | 3–6 | 5 | 로컬 문서 기반 RAG. 툴 사용형~하네스 입문 |
| `plan-execute` | 6–9 | 7 | 2단계 계획·실행. 하네스 이상 단계에 적합 |

---

## 통합 추천 예시

### 기존 clawfit (성숙도 없음)
```bash
clawfit recommend --task code-gen --latency medium --budget 0.01
# → react-agent + claude-sonnet + aws-cpu-medium (fit_score: 0.85)
```

### 통합 후 (성숙도 포함)
```bash
# 5단계 사용자 (서브에이전트 운영자)
clawfit recommend --task code-gen --latency medium --budget 0.01 --maturity 5
# → react-agent (fit_score: 0.945, "Optimal match for stage 5 users.")

# 2단계 사용자 (챗봇 다중 사용)
clawfit recommend --task qa --latency low --maturity 2
# → simple-router (fit_score: 1.0, "Good fit for stage 2")

# 8단계 사용자 (배포 단계)
clawfit recommend --task research --latency high --maturity 8
# → plan-execute (fit_score: 0.828, "Good fit for stage 8, optimal: 7")
```

### Python API
```python
from clawfit.recommend import recommend

results = recommend(
    task="code-gen",
    latency="medium",
    maturity_stage=6,   # 에이전트 하네스 단계
    top_n=3,
)
# results[0]["maturity_note"] → "Optimal match for stage 6 users."
```

---

## 역방향 조회: "이 도구는 어떤 성숙도 사용자에게?"

```bash
clawfit list agents
# 각 에이전트의 maturity_min / maturity_max / maturity_optimal 확인
```

---

## 용어 통일 (두 시스템 간)

| ai-maturity 용어 | clawfit 용어 | 통일안 |
|---|---|---|
| 에이전트 하네스 (6단계) | Harness = L3 Team layer | **개인 하네스(L2)** vs **팀 하네스(L3)** |
| 서브에이전트 팀 (5단계) | L2 Meta-wrapper | **Multi-agent orchestration** |
| 자기개선 루프 (7단계) | L5 Autoresearch | **Self-improvement loop** |
| 시스템 정의형 (10단계) | L3 Executable SSOT | **SSOT-native user** |

---

## 네임스페이스

충돌 방지를 위한 명시적 prefix:

```
user.maturity = 1~11      # ai-maturity-diagnosis 기준
tool.layer    = L1~L7     # clawfit 기준
fit.score     = 0~1.0     # 두 축의 매칭 점수
```

---

## 다음 단계

- [ ] `tools_registry.json`에 `target_maturity` 필드 확장 (생태계 도구 전체 대상)
- [ ] ai-maturity-diagnosis 진단 결과 → clawfit API 직접 연결 엔드포인트
- [ ] "다음 단계 준비 도구" 추천 (현재 단계 + 1의 도구 미리 제시)
- [ ] 팀 평균 성숙도 입력 → 팀 단위 도구 도입 경로 추천
