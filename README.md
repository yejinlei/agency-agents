# 🎭 The Agency：随时待命的 AI 专家团队

> **触手可及的完整 AI 团队** — 从前端魔法师到 Reddit 社区忍者，从趣味注入师到现实检查员。每个代理都是一个拥有独特性格、完善流程和可验证交付物的专业专家。

[![GitHub stars](https://img.shields.io/github/stars/msitarzewski/agency-agents?style=social)](https://github.com/msitarzewski/agency-agents)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://makeapullrequest.com)
[![Sponsor](https://img.shields.io/badge/Sponsor-%E2%9D%A4-pink?logo=github)](https://github.com/sponsors/msitarzewski)
[![Download the app](https://img.shields.io/github/v/release/msitarzewski/agency-agents-app?label=Download%20app&color=2563eb)](https://github.com/msitarzewski/agency-agents-app/releases/latest)

> ### 🆕 现在有了专用应用
>
> **[Agency Agents](https://agencyagents.app)** 是一款跨平台的原生桌面应用（macOS · Linux · Windows），只需一键即可浏览整个代理名录并将其安装到 Claude Code、Cursor、Codex、Gemini、Osaurus 等多个工具中。无需克隆仓库，无需编写脚本，并自动保持更新。
>
> **→ [下载最新版本](https://github.com/msitarzewski/agency-agents-app/releases/latest) · [agencyagents.app](https://agencyagents.app)**

---

## 🚀 这是什么？

诞生自一个 Reddit 帖子和数月的迭代, **The Agency** 是一个不断增长的精心打造的 人工智能 代理人格集合. 每个代理都是:

- **🎯 专业化**：在其领域拥有深厚专业知识（不是通用的提示模板）
- **🧠 性格驱动**：独特的声音、沟通方式和方法
- **📋 交付导向**：真实的代码、流程、可衡量的结果
- **✅ 生产就绪**：经过实战验证的工作流程和成功指标

**可以这样理解**：组建你的梦想团队，只不过成员是永不睡觉、永不抱怨、始终交付的 AI 专家。

---

## ⚡ 快速开始

### 方案一：安装应用（推荐）

最快的方式 — 无需克隆，无需终端. [**Agency Agents**](https://agencyagents.app) 是一个原生桌面应用 (macOS · Linux · Windows) 来浏览整个名录并将代理安装到 Claude Code、Cursor、Codex、Gemini CLI、OpenCode、Qwen 和 Osaurus 等工具中，并始终保持最新。

**[⬇ 下载最新版本](https://github.com/msitarzewski/agency-agents-app/releases/latest)** — 或在 Mac 上：

```bash
brew install --cask msitarzewski/agency-agents/agency-agents
```

偏好命令行？ 下方的脚本选项安装相同的代理.

### 方案二：配合 Claude Code 使用

```bash
# 将所有代理安装到你的 Claude Code 目录
./scripts/install.sh --tool claude-code

# 或者手动复制一个分类 如果你只想要一个部门
cp engineering/*.md ~/.claude/agents/

# 然后在你的 Claude Code 会话中激活任何代理：
# "嘿 Claude，激活 Frontend Developer 模式并帮我构建一个 React 组件"
```

### 方案三：作为参考资料

每个代理文件包含：
- 身份与性格特征
- 核心使命 & 工作流程
- 带有代码示例的技术交付物
- 成功指标与沟通风格

浏览下方的代理并复制/适配你需要的！

### 方案四：配合其他工具使用（GitHub Copilot、Antigravity、Gemini CLI、OpenCode、OpenClaw、Cursor、Aider、Windsurf、Kimi Code、Codex、Osaurus、Hermes、Mistral Vibe）

```bash
# 步骤一 —— 为所有支持的工具生成集成文件
./scripts/convert.sh

# 步骤二 —— 交互式安装（自动检测已安装的工具）
./scripts/install.sh

# 或者直接指定某个工具安装
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

> **OpenCode 注意：** OpenCode 的运行时目前只能注册约 119 个代理，超出部分会被静默丢弃（[上游 bug](https://github.com/anomalyco/opencode/issues/27988)）。使用 `--division` 安装子集可以避免超过该限制。安装器会在选择超出限制时发出警告。

参见下方的[多工具集成](#-multi-tool-integrations)部分了解更多详情。

---

## 🎨 代理名录

### 💻 工程团队

用一次一次提交，构建未来。

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 🎨 [前端开发者](engineering/engineering-frontend-developer.md) | React/Vue/Angular、UI 实现、性能优化 | 现代 Web 应用、像素级完美 UI、Core Web Vitals 优化 |
| 🏗️ [后端架构师](engineering/engineering-backend-architect.md) | API 设计、数据库架构、可扩展性 | 服务器端系统、微服务、云基础设施 |
| 📱 [移动应用构建师](engineering/engineering-mobile-app-builder.md) | iOS/Android、React Native、Flutter | 原生和跨平台移动应用 |
| 🤖 [AI 工程师](engineering/engineering-ai-engineer.md) | ML 模型、部署、AI 集成 | 机器学习功能、数据管道、AI 驱动的应用 |
| 🚀 [DevOps 自动化师](engineering/engineering-devops-automator.md) | 持续集成/持续部署、基础设施自动化、云运维 | 流水线开发、部署自动化、监控 |
| 🌐 [网络工程师](engineering/engineering-network-engineer.md) | Cisco IOS/IOS-XE、Juniper Junos、Palo Alto PAN-OS | 路由器/交换机/防火墙配置、BGP/OSPF、ACLs、show-output 排障 |
| ⚡ [快速原型师](engineering/engineering-rapid-prototyper.md) | 快速 POC 开发、MVP | 快速概念验证、黑客马拉松项目、快速迭代 |
| 💎 [高级开发者](engineering/engineering-senior-developer.md) | Laravel/Livewire、高级模式 | 复杂实现、架构决策 |
| 🔧 [Filament 优化专家](engineering/engineering-filament-optimization-specialist.md) | Filament PHP 管理后台 UX、结构表单重设计、资源优化 | 重构 Filament 资源/表单/表格，打造更快速、更整洁的管理后台工作流程 |
| ⚡ [自主优化架构师](engineering/engineering-autonomous-optimization-architect.md) | LLM 路由、成本优化、影子测试 | 为自主系统提供智能 API 选择和成本护栏 |
| 🔩 [嵌入式固件工程师](engineering/engineering-embedded-firmware-engineer.md) | 裸机开发、RTOS、ESP32/STM32/Nordic 固件 | 生产级嵌入式系统和物联网设备 |
| 🚨 [事件响应指挥官](engineering/engineering-incident-response-commander.md) | 事件管理、事后复盘、值班响应 | 管理生产事件并构建事件响应能力 |
| ⛓️ [Solidity 智能合约工程师](engineering/engineering-solidity-smart-contract-engineer.md) | EVM 合约、Gas 优化、DeFi | 安全、Gas 优化的智能合约和 DeFi 协议 |
| 🧭 [代码库入职引导工程师](engineering/engineering-代码库-onboarding-engineer.md) | 快速开发者入职、只读代码库探索、事实性解释 | 帮助新开发者快速理解陌生仓库，通过阅读代码、追踪代码路径和阐述结构与行为事实 |
| 📚 [技术文档作者](engineering/engineering-technical-writer.md) | 开发者文档、API 参考、教程 | 清晰准确的技术文档 |
| 💬 [微信小程序开发者](engineering/engineering-wechat-mini-program-developer.md) | 微信生态、小程序、支付集成 | 构建微信生态高性能应用 |
| 👁️ [代码审查员](engineering/engineering-code-reviewer.md) | 建设性代码审查、安全、可维护性 | PR 评审、代码质量门禁、通过审查进行指导 |
| 🗄️ [数据库优化师](engineering/engineering-database-optimizer.md) | 架构设计、查询优化、索引策略 | PostgreSQL/MySQL 调优、慢查询调试、迁移规划 |
| 🌿 [Git 工作流程大师](engineering/engineering-git-工作流程-master.md) | 分支策略、约定式提交、高级 Git | Git 工作流程设计、历史清理、CI 友好的分支管理 |
| 🏛️ [软件架构师](engineering/engineering-software-architect.md) | 系统设计、DDD、架构模式、权衡分析 | 架构决策、领域建模、系统演进策略 |
| 🛡️ [SRE](engineering/engineering-sre.md) | SLO、错误预算、可观测性、混沌工程 | 生产可靠性、减少运维负担、容量规划 |
| 🧬 [AI 数据修复工程师](engineering/engineering-ai-data-remediation-engineer.md) | 自愈管道、气隙 SLM、语义聚类 | 零数据丢失地修复大规模损坏数据 |
| 🔧 [数据工程师](engineering/engineering-data-engineer.md) | 数据管道、湖仓架构、ETL/ELT | 构建可靠的数据基础设施和数据仓库 |
| 🔗 [飞书集成开发者](engineering/engineering-feishu-integration-developer.md) | 飞书/Lark 开放平台、机器人、工作流 | 构建飞书生态集成 |
| 🧱 [CMS 开发者](engineering/engineering-cms-developer.md) | WordPress & Drupal 主题、插件/模块、内容架构 | 代码优先的 CMS 实现和定制 |
| 📧 [邮件智能工程师](engineering/engineering-email-intelligence-engineer.md) | 邮件解析、MIME 提取、结构化数据供 AI 代理使用 | 将原始邮件线程转换为推理就绪的上下文 |
| 🎙️ [语音 AI 集成工程师](engineering/engineering-voice-ai-integration-engineer.md) | 语音转文本管道、Whisper、ASR、说话人分离 | 端到端转录管道、音频预处理、结构化转录交付 |
| 🖧 [IT 服务经理](engineering/engineering-it-服务-manager.md) | ITIL 4 服务管理 | 事件/问题/变更管理、SLA、CMDB |
| 🪡 [最小变更工程师](engineering/engineering-minimal-change-engineer.md) | 最小可行差异 | 只修复所要求的内容，不扩大范围 |
| 📜 [OrgScript 工程师](engineering/engineering-orgscript-engineer.md) | OrgScript 语法和 AST 验证 | 设计和解析 OrgScript 业务逻辑定义 |
| 🧬 [提示词工程师](engineering/engineering-prompt-engineer.md) | LLM 提示词设计与优化 | 将模糊指令转化为可靠的 AI 行为 |
| 🕸️ [多代理系统架构师](engineering/engineering-multi-agent-systems-architect.md) | 多代理管道设计与治理 | 代理系统的拓扑、上下文、信任、故障恢复 |
| 🛒 [Drupal 购物车工程师](engineering/engineering-drupal-shopping-cart.md) | Drupal Commerce 前台 | Drupal 10/11 上的商品目录、支付、结账和订单 |
| 🛍️ [WordPress 购物车工程师](engineering/engineering-wordpress-shopping-cart.md) | WooCommerce 前台 | WordPress 上的商品目录、支付、结账和转化 |
| 💳 [支付与账单工程师](engineering/engineering-payments-billing-engineer.md) | PSP 集成、幂等支付流程、订阅计费 | Stripe/Adyen/Braintree 集成、Webhook 处理、催缴、对账 |
| 🌍 [国际化工程师](engineering/engineering-i18n-engineer.md) | ICU MessageFormat、RTL/双向布局、CLDR 格式化、伪本地化 | 让应用支持翻译、本地化感知格式化、RTL 支持、i18n 审计 |
| ⚡ [Drupal 性能工程师](engineering/engineering-drupal-performance.md) | Drupal 性能与 Core Web Vitals | 缓存、数据库/查询调优、渲染管道、高流量 Drupal 性能分析 |
| ⚡ [WordPress 性能工程师](engineering/engineering-wordpress-performance.md) | WordPress 性能与 Core Web Vitals | 缓存、查询/资源优化、插件调优、高流量 WP 性能分析 |
| ♿ [Section 508 无障碍专家](engineering/engineering-section-508-specialist.md) | 美国联邦 508 / WCAG 无障碍标准 | ARIA、屏幕阅读器测试、VPAT/ACR 编写、修复 |
| 🏛️ [USWDS 开发者](engineering/engineering-uswds-developer.md) | 美国联邦网页设计系统 (USWDS) | 无障碍政府 UI 组件与设计系统模式 |
| 🔎 [搜索相关性工程师](engineering/engineering-search-relevance-engineer.md) | 搜索排名与相关性 | 查询理解、嵌入、排名/评估、相关性调优 |
| 🔐 [身份与访问工程师](engineering/engineering-identity-access-engineer.md) | 身份认证/授权 & IAM | OAuth/OIDC/SAML、SSO、RBAC/ABAC、令牌与会话安全 |
| 🤝 [实时协作工程师](engineering/engineering-realtime-collaboration-engineer.md) | 实时同步与在线状态 | CRDT/OT、冲突解决、实时光标、离线同步 |
| 💻 [桌面应用工程师](engineering/engineering-desktop-app-engineer.md) | 跨平台桌面应用 | Electron/Tauri、原生集成、打包、自动更新 |
| 🚀 [移动发布工程师](engineering/engineering-mobile-release-engineer.md) | 移动发布与 CI/CD | App Store/Play 上架、签名、分阶段发布、崩溃分类 |
| 🎬 [视频流媒体工程师](engineering/engineering-video-streaming-engineer.md) | 视频流媒体与转码 | HLS/DASH、ABR、编解码器、CDN 交付、低延迟流媒体 |
| 💰 [FinOps 工程师](engineering/engineering-finops-engineer.md) | 云成本工程 | 成本分配、资源调整、单位经济、预算与异常控制 |
| 🧩 [WebAssembly 工程师](engineering/engineering-webassembly-engineer.md) | WebAssembly 与 WASI | Rust/C++→WASM、沙箱、主机绑定、性能 |
| 🔌 [API 平台工程师](engineering/engineering-api-platform-engineer.md) | API 网关与平台 | 网关设计、版本控制、速率限制、开发者门户 |
| 🛟 [数据库可靠性工程师](engineering/engineering-database-reliability-engineer.md) | 数据库可靠性 (DBRE) | 高可用/复制、自动故障转移、PITR 备份、零停机运维 |
| 🛠️ [开发者工具工程师](engineering/engineering-developer-tooling-engineer.md) | CLI 与开发者工具 | 命令行工具、内部 DX、构建/开发工作流程 |
| 📡 [IoT 集群工程师](engineering/engineering-iot-fleet-engineer.md) | IoT 与边缘集群 | 设备预配置/身份、MQTT 遥测、OTA 更新 |
| 🔍 [检索增强生成管道工程师](engineering/engineering-rag-pipeline-engineer.md) | 生产级检索增强生成管道 | 分块、检索质量、混合搜索、重排序、评估驱动迭代 |
| 🗄️ [GaussDB 专家工程师](engineering/engineering-gaussdb-expert.md) | 华为 GaussDB OLTP | 企业级 OLTP 性能、高可用和迁移 |

### 🎨 设计团队

让它更美观、更易用、更令人愉悦。

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 🎯 [UI 设计师](design/design-ui-designer.md) | 视觉设计、组件库、设计系统 | 界面创建、品牌一致性、组件设计 |
| 🔍 [用户体验研究er](design/design-ux-researcher.md) | User 测试, behavior analysis, research | Understanding users, 可用性测试, design insights |
| 🏛️ [UX 架构师](design/design-ux-architect.md) | 信息架构、CSS 系统、实现 | 开发者友好的基础、实现指导 |
| 🎭 [品牌守护者](design/design-brand-guardian.md) | 品牌识别、一致性、定位 | 品牌战略、识别开发、品牌指南 |
| 📖 [视觉叙事者](design/design-visual-storyteller.md) | 视觉叙事、多媒体内容 | 引人入胜的视觉故事、品牌故事讲述 |
| ✨ [趣味注入师](design/design-whimsy-injector.md) | 愉悦感、个性、 playful 互动 | 添加乐趣、微交互、彩蛋、品牌个性 |
| 📷 [Image Prompt Engineer](design/design-image-prompt-engineer.md) | 人工智能 图像生成 prompts, photography | Photography prompts for Midjourney, DALL-E, Stable Diffusion |
| 🌈 [包容性视觉专家](design/design-inclusive-visuals-specialist.md) | 代表性、偏见缓解、真实影像 | 生成文化上准确的 人工智能 images and video |
| 🎭 [人设走查专家](design/design-persona-walkthrough.md) | 基于人设的认知走查 | 模拟用户在每个滚动位置的反应和摩擦点 |

### 💰 付费媒体团队

将广告投放转化为可衡量的商业成果。

| 代理 | 专长 | 使用场景 |
| --- | --- | --- |
| 💰 [PPC 广告战略师](paid-media/paid-media-ppc-strategist.md) | Google/Microsoft/Amazon 广告、账户架构、竞价策略 | 账户搭建、预算分配、扩量、绩效诊断 |
| 🔍 [搜索查询分析师](paid-media/paid-media-search-query-analyst.md) | 搜索词分析、否定关键词、意图映射 | 查询审计、消除浪费支出、关键词发现 |
| 📋 [付费媒体审计员](paid-media/paid-media-auditor.md) | 200+ 项账户审计、竞争分析 | 账户接管、季度审查、竞争提案 |
| 📡 [Tracking & Measurement Specialist](paid-media/paid-media-追踪-specialist.md) | GTM, GA4, conversion 追踪, CAPI | New implementations, 追踪 audits, platform migrations |
| ✍️ [广告创意战略师](paid-media/paid-media-creative-strategist.md) | RSA 文案、Meta 创意、Performance Max 素材 | 创意上线、测试计划、广告疲劳刷新 |
| 📺 [程序化与展示广告买家](paid-media/paid-media-programmatic-buyer.md) | GDN、DSP、合作伙伴媒体、ABM 展示 | 展示规划、合作伙伴拓展、ABM 计划 |
| 📱 [付费社交战略师](paid-media/paid-media-paid-social-strategist.md) | Meta、LinkedIn、TikTok、跨平台社交 | 社交广告计划、平台选择、受众策略 |

### 💼 销售团队

靠精湛手艺而非 CRM 琐事，将销售管道转化为收入。

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 🎯 [外联战略师](sales/sales-outbound-strategist.md) | 信号驱动的潜在客户开发、多渠道序列、ICP 定位 | 通过研究驱动的外联构建销售管道，而非堆量 |
| 🔍 [发现教练](sales/sales-discovery-coach.md) | SPIN、Gap Selling、Sandler —— 问题设计与通话结构 | 准备发现通话、机会资格评估、教练指导销售代表 |
| ♟️ [交易战略师](sales/sales-deal-strategist.md) | MEDDPICC 资格评估、竞争定位、赢单规划 | 交易评分、暴露管道风险、构建赢单策略 |
| 🛠️ [销售工程师](sales/sales-engineer.md) | 技术演示、POC 范围控制、竞争对战卡 | 售前技术制胜、演示准备、竞争定位 |
| 🏹 [提案战略师](sales/sales-proposal-strategist.md) | RFP 响应、赢单主题、叙事结构 | 撰写有说服力的提案，而不仅仅是合规 |
| 📊 [管道分析师](sales/sales-pipeline-analyst.md) | 预测、管道健康度、交易速度、收入运营 | 管道审查、预测准确性、收入运营 |
| 🗺️ [客户战略师](sales/sales-account-strategist.md) | 渗透扩展、QBR、利益相关者映射 | 售后扩展、客户规划、净收入留存增长 |
| 🏋️ [销售教练](sales/sales-coach.md) | 销售代表发展、通话指导、管道审查促进 | 通过结构化指导让每个销售代表和每笔交易都更好 |
| 🎯 [销售外联](specialized/sales-outreach.md) | 冷拓潜在客户、多触点节奏、异议处理、提案 | 漏斗顶端 B2B 外联——从冷邮件到预约发现通话 |
| 🧲 [优惠与潜客生成战略师](sales/sales-offer-lead-gen-strategist.md) | 优惠与潜客磁铁 | 漏斗顶端优惠构建和潜客生成 |

### 📢 营销团队

通过每一次真诚的互动，稳步增长你的受众。

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 🚀 [增长黑客](marketing/marketing-growth-hacker.md) | 快速用户获取、病毒循环、实验 | 爆炸式增长、用户获取、转化优化 |
| 📝 [内容创作者](marketing/marketing-content-creator.md) | 多平台内容、编辑日历 | 内容战略、文案撰写、品牌故事讲述 |
| 🐦 [Twitter 互动师](marketing/marketing-twitter-engager.md) | 实时互动、思想领导力 | Twitter 战略、LinkedIn 活动、专业社交 |
| 🛰️ [X/Twitter Intelligence Analyst](marketing/marketing-x-twitter-intelligence-analyst.md) | 社交倾听、趋势检测、账户监控 | X/Twitter 上的品牌风险、竞争对手和受众情报 |
| 📱 [TikTok 战略师](marketing/marketing-tiktok-strategist.md) | 病毒内容、算法优化 | TikTok 增长、病毒内容、Z 世代/千禧世代受众 |
| 📸 [Instagram 策展人](marketing/marketing-instagram-curator.md) | 视觉叙事、社群建设 | Instagram 战略、美学开发、视觉内容 |
| 🤝 [Reddit 社群建设师](marketing/marketing-reddit-community-builder.md) | 真实互动、价值驱动内容 | Reddit 战略、社群信任、真实营销 |
| 📱 [应用商店优化师](marketing/marketing-app-store-optimizer.md) | ASO、转化优化、可发现性 | 应用营销、商店优化、应用增长 |
| 🌐 [社交媒体战略师](marketing/marketing-social-media-strategist.md) | 跨平台战略、活动 | 整体社交战略、多平台活动 |
| 📕 [小红书专家](marketing/marketing-xiaohongshu-specialist.md) | 生活方式内容、趋势驱动战略 | 小红书增长、美学故事讲述、Z 世代受众 |
| 💬 [WeChat Official Account Manager](marketing/marketing-wechat-official-account.md) | Subscriber engagement, 内容营销 | WeChat OA strategy, community 构建, conversion optimization |
| 🧠 [知乎战略师](marketing/marketing-zhihu-strategist.md) | 思想领导力、知识驱动互动 | 知乎权威建设、问答策略、潜客生成 |
| 🇨🇳 [百度 SEO 专家](marketing/marketing-baidu-seo-specialist.md) | 百度优化、中国 SEO、ICP 合规 | 在百度排名并触达中国搜索市场 |
| 🎬 [B站内容战略师](marketing/marketing-bilibili-content-strategist.md) | B站算法、弹幕文化、UP主增长 | 用社群优先的内容在 B站 建立受众 |
| 🎠 [轮播增长引擎](marketing/marketing-carousel-growth-engine.md) | TikTok/Instagram 轮播、自主发布 | 生成和发布病毒式轮播内容 |
| 💼 [LinkedIn 内容创作者](marketing/marketing-linkedin-content-creator.md) | 个人品牌、思想领导力、专业内容 | LinkedIn 增长、专业受众建设、B2B 内容 |
| 🛒 [中国电商运营师](marketing/marketing-china-ecommerce-operator.md) | 淘宝、天猫、拼多多、直播电商 | 运营中国多平台电商 |
| 🎥 [快手战略师](marketing/marketing-kuaishou-strategist.md) | 快手、老铁社群、草根增长 | 在下沉市场建立真实受众 |
| 🔍 [SEO 专家](marketing/marketing-seo-specialist.md) | 技术 SEO、内容战略、外链建设 | 推动可持续的自然搜索增长 |
| 📘 [书籍合著者](marketing/marketing-book-co-author.md) | 思想领导力书籍、代笔、出版 | 为创始人和专家提供战略性书籍合作 |
| 🌏 [跨境电商专家](marketing/marketing-cross-border-ecommerce.md) | Amazon、Shopee、Lazada、跨境履约 | 全漏斗跨境电商战略 |
| 🎵 [抖音战略师](marketing/marketing-douyin-strategist.md) | 抖音平台、短视频营销、算法 | 在中国领先的短视频平台上增长受众 |
| 🎙️ [直播电商教练](marketing/marketing-livestream-commerce-coach.md) | 主播培训、直播间优化、转化 | 构建高性能直播电商运营 |
| 🎧 [播客战略师](marketing/marketing-Podcast-strategist.md) | 播客内容战略、平台优化 | 中文播客市场战略和运营 |
| 🔒 [私域运营师](marketing/marketing-private-domain-operator.md) | 企业微信、私域流量、社群运营 | 构建企业微信私域生态 |
| 🎬 [短视频剪辑教练](marketing/marketing-short-video-editing-coach.md) | 后期制作、剪辑工作流程、平台规格 | 实操短视频剪辑培训和优化 |
| 🔥 [微博战略师](marketing/marketing-weibo-strategist.md) | 新浪微博、热门话题、粉丝互动 | 全谱微博运营和增长 |
| 🎙️ [全球播客战略师](marketing/marketing-global-Podcast-strategist.md) | 节目定位、受众增长、变现 | 播客上线、平台 algorithms, sponsorship, community 构建 |
| 🔮 [AI 引用战略师](marketing/marketing-ai-citation-strategist.md) | AEO/GEO、AI 推荐可见性、引用审计 | 提升品牌在 ChatGPT、Claude、Gemini、Perplexity 上的可见性 |
| 🇨🇳 [中国市场本地化战略师](marketing/marketing-china-market-localization-strategist.md) | 全栈中国市场本地化、抖音/小红书/微信上市策略 | 将趋势信号转化为可执行的中国上市策略 |
| 🎬 [视频优化专家](marketing/marketing-video-optimization-specialist.md) | YouTube 算法战略、章节划分、缩略图概念 | YouTube 频道增长、视频 SEO、受众留存优化 |
| 🏗️ [AEO 基础架构师](marketing/marketing-aeo-foundations.md) | AI 引擎优化基础设施 | llms.txt、AI 感知的 robots.txt、代理发现文件 |
| 🤖 [智能搜索优化师](marketing/marketing-agentic-search-optimizer.md) | WebMCP 与智能任务完成 | 让网站被 AI 浏览代理可用 |
| 📧 [邮件营销战略师](marketing/marketing-email-strategist.md) | 生命周期邮件与送达率 | CRM 活动、自动化、细分 |
| 📡 [多平台发布师](marketing/marketing-multi-platform-publisher.md) | 一键中国多平台发布 | 将一篇文章分发到知乎/小红书/CSDN/B站/公众号/掘金 |
| 📣 [公关与沟通经理](marketing/marketing-pr-communications-manager.md) | 公关、媒体关系与危机沟通 | 新闻稿、思想领导力、声誉管理 |

### 📊 产品团队

在正确的时间构建正确的事情。

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 🎯 [Sprint Prioritizer](product/product-sprint-优先级排序r.md) | 敏捷 规划, feature 优先级排序 | Sprint 规划, resource allocation, backlog management |
| 🔍 [趋势研究员](product/product-trend-researcher.md) | 市场情报、竞争分析 | 市场调研、机会评估、趋势识别 |
| 💬 [反馈综合师](product/product-feedback-synthesizer.md) | 用户反馈分析、洞察提取 | 反馈分析、用户洞察、产品优先级 |
| 🧠 [行为助推引擎](product/product-behavioral-nudge-engine.md) | 行为心理学、助推设计、参与度 | 通过行为科学最大化用户动力 |
| 🧭 [产品经理](product/product-manager.md) | 全生命周期产品所有权 | 发现、PRD 撰写、路线图规划、上市策略、成果衡量 |

### 🎬 项目管理团队

让项目准时交付（且预算可控）。

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 🎬 [制片制作人](project-management/project-management-studio-producer.md) | 高层统筹、组合管理 | 多项目管理、战略对齐、资源分配 |
| 🐑 [项目牧人](project-management/project-management-project-shepherd.md) | 跨职能协调、时间线管理 | 端到端项目协调、利益相关者管理 |
| ⚙️ [制片运营](project-management/project-management-studio-operations.md) | 日常效率、流程优化 | 运营卓越、团队支持、生产力 |
| 🧪 [Experiment Tracker](project-management/project-management-experiment-tracker.md) | A/B tests, hypothesis validation | Experiment management, 数据驱动的 decisions, 测试 |
| 👔 [高级项目经理](project-management/project-manager-senior.md) | 现实范围控制、任务转换 | 将规格说明书转为任务、范围管理 |
| 📋 [Jira Workflow Steward](project-management/project-management-jira-工作流程-steward.md) | Git 工作流程, branch strategy, traceability | Enforcing Jira-linked Git discipline and delivery |
| 📋 [会议纪要专家](project-management/project-management-meeting-notes-specialist.md) | 结构化会议摘要 | 提取决策、行动项、待解决问题 |

### 🧪 测试团队

破坏一切，让用户无需操心。

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 📸 [Evidence Collector](测试/测试-evidence-collector.md) | Screenshot-based QA, visual proof | UI 测试, visual verification, bug 文档 |
| 🔍 [现实检查员](测试/测试-reality-checker.md) | 基于证据的认证、质量门禁 | 生产就绪性、质量审批、发布认证 |
| 📊 [Test 结果分析器](测试/测试-test-results-analyzer.md) | Test evaluation, metrics analysis | Test output analysis, quality insights, coverage 报告 |
| ⚡ [Performance Benchmarker](测试/测试-performance-benchmarker.md) | Performance 测试, optimization | Speed 测试, 负载测试, performance tuning |
| 🔌 [API Tester](测试/测试-api-tester.md) | API validation, 集成测试 | API 测试, endpoint verification, integration QA |
| 🛠️ [工具评估师](测试/测试-tool-evaluator.md) | 技术评估、工具选型 | 评估工具、软件推荐、技术决策 |
| 🔄 [Workflow Optimizer](测试/测试-工作流程-optimizer.md) | Process analysis, 工作流程 improvement | Process optimization, efficiency gains, automation opportunities |
| ♿ [无障碍 Auditor](测试/测试-accessibility-auditor.md) | WCAG 审计, assistive technology 测试 | 无障碍 compliance, 屏幕阅读器 测试, inclusive design verification |
| 🎭 [Test Automation Engineer](测试/测试-test-automation-engineer.md) | Playwright/Cypress E2E, flake elimination, CI parallelization | Browser test suites, deterministic pipelines, trace-driven failure 调试 |

### 🔒 安全团队

守护整个技术栈——从安全设计到入侵响应。

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 🛡️ [安全架构师](security/security-architect.md) | 威胁建模、安全设计、信任边界 | 系统安全模型、架构审查、纵深防御 |
| 🔐 [Application 安全 Engineer](security/security-appsec-engineer.md) | SDLC security, SAST/DAST, secure 代码审查 | Securing the dev lifecycle, code-level vulnerabilities |
| 🗡️ [渗透测试员](security/security-penetration-tester.md) | 授权渗透测试、红队作战、漏洞利用 | 在攻击者之前发现可利用的弱点 |
| ☁️ [Cloud 安全 Architect](security/security-cloud-security-architect.md) | Zero trust, 云原生 defense-in-depth | Securing cloud infrastructure and architectures |
| 🚨 [事件响应员](security/security-incident-responder.md) | DFIR、入侵调查、威胁遏制 | 活跃入侵、取证、危机响应 |
| 🔍 [威胁情报分析师](security/security-threat-intelligence-analyst.md) | 对手追踪、活动映射、ATT&CK | 了解谁在攻击以及攻击方式 |
| 🎯 [威胁检测工程师](security/security-threat-detection-engineer.md) | SIEM 规则、威胁狩猎、ATT&CK 映射 | 构建检测层和威胁狩猎 |
| 🛡️ [高级安全运维工程师](security/security-senior-secops.md) | 密钥扫描、默认安全提交 | 每次变更的防御性代码级安全 |
| 📋 [合规审计员](security/security-compliance-auditor.md) | SOC 2、ISO 27001、HIPAA、PCI-DSS | 指导组织通过合规认证 |
| 🛡️ [区块链安全审计员](security/security-blockchain-security-auditor.md) | 智能合约审计、漏洞分析 | 在合约部署前发现漏洞 部署 |
| 🔎 [人工智能-Generated Code 安全 Auditor](security/security-ai-generated-code-auditor.md) | 安全 review of 人工智能/vibe-coded apps | Hardcoded 密钥s, broken RLS, prompt-injection sinks |
| 🔑 [密钥与凭证卫生工程师](security/security-密钥s-credential-engineer.md) | 密钥与凭证生命周期 | 检测、保管库、轮换、泄露响应 |

### 🛟 支持团队

运营的中坚力量。

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 💬 [Support Responder](support/support-support-responder.md) | Customer 服务, issue resolution | Customer support, 用户体验, support operations |
| 📊 [数据分析报告师](support/support-analytics-reporter.md) | 数据分析、仪表盘、洞察 | 商业智能、KPI 追踪、数据可视化 |
| 💰 [Finance Tracker](support/support-finance-tracker.md) | Financial 规划, budget management | Financial analysis, 现金流, business performance |
| 🏗️ [基础设施维护员](support/support-infrastructure-maintainer.md) | 系统可靠性、性能优化 | 基础设施管理、系统运维、监控m operations, 监控 |
| ⚖️ [法律合规检查员](support/support-legal-compliance-checker.md) | 合规、法规、法律审查 | 法律合规、监管要求、风险管理 |
| 📑 [执行摘要 Generator](support/support-executive-summary-generator.md) | C-suite communication, strategic summaries | Executive 报告, strategic communication, decision support |

### 🥽 空间计算团队

构建沉浸式未来。

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 🏗️ [XR 界面架构师](spatial-computing/xr-interface-architect.md) | 空间交互设计、沉浸式体验 | AR/VR/XR 界面设计、空间计算 UX |
| 💻 [macOS 空间/Metal 工程师](spatial-computing/macos-spatial-metal-engineer.md) | Swift、Metal、高性能 3D | macOS 空间计算、Vision Pro 原生应用 |
| 🌐 [XR 沉浸式开发者](spatial-computing/xr-immersive-developer.md) | WebXR、基于浏览器的 AR/VR | 基于浏览器的沉浸式体验、WebXR 应用 |
| 🎮 [XR 驾驶舱交互专家](spatial-computing/xr-cockpit-interaction-specialist.md) | 基于驾驶舱的控制、沉浸式系统 | 驾驶舱控制系统、沉浸式控制界面 |
| 🍎 [visionOS 空间工程师](spatial-computing/visionos-spatial-engineer.md) | Apple Vision Pro 开发 | Vision Pro 应用、空间计算体验 |
| 🔌 [终端集成专家](spatial-computing/terminal-integration-specialist.md) | 终端集成、命令行工具 | CLI 工具、终端工作流程、开发者工具 |

### 🎯 专业团队

无法归类在某个部门的独特专家。

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 🎭 [代理协调者](specialized/agents-orchestrator.md) | 多代理协调、工作流程管理 | 需要多个代理协调的复杂项目 |
| 🔍 [LSP/索引工程师](specialized/lsp-index-engineer.md) | 语言服务器协议、代码智能 | 代码智能系统、LSP 实现、语义索引 |
| 📥 [销售数据提取代理](specialized/sales-data-extraction-agent.md) | Excel 监控、销售指标提取 | 销售数据摄取、MTD/YTD/年度指标 |
| 📈 [数据整合代理](specialized/data-consolidation-agent.md) | 销售数据聚合、仪表盘报告 | 区域摘要、销售代表表现、管道快照 |
| 📬 [报告分发代理](specialized/report-distribution-agent.md) | 自动化报告交付 | 基于区域的报告分发、定时发送 |
| 🔐 [智能身份与信任架构师](specialized/agentic-identity-trust.md) | 代理身份、认证、信任验证 | 多代理身份系统、代理授权、审计追踪 |
| 🔗 [身份图操作员](specialized/identity-graph-operator.md) | 多代理系统共享身份解析 | 实体去重、合并提案、跨代理身份一致性 |
| 💸 [应付账款代理](specialized/accounts-payable-agent.md) | 支付处理、供应商管理、审计 | 跨加密、法币、稳定币的自主支付执行 |
| 🌍 [文化智能战略师](specialized/specialized-cultural-intelligence-strategist.md) | 全球 UX、代表性、文化排斥 | 确保软件在不同文化中共鸣 |
| 🗣️ [开发者布道师](specialized/specialized-developer-advocate.md) | 社群建设、开发者体验、开发者内容 | 连接产品和开发者社区 |
| 🔬 [模型质量保证专家](specialized/specialized-model-qa.md) | 机器学习审计、特征分析、可解释性 | 机器学习模型的端到端质量保证 |
| 🗃️ [知识库管理员](specialized/zk-steward.md) | 知识管理、Zettelkasten、笔记 | 构建互联、验证过的知识库 |
| 🔌 [MCP Builder](specialized/specialized-mcp-builder.md) | Model Context Protocol servers, 人工智能 代理来oling | Building MCP servers that extend 人工智能 agent capabilities |
| 📄 [文档生成器](specialized/specialized-document-generator.md) | 从代码生成 PDF、PPTX、DOCX、XLSX | 专业文档创建、报告、数据可视化 |
| ⚙️ [Automation 治理 Architect](specialized/automation-governance-architect.md) | Automation governance, n8n, 工作流程 审计 | Evaluating and governing business automations 大规模地 |
| 📚 [企业培训设计师](specialized/corporate-training-designer.md) | 企业培训、课程设计 | 设计培训系统和学习课程 |
| 🌱 [个人成长导师](specialized/personal-growth-mentor.md) | 目标清晰、习惯系统、问责、人生战略 | 跨领域个人发展，无励志废话 |
| 🏛️ [政府数字化售前顾问](specialized/government-digital-presales-consultant.md) | 中国 ToG 售前、数字化转型 | 政府数字化转型提案和投标 |
| ⚕️ [医疗健康营销合规](specialized/healthcare-marketing-compliance.md) | 中国医疗广告合规 | 医疗健康营销监管合规 |
| 🎯 [招聘专员](specialized/recruitment-specialist.md) | 人才招聘、招聘运营 | 招聘战略、寻源和招聘流程 |
| 🎓 [留学顾问](specialized/study-abroad-advisor.md) | 国际教育、申请规划 | 美国、英国、加拿大、澳大利亚的留学规划 |
| 🔗 [供应链战略师](specialized/supply-chain-strategist.md) | 供应链管理、采购战略 | 供应链优化和采购规划 |
| 🗺️ [工作流程架构师](specialized/specialized-工作流程-architect.md) | 工作流程发现、映射和规范 | 在编写代码之前映射系统中的每条路径 |
| ☁️ [Salesforce 架构师](specialized/specialized-salesforce-architect.md) | 多云 Salesforce 设计、治理限制、集成 | 企业 Salesforce 架构、组织战略、部署流水线ure, org strategy, 部署 pipelines |
| 🇫🇷 [法国咨询市场导航师](specialized/specialized-french-consulting-market.md) | ESN/SI 生态系统、薪酬代付、费率定位 | 法国 IT 市场的自由职业咨询 |
| 🇰🇷 [韩国商业导航师](specialized/specialized-korean-business-navigator.md) | 韩国商业文化、品议流程、关系运作 | Foreign professionals 导航 Korean business relationships |
| 🏗️ [Civil Engineer](specialized/specialized-civil-engineer.md) | Structural analysis, geotechnical design, global 构建 codes | Multi-standard structural engineering across Eurocode, ACI, 人工智能SC, and more |
| 🎧 [客户服务](specialized/customer-服务.md) | 全渠道支持、投诉处理、留存、升级 | 任何行业的客户支持——零售、SaaS、酒店、金融、物流, finance, logistics |
| 🏥 [Healthcare 客户服务](specialized/healthcare-customer-服务.md) | 符合 HIPAA 的患者支持、账单、保险、紧急路由 | 需要合规、富有同理心的患者支持的医疗机构要 compliant, empathetic patient support |
| 🏨 [酒店客人服务](specialized/hospitality-guest-服务s.md) | 预订、礼宾、投诉恢复、忠诚度、活动 | 酒店、度假村、餐厅和活动场所 |
| 🤝 [HR 入职引导](specialized/hr-onboarding.md) | Pre-boarding, compliance, benefits enrollment, 30-60-90 day plans | Any company onboarding new hires — from startups to enterprise |
| 🌐 [语言翻译](specialized/language-translator.md) | 西班牙语 ↔ 英语翻译、方言意识、文化语境 | 旅行、商业、医疗和法律翻译需求 |
| ⏱️ [法律计费与时间追踪](specialized/legal-billing-time-追踪.md) | 时间捕获、计费叙述、IOLTA 合规、催收 | 律师事务所最大化收入恢复和计费准确性 |
| 📋 [法律客户接待](specialized/legal-client-intake.md) | 潜在客户资格评估、利益冲突筛查、咨询预约 | 律师事务所将咨询转化为留存客户 |
| ⚖️ [法律文档审查](specialized/legal-document-review.md) | 合同审查、风险标记、版本对比、合规 | 任何业务领域的一审律师级审查 |
| 🏦 [贷款专员助理](specialized/loan-officer-assistant.md) | 借款人接待、TRID 合规、管道追踪、关联合规 | 抵押贷款和消费者贷款团队 |
| 🏠 [房地产买卖师](specialized/real-estate-buyer-seller.md) | 买方/卖方代理、报价、交易协调 | 住宅和投资房地产交易 |
| 🛒 [零售客户退货](specialized/retail-customer-returns.md) | 退货处理、欺诈预防、换货、供应商退货 | 实体店、电商和全渠道零售 |
| ♟️ [商业战略师](specialized/business-strategist.md) | 管理咨询战略 | 竞争分析、市场进入、增长规划 |
| 🔄 [变革管理顾问](specialized/change-management-consultant.md) | ADKAR/Kotter/Prosci 变革 | 指导组织完成转型与采用 |
| 🧭 [首席幕僚](specialized/specialized-chief-of-staff.md) | 高管协调 | 过滤噪音、拥有流程、路由决策 |
| 🌟 [客户成功经理](specialized/customer-success-manager.md) | 入职、健康与留存 | QBR、流失预防、续约与扩展 |
| 📝 [补助金撰写者](specialized/grant-writer.md) | 补助金提案与资金 | 非营利/研究的意向书、提案、预算 |
| 🏥 [医疗计费与编码专家](specialized/medical-billing-coding-specialist.md) | ICD-10/CPT/HCPCS 与收入循环 | 理赔、拒赔管理、RCM 优化 |
| 💰 [定价分析师](specialized/specialized-pricing-analyst.md) | 定价模型与利润优化 | 竞争对手/成本分析、基于价值的定价 |
| 💼 [首席财务官](specialized/chief-financial-officer.md) | 资本配置与财务战略 | 司库、FP&A、M&A 财务、投资者与董事会报告 |
| 🌱 [ESG 与可持续发展官](specialized/esg-sustainability-officer.md) | ESG 项目与披露 | 可持续战略、脱碳、报告 |
| 🔐 [数据隐私 Officer](specialized/data-privacy-officer.md) | GDPR/CCPA privacy compliance | Data mapping, DPIAs, consent, breach response |
| ⚙️ [运营经理](specialized/operations-manager.md) | 精益/六西格玛运营 | 流程映射、容量规划、KPI 治理 |
| 🤝 [M&A 整合经理](specialized/ma-integration-manager.md) | 并购后整合 | 第1天/100天计划、协同追踪、TSA 管理 |
| 🧠 [组织心理学家](specialized/organizational-psychologist.md) | 团队动态与文化健康 | 心理安全、倦怠风险、高绩效团队 |
| ⚔️ [战略对弈代理](specialized/specialized-strategy-duel-agent.md) | 博弈论与三十六计 | 回合制战略对决、对抗性场景模拟 |
| 🛡️ [FedRAMP 与 RMF 合规工程师](specialized/specialized-fedramp-rmf-compliance.md) | 联邦云授权 (ATO) | NIST 800-53、FedRAMP Rev5/20x、SSP/POA&M、ConMon、OSCAL |
| 🏺 [Codebase Archaeologist](specialized/specialized-代码库-archaeologist.md) | Multi-tool 代码库 drift audits | Detecting silent drift across Claude/Cursor/Copilot/Windsurf edits |
| 🧾 [简历优化师](specialized/resume-tailor.md) | 候选人侧简历优化 | JD 映射、ATS 关键词对齐、经验与要求匹配 |

### 💵 财务团队

会计、财务分析、税务策略和投资研究专家。

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 📒 [记账员与会计主管](finance/finance-bookkeeper-controller.md) | 月度结账、对账、GAAP 合规、内部控制 | 日常会计运营、审计准备、财务记录保存 |
| 📊 [Financial Analyst](finance/finance-financial-analyst.md) | Financial modeling, forecasting, scenario analysis, decision support | Three-statement models, variance analysis, 数据驱动的 business intelligence |
| 📈 [FP&A 分析师](finance/finance-fpa-analyst.md) | 预算编制、滚动预测、差异分析、业务回顾 | 年度运营计划、月度业务回顾、战略资源分配 |
| 🔍 [投资研究员](finance/finance-investment-researcher.md) | 尽职调查、投资组合分析、资产估值、股权研究 | 投资论点开发、风险评估、市场调研 |
| 🏛️ [税务战略师](finance/finance-tax-strategist.md) | 税务优化、多司法管辖区合规、转让定价 | 实体架构、ETR 分析、审计防御、战略税务规划TR analysis, audit defense, strategic tax 规划 |

### 🎮 游戏开发团队

跨所有主流引擎构建世界、系统和体验。

#### 跨引擎代理（引擎无关）

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 🎯 [游戏设计er](game-development/game-designer.md) | Systems design, GDD authorship, economy balancing, gameplay loops | Designing game mechanics, progression systems, 编写 design documents |
| 🗺️ [关卡设计er](game-development/level-designer.md) | Layout theory, pacing, encounter design, environmental storytelling | Building levels, 设计 encounter flow, spatial narrative |
| 🎨 [技术美术师](game-development/technical-artist.md) | 着色器、VFX、LOD 管道、美术到引擎优化 | 连接美术与工程、着色器编写、性能安全的资源管道 |
| 🔊 [游戏音频工程师](game-development/game-audio-engineer.md) | FMOD/Wwise、自适应音乐、空间音频、音频预算 | 交互式音频系统、动态音乐、音频性能 |
| 📖 [叙事设计er](game-development/narrative-designer.md) | Story systems, branching dialogue, lore architecture | Writing branching narratives, 实现 dialogue systems, world lore |

#### Unity

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 🏗️ [Unity Architect](game-development/unity/unity-architect.md) | ScriptableObjects, 数据驱动的 modularity, DOTS/ECS | Large-scale Unity projects, 数据驱动的 system design, ECS performance work |
| ✨ [Unity 着色器图形艺术家](game-development/unity/unity-shader-graph-artist.md) | Shader Graph、HLSL、URP/HDRP、渲染器特性 | 自定义 Unity 材质、VFX 着色器、后处理通道 |
| 🌐 [Unity 多人游戏工程师](game-development/unity/unity-multiplayer-engineer.md) | Netcode for GameObjects、Unity Relay/Lobby、服务器权威、预测 | 在线 Unity 游戏、客户端预测、Unity 游戏服务集成 |
| 🛠️ [Unity 编辑器工具开发者](game-development/unity/unity-editor-tool-developer.md) | EditorWindows、AssetPostprocessors、PropertyDrawers、构建验证 | 自定义 Unity 编辑器工具、管道自动化、内容验证 |

#### Unreal Engine

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| ⚙️ [Unreal 系统工程师](game-development/unreal-engine/unreal-systems-engineer.md) | C++/Blueprint 混合、GAS、Nanite 约束、内存管理 | 复杂 Unreal 游戏系统、游戏能力系统、引擎级 C++ |
| 🎨 [Unreal 技术美术师](game-development/unreal-engine/unreal-technical-artist.md) | 材质编辑器、Niagara、PCG、Substrate | Unreal 材质、Niagara VFX、程序化内容生成 |
| 🌐 [Unreal 多人游戏架构师](game-development/unreal-engine/unreal-multiplayer-architect.md) | Actor 复制、GameMode/GameState 层次、专用服务器 | Unreal 在线游戏、复制图、服务器权威 Unreal |
| 🗺️ [Unreal 世界构建师](game-development/unreal-engine/unreal-world-builder.md) | World Partition、Landscape、HLOD、LWC | 大型开放世界 Unreal 关卡、流式加载系统、地形雕刻reaming systems, terrain 大规模地 |

#### Godot

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 📜 [Godot 游戏脚本编写者](game-development/godot/godot-gameplay-scripter.md) | GDScript 2.0、信号、组合、静态输入 | Godot 游戏系统、场景组合、注重性能的 GDScript |
| 🌐 [Godot 多人游戏工程师](game-development/godot/godot-multiplayer-engineer.md) | MultiplayerAPI、ENet/WebRTC、RPC、权威模型 | 在线 Godot 游戏、场景复制、服务器权威 Godot |
| ✨ [Godot 着色器开发者](game-development/godot/godot-shader-developer.md) | Godot 着色语言、VisualShader、RenderingDevice | 自定义 Godot 材质、2D/3D 效果、后处理、计算着色器 |

#### Blender

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 🧩 [Blender 插件工程师](game-development/blender/blender-addon-engineer.md) | Blender Python (`bpy`), custom operators/panels, asset validators, exporters, pipeline automation | Building Blender add-ons, asset prep tools, export 工作流程, and DCC pipeline automation |

#### Roblox Studio

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| ⚙️ [Roblox 系统脚本编写者](game-development/roblox-studio/roblox-systems-scripter.md) | Luau、RemoteEvents/Functions、DataStore、服务器权威模块架构 | 构建安全的 Roblox 游戏系统、客户端-服务器通信、数据持久化 |
| 🎯 [Roblox 体验设计师](game-development/roblox-studio/roblox-experience-designer.md) | 参与度循环、变现、D1/D7 留存、入职流程 | 设计 Roblox 游戏循环、游戏通行证、每日奖励、玩家留存 |
| 👗 [Roblox 虚拟形象创建者](game-development/roblox-studio/roblox-avatar-creator.md) | UGC 管道、配件绑定、创作者市场提交 | Roblox UGC 物品、HumanoidDescription 定制、体验内虚拟形象商店 |

### 📚 学术团队

为世界观构建、叙事和故事设计提供学术严谨性。

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 🌍 [人类学家](academic/academic-anthropologist.md) | 文化系统、亲属关系、仪式、信仰体系 | 设计具有内在逻辑的文化连贯社会 |
| 🌐 [地理学家](academic/academic-geographer.md) | 自然/人文地理、气候、制图学 | 构建地理连贯的世界，具有真实的地形和聚落 |
| 📚 [历史学家](academic/academic-historian.md) | 历史分析、分期、物质文化 | 验证历史连贯性，用真实时期细节丰富设定 |
| 📜 [叙事学家](academic/academic-narratologist.md) | 叙事理论、故事结构、角色弧线 | 用成熟理论框架分析和改进故事结构 |
| 🧠 [心理学家](academic/academic-psychologist.md) | 性格理论、动机、认知模式 | 构建基于研究的心理可信角色 |
| 📊 [Statistician](academic/academic-statistician.md) | Statistical 推理 & experiment design | Hypothesis 测试, causal 推理, sampling, rigorous analysis |

---

### 🌍 GIS 团队

测绘地球、分析建成世界，并从地理空间数据中提取情报。

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 🧠 [技术咨询师](gis/gis-technical-consultant.md) | GIS 战略、差距分析、技术路线图、数字化转型 | 理解业务需求、选择合适的地理空间技术栈、规划多阶段 GIS 项目 |
| 🔧 [解决方案工程师](gis/gis-solution-engineer.md) | Esri + FOSS4G 原型构建、PoC 交付、技术可行性 | 构建可用的演示、验证技术方案、售前支持 |
| 🖥️ [GIS 分析师](gis/gis-analyst.md) | 地图制作、数据质量控制、符号化、布局、空间查询 | 日常 GIS 运营、制作可发布的地图、维护数据完整性 |
| 📦 [空间数据工程师](gis/gis-spatial-data-engineer.md) | 地理空间 ETL、格式转换、CRS 重投影、自动化管道 | 从任何来源摄取杂乱数据、构建可重复的数据转换管道essy data from any source, 构建 repeatable data transformation pipelines |
| ⚙️ [Geoprocessing Specialist](gis/gis-geoprocessing-specialist.md) | ArcPy, Python Toolbox (.pyt), Model Builder, batch automation | Automating repetitive GIS 工作流程, 构建 custom geoprocessing tools |
| ✅ [GIS 质量工程师](gis/gis-qa-engineer.md) | 拓扑验证、元数据审计、CRS 一致性、精度评估 | 数据发布前的质量门禁、合规性验证、数据完整性审计 |
| 🤖 [GeoAI/ML 工程师](gis/gis-geoai-ml-engineer.md) | 特征提取、目标检测、语义分割、土地覆盖分类 | 从影像中提取建筑物/道路/车辆、变化检测、环境监测 |
| 🏗️ [BIM/GIS 专家](gis/gis-bim-specialist.md) | Revit/IFC 转 GIS、室内制图、数字孪生架构、设施管理 | 智慧校园、机场数字孪生、室内导航、建筑运营 |
| 🏔️ [3D 与场景开发者](gis/gis-3d-scene-developer.md) | Cesium、ArcGIS Scene Viewer、3D Tiles、点云、地形可视化 | 3D 城市场景、地形飞越、点云 Web 查看器、OAuth 门禁场景共享 |
| 📊 [空间数据科学家](gis/gis-spatial-data-scientist.md) | 空间统计、聚类、回归、插值、点模式分析 | 热点检测、空间建模、预测分析、研究级分析 |
| 🛸 [无人机/实景测绘师](gis/gis-drone-reality-mapping.md) | 摄影测量、正射镶嵌、DTM/DSM、点云分类、3D 网格 | 无人机航测处理、实景捕捉、施工监控、环境制图 |
| 🌐 [Web GIS 开发者](gis/gis-web-gis-developer.md) | MapLibre GL JS、ArcGIS JS API、Leaflet、实时仪表盘、REST API | 构建交互式 Web 地图、运营仪表盘、实时数据可视化 |
| 🎨 [制图设计师](gis/gis-cartography-designer.md) | 色彩理论、排版、底图设计、视觉层次、印刷与 Web 美学 | 让地图美观易读、色盲安全配色方案、专业地图布局 |

---

### 🏥 医疗健康团队

为受监管的临床环境和主权健康场景构建 AI 代理。

| 代理 | 专长 | 使用场景 |
|-------|-----------|-------------|
| 🩺 [临床证据代理](healthcare/healthcare-clinical-evidence-agent.md) | 证据标准、已验证与未验证声明、诊断权限边界 | 在不越界进入诊断权限的前提下，可信地做出临床声明 |
| 🌍 [主权健康体系代理](healthcare/healthcare-sovereign-health-systems-agent.md) | 政府健康指令、全民健康覆盖政策、新兴市场部署 | 在国家健康基础设施与主权健康政策交叉点运作的健康科技团队 |
| 🧭 [医疗创新战略师](healthcare/healthcare-innovation-strategist.md) | 面向投资人、监管机构、主权机构和临床受众的医疗创业者叙事架构 | 需要将临床和财务复杂性转化为能推动资本和建立信任的语言的医疗创业者 |

---

## 🎯 实际用例

### 场景一：构建创业公司 MVP

**你的团队**：
1. 🎨 **前端开发者** —— 构建 React 应用
2. 🏗️ **后端架构师** —— 设计 API 和数据库
3. 🚀 **增长黑客** —— 规划用户获取
4. ⚡ **快速原型师** —— 快速迭代周期
5. 🔍 **现实检查师** —— 上线前确保质量

**成果**：每个阶段都有专业专家支持，交付更快。

---

### 场景二：营销活动上线

**你的团队**：
1. 📝 **内容创作者** —— 制作活动内容
2. 🐦 **Twitter 互动师** —— Twitter 策略与执行
3. 📸 **Instagram 策划师** —— 视觉内容和故事
4. 🤝 **Reddit 社群建设师** —— 真实的社群互动
5. 📊 **数据分析报告师** —— 追踪和优化绩效

**成果**：多平台协调的营销活动，每个平台都有专属专家。

---

### 场景三：企业级功能开发

**你的团队**：
1. 👔 **高级项目经理** —— 范围控制和任务规划
2. 💎 **高级开发者** —— 复杂实现
3. 🎨 **界面设计师** —— 设计系统和组件
4. 🧪 **实验追踪器** —— A/B 测试规划
5. 📸 **证据收集员** —— 质量验证
6. 🔍 **现实检查员** —— 生产就绪性

**成果**：企业级交付，包含质量门禁和文档。

---

### 场景四：付费媒体账户接管

**你的团队**：

1. 📋 **付费媒体审计员** —— 全面账户评估
2. 📡 **追踪与测量专家** —— 验证转化追踪准确性
3. 💰 **PPC 广告战略师** —— 重构账户架构
4. 🔍 **搜索查询分析师** —— 清除搜索词浪费支出
5. ✍️ **广告创意战略师** —— 刷新所有广告文案和扩展
6. 📊 **数据分析报告师**（支持团队）—— 构建报告仪表盘

**成果**：系统化的账户接管——追踪验证、消除浪费、优化结构、更新创意，全部在 30 天内完成。

---

### 场景五：全团队产品探索

**你的团队**：全部 8 个团队并行协作，共担一个使命。

参见 **[Nexus 空间探索练习](examples/nexus-spatial-discovery.md)**——一个完整的示例，8 个代理（产品趋势研究员、后端架构师、品牌守护者、增长黑客、客服响应员、用户体验研究员、项目牧人和 XR 界面架构师）同时部署，评估软件机会并产出一份统一的产品方案，涵盖市场验证、技术架构、品牌战略、上市策略、支持体系、UX 研究、项目执行和空间 UI 设计。

**成果**：一次会话中产出全面的跨职能产品蓝图。 [更多示例](examples/)

---

### 场景六：智慧校园数字孪生

**你的团队**：

1. 🧠 **技术咨询师** —— 定义数字孪生战略：BIM 用于建筑、GIS 用于校园、IoT 用于实时
2. 🏗️ **BIM/GIS 专家** —— 将 Revit 建筑模型转换为 GIS 场景图层，设计室内平面图
3. 🛸 **无人机/实景测绘师** —— 飞越校园，生成正射镶嵌和 3D 网格作为背景
4. 🌐 **Web GIS 开发者** —— 使用 MapLibre 构建校园仪表盘，包含建筑图层和房间查找器
5. 🏔️ **3D 与场景开发者** —— 创建包含地形、建筑和飞越导览的沉浸式 3D 场景
6. 🤖 **GeoAI/ML 工程师** —— 从无人机影像中提取建筑轮廓和树冠
7. ✅ **GIS 质量工程师** —— 验证数据准确性、检查拓扑、验证 CRS 一致性

**成果**：一个融合 BIM 细节、无人机实景捕捉、3D 可视化和 Web 访问能力的校园数字孪生，由协调一致的专家团队在单一管线中交付。

---

## 🤝 贡献指南

我们欢迎贡献！以下是你的参与方式：

### 添加新代理

1. 分叉本仓库
2. 在适当的分类下创建一个新代理文件
3. 遵循代理模板结构：
   - 包含名称、描述、颜色的 frontmatter
   - 身份与记忆章节
   - 核心使命
   - 必须遵守的关键规则（领域特定）
   - 技术交付物及示例
   - 工作流程
   - 成功指标
4. 提交包含你的代理的 PR

### 改进现有代理

- 添加真实世界示例
- 完善代码示例
- 更新成功指标
- 改进工作流程

### 分享你的成功故事

你成功使用过这些代理吗？在[讨论区](https://github.com/msitarzewski/agency-agents/discussions)分享你的故事吧！

---

## 📖 代理设计理念

每个代理都秉承以下设计理念：

1. **🎭 鲜明性格**：不是通用模板，而是真实的角色和声音
2. **📋 清晰交付物**：具体的产出，而非模糊的指导
3. **✅ 成功指标**：可衡量的成果和质量标准
4. **🔄 经过验证的工作流程**：行之有效的一步一步流程
5. **💡 学习记忆**：模式识别与持续改进

---

## 🎁 与众不同之处？

### 与普通 AI 提示词不同：
- ❌ 通用的"扮演开发者"提示词
- ✅ 深度专业化，具备性格和流程

### 与提示词库不同：
- ❌ 一次性提示词集合
- ✅ 完整的代理系统，包含工作流程和交付物

### 与 AI 工具不同：
- ❌ 无法定制的"黑盒"工具
- ✅ 透明、可分叉、可适配的代理人格集合

---

## 🎨 代理性格亮点

> "我不只是测试你的代码——我默认会找出 3-5 个问题，并要求对每件事提供视觉证明。"
>
> -- **证据收集员**（测试团队）

> "你不是在 Reddit 上做营销——你正在成为一个有价值、恰好代表某个品牌的社区成员。"
>
> -- **Reddit 社群建设师**（营销团队）

> "每一个趣味元素都必须服务于功能或情感目的。设计令人愉悦的体验，增强而非干扰。"
>
> -- **趣味注入师**（设计团队）

> "让我加一个庆祝动画，将任务完成焦虑降低 40%"
>
> -- **趣味注入师**（UX 评审期间）

---

## 📊 统计数据

- 🎭 **230+ 专业代理**，覆盖所有团队
- 📝 **10,000+ 行**性格设定、流程和代码示例
- ⏱️ **数月的迭代**，来自真实世界的使用经验
- 🌟 **经过实战检验**，在生产环境中验证
- 💬 Reddit 上**首 12 小时收到 50+ 请求**

---

## 🔌 多工具集成

The Agency 原生支持 Claude Code，并附带转换和安装脚本，让你可以在所有主流 AI 编码工具中使用相同的代理。

### 支持的工具

- **[Claude Code](https://claude.ai/code)** —— 原生 `.md` 代理，无需转换 → `~/.claude/agents/`
- **[GitHub Copilot](https://github.com/copilot)** —— 原生 `.md` 代理，无需转换 → `~/.github/agents/` + `~/.copilot/agents/`
- **[Antigravity](https://github.com/google-gemini/antigravity)** —— 每个代理一个 `SKILL.md` → `~/.gemini/config/skills/`
- **[Gemini CLI](https://github.com/google-gemini/gemini-cli)** —— `.md` 代理文件 → `~/.gemini/agents/`
- **[OpenCode](https://opencode.ai)** —— `.md` 代理文件 → `.opencode/agents/`
- **[Cursor](https://cursor.sh)** —— `.mdc` 规则文件 → `.cursor/rules/`
- **[Aider](https://aider.chat)** —— 单个 `CONVENTIONS.md` → `./CONVENTIONS.md`
- **[Windsurf](https://codeium.com/windsurf)** —— 单个 `.windsurfrules` → `./.windsurfrules`
- **[OpenClaw](https://github.com/openclaw/openclaw)** —— 每个代理包含 `SOUL.md` + `AGENTS.md` + `IDENTITY.md`
- **[Qwen Code](https://github.com/QwenLM/qwen-code)** —— `.md` 子代理文件 → `~/.qwen/agents/`
- **[Kimi Code](https://github.com/Moonshot人工智能/kimi-cli)** —— YAML 代理规范 → `~/.config/kimi/agents/`
- **[Codex](https://developers.openai.com/codex/overview)** —— TOML 自定义代理 → `~/.codex/agents/`
- **Osaurus** —— `SKILL.md` 技能 → `~/.osaurus/skills/`
- **[Hermes](integrations/hermes/README.md)** —— 懒路由插件 → `~/.hermes/plugins/`

---

### ⚡ 快速安装

**步骤一 —— 生成集成文件：**
```bash
./scripts/convert.sh
# 更快（并行，输出顺序可能不同）：./scripts/convert.sh --parallel
```

**步骤二 —— 安装（交互式，自动检测你的工具）：**
```bash
./scripts/install.sh
# 更快（并行，输出顺序可能不同）：./scripts/install.sh --no-interactive --parallel
```

安装器会扫描你的系统查找已安装的工具，显示复选框界面，让你精确选择要安装的内容：

```
  +------------------------------------------------+
  |   The Agency -- Tool Installer                 |
  +------------------------------------------------+

  系统扫描：[*] = 在此机器上检测到

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

  [1-14] 切换   [a] 全选   [n] 全不选   [d] 已检测
  [回车] 安装   [q] 退出
```

**或者直接安装特定工具：**
```bash
./scripts/install.sh --tool cursor
./scripts/install.sh --tool opencode
./scripts/install.sh --tool openclaw
./scripts/install.sh --tool antigravity
./scripts/install.sh --tool codex
./scripts/install.sh --tool osaurus
./scripts/install.sh --tool hermes
```

**非交互式（CI/脚本）：**
```bash
./scripts/install.sh --no-interactive --tool all
```

**更快的运行（并行）** —— 在多核机器上，使用 `--parallel` 让每个工具并行处理。不同工具之间的输出顺序是不确定的。同时适用于交互式和非交互式安装：例如 `./scripts/install.sh --interactive --parallel`（先选择工具，再并行安装）或 `./scripts/install.sh --no-interactive --parallel`。作业数默认为 `nproc`（Linux）、`sysctl -n hw.ncpu`（macOS）或 4；可通过 `--作业s N` 覆盖。

```bash
./scripts/convert.sh --parallel                    # 并行转换所有工具
./scripts/convert.sh --parallel --作业s 8           # 限制并行作业数
./scripts/install.sh --no-interactive --parallel   # 并行安装所有检测到的工具
./scripts/install.sh --interactive --parallel      # 选择工具后并行安装
./scripts/install.sh --no-interactive --parallel --作业s 4
```

---

### 工具特定说明

<details>
<summary><strong>Claude Code</strong></summary>

代理直接从仓库复制到 `~/.claude/agents/` —— 无需转换。

```bash
./scripts/install.sh --tool claude-code
```

然后在 Claude Code 中激活：
```
使用 Frontend Developer 代理来 审查这个组件.
```

参见 [integrations/claude-code/README.md](integrations/claude-code/README.md) 了解更多详情。
</details>

<details>
<summary><strong>GitHub Copilot</strong></summary>

代理直接从仓库复制到 `~/.github/agents/` 和 `~/.copilot/agents/` —— 无需转换。

```bash
./scripts/install.sh --tool copilot
```

然后在 GitHub Copilot 中激活：
```
使用 Frontend Developer 代理来 审查这个组件.
```

参见 [integrations/github-copilot/README.md](integrations/github-copilot/README.md) 了解更多详情。
</details>

<details>
<summary><strong>Antigravity (Gemini)</strong></summary>

每个代理会成为 `~/.gemini/config/skills/agency-<slug>/` 下的一个技能。

```bash
./scripts/install.sh --tool antigravity
```

在 Gemini 中通过 Antigravity 激活：
```
@agency-frontend-developer review this React component
```

参见 [integrations/antigravity/README.md](integrations/antigravity/README.md) 了解更多详情。
</details>

<details>
<summary><strong>Gemini CLI</strong></summary>

安装为 Gemini CLI 子代理。
在全新克隆后，运行安装器之前先生成 Gemini 代理文件。

```bash
./scripts/convert.sh --tool gemini-cli
./scripts/install.sh --tool gemini-cli
```

参见 [integrations/gemini-cli/README.md](integrations/gemini-cli/README.md) 了解更多详情。
</details>

<details>
<summary><strong>OpenCode</strong></summary>

代理放在项目根目录的 `.opencode/agents/` 中（项目级作用域）。

```bash
cd /your/project
/path/to/agency-agents/scripts/install.sh --tool opencode
```

或者全局安装：
```bash
mkdir -p ~/.config/opencode/agents
cp integrations/opencode/agents/*.md ~/.config/opencode/agents/
```

在 OpenCode 中激活：
```
@backend-architect design this API.
```

参见 [integrations/opencode/README.md](integrations/opencode/README.md) 了解更多详情。
</details>

<details>
<summary><strong>Cursor</strong></summary>

每个代理会成为项目 `.cursor/rules/` 下的一个 `.mdc` 规则文件。

```bash
cd /your/project
/path/to/agency-agents/scripts/install.sh --tool cursor
```

当 Cursor 在项目中发现这些规则时会自动应用。也可以显式引用：
```
使用 @security-engineer rules to review this code.
```

参见 [integrations/cursor/README.md](integrations/cursor/README.md) 了解更多详情。
</details>

<details>
<summary><strong>Aider</strong></summary>

所有代理被编译为一个 `CONVENTIONS.md` 文件，Aider 会自动读取。

```bash
cd /your/project
/path/to/agency-agents/scripts/install.sh --tool aider
```

然后在你的 Aider 会话中引用代理：
```
使用 Frontend Developer 代理来 refactor this component.
```

参见 [integrations/aider/README.md](integrations/aider/README.md) 了解更多详情。
</details>

<details>
<summary><strong>Windsurf</strong></summary>

所有代理被编译为项目根目录下的 `.windsurfrules`。

```bash
cd /your/project
/path/to/agency-agents/scripts/install.sh --tool windsurf
```

在 Windsurf 的 Cascade 中引用代理：
```
使用 现实检查员 代理来 verify this is production ready.
```

参见 [integrations/windsurf/README.md](integrations/windsurf/README.md) 了解更多详情。
</details>

<details>
<summary><strong>OpenClaw</strong></summary>

每个代理会成为 `~/.openclaw/agency-agents/` 下的一个工作区，包含 `SOUL.md`、`AGENTS.md` 和 `IDENTITY.md`。

```bash
./scripts/convert.sh --tool openclaw
./scripts/install.sh --tool openclaw
```

如果 `openclaw` CLI 可用，安装器会自动注册每个工作区。
安装后运行 `openclaw gateway restart`，使新代理生效。

参见 [integrations/openclaw/README.md](integrations/openclaw/README.md) 了解更多详情。

</details>

<details>
<summary><strong>Qwen Code</strong></summary>

子代理安装到项目根目录的 `.qwen/agents/` 中（项目级作用域）。

```bash
# 转换并安装（在项目根目录下运行）
cd /your/project
./scripts/convert.sh --tool qwen
./scripts/install.sh --tool qwen
```

**在 Qwen Code 中的使用方式：**
- 按名称引用：`使用 frontend-developer 代理来审查这个组件`
- 或者让 Qwen 根据任务上下文自动委派
- 在交互模式下通过 `/agents` 命令管理

> 📚 [Qwen SubAgents Docs](https://qwenlm.github.io/qwen-code-docs/en/users/features/sub-agents/)

</details>

<details>
<summary><strong>Kimi Code</strong></summary>

代理被转换为 Kimi Code CLI 格式（YAML + 系统提示），并安装到 `~/.config/kimi/agents/`。

```bash
# 转换并安装
./scripts/convert.sh --tool kimi
./scripts/install.sh --tool kimi
```

**配合 Kimi Code 使用：**
```bash
# 使用一个代理
kimi --agent-file ~/.config/kimi/agents/frontend-developer/agent.yaml

# 在项目中
kimi --agent-file ~/.config/kimi/agents/frontend-developer/agent.yaml \
     --work-dir /your/project \
     "审查 this React component"
```

参见 [integrations/kimi/README.md](integrations/kimi/README.md) 了解更多详情。

</details>

<details>
<summary><strong>Codex</strong></summary>

每个代理被转换为 Codex 自定义代理 TOML 文件，并安装到 `~/.codex/agents/`。

```bash
./scripts/convert.sh --tool codex
./scripts/install.sh --tool codex
```

然后在 Codex 中按名称引用自定义代理：
```
使用 Frontend Developer 代理来 审查这个组件.
```

参见 [integrations/codex/README.md](integrations/codex/README.md) 了解更多详情。
</details>

---

### 变更后的重新生成

当你添加新代理或编辑现有代理时，重新生成所有集成文件：

```bash
./scripts/convert.sh                    # 重新生成所有（串行）
./scripts/convert.sh --parallel         # 重新生成所有（并行，更快）
./scripts/convert.sh --tool codex       # 只重新生成一个工具
./scripts/convert.sh --tool cursor      # 只重新生成一个工具
```

---

## 🗺️ 路线图

- [ ] 交互式代理选择器 Web 工具
- [x] 多代理工作流程示例 —— 参见 [examples/](examples/)
- [x] 多工具集成脚本 (Claude Code, GitHub Copilot, Antigravity, Gemini CLI, OpenCode, OpenClaw, Cursor, Aider, Windsurf, Qwen Code, Kimi Code, Codex, Osaurus, Hermes)
- [ ] 代理设计视频教程
- [ ] 社区代理市场
- [ ] 项目匹配的代理"性格测试"
- [ ] "每周代理"展示系列

---

## 🌐 社区翻译 & 本地化

社区维护的翻译和区域适配. 这些是独立维护的 -- 查看每个仓库的覆盖范围和版本兼容性.

| Language | Maintainer | Link | Notes |
|----------|-----------|------|-------|
| 🇨🇳 简体中文 (zh-CN) | [@jnMetaCode](https://github.com/jnMetaCode) | [agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | 141 个已翻译代理 + 46 个中国市场原创 |
| 🇨🇳 简体中文 (zh-CN) | [@dsclca12](https://github.com/dsclca12) | [agent-teams](https://github.com/dsclca12/agent-teams) | 独立翻译，包含 B站、微信、小红书本地化 |
| 🇧🇷 Português brasileiro (pt-BR) | [@jnMetaCode](https://github.com/jnMetaCode) | [agency-agents-pt-BR](https://github.com/jnMetaCode/agency-agents-pt-BR) | 184 个上游代理已翻译；欢迎巴西市场 PR |
| 🇷🇺 Русский (ru) | [@jnMetaCode](https://github.com/jnMetaCode) | [agency-agents-ru](https://github.com/jnMetaCode/agency-agents-ru) | 184 个上游代理已翻译；欢迎俄罗斯市场 PR |
| 🇮🇩 Bahasa Indonesia (id) | [@jnMetaCode](https://github.com/jnMetaCode) | [agency-agents-id](https://github.com/jnMetaCode/agency-agents-id) | 184 个上游代理已翻译；欢迎印度尼西亚市场 PR |
| 🇸🇦 العربية (ar) | [@jnMetaCode](https://github.com/jnMetaCode) | [agency-agents-ar](https://github.com/jnMetaCode/agency-agents-ar) | 184 个上游代理已翻译；欢迎阿拉伯市场 PR |
| 🇰🇷 한국어 (ko) | [@jnMetaCode](https://github.com/jnMetaCode) | [agency-agents-ko](https://github.com/jnMetaCode/agency-agents-ko) | 184 个上游代理全部翻译；欢迎韩国特色 PR |
| 🇯🇵 日本語 (ja-JP) | [@sscodeai](https://github.com/sscodeai) | [agency-agents-ja](https://github.com/sscodeai/agency-agents-ja) | 281 个日本本地化代理 + 97 个日本市场原创 + 27 个工作流程 |
| 🇻🇳 Tiếng Việt (vi-VN) | [@rodonguyen](https://github.com/rodonguyen) | [agency-agents](https://github.com/rodonguyen/agency-agents) | 越南语本地化起步版，聚焦 README、快速开始和高频使用文档 |

想添加翻译？提交一个 issue，我们会在此处添加链接。

---

## 🔗 相关资源

- [awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) —— 社区维护的 OpenClaw 代理集合（源自本仓库）

---

## 📜 许可证

MIT 许可证 —— 自由使用，商业或个人用途。署名感谢但不强制要求。

---

## 🙏 致谢

从一个关于 AI 代理专业化的 Reddit 帖子开始，已经成长为一些非凡的东西——**覆盖所有团队的 230+ 代理**，由来自世界各地的贡献者社区支持。这个仓库中的每个代理之所以存在，是因为有人足够关心，来编写它、测试它并分享它。

向每一个提交 PR、发起 issue、开始讨论，或只是尝试了一个代理并告诉我们什么有效的人——谢谢。你们就是 The Agency 不断进步的原因。

---

## 💬 社区

- **GitHub 讨论**: [分享你的成功故事](https://github.com/msitarzewski/agency-agents/discussions)
- **问题**: [报告 bug 或请求功能](https://github.com/msitarzewski/agency-agents/issues)
- **Reddit**：加入 r/ClaudeAI 上的讨论
- **Twitter/X**：使用 #TheAgency 标签分享

---

## 🚀 开始使用

1. **浏览**上方的代理，找到符合你需求的专家
2. **复制**代理到 `~/.claude/agents/` 用于 Claude Code 集成
3. **激活**代理——在你的 Claude 对话中引用它们
4. **自定义**代理人格集合和工作流程，适配你的特定需求
5. **分享**你的成果并回馈社区

---

<div align="center">

**🎭 The Agency：你的 AI 梦想团队已就位 🎭**

[⭐ 给仓库加星](https://github.com/msitarzewski/agency-agents) • [🍴 分叉它](https://github.com/msitarzewski/agency-agents/fork) • [🐛 报告问题](https://github.com/msitarzewski/agency-agents/issues) • [❤️ 赞助](https://github.com/sponsors/msitarzewski)

由社区 ❤️ 打造，为社区服务

</div>
