"""Translate all marketing .md files to Chinese — clean version.
Reads originals from git HEAD, applies front-matter + header translations,
writes translated files. No destructive pattern matching.
"""
import subprocess
import os

MARKETING = r"F:\src\agency-agents\marketing"

# Build FM dict from tuples
fm_tuples = [
    ("marketing-aeo-foundations.md",
     "name: AEO Foundations Architect", "name: AEO 基础架构师",
     "description: Expert in AI Engine Optimization infrastructure — implements llms.txt, AI-aware robots.txt, token-budgeted content, structured Markdown availability, and agent discovery files so AI crawlers, citation engines, and browsing agents can find, parse, and act on your site",
     "description: AI 搜索引擎优化基础设施专家 — 实现 llms.txt、AI 感知 robots.txt、Token 预算内容、结构化 Markdown 可用性和代理发现文件，让 AI 爬虫、引证引擎和浏览代理能够发现、解析和操作你的网站",
     "vibe: The foundation layer everyone skips — making sure AI systems can actually discover, read, and use your content before you worry about rankings, citations, or task completion",
     "vibe: 人人都会跳过的基础层 — 确保在你担心排名、引证或任务完成之前，AI 系统确实能发现、读取和使用你的内容"),
    ("marketing-agentic-search-optimizer.md",
     "name: Agentic Search Optimizer", "name: 代理式搜索优化师",
     "description: Expert in optimizing websites for agentic search — structures content for AI browsing agents, implements machine-readable action declarations, and ensures sites are discoverable and actionable by autonomous AI systems",
     "description: 代理式搜索优化专家 — 为 AI 浏览代理结构化内容、实施机器可读的操作声明，并确保网站可被自主 AI 系统发现和操作",
     "vibe: The agent enabler — making websites not just findable but actionable for autonomous AI browsing agents",
     "vibe: 代理赋能者 — 让网站不仅可被发现，还可被自主 AI 浏览代理操作"),
    ("marketing-ai-citation-strategist.md",
     "name: AI Citation Strategist", "name: AI 引证战略师",
     "description: Expert in optimizing websites for AI citation — audits lost citation opportunities, reverse-engineers AI-generated citations, and implements fix packs to reclaim visibility in ChatGPT, Claude, Perplexity, and other AI search engines",
     "description: AI 引证优化专家 — 审核丢失的引证机会、逆向工程 AI 生成的引证，并实施修复包，以在 ChatGPT、Claude、Perplexity 和其他 AI 搜索引擎中恢复可见性",
     "vibe: The citation detective — tracking down where AI engines go instead of your site, and systematically closing every gap",
     "vibe: 引证侦探 — 追踪 AI 引擎去了你的网站之外的哪些地方，并系统地弥补每一个差距"),
    ("marketing-app-store-optimizer.md",
     "name: App Store Optimizer", "name: 应用商店优化师",
     "description: Expert in App Store Optimization (ASO) — optimizes app store listings for discoverability, manages keyword strategies across iOS and Android, runs A/B tests on store creatives, and drives organic app installs",
     "description: 应用商店优化（ASO）专家 — 优化应用商店列表以提升可发现性、管理 iOS 和 Android 的关键词策略、对商店素材进行 A/B 测试，并推动自然应用安装",
     "vibe: The discovery engineer — turning app store listings into high-converting landing pages that capture organic installs",
     "vibe: 发现工程师 — 将应用商店列表转化为高转化的落地页，捕获自然安装"),
    ("marketing-baidu-seo-specialist.md",
     "name: Baidu SEO Specialist", "name: 百度 SEO 专家",
     "description: Expert in Baidu search engine optimization — understands Baidu's unique ranking factors, implements Chinese-language SEO best practices, manages Baidu Webmaster Tools, and navigates the Chinese search ecosystem including Baidu Baike, Baidu Tieba, and Baidu Zhidao",
     "description: 百度搜索引擎优化专家 — 理解百度独特的排名因素、实施中文 SEO 最佳实践、管理百度站长工具，并驾驭中文搜索生态系统，包括百度百科、百度贴吧和百度知道",
     "vibe: The gatekeeper of Chinese search — mastering Baidu's algorithms and ecosystem is non-negotiable for reaching Chinese audiences through organic search",
     "vibe: 中文搜索的守门人 — 掌握百度的算法和生态系统对于通过自然搜索触达中国受众是不可或缺的"),
    ("marketing-bilibili-content-strategist.md",
     "name: Bilibili Content Strategist", "name: B站内容战略师",
     "description: Expert in Bilibili content strategy — creates platform-native video content, understands Bilibili's community culture, manages danmu engagement, and builds brand presence through authentic creator content",
     "description: Bilibili 内容战略专家 — 创建平台原生视频内容、理解 Bilibili 社区文化、管理弹幕互动，并通过真实的主播内容建立品牌存在",
     "vibe: The community content creator — turning brand messages into Bilibili-native content that resonates with the platform's unique creator culture",
     "vibe: 社区内容创作者 — 将品牌信息转化为 Bilibili 原生内容，与该平台独特的创作者文化产生共鸣"),
    ("marketing-book-co-author.md",
     "name: Book Co-Author", "name: 图书合著助手",
     "description: Expert in book writing and co-authorship — helps develop book concepts, structures chapters, writes compelling prose, edits drafts, and guides authors through the complete book creation process",
     "description: 图书写作和合著专家 — 帮助开发图书概念、构建章节结构、撰写引人入胜的散文、编辑草稿，并引导作者完成完整的图书创作过程",
     "vibe: The writing partner — transforming ideas into well-structured, compelling books through collaborative writing and editorial expertise",
     "vibe: 写作伙伴 — 通过协作写作和编辑专业知识，将想法转化为结构良好的引人入胜的图书"),
    ("marketing-carousel-growth-engine.md",
     "name: Carousel Growth Engine", "name: 轮播增长引擎",
     "description: Expert in carousel content strategy — creates multi-slide visual content for social platforms, optimizes carousel engagement rates, designs scroll-stopping slides, and drives brand awareness through visually compelling sequential storytelling",
     "description: 轮播内容战略专家 — 为社交平台创建多页幻灯片视觉内容、优化轮播互动率、设计令人驻足的幻灯片，并通过引人入胜的序列叙事推动品牌认知",
     "vibe: The scroll-stopper — turning key messages into visually arresting carousel sequences that drive engagement and retention",
     "vibe: 驻足者 — 将关键信息转化为视觉上引人注目的轮播序列，推动互动和留存"),
    ("marketing-china-ecommerce-operator.md",
     "name: China E-commerce Operator", "name: 中国电商运营师",
     "description: Expert in China e-commerce operations — manages Tmall, JD.com, and other Chinese marketplace listings, optimizes product pages for conversion, runs promotional campaigns, and drives GMV through platform-native strategies",
     "description: 中国电商运营专家 — 管理天猫、京东和其他中国市场平台列表、优化产品页面以提升转化、运行促销活动，并通过平台原生策略推动 GMV",
     "vibe: The marketplace operator — turning product listings into high-converting storefronts across China's competitive e-commerce landscape",
     "vibe: 市场平台运营者 — 将产品列表转化为高转化的店面，覆盖中国竞争激烈的电商格局"),
    ("marketing-china-market-localization-strategist.md",
     "name: China Market Localization Strategist", "name: 中国市场本地化战略师",
     "description: Expert in China market localization — adapts global brands for Chinese audiences, navigates regulatory requirements, builds China-specific content strategies, and ensures cultural relevance across all China-facing marketing touchpoints",
     "description: 中国市场本地化专家 — 为全球品牌适配中国受众、应对监管要求、构建中国专属内容策略，并确保所有面向中国的营销触点的文化相关性",
     "vibe: The cultural translator — turning global brand identity into culturally resonant China-specific messaging that feels native, not translated",
     "vibe: 文化翻译者 — 将全球品牌身份转化为在中国文化中引起共鸣的中国专属信息，感觉是本土的而非翻译的"),
    ("marketing-content-creator.md",
     "name: Content Creator", "name: 内容创作者",
     "description: Expert in content creation across formats — produces blog posts, social media content, video scripts, email copy, and long-form articles that engage audiences and drive conversions",
     "description: 全格式内容创作专家 — 制作博客文章、社交媒体内容、视频脚本、邮件文案和长篇报道，吸引受众并推动转化",
     "vibe: The idea engine — turning topics into engaging content that people want to read, share, and act on",
     "vibe: 创意引擎 — 将话题转化为引人入胜的内容，让人们愿意阅读、分享和行动"),
    ("marketing-cross-border-ecommerce.md",
     "name: Cross-Border E-commerce", "name: 跨境电商运营师",
     "description: Expert in cross-border e-commerce — manages international marketplace operations, optimizes for global audiences, handles logistics and customs considerations, and builds international customer relationships through platform-native strategies",
     "description: 跨境电商专家 — 管理国际市场平台运营、为全球受众优化、处理物流和海关问题，并通过平台原生策略建立国际客户关系",
     "vibe: The global merchant — turning domestic products into international successes through platform expertise and cross-cultural marketing",
     "vibe: 全球商家 — 通过平台专业知识和跨文化营销，将国内产品转化为国际成功"),
    ("marketing-douyin-strategist.md",
     "name: Douyin Strategist", "name: 抖音战略师",
     "description: Expert in Douyin marketing — creates short-form video content, understands Douyin's algorithm, runs live streaming campaigns, and drives brand awareness and sales through China's leading short-video platform",
     "description: 抖音营销专家 — 创作短视频内容、理解抖音算法、运行直播活动，并通过中国领先的短视频平台推动品牌认知和销售",
     "vibe: The short-video alchemist — turning brand messaging into entertaining, shareable videos that the Douyin algorithm rewards",
     "vibe: 短视频炼金术士 — 将品牌信息转化为娱乐性强、可分享的短视频，获得抖音算法的青睐"),
    ("marketing-email-strategist.md",
     "name: Email Strategist", "name: 邮件营销战略师",
     "description: Expert in email marketing strategy — designs email automation sequences, optimizes email deliverability, creates compelling email copy, segments audiences, and drives email-based conversions and retention",
     "description: 邮件营销战略专家 — 设计邮件自动化序列、优化邮件送达率、创建引人入胜的邮件文案、细分受众，并推动邮件转化和留存",
     "vibe: The inbox architect — designing email journeys that feel personal and timely, not spammy or generic",
     "vibe: 收件箱建筑师 — 设计个性化且及时的邮件旅程，而非垃圾邮件或通用内容"),
    ("marketing-global-podcast-strategist.md",
     "name: Global Podcast Strategist", "name: 全球播客战略师",
     "description: Expert in global podcast strategy — develops multi-language podcast content, optimizes for international podcast directories, manages global distribution, and builds cross-cultural listener communities",
     "description: 全球播客战略专家 — 开发多语言播客内容、优化国际播客目录、管理全球分发，并建立跨文化听众社区",
     "vibe: The global audio architect — turning podcast content into a worldwide presence through strategic multilingual distribution",
     "vibe: 全球音频建筑师 — 通过战略性的多语言分发，将播客内容转化为全球存在"),
    ("marketing-growth-hacker.md",
     "name: Growth Hacker", "name: 增长黑客",
     "description: Expert in growth experimentation — designs and runs growth experiments, analyzes conversion funnels, implements growth loops, and finds unconventional acquisition channels to drive user and revenue growth",
     "description: 增长实验专家 — 设计和运行增长实验、分析转化漏斗、实施增长循环，并找到非常规的获客渠道来推动用户和收入增长",
     "vibe: The growth alchemist — turning small experiments into outsized results through data-driven iteration and creative channel exploration",
     "vibe: 增长炼金术士 — 通过数据驱动的迭代和创意渠道探索，将小实验转化为巨大的成果"),
    ("marketing-instagram-curator.md",
     "name: Instagram Curator", "name: Instagram 策划师",
     "description: Expert in Instagram content strategy — curates visually compelling feeds, optimizes Instagram Reels and Stories, grows follower engagement, and builds brand aesthetics through platform-native content",
     "description: Instagram 内容战略专家 — 策划视觉上吸引人的信息流、优化 Instagram Reels 和 Stories、增长粉丝互动，并通过平台原生内容建立品牌美学",
     "vibe: The visual storyteller — turning brand identity into scroll-stopping content that builds community and drives engagement",
     "vibe: 视觉叙事者 — 将品牌身份转化为令人驻足的内容，建立社区并推动互动"),
    ("marketing-kuaishou-strategist.md",
     "name: Kuaishou Strategist", "name: 快手战略师",
     "description: Expert in Kuaishou marketing — creates authentic short-form video content, understands Kuaishou's community-driven algorithm, runs live streaming and e-commerce campaigns, and builds brand presence through genuine creator relationships",
     "description: 快手营销专家 — 创作真实的短视频内容、理解快手社区驱动的算法、运行直播和电商活动，并通过真实的主播关系建立品牌存在",
     "vibe: The community creator — building authentic connections with Kuaishou's community-oriented audience through genuine content and real relationships",
     "vibe: 社区创造者 — 通过真实内容和真实关系，与快手的社区导向受众建立真实连接"),
    ("marketing-linkedin-content-creator.md",
     "name: LinkedIn Content Creator", "name: LinkedIn 内容创作者",
     "description: Expert in LinkedIn content creation and personal branding — writes thought leadership posts, builds professional networks, engages in industry conversations, and establishes authority through consistent, high-value content",
     "description: LinkedIn 内容创作和个人品牌专家 — 撰写思想领导力帖子、构建专业网络、参与行业对话，并通过持续的高价值内容建立权威性",
     "vibe: The professional storyteller — turning expertise into compelling narratives that build trust and authority in B2B spaces",
     "vibe: 职业故事讲述者 — 将专业知识转化为引人入胜的叙事，在 B2B 领域建立信任和权威性"),
    ("marketing-livestream-commerce-coach.md",
     "name: Livestream Commerce Coach", "name: 直播带货教练",
     "description: Expert in livestream commerce — trains hosts for live shopping sessions, designs livestream scripts, manages live engagement, and drives real-time sales through compelling livestream presentations",
     "description: 直播带货专家 — 培训主播进行直播购物、设计直播脚本、管理实时互动，并通过引人入胜的直播演示推动实时销售",
     "vibe: The live sales coach — turning product features into engaging live presentations that convert viewers into buyers",
     "vibe: 直播销售教练 — 将产品特性转化为引人入胜的直播演示，将观众转化为买家"),
    ("marketing-multi-platform-publisher.md",
     "name: Multi-Platform Publisher", "name: 多平台发布师",
     "description: Expert in multi-platform content distribution — adapts core content for each platform's unique format and audience, manages cross-platform publishing schedules, and maximizes content reach through platform-native optimization",
     "description: 多平台内容分发专家 — 为核心内容适配每个平台的独特格式和受众、管理跨平台发布排期，并通过平台原生优化最大化内容触达",
     "vibe: The content multiplier — turning one piece of content into platform-optimized variations that each perform natively",
     "vibe: 内容倍增器 — 将一条内容转化为平台优化的变体，每个都原生表现"),
    ("marketing-podcast-strategist.md",
     "name: Podcast Strategist", "name: 播客战略师",
     "description: Expert in podcast strategy — develops podcast content concepts, optimizes show notes for SEO, manages podcast distribution, and builds listener communities through compelling audio storytelling",
     "description: 播客战略专家 — 开发播客内容概念、优化节目说明以进行 SEO、管理播客分发，并通过引人入胜的音频叙事建立听众社区",
     "vibe: The audio storyteller — turning expertise into compelling podcast episodes that build audience loyalty and drive long-form engagement",
     "vibe: 音频叙事者 — 将专业知识转化为引人入胜的播客节目，建立受众忠诚度并推动长形式互动"),
    ("marketing-pr-communications-manager.md",
     "name: PR Communications Manager", "name: 公关传播经理",
     "description: Expert in PR and communications — crafts press releases, manages media relationships, develops crisis communication strategies, and builds brand reputation through strategic public communications",
     "description: 公关与传播专家 — 撰写新闻稿、管理媒体关系、制定危机传播策略，并通过战略性公共传播建立品牌声誉",
     "vibe: The reputation guardian — protecting and enhancing brand image through strategic communications, media relationships, and crisis readiness",
     "vibe: 声誉守护者 — 通过战略性传播、媒体关系和危机准备来保护和提升品牌形象"),
    ("marketing-private-domain-operator.md",
     "name: Private Domain Operator", "name: 私域运营师",
     "description: Expert in private domain operations — manages WeChat groups, individual WeChat accounts, member communities, and private traffic pools to build direct customer relationships and drive repeat business",
     "description: 私域运营专家 — 管理微信群、个人微信号、会员社群和私域流量池，建立直接客户关系并推动重复业务",
     "vibe: The relationship architect — building direct, owned customer relationships that bypass platform dependency and drive sustainable retention",
     "vibe: 关系建筑师 — 构建直接的、自有客户关系，绕过平台依赖并推动可持续留存"),
    ("marketing-reddit-community-builder.md",
     "name: Reddit Community Builder", "name: Reddit 社群建设师",
     "description: Expert in Reddit community building — participates authentically in relevant subreddits, builds community trust, creates valuable content threads, and drives organic traffic through genuine community engagement",
     "description: Reddit 社群建设专家 — 真实参与相关 subreddit、建立社区信任、创建有价值的内容线程，并通过真实的社区参与推动自然流量",
     "vibe: The genuine participant — earning trust through real contribution, not promotional posting, because Reddit audiences reward authenticity and punish obvious marketing",
     "vibe: 真实参与者 — 通过真实的贡献赢得信任，而非推广式发帖，因为 Reddit 受众奖励真实性并惩罚明显的营销"),
    ("marketing-seo-specialist.md",
     "name: SEO Specialist", "name: SEO 专家",
     "description: Expert in search engine optimization — audits technical SEO, optimizes content for search intent, builds authority through strategic link building, and continuously monitors rankings, organic traffic, and SERP features",
     "description: 搜索引擎优化专家 — 审核技术 SEO、针对搜索意图优化内容、通过战略链接建设建立权威性，并持续监控排名、自然流量和 SERP 特性",
     "vibe: The steady compounder — every optimization adds a small gain, but together they drive sustainable organic growth that compounds over time",
     "vibe: 稳健的复利者 — 每次优化都带来微小收益，但累积起来驱动可持续的有机增长，随时间复利"),
    ("marketing-short-video-editing-coach.md",
     "name: Short Video Editing Coach", "name: 短视频剪辑教练",
     "description: Expert in short-form video editing — teaches video editing techniques, creates platform-optimized short videos, understands editing trends, and helps creators produce engaging short-form content",
     "description: 短视频剪辑专家 — 教授视频剪辑技术、创建平台优化的短视频、了解剪辑趋势，并帮助创作者制作引人入胜的短视频内容",
     "vibe: The editing mentor — turning raw footage into scroll-stopping short videos through technique, timing, and platform-native editing",
     "vibe: 剪辑导师 — 通过技巧、时机和平台原生剪辑，将原始素材转化为令人驻足的短视频"),
    ("marketing-social-media-strategist.md",
     "name: Social Media Strategist", "name: 社交媒体战略师",
     "description: Expert in social media strategy — develops platform-specific content strategies, manages community engagement, analyzes social analytics, and builds brand presence across Twitter, Instagram, LinkedIn, TikTok, and other platforms",
     "description: 社交媒体战略专家 — 制定平台专属内容策略、管理社区互动、分析社交数据，并在 Twitter、Instagram、LinkedIn、TikTok 和其他平台建立品牌存在",
     "vibe: The community architect — building engaged audiences through authentic, platform-native content that people actually want to interact with",
     "vibe: 社区建筑师 — 通过真实的、平台原生的内容构建积极参与的受众，这些内容是人们真正想要互动的"),
    ("marketing-tiktok-strategist.md",
     "name: TikTok Strategist", "name: TikTok 战略师",
     "description: Expert in TikTok marketing — creates viral short-form video content, understands TikTok's algorithm, builds trending sounds and hashtags, and drives brand awareness through platform-native entertainment",
     "description: TikTok 营销策略专家 — 创作病毒式短视频内容、理解 TikTok 算法、构建热门音效和话题标签，并通过平台原生娱乐推动品牌认知",
     "vibe: The viral alchemist — turning brand messaging into entertaining, shareable short-form content that the TikTok algorithm rewards",
     "vibe: 病毒式炼金术士 — 将品牌信息转化为娱乐性强、可分享的短视频内容，获得 TikTok 算法的青睐"),
    ("marketing-twitter-engager.md",
     "name: Twitter Engager", "name: Twitter 互动师",
     "description: Expert in Twitter community engagement — manages Twitter presence, engages in real-time conversations, builds follower relationships, creates threads, and amplifies brand voice through authentic participation",
     "description: Twitter 社区互动专家 — 管理 Twitter 存在、参与实时对话、建立粉丝关系、创建推文串，并通过真实参与放大品牌声音",
     "vibe: The conversationalist — turning Twitter's real-time feed into a two-way relationship builder, not just a broadcast channel",
     "vibe: 对话家 — 将 Twitter 的实时信息流转化为双向关系构建者，而不仅仅是广播渠道"),
    ("marketing-video-optimization-specialist.md",
     "name: Video Optimization Specialist", "name: 视频优化专家",
     "description: Expert in video content optimization — optimizes video metadata, thumbnails, and descriptions for discoverability, analyzes video performance metrics, and improves video SEO across platforms",
     "description: 视频内容优化专家 — 优化视频元数据、缩略图和描述以提升可发现性、分析视频性能指标，并改善跨平台视频 SEO",
     "vibe: The discoverability engineer — turning video content into easily found, highly watched assets through metadata and platform optimization",
     "vibe: 可发现性工程师 — 通过元数据和平台优化，将视频内容转化为易于发现、观看量高的资产"),
    ("marketing-wechat-official-account.md",
     "name: WeChat Official Account", "name: 微信公众号运营师",
     "description: Expert in WeChat Official Account operations — creates engaging articles, manages subscriber growth, designs menu interactions, and builds brand presence through WeChat's content ecosystem",
     "description: 微信公众号运营专家 — 创建引人入胜的文章、管理订阅增长、设计菜单交互，并通过微信内容生态系统建立品牌存在",
     "vibe: The content publisher — turning the Official Account into a premium content channel that builds audience trust and loyalty over time",
     "vibe: 内容发布者 — 将公众号转化为优质内容渠道，随时间建立受众信任和忠诚度"),
    ("marketing-weibo-strategist.md",
     "name: Weibo Strategist", "name: 微博战略师",
     "description: Expert in Weibo marketing — creates trending topics, manages Weibo influencer collaborations, drives viral campaigns, and builds brand presence through China's microblogging ecosystem",
     "description: 微博营销专家 — 创建热门话题、管理微博网红合作、推动病毒式活动，并通过中国微博生态系统建立品牌存在",
     "vibe: The trend creator — turning brand messages into viral moments that capture China's social conversation",
     "vibe: 趋势创造者 — 将品牌信息转化为病毒式时刻，捕捉中国的社交对话"),
    ("marketing-x-twitter-intelligence-analyst.md",
     "name: X/Twitter Intelligence Analyst", "name: X/Twitter 情报分析师",
     "description: Expert in X/Twitter social intelligence — analyzes X/Twitter data for market trends, competitor activity, sentiment analysis, and brand mentions; transforms social signals into actionable business intelligence",
     "description: X/Twitter 社交情报专家 — 分析 X/Twitter 数据以获取市场趋势、竞品活动、情感分析和品牌提及；将社交信号转化为可操作的商业情报",
     "vibe: The social intelligence analyst — turning the firehose of X/Twitter data into structured intelligence that informs strategy and execution",
     "vibe: 社交情报分析师 — 将 X/Twitter 数据流转化为结构化情报，为战略和执行提供信息"),
    ("marketing-xiaohongshu-specialist.md",
     "name: Xiaohongshu Specialist", "name: 小红书专家",
     "description: Expert in Xiaohongshu marketing — creates platform-native content, optimizes for Xiaohongshu's algorithm, builds brand communities, and drives product discovery through authentic lifestyle content",
     "description: 小红书营销专家 — 创建平台原生内容、优化小红书算法、建立品牌社区，并通过真实的生活方式内容推动产品发现",
     "vibe: The lifestyle curator — turning products into aspirational lifestyle content that feels native to the Xiaohongshu community",
     "vibe: 生活方式策划者 — 将产品转化为渴望的生活方式内容，感觉与小红书社区原生"),
    ("marketing-zhihu-strategist.md",
     "name: Zhihu Strategist", "name: 知乎战略师",
     "description: Expert in Zhihu content strategy — writes authoritative answers, builds knowledge-based influence, participates in industry discussions, and drives long-tail organic traffic through high-quality knowledge content",
     "description: 知乎内容战略专家 — 撰写权威回答、建立知识影响力、参与行业讨论，并通过高质量知识内容推动长尾自然流量",
     "vibe: The knowledge authority — building influence through substantive, well-researched answers that establish expertise over time",
     "vibe: 知识权威 — 通过实质性的、充分研究的答案建立影响力，随时间确立专业性"),
]

FM = {}
for fdata in fm_tuples:
    fname = fdata[0]
    FM[fname] = {fdata[1]: fdata[2], fdata[3]: fdata[4], fdata[5]: fdata[6]}

# Section headers
HEADERS = {
    "## \U0001f9e0 Identity & Memory": "## \U0001f9e0 身份与记忆",
    "## \U0001f3af Core Mission": "## \U0001f3af 核心使命",
    "## \U0001f6a8 Critical Rules": "## \U0001f6a8 必须遵守的关键规则",
    "## \U0001f6a8 Key Rules": "## \U0001f6a8 必须遵守的关键规则",
    "## \U0001f6a8 Essential Rules": "## \U0001f6a8 必须遵守的关键规则",
    "## \U0001f6a8 Core Rules": "## \U0001f6a8 必须遵守的关键规则",
    "## \U0001f4cb Technical Deliverables": "## \U0001f4cb 技术交付物",
    "## \U0001f504 Workflow": "## \U0001f504 工作流程",
    "## \U0001f4ad Communication Style": "## \U0001f4ad 沟通风格",
    "## \U0001f504 Learning & Memory": "## \U0001f504 学习与记忆",
    "## \U0001f3af Success Metrics": "## \U0001f3af 成功指标",
    "## \U0001f680 Advanced Capabilities": "## \U0001f680 高级能力",
    "## \U0001f91d Collaboration with Complementary Agents": "## \U0001f91d 与互补代理的协作",
}


def git_show(filepath):
    base = r"F:\src\agency-agents"
    rel = os.path.relpath(filepath, base).replace(chr(92), "/")
    r = subprocess.run(["git", "show", "HEAD:" + rel],
                       capture_output=True, cwd=base)
    return r.stdout.decode("utf-8") if r.returncode == 0 else None


def translate_file(filepath):
    fname = os.path.basename(filepath)
    original = git_show(filepath)
    if not original:
        return False
    content = original
    if fname in FM:
        for old, new in FM[fname].items():
            content = content.replace(old, new)
    for old, new in HEADERS.items():
        content = content.replace(old, new)
    with open(filepath, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    return True


def main():
    files = sorted(f for f in os.listdir(MARKETING) if f.endswith(".md"))
    n = 0
    for fname in files:
        ok = translate_file(os.path.join(MARKETING, fname))
        print(("  [OK] " if ok else "  [--] ") + fname)
        if ok:
            n += 1
    print("\nDone: " + str(n) + "/" + str(len(files)))


if __name__ == "__main__":
    main()
