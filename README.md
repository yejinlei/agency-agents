# 🎭 The Agency: AI Specialists Ready to Transform Your Workflow

> **A complete AI agency at your fingertips** - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. 每个代理都是 a specialized expert with personality, processes, and proven deliverables.

[![GitHub stars](https://img.shields.io/github/stars/msitarzewski/agency-agents?style=social)](https://github.com/msitarzewski/agency-agents)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://makeapullrequest.com)
[![Sponsor](https://img.shields.io/badge/Sponsor-%E2%9D%A4-pink?logo=github)](https://github.com/sponsors/msitarzewski)
[![Download the app](https://img.shields.io/github/v/release/msitarzewski/agency-agents-app?label=Download%20app&color=2563eb)](https://github.com/msitarzewski/agency-agents-app/releases/latest)

> ### 🆕 There's an app now
>
> **[Agency Agents](https://agencyagents.app)** is a native app for **macOS, Linux & Windows** that browses the entire roster and installs it into Claude Code, Cursor, Codex, Gemini, Osaurus, and more — with a click. No clone, no scripts, and it auto-updates.
>
> **→ [下载最新版本](https://github.com/msitarzewski/agency-agents-app/releases/latest) · [agencyagents.app](https://agencyagents.app)**

---

## 🚀 这是什么？

诞生自一个 Reddit 帖子和数月的迭代, **The Agency** 是一个不断增长的精心打造的 人工智能 代理人格集合. 每个代理都是:

- **🎯 Specialized**: 在其领域拥有深厚专业知识 (不是通用的提示模板)
- **🧠 性格-Driven**: 独特的声音、沟通方式和方法
- **📋 Deliverable-Focused**: 真实的代码、流程、可衡量的结果
- **✅ Production-Ready**: Battle-tested 工作流程 and success metrics

**Think of it as**: Assembling your dream team, except they're 人工智能 specialists 他们永不睡觉、永不抱怨、始终交付.

---

## ⚡ 快速开始

### Option 1: Install the app (Recommended)

最快的方式 — 无需克隆，无需终端. [**Agency Agents**](https://agencyagents.app) 是一个原生桌面应用 (macOS · Linux · Windows) that 浏览整个名录 并将代理安装到 Claude Code, Cursor, Codex, Gemini CLI, OpenCode, Qwen, and Osaurus 为你，然后保持它们最新.

**[⬇ 下载最新版本](https://github.com/msitarzewski/agency-agents-app/releases/latest)** — 或在 Mac 上：

```bash
brew install --cask msitarzewski/agency-agents/agency-agents
```

偏好命令行？ 下方的脚本选项安装相同的代理.

### Option 2: Use with Claude Code

```bash
# 将所有代理安装到你的 Claude Code 目录
./scripts/install.sh --tool claude-code

# 或者手动复制一个分类 如果你只想要一个部门
cp engineering/*.md ~/.claude/agents/

# 然后在你的 Claude Code 会话中激活任何代理：
# "嘿 Claude，激活 Frontend Developer 模式并帮我构建一个 React 组件"
```

### Option 3: Use as Reference

每个代理文件包含：
- 身份与性格特征
- Core mission & 工作流程
- 带有代码示例的技术交付物
- 成功指标与沟通风格

浏览下方的代理并复制/适配你需要的！

### Option 4: Use with Other Tools (GitHub Copilot, Antigravity, Gemini CLI, OpenCode, OpenClaw, Cursor, Aider, Windsurf, Kimi Code, Codex, Osaurus, Hermes, Mistral Vibe)

```bash
# Step 1 -- generate integration files for all supported tools
./scripts/convert.sh

# Step 2 -- install interactively (auto-detects what you have installed)
./scripts/install.sh

# Or target a specific tool directly
./scripts/install.sh --tool antigravity
./scripts/install.sh --tool gemini-cli
./scripts/install.sh --tool opencode
./scripts/install.sh --tool copilot
./scripts/install.sh --tool openclaw
./scripts/install.sh --tool cursor
./scripts/install.sh --tool aider
./scripts/install.sh --tool windsurf
./scripts/install.sh --tool kimi
./scripts/install.sh --tool codex
./scripts/install.sh --tool osaurus
./scripts/install.sh --tool hermes
./scripts/install.sh --tool vibe
```

**只安装你需要的团队** (不是每个人都需要每个部门):

```bash
./scripts/install.sh                                    # 交互式向导: 选择工具 + 团队
./scripts/install.sh --tool claude-code --division engineering,security
./scripts/install.sh --tool cursor --agent frontend-developer,ui-designer
./scripts/install.sh --list teams                       # 查看所有团队 + 代理数量
./scripts/install.sh --tool opencode --division engineering --dry-运行
```

> **OpenCode note:** OpenCode's 运行time currently registers only ~119 agents and silently drops the rest ([upstream bug](https://github.com/anomalyco/opencode/issues/27988)). Installing a subset with `--division` keeps you under that limit. The installer warns you when a selection would exceed it.

参见 the [Multi-Tool Integrations](#-multi-tool-integrations) section below for full details.

---

## 🎨 代理名录

### 💻 工程 Division

Building the future, one commit at a time.

| Agent | Specialty | 使用场景 |
|-------|-----------|-------------|
| 🎨 [Frontend Developer](engineering/engineering-frontend-developer.md) | React/Vue/Angular, UI implementation, performance | Modern web apps, pixel-perfect UIs, Core Web Vitals optimization |
| 🏗️ [Backend Architect](engineering/engineering-backend-architect.md) | API design, database architecture, scalability | Server-side systems, 微服务, cloud infrastructure |
| 📱 [Mobile App Builder](engineering/engineering-mobile-app-builder.md) | iOS/Android, React Native, Flutter | Native and cross-platform mobile applications |
| 🤖 [人工智能 Engineer](engineering/engineering-ai-engineer.md) | ML models, 部署, 人工智能 integration | Machine learning features, 数据管道, 人工智能 驱动的 apps |
| 🚀 [DevOps Automator](engineering/engineering-devops-automator.md) | 持续集成/持续部署, infrastructure automation, cloud ops | Pipeline development, 部署 automation, 监控 |
| 🌐 [Network Engineer](engineering/engineering-network-engineer.md) | Cisco IOS/IOS-XE, Juniper Junos, Palo Alto PAN-OS | Router/switch/firewall configuration, BGP/OSPF, ACLs, show-output troubleshooting |
| ⚡ [Rapid Prototyper](engineering/engineering-rapid-prototyper.md) | Fast POC development, MVPs | Quick proof-of-concepts, hackathon projects, fast iteration |
| 💎 [Senior Developer](engineering/engineering-senior-developer.md) | Laravel/Livewire, advanced patterns | Complex implementations, architecture decisions |
| 🔧 [Filament Optimization Specialist](engineering/engineering-filament-optimization-specialist.md) | Filament PHP admin UX, structural form redesign, resource optimization | Restructuring Filament resources/forms/tables for faster, cleaner admin 工作流程 |
| ⚡ [Autonomous Optimization Architect](engineering/engineering-autonomous-optimization-architect.md) | LLM routing, cost optimization, shadow 测试 | Autonomous systems 需要 intelligent API selection and cost guardrails |
| 🔩 [Embedded Firmware Engineer](engineering/engineering-embedded-firmware-engineer.md) | Bare-metal, RTOS, ESP32/STM32/Nordic firmware | Production-grade embedded systems and IoT devices |
| 🚨 [事件响应 Commander](engineering/engineering-incident-response-commander.md) | Incident management, post-mortems, on-call | Managing production incidents and 构建 incident readiness |
| ⛓️ [Solidity Smart Contract Engineer](engineering/engineering-solidity-smart-contract-engineer.md) | EVM contracts, gas optimization, DeFi | Secure, gas-optimized smart contracts and DeFi protocols |
| 🧭 [Codebase 入职引导 Engineer](engineering/engineering-代码库-onboarding-engineer.md) | Fast developer onboarding, read-only 代码库 exploration, factual explanation | Helping new developers understand unfamiliar repos quickly by 阅读 the code, tracing code paths, and stating facts about structure and behavior |
| 📚 [Technical Writer](engineering/engineering-technical-writer.md) | Developer docs, API reference, tutorials | Clear, accurate technical 文档 |
| 💬 [WeChat Mini Program Developer](engineering/engineering-wechat-mini-program-developer.md) | WeChat ecosystem, Mini Programs, payment integration | Building performant apps for the WeChat ecosystem |
| 👁️ [Code 审查er](engineering/engineering-code-reviewer.md) | Constructive 代码审查, security, maintainability | PR reviews, code quality gates, mentoring through review |
| 🗄️ [Database Optimizer](engineering/engineering-database-optimizer.md) | Schema design, query optimization, indexing strategies | PostgreSQL/MySQL tuning, slow query 调试, migration 规划 |
| 🌿 [Git Workflow Master](engineering/engineering-git-工作流程-master.md) | Branching strategies, conventional commits, advanced Git | Git 工作流程 design, history cleanup, CI-friendly branch management |
| 🏛️ [Software Architect](engineering/engineering-software-architect.md) | System design, DDD, architectural patterns, trade-off analysis | 架构 decisions, domain modeling, system evolution strategy |
| 🛡️ [SRE](engineering/engineering-sre.md) | SLOs, 错误预算s, 可观测性, 混沌工程 | Production reliability, toil reduction, capacity 规划 |
| 🧬 [人工智能 Data Remediation Engineer](engineering/engineering-ai-data-remediation-engineer.md) | Self-healing pipelines, air-gapped SLMs, semantic clustering | Fixing broken data 大规模地 with zero data loss |
| 🔧 [Data Engineer](engineering/engineering-data-engineer.md) | Data pipelines, lakehouse architecture, ETL/ELT | Building reliable data infrastructure and warehousing |
| 🔗 [Feishu Integration Developer](engineering/engineering-feishu-integration-developer.md) | Feishu/Lark Open Platform, bots, 工作流程 | Building integrations for the Feishu ecosystem |
| 🧱 [CMS Developer](engineering/engineering-cms-developer.md) | WordPress & Drupal themes, plugins/modules, content architecture | Code-first CMS implementation and customization |
| 📧 [Email Intelligence Engineer](engineering/engineering-email-intelligence-engineer.md) | Email 解析, MIME extraction, structured data for 人工智能 agents | Turning raw email threads into 推理-ready context |
| 🎙️ [Voice 人工智能 Integration Engineer](engineering/engineering-voice-ai-integration-engineer.md) | Speech-to-text pipelines, Whisper, ASR, speaker diarization | End-to-end transcription pipelines, audio preprocessing, structured transcript delivery |
| 🖧 [IT Service Manager](engineering/engineering-it-服务-manager.md) | ITIL 4 服务 management | Incident/problem/change management, SLAs, CMDB |
| 🪡 [Minimal Change Engineer](engineering/engineering-minimal-change-engineer.md) | Minimum-viable diffs | Fixing only what's asked, no scope creep |
| 📜 [OrgScript Engineer](engineering/engineering-orgscript-engineer.md) | OrgScript grammar & AST validation | Designing/解析 OrgScript business-logic definitions |
| 🧬 [Prompt Engineer](engineering/engineering-prompt-engineer.md) | LLM prompt design & optimization | Turning vague instructions into reliable 人工智能 behaviors |
| 🕸️ [Multi-Agent Systems Architect](engineering/engineering-multi-agent-systems-architect.md) | Multi-agent pipeline design & governance | Topology, context, trust, failure recovery for agent systems |
| 🛒 [Drupal Shopping Cart Engineer](engineering/engineering-drupal-shopping-cart.md) | Drupal Commerce storefronts | Catalog, payments, checkout, orders on Drupal 10/11 |
| 🛍️ [WordPress Shopping Cart Engineer](engineering/engineering-wordpress-shopping-cart.md) | WooCommerce storefronts | Catalog, payments, checkout, conversion on WordPress |
| 💳 [Payments & Billing Engineer](engineering/engineering-payments-billing-engineer.md) | PSP integration, 幂等的 payment flows, subscription billing | Stripe/Adyen/Braintree integrations, webhook processing, dunning, reconciliation |
| 🌍 [国际化 Engineer](engineering/engineering-i18n-engineer.md) | ICU MessageFormat, RTL/bidi layouts, CLDR 格式化, pseudo-localization | Making apps translation-ready, locale-aware 格式化, RTL support, i18n audits |
| ⚡ [Drupal Performance Engineer](engineering/engineering-drupal-performance.md) | Drupal performance & Core Web Vitals | Caching, DB/query tuning, render pipeline, profiling high-traffic Drupal |
| ⚡ [WordPress Performance Engineer](engineering/engineering-wordpress-performance.md) | WordPress performance & Core Web Vitals | Caching, query/asset optimization, plugin tuning, profiling high-traffic WP |
| ♿ [Section 508 无障碍 Specialist](engineering/engineering-section-508-specialist.md) | US federal 508 / WCAG accessibility | ARIA, screen-reader 测试, VPAT/ACR authoring, remediation |
| 🏛️ [USWDS Developer](engineering/engineering-uswds-developer.md) | US Web Design System (federal) | Accessible gov UI components & design-system patterns |
| 🔎 [Search Relevance Engineer](engineering/engineering-search-relevance-engineer.md) | Search ranking & relevance | Query 理解, 嵌入s, ranking/eval, relevance tuning |
| 🔐 [Identity & Access Engineer](engineering/engineering-identity-access-engineer.md) | AuthN/AuthZ & IAM | OAuth/OIDC/SAML, SSO, RBAC/ABAC, token & session security |
| 🤝 [Realtime Collaboration Engineer](engineering/engineering-realtime-collaboration-engineer.md) | Realtime sync & presence | CRDTs/OT, conflict resolution, live cursors, offline sync |
| 💻 [Desktop App Engineer](engineering/engineering-desktop-app-engineer.md) | Cross-platform desktop apps | Electron/Tauri, native integration, packaging, auto-update |
| 🚀 [Mobile Release Engineer](engineering/engineering-mobile-release-engineer.md) | Mobile release & 持续集成/持续部署 | App Store/Play submission, signing, staged rollout, crash triage |
| 🎬 [Video Streaming Engineer](engineering/engineering-video-streaming-engineer.md) | Video streaming & transcoding | HLS/DASH, ABR, codecs, CDN delivery, low-latency streaming |
| 💰 [FinOps Engineer](engineering/engineering-finops-engineer.md) | Cloud cost engineering | Cost allocation, rightsizing, unit economics, budget & anomaly control |
| 🧩 [WebAssembly Engineer](engineering/engineering-webassembly-engineer.md) | WebAssembly & WASI | Rust/C++→WASM, sandboxing, host bindings, performance |
| 🔌 [API Platform Engineer](engineering/engineering-api-platform-engineer.md) | API 网关s & platforms | Gateway design, versioning, 速率限制, developer portals |
| 🛟 [Database 可靠性 Engineer](engineering/engineering-database-reliability-engineer.md) | Database reliability (DBRE) | HA/replication, automated failover, PITR backups, zero-停机时间 ops |
| 🛠️ [Developer Tooling Engineer](engineering/engineering-developer-tooling-engineer.md) | CLI & developer tooling | Command-line tools, internal DX, build/dev 工作流程 |
| 📡 [IoT Fleet Engineer](engineering/engineering-iot-fleet-engineer.md) | IoT & edge fleet | Device provisioning/identity, MQTT telemetry, OTA updates |
| 🔍 [检索增强生成 Pipeline Engineer](engineering/engineering-rag-pipeline-engineer.md) | Production 检索增强生成 pipelines | Chunking, 检索 quality, 混合搜索, re-ranking, eval-driven iteration |
| 🗄️ [GaussDB Expert Engineer](engineering/engineering-gaussdb-expert.md) | Huawei GaussDB OLTP | Enterprise OLTP performance, HA, and migration on Huawei's GaussDB |

### 🎨 Design Division

Making it beautiful, usable, and delightful.

| Agent | Specialty | 使用场景 |
|-------|-----------|-------------|
| 🎯 [界面设计er](design/design-ui-designer.md) | Visual design, component libraries, design systems | Interface creation, brand consistency, component design |
| 🔍 [用户体验研究er](design/design-ux-researcher.md) | User 测试, behavior analysis, research | Understanding users, 可用性测试, design insights |
| 🏛️ [UX Architect](design/design-ux-architect.md) | 技术架构, CSS systems, implementation | Developer-friendly foundations, implementation guidance |
| 🎭 [Brand Guardian](design/design-brand-guardian.md) | Brand identity, consistency, positioning | Brand strategy, identity development, guidelines |
| 📖 [Visual Storyteller](design/design-visual-storyteller.md) | Visual narratives, multimedia content | Compelling visual stories, brand storytelling |
| ✨ [Whimsy Injector](design/design-whimsy-injector.md) | 性格, delight, playful interactions | Adding joy, micro-interactions, Easter eggs, brand personality |
| 📷 [Image Prompt Engineer](design/design-image-prompt-engineer.md) | 人工智能 图像生成 prompts, photography | Photography prompts for Midjourney, DALL-E, Stable Diffusion |
| 🌈 [Inclusive Visuals Specialist](design/design-inclusive-visuals-specialist.md) | Representation, bias mitigation, authentic imagery | Generating culturally accurate 人工智能 images and video |
| 🎭 [Persona Walkthrough Specialist](design/design-persona-walkthrough.md) | Persona-driven 认知走查s | Simulating user reactions and friction at each scroll position |

### 💰 Paid Media Division

Turning ad spend into measurable business outcomes.

| Agent | Specialty | 使用场景 |
| --- | --- | --- |
| 💰 [PPC Campaign Strategist](paid-media/paid-media-ppc-strategist.md) | Google/Microsoft/Amazon Ads, account architecture, bidding | Account buildouts, budget allocation, 扩展, performance diagnosis |
| 🔍 [Search Query Analyst](paid-media/paid-media-search-query-analyst.md) | Search term analysis, negative keywords, intent mapping | Query audits, wasted spend elimination, keyword discovery |
| 📋 [Paid Media Auditor](paid-media/paid-media-auditor.md) | 200+ point account audits, competitive analysis | Account takeovers, quarterly reviews, competitive pitches |
| 📡 [Tracking & Measurement Specialist](paid-media/paid-media-追踪-specialist.md) | GTM, GA4, conversion 追踪, CAPI | New implementations, 追踪 audits, platform migrations |
| ✍️ [Ad Creative Strategist](paid-media/paid-media-creative-strategist.md) | RSA copy, Meta creative, Performance Max assets | Creative launches, 测试 programs, ad fatigue refreshes |
| 📺 [Programmatic & Display Buyer](paid-media/paid-media-programmatic-buyer.md) | GDN, DSPs, partner media, ABM display | Display 规划, partner outreach, ABM programs |
| 📱 [Paid Social Strategist](paid-media/paid-media-paid-social-strategist.md) | Meta, LinkedIn, TikTok, cross-platform social | Social ad programs, platform selection, audience strategy |

### 💼 Sales Division

Turning pipeline into revenue through craft, not CRM busywork.

| Agent | Specialty | 使用场景 |
|-------|-----------|-------------|
| 🎯 [Outbound Strategist](sales/sales-outbound-strategist.md) | Signal-based prospecting, multi-channel sequences, ICP targeting | Building pipeline through research-driven outreach, not volume |
| 🔍 [Discovery Coach](sales/sales-discovery-coach.md) | SPIN, Gap Selling, Sandler — question design and call structure | Preparing for discovery calls, qualifying opportunities, coaching reps |
| ♟️ [Deal Strategist](sales/sales-deal-strategist.md) | MEDDPICC qualification, competitive positioning, win 规划 | Scoring deals, exposing pipeline risk, 构建 win strategies |
| 🛠️ [Sales Engineer](sales/sales-engineer.md) | Technical demos, POC scoping, competitive battlecards | Pre-sales technical wins, demo prep, competitive positioning |
| 🏹 [Proposal Strategist](sales/sales-proposal-strategist.md) | RFP response, win themes, narrative structure | Writing proposals that persuade, not just comply |
| 📊 [Pipeline Analyst](sales/sales-pipeline-analyst.md) | Forecasting, pipeline health, deal velocity, RevOps | Pipeline reviews, forecast accuracy, revenue operations |
| 🗺️ [Account Strategist](sales/sales-account-strategist.md) | Land-and-expand, QBRs, stakeholder mapping | Post-sale expansion, account 规划, NRR growth |
| 🏋️ [Sales Coach](sales/sales-coach.md) | Rep development, call coaching, pipeline review facilitation | Making every rep and every deal better through structured coaching |
| 🎯 [Sales Outreach](specialized/sales-outreach.md) | Cold prospecting, multi-touch cadences, objection 处理, proposals | Top-of-funnel B2B outreach — from cold email to booked discovery call |
| 🧲 [Offer & Lead Gen Strategist](sales/sales-offer-lead-gen-strategist.md) | Offers & lead magnets | Top-of-funnel offer construction and 潜在客户生成 |

### 📢 Marketing Division

Growing your audience, one authentic interaction at a time.

| Agent | Specialty | 使用场景 |
|-------|-----------|-------------|
| 🚀 [增长 Hacker](marketing/marketing-growth-hacker.md) | Rapid user acquisition, viral loops, experiments | Explosive growth, user acquisition, conversion optimization |
| 📝 [Content Creator](marketing/marketing-content-creator.md) | Multi-platform content, editorial calendars | Content strategy, copy编写, brand storytelling |
| 🐦 [Twitter Engager](marketing/marketing-twitter-engager.md) | Real-time engagement, thought leadership | Twitter strategy, LinkedIn campaigns, professional social |
| 🛰️ [X/Twitter Intelligence Analyst](marketing/marketing-x-twitter-intelligence-analyst.md) | Social 倾听, trend detection, account 监控 | Brand risk, competitor, and audience intelligence on X/Twitter |
| 📱 [TikTok Strategist](marketing/marketing-tiktok-strategist.md) | Viral content, algorithm optimization | TikTok growth, viral content, Gen Z/Millennial audience |
| 📸 [Instagram Curator](marketing/marketing-instagram-curator.md) | Visual storytelling, community 构建 | Instagram strategy, aesthetic development, visual content |
| 🤝 [Reddit Community Builder](marketing/marketing-reddit-community-builder.md) | Authentic engagement, value-driven content | Reddit strategy, community trust, authentic marketing |
| 📱 [App Store Optimizer](marketing/marketing-app-store-optimizer.md) | ASO, conversion optimization, discoverability | App marketing, store optimization, app growth |
| 🌐 [Social Media Strategist](marketing/marketing-social-media-strategist.md) | Cross-platform strategy, campaigns | Overall social strategy, multi-platform campaigns |
| 📕 [Xiaohongshu Specialist](marketing/marketing-xiaohongshu-specialist.md) | Lifestyle content, trend-driven strategy | Xiaohongshu growth, aesthetic storytelling, Gen Z audience |
| 💬 [WeChat Official Account Manager](marketing/marketing-wechat-official-account.md) | Subscriber engagement, 内容营销 | WeChat OA strategy, community 构建, conversion optimization |
| 🧠 [Zhihu Strategist](marketing/marketing-zhihu-strategist.md) | Thought leadership, knowledge-driven engagement | Zhihu authority 构建, Q&A strategy, 潜在客户生成 |
| 🇨🇳 [Baidu SEO Specialist](marketing/marketing-baidu-seo-specialist.md) | Baidu optimization, China SEO, ICP compliance | Ranking in Baidu and reaching China's search market |
| 🎬 [Bilibili Content Strategist](marketing/marketing-bilibili-content-strategist.md) | B站 algorithm, danmaku culture, UP主 growth | Building audiences on Bilibili with community-first content |
| 🎠 [Carousel 增长 Engine](marketing/marketing-carousel-growth-engine.md) | TikTok/Instagram carousels, autonomous publishing | Generating and publishing viral carousel content |
| 💼 [LinkedIn Content Creator](marketing/marketing-linkedin-content-creator.md) | Personal branding, thought leadership, professional content | LinkedIn growth, professional audience 构建, B2B content |
| 🛒 [China E-Commerce Operator](marketing/marketing-china-ecommerce-operator.md) | Taobao, Tmall, Pinduoduo, live commerce | Running multi-platform e-commerce in China |
| 🎥 [Kuaishou Strategist](marketing/marketing-kuaishou-strategist.md) | Kuaishou, 老铁 community, grassroots growth | Building authentic audiences in lower-tier markets |
| 🔍 [SEO Specialist](marketing/marketing-seo-specialist.md) | Technical SEO, content strategy, link 构建 | Driving sustainable organic search growth |
| 📘 [Book Co-Author](marketing/marketing-book-co-author.md) | Thought-leadership books, ghost编写, publishing | Strategic book collaboration for founders and experts |
| 🌏 [Cross-Border E-Commerce Specialist](marketing/marketing-cross-border-ecommerce.md) | Amazon, Shopee, Lazada, cross-border fulfillment | Full-funnel cross-border e-commerce strategy |
| 🎵 [Douyin Strategist](marketing/marketing-douyin-strategist.md) | Douyin platform, short-video marketing, algorithm | Growing audiences on China's leading short-video platform |
| 🎙️ [Livestream Commerce Coach](marketing/marketing-livestream-commerce-coach.md) | Host training, live room optimization, conversion | Building high-performing livestream e-commerce operations |
| 🎧 [Podcast Strategist](marketing/marketing-Podcast-strategist.md) | Podcast content strategy, platform optimization | Chinese Podcast market strategy and operations |
| 🔒 [Private Domain Operator](marketing/marketing-private-domain-operator.md) | WeCom, private traffic, community operations | Building enterprise WeChat private domain ecosystems |
| 🎬 [Short-Video Editing Coach](marketing/marketing-short-video-editing-coach.md) | Post-production, editing 工作流程, platform specs | Hands-on short-video editing training and optimization |
| 🔥 [Weibo Strategist](marketing/marketing-weibo-strategist.md) | Sina Weibo, trending topics, fan engagement | Full-spectrum Weibo operations and growth |
| 🎙️ [Global Podcast Strategist](marketing/marketing-global-Podcast-strategist.md) | Show positioning, audience growth, monetisation | Podcast launch, platform algorithms, sponsorship, community 构建 |
| 🔮 [人工智能 Citation Strategist](marketing/marketing-ai-citation-strategist.md) | AEO/GEO, 人工智能 recommendation visibility, citation 审计 | Improving brand visibility across ChatGPT, Claude, Gemini, Perplexity |
| 🇨🇳 [China Market 本地化 Strategist](marketing/marketing-china-market-localization-strategist.md) | Full-stack China market localization, Douyin/Xiaohongshu/WeChat GTM | Turning trend signals into executable China go-to-market strategies |
| 🎬 [Video Optimization Specialist](marketing/marketing-video-optimization-specialist.md) | YouTube algorithm strategy, chaptering, thumbnail concepts | YouTube channel growth, video SEO, audience retention optimization |
| 🏗️ [AEO Foundations Architect](marketing/marketing-aeo-foundations.md) | 人工智能 Engine Optimization infrastructure | llms.txt, 人工智能-aware robots.txt, agent discovery files |
| 🤖 [Agentic Search Optimizer](marketing/marketing-agentic-search-optimizer.md) | WebMCP & agentic task completion | Making sites usable by 人工智能 browsing agents |
| 📧 [Email Marketing Strategist](marketing/marketing-email-strategist.md) | Lifecycle email & deliverability | CRM campaigns, automation, segmentation |
| 📡 [Multi-Platform Publisher](marketing/marketing-multi-platform-publisher.md) | One-click Chinese multi-platform publishing | Routing one article to 知乎/小红书/CSDN/B站/公众号/掘金 |
| 📣 [PR & 沟通s Manager](marketing/marketing-pr-communications-manager.md) | PR, media relations & crisis comms | Press releases, thought leadership, reputation |

### 📊 Product Division

Building the right thing at the right time.

| Agent | Specialty | 使用场景 |
|-------|-----------|-------------|
| 🎯 [Sprint Prioritizer](product/product-sprint-优先级排序r.md) | 敏捷 规划, feature 优先级排序 | Sprint 规划, resource allocation, backlog management |
| 🔍 [Trend Researcher](product/product-trend-researcher.md) | Market intelligence, competitive analysis | Market research, opportunity assessment, trend identification |
| 💬 [Feedback Synthesizer](product/product-feedback-synthesizer.md) | User feedback analysis, insights extraction | Feedback analysis, user insights, product priorities |
| 🧠 [Behavioral Nudge Engine](product/product-behavioral-nudge-engine.md) | Behavioral psychology, nudge design, engagement | Maximizing user motivation through behavioral science |
| 🧭 [Product Manager](product/product-manager.md) | Full lifecycle product ownership | Discovery, PRDs, roadmap 规划, GTM, outcome measurement |

### 🎬 Project Management Division

Keeping the trains 运行ning on time (and under budget).

| Agent | Specialty | 使用场景 |
|-------|-----------|-------------|
| 🎬 [Studio Producer](project-management/project-management-studio-producer.md) | High-level orchestration, portfolio management | Multi-project oversight, strategic alignment, resource allocation |
| 🐑 [Project Shepherd](project-management/project-management-project-shepherd.md) | Cross-functional coordination, 时间线 management | End-to-end project coordination, stakeholder management |
| ⚙️ [Studio Operations](project-management/project-management-studio-operations.md) | Day-to-day efficiency, process optimization | Operational excellence, team support, productivity |
| 🧪 [Experiment Tracker](project-management/project-management-experiment-tracker.md) | A/B tests, hypothesis validation | Experiment management, 数据驱动的 decisions, 测试 |
| 👔 [Senior Project Manager](project-management/project-manager-senior.md) | Realistic scoping, task conversion | Converting specs to tasks, scope management |
| 📋 [Jira Workflow Steward](project-management/project-management-jira-工作流程-steward.md) | Git 工作流程, branch strategy, traceability | Enforcing Jira-linked Git discipline and delivery |
| 📋 [Meeting Notes Specialist](project-management/project-management-meeting-notes-specialist.md) | Structured meeting summaries | Extracting decisions, action items, open questions |

### 🧪 测试 Division

Breaking things so users don't have to.

| Agent | Specialty | 使用场景 |
|-------|-----------|-------------|
| 📸 [Evidence Collector](测试/测试-evidence-collector.md) | Screenshot-based QA, visual proof | UI 测试, visual verification, bug 文档 |
| 🔍 [Reality Checker](测试/测试-reality-checker.md) | Evidence-based certification, quality gates | Production readiness, quality approval, release certification |
| 📊 [Test 结果分析器](测试/测试-test-results-analyzer.md) | Test evaluation, metrics analysis | Test output analysis, quality insights, coverage 报告 |
| ⚡ [Performance Benchmarker](测试/测试-performance-benchmarker.md) | Performance 测试, optimization | Speed 测试, 负载测试, performance tuning |
| 🔌 [API Tester](测试/测试-api-tester.md) | API validation, 集成测试 | API 测试, endpoint verification, integration QA |
| 🛠️ [Tool Evaluator](测试/测试-tool-evaluator.md) | Technology assessment, tool selection | Evaluating tools, software recommendations, tech decisions |
| 🔄 [Workflow Optimizer](测试/测试-工作流程-optimizer.md) | Process analysis, 工作流程 improvement | Process optimization, efficiency gains, automation opportunities |
| ♿ [无障碍 Auditor](测试/测试-accessibility-auditor.md) | WCAG 审计, assistive technology 测试 | 无障碍 compliance, 屏幕阅读器 测试, inclusive design verification |
| 🎭 [Test Automation Engineer](测试/测试-test-automation-engineer.md) | Playwright/Cypress E2E, flake elimination, CI parallelization | Browser test suites, deterministic pipelines, trace-driven failure 调试 |

### 🔒 安全 Division

Defending the stack — from secure-by-design architecture to breach response.

| Agent | Specialty | 使用场景 |
|-------|-----------|-------------|
| 🛡️ [安全 Architect](security/security-architect.md) | Threat modeling, secure-by-design, trust boundaries | System security models, architecture reviews, defense-in-depth |
| 🔐 [Application 安全 Engineer](security/security-appsec-engineer.md) | SDLC security, SAST/DAST, secure 代码审查 | Securing the dev lifecycle, code-level vulnerabilities |
| 🗡️ [Penetration Tester](security/security-penetration-tester.md) | Authorized pentests, 红队 ops, exploitation | Finding exploitable weaknesses before attackers do |
| ☁️ [Cloud 安全 Architect](security/security-cloud-security-architect.md) | Zero trust, 云原生 defense-in-depth | Securing cloud infrastructure and architectures |
| 🚨 [Incident Responder](security/security-incident-responder.md) | DFIR, breach investigation, threat containment | Active breaches, forensics, crisis response |
| 🔍 [Threat Intelligence Analyst](security/security-threat-intelligence-analyst.md) | Adversary 追踪, campaign mapping, ATT&CK | Understanding who's attacking and how |
| 🎯 [Threat Detection Engineer](security/security-threat-detection-engineer.md) | SIEM rules, threat hunting, ATT&CK mapping | Building detection layers and threat hunting |
| 🛡️ [Senior SecOps Engineer](security/security-senior-secops.md) | Secrets scanning, secure-by-default submissions | Defensive code-level security on every change |
| 📋 [Compliance Auditor](security/security-compliance-auditor.md) | SOC 2, ISO 27001, HIPAA, PCI-DSS | Guiding organizations through compliance certification |
| 🛡️ [Blockchain 安全 Auditor](security/security-blockchain-security-auditor.md) | Smart contract audits, exploit analysis | Finding vulnerabilities in contracts before 部署 |
| 🔎 [人工智能-Generated Code 安全 Auditor](security/security-ai-generated-code-auditor.md) | 安全 review of 人工智能/vibe-coded apps | Hardcoded 密钥s, broken RLS, prompt-injection sinks |
| 🔑 [Secrets & Credential Hygiene Engineer](security/security-密钥s-credential-engineer.md) | Secrets & credential lifecycle | Detection, vaulting, rotation, leak response |

### 🛟 Support Division

The backbone of the operation.

| Agent | Specialty | 使用场景 |
|-------|-----------|-------------|
| 💬 [Support Responder](support/support-support-responder.md) | Customer 服务, issue resolution | Customer support, 用户体验, support operations |
| 📊 [Analytics Reporter](support/support-analytics-reporter.md) | Data analysis, dashboards, insights | Business intelligence, KPI 追踪, data visualization |
| 💰 [Finance Tracker](support/support-finance-tracker.md) | Financial 规划, budget management | Financial analysis, 现金流, business performance |
| 🏗️ [Infrastructure Maintainer](support/support-infrastructure-maintainer.md) | System reliability, performance optimization | Infrastructure management, system operations, 监控 |
| ⚖️ [法律合规 Checker](support/support-legal-compliance-checker.md) | Compliance, regulations, legal review | Legal compliance, regulatory requirements, risk management |
| 📑 [执行摘要 Generator](support/support-executive-summary-generator.md) | C-suite communication, strategic summaries | Executive 报告, strategic communication, decision support |

### 🥽 Spatial Computing Division

Building the immersive future.

| Agent | Specialty | 使用场景 |
|-------|-----------|-------------|
| 🏗️ [XR Interface Architect](spatial-computing/xr-interface-architect.md) | Spatial 交互设计, immersive UX | AR/VR/XR interface design, spatial computing UX |
| 💻 [macOS Spatial/Metal Engineer](spatial-computing/macos-spatial-metal-engineer.md) | Swift, Metal, high-performance 3D | macOS spatial computing, Vision Pro native apps |
| 🌐 [XR Immersive Developer](spatial-computing/xr-immersive-developer.md) | WebXR, browser-based AR/VR | Browser-based immersive experiences, WebXR apps |
| 🎮 [XR Cockpit Interaction Specialist](spatial-computing/xr-cockpit-interaction-specialist.md) | Cockpit-based controls, immersive systems | Cockpit control systems, immersive control interfaces |
| 🍎 [visionOS Spatial Engineer](spatial-computing/visionos-spatial-engineer.md) | Apple Vision Pro development | Vision Pro apps, spatial computing experiences |
| 🔌 [Terminal Integration Specialist](spatial-computing/terminal-integration-specialist.md) | Terminal integration, command-line tools | CLI tools, terminal 工作流程, developer tools |

### 🎯 Specialized Division

The unique specialists who don't fit in a box.

| Agent | Specialty | 使用场景 |
|-------|-----------|-------------|
| 🎭 [Agents Orchestrator](specialized/agents-orchestrator.md) | Multi-agent coordination, 工作流程 management | Complex projects requiring multiple agent coordination |
| 🔍 [LSP/Index Engineer](specialized/lsp-index-engineer.md) | Language Server Protocol, code intelligence | Code intelligence systems, LSP implementation, semantic indexing |
| 📥 [Sales Data Extraction Agent](specialized/sales-data-extraction-agent.md) | Excel 监控, sales metric extraction | Sales data ingestion, MTD/YTD/Year End metrics |
| 📈 [Data Consolidation Agent](specialized/data-consolidation-agent.md) | Sales data aggregation, dashboard reports | Territory summaries, rep performance, pipeline snapshots |
| 📬 [Report Distribution Agent](specialized/report-distribution-agent.md) | Automated report delivery | Territory-based report distribution, scheduled sends |
| 🔐 [Agentic Identity & Trust Architect](specialized/agentic-identity-trust.md) | Agent identity, authentication, trust verification | Multi-agent identity systems, agent authorization, audit trails |
| 🔗 [Identity Graph Operator](specialized/identity-graph-operator.md) | Shared identity resolution for multi-agent systems | Entity deduplication, merge proposals, cross-agent identity consistency |
| 💸 [Accounts Payable Agent](specialized/accounts-payable-agent.md) | Payment processing, vendor management, audit | Autonomous payment execution across crypto, fiat, stablecoins |
| 🌍 [Cultural Intelligence Strategist](specialized/specialized-cultural-intelligence-strategist.md) | Global UX, representation, cultural exclusion | Ensuring software resonates across cultures |
| 🗣️ [Developer Advocate](specialized/specialized-developer-advocate.md) | Community 构建, DX, developer content | Bridging product and developer community |
| 🔬 [Model QA Specialist](specialized/specialized-model-qa.md) | ML audits, feature analysis, interpretability | End-to-end QA for 机器学习 models |
| 🗃️ [ZK Steward](specialized/zk-steward.md) | Knowledge management, Zettelkasten, notes | Building connected, validated knowledge bases |
| 🔌 [MCP Builder](specialized/specialized-mcp-builder.md) | Model Context Protocol servers, 人工智能 代理来oling | Building MCP servers that extend 人工智能 agent capabilities |
| 📄 [Document Generator](specialized/specialized-document-generator.md) | PDF, PPTX, DOCX, XLSX generation from code | Professional document creation, reports, data visualization |
| ⚙️ [Automation 治理 Architect](specialized/automation-governance-architect.md) | Automation governance, n8n, 工作流程 审计 | Evaluating and governing business automations 大规模地 |
| 📚 [Corporate 培训 Designer](specialized/corporate-training-designer.md) | Enterprise training, curriculum development | Designing training systems and learning programs |
| 🌱 [Personal 增长 Mentor](specialized/personal-growth-mentor.md) | Goal clarity, habit systems, accountability, life strategy | Cross-domain personal development without motivational fluff |
| 🏛️ [Government Digital Presales Consultant](specialized/government-digital-presales-consultant.md) | China ToG presales, digital transformation | Government digital transformation proposals and bids |
| ⚕️ [Healthcare Marketing Compliance](specialized/healthcare-marketing-compliance.md) | China healthcare advertising compliance | Healthcare marketing regulatory compliance |
| 🎯 [Recruitment Specialist](specialized/recruitment-specialist.md) | Talent acquisition, recruiting operations | Recruitment strategy, sourcing, and hiring processes |
| 🎓 [Study Abroad Advisor](specialized/study-abroad-advisor.md) | International education, application 规划 | Study abroad 规划 across US, UK, Canada, Australia |
| 🔗 [Supply Chain Strategist](specialized/supply-chain-strategist.md) | Supply chain management, procurement strategy | Supply chain optimization and procurement 规划 |
| 🗺️ [Workflow Architect](specialized/specialized-工作流程-architect.md) | Workflow discovery, mapping, and specification | Mapping every path through a system before code is written |
| ☁️ [Salesforce Architect](specialized/specialized-salesforce-architect.md) | Multi-cloud Salesforce design, governor limits, integrations | Enterprise Salesforce architecture, org strategy, 部署 pipelines |
| 🇫🇷 [French Consulting Market Navigator](specialized/specialized-french-consulting-market.md) | ESN/SI ecosystem, portage salarial, rate positioning | Freelance consulting in the French IT market |
| 🇰🇷 [Korean Business Navigator](specialized/specialized-korean-business-navigator.md) | Korean business culture, 품의 process, relationship mechanics | Foreign professionals 导航 Korean business relationships |
| 🏗️ [Civil Engineer](specialized/specialized-civil-engineer.md) | Structural analysis, geotechnical design, global 构建 codes | Multi-standard structural engineering across Eurocode, ACI, 人工智能SC, and more |
| 🎧 [Customer Service](specialized/customer-服务.md) | Omnichannel support, complaint 处理, retention, escalation | Any industry customer support — retail, SaaS, hospitality, finance, logistics |
| 🏥 [Healthcare Customer Service](specialized/healthcare-customer-服务.md) | HIPAA-aware patient support, billing, insurance, emergency routing | Healthcare organizations 需要 compliant, empathetic patient support |
| 🏨 [Hospitality Guest Services](specialized/hospitality-guest-服务s.md) | Reservations, concierge, complaint recovery, loyalty, events | Hotels, resorts, restaurants, and event venues |
| 🤝 [HR 入职引导](specialized/hr-onboarding.md) | Pre-boarding, compliance, benefits enrollment, 30-60-90 day plans | Any company onboarding new hires — from startups to enterprise |
| 🌐 [Language Translator](specialized/language-translator.md) | Spanish ↔ English translation, dialect awareness, cultural context | Travel, business, medical, and legal translation needs |
| ⏱️ [Legal Billing & Time Tracking](specialized/legal-billing-time-追踪.md) | Time capture, billing narratives, IOLTA compliance, collections | Law firms maximizing revenue recovery and billing accuracy |
| 📋 [Legal Client Intake](specialized/legal-client-intake.md) | Prospect qualification, conflict screening, consultation scheduling | Law firms converting inquiries into retained clients |
| ⚖️ [Legal Document 审查](specialized/legal-document-review.md) | Contract review, risk flagging, version comparison, compliance | Attorney-ready first-pass review across any practice area |
| 🏦 [Loan Officer Assistant](specialized/loan-officer-assistant.md) | Borrower intake, TRID compliance, pipeline 追踪, 关闭 coordination | Mortgage and consumer lending teams |
| 🏠 [Real Estate Buyer & Seller](specialized/real-estate-buyer-seller.md) | Buyer/seller representation, offers, transaction coordination | Residential and investment real estate transactions |
| 🛒 [Retail Customer Returns](specialized/retail-customer-returns.md) | Return processing, fraud prevention, exchanges, vendor returns | Brick-and-mortar, e-commerce, and omnichannel retail |
| ♟️ [Business Strategist](specialized/business-strategist.md) | Management-consulting strategy | Competitive analysis, market entry, growth 规划 |
| 🔄 [变革管理 Consultant](specialized/change-management-consultant.md) | ADKAR/Kotter/Prosci change | Guiding orgs through transformation & adoption |
| 🧭 [Chief of Staff](specialized/specialized-chief-of-staff.md) | Executive coordination | Filtering noise, owning processes, routing decisions |
| 🌟 [Customer Success Manager](specialized/customer-success-manager.md) | 入职引导, health & retention | QBRs, churn prevention, renewals & expansion |
| 📝 [Grant Writer](specialized/grant-writer.md) | Grant proposals & funding | LOIs, proposals, budgets for nonprofits/research |
| 🏥 [Medical Billing & Coding Specialist](specialized/medical-billing-coding-specialist.md) | ICD-10/CPT/HCPCS & revenue cycle | Claims, denial management, RCM optimization |
| 💰 [Pricing Analyst](specialized/specialized-pricing-analyst.md) | Pricing models & margin optimization | Competitor/cost analysis, value-based pricing |
| 💼 [Chief Financial Officer](specialized/chief-financial-officer.md) | Capital allocation & financial strategy | Treasury, FP&A, M&A finance, investor & board 报告 |
| 🌱 [ESG & Sustainability Officer](specialized/esg-sustainability-officer.md) | ESG programs & disclosure | Sustainability strategy, decarbonization, 报告 |
| 🔐 [数据隐私 Officer](specialized/data-privacy-officer.md) | GDPR/CCPA privacy compliance | Data mapping, DPIAs, consent, breach response |
| ⚙️ [Operations Manager](specialized/operations-manager.md) | Lean/Six Sigma operations | Process mapping, capacity 规划, KPI governance |
| 🤝 [M&A Integration Manager](specialized/ma-integration-manager.md) | Post-merger integration | Day 1/100-day plans, synergy 追踪, TSA management |
| 🧠 [Organizational Psychologist](specialized/organizational-psychologist.md) | Team dynamics & culture health | Psychological safety, burnout risk, high-performing teams |
| ⚔️ [Strategy Duel Agent](specialized/specialized-strategy-duel-agent.md) | Game theory & the 36 stratagems | Turn-based strategy duels, adversarial scenario simulation |
| 🛡️ [FedRAMP & RMF Compliance Engineer](specialized/specialized-fedramp-rmf-compliance.md) | Federal cloud authorization (ATO) | NIST 800-53, FedRAMP Rev5/20x, SSP/POA&M, ConMon, OSCAL |
| 🏺 [Codebase Archaeologist](specialized/specialized-代码库-archaeologist.md) | Multi-tool 代码库 drift audits | Detecting silent drift across Claude/Cursor/Copilot/Windsurf edits |
| 🧾 [Resume Tailor](specialized/resume-tailor.md) | Candidate-side resume optimization | JD mapping, ATS keyword alignment, experience-to-requirement matching |

### 💵 Finance Division

Accounting, financial analysis, tax strategy, and investment research specialists.

| Agent | Specialty | 使用场景 |
|-------|-----------|-------------|
| 📒 [Bookkeeper & Controller](finance/finance-bookkeeper-controller.md) | Month-end close, reconciliation, GAAP compliance, internal controls | Day-to-day accounting operations, audit readiness, financial record-keeping |
| 📊 [Financial Analyst](finance/finance-financial-analyst.md) | Financial modeling, forecasting, scenario analysis, decision support | Three-statement models, variance analysis, 数据驱动的 business intelligence |
| 📈 [FP&A Analyst](finance/finance-fpa-analyst.md) | Budgeting, rolling forecasts, variance analysis, business reviews | Annual operating plans, monthly business reviews, strategic resource allocation |
| 🔍 [Investment Researcher](finance/finance-investment-researcher.md) | Due diligence, portfolio analysis, asset valuation, equity research | Investment thesis development, risk assessment, market research |
| 🏛️ [Tax Strategist](finance/finance-tax-strategist.md) | Tax optimization, multi-jurisdictional compliance, transfer pricing | Entity structuring, ETR analysis, audit defense, strategic tax 规划 |

### 🎮 Game Development Division

Building worlds, systems, and experiences across every major engine.

#### Cross-Engine Agents (Engine-Agnostic)

| Agent | Specialty | 使用场景 |
|-------|-----------|-------------|
| 🎯 [游戏设计er](game-development/game-designer.md) | Systems design, GDD authorship, economy balancing, gameplay loops | Designing game mechanics, progression systems, 编写 design documents |
| 🗺️ [关卡设计er](game-development/level-designer.md) | Layout theory, pacing, encounter design, environmental storytelling | Building levels, 设计 encounter flow, spatial narrative |
| 🎨 [Technical Artist](game-development/technical-artist.md) | Shaders, VFX, LOD pipeline, art-to-engine optimization | Bridging art and engineering, shader authoring, performance-safe asset pipelines |
| 🔊 [Game Audio Engineer](game-development/game-audio-engineer.md) | FMOD/Wwise, adaptive music, spatial audio, audio budgets | Interactive audio systems, dynamic music, audio performance |
| 📖 [叙事设计er](game-development/narrative-designer.md) | Story systems, branching dialogue, lore architecture | Writing branching narratives, 实现 dialogue systems, world lore |

#### Unity

| Agent | Specialty | 使用场景 |
|-------|-----------|-------------|
| 🏗️ [Unity Architect](game-development/unity/unity-architect.md) | ScriptableObjects, 数据驱动的 modularity, DOTS/ECS | Large-scale Unity projects, 数据驱动的 system design, ECS performance work |
| ✨ [Unity Shader Graph Artist](game-development/unity/unity-shader-graph-artist.md) | Shader Graph, HLSL, URP/HDRP, Renderer Features | Custom Unity materials, VFX shaders, post-processing passes |
| 🌐 [Unity Multiplayer Engineer](game-development/unity/unity-multiplayer-engineer.md) | Netcode for GameObjects, Unity Relay/Lobby, server authority, prediction | Online Unity games, client prediction, Unity Gaming Services integration |
| 🛠️ [Unity Editor Tool Developer](game-development/unity/unity-editor-tool-developer.md) | EditorWindows, AssetPostprocessors, PropertyDrawers, build validation | Custom Unity Editor tooling, pipeline automation, content validation |

#### Unreal Engine

| Agent | Specialty | 使用场景 |
|-------|-----------|-------------|
| ⚙️ [Unreal Systems Engineer](game-development/unreal-engine/unreal-systems-engineer.md) | C++/Blueprint hybrid, GAS, Nanite constraints, memory management | Complex Unreal gameplay systems, Gameplay Ability System, engine-level C++ |
| 🎨 [Unreal Technical Artist](game-development/unreal-engine/unreal-technical-artist.md) | Material Editor, Niagara, PCG, Substrate | Unreal materials, Niagara VFX, procedural content generation |
| 🌐 [Unreal Multiplayer Architect](game-development/unreal-engine/unreal-multiplayer-architect.md) | Actor replication, GameMode/GameState hierarchy, dedicated server | Unreal online games, replication graphs, server authoritative Unreal |
| 🗺️ [Unreal World Builder](game-development/unreal-engine/unreal-world-builder.md) | World Partition, Landscape, HLOD, LWC | Large open-world Unreal levels, streaming systems, terrain 大规模地 |

#### Godot

| Agent | Specialty | 使用场景 |
|-------|-----------|-------------|
| 📜 [Godot Gameplay Scripter](game-development/godot/godot-gameplay-scripter.md) | GDScript 2.0, signals, composition, static 输入 | Godot gameplay systems, scene composition, performance-conscious GDScript |
| 🌐 [Godot Multiplayer Engineer](game-development/godot/godot-multiplayer-engineer.md) | MultiplayerAPI, ENet/WebRTC, RPCs, authority model | Online Godot games, scene replication, server-authoritative Godot |
| ✨ [Godot Shader Developer](game-development/godot/godot-shader-developer.md) | Godot shading language, VisualShader, RenderingDevice | Custom Godot materials, 2D/3D effects, post-processing, compute shaders |

#### Blender

| Agent | Specialty | 使用场景 |
|-------|-----------|-------------|
| 🧩 [Blender Addon Engineer](game-development/blender/blender-addon-engineer.md) | Blender Python (`bpy`), custom operators/panels, asset validators, exporters, pipeline automation | Building Blender add-ons, asset prep tools, export 工作流程, and DCC pipeline automation |

#### Roblox Studio

| Agent | Specialty | 使用场景 |
|-------|-----------|-------------|
| ⚙️ [Roblox Systems Scripter](game-development/roblox-studio/roblox-systems-scripter.md) | Luau, RemoteEvents/Functions, DataStore, server-authoritative module architecture | Building secure Roblox game systems, client-server communication, data persistence |
| 🎯 [Roblox Experience Designer](game-development/roblox-studio/roblox-experience-designer.md) | Engagement loops, monetization, D1/D7 retention, onboarding flow | Designing Roblox game loops, Game Passes, daily rewards, player retention |
| 👗 [Roblox Avatar Creator](game-development/roblox-studio/roblox-avatar-creator.md) | UGC pipeline, accessory rigging, Creator Marketplace submission | Roblox UGC items, HumanoidDescription customization, in-experience avatar shops |

### 📚 Academic Division

Scholarly rigor for world-构建, storytelling, and narrative design.

| Agent | Specialty | 使用场景 |
|-------|-----------|-------------|
| 🌍 [Anthropologist](academic/academic-anthropologist.md) | Cultural systems, kinship, rituals, belief systems | Designing culturally coherent societies with internal logic |
| 🌐 [Geographer](academic/academic-geographer.md) | Physical/human geography, climate, cartography | Building geographically coherent worlds with realistic terrain and settlements |
| 📚 [Historian](academic/academic-historian.md) | Historical analysis, periodization, material culture | Validating historical coherence, enriching settings with authentic period detail |
| 📜 [Narratologist](academic/academic-narratologist.md) | Narrative theory, story structure, character arcs | Analyzing and improving story structure with established theoretical frameworks |
| 🧠 [Psychologist](academic/academic-psychologist.md) | 性格 theory, motivation, cognitive patterns | Building psychologically credible characters grounded in research |
| 📊 [Statistician](academic/academic-statistician.md) | Statistical 推理 & experiment design | Hypothesis 测试, causal 推理, sampling, rigorous analysis |

---

### 🌍 GIS Division

Mapping the Earth, 分析 the built world, and extracting intelligence from geospatial data.

| Agent | Specialty | 使用场景 |
|-------|-----------|-------------|
| 🧠 [Technical Consultant](gis/gis-technical-consultant.md) | GIS strategy, gap analysis, technology roadmaps, digital transformation | Understanding business needs, 选择 the right geospatial stack, 规划 multi-phase GIS programs |
| 🔧 [Solution Engineer](gis/gis-solution-engineer.md) | Esri + FOSS4G prototype 构建, PoC delivery, technical feasibility | Building working demos, 验证 technical approaches, pre-sales support |
| 🖥️ [GIS Analyst](gis/gis-analyst.md) | Map production, data QC, symbology, layouts, spatial queries | Day-to-day GIS operations, 创建 publication-ready maps, 维护 data integrity |
| 📦 [Spatial Data Engineer](gis/gis-spatial-data-engineer.md) | Geospatial ETL, format conversion, CRS reprojection, automated pipelines | Ingesting messy data from any source, 构建 repeatable data transformation pipelines |
| ⚙️ [Geoprocessing Specialist](gis/gis-geoprocessing-specialist.md) | ArcPy, Python Toolbox (.pyt), Model Builder, batch automation | Automating repetitive GIS 工作流程, 构建 custom geoprocessing tools |
| ✅ [GIS QA Engineer](gis/gis-qa-engineer.md) | Topology validation, metadata audit, CRS consistency, accuracy assessment | Quality gates before data publication, compliance verification, data integrity audits |
| 🤖 [Geo人工智能/ML Engineer](gis/gis-geoai-ml-engineer.md) | Feature extraction, object detection, semantic segmentation, land cover classification | Extracting 构建s/roads/vehicles from imagery, change detection, environmental 监控 |
| 🏗️ [BIM/GIS Specialist](gis/gis-bim-specialist.md) | Revit/IFC to GIS, indoor mapping, digital twin architecture, facility management | Smart campus, airport digital twins, indoor navigation, 构建 operations |
| 🏔️ [3D & Scene Developer](gis/gis-3d-scene-developer.md) | Cesium, ArcGIS Scene Viewer, 3D Tiles, point clouds, terrain visualization | 3D city scenes, terrain flyovers, point cloud web viewers, OAuth-gated scene sharing |
| 📊 [Spatial Data Scientist](gis/gis-spatial-data-scientist.md) | Spatial statistics, clustering, r出口ion, interpolation, point pattern analysis | Hotspot detection, spatial modeling, predictive analytics, research-grade analysis |
| 🛸 [Drone/Reality Mapping](gis/gis-drone-reality-mapping.md) | Photogrammetry, orthomosaic, DTM/DSM, point cloud classification, 3D mesh | Drone survey processing, reality capture, construction 监控, environmental mapping |
| 🌐 [Web GIS Developer](gis/gis-web-gis-developer.md) | MapLibre GL JS, ArcGIS JS API, Leaflet, real-time dashboards, REST APIs | Building interactive web maps, operational dashboards, real-time data visualization |
| 🎨 [Cartography Designer](gis/gis-cartography-designer.md) | Color theory, typography, basemap design, visual hierarchy, print and web aesthetics | Making maps beautiful and readable, colorblind-safe palettes, professional map layouts |

---

### 🏥 Healthcare Division

Building 人工智能 agents for regulated clinical and sovereign health contexts.

| Agent | Specialty | 使用场景 |
|-------|-----------|-------------|
| 🩺 [Clinical Evidence Agent](healthcare/healthcare-clinical-evidence-agent.md) | Evidence standards, validated vs unvalidated claims, diagnostic authority boundaries | Making clinical claims credibly without overstepping into diagnostic authority |
| 🌍 [Sovereign Health Systems Agent](healthcare/healthcare-sovereign-health-systems-agent.md) | Government health mandates, UHC policy, emerging market 部署 | Health tech teams operating at the intersection of national health infrastructure and sovereign health policy |
| 🧭 [Healthcare Innovation Strategist](healthcare/healthcare-innovation-strategist.md) | Narrative architecture for healthcare founders across investor, regulatory, sovereign, and clinical audiences | Healthcare founders who need to translate clinical and financial complexity into language that moves capital and builds trust |

---

## 🎯 实际用例

### Scenario 1: Building a Startup MVP

**Your Team**:
1. 🎨 **Frontend Developer** - Build the React app
2. 🏗️ **Backend Architect** - Design the API and database
3. 🚀 **增长 Hacker** - Plan user acquisition
4. ⚡ **Rapid Prototyper** - Fast iteration cycles
5. 🔍 **Reality Checker** - Ensure quality before launch

**Result**: Ship faster with specialized expertise at every stage.

---

### Scenario 2: Marketing Campaign Launch

**Your Team**:
1. 📝 **Content Creator** - Develop campaign content
2. 🐦 **Twitter Engager** - Twitter strategy and execution
3. 📸 **Instagram Curator** - Visual content and stories
4. 🤝 **Reddit Community Builder** - Authentic community engagement
5. 📊 **Analytics Reporter** - Track and optimize performance

**Result**: Multi-channel coordinated campaign with platform-specific expertise.

---

### Scenario 3: Enterprise Feature Development

**Your Team**:
1. 👔 **Senior Project Manager** - Scope and task 规划
2. 💎 **Senior Developer** - Complex implementation
3. 🎨 **界面设计er** - Design system and components
4. 🧪 **Experiment Tracker** - A/B test 规划
5. 📸 **Evidence Collector** - Quality verification
6. 🔍 **Reality Checker** - Production readiness

**Result**: Enterprise-grade delivery with quality gates and 文档.

---

### Scenario 4: Paid Media Account Takeover

**Your Team**:

1. 📋 **Paid Media Auditor** - Comprehensive account assessment
2. 📡 **Tracking & Measurement Specialist** - Verify conversion 追踪 accuracy
3. 💰 **PPC Campaign Strategist** - Redesign account architecture
4. 🔍 **Search Query Analyst** - Clean up wasted spend from search terms
5. ✍️ **Ad Creative Strategist** - Refresh all ad copy and extensions
6. 📊 **Analytics Reporter** (Support Division) - Build 报告 dashboards

**Result**: Systematic account takeover with 追踪 verified, waste eliminated, structure optimized, and creative refreshed — all within the first 30 days.

---

### Scenario 5: Full Agency Product Discovery

**Your Team**: All 8 divisions working in parallel on a single mission.

参见 the **[Nexus Spatial Discovery Exercise](examples/nexus-spatial-discovery.md)** -- a complete example where 8 agents (Product Trend Researcher, Backend Architect, Brand Guardian, 增长 Hacker, Support Responder, 用户体验研究er, Project Shepherd, and XR Interface Architect) were deployed simultaneously 来评估软件机会 and produce a unified product plan covering market validation, technical architecture, brand strategy, go-to-market, support systems, UX research, project execution, and spatial UI design.

**Result**: Comprehensive, 跨职能 product blueprint produced in a single session. [More examples](examples/).

---

### Scenario 6: Smart Campus Digital Twin

**Your Team**:

1. 🧠 **Technical Consultant** - Define the digital twin strategy: BIM for 构建s, GIS for campus, IoT for real-time
2. 🏗️ **BIM/GIS Specialist** - Convert Revit 构建 models to GIS scene layers, design indoor floor plans
3. 🛸 **Drone/Reality Mapping** - Fly the campus, generate orthomosaic and 3D mesh for context
4. 🌐 **Web GIS Developer** - Build the campus dashboard with MapLibre, 构建 layer, and room finder
5. 🏔️ **3D & Scene Developer** - Create immersive 3D scene with terrain, 构建s, and flyover tour
6. 🤖 **Geo人工智能/ML Engineer** - Extract 构建 footprints and tree canopy from drone imagery
7. ✅ **GIS QA Engineer** - Validate data accuracy, check topology, verify CRS consistency

**Result**: A campus digital twin that combines BIM detail, drone reality capture, 3D visualization, and web accessibility — delivered by coordinated specialists in a single pipeline.

---

## 🤝 贡献指南

We welcome contributions! Here's how you can help:

### Add a New Agent

1. Fork the repository
2. Create a new agent 文件在 the appropriate category
3. Follow the agent template structure:
   - Frontmatter with name, description, color
   - Identity & Memory section
   - Core Mission
   - 必须遵守的关键规则 (domain-specific)
   - 技术交付物 with examples
   - 工作流程
   - 成功指标
4. Submit a PR with your agent

### Improve Existing Agents

- Add real-world examples
- Enhance code samples
- Update success metrics
- Improve 工作流程

### Share Your Success Stories

Have you used these agents successfully? Share your story in the [Discussions](https://github.com/msitarzewski/agency-agents/discussions)!

---

## 📖 代理设计理念

每个代理都是 designed with:

1. **🎭 Strong 性格**: Not generic templates - real character and voice
2. **📋 Clear 交付物**: Concrete outputs, not vague guidance
3. **✅ 成功指标**: Measurable outcomes and quality standards
4. **🔄 Proven Workflows**: Step-by-step processes that work
5. **💡 Learning Memory**: Pattern recognition and continuous improvement

---

## 🎁 与众不同之处?

### Unlike Generic 人工智能 Prompts:
- ❌ Generic "Act as a developer" prompts
- ✅ Deep specialization with personality and process

### Unlike Prompt Libraries:
- ❌ One-off prompt collections
- ✅ Comprehensive agent systems with 工作流程 and deliverables

### Unlike 人工智能 Tools:
- ❌ Black box tools you can't customize
- ✅ Transparent, forkable, adaptable 代理人格集合

---

## 🎨 Agent 性格 Highlights

> "I don't just test your code - I default to 查找 3-5 issues and require visual proof for everything."
>
> -- **Evidence Collector** (测试 Division)

> "You're not marketing on Reddit - you're becoming a valued community member who happens to represent a brand."
>
> -- **Reddit Community Builder** (Marketing Division)

> "Every playful element must serve a functional or emotional purpose. Design delight that enhances rather than distracts."
>
> -- **Whimsy Injector** (Design Division)

> "Let me add a celebration animation that reduces task completion anxiety by 40%"
>
> -- **Whimsy Injector** (during a UX review)

---

## 📊 统计数据

- 🎭 **230+ Specialized Agents** across every division
- 📝 **10,000+ lines** of personality, process, and code examples
- ⏱️ **Months of iteration** from real-world usage
- 🌟 **Battle-tested** 在生产环境中 environments
- 💬 **50+ requests** in first 12 hours on Reddit

---

## 🔌 Multi-Tool Integrations

The Agency works natively with Claude Code, and ships conversion + install scripts so you can use the same agents across every major agentic coding tool.

### 支持的工具

- **[Claude Code](https://claude.ai/code)** — native `.md` agents, no conversion needed → `~/.claude/agents/`
- **[GitHub Copilot](https://github.com/copilot)** — native `.md` agents, no conversion needed → `~/.github/agents/` + `~/.copilot/agents/`
- **[Antigravity](https://github.com/google-gemini/antigravity)** — `SKILL.md` per agent → `~/.gemini/config/skills/`
- **[Gemini CLI](https://github.com/google-gemini/gemini-cli)** -- `.md` agent files -> `~/.gemini/agents/`
- **[OpenCode](https://opencode.ai)** — `.md` agent files → `.opencode/agents/`
- **[Cursor](https://cursor.sh)** — `.mdc` rule files → `.cursor/rules/`
- **[Aider](https://aider.chat)** — single `CONVENTIONS.md` → `./CONVENTIONS.md`
- **[Windsurf](https://codeium.com/windsurf)** — single `.windsurfrules` → `./.windsurfrules`
- **[OpenClaw](https://github.com/openclaw/openclaw)** — `SOUL.md` + `AGENTS.md` + `IDENTITY.md` per agent
- **[Qwen Code](https://github.com/QwenLM/qwen-code)** — `.md` SubAgent files → `~/.qwen/agents/`
- **[Kimi Code](https://github.com/Moonshot人工智能/kimi-cli)** — YAML agent specs → `~/.config/kimi/agents/`
- **[Codex](https://developers.openai.com/codex/overview)** — TOML custom agents → `~/.codex/agents/`
- **Osaurus** -- `SKILL.md` skills -> `~/.osaurus/skills/`
- **[Hermes](integrations/hermes/README.md)** -- lazy-router plugin -> `~/.hermes/plugins/`

---

### ⚡ 快速安装

**Step 1 -- Generate integration files:**
```bash
./scripts/convert.sh
# Faster (parallel, output order may vary): ./scripts/convert.sh --parallel
```

**Step 2 -- Install (interactive, auto-detects your tools):**
```bash
./scripts/install.sh
# Faster (parallel, output order may vary): ./scripts/install.sh --no-interactive --parallel
```

The installer scans your system for 安装到ols, shows a checkbox UI, and lets you pick exactly what to install:

```
  +------------------------------------------------+
  |   The Agency -- Tool Installer                 |
  +------------------------------------------------+

  System scan: [*] = detected on this machine

  [x]  1)  [*]  Claude Code     (claude.ai/code)
  [x]  2)  [*]  Copilot         (~/.github + ~/.copilot)
  [x]  3)  [*]  Antigravity     (~/.gemini/antigravity)
  [ ]  4)  [ ]  Gemini CLI      (~/.gemini/agents)
  [ ]  5)  [ ]  OpenCode        (opencode.ai)
  [ ]  6)  [ ]  OpenClaw        (~/.openclaw/agency-agents)
  [x]  7)  [*]  Cursor          (.cursor/rules)
  [ ]  8)  [ ]  Aider           (CONVENTIONS.md)
  [ ]  9)  [ ]  Windsurf        (.windsurfrules)
  [ ] 10)  [ ]  Qwen Code       (~/.qwen/agents)
  [ ] 11)  [ ]  Kimi Code       (~/.config/kimi/agents)
  [ ] 12)  [ ]  Codex           (~/.codex/agents)
  [ ] 13)  [ ]  Osaurus         (~/.osaurus/skills)
  [ ] 14)  [ ]  Hermes          (~/.hermes/plugins)

  [1-14] toggle   [a] all   [n] none   [d] detected
  [Enter] install   [q] quit
```

**Or install a specific tool directly:**
```bash
./scripts/install.sh --tool cursor
./scripts/install.sh --tool opencode
./scripts/install.sh --tool openclaw
./scripts/install.sh --tool antigravity
./scripts/install.sh --tool codex
./scripts/install.sh --tool osaurus
./scripts/install.sh --tool hermes
```

**Non-interactive (CI/scripts):**
```bash
./scripts/install.sh --no-interactive --tool all
```

**Faster 运行s (parallel)** — On multi-core machines, use `--parallel` so each tool is processed in parallel. Output order across tools is non-deterministic. Works with both interactive and non-interactive install: e.g. `./scripts/install.sh --interactive --parallel` (pick tools, then install in parallel) or `./scripts/install.sh --no-interactive --parallel`. Job count defaults to `nproc` (Linux), `sysctl -n hw.ncpu` (macOS), or 4; override with `--作业s N`.

```bash
./scripts/convert.sh --parallel                    # convert all tools in parallel
./scripts/convert.sh --parallel --作业s 8           # cap parallel 作业s
./scripts/install.sh --no-interactive --parallel   # install all detected tools in parallel
./scripts/install.sh --interactive --parallel      # pick tools, then install in parallel
./scripts/install.sh --no-interactive --parallel --作业s 4
```

---

### 工具特定说明

<details>
<summary><strong>Claude Code</strong></summary>

Agents are copied directly from the repo into `~/.claude/agents/` -- no conversion needed.

```bash
./scripts/install.sh --tool claude-code
```

然后在 Claude Code 中激活：
```
使用 Frontend Developer 代理来 审查这个组件.
```

参见 [integrations/claude-code/README.md](integrations/claude-code/README.md) 了解更多详情.
</details>

<details>
<summary><strong>GitHub Copilot</strong></summary>

Agents are copied directly from the repo into `~/.github/agents/` and `~/.copilot/agents/` -- no conversion needed.

```bash
./scripts/install.sh --tool copilot
```

然后在 GitHub Copilot 中激活：
```
使用 Frontend Developer 代理来 审查这个组件.
```

参见 [integrations/github-copilot/README.md](integrations/github-copilot/README.md) 了解更多详情.
</details>

<details>
<summary><strong>Antigravity (Gemini)</strong></summary>

Each agent becomes a skill in `~/.gemini/config/skills/agency-<slug>/`.

```bash
./scripts/install.sh --tool antigravity
```

Activate in Gemini with Antigravity:
```
@agency-frontend-developer review this React component
```

参见 [integrations/antigravity/README.md](integrations/antigravity/README.md) 了解更多详情.
</details>

<details>
<summary><strong>Gemini CLI</strong></summary>

Installs as Gemini CLI subagents.
On a fresh clone, generate the Gemini agent files before 运行ning the installer.

```bash
./scripts/convert.sh --tool gemini-cli
./scripts/install.sh --tool gemini-cli
```

参见 [integrations/gemini-cli/README.md](integrations/gemini-cli/README.md) 了解更多详情.
</details>

<details>
<summary><strong>OpenCode</strong></summary>

Agents are placed in `.opencode/agents/` in your project root (project-scoped).

```bash
cd /your/project
/path/to/agency-agents/scripts/install.sh --tool opencode
```

Or install globally:
```bash
mkdir -p ~/.config/opencode/agents
cp integrations/opencode/agents/*.md ~/.config/opencode/agents/
```

Activate in OpenCode:
```
@backend-architect design this API.
```

参见 [integrations/opencode/README.md](integrations/opencode/README.md) 了解更多详情.
</details>

<details>
<summary><strong>Cursor</strong></summary>

Each agent becomes a `.mdc` rule 文件在 `.cursor/rules/` of your project.

```bash
cd /your/project
/path/to/agency-agents/scripts/install.sh --tool cursor
```

Rules are auto-applied when Cursor detects them in the project. Reference them explicitly:
```
使用 @security-engineer rules to review this code.
```

参见 [integrations/cursor/README.md](integrations/cursor/README.md) 了解更多详情.
</details>

<details>
<summary><strong>Aider</strong></summary>

All agents are compiled into a single `CONVENTIONS.md` Aider 自动读取的文件.

```bash
cd /your/project
/path/to/agency-agents/scripts/install.sh --tool aider
```

Then reference agents in your Aider session:
```
使用 Frontend Developer 代理来 refactor this component.
```

参见 [integrations/aider/README.md](integrations/aider/README.md) 了解更多详情.
</details>

<details>
<summary><strong>Windsurf</strong></summary>

All agents are compiled into `.windsurfrules` in your project root.

```bash
cd /your/project
/path/to/agency-agents/scripts/install.sh --tool windsurf
```

Reference agents in Windsurf's Cascade:
```
使用 Reality Checker 代理来 verify this is production ready.
```

参见 [integrations/windsurf/README.md](integrations/windsurf/README.md) 了解更多详情.
</details>

<details>
<summary><strong>OpenClaw</strong></summary>

Each agent becomes a workspace with `SOUL.md`, `AGENTS.md`, and `IDENTITY.md` in `~/.openclaw/agency-agents/`.

```bash
./scripts/convert.sh --tool openclaw
./scripts/install.sh --tool openclaw
```

If the `openclaw` CLI is available, the installer registers each workspace automatically.
Run `openclaw gateway restart` after installation so the new agents are activated.

参见 [integrations/openclaw/README.md](integrations/openclaw/README.md) 了解更多详情.

</details>

<details>
<summary><strong>Qwen Code</strong></summary>

Sub代理安装到 `.qwen/agents/` in your project root (project-scoped).

```bash
# Convert and install (运行 from your project root)
cd /your/project
./scripts/convert.sh --tool qwen
./scripts/install.sh --tool qwen
```

**Usage in Qwen Code:**
- Reference by name: `使用 frontend-developer 代理来 审查这个组件`
- Or let Qwen auto-delegate based on task context
- Manage via `/agents` command in interactive mode

> 📚 [Qwen SubAgents Docs](https://qwenlm.github.io/qwen-code-docs/en/users/features/sub-agents/)

</details>

<details>
<summary><strong>Kimi Code</strong></summary>

Agents are converted to Kimi Code CLI format (YAML + system prompt) and 安装到 `~/.config/kimi/agents/`.

```bash
# Convert and install
./scripts/convert.sh --tool kimi
./scripts/install.sh --tool kimi
```

**Usage with Kimi Code:**
```bash
# Use an agent
kimi --agent-file ~/.config/kimi/agents/frontend-developer/agent.yaml

# In a project
kimi --agent-file ~/.config/kimi/agents/frontend-developer/agent.yaml \
     --work-dir /your/project \
     "审查 this React component"
```

参见 [integrations/kimi/README.md](integrations/kimi/README.md) 了解更多详情.

</details>

<details>
<summary><strong>Codex</strong></summary>

每个代理都是 converted into a Codex custom agent TOML 文件 and 安装到 `~/.codex/agents/`.

```bash
./scripts/convert.sh --tool codex
./scripts/install.sh --tool codex
```

Then reference the custom agent by name in Codex:
```
使用 Frontend Developer 代理来 审查这个组件.
```

参见 [integrations/codex/README.md](integrations/codex/README.md) 了解更多详情.
</details>

---

### Re生成 After Changes

When you add new agents or edit existing ones, 重新生成所有 integration files:

```bash
./scripts/convert.sh                    # 重新生成所有 (serial)
./scripts/convert.sh --parallel         # 重新生成所有 in parallel (faster)
./scripts/convert.sh --tool codex       # 只重新生成一个工具
./scripts/convert.sh --tool cursor      # 只重新生成一个工具
```

---

## 🗺️ 路线图

- [ ] 交互式代理选择器 Web 工具
- [x] Multi-agent 工作流程 examples -- 参见 [examples/](examples/)
- [x] 多工具集成脚本 (Claude Code, GitHub Copilot, Antigravity, Gemini CLI, OpenCode, OpenClaw, Cursor, Aider, Windsurf, Qwen Code, Kimi Code, Codex, Osaurus, Hermes)
- [ ] 代理设计视频教程
- [ ] 社区代理市场
- [ ] Agent "personality quiz" for project matching
- [ ] "Agent of the Week" showcase series

---

## 🌐 社区翻译 & 本地化s

社区维护的翻译和区域适配. 这些是独立维护的 -- 查看每个仓库的覆盖范围和版本兼容性.

| Language | Maintainer | Link | Notes |
|----------|-----------|------|-------|
| 🇨🇳 简体中文 (zh-CN) | [@jnMetaCode](https://github.com/jnMetaCode) | [agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | 141 translated agents + 46 China-market originals |
| 🇨🇳 简体中文 (zh-CN) | [@dsclca12](https://github.com/dsclca12) | [agent-teams](https://github.com/dsclca12/agent-teams) | Independent translation with Bilibili, WeChat, Xiaohongshu localization |
| 🇧🇷 Português brasileiro (pt-BR) | [@jnMetaCode](https://github.com/jnMetaCode) | [agency-agents-pt-BR](https://github.com/jnMetaCode/agency-agents-pt-BR) | 184 upstream agents translated; Brazil-market PRs welcome |
| 🇷🇺 Русский (ru) | [@jnMetaCode](https://github.com/jnMetaCode) | [agency-agents-ru](https://github.com/jnMetaCode/agency-agents-ru) | 184 upstream agents translated; Russia-market PRs welcome |
| 🇮🇩 Bahasa Indonesia (id) | [@jnMetaCode](https://github.com/jnMetaCode) | [agency-agents-id](https://github.com/jnMetaCode/agency-agents-id) | 184 upstream agents translated; Indonesia-market PRs welcome |
| 🇸🇦 العربية (ar) | [@jnMetaCode](https://github.com/jnMetaCode) | [agency-agents-ar](https://github.com/jnMetaCode/agency-agents-ar) | 184 upstream agents translated; Arabic-market PRs welcome |
| 🇰🇷 한국어 (ko) | [@jnMetaCode](https://github.com/jnMetaCode) | [agency-agents-ko](https://github.com/jnMetaCode/agency-agents-ko) | 184 upstream agents fully translated; Korea-specific PRs welcome |
| 🇯🇵 日本語 (ja-JP) | [@sscodeai](https://github.com/sscodeai) | [agency-agents-ja](https://github.com/sscodeai/agency-agents-ja) | 281 Japan-localized agents + 97 Japan-market originals + 27 工作流程 |
| 🇻🇳 Tiếng Việt (vi-VN) | [@rodonguyen](https://github.com/rodonguyen) | [agency-agents](https://github.com/rodonguyen/agency-agents) | Starter Vietnamese localization focused on README, quick start, and high-use docs |

想添加翻译？ Open an issue and we'll link it here.

---

## 🔗 Related 资源

- [awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) — Community-maintained OpenClaw agent collection (derived from this repo)

---

## 📜 许可证

MIT 许可证 - 自由使用，商业或个人. 署名感谢但不要求.

---

## 🙏 致谢

What started as a Reddit thread about 人工智能 agent specialization 已经成长为一些非凡的东西 — **230+ agents across every division**, 由来自世界各地的贡献者社区支持. 这个仓库中的每个代理之所以存在，是因为有人足够关心 来编写它、测试它并分享它.

向每一个打开 PR 的人, 提交 issue, 开始讨论, 或只是尝试了一个代理并告诉我们什么有效 — 谢谢你. You're the reason The Agency keeps getting better.

---

## 💬 社区

- **GitHub 讨论**: [分享你的成功故事](https://github.com/msitarzewski/agency-agents/discussions)
- **问题**: [报告 bug 或请求功能](https://github.com/msitarzewski/agency-agents/issues)
- **Reddit**: Join the conversation on r/Claude人工智能
- **Twitter/X**: 使用 #TheAgency 分享

---

## 🚀 开始使用

1. **Browse** the agents above and find specialists for your needs
2. **Copy** the agents to `~/.claude/agents/` 用于 Claude Code 集成
3. **Activate** agents by referencing them in your Claude conversations
4. **Customize** 代理人格集合 and 工作流程 适合你的特定需求
5. **Share** your results and contribute back to the community

---

<div align="center">

**🎭 The Agency: Your 人工智能 Dream Team Awaits 🎭**

[⭐ Star this repo](https://github.com/msitarzewski/agency-agents) • [🍴 Fork it](https://github.com/msitarzewski/agency-agents/fork) • [🐛 Report an issue](https://github.com/msitarzewski/agency-agents/issues) • [❤️ Sponsor](https://github.com/sponsors/msitarzewski)

Made with ❤️ by the community, for the community

</div>
