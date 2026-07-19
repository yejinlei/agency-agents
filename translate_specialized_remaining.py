"""Translate front-matter for the 2 files missing from git."""
import os

BASE = r"F:\src\agency-agents"
SPECIALIZED = os.path.join(BASE, "specialized")

# resume-tailor.md
path = os.path.join(SPECIALIZED, "resume-tailor.md")
with open(path, "r", encoding="utf-8") as f:
    content = f.read()
replacements = {
    "name: Resume Tailor": "name: 简历定制师",
    "description: Candidate-side resume optimization specialist who analyzes job descriptions, maps real experience to role requirements, improves ATS keyword alignment, and rewrites bullets without fabricating qualifications.":
    "description: 候选人侧简历优化专家，分析职位描述、将真实经验映射到职位要求、改善 ATS 关键词对齐，并改写要点而不伪造资质。",
    "vibe: Tailors the resume to the role without tailoring the truth.":
    "vibe: 将简历适配到职位而不扭曲事实。",
    "# Resume Tailor Agent": "# 简历定制师代理",
}
for old, new in replacements.items():
    content = content.replace(old, new)
with open(path, "w", encoding="utf-8", newline="\n") as f:
    f.write(content)
print("[OK] resume-tailor.md")

# specialized-codebase-archaeologist.md
path = os.path.join(SPECIALIZED, "specialized-codebase-archaeologist.md")
with open(path, "r", encoding="utf-8") as f:
    content = f.read()
replacements = {
    "name: Codebase Archaeologist": "name: 代码库考古学家",
    "description: Multi-session, multi-tool drift detection specialist who audits codebases touched by several AI coding tools (Claude, Cursor, Copilot, Windsurf, etc.) over time, finding silent logic mismatches, dead code, and doc-vs-code divergence that no single session would ever notice on its own.":
    "description: 多会话、多工具漂移检测专家，审计被多个 AI 编码工具（Claude、Cursor、Copilot、Windsurf 等）随时间触及的代码库，发现无声的逻辑不匹配、死代码和文档与代码之间的分歧，这些是任何单个会话都无法自行注意到的。",
    "vibe: I read code like tree rings — I can tell you which layer was written by which hand, and what got left half-finished when the next one took over.":
    "vibe: 我像读年轮一样读代码——我能告诉你哪一层是由哪只手写的，以及当下一只接手时什么被半完成地留下了。",
    "# Codebase Archaeologist Agent 性格": "# 代码库考古学家代理个性",
}
for old, new in replacements.items():
    content = content.replace(old, new)
with open(path, "w", encoding="utf-8", newline="\n") as f:
    f.write(content)
print("[OK] specialized-codebase-archaeologist.md")

print("\nDone: 2 additional files translated")
