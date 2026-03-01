#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path

import yaml

RUNTIME_DIRS = ["hooks", "bin", "lib", "migrations", "prisma", "scripts", "tests", "docs", "sounds", "test-caching"]


def load_frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text()
    if not text.startswith("---\n"):
        return {}, text
    _, remainder = text.split("---\n", 1)
    frontmatter_text, body = remainder.split("\n---\n", 1)
    try:
        data = yaml.safe_load(frontmatter_text) or {}
    except yaml.YAMLError:
        data = {}
        for line in frontmatter_text.splitlines():
            if ":" not in line:
                continue
            key, value = line.split(":", 1)
            key = key.strip()
            value = value.strip().strip('"').strip("'")
            if key in {"name", "description", "model", "color"}:
                data[key] = value
    return data, body.strip() + "\n"


def titleize(name: str) -> str:
    return " ".join(part.capitalize() for part in name.replace("_", "-").split("-"))


def short_description(text: str) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) <= 64:
        return text
    return text[:61].rstrip() + "..."


def clean_description(text: str) -> str:
    text = text.replace("\\n", " ")
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\*\*", "", text)
    text = re.sub(r"\s+", " ", text).strip()
    if " Invoke this agent whenever:" in text:
        text = text.split(" Invoke this agent whenever:", 1)[0].strip()
    if " Example 1 " in text:
        text = text.split(" Example 1 ", 1)[0].strip()
    return text


def yaml_string(text: str) -> str:
    normalized = clean_description(text)
    escaped = normalized.replace("\\", "\\\\").replace('"', '\\"')
    return f'"{escaped}"'


def rewrite_body(body: str, known_skill_names: set[str], known_agent_names: set[str]) -> str:
    body = body.replace("~/.claude", "~/.codex")
    body = body.replace("Claude Code", "Codex")
    body = body.replace("Use Read tool", "Read")
    body = body.replace("AskUserQuestion", "ask the user")
    body = body.replace("Skill tool:", "Invoke the corresponding skill:")
    body = body.replace("Use the Skill tool to invoke", "Invoke the corresponding skill")
    body = body.replace("Then use the Skill tool to invoke", "Then invoke")
    body = body.replace("Task tool", "delegation workflow")
    body = body.replace("uses Task tool to invoke", "invokes")
    body = body.replace("subagent_type=", "skill=")
    body = body.replace("cline-docs", "documentation hub directory")
    body = body.replace("/home/artsmc/.claude/documentation hub directory/", "documentation hub directory/")
    body = body.replace("`/memorybank sync`", "`$memorybank-sync`")
    body = body.replace("/memorybank sync", "$memorybank-sync")
    body = body.replace("Use Glob tool:", "Use `rg --files` or globbing:")
    body = body.replace("Use Glob tool", "Use `rg --files` or globbing")
    body = body.replace("Use Grep tool", "Use `rg`")
    body = body.replace("Use Read tool", "Read")
    body = body.replace("Invoke the corresponding Codex skill", "Invoke")

    for name in sorted(known_skill_names, key=len, reverse=True):
        body = body.replace(f"/{name}", f"${name}")
        body = body.replace(f'"claude-dev-{name}"', f'"{name}"')
        body = body.replace(f"$claude-dev-{name}", f"${name}")

    for name in sorted(known_agent_names, key=len, reverse=True):
        body = body.replace(f"{name} agent", f"`{name}` skill")
        body = body.replace(f'"claude-agent-{name}"', f'"{name}"')
        body = body.replace(f"$claude-agent-{name}", f"${name}")

    body = body.replace("Invoke the corresponding skill:", "Invoke:")
    body = body.replace("Invoke the corresponding skill", "Invoke")
    body = body.replace("delegation workflow with subagent_type", "delegation workflow with skill")
    body = body.replace("use the host application or another Codex session", "use another Codex session or perform the work directly")

    return body


def ensure_clean_dir(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def copy_supporting_files(source_dir: Path, dest_dir: Path) -> list[str]:
    copied: list[str] = []
    for item in sorted(source_dir.iterdir()):
        if item.name == "SKILL.md":
            continue
        if item.is_symlink():
            copied.append(f"SKIPPED_SYMLINK:{item.name}")
            continue
        if item.is_dir():
            if item.name == "scripts":
                target = dest_dir / "scripts"
            elif item.name == "references":
                target = dest_dir / "references"
            else:
                target = dest_dir / "assets" / item.name
            shutil.copytree(item, target, dirs_exist_ok=True, symlinks=True, ignore_dangling_symlinks=True)
            copied.append(str(target.relative_to(dest_dir)))
            continue
        if item.suffix.lower() in {".py", ".sh"}:
            target_dir = dest_dir / "scripts"
        elif item.suffix.lower() == ".md":
            target_dir = dest_dir / "references"
        else:
            target_dir = dest_dir / "assets"
        target_dir.mkdir(parents=True, exist_ok=True)
        target = target_dir / item.name
        shutil.copy2(item, target, follow_symlinks=False)
        copied.append(str(target.relative_to(dest_dir)))
    return copied


def copy_pmdb_runtime_assets(source_root: Path, dest_dir: Path) -> list[str]:
    copied: list[str] = []
    migrations_source = source_root / "migrations"
    if migrations_source.exists():
        migrations_target = dest_dir / "assets" / "migrations"
        shutil.copytree(
            migrations_source,
            migrations_target,
            dirs_exist_ok=True,
            symlinks=True,
            ignore_dangling_symlinks=True,
        )
        copied.append(str(migrations_target.relative_to(dest_dir)))

    prisma_schema = source_root / "prisma" / "schema.prisma"
    if prisma_schema.exists():
        prisma_target_dir = dest_dir / "assets" / "prisma"
        prisma_target_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy2(prisma_schema, prisma_target_dir / prisma_schema.name)
        copied.append(str((prisma_target_dir / prisma_schema.name).relative_to(dest_dir)))

    return copied


def build_skill_markdown(
    name: str,
    description: str,
    overview: str,
    source_path: Path,
    body: str,
    copied_files: list[str],
) -> str:
    lines = [
        "---",
        f"name: {name}",
        f"description: {yaml_string(description)}",
        "---",
        "",
        f"# {titleize(name)}",
        "",
        overview,
        "",
        "## Source",
        "",
        f"Converted from `{source_path}`.",
        "",
    ]
    if copied_files:
        lines.extend(
            [
                "## Bundled Resources",
                "",
                "Supporting files copied from the Claude source:",
                "",
            ]
        )
        for rel in copied_files:
            lines.append(f"- `{rel}`")
        lines.append("")

    lines.extend(
        [
            "## Converted Instructions",
            "",
            "The content below was adapted from the Claude source. Rewrite tool and runtime assumptions as needed when they refer to Claude-only features.",
            "",
            body.rstrip(),
            "",
        ]
    )
    return "\n".join(lines)


def write_openai_yaml(dest_dir: Path, display_name: str, description: str, skill_name: str) -> None:
    agents_dir = dest_dir / "agents"
    agents_dir.mkdir(parents=True, exist_ok=True)
    content = "\n".join(
        [
            "interface:",
            f"  display_name: {yaml_string(display_name)}",
            f"  short_description: {yaml_string(short_description(description))}",
            f"  default_prompt: {yaml_string(f'Use ${skill_name} for this workflow.')}",
            "",
        ]
    )
    (agents_dir / "openai.yaml").write_text(content)


def unique_dest_name(prefix: str, preferred_name: str, fallback_name: str, used_names: set[str]) -> str:
    candidate = f"{prefix}{preferred_name}"
    if candidate not in used_names:
        used_names.add(candidate)
        return candidate
    candidate = f"{prefix}{fallback_name}"
    if candidate not in used_names:
        used_names.add(candidate)
        return candidate
    index = 2
    while True:
        candidate = f"{prefix}{fallback_name}-{index}"
        if candidate not in used_names:
            used_names.add(candidate)
            return candidate
        index += 1


def convert_skill(
    source_dir: Path,
    dest_root: Path,
    known_skill_names: set[str],
    known_agent_names: set[str],
    used_names: set[str],
) -> tuple[str, str]:
    source_skill = source_dir / "SKILL.md"
    frontmatter, body = load_frontmatter(source_skill)
    source_name = frontmatter.get("name", source_dir.name)
    dest_name = unique_dest_name("", source_name, source_dir.name, used_names)
    dest_dir = dest_root / "skills" / dest_name
    ensure_clean_dir(dest_dir)

    copied_files = copy_supporting_files(source_dir, dest_dir)
    if source_name == "pm-db":
        copied_files.extend(copy_pmdb_runtime_assets(source_dir.parent.parent, dest_dir))
    description = clean_description(frontmatter.get("description", f"Converted Claude skill for {source_name}"))
    args = frontmatter.get("args")
    if args:
        description = f"{description}. Use when Codex should run the converted {source_name} workflow. Inputs: {', '.join(args.keys())}."
    else:
        description = f"{description}. Use when Codex should run the converted {source_name} workflow."

    rewritten = rewrite_body(body, known_skill_names, known_agent_names)
    skill_md = build_skill_markdown(
        dest_name,
        description,
        "Converted Claude skill workflow for Codex/OpenAI use.",
        source_skill.relative_to(source_dir.parent.parent),
        rewritten,
        copied_files,
    )
    (dest_dir / "SKILL.md").write_text(skill_md)
    write_openai_yaml(dest_dir, titleize(dest_name), description, dest_name)
    return source_name, dest_name


def convert_agent(
    source_file: Path,
    dest_root: Path,
    known_skill_names: set[str],
    known_agent_names: set[str],
    used_names: set[str],
) -> tuple[str, str]:
    frontmatter, body = load_frontmatter(source_file)
    source_name = frontmatter.get("name", source_file.stem)
    dest_name = unique_dest_name("", source_name, source_file.stem, used_names)
    dest_dir = dest_root / "skills" / dest_name
    ensure_clean_dir(dest_dir)

    description = clean_description(frontmatter.get("description", f"Converted Claude specialist agent for {source_name}"))
    description = f"{description}. Use when Codex needs this specialist perspective or review style."
    rewritten = rewrite_body(body, known_skill_names, known_agent_names)
    skill_md = build_skill_markdown(
        dest_name,
        description,
        "Converted specialist prompt from a Claude agent into a Codex skill.",
        source_file.relative_to(source_file.parent.parent),
        rewritten,
        [],
    )
    (dest_dir / "SKILL.md").write_text(skill_md)
    write_openai_yaml(dest_dir, titleize(dest_name), description, dest_name)
    return source_name, dest_name


def write_report(dest_root: Path, skill_map: list[tuple[str, str]], agent_map: list[tuple[str, str]]) -> None:
    report_dir = dest_root / "reports"
    report_dir.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Claude Dev Agents Migration Report",
        "",
        "## Inventory",
        "",
        f"- Claude skills converted: {len(skill_map)}",
        f"- Claude agents converted: {len(agent_map)}",
        "- Claude runtime and hook directories vendored under `imports/claude-dev-agents/` for reference",
        "",
        "## Target Mapping",
        "",
        "- `skills/*/SKILL.md` -> Codex skills using the original skill name where possible",
        "- `agents/*.md` -> specialist Codex skills using the original agent name or filename on collision",
        "- Claude hooks and orchestration runtime -> vendored under `imports/claude-dev-agents/` and documented as non-equivalent/manual follow-up",
        "",
        "## Converted Skills",
        "",
    ]
    for source_name, dest_name in skill_map:
        lines.append(f"- `{source_name}` -> `{dest_name}`")
    lines.extend(["", "## Converted Agents", ""])
    for source_name, dest_name in agent_map:
        lines.append(f"- `{source_name}` -> `{dest_name}`")
    lines.extend(
        [
            "",
            "## Non-Equivalent Features",
            "",
            "- Claude slash-command UX was approximated with explicit Codex skill invocation via `$skill-name`.",
            "- Claude hooks were vendored as source material, but Codex skills do not have a direct lifecycle hook system.",
            "- Multi-agent runtime orchestration, prompt caching, and PM-DB automation were preserved as source assets under `imports/claude-dev-agents/`, but remain application-level concerns rather than static skill features.",
            "",
        ]
    )
    (report_dir / "claude-dev-agents-migration.md").write_text("\n".join(lines))


def copy_runtime_dirs(source_root: Path, dest_root: Path) -> None:
    imports_root = dest_root / "imports" / "claude-dev-agents"
    imports_root.mkdir(parents=True, exist_ok=True)
    for filename in ["README.md", ".gitignore", "prisma.config.ts"]:
        source_file = source_root / filename
        if source_file.exists():
            shutil.copy2(source_file, imports_root / filename)
    for dirname in RUNTIME_DIRS:
        source = source_root / dirname
        if not source.exists():
            continue
        target = imports_root / dirname
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(source, target, symlinks=True, ignore_dangling_symlinks=True)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--dest", required=True)
    args = parser.parse_args()

    source_root = Path(args.source)
    dest_root = Path(args.dest)

    source_skill_dirs = sorted(path.parent for path in (source_root / "skills").glob("*/SKILL.md"))
    source_agent_files = sorted((source_root / "agents").glob("*.md"))
    known_skill_names = {path.name for path in source_skill_dirs}
    known_agent_names = {path.stem for path in source_agent_files}
    used_names: set[str] = {"claude-to-openai-converter"}

    skill_map = [convert_skill(path, dest_root, known_skill_names, known_agent_names, used_names) for path in source_skill_dirs]
    agent_map = [convert_agent(path, dest_root, known_skill_names, known_agent_names, used_names) for path in source_agent_files]
    copy_runtime_dirs(source_root, dest_root)
    write_report(dest_root, skill_map, agent_map)


if __name__ == "__main__":
    main()
