# 제2장 — Impact–Uncertainty 평가 프롬프트 (v1)

> **사용 시 함께 입력**: `prompts/00-system_v1.md` + `prompts/personas_v1.md` + 본 파일.
> 페르소나의 정의는 본 파일에서 다시 적지 않고 `prompts/personas_v1.md`를 단일 출처로 사용한다.

# Objective
제1장에서 도출된 모든 Factor에 대해,
**4가지 투자 페르소나(P1~P4)** 가 각각 **Impact**와 **Uncertainty**를 평가한다.

# Personas (요약)
- **P1 — Techno-Optimist** (필수)
- **P2 — Risk & Regulation Officer** (필수)
- **P3 — Customer-Centric Realist** (필수)
- **P4 — Capital Allocator** (선택; 투자 실행 가능성과 직접 연결되는 Factor에만 적용)

상세 정의·역할·편향은 `prompts/personas_v1.md`를 따른다.

# Task
각 Factor에 대해 적용 가능한 페르소나가 각각 다음을 평가:

1) Impact (영향도)
   - 1: Very Low / 2: Low / 3: Moderate / 4: High / 5: Very High
2) Uncertainty (불확실성)
   - 1: Very Certain / 2: Certain / 3: Somewhat Uncertain / 4: Uncertain / 5: Very Uncertain

# Instructions
- 각 페르소나의 평가는 **서로 독립적으로** 수행한다 (한 페르소나의 결과를 보고 다른 페르소나를 정렬하지 않음).
- 점수 옆에 반드시 **한 줄 사유**.
- **P4는 모든 Factor에 의무 적용이 아니다.** 다음 조건 중 하나에 해당할 때만 적용:
  - 해당 Factor가 상장/비상장 기업 식별성과 강하게 연결된다고 판단될 때
  - 해당 Factor가 포트폴리오 비중·유동성에 영향을 줄 가능성이 클 때
- 페르소나 간 점수 차가 ±2 이상이면 **분산 메모**에 갈리는 사유를 1줄로 기록한다.

# Output Format
각 Factor에 대해 다음 형식으로 출력 (P4는 적용 시에만 출력):

[Factor 명 / 도메인]
▶ P1 Techno-Optimist
- Impact: (1~5) — 사유: ...
- Uncertainty: (1~5) — 사유: ...
▶ P2 Risk & Regulation Officer
- Impact: (1~5) — 사유: ...
- Uncertainty: (1~5) — 사유: ...
▶ P3 Customer-Centric Realist
- Impact: (1~5) — 사유: ...
- Uncertainty: (1~5) — 사유: ...
▶ P4 Capital Allocator    (선택 적용 시)
- Impact: (1~5) — 사유: ...
- Uncertainty: (1~5) — 사유: ...
▶ 합산 결과
- 평균 Impact: x.x  /  평균 Uncertainty: x.x  (실제 적용된 페르소나 수로 평균)
- 페르소나 분산 메모: (점수가 크게 갈리는 경우 사유 1줄, 없으면 "분산 낮음")
- 메모: (분기 변수 후보 / 모니터링 / 공통 가정 중 어디에 가까운지)
