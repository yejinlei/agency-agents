import re

filepath = "F:/src/agency-agents/README.md"
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

def repl(old, new):
    content_global = [content]
    def inner():
        content_global[0] = content_global[0].replace(old, new)
        return content_global[0]
    return inner()

# ============================================================
# 1. TABLE HEADERS
# ============================================================
content = content.replace("| Agent | Specialty | 使用场景 |", "| 代理 | 专长 | 使用场景 |")
content = content.replace("| Agent | Specialty | 使用场景 |", "| 代理 | 专长 | 使用场景 |")
content = content.replace("| --- | --- | --- |", "| --- | --- | --- |")

# ============================================================
# 2. DIVISION/SECTION HEADERS (English Division suffixes)
# ============================================================
content = content.replace("### 📢 Marketing Division", "### 📢 营销团队")
content = content.replace("### 🧪 测试 Division", "### 🧪 测试团队")
content = content.replace("### 🔒 安全 Division", "### 🔒 安全团队")
content = content.replace("### 🛟 Support Division", "### 🛟 支持团队")
content = content.replace("### 🥽 Spatial Computing Division", "### 🥽 空间计算团队")
content = content.replace("### 🎯 Specialized Division", "### 🎯 专业团队")
content = content.replace("### 💵 Finance Division", "### 💵 财务团队")
content = content.replace("### 📚 Academic Division", "### 📚 学术团队")
content = content.replace("### 🎬 Project Management Division", "### 🎬 项目管理团队")
content = content.replace("### 🎮 Game Development Division", "### 🎮 游戏开发团队")
content = content.replace("### 🌍 GIS Division", "### 🌍 GIS 团队")
content = content.replace("### 📊 Product Division", "### 📊 产品团队")

# ============================================================
# 3. DIVISION DESCRIPTION LINES (standalone English sentences)
# ============================================================
content = content.replace("Building the right thing at the right time.", "在正确的时间构建正确的事情。")
content = content.replace("Keeping the trains 运行ning on time (and under budget).", "让项目准时交付（且预算可控）。")
content = content.replace("Breaking things so users don't have to.", "破坏一切，让用户无需操心。")
content = content.replace("Defending the stack — from secure-by-design architecture to breach response.", "守护整个技术栈——从安全设计到入侵响应。")
content = content.replace("The backbone of the operation.", "运营的中坚力量。")
content = content.replace("Building the immersive future.", "构建沉浸式未来。")
content = content.replace("The unique specialists who don't fit in a box.", "无法归类在某个部门的独特专家。")
content = content.replace("Accounting, financial analysis, tax strategy, and investment research specialists.", "会计、财务分析、税务策略和投资研究专家。")
content = content.replace("Building worlds, systems, and experiences across every major engine.", "跨所有主流引擎构建世界、系统和体验。")
content = content.replace("Cross-Engine Agents (Engine-Agnostic)", "跨引擎代理（引擎无关）")
content = content.replace("Scholarly rigor for world-构建, storytelling, and narrative design.", "为世界观构建、叙事和故事设计提供学术严谨性。")
content = content.replace("Mapping the Earth, 分析 the built world, and extracting intelligence from geospatial data.", "测绘地球、分析建成世界，并从地理空间数据中提取情报。")

# ============================================================
# 4. MISC TEXT (non-table prose)
# ============================================================
content = content.replace("## 🎁 与众不同之处?", "## 🎁 与众不同之处？")
content = content.replace("## 🎨 Agent 性格 Highlights", "## 🎨 代理性格亮点")
content = content.replace("## 🔗 Related 资源", "## 🔗 相关资源")
content = content.replace("社区翻译 & 本地化s", "社区翻译 & 本地化")
content = content.replace(
    "社区翻译 & 本地化. 这些是独立维护的 -- 查看每个仓库的覆盖范围和版本兼容性.",
    "社区翻译 & 本地化。这些是独立维护的——查看每个仓库的覆盖范围和版本兼容性。"
)
content = content.replace("- [x] Multi-agent 工作流程 examples -- 参见 [examples/](examples/)",
    "- [x] 多代理工作流程示例 —— 参见 [examples/](examples/)")
content = content.replace("1. Fork the repository", "1. 分叉本仓库")
content = content.replace(
    "**成果**：一次会话中产出全面的跨职能产品蓝图。 [More examples](examples/).",
    "**成果**：一次会话中产出全面的跨职能产品蓝图。 [更多示例](examples/)"
)
content = content.replace("MIT 许可证 - 自由使用，商业或个人. 署名感谢但不要求.",
    "MIT 许可证 —— 自由使用，商业或个人用途。署名感谢但不强制要求。")
content = content.replace("- **Reddit**：加入 r/Claude人工智能 上的讨论",
    "- **Reddit**：加入 r/ClaudeAI 上的讨论")
content = content.replace("2. **Copy** the agents to `~/.claude/agents/` 用于 Claude Code 集成",
    "2. **复制**代理到 `~/.claude/agents/` 用于 Claude Code 集成")
content = content.replace("4. **Customize** 代理人格集合 and 工作流程 适合你的特定需求",
    "4. **自定义**代理人格集合和工作流程，适配你的特定需求")

# --- Scenarios ---
content = content.replace(
    "**Your Team**:\n1. 🎨 **前端开发者** —— 构建 React 应用\n2. 🏗️ **后端架构师** —— 设计 API 和数据库\n3. 🚀 **增长黑客** —— 规划用户获取\n4. ⚡ **快速原型师** —— 快速迭代周期\n5. 🔍 **现实检查师** —— 上线前确保质量",
    "**你的团队**：\n1. 🎨 **前端开发者** —— 构建 React 应用\n2. 🏗️ **后端架构师** —— 设计 API 和数据库\n3. 🚀 **增长黑客** —— 规划用户获取\n4. ⚡ **快速原型师** —— 快速迭代周期\n5. 🔍 **现实检查师** —— 上线前确保质量"
)
content = content.replace(
    "**Your Team**:\n1. 📝 **内容创作者** —— 制作活动内容\n2. 🐦 **Twitter 互动师** —— Twitter 策略与执行\n3. 📸 **Instagram 策划师** —— 视觉内容和故事\n4. 🤝 **Reddit 社群建设师** —— 真实的社群互动\n5. 📊 **数据分析报告师** —— 追踪和优化绩效",
    "**你的团队**：\n1. 📝 **内容创作者** —— 制作活动内容\n2. 🐦 **Twitter 互动师** —— Twitter 策略与执行\n3. 📸 **Instagram 策划师** —— 视觉内容和故事\n4. 🤝 **Reddit 社群建设师** —— 真实的社群互动\n5. 📊 **数据分析报告师** —— 追踪和优化绩效"
)
content = content.replace(
    "**Your Team**:\n1. 👔 **Senior Project Manager** - Scope and task 规划\n2. 💎 **Senior Developer** - Complex implementation\n3. 🎨 **界面设计er** - Design system and components\n4. 🧪 **Experiment Tracker** - A/B test 规划\n5. 📸 **Evidence Collector** - Quality verification\n6. 🔍 **Reality Checker** - Production readiness",
    "**你的团队**：\n1. 👔 **高级项目经理** —— 范围控制和任务规划\n2. 💎 **高级开发者** —— 复杂实现\n3. 🎨 **界面设计师** —— 设计系统和组件\n4. 🧪 **实验追踪器** —— A/B 测试规划\n5. 📸 **证据收集员** —— 质量验证\n6. 🔍 **现实检查员** —— 生产就绪性"
)
content = content.replace(
    "**Your Team**:\n\n1. 📋 **Paid Media Auditor** - Comprehensive account assessment\n2. 📡 **Tracking & Measurement Specialist** - Verify conversion 追踪 accuracy\n3. 💰 **PPC Campaign Strategist** - Redesign account architecture\n4. 🔍 **Search Query Analyst** - Clean up wasted spend from search terms\n5. ✍️ **Ad Creative Strategist** - Refresh all ad copy and extensions\n6. 📊 **Analytics Reporter** (Support Division) - Build 报告 dashboards",
    "**你的团队**：\n\n1. 📋 **付费媒体审计员** —— 全面账户评估\n2. 📡 **追踪与测量专家** —— 验证转化追踪准确性\n3. 💰 **PPC 广告战略师** —— 重构账户架构\n4. 🔍 **搜索查询分析师** —— 清除搜索词浪费支出\n5. ✍️ **广告创意战略师** —— 刷新所有广告文案和扩展\n6. 📊 **数据分析报告师**（支持团队）—— 构建报告仪表盘"
)

# --- Multi-Tool Integrations headings ---
content = content.replace("## 🔌 Multi-Tool Integrations", "## 🔌 多工具集成")
content = content.replace("### 支持的工具", "### 支持的工具")

# --- Agent personality highlights ---
content = content.replace("-- **Evidence Collector** (测试 Division)", "-- **证据收集员**（测试团队）")
content = content.replace("-- **Reddit Community Builder** (Marketing Division)", "-- **Reddit 社群建设师**（营销团队）")
content = content.replace("-- **Whimsy Injector** (Design Division)", "-- **趣味注入师**（设计团队）")
content = content.replace("-- **Whimsy Injector** (during a UX review)", "-- **趣味注入师**（UX 评审期间）")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Phase 1 done")
