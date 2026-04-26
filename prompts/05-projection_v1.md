# 제5장 — Trend Projection 프롬프트 (v2)

> **v1 → v2 변경 요지**
> 1. **4구역(Driving / Critical / Dependent / Inert)을 인식**해 처리 강도를 다르게 한다.
>    - Driving + Critical + Dependent → **풀 4블록 + 분면별 분기 메모**.
>    - Inert → **압축형** (Direction / Trajectory / Uncertainty + 한 줄 메모).
> 2. 각 4블록(Direction / Trajectory / Uncertainty / Link Drivers)이 **왜 분리해서 봐야 하는가**를 명시.
> 3. **분면별 분기 메모** 규칙 추가 — Driving/Critical/Dependent는 Q1~Q4에서 다르게 나타나는 부분을 1줄로 명시.
> 4. **그룹 정렬은 4구역 → 도메인** 순(Tech → Econ → Pol → Social → Env). v1의 도메인-only 정렬은 4구역 정보 손실.

# Objective
제3장의 14개 핵심 트렌드 각각의 **3~7년 전개 패턴**을 동일 양식으로 정리한다.  
6장 시나리오 본문 작성 직전, 트렌드 단위 “예측 카드”를 만들어 6장이 자연스럽게 인용·차용하도록 한다.

# 4 블록의 의미 (왜 4개인가)

| 블록 | 답하는 질문 | 라벨 옵션 | 분리 이유 |
|------|-------------|-----------|----------|
| **Future Direction** | 어디로 향하는가 (질적) | Increase / Decrease / **Transform** / Maintain | “양 증가”와 “형태 변형”은 투자 함의가 완전히 다름 |
| **Growth Trajectory** | 어떤 속도·곡선으로 가는가 | Rapid / Moderate / **Volatile** / Slow | 방향이 같아도 곡선이 다르면 진입 시점·포지션 사이즈가 달라짐 |
| **Uncertainty Dynamics** | 시간이 갈수록 더 알 수 있게 되는가, 더 모호해지는가 | 증가 / 유지 / 감소 + 한 줄 사유 | 시나리오 플래닝의 핵심 차별점. **증가** = 분기 변수 무게 ↑, **감소** = 베이스라인화 |
| **Link Drivers (STEEP)** | 어떤 다른 도메인 변수가 이 트렌드를 밀거나 누르는가 | 3~6 bullet (STEEP 다른 도메인) | 4장 cross-impact 숫자를 인과 서사로 옮긴 것 |

# Hard Rules
1. **STEEP 5도메인만**(Social, Tech, Econ, Env, Pol). Values 도메인은 사용하지 않는다.
2. **그룹 정렬**: 1순위 = 4구역 (Driving → Critical → Dependent → Inert), 2순위 = 도메인 (Tech → Econ → Pol → Social → Env).
3. **처리 강도**:
   - **Driving / Critical / Dependent (총 8개)** → 풀 4블록 + **분면별 분기 메모(Q1~Q4)**.
   - **Inert (총 6개)** → 압축형. Direction / Trajectory / Uncertainty + “이 트렌드는 ○○의 결과 변수” 한 줄.
4. **분면별 분기 메모**는 다음과 같이 1줄씩 (한 줄에 양 끝의 모습만 비교해도 OK):
   - `Q1 Pax Silica (B+/D−)` / `Q2 Bunkered AI (B+/D+)` / `Q3 Green Concord (B−/D+)` / `Q4 Open Boom (B−/D−)`
   - 4분면이 동일하면 “4분면 차이 없음 — 베이스라인” 한 줄로 마무리.
5. **모순 가능성**(한 트렌드가 두 시나리오에서 반대 방향으로 전개되는 등)은 분기 메모에 명시.
6. **Link Drivers의 ID 표기**: `T-1.1`, `Env-1.2` 등 §3.1의 ID를 그대로 사용 — 4장의 cross-impact 매트릭스와 1:1 대응되도록.

# Task

## Step 1. 14개 트렌드 카드 작성
- §5.1 Driving (1개): Env-1.2.
- §5.2 Critical (6개): P-3.1, T-1.1, P-2.2, P-4.2, P-3.2, T-2.2 (4구역 표 정렬 순).
- §5.3 Dependent (1개): P-5.1.
- §5.4 Inert (6개): E-2.2, T-4.2, S-4.1, E-3.2, Env-2.2, Env-3.2 (압축 표 1개).

## Step 2. Top 5 강조
- 4장 Active/Passive 결과 + 본 장의 분기 메모 강도를 종합해, **시나리오 작성에 가장 영향력 있는 5개**를 선정.
- 각 항목에 “6장에서 어떻게 활용되는가” 한 줄.

## Step 3. 6장 인계
- 5장 → 6장 연결 한 단락: 시나리오 본문에서 어떤 카드를 어떻게 인용하는지.

# Output Format (out/05-projection.md)
1. YAML 메타 + 한눈에 보기 (4구역별 카운트, Top 5, Direction 분포 등).
2. §5.0 4구역별 처리 강도 표.
3. §5.1 Driving (Env-1.2) — 풀 카드.
4. §5.2 Critical (6) — 풀 카드 6장.
5. §5.3 Dependent (P-5.1) — 풀 카드.
6. §5.4 Inert (6) — 압축 표.
7. §5.5 Top 5 강조 + 6장 인계.
