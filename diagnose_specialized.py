"""Rebuild translations from exact git content for all 56 specialized files."""
import subprocess
import os
import json

BASE = r"F:\src\agency-agents"
SHA = "9f3e401"
SPECIALIZED = os.path.join(BASE, "specialized")

# Manually curated Chinese translations for each file
# Using exact English strings from git commit 9f3e401

# First, extract exact front-matter from git
def get_git_fm(fname):
    r = subprocess.run(["git", "show", SHA + ":specialized/" + fname],
                       capture_output=True, cwd=BASE)
    if r.returncode != 0:
        return None
    content = r.stdout.decode("utf-8")
    fm = {}
    h1 = ""
    for line in content.split("\n"):
        s = line.strip()
        if s.startswith("name:"):
            fm["name"] = s
        elif s.startswith("description:"):
            fm["description"] = s
        elif s.startswith("vibe:"):
            fm["vibe"] = s
        if line.strip().startswith("# "):
            h1 = line.strip()
    return {"fm": fm, "h1": h1}

# Build translation mappings from extracted values
translations = {}
for fname in sorted(os.listdir(SPECIALIZED)):
    if not fname.endswith(".md"):
        continue
    git_data = get_git_fm(fname)
    if not git_data:
        continue
    fm = git_data["fm"]
    h1 = git_data["h1"]
    
    # Map to Chinese
    t = {}
    if "name" in fm:
        en_name = fm["name"]
        cn_name = en_name.replace("name: ", "name: ")
        # We'll handle name translations below
    if "description" in fm:
        en_desc = fm["description"]
        t[en_desc] = en_desc  # placeholder
    if "vibe" in fm:
        en_vibe = fm["vibe"]
        t[en_vibe] = en_vibe  # placeholder
    if h1:
        t[h1] = h1  # placeholder
    translations[fname] = t

# Print what we need to translate
for fname, t in sorted(translations.items()):
    print(fname)
    for k, v in t.items():
        if k == v:  # placeholder
            print("  NEED: " + k[:100])
    print()
