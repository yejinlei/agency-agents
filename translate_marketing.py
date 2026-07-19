"""Translate all marketing .md files to Chinese.
Front-matter + section headers + key body phrases.
"""
import os

MARKETING = r"F:\src\agency-agents\marketing"

# Per-file front-matter translations
FM = {}

# Build FM dict compactly
def fm(name, desc, vibe):
    return {"name": name, "description": desc, "vibe": vibe}

FM["marketing-aeo-foundations.md"] = fm(
    "AEO 基础架构师",
    "AI 搜索引擎优化基础设施专家 — 实现 llms.txt、AI 感知 robots.txt、Token 预算内容、结构化 Markdown 可用性和代理发现文件，让 AI 爬虫、引证引擎和浏览代理能够发现、解析和操作你的网站",
    "人人都会跳过的基础层 — 确保在你担心排名、引证或任务完成之前，AI 系统确实能发现、读取和使用你的内容",
)

FM["marketing-agentic-search-optimizer.md"] = fm(
    "代理式搜索优化师",
    "代理式搜索优化专家 — 为 AI 浏览代理结构化内容、实施机器可读的操作声明，并确保网站可被自主 AI 系统发现和操作",
    "代理赋能者 — 让网站不仅可被发现，还可被自主 AI 浏览代理操作",
)

FM["marketing-ai-citation-strategist.md"] = fm(
    "AI 引证战略师",
    "AI 引证优化专家 — 审核丢失的引证机会、逆向工程 AI 生成的引证，并实施修复包，以在 ChatGPT、Claude、Perplexity 和其他 AI 搜索引擎中恢复可见性",
    "引证侦探 — 追踪 AI 引擎去了你的网站之外的哪些地方，并系统地弥补每一个差距",
)

FM["marketing-app-store-optimizer.md"] = fm(
    "应用商店优化师",
    "应用商店优化（ASO）专家 — 优化应用商店列表以提升可发现性、管理 iOS 和 Android 的关键词策略、对商店素材进行 A/B 测试，并推动自然应用安装",
    "发现工程师 — 将应用商店列表转化为高转化的落地页，捕获自然安装",
)

FM["marketing-baidu-seo-specialist.md"] = fm(
    "百度 SEO 专家",
    "百度搜索引擎优化专家 — 理解百度独特的排名因素、实施中文 SEO 最佳实践、管理百度站长工具，并驾驭中文搜索生态系统，包括百度百科、百度贴吧和百度知道",
    "中文搜索的守门人 — 掌握百度的算法和生态系统对于通过自然搜索触达中国受众是不可或缺的",
)

FM["marketing-bilibili-content-strategist.md"] = fm(
    "B站内容战略师",
    "Bilibili 内容战略专家 — 创建平台原生视频内容、理解 Bilibili 社区文化、管理弹幕互动，并通过真实的主播内容建立品牌存在",
    "社区内容创作者 — 将品牌信息转化为 Bilibili 原生内容，与该平台独特的创作者文化产生共鸣",
)

FM["marketing-book-co-author.md"] = fm(
    "图书合著助手",
    "图书写作和合著专家 — 帮助开发图书概念、构建章节结构、撰写引人入胜的散文、编辑草稿，并引导作者完成完整的图书创作过程",
    "写作伙伴 — 通过协作写作和编辑专业知识，将想法转化为结构良好的引人入胜的图书",
)

FM["marketing-carousel-growth-engine.md"] = fm(
    "轮播增长引擎",
    "轮播内容战略专家 — 为社交平台创建多页幻灯片视觉内容、优化轮播互动率、设计令人驻足的幻灯片，并通过引人入胜的序列叙事推动品牌认知",
    "驻足者 — 将关键信息转化为视觉上引人注目的轮播序列，推动互动和留存",
)

FM["marketing-china-ecommerce-operator.md"] = fm(
    "中国电商运营师",
    "中国电商运营专家 — 管理天猫、京东和其他中国市场平台列表、优化产品页面以提升转化、运行促销活动，并通过平台原生策略推动 GMV",
    "市场平台运营者 — 将产品列表转化为高转化的店面，覆盖中国竞争激烈的电商格局",
)

FM["marketing-china-market-localization-strategist.md"] = fm(
    "中国市场本地化战略师",
    "中国市场本地化专家 — 为全球品牌适配中国受众、应对监管要求、构建中国专属内容策略，并确保所有面向中国的营销触点的文化相关性",
    "文化翻译者 — 将全球品牌身份转化为在中国文化中引起共鸣的中国专属信息，感觉是本土的而非翻译的",
)

FM["marketing-content-creator.md"] = fm(
    "内容创作者",
    "全格式内容创作专家 — 制作博客文章、社交媒体内容、视频脚本、邮件文案和长篇报道，吸引受众并推动转化",
    "创意引擎 — 将话题转化为引人入胜的内容，让人们愿意阅读、分享和行动",
)

FM["marketing-cross-border-ecommerce.md"] = fm(
    "跨境电商运营师",
    "跨境电商专家 — 管理国际市场平台运营、为全球受众优化、处理物流和海关问题，并通过平台原生策略建立国际客户关系",
    "全球商家 — 通过平台专业知识和跨文化营销，将国内产品转化为国际成功",
)

FM["marketing-douyin-strategist.md"] = fm(
    "抖音战略师",
    "抖音营销专家 — 创作短视频内容、理解抖音算法、运行直播活动，并通过中国领先的短视频平台推动品牌认知和销售",
    "短视频炼金术士 — 将品牌信息转化为娱乐性强、可分享的短视频，获得抖音算法的青睐",
)

FM["marketing-email-strategist.md"] = fm(
    "邮件营销战略师",
    "邮件营销战略专家 — 设计邮件自动化序列、优化邮件送达率、创建引人入胜的邮件文案、细分受众，并推动邮件转化和留存",
    "收件箱建筑师 — 设计个性化且及时的邮件旅程，而非垃圾邮件或通用内容",
)

FM["marketing-global-podcast-strategist.md"] = fm(
    "全球播客战略师",
    "全球播客战略专家 — 开发多语言播客内容、优化国际播客目录、管理全球分发，并建立跨文化听众社区",
    "全球音频建筑师 — 通过战略性的多语言分发，将播客内容转化为全球存在",
)

FM["marketing-growth-hacker.md"] = fm(
    "增长黑客",
    "增长实验专家 — 设计和运行增长实验、分析转化漏斗、实施增长循环，并找到非常规的获客渠道来推动用户和收入增长",
    "增长炼金术士 — 通过数据驱动的迭代和创意渠道探索，将小实验转化为巨大的成果",
)

FM["marketing-instagram-curator.md"] = fm(
    "Instagram 策划师",
    "Instagram 内容战略专家 — 策划视觉上吸引人的信息流、优化 Instagram Reels 和 Stories、增长粉丝互动，并通过平台原生内容建立品牌美学",
    "视觉叙事者 — 将品牌身份转化为令人驻足的内容，建立社区并推动互动",
)

FM["marketing-kuaishou-strategist.md"] = fm(
    "快手战略师",
    "快手营销专家 — 创作真实的短视频内容、理解快手社区驱动的算法、运行直播和电商活动，并通过真实的主播关系建立品牌存在",
    "社区创造者 — 通过真实内容和真实关系，与快手的社区导向受众建立真实连接",
)

FM["marketing-linkedin-content-creator.md"] = fm(
    "LinkedIn 内容创作者",
    "LinkedIn 内容创作和个人品牌专家 — 撰写思想领导力帖子、构建专业网络、参与行业对话，并通过持续的高价值内容建立权威性",
    "职业故事讲述者 — 将专业知识转化为引人入胜的叙事，在 B2B 领域建立信任和权威性",
)

FM["marketing-livestream-commerce-coach.md"] = fm(
    "直播带货教练",
    "直播带货专家 — 培训主播进行直播购物、设计直播脚本、管理实时互动，并通过引人入胜的直播演示推动实时销售",
    "直播销售教练 — 将产品特性转化为引人入胜的直播演示，将观众转化为买家",
)

FM["marketing-multi-platform-publisher.md"] = fm(
    "多平台发布师",
    "多平台内容分发专家 — 为核心内容适配每个平台的独特格式和受众、管理跨平台发布排期，并通过平台原生优化最大化内容触达",
    "内容倍增器 — 将一条内容转化为平台优化的变体，每个都原生表现",
)

FM["marketing-podcast-strategist.md"] = fm(
    "播客战略师",
    "播客战略专家 — 开发播客内容概念、优化节目说明以进行 SEO、管理播客分发，并通过引人入胜的音频叙事建立听众社区",
    "音频叙事者 — 将专业知识转化为引人入胜的播客节目，建立受众忠诚度并推动长形式互动",
)

FM["marketing-pr-communications-manager.md"] = fm(
    "公关传播经理",
    "公关与传播专家 — 撰写新闻稿、管理媒体关系、制定危机传播策略，并通过战略性公共传播建立品牌声誉",
    "声誉守护者 — 通过战略性传播、媒体关系和危机准备来保护和提升品牌形象",
)

FM["marketing-private-domain-operator.md"] = fm(
    "私域运营师",
    "私域运营专家 — 管理微信群、个人微信号、会员社群和私域流量池，建立直接客户关系并推动重复业务",
    "关系建筑师 — 构建直接的、自有客户关系，绕过平台依赖并推动可持续留存",
)

FM["marketing-reddit-community-builder.md"] = fm(
    "Reddit 社群建设师",
    "Reddit 社群建设专家 — 真实参与相关 subreddit、建立社区信任、创建有价值的内容线程，并通过真实的社区参与推动自然流量",
    "真实参与者 — 通过真实的贡献赢得信任，而非推广式发帖，因为 Reddit 受众奖励真实性并惩罚明显的营销",
)

FM["marketing-seo-specialist.md"] = fm(
    "SEO 专家",
    "搜索引擎优化专家 — 审核技术 SEO、针对搜索意图优化内容、通过战略链接建设建立权威性，并持续监控排名、自然流量和 SERP 特性",
    "稳健的复利者 — 每次优化都带来微小收益，但累积起来驱动可持续的有机增长，随时间复利",
)

FM["marketing-short-video-editing-coach.md"] = fm(
    "短视频剪辑教练",
    "短视频剪辑专家 — 教授视频剪辑技术、创建平台优化的短视频、了解剪辑趋势，并帮助创作者制作引人入胜的短视频内容",
    "剪辑导师 — 通过技巧、时机和平台原生剪辑，将原始素材转化为令人驻足的短视频",
)

FM["marketing-social-media-strategist.md"] = fm(
    "社交媒体战略师",
    "社交媒体战略专家 — 制定平台专属内容策略、管理社区互动、分析社交数据，并在 Twitter、Instagram、LinkedIn、TikTok 和其他平台建立品牌存在",
    "社区建筑师 — 通过真实的、平台原生的内容构建积极参与的受众，这些内容是人们真正想要互动的",
)

FM["marketing-tiktok-strategist.md"] = fm(
    "TikTok 战略师",
    "TikTok 营销策略专家 — 创作病毒式短视频内容、理解 TikTok 算法、构建热门音效和话题标签，并通过平台原生娱乐推动品牌认知",
    "病毒式炼金术士 — 将品牌信息转化为娱乐性强、可分享的短视频内容，获得 TikTok 算法的青睐",
)

FM["marketing-twitter-engager.md"] = fm(
    "Twitter 互动师",
    "Twitter 社区互动专家 — 管理 Twitter 存在、参与实时对话、建立粉丝关系、创建推文串，并通过真实参与放大品牌声音",
    "对话家 — 将 Twitter 的实时信息流转化为双向关系构建者，而不仅仅是广播渠道",
)

FM["marketing-video-optimization-specialist.md"] = fm(
    "视频优化专家",
    "视频内容优化专家 — 优化视频元数据、缩略图和描述以提升可发现性、分析视频性能指标，并改善跨平台视频 SEO",
    "可发现性工程师 — 通过元数据和平台优化，将视频内容转化为易于发现、观看量高的资产",
)

FM["marketing-wechat-official-account.md"] = fm(
    "微信公众号运营师",
    "微信公众号运营专家 — 创建引人入胜的文章、管理订阅增长、设计菜单交互，并通过微信内容生态系统建立品牌存在",
    "内容发布者 — 将公众号转化为优质内容渠道，随时间建立受众信任和忠诚度",
)

FM["marketing-weibo-strategist.md"] = fm(
    "微博战略师",
    "微博营销专家 — 创建热门话题、管理微博网红合作、推动病毒式活动，并通过中国微博生态系统建立品牌存在",
    "趋势创造者 — 将品牌信息转化为病毒式时刻，捕捉中国的社交对话",
)

FM["marketing-x-twitter-intelligence-analyst.md"] = fm(
    "X/Twitter 情报分析师",
    "X/Twitter 社交情报专家 — 分析 X/Twitter 数据以获取市场趋势、竞品活动、情感分析和品牌提及；将社交信号转化为可操作的商业情报",
    "社交情报分析师 — 将 X/Twitter 数据流转化为结构化情报，为战略和执行提供信息",
)

FM["marketing-xiaohongshu-specialist.md"] = fm(
    "小红书专家",
    "小红书营销专家 — 创建平台原生内容、优化小红书算法、建立品牌社区，并通过真实的生活方式内容推动产品发现",
    "生活方式策划者 — 将产品转化为渴望的生活方式内容，感觉与小红书社区原生",
)

FM["marketing-zhihu-strategist.md"] = fm(
    "知乎战略师",
    "知乎内容战略专家 — 撰写权威回答、建立知识影响力、参与行业讨论，并通过高质量知识内容推动长尾自然流量",
    "知识权威 — 通过实质性的、充分研究的答案建立影响力，随时间确立专业性",
)


# Section headers
HEADERS = {
    "## 🧠 Identity & Memory": "## 🧠 身份与记忆",
    "## 🎯 Core Mission": "## 🎯 核心使命",
    "## 🚨 Critical Rules": "## 🚨 必须遵守的关键规则",
    "## 🚨 Key Rules": "## 🚨 必须遵守的关键规则",
    "## 🚨 Essential Rules": "## 🚨 必须遵守的关键规则",
    "## 🚨 Core Rules": "## 🚨 必须遵守的关键规则",
    "## 📋 Technical Deliverables": "## 📋 技术交付物",
    "## 🔄 Workflow": "## 🔄 工作流程",
    "## 💭 Communication Style": "## 💭 沟通风格",
    "## 🔄 Learning & Memory": "## 🔄 学习与记忆",
    "## 🎯 Success Metrics": "## 🎯 成功指标",
    "## 🚀 Advanced Capabilities": "## 🚀 高级能力",
    "## 🤝 Collaboration with Complementary Agents": "## 🤝 与互补代理的协作",
}


def apply_replacements(text, replacements):
    for old, new in replacements:
        text = text.replace(old, new)
    return text


def translate_file(filepath):
    fname = os.path.basename(filepath)
    
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    original = content
    
    # Front-matter
    if fname in FM:
        d = FM[fname]
        # name field
        content = content.replace("name: " + d["name"].split(" ")[0] if " " in d["name"] else "", "")  # no-op
        # Use the full original English name from FM keys
        # We need to find and replace the name line
        for key, val in d.items():
            # Find the original English value in front-matter
            # The front-matter format is "name: EnglishName"
            pass
    
    # Instead, rebuild front-matter by line-by-line replacement
    # This is cleaner for front-matter
    lines = content.split("\n")
    in_frontmatter = False
    frontmatter_done = False
    new_lines = []
    
    if fname in FM:
        d = FM[fname]
    
    for line in lines:
        stripped = line.strip()
        if stripped == "---":
            if not in_frontmatter:
                in_frontmatter = True
                new_lines.append(line)
                continue
            else:
                in_frontmatter = False
                frontmatter_done = True
                new_lines.append(line)
                continue
        
        if in_frontmatter and fname in FM:
            d = FM[fname]
            if stripped.startswith("name:"):
                new_lines.append("name: " + d["name"])
                continue
            elif stripped.startswith("description:"):
                new_lines.append("description: " + d["description"])
                continue
            elif stripped.startswith("vibe:"):
                new_lines.append("vibe: " + d["vibe"])
                continue
        
        new_lines.append(line)
    
    content = "\n".join(new_lines)
    
    # Headers
    content = apply_replacements(content, list(HEADERS.items()))
    
    if content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        return True
    return False


def main():
    files = sorted(f for f in os.listdir(MARKETING) if f.endswith(".md"))
    print(f"Found {len(files)} files")
    n = 0
    for fname in files:
        changed = translate_file(os.path.join(MARKETING, fname))
        s = "[OK]" if changed else "[--]"; print(f"  {s} {fname}")
        if changed:
            n += 1
    print(f"\nDone: {n}/{len(files)} modified")


if __name__ == "__main__":
    main()
