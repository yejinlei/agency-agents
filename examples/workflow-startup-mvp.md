# Multi-Agent 工作流程: Startup MVP

> A step-by-step example of how to coordinate multiple agents to go from idea to shipped MVP.

## The Scenario

You're building a SaaS MVP — a team retrospective tool for remote teams. You have 4 weeks to ship a working product with user signups, a core feature, and a landing page.

## Agent Team

| Agent | Role in this workflow |
|-------|---------------------|
| Sprint Prioritizer | Break the project into weekly sprints |
| 用户体验研究er | Validate the idea with quick user interviews |
| Backend Architect | Design the API and data model |
| Frontend Developer | Build the React app |
| Rapid Prototyper | Get the first version running fast |
| 增长 Hacker | Plan launch strategy while 构建 |
| Reality Checker | Gate each milestone before moving on |

## The 工作流程

### Week 1: Discovery + 架构

**第一步 — Activate Sprint Prioritizer**

```
Activate Sprint Prioritizer.

Project: RetroBoard — a real-time team retrospective tool for remote teams.
时间线: 4 weeks to MVP launch.
Core features: user auth, create retro boards, add cards, vote, action items.
Constraints: solo developer, React + Node.js stack, deploy to Vercel + Railway.

Break this into 4 weekly sprints with clear deliverables and acceptance criteria.
```

**Step 2 — Activate 用户体验研究er (in parallel)**

```
Activate 用户体验研究er.

I'm 构建 a team retrospective tool for remote teams (5-20 people).
Competitors: EasyRetro, Retrium, Parabol.

Run a quick competitive analysis and identify:
1. What features are table stakes
2. Where competitors fall short
3. One differentiator we could own

Output a 1-page research brief.
```

**第三步 — Hand off to Backend Architect**

```
Activate Backend Architect.

Here's our sprint plan: [paste Sprint Prioritizer output]
Here's our research brief: [paste 用户体验研究er output]

Design the API and database schema for RetroBoard.
Stack: Node.js, Express, PostgreSQL, Socket.io for real-time.

Deliver:
1. Database schema (SQL)
2. REST API 端点 list
3. WebSocket events for real-time board updates
4. Auth strategy recommendation
```

### Week 2: Build Core Features

**第四步 — Activate Frontend Developer + Rapid Prototyper**

```
Activate Frontend Developer.

Here's the API spec: [paste Backend Architect output]

Build the RetroBoard React app:
- Stack: React, TypeScript, Tailwind, Socket.io-client
- Pages: Login, 仪表板, Board view
- Components: RetroCard, VoteButton, ActionItem, BoardColumn

Start with the Board view — it's the core experience.
Focus on real-time: when one user adds a card, everyone sees it.
```

**第五步 — Reality Check at midpoint**

```
Activate Reality Checker.

We're at week 2 of a 4-week MVP build for RetroBoard.

Here's what we have so far:
- Database schema: [paste]
- API 端点: [paste]
- Frontend components: [paste]

Evaluate:
1. Can we realistically ship in 2 more weeks?
2. What should we cut to make the 截止日期?
3. Any 技术债务 that will bite us at launch?
```

### Week 3: Polish + Landing Page

**Step 6 — Frontend Developer continues, 增长 Hacker starts**

```
Activate 增长 Hacker.

Product: RetroBoard — team retrospective tool, launching in 1 week.
Target: 工程 managers and scrum masters at remote-first companies.
Budget: $0 (organic launch only).

Create a launch plan:
1. Landing page copy (hero, features, CTA)
2. Launch channels (Product Hunt, Reddit, Hacker News, Twitter)
3. Day-by-day launch sequence
4. 指标 to track in week 1
```

### Week 4: Launch

**第七步 — Final Reality Check**

```
Activate Reality Checker.

RetroBoard is ready to launch. Evaluate production readiness:

- Live URL: [url]
- Test accounts created: yes
- Error 监控: Sentry configured
- Database backups: daily automated

Run through the launch checklist and give a GO / NO-GO decision.
Require evidence for each criterion.
```

## Key Patterns

1. **Sequential 交接**: Each agent's output becomes the next agent's input
2. **Parallel work**: 用户体验研究er and Sprint Prioritizer can run simultaneously in Week 1
3. **Quality gates**: Reality Checker at midpoint and before launch prevents shipping broken code
4. **Context passing**: Always paste previous agent outputs into the next prompt — agents don't share memory

## Tips

- Copy-paste agent outputs between steps — don't summarize, use the full output
- If a Reality Checker flags an issue, loop back to the relevant specialist to fix it
- Keep the Orchestrator agent in mind for 自动化 this flow once you're comfortable with the manual version
