#!/usr/bin/env python3
# /// script
# requires-python = ">=3.10"
# dependencies = ["pyyaml==6.0.3"]
# ///
"""Check that every skill stays within the format both Claude and ChatGPT accept.

`claude plugin validate` checks that front matter parses. This adds the
portability rules from the Agent Skills specification (https://agentskills.io)
that it does not enforce: front matter uses only keys both hosts accept
(claude.ai rejects any others; its Claude-specific `allowed-tools` is left
out), `name` matches the skill's folder, and the specification's field limits
hold. The line limit is the specification's recommendation, kept so long
guidance moves into supporting files.
"""

import re
import sys
from pathlib import Path

import yaml

ALLOWED_KEYS = {"name", "description", "license", "compatibility", "metadata"}
NAME_PATTERN = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
MAX_NAME_LENGTH = 64
MAX_DESCRIPTION_LENGTH = 1024
MAX_COMPATIBILITY_LENGTH = 500
MAX_SKILL_LINES = 500

SKILLS_DIR = Path(__file__).resolve().parent.parent / "gumnut-photos" / "skills"


def parse_front_matter(text: str) -> dict | str:
    """Return the parsed front-matter mapping, or a message saying why it is invalid."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return "SKILL.md has no front matter"
    try:
        end = lines.index("---", 1)
    except ValueError:
        return "front matter is not closed with ---"
    try:
        fields = yaml.safe_load("\n".join(lines[1:end]))
    except yaml.YAMLError as error:
        return f"front matter is not valid YAML: {error}"
    if not isinstance(fields, dict):
        return "front matter must be a mapping of keys to values"
    return fields


def check_text_field(
    skill: str, fields: dict, key: str, max_length: int | None = None
) -> list[str]:
    value = fields.get(key)
    if not isinstance(value, str) or not value.strip():
        return [f"{skill}: {key} must be non-empty text"]
    if max_length is not None and len(value) > max_length:
        return [f"{skill}: {key} is {len(value)} characters (max {max_length})"]
    return []


def check_skill(skill_dir: Path) -> list[str]:
    skill = skill_dir.name
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        return [f"{skill}: missing SKILL.md"]

    text = skill_file.read_text(encoding="utf-8")
    fields = parse_front_matter(text)
    if isinstance(fields, str):
        return [f"{skill}: {fields}"]

    errors = []
    extra = sorted(str(key) for key in fields if key not in ALLOWED_KEYS)
    if extra:
        errors.append(f"{skill}: unsupported front-matter keys {extra}")

    name = fields.get("name")
    if name != skill:
        errors.append(f"{skill}: name {name!r} must match the folder name")
    if (
        not isinstance(name, str)
        or not NAME_PATTERN.match(name)
        or len(name) > MAX_NAME_LENGTH
    ):
        errors.append(
            f"{skill}: name must be lowercase letters, digits, and single "
            f"hyphens, at most {MAX_NAME_LENGTH} characters"
        )

    errors += check_text_field(skill, fields, "description", MAX_DESCRIPTION_LENGTH)
    if "compatibility" in fields:
        errors += check_text_field(
            skill, fields, "compatibility", MAX_COMPATIBILITY_LENGTH
        )
    if "license" in fields:
        errors += check_text_field(skill, fields, "license")
    if "metadata" in fields:
        metadata = fields["metadata"]
        if not isinstance(metadata, dict) or not all(
            isinstance(key, str) and isinstance(value, str)
            for key, value in metadata.items()
        ):
            errors.append(f"{skill}: metadata must map text keys to text values")

    line_count = len(text.splitlines())
    if line_count > MAX_SKILL_LINES:
        errors.append(
            f"{skill}: SKILL.md is {line_count} lines (max {MAX_SKILL_LINES}); "
            "move detail into supporting files"
        )
    return errors


def main() -> int:
    skill_dirs = (
        sorted(p for p in SKILLS_DIR.glob("*") if p.is_dir())
        if SKILLS_DIR.is_dir()
        else []
    )
    errors = [error for skill_dir in skill_dirs for error in check_skill(skill_dir)]
    for error in errors:
        print(f"error: {error}", file=sys.stderr)
    if not errors:
        print(f"Checked {len(skill_dirs)} skill(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
