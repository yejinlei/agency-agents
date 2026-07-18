"""
Extract all English prose from agent body files for translation.
Outputs a JSON translation table to scripts/i18n/translations.json
"""
import os, re, json

BASE = r'F:\src\agency-agents'
SKIP_DIRS = {'node_modules','.git','.agent_context','.codex','.multica','.agents','__pycache__'}

# Collect all English sentences from agent body files
all_sentences = {}

for root, dirs, files in os.walk(BASE):
    dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
    for f in sorted(files):
        if not f.endswith('.md'):
            continue
        path = os.path.join(root, f)
        try:
            with open(path, 'r', encoding='utf-8') as fh:
                content = fh.read()
        except:
            continue
        # Extract body after frontmatter
        fm = content.find('---', 3)
        if fm < 0:
            continue
        body = content[fm + 3:]
        # Skip code blocks
        in_code = False
        for line in body.split('\n'):
            stripped = line.strip()
            if stripped.startswith('```'):
                in_code = not in_code
                continue
            if in_code:
                continue
            # Extract English sentences (>= 15 chars, >= 70% ASCII letters)
            # Use regex to find complete sentences
            for m in re.finditer(r'([A-Z][a-zA-Z,;\s:!\u2013\u2014\u2018\u2019\u201c\u201d\.\-?\'\"\(\)]{15,300}(?=[.\s](?:[A-Z][a-zA-Z]|\s*$)))', line):
                s = m.group(1).strip().rstrip('.,;:!?\"')
                s = re.sub(r'\s+', ' ', s)
                # Check if mostly English
                ascii_letters = sum(1 for c in s if c.isalpha() and c.isascii())
                total_chars = len(s)
                if total_chars >= 15 and total_chars <= 300 and ascii_letters / max(total_chars, 1) >= 0.6:
                    all_sentences[s] = all_sentences.get(s, 0) + 1

# Sort by frequency
sorted_sentences = sorted(all_sentences.items(), key=lambda x: -x[1])
print(f"Total unique English sentences: {len(sorted_sentences)}")
print(f"Total sentence occurrences: {sum(c for _, c in sorted_sentences)}")
print()
print("Top 100 most common:")
for s, c in sorted_sentences[:100]:
    print(f"  {c:3d}x  {s[:120]}")

# Save to JSON
with open(r'F:\src\agency-agents\scripts\i18n\sentences.json', 'w', encoding='utf-8') as f:
    json.dump([{'sentence': s, 'count': c} for s, c in sorted_sentences], f, ensure_ascii=False, indent=2)
print(f"\nSaved to scripts/i18n/sentences.json")
