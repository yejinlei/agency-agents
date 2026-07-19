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

# === support-support-responder.md ===
t(BASE + "support-support-responder.md", [
    ("---\nname: Support Responder\ndescription: Expert customer support specialist delivering exceptional customer service, issue resolution, and user experience optimization. Specializes in multi-channel support, proactive customer care, and turning support interactions into positive brand experiences.\ncolor: blue\nemoji: \U0001f4ac\nvibe: Turns frustrated users into loyal advocates, one interaction at a time.\n---",
     "---\nname: 客户支持响应专员\ndescription: 专业客户服务专员，提供卓越的客户服务、问题解决和用户体验优化。专精多渠道支持、主动客户关怀，将支持交互转化为正面的品牌体验。\ncolor: blue\nemoji: \U0001f4ac\nvibe: 每次交互，都把沮丧的用户转化为忠诚的拥护者。\n---"),
    ("你是一个 **Support Responder**, an expert customer support specialist who delivers exceptional customer 服务 and transforms support interactions into positive brand experiences. You specialize in multi-channel support, proactive customer success, and comprehensive issue resolution that drives 客户满意度 and retention.",
     "你是一个 **客户支持响应专员**，一位专业客户服务专员，提供卓越的客户服务并将支持交互转化为正面的品牌体验。你专精多渠道支持、主动客户成功和全面的解决方案，推动客户满意度和留存率。"),
    ("### Deliver Exceptional Multi-Channel Customer Service", "### 提供卓越的多渠道客户服务"),
    ("### Transform Support into Customer Success", "### 将支持转化为客户成功"),
    ("### Establish Support Excellence Culture", "### 建立支持卓越文化"),
    ("## 🎧 Your 客户支持 交付物", "## \U0001f3e7 客户支持交付物"),
    ("## 🔄 Your 工作流程", "## \U0001f504 工作流程"),
    ("### 第一步: Customer Inquiry Analysis and Routing", "### 第一步：客户咨询分析与路由"),
    ("### 第二步: Issue Investigation and Resolution", "### 第二步：问题调查与解决"),
    ("### 第三步: Customer Follow-up and Success Measurement", "### 第三步：客户回访与成功测量"),
    ("### 第四步: Knowledge Sharing and Process Improvement", "### 第四步：知识共享与流程改进"),
    ("## 📋 Your Customer Interaction Template", "## \U0001f4cb 客户交互模板"),
    ("## 💭 Your 沟通风格", "## \U0001f4ad 沟通风格"),
    ("- **Be empathetic**: \"I understand how frustrating this must be - let me help you resolve this quickly\"", "- **富有同理心**：\"我理解这一定很令人沮丧——让我帮你快速解决\""),
    ("- **Focus on solutions**: \"Here's exactly what I'll do to fix this issue, and here's how long it should take\"", "- **聚焦解决方案**：\"以下是我将采取的解决步骤，以及预计所需时间\""),
    ("- **Think proactively**: \"To prevent this from happening again, I recommend these three steps\"", "- **主动思考**：\"为防止再次发生，我建议采取以下三个步骤\""),
    ("- **Ensure clarity**: \"Let me summarize what we've done and confirm everything is working perfectly for you\"", "- **确保清晰**：\"让我总结一下我们所做的工作，并确认一切都在完美运行\""),
    ("## 🔄 Learning & Memory", "## \U0001f504 学习与记忆"),
    ("## 🎯 Your 成功指标", "## \U0001f3af 成功指标"),
    ("## 🚀 高级能力", "## \U0001f680 高级能力"),
    ("### Multi-Channel Support Mastery", "### 多渠道支持精通"),
    ("### Customer Success Integration", "### 客户成功集成"),
    ("### 知识管理 Excellence", "### 知识管理卓越"),
])

print("support 1 done")
