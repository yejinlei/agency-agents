import sys

BASE = "F:/src/agency-agents/"

def t(path, replacements):
    with open(path, 'r', encoding='utf-8') as f:
        c = f.read()
    for old, new in replacements:
        c = c.replace(old, new, 1)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(c)
    print(f"  {path.split('/')[-1]}")

# paid-media-vibe only (frontmatter has no vibe key, only name+desc)
# Just do the body for all 7 paid-media files
files_pm = [
    "paid-media-auditor.md",
    "paid-media-creative-strategist.md",
    "paid-media-paid-social-strategist.md",
    "paid-media-ppc-strategist.md",
    "paid-media-programmatic-buyer.md",
    "paid-media-search-query-analyst.md",
    "paid-media-tracking-specialist.md",
]

for fn in files_pm:
    path = BASE + "paid-media/" + fn
    replacements = [
        ("# Paid Media 审计or Agent", "# 付费媒体审计师 Agent"),
        ("# Paid Media Creative Strategist Agent", "# 广告创意战略师 Agent"),
        ("# Paid Social Strategist Agent", "# 付费社交广告战略师 Agent"),
        ("# PPC Campaign Strategist Agent", "# PPC 广告战略师 Agent"),
        ("# Programmatic & Display Buyer Agent", "# 程序化与展示广告采购师 Agent"),
        ("# Search Query Analyst Agent", "# 搜索查询分析师 Agent"),
        ("# Tracking & Measurement Specialist Agent", "# 追踪与测量专家 Agent"),
        ("## Identity & 角色定义", "## 身份与角色定义"),
        ("## Core 能力", "## 核心能力"),
        ("## 核心能力", "## 核心能力"),
        ("## 专业技能", "## 专业技能"),
        ("## Tooling & 自动化", "## 工具与自动化"),
        ("## 决策框架", "## 决策框架"),
        ("## 成功指标", "## 成功指标"),
        ("## 你的身份与记忆", "## 你的身份与记忆"),
        ("## 你的核心使命", "## 你的核心使命"),
        ("## 你必须遵守的关键规则", "## 你必须遵守的关键规则"),
        ("## Your 交付物", "## 交付物"),
        ("## Your 工作流程", "## 工作流程"),
        ("## Your 沟通风格", "## 沟通风格"),
        ("## Your 成功指标", "## 成功指标"),
        ("## Your 学习", "## 学习"),
    ]
    t(path, replacements)

# product files
files_pd = [
    ("product-behavioral-nudge-engine.md", [
        ("# Behavioral Nudge Engine Agent", "# 行为助推引擎 Agent"),
    ]),
    ("product-feedback-synthesizer.md", [
        ("# Feedback Synthesizer Agent", "# 反馈综合器 Agent"),
    ]),
    ("product-manager.md", [
        ("# Product Manager Agent", "# 产品经理 Agent"),
    ]),
    ("product-sprint-prioritizer.md", [
        ("# Sprint Prioritizer Agent", "# 冲刺优先排序师 Agent"),
    ]),
    ("product-trend-researcher.md", [
        ("# Trend Researcher Agent", "# 趋势研究员 Agent"),
    ]),
]

for fn, repls in files_pd:
    path = BASE + "product/" + fn
    for old, new in repls:
        with open(path, 'r', encoding='utf-8') as f:
            c = f.read()
        c = c.replace(old, new, 1)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(c)
    print(f"  {fn}")

# project-management files
files_pm2 = [
    ("project-management-experiment-tracker.md", [
        ("# Experiment Tracker Agent", "# 实验追踪器 Agent"),
    ]),
    ("project-management-jira-workflow-steward.md", [
        ("# Jira Workflow Steward Agent", "# Jira 工作流管理员 Agent"),
    ]),
    ("project-management-meeting-notes-specialist.md", [
        ("# Meeting Notes Specialist Agent", "# 会议纪要专家 Agent"),
    ]),
    ("project-management-project-shepherd.md", [
        ("# Project Shepherd Agent", "# 项目牧羊人 Agent"),
    ]),
    ("project-management-studio-operations.md", [
        ("# Studio Operations Agent", "# 工作室运营师 Agent"),
    ]),
    ("project-management-studio-producer.md", [
        ("# Studio Producer Agent", "# 工作室制作人 Agent"),
    ]),
    ("project-manager-senior.md", [
        ("# Senior Project Manager Agent", "# 高级项目经理 Agent"),
    ]),
]

for fn, repls in files_pm2:
    path = BASE + "project-management/" + fn
    for old, new in repls:
        with open(path, 'r', encoding='utf-8') as f:
            c = f.read()
        c = c.replace(old, new, 1)
        with open(path, 'w', encoding='utf-8') as f:
            f.write(c)
    print(f"  {fn}")

print("All body headings done")
