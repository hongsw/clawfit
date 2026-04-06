# clawfit

> 에이전트 + LLM + 하드웨어 추천 엔진 및 증거 허브

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7%2B-blue)](pyproject.toml)
[![Tests](https://img.shields.io/badge/tests-pytest-informational)](tests/)
[![Status](https://img.shields.io/badge/status-early%20public-green)](https://github.com/hongsw/clawfit)

**다른 언어로 읽기:** [English 🇺🇸](README.md)

`clawfit`은 하나의 실용적인 질문에 답합니다:

**주어진 태스크, 레이턴시 목표, 예산, 네트워크 환경, 상태 유지 요구사항에 대해, 어떤 에이전트 패턴 + 모델 + 하드웨어 조합이 가장 적합한가?**

경량 추천 CLI로 시작해서, AI 코딩 도구, 에이전트 런타임, 오케스트레이션 프레임워크, 지원 인프라를 위한 더 넓은 **비교 + 증거 허브**로 진화하고 있습니다.

> [!IMPORTANT]
> **에코시스템 맵 — 여기서 시작하세요**
>
> `clawfit`이 실제로 무엇을 매핑·비교·추적하는지 이해하려면 **이것을 먼저 클릭하세요**:
>
> ## **[에코시스템 맵 바로가기: `docs/reference-levels.ko.md`](docs/reference-levels.ko.md)**
>
> 현재 AI 도구 생태계의 전체 구도를 가장 빠르게 파악할 수 있습니다:
> - 기본 에이전트 런타임
> - 하네스 / 래퍼 레이어
> - 리서치 루프 시스템
> - MCP / 메모리 / 툴 에코시스템
> - 바이브코딩 / 에이전트 도구 / 메타 래퍼 트렌드

---

## 🔥 지금 가장 뜨거운 것들 (2026-04)

에코시스템이 빠르게 움직이고 있습니다. 이번 주 주목해야 할 신호들:

| 신호 | 왜 중요한가 | 레벨 |
|------|------------|------|
| **[claude-mem](https://github.com/thedotmack/claude-mem) ⭐45k** | Claude Code용 세션 간 영구 메모리. 훅 + SQLite + Chroma 기반. `npx claude-mem install`로 설치. | L4 메모리 |
| **[deepagents](https://github.com/langchain-ai/deepagents) ⭐19k** | LangChain의 배터리 포함 오픈소스 에이전트 하네스. Claude Code CLI의 직접 경쟁자. | L1/L2 |
| **Agentic AI Foundation** | MCP가 Linux Foundation 컨소시엄에 기증됨 (Microsoft + Google + OpenAI + Anthropic). 월 9,700만 SDK 다운로드. OpenAI의 AGENTS.md는 새로운 크로스 플랫폼 스펙. | 거버넌스 |
| **[oh-my-claudecode](https://github.com/yeachan-heo/oh-my-claudecode) ⭐24k** | 스타 수 두 배 성장 — 멀티에이전트 Claude Code 오케스트레이션이 본격화. | L2 |
| **[everything-claude-code](https://github.com/affaan-m/everything-claude-code) ⭐140k** | 가장 큰 Claude Code 리소스 허브. | L3 |
| **Claude 컴퓨터 사용** | 퍼스트파티 데스크탑 제어 (마우스/키보드/화면). Claude Code Desktop + Cowork 통합. L1/L7 경계 붕괴. | L1/L7 |
| **스킬 레이어 성숙** | [Chops](https://github.com/Shpigford/chops), [skills-cleaner](https://github.com/amebahead/skills-cleaner), [Impeccable](https://github.com/pbakaus/impeccable), [K-Skill](https://github.com/NomaDamas/k-skill) — 같은 주에 동시 등장. L4가 스킬 매니저 / 도메인 팩 / 툴 인프라로 분화 중. | L4 |
| **[Mozilla cq](https://blog.mozilla.ai/cq-stack-overflow-for-agents/)** | "에이전트를 위한 Stack Overflow" — 멀티에이전트 공유 지식 커먼스. 새로운 상태유지 패턴: *집단적(collective)*. | L5 |

전체 분석: [`docs/research-watch/`](docs/research-watch/) · 전체 맵: [`docs/reference-levels.ko.md`](docs/reference-levels.ko.md)

---

## 변경 이력

| 날짜 | 변경 내용 |
|------|----------|
| 2026-04-06 | GitHub API로 50개+ 추적 레포 스타 수 전수 검증 |
| 2026-04-06 | research-watch 문서 13개 신규: deepagents, claude-mem, Agentic AI Foundation, Codex 플러그인, Claude 컴퓨터 사용, oh-my-pi Hashline, cq, gitagent, 스킬 레이어 군집, understudy |
| 2026-04-06 | `reference-levels.md` → v0.3: L4를 4a/4b/4c로 세분화; L3에 AGENTS.md 추가; L7에 컴퓨터 사용 에이전트 추가 |
| 2026-04-06 | 하네스팀 추가: `.claude/agents/`에 5개 전문 서브에이전트 |
| 2026-03-31 | 에코시스템 맵 v0.2: 7레이어 분류체계, research-watch 스캔 시작 |

---

## 처음 방문하셨나요?

- **소개 문서:** [`clawfit 소개`](https://github.com/hongsw/clawfit/blob/main/docs/posts/2026-03-28-introducing-clawfit.md)
- **에코시스템 개요:** [`docs/pages/ecosystem-overview.md`](https://github.com/hongsw/clawfit/blob/main/docs/pages/ecosystem-overview.md)

## 왜 만들었나

AI 도구 생태계는 파편화되어 있습니다.

사람들이 비교하는 것들:
- 에이전트 프레임워크
- 코딩 어시스턴트
- 모델 제공자
- 로컬 vs 클라우드 하드웨어
- 메모리 / MCP / 플러그인 에코시스템
- 워크플로우 래퍼와 오케스트레이션 레이어

하지만 대부분의 비교는:
- 경험에만 의존하거나,
- 마케팅 위주이거나,
- 범위가 너무 좁거나,
- 실제 실행 제약과 동떨어져 있습니다.

`clawfit`은 그 트레이드오프를 더 명확하게 만들기 위한 시도입니다.

---

## clawfit이 지금 하는 것

### 1) 조합 추천
다음 조합의 후보를 랭킹합니다:
- **에이전트 패턴**
- **LLM**
- **하드웨어**

제약 조건 기준:
- 태스크 유형
- 레이턴시
- 예산
- 하드웨어 선호도
- 온라인/오프라인 네트워크 요구사항
- 상태 유지 요구사항

### 2) 구조화된 레지스트리에 트레이드오프 저장
비교 가정을 산문에 묻는 대신, 기계가 읽을 수 있는 데이터 파일로 저장합니다.

### 3) 에코시스템을 참조 레벨로 분류
AI 에이전트 및 코딩 도구 에코시스템을 위한 확장 증거 맵을 포함합니다.

---

## 빠른 시작

### 설치

```bash
git clone https://github.com/hongsw/clawfit.git
cd clawfit
pip install -e .
```

### 추천 실행

```bash
clawfit recommend --task qa --latency low --budget 0.01
```

### 상세 예시

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

### 레지스트리 확인

```bash
clawfit list agents
clawfit list llms
clawfit list hardware
clawfit profile
```

---

## 출력 예시

`clawfit recommend`는 JSON을 반환합니다:

```json
[
  {
    "agent": "react-agent",
    "llm": "claude-sonnet",
    "hardware": "aws-cpu-medium",
    "architecture": "cloud-api",
    "fit_score": 0.85,
    "why": [
      "QA 워크로드에 좋은 태스크 매칭",
      "레이턴시 목표가 에이전트 + 모델 프로파일과 일치"
    ],
    "risk": [
      "소형 대안 대비 토큰당 비용이 높음"
    ]
  }
]
```

---

## 지원 태스크 카테고리

- `classification` — 분류
- `code-gen` — 코드 생성
- `data-analysis` — 데이터 분석
- `qa` — 질의응답
- `research` — 리서치
- `summarization` — 요약

---

## Python API

```python
from clawfit.recommend import recommend

results = recommend(
    task="research",
    latency="high",
    network="online",
    top_n=3,
)

print(results[0])
```

---

## 작동 방식

파이프라인은 의도적으로 단순하고 검사 가능합니다:

1. **레지스트리 로딩** — 에이전트 / LLM / 하드웨어 정의 로드
2. **제약 필터링** — 호환되지 않는 옵션 제거
3. **스코어링** — 나머지 조합을 적합도로 랭킹
4. **추천 출력** — 근거와 리스크가 포함된 상위 후보 반환

---

## 리포지터리 구조

```text
clawfit/
├─ .claude/agents/          ← 하네스팀 서브에이전트 (5개)
├─ clawfit/
│  ├─ cli.py
│  ├─ filters.py
│  ├─ loader.py
│  ├─ recommend.py
│  ├─ scoring.py
│  └─ schemas.py
├─ docs/
│  ├─ reference-levels.md   ← 에코시스템 맵 (영문)
│  ├─ reference-levels.ko.md← 에코시스템 맵 (한국어)
│  ├─ research-watch/       ← 개별 도구 분석 (38개+)
│  └─ pages/
├─ tests/
│  ├─ test_filters.py
│  └─ test_recommend.py
└─ pyproject.toml
```

---

## 에코시스템 리서치 레이어

clawfit은 좁은 추천 엔진을 넘어 AI 도구를 위한 더 넓은 비교 프레임워크로 진화하고 있습니다.

### 7레이어 구조

| 레벨 | 영문명 | 설명 |
|------|--------|------|
| 1 | Base runtimes | 기본 에이전트 런타임 (Claude Code, OpenClaw, Aider 등) |
| 2 | Meta wrappers / harnesses | 메타 래퍼 / 하네스 (oh-my-*, SuperClaude, 라우터 등) |
| 3 | Team harness / SSOT | 팀 하네스 / 실행 가능 단일 진실 공급원 (gitagent, AGENTS.md 등) |
| 4 | Capability extension | 기능 확장 레이어 (MCP / 메모리 / 플러그인 / 스킬) |
| 5 | Research / evaluation | 리서치 / 평가 / 벤치마크 / 집단 지식 시스템 |
| 6 | Data / knowledge infra | 데이터 / 증거 / 지식 인프라 |
| 7 | Human interface | 휴먼 인터페이스 / 음성 / 컴퓨터 사용 |

전체 맵: [`docs/reference-levels.ko.md`](docs/reference-levels.ko.md)

---

## 테스트 실행

```bash
python -m pytest tests/ -v
```

---

## 라이선스

MIT
