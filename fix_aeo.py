"""Fix the corrupted name line in marketing-aeo-foundations.md"""
path = r"F:\src\agency-agents\marketing\marketing-aeo-foundations.md"
lines = open(path, encoding="utf-8").read().split("\n")
new = []
for line in lines:
    if line.strip() == " Foundations Architect":
        new.append("name: AEO 基础架构师")
    else:
        new.append(line)
open(path, "w", encoding="utf-8").write("\n".join(new))
print("fixed name line")
