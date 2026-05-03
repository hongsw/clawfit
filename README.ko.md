# clawfit

> AI 에이전트 + LLM + 하드웨어 추천 엔진 — 76개 도구, 7레이어 에코시스템 맵, 10차원 조직 적합도 스코어링

[![MIT License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Python](https://img.shields.io/badge/python-3.7%2B-blue)](pyproject.toml)
[![Tests](https://img.shields.io/badge/tests-pytest-informational)](tests/)
[![Status](https://img.shields.io/badge/status-early%20public-green)](https://github.com/hongsw/clawfit)

**다른 언어로 읽기:** [English 🇺🇸](README.md)

---

## clawfit이 뭔가요?

`clawfit`은 하나의 실용적인 질문에 답합니다:

**주어진 태스크, 레이턴시 목표, 예산, 네트워크 환경, 팀 성숙도에서 어떤 에이전트 + 모델 + 하드웨어 조합이 가장 적합한가?**

세 가지를 하나로 통합합니다:

1. **추천 엔진** — 76개 도구를 10차원으로 스코어링 (태스크 적합도, 성숙도, 역할, 레이어, 팀 규모, 네트워크, 레이턴시, 기능, 복잡도, 예산). 치명적 불일치에는 하드 멀티플라이어 적용 (오프라인 필요 + 온라인 전용 도구 → x0.25).

2. **에코시스템 맵** — 7레이어 분류체계 (L1 기본 런타임 → L7 휴먼 인터페이스)에 150개 이상의 research-watch 신호 문서. GitHub Trending, GeekNews, Hacker News를 매일 자동 에이전트로 스캔.

3. **조직 적합도 진단** — 10문항 인터랙티브 설문 (TUI, CLI, 웹)으로 조직 프로파일을 구축하고 우선순위화된 멀티 레이어 도구 스택을 추천.

### 누구를 위한 것인가?

- 에이전트 스택을 비교하는 팀 (Claude Code vs OpenClaw vs Aider vs ...)
- 로컬 vs 클라우드 실행 토폴로지를 결정하는 DevOps
- AI 도구 도입 전략을 평가하는 경영진
- AI 에이전트 에코시스템을 매핑하는 연구자
- 증거 기반 추천 레이어를 구축하려는 모든 사람

> [!IMPORTANT]
> **에코시스템 맵 — 여기서 시작하세요**
>
> `clawfit`이 실제로 무엇을 매핑·비교·추적하는지 이해하려면:
>
> ## **[에코시스템 맵 바로가기: `docs/reference-levels.md`](https://github.com/hongsw/clawfit/blob/main/docs/reference-levels.md)**
>
> 현재 AI 도구 생태계의 전체 구도를 가장 빠르게 파악할 수 있습니다:
> - 기본 에이전트 런타임 (Claude Code, OpenClaw, Goose, Aider, pi-mono, ATLAS...)
> - 하네스 / 래퍼 레이어 (oh-my-*, DureClaw, SuperClaude, Archon...)
> - 리서치 루프 시스템 (autoresearch, mdarena, cq...)
> - MCP / 메모리 / 툴 에코시스템 (claude-mem, korean-law-mcp, rtk...)
> - 스킬팩 & 페르소나 레이어 (career-ops, caveman, Polysona...)
> - 휴먼 인터페이스 / 생성형 UI (pi-generative-ui, Ghost Pepper...)

---

## 🔥 지금 가장 뜨거운 것들 (2026-04)

| 신호 | 왜 중요한가 | 레벨 |
|------|------------|------|
| **[Warp](https://github.com/warpdotdev/warp) ⭐42.3k** | OpenAI가 창립 스폰서로 참여해 오픈소스화된 터미널/ADE. 하루 +11,955★ — 신규 속도 기록. | L6/L2/L1 |
| **[Zed 1.0](https://github.com/zed-industries/zed)** | 안정 버전 출시 + Zed for Business. ACP 멀티플렉싱 (Claude/Codex/OpenCode/Cursor) + 엔터프라이즈 RBAC. | L7 |
| **[cc-switch](https://github.com/hongsw/cc-switch) ⭐52.8k** | 크로스 CLI 프로바이더 전환기: Claude Code, Codex, Gemini, OpenCode, OpenClaw를 하나의 SSOT로 통합. | L3/L4 |
| **[memvid](https://github.com/memvid/memvid) ⭐15.3k** | 단일 파일 `.mv2` 이식형 바이너리 메모리 컨테이너. 0.025ms P50 검색; L4a 세 번째 메모리 서브트랙. | L4a |
| **[Mistral Medium 3.5](https://mistral.ai) 🆕** | 128B, 256k ctx, SWE-Bench Verified 77.6%. "Vibe Remote Agents" — 메이저 모델 랩 최초로 "vibe"를 제품명에 채택. | LLM |
| **[superpowers](https://github.com/obra/superpowers) ⭐145k** | 가장 큰 하네스/SSOT 리포. Shell 기반 에이전틱 스킬 프레임워크 + 방법론. | L3/L4b |
| **[NVIDIA OpenShell](https://github.com/NVIDIA/OpenShell) ⭐5.4k** | NVIDIA의 첫 L1 엔트리. K3s-in-Docker 내장 샌드박스; 런타임 무관. | L1 |
| **[DureClaw](https://github.com/DureClaw/dureclaw) 🔥** | 크로스 머신 멀티 에이전트 오케스트레이션. Claude Code + Phoenix WebSocket + 이종 백엔드. hongsw 직접 제작. | L2/L4c |
| **[cmux](https://github.com/cmux/cmux) ⭐15.6k** | `claude-teams` 통합을 갖춘 네이티브 macOS 터미널 멀티플렉서. | L6 |
| **[GitNexus](https://github.com/gitnexus/gitnexus) ⭐31.5k** | WASM/WebGPU 클라이언트 사이드 모드를 갖춘 코드 특화 그래프-RAG. MCP 도구 16개. | L4a/L4c |

전체 분석: [`docs/research-watch/`](docs/research-watch/) (150개+ 문서) · 전체 맵: [`docs/reference-levels.md`](docs/reference-levels.md)

---

## 변경 이력

| 날짜 | 변경 내용 |
|------|----------|
| 2026-04-30 | 데일리 스캔: Warp 오픈소스 +11,955★/일 기록, Zed 1.0 안정화, Mistral Medium 3.5 → llms.json, NVIDIA OpenShell L1, memvid L4a 이식형 바이너리, cc-connect L7 3번째 데이터포인트, hongsw/harness L2. research-watch 7개 추가. |
| 2026-04-28 | GitHub 스타 전체 최신화. 분류 목록·테이블 스타순 정렬. 04-21~04-28 데일리 스캔: cc-switch 52.8k★, cmux 15.6k★, GitNexus 31.5k★, dirac TB2 리더, Engram+wuphf L4a, DureClaw L3 SSOT 확인. research-watch 12개 추가. |
| 2026-04-20 | Thunderbolt Mozilla AI 클라이언트 L7, OpenMythos 루프 트랜스포머 신호, Qwen3.6-35B-A3B 오픈웨이트 에이전틱 코딩. |
| 2026-04-12 | DureClaw 하이라이트 추가. 신규 도구 8개 (50→58). 태스크 분류 확장: +orchestration, +education, +legal-research. exec 역할 스코어링 수정. |
| 2026-04-12 | 데일리 스캔: Strix 보안 에이전트, GBrain 개인 지식 베이스 |
| 2026-04-11 | 데일리 스캔: superpowers 145k★, Archon 하네스 빌더, rowboat 메모리 네이티브, Twill.ai 클라우드 위임 |
| 2026-04-08 | Claude Mythos Preview 모델, GLM-5.1 장기 태스크, NVIDIA PersonaPlex, Addy Osmani agent-skills |
| 2026-04-07 | hongsw stars 8개 리포 추가: career-ops, claude-peers-mcp, polysona, pi-generative-ui, dureclaw. 한국어 재작성. 전체 수치 검증. |
| 2026-04-06 | reference-levels.md v0.3: L4 → 4a/4b/4c 세분화. research-watch 19개. 하네스팀 (`.claude/agents/`). |
| 2026-03-31 | 에코시스템 맵 v0.2: 7레이어 분류체계, research-watch 스캔 시작 |

---

## 빠른 시작

### 설치

**방법 A — pipx (권장: 가상환경 없이 전역 설치)**

```bash
pipx install git+https://github.com/hongsw/clawfit
```

> pipx가 없으면: `brew install pipx` 또는 `pip install pipx`

**방법 B — 개발용 editable 설치**

```bash
git clone https://github.com/hongsw/clawfit.git
cd clawfit
python3 -m venv .venv && source .venv/bin/activate
pip install -e .
```

---

### 조직 적합도 진단 — 우리 팀에 맞는 도구 스택 찾기

10개 질문에 답하면 팀에 최적화된 멀티 레이어 도구 조합을 추천합니다.

**TUI** (권장 — 화살표로 탐색, 오른쪽 패널에 결과 실시간 업데이트):

```bash
clawfit tui
```

```
 ████████████░░░░░░  5/10  [USECASE]
 ──────────────────────────┬──────────────────────────────
 AI로 주로 무엇을 하고     │ 4단계 — 도구 활용 에이전트
 싶으신가요?               │
                           │ [PRIMARY] L1 Base runtime
  ○ 코드 작성/리뷰         │    45% Claude Code
  ● 정보 조사 및 요약      │    39% Aider
  ○ 문서 Q&A               │    38% Goose
  ○ 데이터 분류            │
  ○ 데이터 분석            │ [PRIMARY] L4c Tool-use infra
  ○ 콘텐츠 요약            │    41% Serena
                           │    35% Context7
 ─ answered ─              │
  팀 규모: 소규모 팀       │ NEXT STEP
  역할: 개발자             │ meta-wrapper(L2) 도입을
                           │ 고려해보세요...
 ──────────────────────────┴──────────────────────────────
  ↑/↓ 이동   Space/Enter 선택+다음   ← 뒤로   → 앞으로   q 종료
```

| 키 | 동작 |
|----|------|
| `↑` / `↓` | 옵션 이동 |
| `Space` / `Enter` | 선택 + 다음 질문으로 자동 이동 |
| `←` / `h` | 이전 질문으로 |
| `→` / `l` | 다음 질문으로 (이미 답변한 경우) |
| `1` ~ `9` | 해당 번호 질문으로 바로 이동 |
| `q` / `ESC` | 종료 (터미널에 최종 결과 출력) |

**CLI (답변을 JSON으로 미리 입력):**

```bash
clawfit diagnose --answers '{
  "team_size": "small",
  "primary_role": "developer",
  "current_ai_usage": "coding_agent",
  "primary_task": "code-gen",
  "output_destination": "team",
  "frequency": "daily",
  "data_sensitivity": "internal",
  "monthly_budget": "medium",
  "governance_need": "soft",
  "growth_horizon": "deepen"
}'
```

답변 옵션값 참고:

| 질문 ID | 선택 가능한 값 |
|---------|--------------|
| `team_size` | `solo` / `small` / `mid` / `large` |
| `primary_role` | `developer` / `researcher` / `pm` / `exec` / `mixed` |
| `current_ai_usage` | `none` / `chat` / `coding_assistant` / `coding_agent` / `multi_agent` / `building` |
| `primary_task` | `code-gen` / `research` / `qa` / `classification` / `data-analysis` / `summarization` / `orchestration` / `education` / `legal-research` |
| `output_destination` | `personal` / `team` / `internal_product` / `external` |
| `frequency` | `occasional` / `daily` / `continuous` |
| `data_sensitivity` | `public` / `internal` / `confidential` / `regulated` |
| `monthly_budget` | `free` / `low` / `medium` / `high` |
| `governance_need` | `none` / `soft` / `hard` |
| `growth_horizon` | `stable` / `expand` / `deepen` |

**웹 UI** (브라우저에서 실시간 필터링):

```bash
clawfit serve          # http://localhost:7771 자동 오픈
clawfit serve --port 8080
```

---

### 제약 조건을 이미 알고 있다면 — 직접 추천

```bash
clawfit recommend --task qa --latency low --budget 0.01
```

```bash
clawfit recommend \
  --task code-gen \
  --latency medium \
  --budget 0.01 \
  --hardware cloud \
  --network online \
  --statefulness session \
  --maturity 5 \
  --top 5
```

> `--maturity 5` = 서브에이전트 운영 단계. 전체 11단계 정의는 [성숙도 × 레이어 맵](docs/pages/maturity-layer-map.md) 참고.

### 레지스트리 확인

```bash
clawfit list agents
clawfit list llms
clawfit list hardware
clawfit profile
```

---

## 스코어링 모델

10차원 가중 스코어링 + 하드 멀티플라이어:

| 차원 | 가중치 | 측정 대상 |
|------|--------|----------|
| task_fit | 0.22 | 도구의 태스크 목록이 사용자의 주요 태스크와 일치하는가? |
| maturity_fit | 0.18 | 사용자의 AI 성숙도 단계(1-11)에 적합한 도구인가? |
| role_fit | 0.15 | 사용자의 역할(개발자/경영진/연구자/DevOps)에 맞는 도구인가? |
| layer_relevance | 0.12 | 도구의 에코시스템 레이어(L1-L7)가 프로파일의 레이어 가중치와 일치하는가? |
| team_size_fit | 0.09 | 사용자의 팀 규모(solo/small/mid/large)에 설계된 도구인가? |
| network_fit | 0.08 | 필요한 네트워크 환경(online/offline/hybrid)에서 작동하는가? |
| latency_fit | 0.06 | 요구되는 레이턴시 티어를 충족하는가? |
| feature_fit | 0.05 | 필요한 기능(거버넌스, 팀 공유, 오프라인)을 지원하는가? |
| complexity_fit | 0.04 | 설치 복잡도가 팀 성숙도에 적합한가? |
| budget_fit | 0.01 | 가격 티어가 예산과 맞는가? |

**하드 멀티플라이어** (가중합 이후 적용):
- 오프라인 필요 + 온라인 전용 도구 → **x0.25**
- 역할 불일치 (역할 겹침 없음) → **x0.75**

---

## 지원 태스크 카테고리

| 태스크 | 설명 |
|--------|------|
| `code-gen` | 코드 생성, 리뷰, 리팩토링 |
| `research` | 정보 수집, 문헌 조사, 심층 분석 |
| `qa` | 질의응답, 문서 Q&A |
| `summarization` | 대규모 콘텐츠 요약 |
| `data-analysis` | 데이터 처리, 시각화, 통계 분석 |
| `orchestration` | 멀티 에이전트 조율, 크로스 머신 태스크 분배 |
| `education` | 개인화 학습, 튜터링, 퀴즈 생성 |
| `legal-research` | 법률 문서 검색, 판례 분석, 규정 준수 |

---

## 작동 방식

파이프라인은 의도적으로 단순하고 검사 가능합니다:

1. **레지스트리 로딩** — 76개 도구 정의 + 10필드 org_fit 메타데이터 로드
2. **프로파일 구축** — 10개 설문 답변 → OrgProfile 변환
3. **스코어링** — 10차원 + 하드 멀티플라이어로 각 도구 평가
4. **레이어 그루핑** — 에코시스템 레이어(L1-L7)별 그룹화, 성숙도 단계별 우선순위
5. **추천 출력** — 근거가 포함된 우선순위화 멀티 레이어 스택 반환

---

## 리포지터리 구조

```text
clawfit/
├─ .claude/agents/          ← 하네스팀 서브에이전트 (5개)
├─ clawfit/
│  ├─ cli.py                ← argparse CLI (recommend, list, tui, serve, diagnose)
│  ├─ org_scorer.py         ← 10차원 스코어링 엔진
│  ├─ tui.py                ← curses TUI (분할 화면 실시간 프리뷰)
│  ├─ server.py             ← stdlib HTTP 서버 (localhost:7771)
│  ├─ diagnose.py           ← 인터랙티브 CLI 설문
│  ├─ filters.py            ← 하드 제약 필터링
│  ├─ scoring.py            ← 카테시안 프로덕트 스코어링 (에이전트 × LLM × 하드웨어)
│  ├─ recommend.py          ← 공개 API: recommend() → list[dict]
│  ├─ schemas.py            ← 데이터클래스: Agent, LLM, Hardware, Recommendation
│  ├─ loader.py             ← registry/*.json 로더
│  ├─ data/
│  │  ├─ tools_registry.json  ← 76개 에코시스템 도구 (org_fit 10필드)
│  │  └─ org_questions.json   ← 10문항 설문, 3 페이즈
│  └─ registry/             ← agents.json, llms.json, hardware.json
├─ docs/
│  ├─ reference-levels.md   ← 에코시스템 맵 v0.3 (7레이어 분류체계)
│  ├─ research-watch/       ← 150개+ 신호 분석 문서 (데일리 자동 스캔)
│  └─ pages/                ← ecosystem-overview, ecosystem-axes, maturity-layer-map
├─ data/
│  └─ tools_registry.json   ← clawfit/data/ 미러
├─ tests/
│  ├─ test_filters.py
│  └─ test_recommend.py
└─ pyproject.toml
```

---

## 에코시스템 리서치 레이어

clawfit은 더 넓은 AI 도구 생태계를 추적합니다:
- [`docs/reference-levels.md`](docs/reference-levels.md) — 정식 7레이어 에코시스템 맵
- [`docs/pages/ecosystem-axes.md`](docs/pages/ecosystem-axes.md) — 분류 로직, 경계 규칙, 예제
- [`docs/research-watch/`](docs/research-watch/) — 150개+ 도구/트렌드 분석 (매일 자동 스캔)
- [`docs/pages/maturity-layer-map.md`](docs/pages/maturity-layer-map.md) — 성숙도 단계(1-11) × 도구 레이어(L1-L7) 매핑

### 7레이어 구조

| 레벨 | 이름 | 주요 도구 |
|------|------|----------|
| 1 | 기본 런타임 | Claude Code, OpenClaw, Aider, pi-mono, ATLAS, Hermes Agent |
| 2 | 메타 래퍼 / 하네스 | oh-my-*, DureClaw, SuperClaude, Archon, multica |
| 3 | 팀 하네스 / SSOT | CLAUDE.md, AGENTS.md, DESIGN.md, gitagent, superpowers |
| 4a | 메모리 / 영구 컨텍스트 | claude-mem, GBrain, Polysona |
| 4b | 스킬팩 & 매니저 | career-ops, caveman, obsidian-skills, Chops |
| 4c | 도구 사용 / 액션 인프라 | korean-law-mcp, rtk, claude-peers-mcp, serena |
| 5 | 리서치 / 평가 | autoresearch, mdarena, Mozilla cq |
| 6 | 데이터 / 지식 인프라 | DeepTutor, AnythingLLM |
| 7 | 휴먼 인터페이스 | pi-generative-ui, Ghost Pepper, ouroboros |

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

## 테스트 실행

```bash
python -m pytest tests/ -v
```

---

## 기여하기

특히 다음 영역의 기여를 환영합니다:
- 레지스트리 확장 (완전한 org_fit 메타데이터가 포함된 신규 도구)
- 스코어링 로직 개선
- 벤치마크 참조 및 증거
- research-watch 신호 분석

이슈 또는 PR을 열어주세요: 무엇을 추가하는지, 어떤 증거가 뒷받침하는지, 비교 모델에 어떻게 맞는지를 포함해주세요.

---

## 라이선스

MIT
