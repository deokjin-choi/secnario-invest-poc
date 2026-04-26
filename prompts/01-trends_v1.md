# 제1장 — 주요 트렌드 분석 프롬프트 (v1)

> 사용 시 `prompts/00-system_v1.md`를 먼저 입력한 뒤 본 프롬프트를 입력한다.

# Objective
업로드된 `references/` 내 AI 산업 자료를 기반으로,
AI 산업의 중장기 투자 시나리오 플래닝을 위한 **구조화된 트렌드 분석**을 수행한다.

# Task
**STEEP** (Social, Technological, Economic, Environmental, Political) 프레임에 따라
각 도메인별로 **5개의 Cluster**를 도출하고,
각 Cluster별로 **2개의 Factor**를 정의한다. (5 도메인 × 5 Cluster × 2 Factor = 약 50개)

---

# Source Map (현재 `references/`)
세 자료의 **성격·강점·한계**를 모델이 인지한 상태에서 트렌드를 도출하도록 한다.
서로 다른 관점을 가진 자료들이므로, **한 자료에 끌려가지 말 것**.

| 코드 | 자료 | 성격 | 강한 영역 (STEEP) | 약한 영역 / 주의 |
|------|------|------|----------------------|-------------------|
| `Mirae` | 미래에셋 — *AI 현황 보고서* (2025-09, 한국어) | 증권사 리서치, 풀스택 패권·기업 분석 위주 | T(기술 패권·인프라), E(자본·기업), P(미·중·소버린), S(고용 충격) | 정량 1차 출처 약함, Environmental 비중 제한 |
| `OECD` | OECD — *AI VC Investment Report* (2026-02, ~2025 데이터, 영문) | 정책 브리프, 정량 통계 | E(VC 자본 흐름·국가별), T/E(IT 인프라 투자), P(국가 정책 비교) | Social·Environmental 거의 다루지 않음 |
| `Stanford` | Stanford HAI — *AI Index Report 2026* (영문) | 연례 인덱스, 광범위 메타 데이터 | T(성능·R&D), S(공공 인식·교육·고용), P(거버넌스·소버린), E(경제 임팩트) | Environmental 일부만, 산업 경쟁사 시각은 적음 |
| `general` | 위 자료에 없는 일반 지식 사용 시 표기 | — | — | 가능한 한 위 자료로 대체하고 불가피한 경우만 사용 |

## Source Triangulation 규칙
- **Strong**: Factor의 근거가 위 자료 **2개 이상**에서 명시적으로 확인됨.
- **Single**: **1개 자료**에서만 확인 → "단일 출처(검증 필요)" 로 메모.
- **General**: 자료 외 일반 지식에 의존 → "general — 출처 보강 필요" 로 메모.
- 각 Factor 출력에 **Source Tag**를 반드시 붙인다 (아래 Output Format 참조).

## Environmental 도메인 가드
- 자료에서 Environmental(전력·탄소·자원·기후) 관련 직접 근거가 부족할 수 있다.
- 그래도 클러스터 5개를 **억지로 채우려 하지 말 것**.
  - 자료 근거가 부족한 클러스터는 `general`로 표기하고, 가능하면 **3~4개로 축소**해도 된다.
  - 이때 본문에 “자료 보강 권장: (어떤 종류의 자료가 더 필요한가)” 한 줄 메모.

---

# Instructions

## 1. 데이터 기반 원칙
- 반드시 업로드된 보고서 내용을 우선 기반으로 분석한다.
- 근거가 불명확한 경우 “추정” / “일반적으로 알려진 바” 로 명시.
- 인용·수치는 자료에 실제로 있는 것만 사용. **존재하지 않는 통계 생성 금지**.

## 2. 구조 요구사항
각 도메인(S, T, E, E, P)에 대해 아래 구조로 작성:

[Domain]
1) Cluster 1: (클러스터명)
   - Cluster Source Tag: [Mirae | OECD | Stanford | general] — Strong / Single / General
   - Factor 1: (요인명)
     - Description: (2~3문장 — 원인 / 영향 / 시나리오적 함의)
     - Source Tag: [Mirae | OECD | Stanford | general] — Strong / Single / General
     - Source Note: (어느 자료의 어느 섹션·맥락에서 비롯되었는지 한 줄)
   - Factor 2: (요인명)
     - Description: ...
     - Source Tag: ...
     - Source Note: ...
2) Cluster 2: ...

## 3. 분석 기준
- Cluster: **거시 트렌드 단위** (예: AI 인프라 재편, 데이터·전력 병목, AI 거버넌스 정착 등)
- Factor: Cluster를 구성하는 **구체적 동인** (예: 데이터센터 전력 수요 급증, 자국 우선 보조금 확대 등)
- Description에는 반드시 다음 포함:
  1) 원인(왜 발생하는가)
  2) 영향(무엇을 변화시키는가)
  3) 시나리오적 함의(왜 중요한가, 어떤 분기 가능성이 있는가)

## 4. 편향 가드 (Source Map과 함께 점검)
- 자본·VC 흐름 트렌드만 비대해지면 → `OECD`에 끌렸을 가능성 점검.
- 미·중 패권/특정 기업 사례에 몰리면 → `Mirae`에 끌렸을 가능성 점검.
- 거버넌스·여론·교육에만 몰리면 → `Stanford`에 끌렸을 가능성 점검.
- 한 도메인에 같은 출처만 반복되면 다른 자료에서 보완할 수 있는지 확인.

## 5. 스타일 가이드
- 분석적 보고서 톤 유지, 인과관계 중심.
- 모호한 표현 지양.

## 6. Output Format
- 마크다운 계층 구조로 출력.
- 결과는 `out/01-trends.md`의 섹션 구조와 호환되도록 작성.
- 마지막에 **Coverage 요약**을 추가:
  - 자료별 활용 빈도 (Mirae / OECD / Stanford / general 각각 몇 개의 Factor에 반영되었는가)
  - Single·General 표기된 Factor 수 (검증 필요 후보 리스트)
  - Environmental 도메인 클러스터 수 (5개 미만이면 사유)
