#!/usr/bin/env python3
"""Make one portable ZIP per skill without repository development files."""
from pathlib import Path
import re
import zipfile


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"


def package(skill):
    text = (skill / "SKILL.md").read_text(encoding="utf-8")
    version = re.search(r'^  version: "([0-9]+\.[0-9]+\.[0-9]+)"$', text, re.MULTILINE)
    if not version:
        raise SystemExit(f"{skill.name}: no semantic version in SKILL.md metadata")
    destination = ROOT / "dist" / f"{skill.name}-v{version[1]}.zip"
    destination.parent.mkdir(exist_ok=True)
    files = sorted(
        path for path in skill.rglob("*")
        if path.is_file()
        and not any(part.startswith(".") or part == "__pycache__"
                    for part in path.relative_to(skill).parts)
        and path.suffix not in {".pyc", ".pyo"}
    )
    with zipfile.ZipFile(destination, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in files:
            member = zipfile.ZipInfo(path.relative_to(SKILLS).as_posix())
            member.external_attr = 0o100644 << 16
            archive.writestr(member, path.read_bytes(), compress_type=zipfile.ZIP_DEFLATED)
    with zipfile.ZipFile(destination) as archive:
        if archive.testzip() is not None:
            raise SystemExit(f"{skill.name}: ZIP integrity check failed")
    return destination


def main():
    for entry in sorted(SKILLS.glob("*/SKILL.md")):
        print(package(entry.parent))


if __name__ == "__main__":
    main()
