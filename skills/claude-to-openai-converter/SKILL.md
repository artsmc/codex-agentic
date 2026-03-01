---
name: claude-to-openai-converter
description: "Analyze Claude Code artifacts and convert them into the appropriate OpenAI target: Codex/OpenAI skills, AGENTS.md repository instructions, or API/Agents SDK tool-based agents. Use when a repo contains CLAUDE.md files, .claude/agents, .claude/skills, or .claude/commands and Codex should first inventory the source, produce a migration plan, identify non-equivalent features, and then implement a careful conversion."
---

# Claude To OpenAI Converter

Convert Claude Code memory files, skills, slash commands, and subagents into the closest OpenAI/Codex form without doing a blind syntax rewrite.

## Workflow

1. Inventory the Claude source before proposing edits.
Use `rg --files` to look for:
- `CLAUDE.md`
- `CLAUDE.local.md`
- `.claude/agents/*.md`
- `.claude/skills/**/SKILL.md`
- `.claude/commands/*.md`
- `.claude/settings.json`

2. Classify each artifact by behavior, not filename.
- Project guidance and working conventions usually map to `AGENTS.md`.
- Reusable prompt workflows usually map to a Codex/OpenAI skill.
- Tool-gated specialist behavior may map to a skill, to repo instructions, or to an Agents SDK handoff design.
- Claude-only features such as subagent memory, worktree isolation, background execution, or hooks may require approximation rather than direct conversion.

3. Produce a conversion plan before editing.
Include:
- Source inventory
- Proposed target for each source file
- Gaps or non-equivalent features
- Files to create or modify
- Validation steps

4. Convert incrementally.
Preserve intent, constraints, and trigger conditions. Rewrite structure for the target platform instead of copying Claude frontmatter fields verbatim.

5. Validate the result.
- For Codex skills, run the local skill validator.
- For repo instructions, check that the guidance is concise, actionable, and placed where Codex will discover it.
- For API-oriented output, ensure tools and handoffs are described as explicit tool-calling flows.

## Target Selection

Default to the smallest target that preserves behavior.

### Convert to `AGENTS.md`

Use `AGENTS.md` when the Claude source primarily describes:
- repository conventions
- architecture notes
- test commands
- review/checklist expectations
- coding style or workflow constraints

### Convert to a Codex/OpenAI skill

Use a skill when the Claude source is a reusable workflow with a clear trigger, such as:
- a custom slash command
- a Claude skill directory
- a specialized migration or analysis playbook
- a focused expert behavior that is mostly prompt-driven

When building a skill, keep `SKILL.md` concise and move detail into `references/`, `scripts/`, or `assets/` only when needed.

### Convert to an API or Agents SDK design

Use this path when the Claude source depends on runtime orchestration rather than static prompt instructions, such as:
- explicit agent handoffs
- multiple specialists with separate contexts
- structured tool-calling requirements
- application-managed state or tool outputs

In that case, produce:
- agent role definitions
- tool schemas
- handoff rules
- a short implementation plan for Responses API or Agents SDK integration

## Mapping Rules

Read [claude-formats.md](references/claude-formats.md) and [openai-targets.md](references/openai-targets.md) before converting unfamiliar constructs.

Use this default mapping:
- `CLAUDE.md` -> `AGENTS.md`
- `.claude/commands/*.md` -> a Codex skill, unless it is just general project guidance
- `.claude/skills/*/SKILL.md` -> a Codex skill with rewritten frontmatter and resource layout
- `.claude/agents/*.md` -> either a Codex skill plus `AGENTS.md` guidance, or an Agents SDK design if true agent delegation is required

Do not assume a Claude subagent always becomes an OpenAI skill. Separate-context delegation is often a runtime concern, not a static skill concern.

## Output Contract

Before making edits, present a compact plan with these headings:
- `Inventory`
- `Target mapping`
- `Conversion plan`
- `Open questions`

After the plan, implement the conversion unless a major target ambiguity makes that risky.

When reporting non-equivalences, be explicit:
- what Claude feature exists
- whether OpenAI/Codex has a direct equivalent
- what approximation you are using
- what behavior is lost or moved into application code

## Implementation Notes

- Prefer preserving semantics over preserving filenames.
- Keep descriptions trigger-oriented. They are the main activation mechanism for skills and subagents.
- If converting to a Codex skill, include `agents/openai.yaml` metadata that matches the skill.
- If converting to `AGENTS.md`, compress guidance and remove Claude-specific UI references like `/memory` or `/agents`.
- If converting to API tools, express Claude capabilities as explicit tool schemas and tool-call loops.

## References

- Claude source formats: [claude-formats.md](references/claude-formats.md)
- OpenAI/Codex targets: [openai-targets.md](references/openai-targets.md)
- Conversion checklist: [conversion-checklist.md](references/conversion-checklist.md)
