# 제4장 — Scenario Backbone 프롬프트 (v2)

> **v1 → v2 변경 요지**
> 1. 본 분석에서는 **Cross-Impact를 먼저 돌려 `Driving / Dependent / Critical / Inert` 4구역**을 구한 뒤,
>    제3장에서 **가설로 둔 `B × D` 축이 검증되는지** 점검한다 (Validation-first).
> 2. **Cross-impact 척도**는 0~5가 아니라 **0~3** (`0 영향 없음 / 1 약 / 2 중 / 3 강`).
>    - POC 단계에서 14×14 = 196셀을 사람이 평가해야 하므로, 스케일을 좁혀 일관성을 확보한다.
> 3. **DAG**(Influence Diagram)는 임계치 ≥ 3 + 양방향 페어는 우세 방향 1개만 남겨 무순환으로 정리한다.
> 4. **CLD**는 동일 매트릭스에서 도출된 양방향·순환 페어를 묶어 R/B 루프를 식별한다.
> 5. **레버리지 포인트**는 `Critical` 구역에서 1~2개를 고른다 (A·P가 모두 큰 노드 = 시스템 피드백 중심).

# Objective
제3장의 14개 핵심 트렌드 간 **인과 강도**를 정량 평가(Cross-Impact)하고,
- **검증된 2×2 축**(B × D 가설을 cross-impact로 점검),
- **양 끝 라벨링**,
- **4분면 시나리오 backbone (Q1~Q4 모두)**,
- **Influence Diagram (DAG)**, **CLD (피드백)**, **레버리지 포인트**
를 산출한다.

# Hard Rules
1. **Cross-impact 평가는 14개 핵심 트렌드만** 사용 (`out/03-core-trends.md §3.1`의 14개).
2. 척도 = **0~3**. 자기 자신(대각선)은 평가하지 않음 (`-`).
3. 셀 점수는 페르소나 P1·P2·P3의 **암묵 평균** 관점 1개 값으로 입력
   (개별 페르소나 분산까지는 4장에서 다루지 않는다 — POC 효율).
4. **Driving / Dependent / Critical / Inert** 분류는 `Active sum (행 합)`과 `Passive sum (열 합)`의
   **중앙값(median)** 을 임계로 사용한다.
   - High A & Low P → **Driving**
   - High A & High P → **Critical (피드백 중심, 레버리지 후보)**
   - Low A & High P → **Dependent**
   - Low A & Low P → **Inert**
5. **2×2 축 후보 선정 절차**
   1. `Critical + Driving` 풀에서 후보를 뽑는다 (`Inert/Dependent`는 축이 아니라 결과 변수).
   2. 후보 중 **클러스터(A~F)가 다른 두 노드**를 짝지어 “서로 독립인” 축 페어를 만든다.
   3. **B × D 가설** (제3장 §3.4)이 이 절차로도 살아남는지 확인. 살아남으면 **확정**, 일부 노드가 다른 구역에 떨어지면 **축의 의미를 재정의**한다 (예: D 축을 “환경 일반”이 아니라 “DC 빌드 진폭”으로 좁힌다).
   4. 살아남지 않으면 새로운 축 페어를 제시하고 사유 작성.
6. **시나리오는 Q1~Q4 모두 전개** (3개만 쓰고 1개를 버리지 않는다 — POC에서는 분기 가능성을 모두 본다).
7. **DAG에는 P-2.2(Critical 피드백 중심)처럼 양방향 강결합 노드는 표시하되, 순환 엣지는 제거**한다.
   순환 정보는 4.5 CLD에서 명시.
8. **확률 사전 견적**(Q1~Q4 합 100%)을 4장 말미에 넣는다. 정식 확률·서사는 6장에서 확정한다.

# Task

## Step 1. Cross-Impact 14×14 평가
- `from` → `to` 매트릭스를 0~3 정수로 채운다.
- 행 합(Active = Driving 강도), 열 합(Passive = Dependency 강도)을 계산.
- Active vs Passive **산점도** + 4구역 (Driving / Dependent / Critical / Inert) 시각화 → `assets/04-active-passive-map.png`.
- Cross-impact **히트맵** → `assets/04-cross-impact-heatmap.png`.
- 코드: `scripts/04_cross_impact.py` (재현 가능, 매트릭스 데이터를 스크립트에 인라인).

## Step 2. B × D 가설 검증
- 제3장 §3.4의 후보 `B × D`가 cross-impact 결과에서 다음 두 조건을 만족하는지 확인:
  1. **B 축 대표 노드는 Driving 또는 Critical**일 것.
  2. **D 축 대표 노드는 다른 클러스터의 Driving 또는 Critical**일 것.
- 조건 충족 → 축 확정. 부분 충족 → **축 의미 재정의** + 어떤 노드가 axis-representative인지 명시.
- 미충족 → 대안 축 페어 제시 + 사유.

## Step 3. 양 끝 라벨링
- 각 축의 양 끝(`+ / -`)에 대해
  - 정의 한 줄, 트리거 신호 2~3개, 영향받는 14개 중 어느 것에 어떻게 작용하는지 매핑.

## Step 4. 4분면 시나리오 Backbone (Q1~Q4)
- 각 분면에 다음을 작성:
  - 가칭 시나리오명 (1~3 단어)
  - 1줄 요지 / 시작 트리거 / 진행 동학(어느 R·B 루프가 우세하게 도는지)
  - 14개 트렌드 매핑 (이 분면에서 각 트렌드가 어떤 모습인지 한 줄)
  - 투자 함의 (개인·기업 각 1~2 줄)
- 각 분면별로 `Driving` 노드의 위치(High/Low)와 `Dependent` 노드의 결과를 명시.

## Step 5. Influence Diagram (DAG)
- 임계치 ≥ 3 엣지를 우선 채택, 양방향 페어는 우세 방향(또는 conceptually-master 노드 우선)만 유지하여 **순환 없는 그래프**.
- 보강용으로 ≥ 2 엣지 일부를 추가할 수 있으나, **반드시 순환을 만들지 않을 것**.
- 출력: Mermaid `flowchart TD` + 한 줄 설명.
- Top 3 Drivers / Top 3 Most Affected 표기.

## Step 6. CLD (피드백 포함) + 레버리지 포인트
- DAG에서 **빠뜨렸던 양방향·순환 엣지** 를 재조립해 R/B 루프 식별.
- 최소 2~3개 루프 (R1/R2/B1) 작성. 각 루프에 노드 시퀀스, 메커니즘 해설, 시스템적 함의.
- **레버리지 포인트** 1~2개 = `Critical` 구역에서 A+P가 가장 큰 노드.
- DAG vs CLD **차이 한 줄 메모** 포함.

## Step 7. 시나리오 확률 사전 견적
- Q1~Q4 합 100%, 각 분면에 “현재 모멘텀 vs 6장 정식 평가 시 변동 가능성” 한 줄 사유.

# Output Format (out/04-backbone.md)
1. YAML 메타 + “한눈에 보기” (Active-Passive 4구역 요약 + B×D 검증 결론 + 4 시나리오 한 줄).
2. §4.1 Cross-Impact 매트릭스(축약 표 또는 첨부 이미지) + Active/Passive 표 + 4구역 분류.
3. §4.2 B × D 가설 검증 결과.
4. §4.3 2×2 축 양 끝 라벨링.
5. §4.4 4분면 시나리오 backbone (Q1~Q4).
6. §4.5 Influence Diagram (DAG, Mermaid).
7. §4.6 CLD (Mermaid) + 루프 해설 + 레버리지 포인트.
8. §4.7 시나리오 확률 사전 견적.
9. §4.8 다음 단계로의 인계 (제5장 Trend Projection 입력 / 제6장 Scenario 본문 입력).
