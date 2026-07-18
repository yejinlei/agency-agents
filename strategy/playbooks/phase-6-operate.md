# 🔄 Phase 6 Playbook — Operate & Evolve

> **Duration**: Ongoing | **Agents**: 12+ (rotating) | **Governance**: Studio Producer

---

## 目标

Sustained operations with continuous improvement. The product is live — now make it thrive. This phase has no end date; it runs as long as the product is in market.

## 前置条件

- [ ] Phase 5 Quality Gate passed (stable launch)
- [ ] Phase 5 交接 Package received
- [ ] Operational cadences established
- [ ] Baseline metrics documented

## Operational Cadences

### Continuous (Always Active)

| Agent | Responsibility | SLA |
|-------|---------------|-----|
| **Infrastructure Maintainer** | System 正常运行时间, performance, security | 99.9% 正常运行时间, < 30min MTTR |
| **Support Responder** | Customer support, issue resolution | < 4hr first response |
| **DevOps Automator** | Deployment pipeline, hotfixes | Multiple deploys/day capability |

### Daily

| Agent | Activity | Output |
|-------|----------|--------|
| **Analytics Reporter** | KPI dashboard update | Daily metrics snapshot |
| **Support Responder** | Issue triage and resolution | Support ticket summary |
| **Infrastructure Maintainer** | System health check | Health status report |

### Weekly

| Agent | Activity | Output |
|-------|----------|--------|
| **Analytics Reporter** | Weekly performance analysis | Weekly Analytics Report |
| **Feedback Synthesizer** | User feedback synthesis | Weekly Feedback 总结 |
| **Sprint Prioritizer** | Backlog grooming + 冲刺规划 | Sprint Plan |
| **增长 Hacker** | 增长 channel optimization | 增长 指标 Report |
| **Project Shepherd** | Cross-team coordination | Weekly Status Update |

### Bi-Weekly

| Agent | Activity | Output |
|-------|----------|--------|
| **Feedback Synthesizer** | Deep feedback analysis | Bi-Weekly Insights Report |
| **Experiment Tracker** | A/B test analysis | Experiment Results 总结 |
| **Content Creator** | Content calendar execution | Published Content Report |

### Monthly

| Agent | Activity | Output |
|-------|----------|--------|
| **执行摘要 Generator** | C-suite 报告 | Monthly 执行摘要 |
| **Finance Tracker** | Financial performance review | Monthly Financial Report |
| **法律合规 Checker** | Regulatory 监控 | Compliance Status Report |
| **Trend Researcher** | Market intelligence update | Monthly Market Brief |
| **Brand Guardian** | Brand consistency audit | Brand Health Report |

### Quarterly

| Agent | Activity | Output |
|-------|----------|--------|
| **Studio Producer** | Strategic portfolio review | Quarterly Strategic 审查 |
| **Workflow Optimizer** | Process efficiency audit | Optimization Report |
| **Performance Benchmarker** | Performance 回归测试 | Quarterly Performance Report |
| **Tool Evaluator** | Technology stack review | Tech Debt Assessment |

## Continuous Improvement Loop

```
MEASURE (Analytics Reporter)
    │
    ▼
ANALYZE (Feedback Synthesizer + Analytics Reporter)
    │
    ▼
PLAN (Sprint Prioritizer + Studio Producer)
    │
    ▼
BUILD (Phase 3 Dev↔QA Loop — mini-cycles)
    │
    ▼
VALIDATE (Evidence Collector + Reality Checker)
    │
    ▼
DEPLOY (DevOps Automator)
    │
    ▼
MEASURE (back to start)
```

### Feature Development in Phase 6

New features follow a compressed NEXUS cycle:

```
1. Sprint Prioritizer selects feature from backlog
2. Appropriate Developer Agent implements
3. Evidence Collector validates (Dev↔QA loop)
4. DevOps Automator deploys (feature flag or direct)
5. Experiment Tracker monitors (A/B test if applicable)
6. Analytics Reporter measures impact
7. Feedback Synthesizer collects user response
```

## 事件响应 Protocol

### Severity Levels

| Level | Definition | Response Time | Decision Authority |
|-------|-----------|--------------|-------------------|
| **P0 — Critical** | Service down, data loss, security breach | Immediate | Studio Producer |
| **P1 — High** | Major feature broken, significant degradation | < 1 hour | Project Shepherd |
| **P2 — Medium** | Minor feature issue, workaround available | < 4 hours | Agents Orchestrator |
| **P3 — Low** | Cosmetic issue, minor inconvenience | Next sprint | Sprint Prioritizer |

### 事件响应 Sequence

```
DETECTION (Infrastructure Maintainer or Support Responder)
    │
    ▼
TRIAGE (Agents Orchestrator)
    ├── Classify severity (P0-P3)
    ├── Assign response team
    └── Notify stakeholders
    │
    ▼
RESPONSE
    ├── P0: Infrastructure Maintainer + DevOps Automator + Backend Architect
    ├── P1: Relevant Developer Agent + DevOps Automator
    ├── P2: Relevant Developer Agent
    └── P3: Added to 冲刺待办
    │
    ▼
RESOLUTION
    ├── Fix implemented and deployed
    ├── Evidence Collector verifies fix
    └── Infrastructure Maintainer confirms stability
    │
    ▼
POST-MORTEM
    ├── Workflow Optimizer leads retrospective
    ├── Root cause analysis documented
    ├── Prevention measures identified
    └── Process improvements implemented
```

## 增长 Operations

### Monthly 增长 审查 (增长 Hacker leads)

```
1. Channel Performance Analysis
   - Acquisition by channel (organic, paid, referral, social)
   - CAC by channel
   - Conversion rates by funnel stage
   - LTV:CAC ratio trends

2. Experiment Results
   - Completed A/B tests and outcomes
   - Statistical significance validation
   - Winner implementation status
   - New experiment pipeline

3. Retention Analysis
   - Cohort retention curves
   - Churn risk identification
   - Re-engagement campaign results
   - Feature adoption metrics

4. 增长 Roadmap Update
   - Next month's growth experiments
   - Channel budget reallocation
   - New channel exploration
   - Viral coefficient optimization
```

### Content Operations (Content Creator + Social Media Strategist)

```
Weekly:
- Content calendar execution
- Social media engagement
- Community management
- Performance 追踪

Monthly:
- Content performance review
- Editorial calendar 规划
- Platform algorithm updates
- Content strategy refinement

Platform-Specific:
- Twitter Engager → Daily engagement, weekly threads
- Instagram Curator → 3-5 posts/week, daily stories
- TikTok Strategist → 3-5 videos/week
- Reddit Community Builder → Daily authentic engagement
```

## Financial Operations

### Monthly Financial 审查 (Finance Tracker)

```
1. Revenue Analysis
   - MRR/ARR 追踪
   - Revenue by segment/plan
   - Expansion revenue
   - Churn revenue impact

2. Cost Analysis
   - Infrastructure costs
   - Marketing spend by channel
   - Team/resource costs
   - Tool and 服务 costs

3. Unit Economics
   - CAC trends
   - LTV trends
   - LTV:CAC ratio
   - Payback period

4. Forecasting
   - Revenue forecast (3-month rolling)
   - Cost forecast
   - Cash flow projection
   - Budget variance analysis
```

## Compliance Operations

### Monthly Compliance Check (法律合规 Checker)

```
1. Regulatory Monitoring
   - New regulations affecting the product
   - Existing regulation changes
   - Enforcement actions in the industry
   - Compliance 截止日期 追踪

2. Privacy Compliance
   - Data subject request 处理
   - Consent management effectiveness
   - Data retention policy adherence
   - Cross-border transfer compliance

3. 安全 Compliance
   - Vulnerability scan results
   - Patch management status
   - Access control review
   - Incident log review

4. Audit Readiness
   - 文档 currency
   - Evidence collection status
   - 培训 completion rates
   - Policy acknowledgment 追踪
```

## Strategic Evolution

### Quarterly Strategic 审查 (Studio Producer)

```
1. Market Position Assessment
   - Competitive landscape changes (Trend Researcher input)
   - Market share evolution
   - Brand perception (Brand Guardian input)
   - Customer satisfaction trends (Feedback Synthesizer input)

2. Product Strategy
   - Feature roadmap review
   - Technology debt assessment (Tool Evaluator input)
   - Platform expansion opportunities
   - Partnership evaluation

3. 增长 Strategy
   - Channel effectiveness review
   - New market opportunities
   - Pricing strategy assessment
   - Expansion 规划

4. Organizational Health
   - Process efficiency (Workflow Optimizer input)
   - Team performance metrics
   - Resource allocation optimization
   - Capability development needs

Output: Quarterly Strategic 审查 → Updated roadmap and priorities
```

## Phase 6 成功指标

| Category | Metric | Target | Owner |
|----------|--------|--------|-------|
| **可靠性** | System 正常运行时间 | > 99.9% | Infrastructure Maintainer |
| **可靠性** | MTTR | < 30 minutes | Infrastructure Maintainer |
| **增长** | MoM user growth | > 20% | 增长 Hacker |
| **增长** | Activation rate | > 60% | Analytics Reporter |
| **Retention** | Day 7 retention | > 40% | Analytics Reporter |
| **Retention** | Day 30 retention | > 20% | Analytics Reporter |
| **Financial** | LTV:CAC ratio | > 3:1 | Finance Tracker |
| **Financial** | Portfolio ROI | > 25% | Studio Producer |
| **Quality** | NPS score | > 50 | Feedback Synthesizer |
| **Quality** | Support resolution time | < 4 hours | Support Responder |
| **Compliance** | Regulatory adherence | > 98% | 法律合规 Checker |
| **Efficiency** | Deployment frequency | Multiple/day | DevOps Automator |
| **Efficiency** | Process improvement | 20%/quarter | Workflow Optimizer |

---

*Phase 6 has no end date. It runs as long as the product is in market, with continuous improvement cycles driving the product forward. The NEXUS pipeline can be re-activated (NEXUS-Sprint or NEXUS-Micro) for major new features or pivots.*
