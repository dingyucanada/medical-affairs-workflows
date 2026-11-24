#!/usr/bin/env python3
"""Make a portable skill-only ZIP without repository development files."""
from pathlib import Path
import re
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "medical-affairs-workflows"


def main():
    text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
    version = re.search(r'^  version: "([0-9]+\.[0-9]+\.[0-9]+)"$', text, re.MULTILINE)
    if not version:
        raise SystemExit("No semantic version in SKILL.md metadata")
    destination = ROOT / "dist" / f"{SKILL.name}-v{version[1]}.zip"
    destination.parent.mkdir(exist_ok=True)
    files = sorted(
        p for p in SKILL.rglob("*")
        if p.is_file() and not any(part.startswith(".") or part == "__pycache__"
                                   for part in p.relative_to(SKILL).parts)
        and p.suffix not in {".pyc", ".pyo"}
    )
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            member = zipfile.ZipInfo(path.relative_to(SKILL.parent).as_posix())
            member.external_attr = 0o100644 << 16
            archive.writestr(member, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED)
    with zipfile.ZipFile(destination) as archive:
        if archive.testzip() is not None:
            raise SystemExit("ZIP integrity check failed")
    print(destination)


if __name__ == "__main__":
    main()
