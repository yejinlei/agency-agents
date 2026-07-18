# 🚨 Runbook: Incident Response

> **Mode**: NEXUS-Micro | **Duration**: Minutes to hours | **Agents**: 3-8

---

## Scenario

Something is broken 在生产环境中. Users are affected. Speed of response matters, but so does doing it right. This 运行手册 covers detection through post-mortem.

## Severity Classification

| Level | Definition | Examples | Response Time |
|-------|-----------|----------|--------------|
| **P0 — Critical** | Service completely down, data loss, security breach | Database corruption, DDoS attack, auth system failure | Immediate (all hands) |
| **P1 — High** | Major feature broken, significant performance degradation | Payment processing down, 50%+ error rate, 10x latency | < 1 hour |
| **P2 — Medium** | Minor feature broken, workaround available | Search not working, non-critical API errors | < 4 hours |
| **P3 — Low** | Cosmetic issue, minor inconvenience | Styling bug, typo, minor UI glitch | Next sprint |

## Response Teams by Severity

### P0 — Critical Response Team
| Agent | Role | Action |
|-------|------|--------|
| **Infrastructure Maintainer** | Incident commander | Assess scope, coordinate response |
| **DevOps Automator** | Deployment/rollback | Execute rollback if needed |
| **Backend Architect** | Root cause investigation | Diagnose system issues |
| **Frontend Developer** | UI-side investigation | Diagnose client-side issues |
| **Support Responder** | User communication | Status page updates, user notifications |
| **执行摘要 Generator** | Stakeholder communication | Real-time executive updates |

### P1 — High Response Team
| Agent | Role |
|-------|------|
| **Infrastructure Maintainer** | Incident commander |
| **DevOps Automator** | Deployment support |
| **Relevant Developer Agent** | Fix implementation |
| **Support Responder** | User communication |

### P2 — Medium Response
| Agent | Role |
|-------|------|
| **Relevant Developer Agent** | Fix implementation |
| **Evidence Collector** | Verify fix |

### P3 — Low Response
| Agent | Role |
|-------|------|
| **Sprint Prioritizer** | Add to backlog |

## 事件响应 Sequence

### Step 1: Detection & Triage (0-5 minutes)

```
TRIGGER: Alert from 监控 / User report / Agent detection

Infrastructure Maintainer:
1. Acknowledge alert
2. Assess scope and impact
   - How many users affected?
   - Which 服务s are impacted?
   - Is data at risk?
3. Classify severity (P0/P1/P2/P3)
4. Activate appropriate response team
5. Create incident channel/thread

Output: Incident classification + response team activated
```

### Step 2: Investigation (5-30 minutes)

```
PARALLEL INVESTIGATION:

Infrastructure Maintainer:
├── Check system metrics (CPU, memory, network, disk)
├── 审查 error logs
├── Check recent 部署s
└── Verify external dependencies

Backend Architect (if P0/P1):
├── Check database health
├── 审查 API error rates
├── Check 服务 communication
└── Identify failing component

DevOps Automator:
├── 审查 recent 部署 history
├── Check 持续集成/持续部署 pipeline status
├── Prepare rollback if needed
└── Verify infrastructure state

Output: Root cause identified (or narrowed to component)
```

### Step 3: Mitigation (15-60 minutes)

```
DECISION TREE:

IF caused by recent 部署:
  → DevOps Automator: Execute rollback
  → Infrastructure Maintainer: Verify recovery
  → Evidence Collector: Confirm fix

IF caused by infrastructure issue:
  → Infrastructure Maintainer: Scale/restart/failover
  → DevOps Automator: Support infrastructure changes
  → Verify recovery

IF caused by code bug:
  → Relevant Developer Agent: Implement hotfix
  → Evidence Collector: Verify fix
  → DevOps Automator: Deploy hotfix
  → Infrastructure Maintainer: Monitor recovery

IF caused by external dependency:
  → Infrastructure Maintainer: Activate fallback/cache
  → Support Responder: Communicate to users
  → Monitor for external recovery

THROUGHOUT:
  → Support Responder: Update status page every 15 minutes
  → 执行摘要 Generator: Brief stakeholders (P0 only)
```

### Step 4: Resolution Verification (Post-fix)

```
Evidence Collector:
1. Verify the fix resolves the issue
2. Screenshot evidence of working state
3. Confirm no new issues introduced

Infrastructure Maintainer:
1. Verify all metrics returning to normal
2. Confirm no cascading failures
3. Monitor for 30 minutes post-fix

API Tester (if API-related):
1. Run r出口ion on affected endpoints
2. Verify response times normalized
3. Confirm error rates at baseline

Output: Incident resolved confirmation
```

### Step 5: 事后复盘 (Within 48 hours)

```
Workflow Optimizer leads post-mortem:

1. 时间线 reconstruction
   - When was the issue introduced?
   - When was it detected?
   - When was it resolved?
   - Total user impact duration

2. Root cause analysis
   - What failed?
   - Why did it fail?
   - Why wasn't it caught earlier?
   - 5 Whys analysis

3. Impact assessment
   - Users affected
   - Revenue impact
   - Reputation impact
   - Data impact

4. Prevention measures
   - What 监控 would have caught this sooner?
   - What 测试 would have prevented this?
   - What process changes are needed?
   - What infrastructure changes are needed?

5. Action items
   - [Action] → [Owner] → [Deadline]
   - [Action] → [Owner] → [Deadline]
   - [Action] → [Owner] → [Deadline]

Output: 事后复盘 Report → Sprint Prioritizer adds prevention tasks to backlog
```

## 沟通 Templates

### Status Page Update (Support Responder)
```
[TIMESTAMP] — [SERVICE NAME] Incident

Status: [Investigating / Identified / Monitoring / Resolved]
Impact: [Description of user impact]
Current action: [What we're doing about it]
Next update: [When to expect the next update]
```

### Executive Update (执行摘要 Generator — P0 only)
```
INCIDENT BRIEF — [TIMESTAMP]

SITUATION: [Service] is [down/degraded] affecting [N users/% of traffic]
CAUSE: [Known/Under investigation] — [Brief description if known]
ACTION: [What's 是 done] — ETA [时间估算]
IMPACT: [Business impact — revenue, users, reputation]
NEXT UPDATE: [Timestamp]
```

## 升级 Matrix

| Condition | Escalate To | Action |
|-----------|------------|--------|
| P0 not resolved in 30 min | Studio Producer | Additional resources, vendor escalation |
| P1 not resolved in 2 hours | Project Shepherd | Resource reallocation |
| Data breach suspected | 法律合规 Checker | Regulatory notification assessment |
| User data affected | 法律合规 Checker + 执行摘要 Generator | GDPR/CCPA notification |
| Revenue impact > $X | Finance Tracker + Studio Producer | Business impact assessment |
