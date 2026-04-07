# Research Watch: pi-generative-ui

- Repo/Link: https://github.com/Michaelliv/pi-generative-ui
- Source: hongsw GitHub stars

## 무엇인가

pi-generative-ui는 **Claude.ai의 내부 `show_widget` 도구를 역엔지니어링해 `pi` macOS 에이전트 런타임용으로 재구현한 생성형 UI 플러그인**이다. 대화 내보내기 JSON에서 Anthropic의 72KB 프로덕션 디자인 가이드라인을 추출했으며, LLM이 생성하는 HTML/SVG 위젯을 macOS 네이티브 창(Glimpse/WKWebView)에서 토큰 스트리밍 중에 실시간으로 렌더링한다.

## 주요 특징

- **스트리밍 렌더링**: morphdom DOM diffing으로 HTML 토큰이 생성되는 즉시 위젯이 라이브 업데이트 (<50ms 레이턴시)
- **Anthropic 디자인 시스템 탑재**: 5개 모듈 lazy-loading — diagram(59KB), chart(22KB), interactive(19KB), mockup(19KB), art(17KB). claude.ai 내보내기에서 추출한 실제 가이드라인 (총 72KB 인용은 단일 모듈 기준)
- **양방향 통신**: `window.glimpse.send(data)`로 위젯에서 에이전트로 데이터 전송
- **자동 LLM 도구 2개**: `visualize_read_me`(지연 로딩 디자인 가이드라인), `show_widget`(HTML 렌더러)
- **macOS 전용**: Swift/WKWebView 의존, Xcode Command Line Tools 필요
- 설치: `pi install git:github.com/Michaelliv/pi-generative-ui` 단일 명령

## clawfit 관점에서 의미

- 생성형 UI가 브라우저를 벗어나 **네이티브 데스크톱 에이전트 Surface로 이동**하는 L7 신호
- 현재 human interface 카테고리에 인터랙티브 시각화/생성형 UI 항목 없음 → 갭
- Anthropic 디자인 시스템 추출은 Claude.ai가 시각적 출력 제약을 내부적으로 구조화하는 방식을 보여주는 연구 아티팩트
- 스타 876개: 브라우저 외 생성형 UI 수요 확인

## 분류

**Level 7 — 인간 인터페이스 / 생성형 UI (macOS 네이티브, 스트리밍 위젯 렌더링)**

## 상태

- 추적 중: 신규 등록. 중간-높은 신호. 스타 876개. macOS 전용 제약이 도달 범위를 제한; 크로스 플랫폼 포팅 및 Anthropic의 `show_widget` API 공식화 여부 모니터링.
