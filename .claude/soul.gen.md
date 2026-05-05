# clawfit Soul Document — Claude 작업 가이드

> 이 파일은 오너(hongsw)의 의도, 작업 패턴, 반복 실수 방지 규칙을 담고 있다.
> 새 대화를 시작할 때 이 파일을 먼저 읽어라.
> 자동 생성: 2026-05-05 | 세션: 378bbd5c

---

## 1. 이 프로젝트가 무엇인가

`clawfit`은 두 가지 역할을 동시에 한다:

1. **추천 엔진** — 사용자의 조건(task, latency, budget, network, hardware)에 맞는 AI 에이전트+LLM+하드웨어 조합을 추천하는 Python CLI. 핵심 파이프라인: `load → filter → score → rank → output`
2. **에코시스템 지도** — AI 툴링 생태계를 7-레이어 분류 체계로 추적하는 문서 프로젝트. 레이어 정의는 `docs/reference-levels.md`(EN) + `docs/reference-levels.ko.md`(KO).

두 역할은 분리되어 있다. 추천 엔진 코드를 건드리지 않아도 에코시스템 지도는 매일 업데이트된다.

---

## 2. 오너의 작업 철학

### 정확성 > 속도
- registry 등록 기준: **GitHub ⭐5,000 이상 + 독립 검증 가능 사실 데이터** 두 조건 모두 충족. 애매하면 `research-watch`에만 남기고 registry는 보류.
- 분류도 마찬가지. 하나의 신호만으로 레이어 승격 금지. 두 번째 독립 신호가 올 때까지 `### 📡` 로그에만 기록.

### 한국어 문서는 영어 문서와 동기화해야 한다
- `docs/reference-levels.md` 변경 → `docs/reference-levels.ko.md`도 동일하게 반영.
- `README.md` 변경 → `README.ko.md`도 동일하게 반영.
- **자주 발생하는 실수**: 영어만 업데이트하고 한국어를 빠뜨리는 것. 작업 완료 전에 반드시 둘 다 확인.

### 시각적 위계가 중요하다
- `## 🗓` — 월별 패턴 요약 (안정적, 큐레이션된 내용)
- `### 📡` — 일별 신규 신호 로그 (발견 즉시 기록, 임시적)
- `####` — 각 레이어 내 서브섹션
- 같은 레벨(`###`)로 섞으면 즉시 지적받는다.

---

## 3. 7-레이어 분류 체계 (핵심 개념)

```
L7  Human Interface / Voice / I-O
L6a Retrieval-native Knowledge Infra    (LLM은 소비자, 파이프라인이 저장소 유지)
L6b LLM-native KB                       (LLM이 직접 저장소 유지, 검색 파이프라인 없음)
L5  Research / Evaluation / Benchmark
L4a Memory / Persistent Context
L4b Skills / Skill Packs / Skill Managers
L4c Tool-use / Action Infra / MCP
L3  Team Harness / SSOT / Governance
L2  Meta Wrappers / Harnesses / Orchestration
L1  Base Runtimes / Primary Agent Surfaces
L0* Inference Runtime Substrate (companion axis, NOT a numbered level)
```

### L6a vs L6b 구분 기준 (2026-05-05 공식화)
- **쓰기 주체가 LLM** → L6b (wuphf, GBrain, 찰떡AI)
- **읽기 주체가 LLM** → L6a (MinerU, LightRAG, CocoIndex, airweave)

### Multi-layer collapse 패턴
도구가 두 레이어에 걸치면: primary level + secondary level로 표기. 신호만 있다고 secondary로 넣지 않는다. 기능이 실제로 그 레이어에서 작동해야 한다.

---

## 4. 매일 해야 할 일 (Daily Scan)

`/daily-ecosystem-scan` 스킬이 자동화하지만, 주요 체크리스트:

1. `docs/research-watch/YYYY-MM-DD-*.md` 신규 문서 작성 (research-watcher 에이전트 위임)
2. `docs/reference-levels.md` 업데이트 (ecosystem-mapper 조건부 위임)
3. `docs/reference-levels.ko.md`도 동일하게 업데이트 ← 자주 빠뜨림
4. `README.md` + `README.ko.md` 핫 테이블 갱신
5. `python -m pytest tests/ -v` 통과 확인
6. 커밋 (푸시는 사용자 검토 후)

### 스캔 스케줄
사용자 휴식 시간: **낮 12시, 저녁 18시, 새벽 4~9시** → 이때 cron 실행.

---

## 5. 반복 실수 목록

| 실수 | 올바른 행동 |
|------|------------|
| 영어 `reference-levels.md`만 수정, 한국어 빠뜨림 | 항상 두 파일 동시에 수정 |
| `### 신규 신호` 섹션을 영어만 추가 | 한국어 파일에도 `### 📡 YYYY-MM-DD 신규 신호` 추가 |
| monthly 패턴 요약을 `###`로 작성 | `## 🗓`으로 작성 |
| daily 신호를 `##`로 올려쓰기 | `### 📡`로 유지 |
| registry 기준 미달 항목을 추가 | research-watch 문서에만 기록, registry 보류 |
| L0를 "Level 0"으로 표기 | L0는 companion axis — 레벨 번호에 포함하지 않음 |
| git push를 자동으로 실행 | 커밋까지만. 푸시는 사용자가 검토 후 결정 |
| `--no-verify` 사용 | 절대 사용 금지 |

---

## 6. 커밋 메시지 패턴

영문 원칙:
```
<scope>: <what changed> (<N> signals / <change type>)

- Signal 1: detail
- Signal 2: detail

reference-levels.md: <changes or "no changes">
Scoring audit: <result>
Registry: <added / "No registry entries added (none above threshold)">
```

매일 스캔 커밋 예:
```
Daily scan 2026-05-05: 6 new research-watch signals; scoring clean
```

---

## 7. 파일 구조 핵심

```
clawfit/
├── registry/
│   ├── agents.json       # 추천 엔진 데이터
│   ├── llms.json
│   └── hardware.json
├── cli.py / filters.py / scoring.py / recommend.py
docs/
├── reference-levels.md      # 영문 에코시스템 지도 (canonical)
├── reference-levels.ko.md   # 한국어 번역 (항상 동기화)
├── research-watch/          # 일별 신호 문서
│   └── YYYY-MM-DD-<kebab>.md
└── reference-notes/
    └── ecosystem-layers-diagram.md  # 버전 표기 동기화 필요
README.md       # 영문 (핫 테이블 매일 갱신)
README.ko.md    # 한국어 (영문과 동기화)
```

---

## 8. 현재 버전 상태 (2026-05-05)

- `docs/reference-levels.md`: **v0.4** (L6a/L6b 분리로 v0.3 → v0.4)
- `docs/reference-levels.ko.md`: **v0.4**
- `docs/reference-notes/ecosystem-layers-diagram.md`: v0.4 동기화됨
- pytest: PASS
- 마지막 커밋: `3037152`

### v0.4 핵심 변경 (2026-05-05)
- L6 → L6a + L6b 공식 분리
- L4b에 agency-agents 추가 (⭐92.4k)
- L6b에 찰떡AI 추가 (한국 첫 사례)
- `## 🗓` / `### 📡` 헤딩 위계 도입

---

## 9. 사용자 소통 스타일

- 짧게 보고한다. 완료 후 1-2줄 요약.
- 한국어 메시지에는 한국어로 답한다.
- 실수를 지적받으면 사과 없이 즉시 수정한다.
- "잘 되고 있닌지 점검하고" 같은 말은 단순 상태 확인이 아니라 **문제가 있을 수 있다는 신호**다. 먼저 실제 상태를 확인하라.
- 사용자가 URL을 주면 직접 분석하고 레이어 분류까지 제안한다.

---

## 10. 중요 외부 참조

- Karpathy LLM Wiki gist (2026-04-04) — L6b 분류의 기준점
- 찰떡AI (https://chaltteok-app.baryon.ai/) — 한국 L6b 첫 확인 사례
- Linux Foundation Agentic AI Foundation — MCP 거버넌스 이관 (Microsoft + Google + OpenAI + Anthropic)
