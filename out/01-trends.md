---
chapter: 1
title: 주요 트렌드 분석
status: 진행            # 1차 초안 — 출처 검증/보강 필요
source_prompts:
  - prompts/00-system_v1.md
  - prompts/01-trends_v1.md
references:
  - references/20250910_미래에셋_AI 현황 보고서.pdf
  - references/OECD AI VC Investment Report.pdf
  - references/stanford ai_index_report_2026.pdf
updated: 2026-04-26
note: |
  사전 정의된 시스템 프롬프트(prompts/00-system_v1.md)와
  1장 트렌드 프롬프트(prompts/01-trends_v1.md)를 그대로 사용한 1차 초안.
  이후 평가·시나리오 단계에서 출처(특히 Single 표기 항목)를 1회 더 검증할 것.
---

# 제1장 — 주요 트렌드 분석

> AI 산업과 거시 환경(**STEEP**)에서 **클러스터 → 팩터** 계층으로 트렌드를 구조화한다.  
> 진행 체크리스트: `poc-flow-refer.md` → 제1장

## 1.1 분석 프레임 (STEEP)

- 도메인: Social, Technological, Economic, Environmental, Political (5개)
- 권장 규모: 도메인당 5 Cluster × 2 Factor (전체 약 50 Factor)
- **자료 활용 가이드**: `prompts/01-trends_v1.md`의 **Source Map / Source Triangulation** 규칙을 따른다.
  - 각 Factor에 **Source Tag** `[Mirae | OECD | Stanford | general]` 와 **Strong / Single / General** 표기.
  - Environmental 도메인은 자료가 부족하면 클러스터 수를 줄이고 "자료 보강 권장" 메모.

## 1.2 도메인별 클러스터·팩터

### Social (5 Clusters × 2 Factors)

- **S-1. 일·고용 구조 변화 (AI 고용 충격)** — Cluster Source Tag: Mirae+Stanford — Strong
  - **S-1.1**: 화이트칼라·주니어 직무의 자동화 가속
    - Description: 코딩·고객 응대 등 **구조화된 화이트칼라 작업**부터 AI 대체가 진행 중. 원인은 GenAI/에이전트의 능력 향상과 비용 하락. 영향은 신규 채용 축소와 직급 피라미드의 하단부 압축. 시나리오적 함의는 “신규·청년 노동 기회”가 시나리오 분기를 가르는 핵심 사회 변수.
    - Source Tag: Stanford+Mirae — **Strong**
    - Source Note: Stanford AI Index 2026 *Economy* — 22~25세 SW 개발자 고용 약 -20%, 1/3 기업 인력 감축 예상 / Mirae *I. AI와 사회 변화 — 고용충격*.
  - **S-1.2**: AI 활용 노동의 생산성 격차 확대
    - Description: 분야별 생산성 향상은 14~50%까지 보고되나, 이 이득은 **AI를 능숙히 쓰는 인력**에 비대칭적으로 귀속. 영향은 동일 직군 내 임금·평가 격차 확대. 시나리오적 함의는 사회 안전망·재교육이 따라가는지에 따라 “포용적 성장” vs “양극화” 분기.
    - Source Tag: Stanford — **Single**
    - Source Note: Stanford *Economy*, productivity gains 14~26% (CS/SE), 50% (marketing).

- **S-2. 인공지능의 대중화·일상화** — Cluster Source Tag: Stanford — Strong
  - **S-2.1**: GenAI의 역사적 침투 속도 (3년 내 53%)
    - Description: GenAI는 PC·인터넷보다 빠르게 인구 침투 53%에 도달. 원인은 무료/저비용 진입과 모델 능력 급상승. 영향은 광범위한 소비자 행동·소프트웨어 인터페이스 재편. 시나리오적 함의는 **수요 측 동인**이 제도/규제 속도보다 빠를 때 발생할 수 있는 사회적 마찰의 전조.
    - Source Tag: Stanford — **Single**
    - Source Note: Stanford *Top Takeaways* #8 / *Economy* Ch.4 highlights.
  - **S-2.2**: GenAI 소비자 잉여 급증 (미국 ~$172B/년)
    - Description: 무료·저가 도구 기반 소비자 잉여가 1년 새 54% 증가. 원인은 가격 대비 효용의 비대칭. 영향은 “지표상 GDP에 잡히지 않는 가치”가 누적되며 생산성 통계와 체감의 괴리. 시나리오적 함의는 **가치 포착(value capture)** 의 주체(빅테크 vs 사용자 vs 정부)가 시나리오를 가른다.
    - Source Tag: Stanford — **Single**
    - Source Note: Stanford *Economy*, consumer surplus $172B, median per-user value tripled.

- **S-3. 신뢰·여론의 양극화** — Cluster Source Tag: Stanford — Strong
  - **S-3.1**: 전문가–일반 대중의 인식 격차
    - Description: AI의 일자리 영향에 대해 전문가 73%가 긍정적인 반면 일반 대중은 23%로, 약 50pt 격차. 원인은 정보 비대칭과 대체 우려. 영향은 정책 수용성 저하와 ‘기술 vs 사회’ 균열. 시나리오적 함의는 정치 시나리오의 진폭(규제 강화 vs 완화)을 좌우.
    - Source Tag: Stanford — **Single**
    - Source Note: Stanford *Top Takeaways* #15 / *Public Opinion* Ch.9.
  - **S-3.2**: 낙관과 불안의 동시 상승
    - Description: AI 혜택 인식(55→59%)과 동시에 “AI가 불안하다” 비율(52%)이 함께 상승. 원인은 가치와 위협이 같은 도구에서 동시에 발생. 영향은 양가적 여론이 정책 변동성을 키움. 시나리오적 함의는 **정치적 진자 운동** 가능성을 시나리오에 반영해야 함을 시사.
    - Source Tag: Stanford — **Single**
    - Source Note: Stanford *Public Opinion* Ch.9 highlights.

- **S-4. 정서·관계의 AI 의존** — Cluster Source Tag: Stanford — Single
  - **S-4.1**: AI 컴패니언/동반자 사용 확산
    - Description: 정서 교감 가능한 AI 사용이 빠르게 확산되며 입법·소송 사례 증가. 원인은 외로움·접근성 격차의 사회적 충족. 영향은 인간관계의 재정의와 광고·구독 비즈니스의 신모델. 시나리오적 함의는 “인간-기계 공생” vs “정서적 위기”의 분기.
    - Source Tag: Stanford — **Single**
    - Source Note: Stanford *Policy & Governance* Ch.8 — Utah HB 452, CA SB 243(companion bots), Aug 2025 companion lawsuits.
  - **S-4.2**: 청소년·청년의 정신건강 리스크
    - Description: 컴패니언 AI 관련 청소년 자살 사건이 입법 검토를 촉발. 원인은 안전장치 부재·중독성 설계. 영향은 강한 ‘아동·청소년 보호’ 입법 흐름. 시나리오적 함의는 사회 신뢰 시나리오의 핵심 분기점.
    - Source Tag: Stanford — **Single**
    - Source Note: Stanford *Policy* Ch.8 — “AI Companion Lawsuits Prompt Renewed Scrutiny” (Aug 2025).

- **S-5. 교육·학습 행태 변화** — Cluster Source Tag: Stanford — Single
  - **S-5.1**: 학생·교육 현장의 GenAI 표준화
    - Description: 미국 고·대학생의 80% 이상이 학업에 GenAI 사용. 원인은 도구 보편화와 학습 곡선 단축. 영향은 평가·과제 체계의 재설계 압력. 시나리오적 함의는 인적 자본의 형성 방식 변화 → 장기 산업 경쟁력의 결정적 변수.
    - Source Tag: Stanford — **Single**
    - Source Note: Stanford *Education* Ch.7 highlights.
  - **S-5.2**: AI 스킬 숙련의 신흥국 약진
    - Description: AI 엔지니어링 스킬은 UAE·칠레·남아공 등에서 가장 빠르게 성장. 원인은 정책적 의지·낮은 진입장벽·LinkedIn 등 글로벌 학습 자원. 영향은 AI 인재 분산. 시나리오적 함의는 **인재 흐름**이 미·중 외 제3블록 형성에 기여할 수 있음.
    - Source Tag: Stanford — **Single**
    - Source Note: Stanford *Top Takeaways* #13, *Education* Ch.7.

---

### Technological (5 Clusters × 2 Factors)

- **T-1. 모델 성능 프런티어와 수렴** — Cluster Source Tag: Stanford+Mirae — Strong
  - **T-1.1**: 미·중 프론티어 모델 성능 격차 축소
    - Description: 2025년 들어 미·중 최상위 모델이 여러 차례 선두를 교대(2026.03 기준 미국 모델 우위 약 2.7%p). 원인은 중국의 인재·자체 학습 인프라 강화. 영향은 단일 표준이 아닌 **이중 표준 생태계** 가능성. 시나리오적 함의는 “표준화·협력” vs “블록화” 시나리오 결정 변수.
    - Source Tag: Stanford+Mirae — **Strong**
    - Source Note: Stanford *Top Takeaways* #2 / Mirae *VII. 중국 AI*.
  - **T-1.2**: 효율화·오픈소스 모델의 약진
    - Description: 작은 모델로 큰 모델 성능을 따라잡는 사례 누적(예: OLMo 3.1, GPN-Star). 원인은 데이터 큐레이션·후처리·증류 기술의 진보. 영향은 진입장벽 하락과 멀티 벤더 경쟁. 시나리오적 함의는 **빅테크 독점**과 **분산 혁신**의 균형을 가르는 핵심 변수.
    - Source Tag: Stanford+Mirae — **Strong**
    - Source Note: Stanford *R&D* Ch.1 — open-source 5.6M projects, OLMo 3.1 / Mirae *II. 주류 연구방향* — 추론·RL 스케일링.

- **T-2. 컴퓨트·인프라 구심력 (Compute Centrality)** — Cluster Source Tag: Stanford+Mirae — Strong
  - **T-2.1**: 글로벌 AI 컴퓨트 연 3.3배 증가 (≈17.1M H100-eq)
    - Description: 2022년 이후 글로벌 학습/추론 컴퓨트가 연 3.3배 성장. NVDA 60%+ 점유, Google·Amazon이 잔여 다수, Huawei가 소수 점유. 원인은 모델 스케일링·추론 수요. 영향은 **자본·전력 의존도**의 구조적 상승. 시나리오적 함의는 자본·전력 가용성이 시나리오의 가속 페달 역할.
    - Source Tag: Stanford — **Single**
    - Source Note: Stanford *R&D* Ch.1 — Global AI compute capacity 3.3×/yr; 17.1M H100-eq.
  - **T-2.2**: 칩 공급망의 TSMC 단일 의존 + 미국 데이터센터 집중
    - Description: 사실상 모든 선도 AI 칩이 대만 TSMC 1개 파운드리에서 제조, 미국이 5,427개 DC로 글로벌 1위 보유. 원인은 첨단 노드 독점·하이퍼스케일러 집중 투자. 영향은 지정학적 리스크 + 에너지 집중. 시나리오적 함의는 **TSMC 위기/대만 해협 이슈**가 시나리오 트리거 사건으로 작동.
    - Source Tag: Stanford+Mirae — **Strong**
    - Source Note: Stanford *Top Takeaways* #3, *R&D* Ch.1 / Mirae *VIII. 엔비디아*.

- **T-3. AI 에이전트화·자율 실행** — Cluster Source Tag: Stanford+Mirae — Strong
  - **T-3.1**: 에이전트 능력의 비선형 도약 (OSWorld 12% → ~66%)
    - Description: 1년 새 컴퓨터 작업 자동화 능력이 5배 이상 도약. 원인은 도구 사용·계획 능력 결합. 영향은 BPO·운영 자동화의 본격적 침투. 시나리오적 함의는 “AI 에이전트 주도 자동화 사회” vs “감독 하 보조 도구” 시나리오의 핵심 분기 변수.
    - Source Tag: Stanford+Mirae — **Strong**
    - Source Note: Stanford *Top Takeaways* #4 / Mirae *IX. 테슬라*, *X. 팔란티어* — 에이전트·온톨로지.
  - **T-3.2**: 가정·물리 환경에서의 능력 한계 (RLBench 89.4% vs 가정 12%)
    - Description: 통제 시뮬레이션에서는 90% 가까운 성능을 보이지만 가정 등 비정형 환경 성공률은 12%. 원인은 분포 외 일반화·물리 인터랙션 난이도. 영향은 로봇 상용화 시점의 지연 가능성. 시나리오적 함의는 “물리 AI 상용화” 시점의 프로젝션이 시나리오를 가른다.
    - Source Tag: Stanford — **Single**
    - Source Note: Stanford *Top Takeaways* #5; *Technical Performance* Ch.2.

- **T-4. 풀스택 헤게모니·AI ↔ 물리 결합** — Cluster Source Tag: Mirae — Strong
  - **T-4.1**: 풀스택(반도체–전력–데이터–모델–앱) 통합 경쟁
    - Description: 단일 레이어가 아닌 **반도체+전력+데이터+모델+운영 시스템 전체**를 장악하려는 경쟁이 가속. 원인은 한 레이어의 병목이 전체 가치를 좌우하기 때문. 영향은 거대 기업·국가 단위 통합 투자 확대. 시나리오적 함의는 “수직 통합 vs 수평 분산”의 산업 구조 분기.
    - Source Tag: Mirae — **Single**
    - Source Note: Mirae *결론 — 풀 스택 패권의 시대*.
  - **T-4.2**: AI–물리 세계 결합(자율주행·휴머노이드·온톨로지)
    - Description: 로보택시·휴머노이드 로봇·기업 운영 통합(팔란티어 온톨로지) 등 AI가 **물리·운영 영역**으로 확장. 원인은 모델 능력 + 센서·액츄에이터 비용 하락. 영향은 자본·서비스 산업의 재편. 시나리오적 함의는 **물리 AI 시점**이 자산군별 수혜 순위를 결정.
    - Source Tag: Stanford+Mirae — **Strong**
    - Source Note: Stanford *Economy* — Physical Intelligence $5.6B / Mirae *IX·X. 테슬라·팔란티어*.

- **T-5. AI 안전·평가 체계의 한계** — Cluster Source Tag: Stanford — Single
  - **T-5.1**: 책임 AI(RAI) 평가가 능력 발전을 따라가지 못함
    - Description: 능력 벤치마크는 보고되지만 안전·공정성 등 RAI 보고는 산발적. AI 사고는 233 → 362건으로 급증. 원인은 평가 표준의 부재·기업 자율 보고. 영향은 규제 충돌·소송 리스크. 시나리오적 함의는 “신뢰 우선 통제” 시나리오의 진입 트리거.
    - Source Tag: Stanford — **Single**
    - Source Note: Stanford *Top Takeaways* #6, *Responsible AI* Ch.3.
  - **T-5.2**: RAI 차원 간 트레이드오프(개선 시 다른 차원 악화)
    - Description: 안전·공정성·정확성·프라이버시는 동시에 개선되지 않으며, 특정 차원을 강화하면 다른 차원이 악화. 원인은 학습·정렬 기법의 구조적 제약. 영향은 “단일 모델로 모든 책임 요건 충족 불가”라는 구조적 한계. 시나리오적 함의는 **인증·평가 산업** 자체가 신규 산업으로 부상.
    - Source Tag: Stanford — **Single**
    - Source Note: Stanford *Responsible AI* Ch.3.10 — Tradeoffs Across RAI Dimensions.

---

### Economic (5 Clusters × 2 Factors)

- **E-1. AI 자본 집중·메가딜 가속** — Cluster Source Tag: OECD+Stanford — Strong
  - **E-1.1**: AI VC 비중 61% / 메가딜이 자본의 73%
    - Description: 2025년 글로벌 VC의 61%(USD 258.7B)가 AI로 흘러가며, USD 100M 초과 메가딜이 자본의 73%, USD 1B 초과 딜이 거의 절반을 차지. 원인은 인프라 자본 집약성 + 후기 단계 베팅 집중. 영향은 초기 단계 다양성 축소. 시나리오적 함의는 **자본 분포의 양극화**가 산업 구조 시나리오를 가른다.
    - Source Tag: OECD — **Single**
    - Source Note: OECD *Key messages*, mega deals 73%, USD 100M+; deals USD 1B+ ≈ 절반.
  - **E-1.2**: 미국으로의 압도적 자본 집중 (≈75%)
    - Description: 미국 AI 기업이 전체 AI VC의 약 75%(USD 194B)를 흡수, EU27·중국·영국이 각각 5~6%. 원인은 인재·인프라·자본의 정의 효과. 영향은 **미국 의존도 심화**. 시나리오적 함의는 정치/공급망 시나리오에서 “단극” vs “복수 허브” 분기.
    - Source Tag: OECD+Stanford — **Strong**
    - Source Note: OECD *Key messages* / Stanford *Top Takeaways* #7 — US private investment $285.9B (2025).

- **E-2. 빅테크 CapEx·인프라 군비경쟁** — Cluster Source Tag: Stanford+Mirae — Strong
  - **E-2.1**: 데이터센터 빌드아웃 ($500B Stargate, Google $40B Texas 등)
    - Description: 2025년 발표된 데이터센터 투자 계획만 수천억 달러 단위. 원인은 학습/추론 컴퓨트 수요 폭증. 영향은 자본·에너지·부지의 동시 압력 + 1차 산업(전력·건설·HVAC)으로의 파급. 시나리오적 함의는 **CAPEX 사이클**이 매크로 자본·금리에 민감하게 반응.
    - Source Tag: Stanford+Mirae — **Strong**
    - Source Note: Stanford *Economy* 4.1 timeline (Stargate $500B, Anthropic $13B, OpenAI $40B / $300B Oracle) / Mirae *IV. AI 군비경쟁*.
  - **E-2.2**: NVDA 시총 $4T·인프라 단일 사슬 (CUDA·3계층 네트워크)
    - Description: NVDA가 첫 시총 $4T 기업 도달, CUDA·NVLink·Spectrum-X로 GPU↔서버↔DC 전 계층을 장악. 원인은 SW–HW 통합 락인. 영향은 AI 가치사슬의 단일 의존. 시나리오적 함의는 “경쟁사 부상”·“반독점 규제”가 시나리오 분기 트리거.
    - Source Tag: Stanford+Mirae — **Strong**
    - Source Note: Stanford *Economy* July 9, 2025 / Mirae *VIII. 엔비디아 — CUDA 생태계*.

- **E-3. 노동 시장의 세대·직군 비대칭 충격** — Cluster Source Tag: Stanford — Single
  - **E-3.1**: 22~25세 SW 개발자 고용 약 -20%
    - Description: 생산성 이득이 측정된 분야(소프트웨어 등)에서 **신규(주니어) 채용 감소**가 가장 두드러짐. 원인은 AI가 “모방 가능한 신규 작업”을 우선 대체. 영향은 진입 코호트 단절. 시나리오적 함의는 “노동력 재교육·재배치”가 따라가는지에 따른 사회·정치 시나리오 변화.
    - Source Tag: Stanford — **Single**
    - Source Note: Stanford *Economy* Ch.4 highlights / *Top Takeaways* #9.
  - **E-3.2**: 1/3 기업이 향후 1년 내 인력 감축 예상
    - Description: 서비스 운영·공급망·SW 엔지니어링 분야에서 **선행 기대치**가 가장 높음. 원인은 에이전트·자동화 도입 계획. 영향은 “기대 vs 실제” 격차의 변동성. 시나리오적 함의는 **고용 인플레이션·임금**과 결합되어 거시 변동성을 키움.
    - Source Tag: Stanford — **Single**
    - Source Note: Stanford *Economy* Ch.4 highlights #8.

- **E-4. 생산성·소비자 가치의 비대칭** — Cluster Source Tag: Stanford+Mirae — Strong
  - **E-4.1**: 분야별 생산성 14~50%, 그러나 **고판단 영역은 약함**
    - Description: 고객지원 14~15%, SW 개발 26%, 마케팅 50% 수준의 생산성 향상이 보고되나 깊은 추론 작업에서는 효과가 약하거나 부정적. 원인은 작업 구조화 가능성. 영향은 산업·직군별 ROI 격차. 시나리오적 함의는 ROI가 큰 영역(인프라·BPO)이 자산 시나리오의 1차 수혜.
    - Source Tag: Stanford — **Single**
    - Source Note: Stanford *Economy* Ch.4 highlights #9.
  - **E-4.2**: 소비자 가치 폭증과 모델 공급자 마진 압박의 공존
    - Description: 소비자 잉여는 급증(미국 ~$172B/년)하지만 모델 공급자 가격 경쟁과 추론 비용 부담으로 마진 확보가 쉽지 않음. 원인은 모델 무료/프리티어 + 컴퓨트 비용 상승의 동시 작동. 영향은 “돈을 버는 곳 vs 가치가 발생하는 곳”의 어긋남. 시나리오적 함의는 **밸류 체인 어디에 자본을 투입할지**의 핵심 의사결정 포인트.
    - Source Tag: Stanford+Mirae — **Strong**
    - Source Note: Stanford *Economy* — consumer surplus / Mirae *VIII. 엔비디아* — 인프라 마진 vs 모델사 마진 비교.

- **E-5. AI 산업·시장 구조의 양극화** — Cluster Source Tag: OECD — Strong
  - **E-5.1**: 후기 단계로의 자본 쏠림 (early avg $11.8M vs late $131M)
    - Description: 딜 수에서는 초기 단계가 75%지만 자본의 절반 이상은 후기 단계로 흐름. 원인은 “승자에게 더”의 베팅 구조. 영향은 초기 혁신 다양성 약화. 시나리오적 함의는 “분산 혁신”·“대표주 집중” 시나리오 분기 신호.
    - Source Tag: OECD — **Single**
    - Source Note: OECD report — early-stage 75% of deal count, mega deals 73% of value.
  - **E-5.2**: AI VC가 IT 인프라/호스팅으로 집중 (USD 109.3B in 2025)
    - Description: 산업별로 IT 인프라·호스팅 분야의 AI VC가 압도적 1위(누적 USD 256.1B, 2012–25). 원인은 컴퓨트 자본 집약. 영향은 **‘곡괭이 판매’ 사업모델의 우위**. 시나리오적 함의는 자본이 인프라 → 모델 → 응용 순으로 흐르는 사이클을 시나리오에 반영.
    - Source Tag: OECD — **Single**
    - Source Note: OECD report — IT infrastructure & hosting AI VC.

---

### Environmental (4 Clusters × 2 Factors)

> **자료 보강 권장**: Environmental 도메인은 자료에서 직접 근거가 풍부한 영역이 **에너지·전력 인프라**에 편중. 기후·물·자원 순환 등은 자료 1건에서만 다뤄지는 경우가 많아 **5번째 클러스터**는 무리하게 추가하지 않음.

- **Env-1. 데이터센터 전력·그리드 병목** — Cluster Source Tag: Stanford+Mirae — Strong
  - **Env-1.1**: AI 데이터센터 전력 용량 29.6 GW (NY주 피크급)
    - Description: 글로벌 AI DC 전력 용량이 한 주(state) 단위 피크 수요와 비교되는 수준으로 상승. 원인은 학습·추론 동시 수요 + 클러스터 거대화. 영향은 송배전·발전 부족과 가격 변동성. 시나리오적 함의는 **전력 가용성**이 AI 발전 속도의 강제 페이서가 됨.
    - Source Tag: Stanford+Mirae — **Strong**
    - Source Note: Stanford *Top Takeaways* #10 / Mirae *V. 에너지와 그리드 — Electric Shock*.
  - **Env-1.2**: 신규 DC 프로젝트의 거대화 (100MW 초과 48%, GW급 4%)
    - Description: 신규 DC 약 절반이 100MW 초과, 4%는 이미 GW 도달. 원인은 LLM 학습 클러스터의 인접성·고밀도 요구. 영향은 입지·수도·송전 인프라의 재설계 필요. 시나리오적 함의는 “전력·부지 가용 지역”이 AI 산업 지도를 다시 그림.
    - Source Tag: Mirae — **Single**
    - Source Note: Mirae *V. 에너지와 그리드*, SemiAnalysis 설문 인용.

- **Env-2. 탄소·수자원 발자국** — Cluster Source Tag: Stanford — Single
  - **Env-2.1**: 학습 단계 탄소 배출 누적 (Grok 4 ≈ 72,816 tCO₂e)
    - Description: 단일 모델 학습으로도 도시 단위에 비견되는 탄소 발자국. 원인은 학습 컴퓨트의 가파른 증가. 영향은 ESG 리스크와 탄소 규제 노출. 시나리오적 함의는 **탄소 가격·규제 강도**가 AI 모델 경제성을 흔들 수 있음.
    - Source Tag: Stanford — **Single**
    - Source Note: Stanford *R&D* Ch.1.4 / *Top Takeaways* #10.
  - **Env-2.2**: 추론 단계 수자원 사용 급증 (GPT-4o 추론수 ≈ 1,200만명 식수 추정)
    - Description: 학습뿐 아니라 **상시 추론**에서도 냉각수 소비가 큰 변수로 부상. 원인은 추론 트래픽 폭증 + 냉각 효율 한계. 영향은 “물 부족 지역의 DC 입지 제한”. 시나리오적 함의는 지역별 입지 경쟁이 심화.
    - Source Tag: Stanford — **Single**
    - Source Note: Stanford *R&D* Ch.1.4.

- **Env-3. 전력 인프라 재설계** — Cluster Source Tag: Mirae — Single
  - **Env-3.1**: 800V HVDC·액체냉각·온사이트 발전의 표준화 흐름
    - Description: 랙 전력 12kW → 120kW(>1MW)로 도약하면서 기존 12V AC/DC 변환·공랭 한계가 명확. 원인은 GPU 밀도와 TDP 폭증. 영향은 DC 자체가 “전원·냉각 산업 플랜트”로 재정의. 시나리오적 함의는 전력·냉각 부품 산업이 **2차 수혜군**으로 부상.
    - Source Tag: Mirae — **Single**
    - Source Note: Mirae *V. 에너지와 그리드 — Kyber 랙 / 800V HVDC*.
  - **Env-3.2**: 청정전력·SMR·신재생 PPA로의 직거래 확산
    - Description: AI 기업이 발전·저장(BESS) 자산과 직거래 PPA를 체결하는 흐름이 확산. 원인은 그리드 대기 시간·탄소 규제. 영향은 발전·유틸리티 산업과 AI 산업의 결합. 시나리오적 함의는 **AI 인접 발전·전력 인프라 자산**이 시나리오에서 별도의 투자 대상이 됨.
    - Source Tag: Mirae — **Single**
    - Source Note: Mirae *V. 에너지와 그리드 — 신재생/IPP/유틸리티 AI 언급도*.

- **Env-4. 효율성·저전력 기술 혁신** — Cluster Source Tag: Stanford+Mirae — Strong
  - **Env-4.1**: 알고리즘 효율 매년 약 3배 (동일 연산 대비 성능)
    - Description: 모델 알고리즘·학습 기법·프롬프팅·도구 사용 최적화의 누적으로 **추론 비용은 매년 약 1/10**로 감소. 원인은 RL·증류·MoE 등 후처리 기법의 발전. 영향은 일정 성능을 더 적은 자원으로 달성. 시나리오적 함의는 **에너지 제약 시나리오**에서도 일부 영역의 발전이 지속될 수 있음.
    - Source Tag: Mirae — **Single**
    - Source Note: Mirae *I. AI와 사회 변화 — 발전 속도* (Forethought 분석 인용).
  - **Env-4.2**: 모델 슬림화·소형 모델 약진(OLMo 3.1 Think 32B)
    - Description: Grok 4 대비 약 90배 적은 파라미터의 OLMo 3.1 Think 32B가 일부 벤치마크에서 동등 수준 성능. 원인은 큐레이션·디둡·프루닝의 진보. 영향은 엣지·온디바이스 AI의 확장. 시나리오적 함의는 **에너지 임계 시 분산형 추론**이 가능해지는 경로.
    - Source Tag: Stanford — **Single**
    - Source Note: Stanford *R&D* Ch.1 highlights #4.

---

### Political (5 Clusters × 2 Factors)

- **P-1. AI 주권(Sovereign AI)의 부상** — Cluster Source Tag: Stanford+Mirae — Strong
  - **P-1.1**: 국가 AI 전략 채택의 신흥국 가속
    - Description: 2024~25년 신규 AI 전략의 절반 이상이 신흥국. 원인은 “전략을 가져야 한다”는 정책 확산 효과. 영향은 정책 표준의 다양화. 시나리오적 함의는 **3극 이상 다극화** 시나리오의 정치적 토대.
    - Source Tag: Stanford — **Single**
    - Source Note: Stanford *Policy* Ch.8 highlights #1.
  - **P-1.2**: 국가 AI 슈퍼컴 인프라 격차 확대
    - Description: 유럽·중앙아시아의 국가 후원 AI 슈퍼컴 클러스터가 3 → 44개로 급증한 반면 남아시아·라틴아메리카·MENA는 한 자리 수. 원인은 재정 여력·전략 의지 격차. 영향은 모델 주권의 차등 실현. 시나리오적 함의는 AI 주권 시나리오의 **실현 가능 국가군**을 결정.
    - Source Tag: Stanford+Mirae — **Strong**
    - Source Note: Stanford *Policy* Ch.8.3 / Mirae *VI. 소버린 AI*.

- **P-2. 미국 vs EU 규제 분기** — Cluster Source Tag: Stanford+Mirae — Strong
  - **P-2.1**: EU AI Act 단계적 발효 + 회원국 자체 입법 (이탈리아 등)
    - Description: 2025년 2월 1차 금지 조항 발효, 8월 일반 목적 AI 의무 시행, 9월 이탈리아 회원국 법 통과. 원인은 위험 기반 접근의 제도화. 영향은 글로벌 규제의 사실상의 표준 효과(De facto standard). 시나리오적 함의는 “규범 기반 표준화” 시나리오의 핵심 동인.
    - Source Tag: Stanford+Mirae — **Strong**
    - Source Note: Stanford *Policy* Ch.8.1 timeline / Mirae *VI. 소버린 AI*.
  - **P-2.2**: 미국 연방 디레귤레이션 + 주(州) 규제 경쟁
    - Description: 연방은 “America’s AI Action Plan”·EO 등 규제 완화 방향, 캘리포니아 SB 53·텍사스 TRAIGA 등 주는 강화. 원인은 정치·산업 정책의 비대칭. 영향은 미국 내 **규제 패치워크**. 시나리오적 함의는 “주·연방 충돌” 자체가 단·중기 정책 변동성의 원천.
    - Source Tag: Stanford — **Single**
    - Source Note: Stanford *Policy* Ch.8.1, Ch.8.4 — state-level legislation, federal preemption attempts.

- **P-3. 미·중 기술 패권 경쟁의 구조화** — Cluster Source Tag: Stanford+Mirae — Strong
  - **P-3.1**: 모델 성능 격차 축소 + 산업 생태계 비대칭
    - Description: 모델 성능은 수렴 중이나 자본·인프라는 미국 우위, 산업 로봇·특허는 중국 우위. 원인은 양국의 정책·자원 차별화. 영향은 **상호 의존+상호 견제**의 이중 구조. 시나리오적 함의는 “기술 블록화” 시나리오의 정중앙 변수.
    - Source Tag: Stanford+Mirae — **Strong**
    - Source Note: Stanford *Top Takeaways* #2 / Mirae *VII. 중국 AI*.
  - **P-3.2**: 미국 대중국 수출통제 + 중국의 자력갱생(국가대표 모델)
    - Description: 미국 측 첨단 칩·장비 통제, 중국은 DeepSeek·Alibaba·Moonshot 등 자체 모델 개발과 대규모 국가 펀드(2025.03 USD 138B). 원인은 안보·산업 정책. 영향은 양 진영의 **이중 표준 생태계** 정착 가능성. 시나리오적 함의는 **수출통제·자원 규제**가 시나리오 트리거 사건.
    - Source Tag: Stanford+Mirae — **Strong**
    - Source Note: Stanford *Economy* 4.1 timeline (Mar 6 — China $138B fund) / Mirae *VII. 중국 AI*.

- **P-4. 데이터·공급망 주권화** — Cluster Source Tag: Stanford+Mirae — Strong
  - **P-4.1**: 데이터 현지화(Data Localization) 조치의 지역별 확산
    - Description: 동아시아·태평양 77건, 사하라이남 71건, 유럽·중앙아시아 66건 vs 북미 3건. 원인은 디지털 주권·산업 정책 의지. 영향은 글로벌 데이터 흐름의 분절. 시나리오적 함의는 “데이터 블록화”가 AI 모델 학습 비용·다양성에 직접 영향.
    - Source Tag: Stanford — **Single**
    - Source Note: Stanford *Policy* Ch.8.3 (Data Sovereignty) — highlights #3.
  - **P-4.2**: 반도체·하드웨어 동맹 (Pax Silica, TSMC-US 확장)
    - Description: 미국 주도 Pax Silica 선언(2025.12), TSMC 미국 공장 가동 시작(2025). 원인은 칩·DC 인프라 안보화. 영향은 **‘동맹 안의 분업·동맹 밖의 분리’** 구조 가속. 시나리오적 함의는 “기술 블록화” 시나리오의 강한 트리거.
    - Source Tag: Stanford+Mirae — **Strong**
    - Source Note: Stanford *Policy* Ch.8.1 (Dec 11 Pax Silica) / Mirae *VIII. 엔비디아·VI. 소버린 AI*.

- **P-5. 글로벌 거버넌스의 분열·재구성** — Cluster Source Tag: Stanford — Single
  - **P-5.1**: G7/UN의 다자 협력 시도 vs 일부 국가의 거리두기
    - Description: G7 공동성명·UN AI 거버넌스 패널 등 다자 시도와, Paris AI Action Summit에서의 미·영 미서명이 공존. 원인은 협력 인센티브와 자국 우선주의의 충돌. 영향은 표준의 **다중 트랙화**. 시나리오적 함의는 “글로벌 표준화” 진폭의 변동성.
    - Source Tag: Stanford — **Single**
    - Source Note: Stanford *Policy* Ch.8.1 — Feb 11 (Paris Summit), Jun 17 (G7), Aug 26 (UN panel).
  - **P-5.2**: 입법·규제에서의 빅테크 영향력 증가
    - Description: 미국 의회의 AI 관련 청문회 산업계 증인이 13% → 37%로 상승, 학계 비중 하락. 원인은 의제 형성에서의 자원 우위. 영향은 정책의 **산업 친화적 경향** 강화. 시나리오적 함의는 “규제 강화” 시나리오의 발생 빈도와 강도를 약화시키는 동인.
    - Source Tag: Stanford — **Single**
    - Source Note: Stanford *Policy* Ch.8 highlights #4.

---

## 1.3 출처 매핑 (대표 예시)

| Factor | Source Tag | 근거 파일 / 섹션 |
|--------|------------|-------------------|
| E-1.1 AI VC 메가딜 73% | OECD — Single | `references/OECD AI VC Investment Report.pdf`, *Key messages* |
| E-2.2 NVDA $4T 시총 | Stanford+Mirae — Strong | Stanford *Economy* 4.1 (Jul 9 2025) / Mirae *VIII. 엔비디아* |
| Env-1.2 신규 DC 100MW+ 48% | Mirae — Single | Mirae *V. 에너지와 그리드* (SemiAnalysis 인용) |
| P-2.1 EU AI Act 발효 | Stanford+Mirae — Strong | Stanford *Policy* Ch.8.1 / Mirae *VI. 소버린 AI* |
| T-1.1 미·중 모델 격차 축소 | Stanford+Mirae — Strong | Stanford *Top Takeaways* #2 / Mirae *VII. 중국 AI* |
| S-4.1 AI 컴패니언 입법 | Stanford — Single | Stanford *Policy* Ch.8.1 (Utah HB 452, CA SB 243) |

> 전체 Factor의 Source Tag/Note는 §1.2 본문에서 각 Factor 항목에 직접 표기됨.

---

## 1.4 Coverage 요약

> 자가 점검: 자료 편향과 취약 영역 가시화.

- **자료별 반영 Factor 수** (한 Factor가 복수 출처면 모두 카운트):
  - **Mirae**: 약 13개 (T-1.1/1.2, T-2.2, T-4.1/4.2, E-2.1/2.2, E-4.2, Env-1.1/1.2, Env-3.1/3.2, Env-4.1, P-1.2, P-2.1, P-3.1/3.2, P-4.2)
  - **OECD**: 약 4개 (E-1.1, E-1.2, E-5.1, E-5.2)
  - **Stanford**: 약 38개 (S 전체, T 대부분, E 대부분, Env-1/2/4 일부, P 대부분)
  - **general**: 0개 (모든 Factor는 자료 기반)
- **Single 출처 Factor 수**: 약 28개 → 제2장 평가 전 **출처 보강 우선 후보**:
  - Stanford 단독: S-1.2, S-2.1, S-2.2, S-3.1, S-3.2, S-4.1, S-4.2, S-5.1, S-5.2, T-2.1, T-3.2, T-5.1, T-5.2, E-3.1, E-3.2, E-4.1, P-1.1, P-2.2, P-4.1, P-5.1, P-5.2
  - Mirae 단독: T-4.1, Env-1.2, Env-3.1, Env-3.2, Env-4.1
  - OECD 단독: E-1.1, E-5.1, E-5.2
- **Environmental 도메인 클러스터 수**: 4개 (목표 5 미만).
  - 사유: 자료에서 직접적 근거가 **에너지·전력·효율**에 편중되어 있어, 무리하게 5번째 클러스터(예: 폐기·생물다양성)를 만들지 않음.
  - **자료 보강 권장**: ① IEA·EIA의 글로벌 전력 수요 시나리오, ② 데이터센터 물 사용 통계(예: 미국 EPA·McKinsey·Bluefield), ③ 전자폐기물·반도체 산업 자원 통계.
- **편향 점검 메모**:
  - OECD에 끌릴 위험은 자본 흐름 트렌드(E-1, E-5)에 한정, 다른 도메인에서 OECD는 거의 사용되지 않음. 추후 `references/`에 정책·산업 자료(예: G7·OECD AI Principles 2026, IEA Energy Outlook)를 추가하면 균형이 좋아짐.
  - Mirae 의존이 큰 영역은 풀스택·전력 인프라·중국 AI. 검증을 위해 Stanford R&D 그래프와 Cross-check 권장.
  - Stanford 비중이 매우 큼 — 전반적으로 “관찰자(인덱스)” 시각이라 **시장·기업 전략 시각**이 약할 수 있음. 미래에셋·OECD 외 기업 IR/리서치를 1~2건 추가하면 균형이 개선됨.

---

## 1.5 다음 단계로의 인계

- 제2장(`out/02-impact-uncertainty.md`)에서 평가할 **팩터 후보 목록**: 위 §1.2의 모든 Factor (총 약 48개).
- 제2장 평가 시 **P4 Capital Allocator 적용 후보**(투자 실행 가능성·유동성과 직접 연결):
  - T-2.2 (TSMC·DC 집중), T-4.1 (풀스택), T-4.2 (물리 AI), E-1.x (자본 집중·미국), E-2.x (CapEx), E-4.2 (가치 포착 위치), E-5.2 (인프라 집중), Env-1.x (전력·DC), Env-3.x (전력 인프라 자산), P-4.2 (반도체 동맹).
- 제2장 결과의 **분기 변수 후보**(시나리오 백본 축으로 검토):
  - **AI 자율성 수준** 축: T-3.1, T-4.2, S-4.1
  - **글로벌 협력 vs 블록화** 축: P-3.x, P-4.x, P-2.x
  - **에너지·환경 제약** 축: Env-1.x, Env-4.x
  - **자본·시장 구조 양극화** 축: E-1.x, E-5.x
