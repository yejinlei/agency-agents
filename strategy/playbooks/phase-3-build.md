# 🔨 Phase 3 Playbook — Build & Iterate

> **Duration**: 2-12 weeks (varies by scope) | **Agents**: 15-30+ | **Gate Keeper**: Agents Orchestrator

---

## 目标

Implement all features through continuous Dev↔QA loops. Every task is validated before the next begins. This is where the bulk of the work happens — and where NEXUS's orchestration delivers the most value.

## 前置条件

- [ ] Phase 2 Quality Gate passed (foundation verified)
- [ ] Sprint Prioritizer backlog available with RICE scores
- [ ] 持续集成/持续部署 pipeline operational
- [ ] Design system and component library ready
- [ ] API scaffold with auth system ready

## The Dev↔QA Loop — Core Mechanic

The Agents Orchestrator manages every task through this cycle:

```
FOR EACH task IN sprint_backlog (ordered by RICE score):

  1. ASSIGN task to appropriate Developer Agent (see assignment matrix)
  2. Developer IMPLEMENTS task
  3. Evidence Collector TESTS task
     - Visual screenshots (desktop, tablet, mobile)
     - Functional verification against acceptance criteria
     - Brand consistency check
  4. IF verdict == PASS:
       Mark task complete
       Move to next task
     ELIF verdict == F人工智能L AND attempts < 3:
       Send QA feedback to Developer
       Developer FIXES specific issues
       Return to step 3
     ELIF attempts >= 3:
       ESCALATE to Agents Orchestrator
       Orchestrator decides: reassign, decompose, defer, or accept
  5. UPDATE pipeline status report
```

## Agent Assignment Matrix

### Primary Developer Assignment

| Task Category | Primary Agent | Backup Agent | QA Agent |
|--------------|--------------|-------------|----------|
| **React/Vue/Angular UI** | Frontend Developer | Rapid Prototyper | Evidence Collector |
| **REST/GraphQL API** | Backend Architect | Senior Developer | API Tester |
| **Database operations** | Backend Architect | — | API Tester |
| **Mobile (iOS/Android)** | Mobile App Builder | — | Evidence Collector |
| **ML model/pipeline** | 人工智能 Engineer | — | Test 结果分析器 |
| **持续集成/持续部署/Infrastructure** | DevOps Automator | Infrastructure Maintainer | Performance Benchmarker |
| **Premium/complex feature** | Senior Developer | Backend Architect | Evidence Collector |
| **Quick prototype/POC** | Rapid Prototyper | Frontend Developer | Evidence Collector |
| **WebXR/immersive** | XR Immersive Developer | — | Evidence Collector |
| **visionOS** | visionOS Spatial Engineer | macOS Spatial/Metal Engineer | Evidence Collector |
| **Cockpit controls** | XR Cockpit Interaction Specialist | XR Interface Architect | Evidence Collector |
| **CLI/terminal tools** | Terminal Integration Specialist | — | API Tester |
| **Code intelligence** | LSP/Index Engineer | — | Test 结果分析器 |
| **Performance optimization** | Performance Benchmarker | Infrastructure Maintainer | Performance Benchmarker |

### Specialist Support (activated as needed)

| Specialist | When to Activate | Trigger |
|-----------|-----------------|---------|
| 界面设计er | Component needs visual refinement | Developer requests design guidance |
| Whimsy Injector | Feature needs delight/personality | UX review identifies opportunity |
| Visual Storyteller | Visual narrative content needed | Content requires visual assets |
| Brand Guardian | Brand consistency concern | QA finds brand deviation |
| XR Interface Architect | Spatial 交互设计 needed | XR feature requires UX guidance |
| Analytics Reporter | Deep data analysis needed | Feature requires analytics integration |

## Parallel Build Tracks

For NEXUS-Full 部署s, four tracks run simultaneously:

### Track A: Core Product Development
```
Managed by: Agents Orchestrator (Dev↔QA loop)
Agents: Frontend Developer, Backend Architect, 人工智能 Engineer,
        Mobile App Builder, Senior Developer
QA: Evidence Collector, API Tester, Test 结果分析器

Sprint cadence: 2-week sprints
Daily: Task implementation + QA validation
End of sprint: Sprint review + retrospective
```

### Track B: 增长 & Marketing Preparation
```
Managed by: Project Shepherd
Agents: 增长 Hacker, Content Creator, Social Media Strategist,
        App Store Optimizer

Sprint cadence: Aligned with Track A milestones
Activities:
- 增长 Hacker → Design viral loops and referral mechanics
- Content Creator → Build launch content pipeline
- Social Media Strategist → Plan cross-platform campaign
- App Store Optimizer → Prepare store listing (if mobile)
```

### Track C: Quality & Operations
```
Managed by: Agents Orchestrator
Agents: Evidence Collector, API Tester, Performance Benchmarker,
        Workflow Optimizer, Experiment Tracker

Continuous activities:
- Evidence Collector → Screenshot QA for every task
- API Tester → Endpoint validation for every API task
- Performance Benchmarker → Periodic 负载测试
- Workflow Optimizer → Process improvement identification
- Experiment Tracker → A/B 测试集up for validated features
```

### Track D: Brand & Experience Polish
```
Managed by: Brand Guardian
Agents: 界面设计er, Brand Guardian, Visual Storyteller,
        Whimsy Injector

Triggered activities:
- 界面设计er → Component refinement when QA identifies visual issues
- Brand Guardian → Periodic brand consistency audit
- Visual Storyteller → Visual narrative assets as features complete
- Whimsy Injector → Micro-interactions and delight moments
```

## Sprint Execution Template

### Sprint Planning (Day 1)

```
Sprint Prioritizer activates:
1. 审查 backlog with updated RICE scores
2. Select tasks for sprint based on team velocity
3. Assign tasks to developer agents
4. Identify dependencies and ordering
5. Set 冲刺目标 and success criteria

Output: Sprint Plan with task assignments
```

### Daily Execution (Day 2 to Day N-1)

```
Agents Orchestrator manages:
1. Current task status check
2. Dev↔QA loop execution
3. Blocker identification and resolution
4. Progress 追踪 and 报告

Status report format:
- Tasks completed today: [list]
- Tasks in QA: [list]
- Tasks in development: [list]
- Blocked tasks: [list with reason]
- QA pass rate: [X/Y]
```

### Sprint 审查 (Day N)

```
Project Shepherd facilitates:
1. Demo completed features
2. 审查 QA evidence for each task
3. Collect stakeholder feedback
4. Update backlog based on learnings

Participants: All active agents + stakeholders
Output: Sprint 审查 总结
```

### Sprint 回顾

```
Workflow Optimizer facilitates:
1. What went well?
2. What could improve?
3. What will we change next sprint?
4. Process efficiency metrics

Output: 回顾 Action Items
```

## Orchestrator Decision Logic

### Task Failure Handling

```
WHEN task fails QA:
  IF attempt == 1:
    → Send specific QA feedback to developer
    → Developer fixes ONLY the identified issues
    → Re-submit for QA
    
  IF attempt == 2:
    → Send accumulated QA feedback
    → Consider: Is the developer agent the right fit?
    → Developer fixes with additional context
    → Re-submit for QA
    
  IF attempt == 3:
    → ESCALATE
    → Options:
      a) Reassign to different developer agent
      b) Decompose task into smaller sub-tasks
      c) Revise approach/architecture
      d) Accept with known limitations (document)
      e) Defer to future sprint
    → Document decision and rationale
```

### Parallel Task Management

```
WHEN multiple tasks have no dependencies:
  → Assign to different developer agents simultaneously
  → Each runs independent Dev↔QA loop
  → Orchestrator tracks all loops concurrently
  → Merge completed tasks in dependency order

WHEN task has dependencies:
  → Wait for dependency to pass QA
  → Then assign dependent task
  → Include dependency context in 交接
```

## Quality Gate Checklist

| # | Criterion | Evidence Source | Status |
|---|-----------|----------------|--------|
| 1 | All sprint tasks pass QA (100% completion) | Evidence Collector screenshots per task | ☐ |
| 2 | All API 端点 validated | API Tester r出口ion report | ☐ |
| 3 | Performance baselines met (P95 < 200ms) | Performance Benchmarker report | ☐ |
| 4 | Brand consistency verified (95%+ adherence) | Brand Guardian audit | ☐ |
| 5 | No critical bugs (zero P0/P1 open) | Test 结果分析器 summary | ☐ |
| 6 | All acceptance criteria met | Task-by-task verification | ☐ |
| 7 | Code review completed for all PRs | Git history evidence | ☐ |

## Gate Decision

**关卡守门人**: Agents Orchestrator

- **PASS**: Feature-complete application → Phase 4 activation
- **CONTINUE**: More sprints needed → Continue Phase 3
- **ESCALATE**: Systemic issues → Studio Producer intervention

## 交接 to Phase 4

```markdown
## Phase 3 → Phase 4 交接 Package

### For Reality Checker:
- Complete application (all features implemented)
- All QA evidence from Dev↔QA loops
- API Tester r出口ion results
- Performance Benchmarker baseline data
- Brand Guardian consistency audit
- Known issues list (if any accepted limitations)

### For 法律合规 Checker:
- Data 处理 implementation details
- Privacy policy implementation
- Consent management implementation
- 安全 measures implemented

### For Performance Benchmarker:
- Application URLs for 负载测试
- Expected traffic patterns
- Performance budgets from architecture

### For Infrastructure Maintainer:
- Production environment requirements
- Scaling configuration needs
- Monitoring alert thresholds
```

---

*Phase 3 is complete when all sprint tasks pass QA, all API 端点 are validated, performance baselines are met, and no critical bugs remain open.*
