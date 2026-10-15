#!/usr/bin/env python3
"""Check that every skill stays within the format both Claude and ChatGPT accept.

`claude plugin validate` checks that front matter parses. This adds the
portability rules from the Agent Skills specification (https://agentskills.io)
that it does not enforce: front matter uses only keys both hosts accept
(claude.ai rejects any others; its Claude-specific `allowed-tools` is left
out), and `name` matches the skill's folder. The line limit is the
specification's recommendation, kept so long guidance moves into supporting
files.
"""

import re
import sys
from pathlib import Path

ALLOWED_KEYS = {"name", "description", "license", "compatibility", "metadata"}
NAME_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MAX_NAME_LENGTH = 64
MAX_DESCRIPTION_LENGTH = 1024
MAX_SKILL_LINES = 500

SKILLS_DIR = Path(__file__).resolve().parent.parent / "gumnut-photos" / "skills"


def parse_front_matter(text: str) -> dict[str, str] | None:
    """Return top-level front-matter keys and their (unfolded) scalar values.

    Every unindented line counts as a top-level key, whatever its syntax, so an
    unusual key form shows up as an unsupported key instead of slipping past
    the allowlist. A line with no colon is returned whole as its own key.
    """
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    try:
        end = lines.index("---", 1)
    except ValueError:
        return None

    fields: dict[str, str] = {}
    key = None
    for line in lines[1:end]:
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith((" ", "\t")):
            if key:
                fields[key] = f"{fields[key]} {line.strip()}".strip()
            continue
        key, _, value = line.partition(":")
        key = key.strip()
        if len(key) >= 2 and key[0] == key[-1] and key[0] in "\"'":
            key = key[1:-1]
        value = value.strip()
        fields[key] = "" if value in (">", "|", ">-", "|-") else value.strip("\"'")
    return fields


def check_skill(skill_dir: Path) -> list[str]:
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        return [f"{skill_dir.name}: missing SKILL.md"]

    text = skill_file.read_text(encoding="utf-8")
    fields = parse_front_matter(text)
    if fields is None:
        return [f"{skill_dir.name}: SKILL.md has no front matter"]

    errors = []
    extra = sorted(set(fields) - ALLOWED_KEYS)
    if extra:
        errors.append(f"{skill_dir.name}: unsupported front-matter keys {extra}")

    name = fields.get("name", "")
    if name != skill_dir.name:
        errors.append(f"{skill_dir.name}: name {name!r} must match the folder name")
    if not NAME_PATTERN.match(name) or len(name) > MAX_NAME_LENGTH:
        errors.append(
            f"{skill_dir.name}: name must be lowercase letters, digits, and single "
            f"hyphens, at most {MAX_NAME_LENGTH} characters"
        )

    description = fields.get("description", "")
    if not description:
        errors.append(f"{skill_dir.name}: description is required")
    elif len(description) > MAX_DESCRIPTION_LENGTH:
        errors.append(
            f"{skill_dir.name}: description is {len(description)} characters "
            f"(max {MAX_DESCRIPTION_LENGTH})"
        )

    line_count = len(text.splitlines())
    if line_count > MAX_SKILL_LINES:
        errors.append(
            f"{skill_dir.name}: SKILL.md is {line_count} lines (max {MAX_SKILL_LINES}); "
            "move detail into supporting files"
        )
    return errors


def main() -> int:
    skill_dirs = sorted(p for p in SKILLS_DIR.glob("*") if p.is_dir()) if SKILLS_DIR.is_dir() else []
    errors = [error for skill_dir in skill_dirs for error in check_skill(skill_dir)]
    for error in errors:
        print(f"error: {error}", file=sys.stderr)
    if not errors:
        print(f"Checked {len(skill_dirs)} skill(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
