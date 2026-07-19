import sys

BASE = "F:/src/agency-agents/"

def batch_fm(dname, replacements):
    for fname, old, new in replacements:
        path = BASE + dname + "/" + fname
        try:
            with open(path, 'r', encoding='utf-8') as f:
                c = f.read()
            c = c.replace(old, new, 1)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(c)
            print(f"  {fname}")
        except FileNotFoundError:
            print(f"  NOT FOUND: {fname}")

# === paid-media (7 files) ===
print("=== paid-media ===")
batch_fm("paid-media", [
    ("paid-media-auditor.md",
     "---\nname: Paid Media Auditor\ndescription: Comprehensive paid media auditor who systematically evaluates Google Ads, Microsoft Ads, and Meta accounts across 200+ checkpoints spanning account structure, tracking, bidding, creative, audiences, and competitive positioning. Produces actionable audit reports with prioritized recommendations and projected impact.\n",
     "---\nname: 付费媒体审计师\ndescription: 全面的付费媒体审计师，系统性评估 Google Ads、Microsoft Ads 和 Meta 账户，跨越账户结构、追踪、竞价、创意、受众和竞争定位的 200+ 检查点。产出可操作的审计报告，包含优先排序的建议和预期影响。\n"),
    ("paid-media-creative-strategist.md",
     "---\nname: Ad Creative Strategist\ndescription: Paid media creative specialist focused on ad copywriting, RSA optimization, asset group design, and creative testing frameworks across Google, Meta, Microsoft, and programmatic platforms. Bridges the gap between performance data and persuasive messaging.\n",
     "---\nname: 广告创意战略师\ndescription: 付费媒体创意专家，专注于广告文案撰写、RSA 优化、资产组设计和跨 Google、Meta、Microsoft 及程序化平台的创意测试框架。架起性能数据与说服性信息之间的桥梁。\n"),
    ("paid-media-paid-social-strategist.md",
     "---\nname: Paid Social Strategist\ndescription: Cross-platform paid social advertising specialist covering Meta (Facebook/Instagram), LinkedIn, TikTok, Pinterest, X, and Snapchat. Designs full-funnel social ad programs from prospecting through retargeting with platform-specific creative and audience strategies.\n",
     "---\nname: 付费社交广告战略师\ndescription: 跨平台付费社交广告专家，覆盖 Meta（Facebook/Instagram）、LinkedIn、TikTok、Pinterest、X 和 Snapchat。设计从潜客开发到再营销的全漏斗社交广告计划，附带平台特定的创意和受众策略。\n"),
    ("paid-media-ppc-strategist.md",
     "---\nname: PPC Campaign Strategist\ndescription: Senior paid media strategist specializing in large-scale search, shopping, and performance max campaign architecture across Google, Microsoft, and Amazon ad platforms. Designs account structures, budget allocation frameworks, and bidding strategies that scale from $10K to $10M+ monthly spend.\n",
     "---\nname: PPC 广告战略师\ndescription: 资深付费媒体战略师，专精跨 Google、Microsoft 和 Amazon 广告平台的大规模搜索、购物和效果最大化广告架构。设计账户结构、预算分配框架和竞价策略，支持从每月 1 万美元到 1000 万美元以上的规模扩展。\n"),
    ("paid-media-programmatic-buyer.md",
     "---\nname: Programmatic & Display Buyer\ndescription: Display advertising and programmatic media buying specialist covering managed placements, Google Display Network, DV360, trade desk platforms, partner media (newsletters, sponsored content), and ABM display strategies via platforms like Demandbase and 6Sense.\n",
     "---\nname: 程序化与展示广告采购师\ndescription: 展示广告和程序化媒体采购专家，覆盖管理广告位、Google 展示网络、DV360、交易台平台、合作伙伴媒体（通讯、赞助内容）以及通过 Demandbase 和 6Sense 等平台的 ABM 展示策略。\n"),
    ("paid-media-search-query-analyst.md",
     "---\nname: Search Query Analyst\ndescription: Specialist in search term analysis, negative keyword architecture, and query-to-intent mapping. Turns raw search query data into actionable optimizations that eliminate waste and amplify high-intent traffic across paid search accounts.\n",
     "---\nname: 搜索查询分析师\ndescription: 搜索词分析、否定关键词架构和查询意图映射专家。将原始搜索查询数据转化为可操作的优化，消除浪费并在付费搜索账户中放大高意图流量。\n"),
    ("paid-media-tracking-specialist.md",
     "---\nname: Tracking & Measurement Specialist\ndescription: Expert in conversion tracking architecture, tag management, and attribution modeling across Google Tag Manager, GA4, Google Ads, Meta CAPI, LinkedIn Insight Tag, and server-side implementations. Ensures every conversion is counted correctly and every dollar of ad spend is measurable.\n",
     "---\nname: 追踪与测量专家\ndescription: 跨 Google Tag Manager、GA4、Google Ads、Meta CAPI、LinkedIn Insight Tag 和服务端实施的转化追踪架构、标签管理和归因建模专家。确保每次转化都被正确计数，每美元广告支出都可测量。\n"),
])

# === product (5 files) ===
print("=== product ===")
batch_fm("product", [
    ("product-behavioral-nudge-engine.md",
     "---\nname: Behavioral Nudge Engine\ndescription: Behavioral science specialist who applies choice architecture, loss aversion, and motivational psychology to product design. Designs interventions that move behavior through micro-friction, default optimization, and incentive restructuring rather than feature bloat.\n",
     "---\nname: 行为助推引擎\ndescription: 行为科学专家，将选择架构、损失厌恶和动机心理学应用于产品设计。通过微摩擦、默认值优化和激励重构而非功能膨胀来设计推动行为的干预措施。\n"),
    ("product-feedback-synthesizer.md",
     "---\nname: Feedback Synthesizer\ndescription: Customer feedback analyst who aggregates, synthesizes, and prioritizes user feedback from support tickets, app store reviews, NPS surveys, user interviews, and product analytics. Turns scattered signals into structured product priorities.\n",
     "---\nname: 反馈综合器\ndescription: 客户反馈分析师，聚合、综合和优先排序来自支持工单、应用商店评论、NPS 调查、用户访谈和产品分析的用户反馈。将零散信号转化为结构化的产品优先级。\n"),
    ("product-manager.md",
     "---\nname: Product Manager\ndescription: Strategic product leader who defines vision, prioritizes roadmap, and orchestrates cross-functional execution. Translates customer needs into product strategy, balances trade-offs across stakeholder interests, and drives measurable outcomes from concept to launch.\n",
     "---\nname: 产品经理\ndescription: 战略产品领导者，定义愿景、优先排序路线图并协调跨职能执行。将客户需求转化为产品战略，平衡不同利益相关者之间的权衡，从概念到发布推动可衡量的成果。\n"),
    ("product-sprint-prioritizer.md",
     "---\nname: Sprint Prioritizer\ndescription: Agile sprint planning specialist who translates strategic priorities into sprint-ready backlogs. Applies WSJF scoring, dependency analysis, and capacity modeling to sequence work that maximizes value delivery within team constraints.\n",
     "---\nname: 冲刺优先排序师\ndescription: 敏捷冲刺规划专家，将战略优先级转化为冲刺就绪的待办列表。应用 WSJF 评分、依赖分析和容量建模，在团队约束内排序最大化价值交付的工作。\n"),
    ("product-trend-researcher.md",
     "---\nname: Trend Researcher\ndescription: Market intelligence analyst who identifies emerging product trends, competitive shifts, and technology inflection points. Synthesizes signals from research reports, funding announcements, patent filings, and community discussions into actionable product intelligence.\n",
     "---\nname: 趋势研究员\ndescription: 市场情报分析师，识别新兴产品趋势、竞争变化和技术拐点。将来自研究报告、融资公告、专利申请和社区讨论的信号综合为可操作的产品情报。\n"),
])

# === project-management (7 files) ===
print("=== project-management ===")
batch_fm("project-management", [
    ("project-management-experiment-tracker.md",
     "---\nname: Experiment Tracker\ndescription: Scientific rigor specialist for product experimentation. Designs A/B tests, defines success metrics, monitors statistical significance, and turns experimental findings into product decisions with proper confidence intervals and practical significance assessment.\n",
     "---\nname: 实验追踪器\ndescription: 产品实验的科学严谨性专家。设计 A/B 测试、定义成功指标、监控统计显著性，将实验发现转化为产品决策，附带适当的置信区间和实际显著性评估。\n"),
    ("project-management-jira-workflow-steward.md",
     "---\nname: Jira Workflow Steward\ndescription: Project workflow architect who designs, documents, and maintains Jira workflows, board configurations, and reporting structures. Ensures project visibility, proper handoffs, and accurate progress tracking across all teams.\n",
     "---\nname: Jira 工作流管理员\ndescription: 项目工作流架构师，设计、记录和维护 Jira 工作流、看板配置和报告结构。确保项目可见性、正确的交接和所有团队的准确进度追踪。\n"),
    ("project-management-meeting-notes-specialist.md",
     "---\nname: Meeting Notes Specialist\ndescription: Document specialist who transforms meeting transcripts into structured, actionable notes. Captures decisions, action items, owners, and deadlines while maintaining context and follow-up threads.\n",
     "---\nname: 会议纪要专家\ndescription: 文档专家，将会议记录转化为结构化、可操作的笔记。捕获决策、行动项目、负责人和截止日期，同时保持上下文和后续线程。\n"),
    ("project-management-project-shepherd.md",
     "---\nname: Project Shepherd\ndescription: End-to-end project coordinator who manages project lifecycles from intake through delivery. Tracks dependencies, mitigates risks, coordinates handoffs, and ensures projects complete on time with clear communication to all stakeholders.\n",
     "---\nname: 项目牧羊人\ndescription: 端到端项目协调员，管理从接收到交付的项目生命周期。追踪依赖关系、缓解风险、协调交接，确保项目按时完成并与所有利益相关者保持清晰沟通。\n"),
    ("project-management-studio-operations.md",
     "---\nname: Studio Operations\ndescription: Creative studio operations specialist who manages project intake, resource allocation, deadline tracking, and production workflows. Ensures creative teams have what they need, when they need it, without operational friction.\n",
     "---\nname: 工作室运营师\ndescription: 创意工作室运营专家，管理项目接收、资源分配、截止日期追踪和生产工作流。确保创意团队在需要时获得所需资源，没有运营摩擦。\n"),
    ("project-management-studio-producer.md",
     "---\nname: Studio Producer\ndescription: Creative production manager who coordinates talent scheduling, asset tracking, revision workflows, and delivery milestones. Bridges creative vision with operational execution to deliver projects on time and on brand.\n",
     "---\nname: 工作室制作人\ndescription: 创意制作经理，协调人才调度、资产追踪、修订工作流和交付里程碑。架起创意愿景与运营执行之间的桥梁，按时按品牌交付项目。\n"),
    ("project-manager-senior.md",
     "---\nname: Senior Project Manager\ndescription: Strategic project leader who manages complex, high-stakes initiatives across multiple workstreams. Balances scope, timeline, budget, and quality while maintaining stakeholder alignment and driving execution excellence.\n",
     "---\nname: 高级项目经理\ndescription: 战略项目领导者，管理跨多个工作流的复杂、高风险举措。平衡范围、时间线、预算和质量，同时保持利益相关者对齐并推动执行卓越。\n"),
])

print("All frontmatters done")
