"""Fix corrupted name: lines across all marketing files.
The pattern is: name: X was partially replaced, leaving just " X" or similar.
"""
import os

MARKETING = r"F:\src\agency-agents\marketing"

# Correct Chinese names for each file
CORRECT_NAMES = {
    "marketing-aeo-foundations.md": "AEO 基础架构师",
    "marketing-agentic-search-optimizer.md": "代理式搜索优化师",
    "marketing-ai-citation-strategist.md": "AI 引证战略师",
    "marketing-app-store-optimizer.md": "应用商店优化师",
    "marketing-baidu-seo-specialist.md": "百度 SEO 专家",
    "marketing-bilibili-content-strategist.md": "B站内容战略师",
    "marketing-book-co-author.md": "图书合著助手",
    "marketing-carousel-growth-engine.md": "轮播增长引擎",
    "marketing-china-ecommerce-operator.md": "中国电商运营师",
    "marketing-china-market-localization-strategist.md": "中国市场本地化战略师",
    "marketing-content-creator.md": "内容创作者",
    "marketing-cross-border-ecommerce.md": "跨境电商运营师",
    "marketing-douyin-strategist.md": "抖音战略师",
    "marketing-email-strategist.md": "邮件营销战略师",
    "marketing-global-podcast-strategist.md": "全球播客战略师",
    "marketing-growth-hacker.md": "增长黑客",
    "marketing-instagram-curator.md": "Instagram 策划师",
    "marketing-kuaishou-strategist.md": "快手战略师",
    "marketing-linkedin-content-creator.md": "LinkedIn 内容创作者",
    "marketing-livestream-commerce-coach.md": "直播带货教练",
    "marketing-multi-platform-publisher.md": "多平台发布师",
    "marketing-podcast-strategist.md": "播客战略师",
    "marketing-pr-communications-manager.md": "公关传播经理",
    "marketing-private-domain-operator.md": "私域运营师",
    "marketing-reddit-community-builder.md": "Reddit 社群建设师",
    "marketing-seo-specialist.md": "SEO 专家",
    "marketing-short-video-editing-coach.md": "短视频剪辑教练",
    "marketing-social-media-strategist.md": "社交媒体战略师",
    "marketing-tiktok-strategist.md": "TikTok 战略师",
    "marketing-twitter-engager.md": "Twitter 互动师",
    "marketing-video-optimization-specialist.md": "视频优化专家",
    "marketing-wechat-official-account.md": "微信公众号运营师",
    "marketing-weibo-strategist.md": "微博战略师",
    "marketing-x-twitter-intelligence-analyst.md": "X/Twitter 情报分析师",
    "marketing-xiaohongshu-specialist.md": "小红书专家",
    "marketing-zhihu-strategist.md": "知乎战略师",
}

def fix_file(filepath):
    fname = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    changed = False
    new_lines = []
    i = 0
    in_frontmatter = False
    found_name = False
    
    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        
        if stripped == "---":
            if not in_frontmatter:
                in_frontmatter = True
                new_lines.append(line)
                i += 1
                continue
            else:
                in_frontmatter = False
                new_lines.append(line)
                i += 1
                continue
        
        if in_frontmatter and fname in CORRECT_NAMES:
            # Check if this is the name: line (could be corrupted)
            if stripped.startswith("name:"):
                new_lines.append("name: " + CORRECT_NAMES[fname] + "\n")
                changed = True
                i += 1
                continue
            elif stripped and not stripped.startswith("name") and not found_name and i > 0:
                # The name line was corrupted - the previous line might be empty
                # Check if previous line in output is the broken name
                # This is the case where "name: X" became just " X"
                pass
        
        new_lines.append(line)
        i += 1
    
    if changed:
        with open(filepath, "w", encoding="utf-8") as f:
            f.writelines(new_lines)
    return changed

# Also need to handle the case where "name: X" was replaced to just " X"
# Let's do a second pass for that specific corruption pattern
def fix_corrupted_name_lines(filepath):
    fname = os.path.basename(filepath)
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    original = content
    in_fm = False
    lines = content.split("\n")
    new_lines = []
    
    for i, line in enumerate(lines):
        stripped = line.strip()
        
        if stripped == "---":
            if not in_fm:
                in_fm = True
                new_lines.append(line)
                continue
            else:
                in_fm = False
                new_lines.append(line)
                continue
        
        if in_fm and fname in CORRECT_NAMES:
            # Check if this looks like a corrupted name line
            # Pattern: starts with a space or a word, no "name:" prefix
            # and the next non-empty line starts with "description:" or another key
            if i + 1 < len(lines):
                next_line = lines[i + 1].strip()
                if next_line.startswith("description:") or next_line.startswith("tools:") or next_line.startswith("color:") or next_line.startswith("emoji:"):
                    # This might be a corrupted name line
                    # Check if it doesn't start with "name:"
                    if not stripped.startswith("name:") and not stripped.startswith("---"):
                        # It's likely a corrupted name line
                        new_lines.append("name: " + CORRECT_NAMES[fname])
                        continue
        
        new_lines.append(line)
    
    new_content = "\n".join(new_lines)
    if new_content != original:
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
    return False


def main():
    files = sorted(f for f in os.listdir(MARKETING) if f.endswith(".md"))
    n = 0
    for fname in files:
        path = os.path.join(MARKETING, fname)
        c1 = fix_file(path)
        c2 = fix_corrupted_name_lines(path)
        if c1 or c2:
            n += 1
            print(f"  [FIX] {fname}")
    print(f"\nFixed {n} files")


if __name__ == "__main__":
    main()
