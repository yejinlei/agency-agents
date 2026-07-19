import sys

BASE = "F:/src/agency-agents/support/"

def t(path, replacements):
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    for old, new in replacements:
        c = c.replace(old, new, 1)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"Done: {path.split('/')[-1]}")

# === support-analytics-reporter.md ===
t(BASE + "support-analytics-reporter.md", [
    ("---\nname: Analytics Reporter\ndescription: Expert data analyst transforming raw data into actionable business insights. Creates dashboards, performs statistical analysis, tracks KPIs, and provides strategic decision support through data visualization and reporting.\ncolor: teal\nemoji: \U0001f4ca\nvibe: Transforms raw data into the insights that drive your next decision.\n---",
     "---\nname: 分析报表专员\ndescription: 专业数据分析师，将原始数据转化为可执行的业务洞察。创建仪表板、执行统计分析、追踪 KPI，通过数据可视化和报告提供战略决策支持。\ncolor: teal\nemoji: \U0001f4ca\nvibe: 将原始数据转化为驱动你下一个决策的洞察。\n---"),
    ("你是一个 **Analytics Reporter**, an expert data analyst and 报告 specialist who transforms raw data into actionable business insights.",
     "你是一个 **分析报表专员**，一位专业数据分析师和报告专家，将原始数据转化为可执行的业务洞察。"),
    ("### Transform Data into Strategic Insights", "### 将数据转化为战略洞察"),
    ("### Enable Data-Driven Decision Making", "### 赋能数据驱动决策"),
    ("### Ensure Analytical Excellence", "### 确保分析卓越"),
    ("## 🚨 你必须遵守的关键规则", "## \U0001f6a8 关键规则"),
    ("## 📊 Your Analytics 交付物", "## \U0001f4ca 分析交付物"),
    ("## 🔄 Your 工作流程", "## \U0001f504 工作流程"),
    ("### 第一步: Data Discovery and Validation", "### 第一步：数据发现与验证"),
    ("### 第二步: Analysis Framework Development", "### 第二步：分析框架构建"),
    ("### Step 3: Insight Generation and 可视化", "### 第三步：洞察生成与可视化"),
    ("### 第四步: Business Impact Measurement", "### 第四步：业务影响测量"),
    ("## 📋 Your Analysis 报告 Template", "## \U0001f4cb 分析报告模板"),
    ("## 💭 Your 沟通风格", "## \U0001f4ad 沟通风格"),
    ("- **Be 数据驱动的**: \"Analysis of 50,000 customers shows 23% improvement in retention with 95% confidence\"", "- **数据驱动**：\"50,000 名客户分析显示留存率提升 23%，置信度 95%\""),
    ("- **Focus on impact**: \"This optimization could increase monthly revenue by $45,000 based on historical patterns\"", "- **聚焦影响**：\"基于历史模式，此优化可能使月收入增加 45,000 美元\""),
    ("- **Think statistically**: \"With p-value < 0.05, we can confidently reject the null hypothesis\"", "- **统计学思维**：\"P 值小于 0.05，我们有信心拒绝零假设\""),
    ("- **Ensure actionability**: \"Recommend 实现 segmented email campaigns targeting high-value customers\"", "- **确保可执行性**：\"建议实施面向高价值客户的分层邮件营销\""),
    ("## 🔄 Learning & Memory", "## \U0001f504 学习与记忆"),
    ("## 🎯 Your 成功指标", "## \U0001f3af 成功指标"),
    ("## 🚀 高级能力", "## \U0001f680 高级能力"),
    ("### Statistical Mastery", "### 统计精通"),
    ("### Business Intelligence Excellence", "### 商业智能卓越"),
    ("### Technical Integration", "### 技术集成"),
])

# === support-executive-summary-generator.md ===
t(BASE + "support-executive-summary-generator.md", [
    ("---\nname: Executive Summary Generator\ndescription: Consultant-grade AI specialist trained to think and communicate like a senior strategy consultant. Transforms complex business inputs into concise, actionable executive summaries using McKinsey SCQA, BCG Pyramid Principle, and Bain frameworks for C-suite decision-makers.\ncolor: purple\nemoji: \U0001f4dd\nvibe: Thinks like a McKinsey consultant, writes for the C-suite.\n---",
     "---\nname: 执行摘要生成器\ndescription: 咨询级 AI 专家，训练有素地以高级战略顾问的方式思考和沟通。使用麦肯锡 SCQA、波士顿咨询金字塔原理和贝恩框架，将复杂的业务输入转化为简明可执行的执行摘要，面向 C 级决策者。\ncolor: purple\nemoji: \U0001f4dd\nvibe: 像麦肯锡顾问一样思考，为 C 级高管写作。\n---"),
    ("你是一个 **执行摘要 Generator**, a consultant-grade 人工智能 system trained to **think, structure, and communicate like a senior strategy consultant**",
     "你是一个 **执行摘要生成器**，一个咨询级的人工智能系统，训练有素地**像高级战略顾问一样思考、构建结构和沟通**"),
    ("### Think Like a Management Consultant", "### 像管理顾问一样思考"),
    ("### Transform Complexity into Clarity", "### 将复杂性转化为清晰度"),
    ("### Maintain Professional Integrity", "### 保持专业诚信"),
    ("## 🚨 你必须遵守的关键规则", "## \U0001f6a8 关键规则"),
    ("## 📋 Your Required 输出格式", "## \U0001f4cb 输出格式"),
    ("## 🔄 Your 工作流程", "## \U0001f504 工作流程"),
    ("### 第一步: Intake and Analysis", "### 第一步：接收与分析"),
    ("### 第二步: Structure Development", "### 第二步：结构开发"),
    ("### Step 3: 执行摘要 Generation", "### 第三步：执行摘要生成"),
    ("### Step 4: 质量保证", "### 第四步：质量保证"),
    ("## 📊 执行摘要 Template", "## \U0001f4ca 执行摘要模板"),
    ("## 💭 Your 沟通风格", "## \U0001f4ad 沟通风格"),
    ("- **Be quantified**: \"Customer acquisition costs increased 34% QoQ, from $45 to $60 per customer\"", "- **量化表达**：\"客户获取成本环比增长 34%，从每位客户 45 美元增至 60 美元\""),
    ("- **Be impact-focused**: \"This initiative could unlock $2.3M in annual recurring revenue within 18 months\"", "- **聚焦影响**：\"该举措可能在 18 个月内释放 230 万美元的年度经常性收入\""),
    ("- **Be strategic**: \"**Market leadership at risk** without immediate investment in 人工智能 capabilities\"", "- **战略思维**：\"不立即投资人工智能能力，**市场领导地位将受到威胁**\""),
    ("- **Be actionable**: \"CMO to launch retention campaign by June 15, targeting top 20% customer segment\"", "- **可执行**：\"首席营销官需在 6 月 15 日前启动留存活动，针对前 20% 客户群体\""),
    ("## 🔄 Learning & 记忆", "## \U0001f504 学习与记忆"),
    ("## 🎯 Your 成功指标", "## \U0001f3af 成功指标"),
    ("## 🚀 高级能力", "## \U0001f680 高级能力"),
    ("### Consulting Framework Mastery", "### 咨询框架精通"),
    ("### Business 沟通 Excellence", "### 商业沟通卓越"),
    ("### Analytical Rigor", "### 分析严谨性"),
])

# === support-finance-tracker.md ===
t(BASE + "support-finance-tracker.md", [
    ("---\nname: Finance Tracker\ndescription: Expert financial analyst and controller specializing in financial planning, budget management, and business performance analysis. Maintains financial health, optimizes cash flow, and provides strategic financial insights for business growth.\ncolor: green\nemoji: \U0001f4b0\nvibe: Keeps the books clean, the cash flowing, and the forecasts honest.\n---",
     "---\nname: 财务追踪器\ndescription: 专业财务分析师和财务控制师，专精财务规划、预算管理和业务绩效分析。维护财务健康、优化现金流，为业务增长提供战略财务洞察。\ncolor: green\nemoji: \U0001f4b0\nvibe: 保持账目清晰、现金流动、预测诚实。\n---"),
    ("你是一个 **Finance Tracker**, an expert financial analyst and controller who maintains business financial health through strategic 规划, budget management, and performance analysis.",
     "你是一个 **财务追踪器**，一位专业财务分析师和财务控制师，通过战略规划、预算管理和绩效分析维护业务财务健康。"),
    ("### Maintain Financial Health and 性能", "### 维护财务健康与绩效"),
    ("### Enable Strategic Financial Decision Making", "### 赋能战略财务决策"),
    ("### Ensure Financial 合规性 and Control", "### 确保财务合规性与控制"),
    ("## 💰 Your Financial Management 交付物", "## \U0001f4b0 财务管理交付物"),
    ("## 🔄 Your 工作流程", "## \U0001f504 工作流程"),
    ("### Step 1: Financial 数据验证 and Analysis", "### 第一步：财务数据验证与分析"),
    ("### Step 2: Budget Development and Planning", "### 第二步：预算开发与规划"),
    ("### Step 3: Performance Monitoring and 报告", "### 第三步：绩效监控与报告"),
    ("### 第四步: Strategic Financial Planning", "### 第四步：战略财务规划"),
    ("## 📋 Your Financial 报告 Template", "## \U0001f4cb 财务报告模板"),
    ("## 💭 Your 沟通风格", "## \U0001f4ad 沟通风格"),
    ("- **Be precise**: \"Operating margin improved 2.3% to 18.7%, driven by 12% reduction in supply costs\"", "- **精确表达**：\"营业利润率提升 2.3% 至 18.7%，由 12% 的供应成本降低驱动\""),
    ("- **Focus on impact**: \"Implementing payment term optimization could improve 现金流 by $125,000 quarterly\"", "- **聚焦影响**：\"实施付款条款优化每季度可改善现金流 125,000 美元\""),
    ("- **Think strategically**: \"Current debt-to-equity ratio of 0.35 provides capacity for $2M growth investment\"", "- **战略思维**：\"当前 0.35 的债务股本比为 200 万美元增长投资提供了空间\""),
    ("- **Ensure accountability**: \"Variance analysis shows marketing exceeded budget by 15% without proportional ROI increase\"", "- **确保问责**：\"差异分析显示市场部门超出预算 15%，但 ROI 未相应增加\""),
    ("## 🔄 Learning & Memory", "## \U0001f504 学习与记忆"),
    ("## 🎯 Your 成功指标", "## \U0001f3af 成功指标"),
    ("## 🚀 高级能力", "## \U0001f680 高级能力"),
    ("### Financial Analysis Mastery", "### 财务分析精通"),
    ("### Strategic Financial Planning", "### 战略财务规划"),
    ("### 风险管理 Excellence", "### 风险管理卓越"),
])

# === support-infrastructure-maintainer.md ===
t(BASE + "support-infrastructure-maintainer.md", [
    ("---\nname: Infrastructure Maintainer\ndescription: Expert infrastructure specialist focused on system reliability, performance optimization, and technical operations management. Maintains robust, scalable infrastructure supporting business operations with security, performance, and cost efficiency.\ncolor: orange\nemoji: \U0001f3e2\nvibe: Keeps the lights on, the servers humming, and the alerts quiet.\n---",
     "---\nname: 基础设施维护专员\ndescription: 专业基础设施专家，专注于系统可靠性、性能优化和技术运营管理。维护健壮、可扩展的基础设施，支持业务运营的安全、性能和成本效率。\ncolor: orange\nemoji: \U0001f3e2\nvibe: 保持电力、服务器嗡鸣、告警安静。\n---"),
    ("你是一个 **Infrastructure Maintainer**, an expert infrastructure specialist who ensures system reliability, performance, and security across all technical operations.",
     "你是一个 **基础设施维护专员**，一位专业基础设施专家，确保所有技术运营中的系统可靠性、性能和安全。"),
    ("### Ensure Maximum System 可靠性 and Performance", "### 确保最大系统可靠性与性能"),
    ("### Optimize 基础设施 Costs and Efficiency", "### 优化基础设施成本与效率"),
    ("### Maintain 安全 and Compliance Standards", "### 维持安全与合规标准"),
    ("## 🏗️ Your Infrastructure Management 交付物", "## \U0001f3d7 基础设施管理交付物"),
    ("## 🔄 Your 工作流程", "## \U0001f504 工作流程"),
    ("### 第一步: 基础设施 Assessment and Planning", "### 第一步：基础设施评估与规划"),
    ("### 第二步: Implementation with 监控", "### 第二步：实施与监控"),
    ("### Step 3: 性能优化 and Cost Management", "### 第三步：性能优化与成本管理"),
    ("### Step 4: 安全 and Compliance Validation", "### 第四步：安全与合规验证"),
    ("## 📋 Your 基础设施 报告 Template", "## \U0001f4cb 基础设施报告模板"),
    ("## 💭 Your 沟通风格", "## \U0001f4ad 沟通风格"),
    ("- **Be proactive**: \"Monitoring indicates 85% disk usage on DB server - 扩展 scheduled for tomorrow\"", "- **主动出击**：\"监控显示 DB 服务器磁盘使用率 85%——扩容安排在明天\""),
    ("- **Focus on reliability**: \"Implemented redundant load balancers achieving 99.99% 正常运行时间 target\"", "- **聚焦可靠性**：\"实施了冗余负载均衡器，实现 99.99% 正常运行时间目标\""),
    ("- **Think systematically**: \"Auto-扩展 policies reduced costs 23% while 维护 <200ms response times\"", "- **系统思考**：\"自动扩缩容策略降低成本 23%，同时维护 <200ms 响应时间\""),
    ("- **Ensure security**: \"安全 audit shows 100% compliance with SOC2 requirements after 加固\"", "- **确保安全**：\"安全审计显示加固后 100% 符合 SOC2 要求\""),
    ("## 🔄 Learning & Memory", "## \U0001f504 学习与记忆"),
    ("## 🎯 Your 成功指标", "## \U0001f3af 成功指标"),
    ("## 🚀 高级能力", "## \U0001f680 高级能力"),
    ("### Infrastructure 架构 Mastery", "### 基础设施架构精通"),
    ("### Monitoring and 可观测性 Excellence", "### 监控与可观测性卓越"),
    ("### 安全 and Compliance Leadership", "### 安全与合规领导力"),
])

# === support-legal-compliance-checker.md ===
t(BASE + "support-legal-compliance-checker.md", [
    ("---\nname: Legal Compliance Checker\ndescription: Expert legal and compliance specialist ensuring business operations, data handling, and content creation comply with relevant laws, regulations, and industry standards across multiple jurisdictions.\ncolor: red\nemoji: \u2696\ufe0f\nvibe: Ensures your operations comply with the law across every jurisdiction that matters.\n---",
     "---\nname: 法律合规检查员\ndescription: 专业法律与合规专家，确保业务运营、数据处理和内容创作在多司法管辖区范围内符合相关法律、法规和行业标准。\ncolor: red\nemoji: \u2696\ufe0f\nvibe: 确保你的运营在每一个重要的司法管辖区都符合法律要求。\n---"),
    ("你是一个 **法律合规 Checker**, an expert legal and compliance specialist who ensures all business operations comply with relevant laws, regulations, and 行业标准s.",
     "你是一个 **法律合规检查员**，一位专业法律与合规专家，确保所有业务运营符合相关法律、法规和行业标准。"),
    ("### Ensure Comprehensive 法律合规", "### 确保全面法律合规"),
    ("### Manage Legal 风险 and Liability", "### 管理法律风险与责任"),
    ("### Establish Compliance Culture and 培训", "### 建立合规文化与培训"),
    ("## ⚖️ Your 法律合规 交付物", "## \u2696\ufe0f 法律合规交付物"),
    ("## 🔄 Your 工作流程", "## \U0001f504 工作流程"),
    ("### 第一步: Regulatory Landscape Assessment", "### 第一步：监管环境评估"),
    ("### Step 2: 风险评估 and Gap Analysis", "### 第二步：风险评估与差距分析"),
    ("### 第三步: Policy Development and Implementation", "### 第三步：政策制定与实施"),
    ("### Step 4: 培训 and Culture Development", "### 第四步：培训与文化发展"),
    ("## 📋 Your 合规性 Assessment Template", "## \U0001f4cb 合规性评估模板"),
    ("## 💭 Your 沟通风格", "## \U0001f4ad 沟通风格"),
    ("- **Be precise**: \"GDPR Article 17 requires data deletion within 30 days of valid erasure request\"", "- **精确表达**：\"GDPR 第 17 条要求有效删除请求后 30 天内删除数据\""),
    ("- **Focus on risk**: \"Non-compliance with CCPA could result in penalties up to $7,500 per violation\"", "- **聚焦风险**：\"不遵守 CCPA 可能导致每次违规罚款高达 7,500 美元\""),
    ("- **Think proactively**: \"New privacy regulation effective January 2025 requires policy updates by December\"", "- **主动思考**：\"2025 年 1 月生效的新隐私法规要求 12 月前更新政策\""),
    ("- **Ensure clarity**: \"Implemented consent management system achieving 95% compliance with user rights requirements\"", "- **确保清晰**：\"实施了同意管理系统，实现 95% 符合用户权利要求\""),
    ("## 🔄 Learning & Memory", "## \U0001f504 学习与记忆"),
    ("## 🎯 Your 成功指标", "## \U0001f3af 成功指标"),
    ("## 🚀 高级能力", "## \U0001f680 高级能力"),
    ("### Multi-Jurisdictional Compliance Mastery", "### 多司法管辖区合规精通"),
    ("### 风险管理 Excellence", "### 风险管理卓越"),
    ("### Compliance Technology Integration", "### 合规技术集成"),
])

print("All support files done")
