"""Check simple relative Markdown links and required foundational documents."""
from pathlib import Path
import re
import sys

root = Path(__file__).resolve().parents[1]
required = [
    "README.md", "PRINCIPLES.md", "AGENTS.md", "SECURITY.md",
    "docs/MASTER_PLAN.md", "docs/ROADMAP.md",
    "docs/architecture/ARCHITECTURE.md", "docs/ai-native/AI_ARCHITECTURE.md",
]
errors = [f"Missing {p}" for p in required if not (root / p).is_file()]
for file in root.rglob("*.md"):
    if ".git" in file.parts or "target" in file.parts:
        continue
    for target in re.findall(r"\]\(([^)\s]+)\)", file.read_text(encoding="utf-8")):
        if "://" in target or target.startswith(("#", "mailto:")):
            continue
        path = target.split("#", 1)[0]
        if path and not (file.parent / path).exists():
            errors.append(f"{file.relative_to(root)}: missing {target}")
if errors:
    print("\n".join(errors), file=sys.stderr)
    sys.exit(1)
print("Foundational documentation and simple relative links: OK")
