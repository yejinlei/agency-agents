import sys
path = "F:\\src\\agency-agents\\README.md"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()

repl = []

# === Title & Tagline ===
repl.append(("# 🎭 The Agency: AI Specialists Ready to Transform Your Workflow", "# 🎭 The Agency：随时待命的 AI 专家团队"))
repl.append(("> **A complete AI agency at your fingertips** - From frontend wizards to Reddit community ninjas, from whimsy injectors to reality checkers. 每个代理都是 a specialized expert with personality, processes, and proven deliverables.", "> **触手可及的完整 AI 团队** — 从前端魔法师到 Reddit 社区忍者，从趣味注入师到现实检查员。每个代理都是一个拥有独特性格、完善流程和可验证交付物的专业专家。"))
repl.append(("> ### 🆕 There's an app now", "> ### 🆕 现在有了专用应用"))
repl.append(("> **[Agency Agents](https://agencyagents.app)** is a native app for **macOS, Linux & Windows** that browses the entire roster and installs it into Claude Code, Cursor, Codex, Gemini, Osaurus, and more — with a click. No clone, no scripts, and it auto-updates.", "> **[Agency Agents](https://agencyagents.app)** 是一款跨平台的原生桌面应用（macOS · Linux · Windows），只需一键即可浏览整个代理名录并将其安装到 Claude Code、Cursor、Codex、Gemini、Osaurus 等多个工具中。无需克隆仓库，无需编写脚本，并自动保持更新。"))

# === What is this? ===
repl.append(("- **🎯 Specialized**: 在其领域拥有深厚专业知识 (不是通用的提示模板)", "- **🎯 专业化**：在其领域拥有深厚专业知识（不是通用的提示模板）"))
repl.append(("- **🧠 性格-Driven**: 独特的声音、沟通方式和方法", "- **🧠 性格驱动**：独特的声音、沟通方式和方法"))
repl.append(("- **📋 Deliverable-Focused**: 真实的代码、流程、可衡量的结果", "- **📋 交付导向**：真实的代码、流程、可衡量的结果"))
repl.append(("- **✅ Production-Ready**: Battle-tested 工作流程 and success metrics", "- **✅ 生产就绪**：经过实战验证的工作流程和成功指标"))
repl.append(("**Think of it as**: Assembling your dream team, except they're 人工智能 specialists 他们永不睡觉、永不抱怨、始终交付.", "**可以这样理解**：组建你的梦想团队，只不过成员是永不睡觉、永不抱怨、始终交付的 AI 专家。"))

# === Quick Start Headers ===
repl.append(("### Option 1: Install the app (Recommended)", "### 方案一：安装应用（推荐）"))
repl.append(("### Option 2: Use with Claude Code", "### 方案二：配合 Claude Code 使用"))
repl.append(("### Option 3: Use as Reference", "### 方案三：作为参考资料"))
repl.append(("### Option 4: Use with Other Tools (GitHub Copilot, Antigravity, Gemini CLI, OpenCode, OpenClaw, Cursor, Aider, Windsurf, Kimi Code, Codex, Osaurus, Hermes, Mistral Vibe)", "### 方案四：配合其他工具使用（GitHub Copilot、Antigravity、Gemini CLI、OpenCode、OpenClaw、Cursor、Aider、Windsurf、Kimi Code、Codex、Osaurus、Hermes、Mistral Vibe）"))
repl.append(("that 浏览整个名录 并将代理安装到 Claude Code, Cursor, Codex, Gemini CLI, OpenCode, Qwen, and Osaurus 为你，然后保持它们最新.", "来浏览整个名录并将代理安装到 Claude Code、Cursor、Codex、Gemini CLI、OpenCode、Qwen 和 Osaurus 等工具中，并始终保持最新。"))
repl.append(("- Core mission & 工作流程", "- 核心使命 & 工作流程"))
repl.append(("# Step 1 -- generate integration files for all supported tools", "# 步骤一 —— 为所有支持的工具生成集成文件"))
repl.append(("# Step 2 -- install interactively (auto-detects what you have installed)", "# 步骤二 —— 交互式安装（自动检测已安装的工具）"))
repl.append(("# Or target a specific tool directly", "# 或者直接指定某个工具安装"))
repl.append(("> **OpenCode note:** OpenCode's 运行time currently registers only ~119 agents and silently drops the rest ([upstream bug](https://github.com/anomalyco/opencode/issues/27988)). Installing a subset with `--division` keeps you under that limit. The installer warns you when a selection would exceed it.", "> **OpenCode 注意：** OpenCode 的运行时目前只能注册约 119 个代理，超出部分会被静默丢弃（[上游 bug](https://github.com/anomalyco/opencode/issues/27988)）。使用 `--division` 安装子集可以避免超过该限制。安装器会在选择超出限制时发出警告。"))
repl.append(("参见 the [Multi-Tool Integrations](#-multi-tool-integrations) section below for full details.", "参见下方的[多工具集成](#-multi-tool-integrations)部分了解更多详情。"))

# === Division Intros ===
repl.append(("### 💻 工程 Division", "### 💻 工程团队"))
repl.append(("Building the future, one commit at a time.", "用一次一次提交，构建未来。"))
repl.append(("### 🎨 Design Division", "### 🎨 设计团队"))
repl.append(("Making it beautiful, usable, and delightful.", "让它更美观、更易用、更令人愉悦。"))
repl.append(("### 💰 Paid Media Division", "### 💰 付费媒体团队"))
repl.append(("Turning ad spend into measurable business outcomes.", "将广告投放转化为可衡量的商业成果。"))
repl.append(("### 💼 Sales Division", "### 💼 销售团队"))
repl.append(("Turning pipeline into revenue through craft, not CRM busywork.", "靠精湛手艺而非 CRM 琐事，将销售管道转化为收入。"))
repl.append(("### 📣 Marketing Division", "### 📣 营销团队"))
repl.append(("Growing your audience, one authentic interaction at a time.", "通过每一次真诚的互动，稳步增长你的受众。"))
repl.append(("### 🏥 Healthcare Division", "### 🏥 医疗健康团队"))
repl.append(("Building 人工智能 agents for regulated clinical and sovereign health contexts.", "为受监管的临床环境和主权健康场景构建 AI 代理。"))

# === Workflow Scenarios ===
repl.append(("### Scenario 1: Building a Startup MVP", "### 场景一：构建创业公司 MVP"))
repl.append(("**Result**: Ship faster with specialized expertise at every stage.", "**成果**：每个阶段都有专业专家支持，交付更快。"))
repl.append(("### Scenario 2: Marketing Campaign Launch", "### 场景二：营销活动上线"))
repl.append(("**Result**: Multi-channel coordinated campaign with platform-specific expertise.", "**成果**：多平台协调的营销活动，每个平台都有专属专家。"))
repl.append(("### Scenario 3: Enterprise Feature Development", "### 场景三：企业级功能开发"))
repl.append(("**Result**: Enterprise-grade delivery with quality gates and 文档.", "**成果**：企业级交付，包含质量门禁和文档。"))
repl.append(("### Scenario 4: Paid Media Account Takeover", "### 场景四：付费媒体账户接管"))
repl.append(("**Result**: Systematic account takeover with 追踪 verified, waste eliminated, structure optimized, and creative refreshed — all within the first 30 days.", "**成果**：系统化的账户接管——追踪验证、消除浪费、优化结构、更新创意，全部在 30 天内完成。"))
repl.append(("### Scenario 5: Full Agency Product Discovery", "### 场景五：全团队产品探索"))
repl.append(("**Your Team**: All 8 divisions working in parallel on a single mission.", "**你的团队**：全部 8 个团队并行协作，共担一个使命。"))
repl.append(("参见 the **[Nexus Spatial Discovery Exercise](examples/nexus-spatial-discovery.md)** -- a complete example where 8 agents (Product Trend Researcher, Backend Architect, Brand Guardian, 增长 Hacker, Support Responder, 用户体验研究er, Project Shepherd, and XR Interface Architect) were deployed simultaneously 来评估软件机会 and produce a unified product plan covering market validation, technical architecture, brand strategy, go-to-market, support systems, UX research, project execution, and spatial UI design.", "参见 **[Nexus 空间探索练习](examples/nexus-spatial-discovery.md)**——一个完整的示例，8 个代理（产品趋势研究员、后端架构师、品牌守护者、增长黑客、客服响应员、用户体验研究员、项目牧人和 XR 界面架构师）同时部署，评估软件机会并产出一份统一的产品方案，涵盖市场验证、技术架构、品牌战略、上市策略、支持体系、UX 研究、项目执行和空间 UI 设计。"))
repl.append(("**Result**: Comprehensive, 跨职能 product blueprint produced in a single session.", "**成果**：一次会话中产出全面的跨职能产品蓝图。"))
repl.append(("### Scenario 6: Smart Campus Digital Twin", "### 场景六：智慧校园数字孪生"))
repl.append(("**Result**: A campus digital twin that combines BIM detail, drone reality capture, 3D visualization, and web accessibility — delivered by coordinated specialists in a single pipeline.", "**成果**：一个融合 BIM 细节、无人机实景捕捉、3D 可视化和 Web 访问能力的校园数字孪生，由协调一致的专家团队在单一管线中交付。"))

# === Contribution Guide ===
repl.append(("We welcome contributions! Here's how you can help:", "我们欢迎贡献！以下是你的参与方式："))
repl.append(("### Add a New Agent", "### 添加新代理"))
repl.append(("2. Create a new agent 文件在 the appropriate category", "2. 在适当的分类下创建一个新代理文件"))
repl.append(("3. Follow the agent template structure:", "3. 遵循代理模板结构："))
repl.append(("   - Frontmatter with name, description, color", "   - 包含名称、描述、颜色的 frontmatter"))
repl.append(("   - Identity & Memory section", "   - 身份与记忆章节"))
repl.append(("   - Core Mission", "   - 核心使命"))
repl.append(("   - 必须遵守的关键规则 (domain-specific)", "   - 必须遵守的关键规则（领域特定）"))
repl.append(("   - 技术交付物 with examples", "   - 技术交付物及示例"))
repl.append(("4. Submit a PR with your agent", "4. 提交包含你的代理的 PR"))
repl.append(("### Improve Existing Agents", "### 改进现有代理"))
repl.append(("- Add real-world examples", "- 添加真实世界示例"))
repl.append(("- Enhance code samples", "- 完善代码示例"))
repl.append(("- Update success metrics", "- 更新成功指标"))
repl.append(("- Improve 工作流程", "- 改进工作流程"))
repl.append(("### Share Your Success Stories", "### 分享你的成功故事"))
repl.append(("Have you used these agents successfully? Share your story in the [Discussions](https://github.com/msitarzewski/agency-agents/discussions)!", "你成功使用过这些代理吗？在[讨论区](https://github.com/msitarzewski/agency-agents/discussions)分享你的故事吧！"))

# === Design Philosophy ===
repl.append(("每个代理都是 designed with:", "每个代理都秉承以下设计理念："))
repl.append(("1. **🎭 Strong 性格**: Not generic templates - real character and voice", "1. **🎭 鲜明性格**：不是通用模板，而是真实的角色和声音"))
repl.append(("2. **📋 Clear 交付物**: Concrete outputs, not vague guidance", "2. **📋 清晰交付物**：具体的产出，而非模糊的指导"))
repl.append(("3. **✅ 成功指标**: Measurable outcomes and quality standards", "3. **✅ 成功指标**：可衡量的成果和质量标准"))
repl.append(("4. **🔄 Proven Workflows**: Step-by-step processes that work", "4. **🔄 经过验证的工作流程**：行之有效的一步一步流程"))
repl.append(("5. **💡 Learning Memory**: Pattern recognition and continuous improvement", "5. **💡 学习记忆**：模式识别与持续改进"))

# === What Makes It Unique ===
repl.append(("### Unlike Generic 人工智能 Prompts:", "### 与普通 AI 提示词不同："))
repl.append(("- ❌ Generic \"Act as a developer\" prompts", "- ❌ 通用的\"扮演开发者\"提示词"))
repl.append(("- ✅ Deep specialization with personality and process", "- ✅ 深度专业化，具备性格和流程"))
repl.append(("### Unlike Prompt Libraries:", "### 与提示词库不同："))
repl.append(("- ❌ One-off prompt collections", "- ❌ 一次性提示词集合"))
repl.append(("- ✅ Comprehensive agent systems with 工作流程 and deliverables", "- ✅ 完整的代理系统，包含工作流程和交付物"))
repl.append(("### Unlike 人工智能 Tools:", "### 与 AI 工具不同："))
repl.append(("- ❌ Black box tools you can't customize", "- ❌ 无法定制的\"黑盒\"工具"))
repl.append(("- ✅ Transparent, forkable, adaptable 代理人格集合", "- ✅ 透明、可分叉、可适配的代理人格集合"))

# === Personality Highlights ===
repl.append(("> \"I don't just test your code - I default to 查找 3-5 issues and require visual proof for everything.\"", "> \"我不只是测试你的代码——我默认会找出 3-5 个问题，并要求对每件事提供视觉证明。\""))
repl.append(("> \"You're not marketing on Reddit - you're becoming a valued community member who happens to represent a brand.\"", "> \"你不是在 Reddit 上做营销——你正在成为一个有价值、恰好代表某个品牌的社区成员。\""))
repl.append(("> \"Every playful element must serve a functional or emotional purpose. Design delight that enhances rather than distracts.\"", "> \"每一个趣味元素都必须服务于功能或情感目的。设计令人愉悦的体验，增强而非干扰。\""))
repl.append(("> \"Let me add a celebration animation that reduces task completion anxiety by 40%\"", "> \"让我加一个庆祝动画，将任务完成焦虑降低 40%\""))

# === Statistics ===
repl.append(("- 🎭 **230+ Specialized Agents** across every division", "- 🎭 **230+ 专业代理**，覆盖所有团队"))
repl.append(("- 📝 **10,000+ lines** of personality, process, and code examples", "- 📝 **10,000+ 行**性格设定、流程和代码示例"))
repl.append(("- ⏱️ **Months of iteration** from real-world usage", "- ⏱️ **数月的迭代**，来自真实世界的使用经验"))
repl.append(("- 🌟 **Battle-tested** 在生产环境中 environments", "- 🌟 **经过实战检验**，在生产环境中验证"))
repl.append(("- 💬 **50+ requests** in first 12 hours on Reddit", "- 💬 Reddit 上**首 12 小时收到 50+ 请求**"))

# === Multi-Tool Integrations ===
repl.append(("The Agency works natively with Claude Code, and ships conversion + install scripts so you can use the same agents across every major agentic coding tool.", "The Agency 原生支持 Claude Code，并附带转换和安装脚本，让你可以在所有主流 AI 编码工具中使用相同的代理。"))
repl.append(("- **[Claude Code](https://claude.ai/code)** — native `.md` agents, no conversion needed → `~/.claude/agents/`", "- **[Claude Code](https://claude.ai/code)** —— 原生 `.md` 代理，无需转换 → `~/.claude/agents/`"))
repl.append(("- **[GitHub Copilot](https://github.com/copilot)** — native `.md` agents, no conversion needed → `~/.github/agents/` + `~/.copilot/agents/`", "- **[GitHub Copilot](https://github.com/copilot)** —— 原生 `.md` 代理，无需转换 → `~/.github/agents/` + `~/.copilot/agents/`"))
repl.append(("- **[Antigravity](https://github.com/google-gemini/antigravity)** — `SKILL.md` per agent → `~/.gemini/config/skills/`", "- **[Antigravity](https://github.com/google-gemini/antigravity)** —— 每个代理一个 `SKILL.md` → `~/.gemini/config/skills/`"))
repl.append(("- **[Gemini CLI](https://github.com/google-gemini/gemini-cli)** -- `.md` agent files -> `~/.gemini/agents/`", "- **[Gemini CLI](https://github.com/google-gemini/gemini-cli)** —— `.md` 代理文件 → `~/.gemini/agents/`"))
repl.append(("- **[OpenCode](https://opencode.ai)** — `.md` agent files → `.opencode/agents/`", "- **[OpenCode](https://opencode.ai)** —— `.md` 代理文件 → `.opencode/agents/`"))
repl.append(("- **[Cursor](https://cursor.sh)** — `.mdc` rule files → `.cursor/rules/`", "- **[Cursor](https://cursor.sh)** —— `.mdc` 规则文件 → `.cursor/rules/`"))
repl.append(("- **[Aider](https://aider.chat)** — single `CONVENTIONS.md` → `./CONVENTIONS.md`", "- **[Aider](https://aider.chat)** —— 单个 `CONVENTIONS.md` → `./CONVENTIONS.md`"))
repl.append(("- **[Windsurf](https://codeium.com/windsurf)** — single `.windsurfrules` → `./.windsurfrules`", "- **[Windsurf](https://codeium.com/windsurf)** —— 单个 `.windsurfrules` → `./.windsurfrules`"))
repl.append(("- **[OpenClaw](https://github.com/openclaw/openclaw)** — `SOUL.md` + `AGENTS.md` + `IDENTITY.md` per agent", "- **[OpenClaw](https://github.com/openclaw/openclaw)** —— 每个代理包含 `SOUL.md` + `AGENTS.md` + `IDENTITY.md`"))
repl.append(("- **[Qwen Code](https://github.com/QwenLM/qwen-code)** — `.md` SubAgent files → `~/.qwen/agents/`", "- **[Qwen Code](https://github.com/QwenLM/qwen-code)** —— `.md` 子代理文件 → `~/.qwen/agents/`"))
repl.append(("- **[Kimi Code](https://github.com/Moonshot人工智能/kimi-cli)** — YAML agent specs → `~/.config/kimi/agents/`", "- **[Kimi Code](https://github.com/Moonshot人工智能/kimi-cli)** —— YAML 代理规范 → `~/.config/kimi/agents/`"))
repl.append(("- **[Codex](https://developers.openai.com/codex/overview)** — TOML custom agents → `~/.codex/agents/`", "- **[Codex](https://developers.openai.com/codex/overview)** —— TOML 自定义代理 → `~/.codex/agents/`"))
repl.append(("- **Osaurus** -- `SKILL.md` skills -> `~/.osaurus/skills/`", "- **Osaurus** —— `SKILL.md` 技能 → `~/.osaurus/skills/`"))
repl.append(("- **[Hermes](integrations/hermes/README.md)** -- lazy-router plugin -> `~/.hermes/plugins/`", "- **[Hermes](integrations/hermes/README.md)** —— 懒路由插件 → `~/.hermes/plugins/`"))

# === Install Steps ===
repl.append(("**Step 1 -- Generate integration files:**", "**步骤一 —— 生成集成文件：**"))
repl.append(("# Faster (parallel, output order may vary): ./scripts/convert.sh --parallel", "# 更快（并行，输出顺序可能不同）：./scripts/convert.sh --parallel"))
repl.append(("**Step 2 -- Install (interactive, auto-detects your tools):**", "**步骤二 —— 安装（交互式，自动检测你的工具）：**"))
repl.append(("# Faster (parallel, output order may vary): ./scripts/install.sh --no-interactive --parallel", "# 更快（并行，输出顺序可能不同）：./scripts/install.sh --no-interactive --parallel"))
repl.append(("The installer scans your system for 安装到ols, shows a checkbox UI, and lets you pick exactly what to install:", "安装器会扫描你的系统查找已安装的工具，显示复选框界面，让你精确选择要安装的内容："))
repl.append(("System scan: [*] = detected on this machine", "系统扫描：[*] = 在此机器上检测到"))
repl.append(("[1-14] toggle   [a] all   [n] none   [d] detected", "[1-14] 切换   [a] 全选   [n] 全不选   [d] 已检测"))
repl.append(("[Enter] install   [q] quit", "[回车] 安装   [q] 退出"))
repl.append(("**Or install a specific tool directly:**", "**或者直接安装特定工具：**"))
repl.append(("**Non-interactive (CI/scripts):**", "**非交互式（CI/脚本）：**"))
repl.append(("**Faster 运行s (parallel)** — On multi-core machines, use `--parallel` so each tool is processed in parallel. Output order across tools is non-deterministic. Works with both interactive and non-interactive install: e.g. `./scripts/install.sh --interactive --parallel` (pick tools, then install in parallel) or `./scripts/install.sh --no-interactive --parallel`. Job count defaults to `nproc` (Linux), `sysctl -n hw.ncpu` (macOS), or 4; override with `--作业s N`.", "**更快的运行（并行）** —— 在多核机器上，使用 `--parallel` 让每个工具并行处理。不同工具之间的输出顺序是不确定的。同时适用于交互式和非交互式安装：例如 `./scripts/install.sh --interactive --parallel`（先选择工具，再并行安装）或 `./scripts/install.sh --no-interactive --parallel`。作业数默认为 `nproc`（Linux）、`sysctl -n hw.ncpu`（macOS）或 4；可通过 `--作业s N` 覆盖。"))
repl.append(("# convert all tools in parallel", "# 并行转换所有工具"))
repl.append(("# cap parallel 作业s", "# 限制并行作业数"))
repl.append(("# install all detected tools in parallel", "# 并行安装所有检测到的工具"))
repl.append(("# pick tools, then install in parallel", "# 选择工具后并行安装"))

# === Tool-specific sections ===
repl.append(("Agents are copied directly from the repo into `~/.claude/agents/` -- no conversion needed.", "代理直接从仓库复制到 `~/.claude/agents/` —— 无需转换。"))
repl.append(("参见 [integrations/claude-code/README.md](integrations/claude-code/README.md) 了解更多详情.", "参见 [integrations/claude-code/README.md](integrations/claude-code/README.md) 了解更多详情。"))
repl.append(("Agents are copied directly from the repo into `~/.github/agents/` and `~/.copilot/agents/` -- no conversion needed.", "代理直接从仓库复制到 `~/.github/agents/` 和 `~/.copilot/agents/` —— 无需转换。"))
repl.append(("参见 [integrations/github-copilot/README.md](integrations/github-copilot/README.md) 了解更多详情.", "参见 [integrations/github-copilot/README.md](integrations/github-copilot/README.md) 了解更多详情。"))
repl.append(("Each agent becomes a skill in `~/.gemini/config/skills/agency-<slug>/`.", "每个代理会成为 `~/.gemini/config/skills/agency-<slug>/` 下的一个技能。"))
repl.append(("Activate in Gemini with Antigravity:", "在 Gemini 中通过 Antigravity 激活："))
repl.append(("参见 [integrations/antigravity/README.md](integrations/antigravity/README.md) 了解更多详情.", "参见 [integrations/antigravity/README.md](integrations/antigravity/README.md) 了解更多详情。"))
repl.append(("Installs as Gemini CLI subagents.", "安装为 Gemini CLI 子代理。"))
repl.append(("On a fresh clone, generate the Gemini agent files before 运行ning the installer.", "在全新克隆后，运行安装器之前先生成 Gemini 代理文件。"))
repl.append(("参见 [integrations/gemini-cli/README.md](integrations/gemini-cli/README.md) 了解更多详情.", "参见 [integrations/gemini-cli/README.md](integrations/gemini-cli/README.md) 了解更多详情。"))
repl.append(("Agents are placed in `.opencode/agents/` in your project root (project-scoped).", "代理放在项目根目录的 `.opencode/agents/` 中（项目级作用域）。"))
repl.append(("Or install globally:", "或者全局安装："))
repl.append(("Activate in OpenCode:", "在 OpenCode 中激活："))
repl.append(("参见 [integrations/opencode/README.md](integrations/opencode/README.md) 了解更多详情.", "参见 [integrations/opencode/README.md](integrations/opencode/README.md) 了解更多详情。"))
repl.append(("Each agent becomes a `.mdc` rule 文件在 `.cursor/rules/` of your project.", "每个代理会成为项目 `.cursor/rules/` 下的一个 `.mdc` 规则文件。"))
repl.append(("Rules are auto-applied when Cursor detects them in the project. Reference them explicitly:", "当 Cursor 在项目中发现这些规则时会自动应用。也可以显式引用："))
repl.append(("参见 [integrations/cursor/README.md](integrations/cursor/README.md) 了解更多详情.", "参见 [integrations/cursor/README.md](integrations/cursor/README.md) 了解更多详情。"))
repl.append(("All agents are compiled into a single `CONVENTIONS.md` Aider 自动读取的文件.", "所有代理被编译为一个 `CONVENTIONS.md` 文件，Aider 会自动读取。"))
repl.append(("Then reference agents in your Aider session:", "然后在你的 Aider 会话中引用代理："))
repl.append(("参见 [integrations/aider/README.md](integrations/aider/README.md) 了解更多详情.", "参见 [integrations/aider/README.md](integrations/aider/README.md) 了解更多详情。"))
repl.append(("All agents are compiled into `.windsurfrules` in your project root.", "所有代理被编译为项目根目录下的 `.windsurfrules`。"))
repl.append(("Reference agents in Windsurf's Cascade:", "在 Windsurf 的 Cascade 中引用代理："))
repl.append(("参见 [integrations/windsurf/README.md](integrations/windsurf/README.md) 了解更多详情.", "参见 [integrations/windsurf/README.md](integrations/windsurf/README.md) 了解更多详情。"))
repl.append(("Each agent becomes a workspace with `SOUL.md`, `AGENTS.md`, and `IDENTITY.md` in `~/.openclaw/agency-agents/`.", "每个代理会成为 `~/.openclaw/agency-agents/` 下的一个工作区，包含 `SOUL.md`、`AGENTS.md` 和 `IDENTITY.md`。"))
repl.append(("If the `openclaw` CLI is available, the installer registers each workspace automatically.", "如果 `openclaw` CLI 可用，安装器会自动注册每个工作区。"))
repl.append(("Run `openclaw gateway restart` after installation so the new agents are activated.", "安装后运行 `openclaw gateway restart`，使新代理生效。"))
repl.append(("参见 [integrations/openclaw/README.md](integrations/openclaw/README.md) 了解更多详情.", "参见 [integrations/openclaw/README.md](integrations/openclaw/README.md) 了解更多详情。"))
repl.append(("Sub代理安装到 `.qwen/agents/` in your project root (project-scoped).", "子代理安装到项目根目录的 `.qwen/agents/` 中（项目级作用域）。"))
repl.append(("# Convert and install (运行 from your project root)", "# 转换并安装（在项目根目录下运行）"))
repl.append(("**Usage in Qwen Code:**", "**在 Qwen Code 中的使用方式：**"))
repl.append(("- Reference by name: `使用 frontend-developer 代理来 审查这个组件`", "- 按名称引用：`使用 frontend-developer 代理来审查这个组件`"))
repl.append(("- Or let Qwen auto-delegate based on task context", "- 或者让 Qwen 根据任务上下文自动委派"))
repl.append(("- Manage via `/agents` command in interactive mode", "- 在交互模式下通过 `/agents` 命令管理"))
repl.append(("Agents are converted to Kimi Code CLI format (YAML + system prompt) and 安装到 `~/.config/kimi/agents/`.", "代理被转换为 Kimi Code CLI 格式（YAML + 系统提示），并安装到 `~/.config/kimi/agents/`。"))
repl.append(("# Convert and install", "# 转换并安装"))
repl.append(("**Usage with Kimi Code:**", "**配合 Kimi Code 使用：**"))
repl.append(("# Use an agent", "# 使用一个代理"))
repl.append(("# In a project", "# 在项目中"))
repl.append(("参见 [integrations/kimi/README.md](integrations/kimi/README.md) 了解更多详情.", "参见 [integrations/kimi/README.md](integrations/kimi/README.md) 了解更多详情。"))
repl.append(("每个代理都是 converted into a Codex custom agent TOML 文件 and 安装到 `~/.codex/agents/`.", "每个代理被转换为 Codex 自定义代理 TOML 文件，并安装到 `~/.codex/agents/`。"))
repl.append(("Then reference the custom agent by name in Codex:", "然后在 Codex 中按名称引用自定义代理："))
repl.append(("参见 [integrations/codex/README.md](integrations/codex/README.md) 了解更多详情.", "参见 [integrations/codex/README.md](integrations/codex/README.md) 了解更多详情。"))

# === Re-generate ===
repl.append(("### Re生成 After Changes", "### 变更后的重新生成"))
repl.append(("When you add new agents or edit existing ones, 重新生成所有 integration files:", "当你添加新代理或编辑现有代理时，重新生成所有集成文件："))
repl.append(("# 重新生成所有 (serial)", "# 重新生成所有（串行）"))
repl.append(("# 重新生成所有 in parallel (faster)", "# 重新生成所有（并行，更快）"))
repl.append(("# 只重新生成一个工具", "# 只重新生成一个工具"))

# === Roadmap ===
repl.append(("- [ ] Agent \"personality quiz\" for project matching", "- [ ] 项目匹配的代理\"性格测试\""))
repl.append(("- [ ] \"Agent of the Week\" showcase series", "- [ ] \"每周代理\"展示系列"))

# === Acknowledgments ===
repl.append(("What started as a Reddit thread about 人工智能 agent specialization 已经成长为一些非凡的东西 — **230+ agents across every division**, 由来自世界各地的贡献者社区支持. 这个仓库中的每个代理之所以存在，是因为有人足够关心 来编写它、测试它并分享它.", "从一个关于 AI 代理专业化的 Reddit 帖子开始，已经成长为一些非凡的东西——**覆盖所有团队的 230+ 代理**，由来自世界各地的贡献者社区支持。这个仓库中的每个代理之所以存在，是因为有人足够关心，来编写它、测试它并分享它。"))
repl.append(("向每一个打开 PR 的人, 提交 issue, 开始讨论, 或只是尝试了一个代理并告诉我们什么有效 — 谢谢你. You're the reason The Agency keeps getting better.", "向每一个提交 PR、发起 issue、开始讨论，或只是尝试了一个代理并告诉我们什么有效的人——谢谢。你们就是 The Agency 不断进步的原因。"))

# === Community ===
repl.append(("- **Reddit**: Join the conversation on r/Claude人工智能", "- **Reddit**：加入 r/Claude人工智能 上的讨论"))
repl.append(("- **Twitter/X**: 使用 #TheAgency 分享", "- **Twitter/X**：使用 #TheAgency 标签分享"))

# === Getting Started ===
repl.append(("1. **Browse** the agents above and find specialists for your needs", "1. **浏览**上方的代理，找到符合你需求的专家"))
repl.append(("3. **Activate** agents by referencing them in your Claude conversations", "3. **激活**代理——在你的 Claude 对话中引用它们"))
repl.append(("5. **Share** your results and contribute back to the community", "5. **分享**你的成果并回馈社区"))

# === Footer ===
repl.append(("**🎭 The Agency: Your 人工智能 Dream Team Awaits 🎭**", "**🎭 The Agency：你的 AI 梦想团队已就位 🎭**"))
repl.append(("[⭐ Star this repo](https://github.com/msitarzewski/agency-agents) • [🍴 Fork it](https://github.com/msitarzewski/agency-agents/fork) • [🐛 Report an issue](https://github.com/msitarzewski/agency-agents/issues) • [❤️ Sponsor](https://github.com/sponsors/msitarzewski)", "[⭐ 给仓库加星](https://github.com/msitarzewski/agency-agents) • [🍴 分叉它](https://github.com/msitarzewski/agency-agents/fork) • [🐛 报告问题](https://github.com/msitarzewski/agency-agents/issues) • [❤️ 赞助](https://github.com/sponsors/msitarzewski)"))
repl.append(("Made with ❤️ by the community, for the community", "由社区 ❤️ 打造，为社区服务"))

# === Translation Table Notes ===
repl.append(("141 translated agents + 46 China-market originals", "141 个已翻译代理 + 46 个中国市场原创"))
repl.append(("Independent translation with Bilibili, WeChat, Xiaohongshu localization", "独立翻译，包含 B站、微信、小红书本地化"))
repl.append(("184 upstream agents translated; Brazil-market PRs welcome", "184 个上游代理已翻译；欢迎巴西市场 PR"))
repl.append(("184 upstream agents translated; Russia-market PRs welcome", "184 个上游代理已翻译；欢迎俄罗斯市场 PR"))
repl.append(("184 upstream agents translated; Indonesia-market PRs welcome", "184 个上游代理已翻译；欢迎印度尼西亚市场 PR"))
repl.append(("184 upstream agents translated; Arabic-market PRs welcome", "184 个上游代理已翻译；欢迎阿拉伯市场 PR"))
repl.append(("184 upstream agents fully translated; Korea-specific PRs welcome", "184 个上游代理全部翻译；欢迎韩国特色 PR"))
repl.append(("281 Japan-localized agents + 97 Japan-market originals + 27 工作流程", "281 个日本本地化代理 + 97 个日本市场原创 + 27 个工作流程"))
repl.append(("Starter Vietnamese localization focused on README, quick start, and high-use docs", "越南语本地化起步版，聚焦 README、快速开始和高频使用文档"))
repl.append(("想添加翻译？ Open an issue and we'll link it here.", "想添加翻译？提交一个 issue，我们会在此处添加链接。"))

# === Related Resources ===
repl.append(("- [awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) — Community-maintained OpenClaw agent collection (derived from this repo)", "- [awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) —— 社区维护的 OpenClaw 代理集合（源自本仓库）"))

# === Agent Table Translations ===
repl.append(("| 🎨 [Frontend Developer](engineering/engineering-frontend-developer.md) | React/Vue/Angular, UI implementation, performance | Modern web apps, pixel-perfect UIs, Core Web Vitals optimization |", "| 🎨 [前端开发者](engineering/engineering-frontend-developer.md) | React/Vue/Angular、UI 实现、性能优化 | 现代 Web 应用、像素级完美 UI、Core Web Vitals 优化 |"))
repl.append(("| 🏗️ [Backend Architect](engineering/engineering-backend-architect.md) | API design, database architecture, scalability | Server-side systems, 微服务, cloud infrastructure |", "| 🏗️ [后端架构师](engineering/engineering-backend-architect.md) | API 设计、数据库架构、可扩展性 | 服务器端系统、微服务、云基础设施 |"))
repl.append(("| 📱 [Mobile App Builder](engineering/engineering-mobile-app-builder.md) | iOS/Android, React Native, Flutter | Native and cross-platform mobile applications |", "| 📱 [移动应用构建师](engineering/engineering-mobile-app-builder.md) | iOS/Android、React Native、Flutter | 原生和跨平台移动应用 |"))
repl.append(("| 🤖 [人工智能 Engineer](engineering/engineering-ai-engineer.md) | ML models, 部署, 人工智能 integration | Machine learning features, 数据管道, 人工智能 驱动的 apps |", "| 🤖 [AI 工程师](engineering/engineering-ai-engineer.md) | ML 模型、部署、AI 集成 | 机器学习功能、数据管道、AI 驱动的应用 |"))
repl.append(("| 🚀 [DevOps Automator](engineering/engineering-devops-automator.md) | 持续集成/持续部署, infrastructure automation, cloud ops | Pipeline development, 部署 automation, 监控 |", "| 🚀 [DevOps 自动化师](engineering/engineering-devops-automator.md) | 持续集成/持续部署、基础设施自动化、云运维 | 流水线开发、部署自动化、监控 |"))
repl.append(("| 🌐 [Network Engineer](engineering/engineering-network-engineer.md) | Cisco IOS/IOS-XE, Juniper Junos, Palo Alto PAN-OS | Router/switch/firewall configuration, BGP/OSPF, ACLs, show-output troubleshooting |", "| 🌐 [网络工程师](engineering/engineering-network-engineer.md) | Cisco IOS/IOS-XE、Juniper Junos、Palo Alto PAN-OS | 路由器/交换机/防火墙配置、BGP/OSPF、ACLs、show-output 排障 |"))
repl.append(("| ⚡ [Rapid Prototyper](engineering/engineering-rapid-prototyper.md) | Fast POC development, MVPs | Quick proof-of-concepts, hackathon projects, fast iteration |", "| ⚡ [快速原型师](engineering/engineering-rapid-prototyper.md) | 快速 POC 开发、MVP | 快速概念验证、黑客马拉松项目、快速迭代 |"))
repl.append(("| 💎 [Senior Developer](engineering/engineering-senior-developer.md) | Laravel/Livewire, advanced patterns | Complex implementations, architecture decisions |", "| 💎 [高级开发者](engineering/engineering-senior-developer.md) | Laravel/Livewire、高级模式 | 复杂实现、架构决策 |"))
repl.append(("| 🎯 [界面设计r](design/design-ui-designer.md) | Visual design, component libraries, design systems | Interface creation, brand consistency, component design |", "| 🎯 [UI 设计师](design/design-ui-designer.md) | 视觉设计、组件库、设计系统 | 界面创建、品牌一致性、组件设计 |"))
repl.append(("| 🏛️ [UX Architect](design/design-ux-architect.md) | 技术架构, CSS systems, implementation | Developer-friendly foundations, implementation guidance |", "| 🏛️ [UX 架构师](design/design-ux-architect.md) | 信息架构、CSS 系统、实现 | 开发者友好的基础、实现指导 |"))
repl.append(("| 💰 [PPC Campaign Strategist](paid-media/paid-media-ppc-strategist.md) | Google/Microsoft/Amazon Ads, account architecture, bidding | Account buildouts, budget allocation, 扩展, performance diagnosis |", "| 💰 [PPC 广告战略师](paid-media/paid-media-ppc-strategist.md) | Google/Microsoft/Amazon 广告、账户架构、竞价策略 | 账户搭建、预算分配、扩量、绩效诊断 |"))
repl.append(("| 🔍 [Search Query Analyst](paid-media/paid-media-search-query-analyst.md) | Search term analysis, negative keywords, intent mapping | Query audits, wasted spend elimination, keyword discovery |", "| 🔍 [搜索查询分析师](paid-media/paid-media-search-query-analyst.md) | 搜索词分析、否定关键词、意图映射 | 查询审计、消除浪费支出、关键词发现 |"))
repl.append(("| 🎯 [Outbound Strategist](sales/sales-outbound-strategist.md) | Signal-based prospecting, multi-channel sequences, ICP targeting | Building pipeline through research-driven outreach, not volume |", "| 🎯 [外联战略师](sales/sales-outbound-strategist.md) | 信号驱动的潜在客户开发、多渠道序列、ICP 定位 | 通过研究驱动的外联构建销售管道，而非堆量 |"))
repl.append(("| 🩺 [Clinical Evidence Agent](healthcare/healthcare-clinical-evidence-agent.md) | Evidence standards, validated vs unvalidated claims, diagnostic authority boundaries | Making clinical claims credibly without overstepping into diagnostic authority |", "| 🩺 [临床证据代理](healthcare/healthcare-clinical-evidence-agent.md) | 证据标准、已验证与未验证声明、诊断权限边界 | 在不越界进入诊断权限的前提下，可信地做出临床声明 |"))
repl.append(("| 🌍 [Sovereign Health Systems Agent](healthcare/healthcare-sovereign-health-systems-agent.md) | Government health mandates, UHC policy, emerging market 部署 | Health tech teams operating at the intersection of national health infrastructure and sovereign health policy |", "| 🌍 [主权健康体系代理](healthcare/healthcare-sovereign-health-systems-agent.md) | 政府健康指令、全民健康覆盖政策、新兴市场部署 | 在国家健康基础设施与主权健康政策交叉点运作的健康科技团队 |"))
repl.append(("| 🧭 [Healthcare Innovation Strategist](healthcare/healthcare-innovation-strategist.md) | Narrative architecture for healthcare founders across investor, regulatory, sovereign, and clinical audiences | Healthcare founders who need to translate clinical and financial complexity into language that moves capital and builds trust |", "| 🧭 [医疗创新战略师](healthcare/healthcare-innovation-strategist.md) | 面向投资人、监管机构、主权机构和临床受众的医疗创业者叙事架构 | 需要将临床和财务复杂性转化为能推动资本和建立信任的语言的医疗创业者 |"))

# === GIS Table ===
repl.append(("| 🧠 [Technical Consultant](gis/gis-technical-consultant.md) | GIS consulting, architecture planning, strategy | 咨询, 战略, 规划", "| 🧠 [技术咨询师](gis/gis-technical-consultant.md) | GIS 咨询、架构规划、战略 | 咨询、战略、规划"))
repl.append(("| 🔧 [GeoProcessing Specialist](gis/gis-geoprocessing-specialist.md) | ArcPy, Python Toolbox (.pyt), Model Builder, batch automation | Automating repetitive GIS 工作流程, 构建 custom geoprocessing tools |", "| 🔧 [地理处理专家](gis/gis-geoprocessing-specialist.md) | ArcPy、Python Toolbox (.pyt)、Model Builder、批量自动化 | 自动化重复的 GIS 工作流程、构建自定义地理处理工具 |"))
repl.append(("| ✅ [GIS QA Engineer](gis/gis-qa-engineer.md) | Topology validation, metadata audit, CRS consistency, accuracy assessment | Quality gates before data publication, compliance verification, data integrity audits |", "| ✅ [GIS 质量工程师](gis/gis-qa-engineer.md) | 拓扑验证、元数据审计、CRS 一致性、精度评估 | 数据发布前的质量门禁、合规性验证、数据完整性审计 |"))
repl.append(("| 🤖 [Geo人工智能/ML Engineer](gis/gis-geoai-ml-engineer.md) | Feature extraction, object detection, semantic segmentation, land cover classification | Extracting 构建s/roads/vehicles from imagery, change detection, environmental 监控 |", "| 🤖 [GeoAI/ML 工程师](gis/gis-geoai-ml-engineer.md) | 特征提取、目标检测、语义分割、土地覆盖分类 | 从影像中提取建筑物/道路/车辆、变化检测、环境监测 |"))
repl.append(("| 🏗️ [BIM/GIS Specialist](gis/gis-bim-specialist.md) | Revit/IFC to GIS, indoor mapping, digital twin architecture, facility management | Smart campus, airport digital twins, indoor navigation, 构建 operations |", "| 🏗️ [BIM/GIS 专家](gis/gis-bim-specialist.md) | Revit/IFC 转 GIS、室内制图、数字孪生架构、设施管理 | 智慧校园、机场数字孪生、室内导航、建筑运营 |"))
repl.append(("| 🏔️ [3D & Scene Developer](gis/gis-3d-scene-developer.md) | Cesium, ArcGIS Scene Viewer, 3D Tiles, point clouds, terrain visualization | 3D city scenes, terrain flyovers, point cloud web viewers, OAuth-gated scene sharing |", "| 🏔️ [3D 与场景开发者](gis/gis-3d-scene-developer.md) | Cesium、ArcGIS Scene Viewer、3D Tiles、点云、地形可视化 | 3D 城市场景、地形飞越、点云 Web 查看器、OAuth 门禁场景共享 |"))
repl.append(("| 📊 [Spatial Data Scientist](gis/gis-spatial-data-scientist.md) | Spatial statistics, clustering, r出口ion, interpolation, point pattern analysis | Hotspot detection, spatial modeling, predictive analytics, research-grade analysis |", "| 📊 [空间数据科学家](gis/gis-spatial-data-scientist.md) | 空间统计、聚类、回归、插值、点模式分析 | 热点检测、空间建模、预测分析、研究级分析 |"))
repl.append(("| 🛸 [Drone/Reality Mapping](gis/gis-drone-reality-mapping.md) | Photogrammetry, orthomosaic, DTM/DSM, point cloud classification, 3D mesh | Drone survey processing, reality capture, construction 监控, environmental mapping |", "| 🛸 [无人机/实景测绘师](gis/gis-drone-reality-mapping.md) | 摄影测量、正射镶嵌、DTM/DSM、点云分类、3D 网格 | 无人机航测处理、实景捕捉、施工监控、环境制图 |"))
repl.append(("| 🌐 [Web GIS Developer](gis/gis-web-gis-developer.md) | MapLibre GL JS, ArcGIS JS API, Leaflet, real-time dashboards, REST APIs | Building interactive web maps, operational dashboards, real-time data visualization |", "| 🌐 [Web GIS 开发者](gis/gis-web-gis-developer.md) | MapLibre GL JS、ArcGIS JS API、Leaflet、实时仪表盘、REST API | 构建交互式 Web 地图、运营仪表盘、实时数据可视化 |"))
repl.append(("| 🎨 [Cartography Designer](gis/gis-cartography-designer.md) | Color theory, typography, basemap design, visual hierarchy, print and web aesthetics | Making maps beautiful and readable, colorblind-safe palettes, professional map layouts |", "| 🎨 [制图设计师](gis/gis-cartography-designer.md) | 色彩理论、排版、底图设计、视觉层次、印刷与 Web 美学 | 让地图美观易读、色盲安全配色方案、专业地图布局 |"))

# === Workflow Scenario Details ===
repl.append(("1. 🎨 **Frontend Developer** - Build the React app", "1. 🎨 **前端开发者** —— 构建 React 应用"))
repl.append(("2. 🏗️ **Backend Architect** - Design the API and database", "2. 🏗️ **后端架构师** —— 设计 API 和数据库"))
repl.append(("3. 🚀 **增长 Hacker** - Plan user acquisition", "3. 🚀 **增长黑客** —— 规划用户获取"))
repl.append(("4. ⚡ **Rapid Prototyper** - Fast iteration cycles", "4. ⚡ **快速原型师** —— 快速迭代周期"))
repl.append(("5. 🔍 **Reality Checker** - Ensure quality before launch", "5. 🔍 **现实检查师** —— 上线前确保质量"))
repl.append(("1. 📝 **Content Creator** - Develop campaign content", "1. 📝 **内容创作者** —— 制作活动内容"))
repl.append(("2. 🐦 **Twitter Engager** - Twitter strategy and execution", "2. 🐦 **Twitter 互动师** —— Twitter 策略与执行"))
repl.append(("3. 📸 **Instagram Curator** - Visual content and stories", "3. 📸 **Instagram 策划师** —— 视觉内容和故事"))
repl.append(("4. 🤝 **Reddit Community Builder** - Authentic community engagement", "4. 🤝 **Reddit 社群建设师** —— 真实的社群互动"))
repl.append(("5. 📊 **Analytics Reporter** - Track and optimize performance", "5. 📊 **数据分析报告师** —— 追踪和优化绩效"))

# === Smart Campus Details ===
repl.append(("1. 🧠 **Technical Consultant** - Define the digital twin strategy: BIM for 构建s, GIS for campus, IoT for real-time", "1. 🧠 **技术咨询师** —— 定义数字孪生战略：BIM 用于建筑、GIS 用于校园、IoT 用于实时"))
repl.append(("2. 🏗️ **BIM/GIS Specialist** - Convert Revit 构建 models to GIS scene layers, design indoor floor plans", "2. 🏗️ **BIM/GIS 专家** —— 将 Revit 建筑模型转换为 GIS 场景图层，设计室内平面图"))
repl.append(("3. 🛸 **Drone/Reality Mapping** - Fly the campus, generate orthomosaic and 3D mesh for context", "3. 🛸 **无人机/实景测绘师** —— 飞越校园，生成正射镶嵌和 3D 网格作为背景"))
repl.append(("4. 🌐 **Web GIS Developer** - Build the campus dashboard with MapLibre, 构建 layer, and room finder", "4. 🌐 **Web GIS 开发者** —— 使用 MapLibre 构建校园仪表盘，包含建筑图层和房间查找器"))
repl.append(("5. 🏔️ **3D & Scene Developer** - Create immersive 3D scene with terrain, 构建s, and flyover tour", "5. 🏔️ **3D 与场景开发者** —— 创建包含地形、建筑和飞越导览的沉浸式 3D 场景"))
repl.append(("6. 🤖 **Geo人工智能/ML Engineer** - Extract 构建 footprints and tree canopy from drone imagery", "6. 🤖 **GeoAI/ML 工程师** —— 从无人机影像中提取建筑轮廓和树冠"))
repl.append(("7. ✅ **GIS QA Engineer** - Validate data accuracy, check topology, verify CRS consistency", "7. ✅ **GIS 质量工程师** —— 验证数据准确性、检查拓扑、验证 CRS 一致性"))

# Apply all replacements
count = 0
missing = []
for old, new in repl:
    if old in text:
        text = text.replace(old, new)
        count += 1
    else:
        missing.append(old[:60])

with open(path, "w", encoding="utf-8") as f:
    f.write(text)

print(f"Done. Applied {count} replacements.")
if missing:
    print(f"{len(missing)} replacements did not match:")
    for m in missing:
        print(f"  - {m}")
