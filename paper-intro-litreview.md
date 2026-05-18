# Introduction and Literature Review (Draft)

> Target journal: Expert Systems with Applications (ESWA)
> Citation style: Harvard
> Status: Draft — [⚠] 표시된 항목은 저자가 직접 URL/접근 확인 필요

---

## 1. Introduction

### 1.1 Background and Motivation

Technology scenario planning has long served as a cornerstone of strategic foresight in management of technology (MOT). By mapping the interaction of key drivers, constructing alternative futures, and translating them into investment and innovation decisions, scenario planning enables organisations to act under deep uncertainty (Schoemaker, 1995). Empirical evidence further shows that firms with mature foresight practices outperform peers by up to 33% in profitability and 200% in growth (Rohrbeck and Kum, 2018), underscoring the strategic value of systematic foresight.

Yet in practice, the discipline remains resource-intensive and expert-dependent. A comprehensive review of 23 scenario development techniques catalogued by Bishop, Hines and Collins (2007) reveals that virtually every technique relies on facilitated workshops, structured elicitation, and domain expertise—resources that are scarce, expensive, and inaccessible to smaller organisations. Bradfield et al. (2005) further document the field's fragmentation into three distinct methodological schools—the intuitive logics tradition of Shell/GBN, the French *la prospective* school of Godet, and the probabilistic approaches—each demanding specialised human expertise. This expert dependency creates a structural bottleneck: the more sophisticated the foresight method, the more organisational capability is required to execute it (Rohrbeck, 2010).

Recent advances in large language models (LLMs) offer a potential pathway to address this bottleneck. LLMs have demonstrated strong performance across structured reasoning, multi-step analysis, and domain-specific judgment tasks. When deployed as autonomous agents equipped with tool use and iterative self-review, LLMs can execute complex analytical pipelines with minimal human orchestration. However, a fundamental question remains unresolved: in a multi-stage analytical workflow, which stages can be reliably delegated to an LLM agent, and which require human oversight?

This question is non-trivial. Delegating the wrong stage to an agent risks propagating errors across downstream steps; retaining human control over every stage negates the efficiency gains of automation. What practitioners need is an empirically grounded map of agent task difficulty—a diagnostic tool that identifies where agents reliably operate and where they struggle.

### 1.2 Research Gap

Existing work on LLMs in strategic contexts has largely focused on single-step tasks: evaluating documents (Choi and Park, 2026), assessing decisions under framing conditions (Choi, 2026), or generating strategic narratives (Rohrbeck, Szuppa and Schmidt, forthcoming [⚠ SSRN 5636869]). No study has examined LLM agent behaviour across the *full pipeline* of a complex MOT task, nor proposed a framework for characterising stage-level task difficulty from agent behavioural traces.

Meanwhile, corporate foresight scholars have called for greater integration of AI tools into foresight processes (Fergnani, 2022; Gavetti and Menon, 2016), but without specifying how to govern the human-agent boundary within a multi-step foresight workflow. This gap between the methodological richness of scenario planning and the emerging capability of LLM agents constitutes the central motivation for the present study.

### 1.3 Research Questions

This study addresses three research questions:

- **RQ1**: How can the task difficulty of individual stages in an LLM-agent-driven analytical pipeline be characterised using observable behavioural proxy metrics?
- **RQ2**: When applied to the full technology scenario planning pipeline, what difficulty gradient does the proposed framework reveal across stages?
- **RQ3**: What are the structural explanations for the observed difficulty pattern, and what do they imply for human-in-the-loop governance in LLM-assisted foresight?

### 1.4 Contributions

This paper makes three contributions:

1. **Behavioral Load Profiling (BLP) Framework**: a stage-level diagnostic tool for characterising LLM agent task difficulty using four proxy metrics derivable from agent interaction traces.
2. **Stress-test evidence**: application of the BLP framework to technology scenario planning—one of the most structurally demanding MOT tasks—demonstrating its utility in a high-complexity empirical setting.
3. **Governance implications**: an empirically grounded guide identifying which stages of a scenario planning pipeline can be delegated to an LLM agent and which require human judgment, with generalisation to other MOT workflows.

---

## 2. Literature Review

### 2.1 Technology Scenario Planning: Methodology and Structural Complexity

Scenario planning is a disciplined method for constructing internally consistent alternative futures that bound the range of strategic uncertainty (Schoemaker, 1995). Schoemaker's seminal ten-step framework—spanning scope definition, trend identification, key uncertainty mapping, scenario construction, and decision scenario evolution—remains the most widely cited structured process in the field. Its enduring influence stems from the recognition that scenario planning must be both analytically rigorous and narratively accessible if it is to support strategic action.

Parallel to the Anglo-American intuitive logics tradition, Godet (1986) developed the French *prospective* school, centred on structural analysis and cross-impact matrix methods. Godet's MICMAC approach classifies variables by their active and passive influence scores—producing Driving, Critical, Dependent, and Inert roles—and uses this classification to identify the axes of a 2×2 scenario backbone. This quantitative grounding makes the method particularly amenable to systematic replication, yet it demands careful expert judgment at the cross-impact scoring stage, where a typical analysis of fourteen variables requires 196 pair-wise assessments.

Bradfield et al. (2005) synthesise the evolution of both traditions, documenting three main schools and noting that the field has long suffered from "methodological chaos"—a proliferation of techniques without consensus on standards or evaluation criteria. This fragmentation, they argue, reflects the inherent complexity of the foresight task and the irreducibly expert-dependent character of its core analytical steps.

Bishop, Hines and Collins (2007) extend this survey to identify 23 distinct scenario development techniques across eight categories. Their catalogue confirms that no technique in the mainstream repertoire is designed for automation: all presuppose human facilitators, structured elicitation sessions, and iterative expert negotiation. The implication is clear—the bottleneck in scenario planning is not analytical capacity but human attention and expertise.

### 2.2 Corporate Foresight as Organisational Capability

Corporate foresight research situates scenario planning within a broader organisational capability framework. Rohrbeck (2010) proposes a maturity model for organisational future orientation, identifying five dimensions and twenty elements that collectively determine a firm's capacity to anticipate and respond to discontinuous change. A key finding is that firms face three primary barriers during discontinuous change: the rate of change itself, organisational ignorance, and inertia—barriers that foresight capability is designed to address.

The performance consequences of this capability are substantial. Rohrbeck and Kum (2018) demonstrate, through a longitudinal study, that future-prepared firms achieve 33% higher profitability and 200% higher growth relative to industry peers. Firms with foresight deficiencies, by contrast, incur a performance discount of 37% to 108%. These findings establish that systematic foresight is not a luxury but a strategic necessity.

Fergnani (2022) argues that corporate foresight represents a new frontier for strategy and management scholarship, positioning it as a dynamic capability that enables firms to evaluate future scenarios of the business environment. Critically, Fergnani grounds this argument in the dynamic capabilities framework, suggesting that the *capacity to foresee*—not merely the *act of planning*—constitutes a firm-level source of competitive advantage. This framing elevates foresight automation from an operational efficiency question to a strategic capability question: if the ability to conduct foresight rapidly and accessibly can be democratised through AI, the competitive implications are significant.

Gavetti and Menon (2016) contribute a theoretical model of strategic foresight as agency-in-evolution, arguing that disciplined foresight is possible and replicable within bounded conditions. Their emphasis on *agency*—the capacity of a bounded rational actor to model and navigate future environments—provides theoretical grounding for the notion of an LLM agent as a foresight actor, albeit one whose agency is contingent on the structural demands of the task.

### 2.3 AI and LLMs in Strategic Foresight

The integration of artificial intelligence into foresight practices is an emerging research area. Rohrbeck, Szuppa and Schmidt [⚠ forthcoming, SSRN 5636869] document the case of Siemens Professional Education, where an AI-human collaboration model reduced foresight process duration by approximately 20%, resource utilisation by 25%, and expert time requirements by 50%, while increasing analytic quality by 30%. Their work demonstrates that AI integration into foresight is not merely a theoretical proposition but a practitioner reality—and that the key design challenge lies in re-engineering the foresight process itself rather than inserting AI into legacy workflows.

Within the broader LLM literature, structured prompting approaches have shown particular promise for multi-dimensional analytical tasks. Choi and Park (2026) demonstrate that structured prompting frameworks improve consistency, alignment, and interpretability of LLM judgments in patent evaluation—a high-stakes comparative assessment task sharing structural similarities with cross-impact analysis. A complementary study (Choi, 2026) shows that LLM strategic judgments exhibit pronounced context-sensitivity and framing effects, underscoring the need for principled governance when deploying LLMs in strategic decision contexts.

These findings suggest that LLMs are not neutral analytical engines: their outputs are systematically shaped by the structure of the task, the framing of the prompt, and the domain in question. For scenario planning, where each stage has distinct structural demands—from open-ended trend scanning to constrained logical inference in cross-impact classification—the implication is that LLM agent behaviour will vary significantly across stages. Characterising this variation is the central empirical contribution of the present study.

### 2.4 Human-in-the-Loop Design in LLM Agent Systems

As LLM agents are deployed in increasingly complex analytical workflows, the question of where to position human oversight has attracted significant research attention. A multi-step transparent (MST) decision workflow study (arXiv:2501.10909) found that structured human checkpoints outperform single-step AI collaboration in settings where AI reasoning is prone to error, suggesting that granular oversight—targeted at specific high-risk stages—is more effective than blanket human review.

Complementary work on cascaded LLM frameworks (arXiv:2506.11887) proposes adaptive task delegation across capability tiers, with deferral policies calibrated to task complexity and correctness risk. The key insight is that optimal human-AI task allocation is *stage-specific*, not workflow-level: some stages warrant full AI autonomy, while others require mandatory human validation.

The present study builds on this insight by proposing observable behavioural proxies—rather than ground-truth correctness measures—as the basis for identifying stages that require human oversight. This approach is particularly suited to novel analytical domains like scenario planning, where gold-standard outputs do not exist for comparison.

---

## 3. References

Bradfield, R., Wright, G., Burt, G., Cairns, G. and Van der Heijden, K. (2005). The origins and evolution of scenario techniques in long range business planning. *Futures*, 37(8), pp.795–812. https://doi.org/10.1016/j.futures.2005.01.003

Bishop, P., Hines, A. and Collins, T. (2007). The current state of scenario development: an overview of techniques. *Foresight*, 9(1), pp.5–25. https://doi.org/10.1108/14636680710727516

Choi, D. and Park, B. (2026). Structured LLM-based patent comparison across three evaluation dimensions. *World Patent Information*, 102430. https://doi.org/10.1016/j.wpi.2026.102430

Choi, D. (2026). Context and framing sensitivity in LLM-based strategic decision-making. [Manuscript under review]

Fergnani, A. (2022). Corporate foresight: A new frontier for strategy and management. *Academy of Management Perspectives*, 36(2), pp.820–844. https://doi.org/10.5465/amp.2018.0178

Gavetti, G. and Menon, A. (2016). Evolution cum agency: Toward a model of strategic foresight. *Strategy Science*, 1(3), pp.207–233. https://doi.org/10.1287/stsc.2016.0018

Godet, M. (1986). Introduction to *la prospective*: Seven key ideas and one scenario method. *Futures*, 18(2), pp.134–157. https://doi.org/10.1016/0016-3287(86)90094-7

Rohrbeck, R. (2010). Towards a maturity model for organizational future orientation. *Academy of Management Proceedings*, 2010(1), pp.1–6. https://doi.org/10.5465/AMBPP.2010.54493637

Rohrbeck, R. and Kum, M.E. (2018). Corporate foresight and its impact on firm performance: A longitudinal analysis. *Technological Forecasting and Social Change*, 129, pp.105–116. https://doi.org/10.1016/j.techfore.2017.12.013

Rohrbeck, R., Szuppa, S. and Schmidt, J. (forthcoming). Artificial intelligence in strategic foresight: The case of Siemens Professional Education. [⚠ 저자 직접 확인 필요 — SSRN 5636869로 검색]

Schoemaker, P.J.H. (1995). Scenario planning: A tool for strategic thinking. *Sloan Management Review*, 36(2), pp.25–40. https://sloanreview.mit.edu/article/scenario-planning-a-tool-for-strategic-thinking/

---

> **[⚠] 확인 필요 항목**
>
> - **Rohrbeck, Szuppa & Schmidt (forthcoming)**: 연구 내용은 여러 출처에서 확인되었으나, SSRN 5636869 직접 접근 확인 필요. https://ssrn.com/abstract=5636869 에서 직접 확인 권장.
> - **Godet (1986)**: ScienceDirect에서 초록 확인됨. 전문 접근은 기관 구독 필요.
