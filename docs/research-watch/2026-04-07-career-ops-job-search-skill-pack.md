# Research Watch: Career-Ops

- Repo/Link: https://github.com/santifer/career-ops
- Source: hongsw GitHub stars

## 무엇인가

Career-Ops는 Claude Code 위에 구축된 **취업 자동화 스킬팩**이다. 채용 공고 평가, ATS 최적화 이력서 PDF 생성, 구직 포털 자동 스캔, 면접 준비까지 취업 파이프라인 전체를 하나의 시스템으로 통합한다. 제작자 Santiago가 740개 이상의 실제 채용 공고에 적용해 Head of Applied AI 직책을 얻어낸 검증된 프로덕션 도구다.

## 주요 기능

- **채용 공고 평가**: A-F 등급 + 10개 가중 항목으로 정량 평가
- **이력서 자동 생성**: ATS 통과를 위한 맞춤형 PDF 생성
- **포털 자동 스캔**: Greenhouse, Ashby, Lever 등 45개 이상 회사의 채용 사이트를 Playwright로 자동 탐색
- **병렬 처리**: 다수의 Claude 워커가 동시에 여러 공고를 분석
- **면접 준비 기록**: STAR+Reflection 방식으로 면접 스토리 뱅크 축적
- **터미널 대시보드**: Bubble Tea 기반 Go 대시보드로 진행 상황 추적

## 기술 스택

Go, Node.js, Playwright, Claude Code, Markdown/YAML/TSV. 단순 스크립트가 아닌 다언어 풀스택 애플리케이션.

## clawfit 관점에서 의미

- `tasks` 분류에 `career-ops` / `job-search` 카테고리가 없음 → 갭 발견
- 개발자 외 페르소나(구직자/연구자)를 대상으로 한 L4b 스킬팩의 가장 성숙한 사례
- 멀티 언어 스택(Go + Node)은 "스킬팩 = 단일 언어 CLI" 가정을 깨뜨림
- 스타 ~12,300개 (12.3k), 포크 ~2,300개 (2.3k), 커밋 35: 실무자 채택이 확인된 높은 신호

## 분류

**Level 4b — Claude Code 위에서 동작하는 도메인 특화 스킬팩 (커리어/채용 분야)**

## 상태

- 추적 중: 신규 등록. 매우 높은 신호. 스타 ~12,300개 (포크 ~2,300, 커밋 35). 팀/엔터프라이즈 기능 확장 여부 및 스킬 모드가 재사용 가능한 프리미티브로 분리되는지 모니터링.
