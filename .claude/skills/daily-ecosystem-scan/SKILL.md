---
name: daily-ecosystem-scan
description: clawfit 데일리 생태계 스캔 워크플로우. 매일 정해진 키워드/소스에서 새로운 AI 도구·하네스·MCP·스킬·하드웨어 신호를 발굴하고, 5개 전문 에이전트(harness)에게 위임하여 research-watch 문서·reference-levels.md·registry JSON·scoring·tests를 일괄 갱신한다. 트리거: "/daily-ecosystem-scan", "데일리 스캔", "오늘의 생태계 스캔", 또는 cron prompt.
---

# Daily Ecosystem Scan

clawfit 프로젝트의 매일 03:00 자동 실행 워크플로우. 5개 전문 에이전트(`research-watcher`, `ecosystem-mapper`, `registry-curator`, `scoring-analyst`, `test-guardian`)를 오케스트레이션하여 AI 생태계의 새 신호를 수집·분류·등록·검증한다.

이 스킬을 호출하면 클로드는 **본인이 모든 조사 작업을 직접 하지 않고**, 명시된 단계에 따라 Agent 도구로 5개 전문 에이전트에 작업을 위임한다.

## 입력 (있을 경우)
- 사용자가 특정 소스/주제를 지정하면 그것만 스캔
- 인자가 없으면 `KEYWORDS.md`의 전체 소스를 스캔

## 출력 (성공 기준)
- `docs/research-watch/YYYY-MM-DD-*.md` 신규 문서 (보통 3-6개)
- 필요 시 `docs/reference-levels.md` 업데이트
- 필요 시 `clawfit/registry/{agents,llms,hardware}.json` 신규 엔트리
- `python -m pytest tests/ -v` 통과
- 표준 포맷 커밋 메시지(아래 템플릿) 생성. **푸시는 하지 않는다.**

---

## Phase 0 — 사전 점검 (직접 수행)

```bash
cd /Users/hongmartin/dev/clawfit
git status -s
ls docs/research-watch/ | grep "^$(date +%Y-%m-%d)" | wc -l   # 오늘 이미 있는 문서 수
git log --oneline -5
```

- 작업 디렉토리가 깨끗하지 않으면 즉시 중단하고 사용자에게 보고
- 오늘 날짜로 이미 N개 문서가 있으면 "기존 N개 + 추가 스캔" 모드로 진행

오늘 날짜를 시스템에서 확인 (`date +%Y-%m-%d`).

---

## Phase 1 — 신호 수집 (직접 수행, 병렬 WebFetch/WebSearch)

`KEYWORDS.md`의 **소스 목록**을 읽고, 각 소스에서 후보를 수집한다. 병렬로 여러 WebFetch/WebSearch 호출을 한 메시지에 묶는다.

각 후보에 대해 다음을 메모:
1. 이름 / repo URL
2. 핵심 1-2줄 (무엇을 하는가)
3. 신호 출처 (예: "GitHub Trending Daily Python #3", "GeekNews 2위", "Hacker News 312pts")
4. 즉시 식별 가능한 ecosystem 레이어 (1-7) 짐작값

**중복 제거**: 각 후보의 repo URL을 `docs/research-watch/*.md`에서 grep. 이미 추적 중인 도구는 제외.

```bash
grep -rl "github.com/<owner>/<repo>" docs/research-watch/ 2>/dev/null
```

**품질 임계값**:
- GitHub repo: 최소 100 stars (그 이하는 노이즈) — 단, 학술/저자 신뢰도 높으면 예외
- 블로그/뉴스: clawfit 7-layer 분류와 직결되는 신호여야 함
- 신규성: 6개월 이내 첫 공개 또는 최근 2주 내 큰 릴리스

**일일 목표 산출물**: 3-6개 신규 신호. 5개 초과 시 신호 강도 기준으로 컷오프.

---

## Phase 2 — research-watcher에 위임 (병렬)

선별된 각 신호마다 `research-watcher` 서브에이전트를 **병렬로** 호출한다 (한 메시지에 여러 Agent tool use blocks).

각 Agent 호출 prompt 템플릿:
```
[NEW SIGNAL] <name>
- Repo: <url>
- Source: <source/rank>
- One-liner: <what it does>
- Suggested layer (preliminary): Level <N>

위 신호에 대해 docs/research-watch/$(date +%Y-%m-%d)-<kebab-title>.md 를 작성해주세요.
이미 작성된 최근 5개 문서를 먼저 읽고 톤/깊이 캘리브레이션 후, 분석적으로 작성합니다.
docs/reference-levels.md는 수정하지 마세요 — 강한 신호일 경우 status에만 기록.
완료 후 파일 경로와 최종 레이어 분류를 200자 이내로 보고해주세요.
```

각 에이전트가 끝나면 그 결과를 모아둔다 (파일 경로 + 레이어).

---

## Phase 3 — ecosystem-mapper 판단 (조건부)

다음 중 하나라도 해당하면 `ecosystem-mapper`를 호출:
- Phase 2에서 한 에이전트라도 "Level X에 추가 권장" 명시
- 동일 레이어에 신호 2개 이상 동시 발생 (high confidence)
- 새 sub-layer 후보가 등장 (예: L4c, L5d 등)

위임 prompt:
```
오늘 추가된 research-watch 문서들: <파일 경로 목록>
이 신호들을 docs/reference-levels.md에 반영할 만한 것이 있는지 판단하고, 
필요시 항목을 추가하거나 "New signals as of YYYY-MM-DD" 섹션을 갱신해주세요.
단일 신호 기반 promotion은 금지. 분류가 애매하면 reference-levels.md를 건드리지 말고 그 이유를 보고하세요.
```

해당 없으면 이 단계는 건너뛰고 다음으로 간다.

---

## Phase 4 — registry-curator 판단 (조건부)

신호가 다음 조건을 모두 만족할 때만 `registry-curator` 호출:
- GitHub stars ≥ 5,000 OR 상용 제품으로 유의미한 사용처
- clawfit registry 스키마(agents/llms/hardware)에 명확히 매핑 가능
- task/latency/cost/network 등 사실 데이터 확인 가능 (추정 금지)

위임 prompt:
```
다음 신호를 clawfit/registry/{agents.json|llms.json|hardware.json} 중 적합한 곳에 추가해주세요.
- Tool: <name>
- Repo: <url>
- 5k+ stars 또는 상용 사용처 확인됨

스키마 검증, 중복 체크, pytest 회귀 테스트까지 완료 후 보고해주세요.
```

해당 없으면 건너뛴다 (대부분 일자에 등록 가능 항목 없음 — 정상).

---

## Phase 5 — scoring-analyst 감사 (항상 실행)

```
오늘 데일리 스캔이 끝났습니다. 다음을 확인해주세요:
1. python -m pytest tests/ -v 통과 여부
2. clawfit recommend --task qa --latency low --budget 0.01 정상 출력
3. clawfit recommend --task code-gen --latency medium --network online 정상 출력
4. registry 메타데이터에서 명백히 잘못된 항목이 있는지

문제 없으면 "scoring clean"으로 보고. 메타 수정이 필요하면 최소 변경으로 처리하고 diff 보고.
```

---

## Phase 6 — test-guardian 검증 (Phase 4가 실행됐을 때만)

registry에 새 엔트리가 추가됐다면:
```
오늘 추가된 registry 엔트리: <목록>
이에 대한 회귀 테스트가 필요한지 판단하고, 필요하면 tests/test_recommend.py 또는 tests/test_filters.py에 추가해주세요.
모든 테스트 통과 확인 후 보고해주세요.
```

---

## Phase 7 — 커밋 (직접 수행)

```bash
cd /Users/hongmartin/dev/clawfit
git status
git diff --stat
```

표준 커밋 메시지 포맷 (이전 데일리 스캔과 일관성 유지):

```
Daily scan YYYY-MM-DD: <N> new research-watch signals; <scoring status>

New research-watch documents:
- <tool-name>: <one-liner> (<source>, <stars/rank>) — Level <N> <classification note>
- <tool-name>: ...

reference-levels.md: <변경 요약 또는 "no changes">

Scoring audit: <healthy / N metadata fixes>
<Registry: <added entries> 또는 "No registry entries added (none above threshold)">
```

`git add -A && git commit` 으로 커밋. **푸시는 하지 않는다** — 사용자 검토 후 직접 푸시.

---

## Phase 8 — 사용자 보고 (3-5줄)

```
✅ Daily scan YYYY-MM-DD 완료
- 신규 research-watch 문서: N개
- reference-levels.md: <변경 / 변경 없음>
- registry 신규: <0 / 1-2개>
- pytest: <PASS / FAIL>
- 커밋 SHA: <short-sha> (푸시 대기)
```

---

## 실패 처리

- Phase 1에서 후보가 0개 → 그날 의미 있는 신호가 없는 것. 빈 커밋 만들지 말고 사용자에게 "오늘은 신호 없음"만 보고.
- Phase 5에서 pytest fail → 즉시 중단, 커밋 금지, 실패 출력 그대로 사용자에게 보고.
- Phase 2에서 research-watcher 에이전트 일부 실패 → 성공한 것만 진행. 실패 항목은 보고에 명시.
- 네트워크 오류로 WebFetch 실패 → 가능한 소스만으로 진행하고 누락 소스를 보고.

## 규칙

- Claude 본인은 research-watch 문서를 직접 작성하지 않는다 — 반드시 `research-watcher` 에이전트에 위임.
- 모든 Phase 2 에이전트 호출은 병렬로 한 메시지에 묶는다 (직렬 실행 금지).
- 문서 톤은 분석적이어야 한다. 홍보 문구나 별 개수 자랑 금지.
- "오늘 날짜"는 `date +%Y-%m-%d`로 매번 시스템에서 확인 (하드코딩 금지).
- registry 등록은 보수적으로. 애매하면 research-watch에만 남긴다.
- `--no-verify`, `git push --force`, `git push` 절대 금지.
