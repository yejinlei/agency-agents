# 🛡️ Phase 4 Playbook — Quality & Hardening

> **Duration**: 3-7 days | **Agents**: 8 | **Gate Keeper**: Reality Checker (sole authority)

---

## 目标

The final quality gauntlet. The Reality Checker defaults to "NEEDS WORK" — you must prove production readiness with overwhelming evidence. This phase exists because first implementations typically need 2-3 revision cycles, and that's healthy.

## 前置条件

- [ ] Phase 3 Quality Gate passed (all tasks QA'd)
- [ ] Phase 3 交接 Package received
- [ ] All features implemented and individually verified

## Critical Mindset

> **The Reality Checker's default verdict is NEEDS WORK.**
> 
> This is not pessimism — it's realism. Production readiness requires:
> - Complete 用户旅程s working 端到端
> - Cross-device consistency (desktop, tablet, mobile)
> - Performance under load (not just happy path)
> - 安全 validation (not just "we added auth")
> - Specification compliance (every requirement, not most)
>
> A B/B+ rating on first pass is normal and expected.

## 智能体激活序列

### Step 1: Evidence Collection (Day 1-2, All Parallel)

#### 📸 Evidence Collector — Comprehensive Visual Evidence
```
Activate Evidence Collector for comprehensive system evidence on [PROJECT].

交付物 required:
1. Full screenshot suite:
   - Desktop (1920x1080) — every page/view
   - Tablet (768x1024) — every page/view
   - Mobile (375x667) — every page/view
2. Interaction evidence:
   - Navigation flows (before/after clicks)
   - Form interactions (empty, filled, submitted, error states)
   - Modal/dialog interactions
   - Accordion/expandable content
3. Theme evidence:
   - Light mode — all pages
   - Dark mode — all pages
   - System preference detection
4. Error state evidence:
   - 404 pages
   - Form validation errors
   - Network error 处理
   - Empty states

Format: Screenshot Evidence Package with test-results.json
时间线: 2 days
```

#### 🔌 API Tester — Full API R出口ion
```
Activate API Tester for complete API r出口ion on [PROJECT].

交付物 required:
1. Endpoint r出口ion suite:
   - All endpoints tested (GET, POST, PUT, DELETE)
   - Authentication/authorization verification
   - Input validation 测试
   - Error response verification
2. Integration 测试:
   - Cross-服务 communication
   - Database operation verification
   - External API integration
3. Edge case 测试:
   - Rate limiting behavior
   - Large payload 处理
   - Concurrent request 处理
   - Malformed input 处理

Format: API Test Report with pass/fail per endpoint
时间线: 2 days
```

#### ⚡ Performance Benchmarker — 负载测试
```
Activate Performance Benchmarker for 负载测试 on [PROJECT].

交付物 required:
1. Load test at 10x expected traffic:
   - Response time distribution (P50, P95, P99)
   - Throughput under load
   - Error rate under load
   - Resource utilization (CPU, memory, network)
2. Core Web Vitals measurement:
   - LCP (Largest Contentful Paint) < 2.5s
   - FID (First Input Delay) < 100ms
   - CLS (Cumulative Layout Shift) < 0.1
3. Database performance:
   - Query execution times
   - Connection pool utilization
   - Index effectiveness
4. Stress test results:
   - Breaking point identification
   - Graceful degradation behavior
   - Recovery time after overload

Format: Performance Certification Report
时间线: 2 days
```

#### ⚖️ 法律合规 Checker — Final Compliance Audit
```
Activate 法律合规 Checker for final compliance audit on [PROJECT].

交付物 required:
1. Privacy compliance verification:
   - Privacy policy accuracy
   - Consent management functionality
   - Data subject rights implementation
   - Cookie consent implementation
2. 安全 compliance:
   - Data encryption (静态 and 传输中)
   - Authentication security
   - Input sanitization
   - OWASP Top 10 check
3. Regulatory compliance:
   - GDPR requirements (if applicable)
   - CCPA requirements (if applicable)
   - Industry-specific requirements
4. 无障碍 compliance:
   - WCAG 2.1 AA verification
   - Screen reader compatibility
   - Keyboard navigation

Format: Compliance Certification Report
时间线: 2 days
```

### Step 2: Analysis (Day 3-4, Parallel, after Step 1)

#### 📊 Test 结果分析器 — Quality 指标 Aggregation
```
Activate Test 结果分析器 for quality metrics aggregation on [PROJECT].

Input: ALL Step 1 reports
交付物 required:
1. Aggregate quality dashboard:
   - Overall quality score
   - Category breakdown (visual, functional, performance, security, compliance)
   - Issue severity distribution
   - Trend analysis (if multiple test cycles)
2. Issue 优先级排序:
   - Critical issues (must fix before production)
   - High issues (should fix before production)
   - Medium issues (fix in next sprint)
   - Low issues (backlog)
3. Risk assessment:
   - Production readiness probability
   - Remaining risk areas
   - Recommended mitigations

Format: Quality 指标 仪表板
时间线: 1 day
```

#### 🔄 Workflow Optimizer — Process Efficiency 审查
```
Activate Workflow Optimizer for process efficiency review on [PROJECT].

Input: Phase 3 execution data + Step 1 查找s
交付物 required:
1. Process efficiency analysis:
   - Dev↔QA loop efficiency (first-pass rate, average retries)
   - Bottleneck identification
   - Time-to-resolution for different issue types
2. Improvement recommendations:
   - Process changes for Phase 6 operations
   - Automation opportunities
   - Quality improvement suggestions

Format: Optimization Recommendations Report
时间线: 1 day
```

#### 🏗️ Infrastructure Maintainer — Production Readiness Check
```
Activate Infrastructure Maintainer for production readiness on [PROJECT].

交付物 required:
1. Production environment validation:
   - All 服务s healthy and 响应
   - Auto-扩展 configured and tested
   - Load balancer configuration verified
   - SSL/TLS certificates valid
2. Monitoring validation:
   - All critical metrics 是 collected
   - Alert rules configured and tested
   - 仪表板 access verified
   - Log aggregation working
3. Disaster recovery validation:
   - Backup systems operational
   - Recovery procedures documented and tested
   - Failover mechanisms verified
4. 安全 validation:
   - Firewall rules reviewed
   - Access controls verified
   - Secrets management confirmed
   - Vulnerability scan clean

Format: Infrastructure Readiness Report
时间线: 1 day
```

### Step 3: Final Judgment (Day 5-7, Sequential)

#### 🔍 Reality Checker — THE FINAL VERDICT
```
Activate Reality Checker for final 集成测试 on [PROJECT].

MANDATORY PROCESS — DO NOT SKIP:

Step 1: Reality Check Commands
- Verify what was actually built (ls, grep for claimed features)
- Cross-check claimed features against specification
- Run comprehensive screenshot capture
- 审查 all evidence from Step 1 and Step 2

Step 2: QA Cross-Validation
- 审查 Evidence Collector 查找s
- Cross-reference with API Tester results
- Verify Performance Benchmarker data
- Confirm 法律合规 Checker 查找s

Step 3: End-to-End System Validation
- Test COMPLETE 用户旅程s (not individual features)
- Verify responsive behavior across ALL devices
- Check interaction flows 端到端
- 审查 actual performance data

Step 4: Specification Reality Check
- Quote EXACT text from original specification
- Compare with ACTUAL implementation evidence
- Document EVERY gap between spec and reality
- No assumptions — evidence only

VERDICT OPTIONS:
- READY: Overwhelming evidence of production readiness (rare first pass)
- NEEDS WORK: Specific issues identified with fix list (expected)
- NOT READY: Major architectural issues requiring Phase 1/2 revisit

Format: Reality-Based Integration Report
Default: NEEDS WORK unless proven otherwise
```

## Quality Gate — THE FINAL GATE

| # | Criterion | Threshold | Evidence Required |
|---|-----------|-----------|-------------------|
| 1 | User journeys complete | All critical paths working 端到端 | Reality Checker screenshots |
| 2 | Cross-device consistency | Desktop + Tablet + Mobile all working | Responsive screenshots |
| 3 | Performance certified | P95 < 200ms, LCP < 2.5s, 正常运行时间 > 99.9% | Performance Benchmarker report |
| 4 | 安全 validated | Zero critical vulnerabilities | 安全 scan + compliance report |
| 5 | Compliance certified | All regulatory requirements met | 法律合规 Checker report |
| 6 | Specification compliance | 100% of spec requirements implemented | Point-by-point verification |
| 7 | Infrastructure ready | Production environment validated | Infrastructure Maintainer report |

## Gate Decision

**Sole authority**: Reality Checker

### If READY (proceed to Phase 5):
```markdown
## Phase 4 → Phase 5 交接 Package

### For Launch Team:
- Reality Checker certification report
- Performance certification
- Compliance certification
- Infrastructure readiness report
- Known limitations (if any)

### For 增长 Hacker:
- Product ready for users
- Feature list for marketing messaging
- Performance data for credibility

### For DevOps Automator:
- Production 部署 approved
- Blue-green 部署 plan
- Rollback procedures confirmed
```

### If NEEDS WORK (return to Phase 3):
```markdown
## Phase 4 → Phase 3 Return Package

### Fix List (from Reality Checker):
1. [Critical Issue 1]: [Description + evidence + fix instruction]
2. [Critical Issue 2]: [Description + evidence + fix instruction]
3. [High Issue 1]: [Description + evidence + fix instruction]
...

### Process:
- Issues enter Dev↔QA loop (Phase 3 mechanics)
- Each fix must pass Evidence Collector QA
- When all fixes complete → Return to Phase 4 Step 3
- Reality Checker re-evaluates with updated evidence

### Expected: 2-3 revision cycles is normal
```

### If NOT READY (return to Phase 1/2):
```markdown
## Phase 4 → Phase 1/2 Return Package

### Architectural Issues Identified:
1. [Fundamental Issue]: [Why it can't be fixed in Phase 3]
2. [Structural Problem]: [What needs to change at architecture level]

### Recommended Action:
- [ ] Revise system architecture (Phase 1)
- [ ] Rebuild foundation (Phase 2)
- [ ] Descope and redefine (Phase 1)

### Studio Producer Decision Required
```

---

*Phase 4 is complete when the Reality Checker issues a READY verdict with overwhelming evidence. NEEDS WORK is the expected first-pass result — it means the system is working but needs polish.*
