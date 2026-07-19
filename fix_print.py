"""Fix the print line in translate_marketing.py"""
path = r"F:\src\agency-agents\translate_marketing.py"
lines = open(path, encoding="utf-8").read().split("\n")
new = []
for line in lines:
    if "changed" in line and "fname" in line and "print" in line:
        new.append('        s = "[OK]" if changed else "[--]"; print(f"  {s} {fname}")')
    else:
        new.append(line)
open(path, "w", encoding="utf-8").write("\n".join(new))
print("fixed")
