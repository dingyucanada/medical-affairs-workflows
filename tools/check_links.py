#!/usr/bin/env python3
"""Check local Markdown targets and the pinned original catalog mapping."""
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "medical-affairs-workflows"
MAPPING = SKILL / "references" / "source-map.md"
LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")
errors = []
documents = [*ROOT.glob("*.md"), *ROOT.glob("docs/*.md"),
             *ROOT.glob("evals/*.md"), SKILL / "SKILL.md", *SKILL.glob("references/*.md")]
for document in documents:
    inline_code_free = re.sub(r"`[^`\n]*`", "", document.read_text(encoding="utf-8"))
    for target in LINK.findall(inline_code_free):
        if "#" in target:
            target = target.split("#", 1)[0]
        if target and "://" not in target and not (document.parent / target).exists():
            errors.append(f"{document.relative_to(ROOT)}: missing {target}")

mapping = MAPPING.read_text(encoding="utf-8")
originals = re.findall(r"^\| \[.+?\]\(https://medical-skills\.pages\.dev/skills/([a-z-]+)\) \| `([a-z-]+)`", mapping, re.M)
if len(originals) != 64 or len({slug for slug, _ in originals}) != 64 or any(a != b for a, b in originals):
    errors.append("Original catalog mapping must contain the 64 distinct pinned slugs.")
for group in re.split(r"^## ", mapping, flags=re.M)[1:]:
    file = re.search(r"\[打开整合工作流\]\(([^)]+)\)", group)
    if file is None:
        errors.append("Original catalog group is missing its workflow link.")
        continue
    target = MAPPING.parent / file[1]
    if not target.is_file():
        continue
    headings = set(re.findall(r"^## (.+)$", target.read_text(encoding="utf-8"), re.M))
    for row in re.findall(r"^\| \[.+ \| ([^|]+) · [^|]+ \|$", group, re.M):
        if row not in headings:
            errors.append(f"{target.name}: missing mapped section {row}")
if errors:
    raise SystemExit("\n".join(errors))
print(f"Checked {len(documents)} Markdown documents and the 64 pinned catalog entries.")
