# 🔍 Phase 0 Playbook — Intelligence & Discovery

> **Duration**: 3-7 days | **Agents**: 6 | **Gate Keeper**: Executive Summary Generator

---

## 目标

Validate the opportunity before committing resources. No 构建 until the problem, market, and regulatory landscape are understood.

## 前置条件

- [ ] Project brief or initial concept exists
- [ ] Stakeholder sponsor identified
- [ ] Budget for discovery phase approved

## 智能体激活序列

### Wave 1: 并行启动 (Day 1)

#### 🔍 Trend Researcher — Market Intelligence Lead
```
Activate Trend Researcher for market intelligence on [PROJECT DOM人工智能N].

交付物 required:
1. Competitive landscape analysis (direct + indirect competitors)
2. Market sizing: TAM, SAM, SOM with methodology
3. Trend lifecycle mapping: where is this market in the adoption curve?
4. 3-6 month trend forecast with confidence intervals
5. Investment and funding trends in the space

Sources: Minimum 15 unique, verified sources
Format: Strategic Report with executive summary
时间线: 3 days
```

#### 💬 Feedback Synthesizer — User Needs Analysis
```
Activate Feedback Synthesizer for user needs analysis on [PROJECT DOM人工智能N].

交付物 required:
1. Multi-channel feedback collection plan (surveys, interviews, reviews, social)
2. Sentiment analysis across existing user touchpoints
3. Pain point identification and 优先级排序 (RICE scored)
4. Feature request analysis with business value estimation
5. Churn risk indicators from feedback patterns

Format: Synthesized Feedback Report with priority matrix
时间线: 3 days
```

#### 🔍 用户体验研究er — User Behavior Analysis
```
Activate 用户体验研究er for user behavior analysis on [PROJECT DOM人工智能N].

交付物 required:
1. User interview plan (5-10 target users)
2. Persona development (3-5 primary personas)
3. Journey mapping for primary 用户流s
4. Usability 启发式评估 of competitor products
5. Behavioral insights with statistical validation

Format: Research Findings Report with personas and 旅程图s
时间线: 5 days
```

### Wave 2: 并行启动 (Day 1, independent of Wave 1)

#### 📊 Analytics Reporter — Data Landscape Assessment
```
Activate Analytics Reporter for data landscape assessment on [PROJECT DOM人工智能N].

交付物 required:
1. Existing data source audit (what data is available?)
2. Signal identification (what can we measure?)
3. Baseline metrics establishment
4. Data quality assessment with completeness scoring
5. Analytics infrastructure recommendations

Format: Data Audit Report with signal map
时间线: 2 days
```

#### ⚖️ 法律合规 Checker — Regulatory Scan
```
Activate 法律合规 Checker for regulatory scan on [PROJECT DOM人工智能N].

交付物 required:
1. Applicable regulatory frameworks (GDPR, CCPA, HIPAA, etc.)
2. Data 处理 requirements and constraints
3. Jurisdiction mapping for target markets
4. Compliance risk assessment with severity ratings
5. Blocking vs. manageable compliance issues

Format: Compliance 要求 Matrix
时间线: 3 days
```

#### 🛠️ Tool Evaluator — Technology Landscape
```
Activate Tool Evaluator for technology landscape assessment on [PROJECT DOM人工智能N].

交付物 required:
1. Technology stack assessment for the problem domain
2. Build vs. buy analysis for key components
3. Integration feasibility with existing systems
4. Open source vs. commercial evaluation
5. Technology risk assessment

Format: Tech Stack Assessment with recommendation matrix
时间线: 2 days
```

## Convergence Point (Day 5-7)

All six agents deliver their reports. The 执行摘要 Generator synthesizes:

```
Activate 执行摘要 Generator to synthesize Phase 0 查找s.

Input documents:
1. Trend Researcher → 市场分析 Report
2. Feedback Synthesizer → Synthesized Feedback Report
3. 用户体验研究er → Research Findings Report
4. Analytics Reporter → Data Audit Report
5. 法律合规 Checker → Compliance 要求 Matrix
6. Tool Evaluator → Tech Stack Assessment

Output: 执行摘要 (≤500 words, SCQA format)
Decision required: GO / NO-GO / PIVOT
Include: Quantified market opportunity, validated user needs, regulatory path, technology feasibility
```

## Quality Gate Checklist

| # | Criterion | Evidence Source | Status |
|---|-----------|----------------|--------|
| 1 | Market opportunity validated with TAM > minimum viable threshold | Trend Researcher report | ☐ |
| 2 | ≥3 validated user pain points with 支持 data | Feedback Synthesizer + 用户体验研究er | ☐ |
| 3 | No blocking compliance issues identified | 法律合规 Checker matrix | ☐ |
| 4 | Key metrics and data sources identified | Analytics Reporter audit | ☐ |
| 5 | Technology stack feasible and assessed | Tool Evaluator assessment | ☐ |
| 6 | Executive summary delivered with GO/NO-GO recommendation | 执行摘要 Generator | ☐ |

## Gate Decision

- **GO**: Proceed to Phase 1 — Strategy & 架构
- **NO-GO**: Archive 查找s, document learnings, redirect resources
- **PIVOT**: Modify scope/direction based on 查找s, re-run targeted discovery

## 交接 to Phase 1

```markdown
## Phase 0 → Phase 1 交接 Package

### Documents to carry forward:
1. 市场分析 Report (Trend Researcher)
2. Synthesized Feedback Report (Feedback Synthesizer)
3. User Personas and Journey Maps (用户体验研究er)
4. Data Audit Report (Analytics Reporter)
5. Compliance 要求 Matrix (法律合规 Checker)
6. Tech Stack Assessment (Tool Evaluator)
7. 执行摘要 with GO decision (执行摘要 Generator)

### Key constraints identified:
- [Regulatory constraints from 法律合规 Checker]
- [Technical constraints from Tool Evaluator]
- [Market timing constraints from Trend Researcher]

### Priority user needs (for Sprint Prioritizer):
1. [Pain point 1 — from Feedback Synthesizer]
2. [Pain point 2 — from 用户体验研究er]
3. [Pain point 3 — from Feedback Synthesizer]
```

---

*Phase 0 is complete when the 执行摘要 Generator delivers a GO decision with 支持 evidence from all six discovery agents.*
