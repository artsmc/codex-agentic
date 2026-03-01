# OpenAI And Codex Targets

Use this file to choose the correct destination for converted Claude artifacts.

## Target 1: `AGENTS.md`

Use `AGENTS.md` for persistent repository instructions.

Good fits:
- coding conventions
- test and lint commands
- architecture notes
- workflow constraints
- review expectations

Notes:
- Keep it direct and operational.
- Remove product-specific references that only make sense in Claude Code.
- Prefer stable instructions over conversational framing.

## Target 2: Codex Skill

Use a Codex skill when the source is a reusable workflow or specialized body of instructions.

Expected layout:
- `SKILL.md`
- `agents/openai.yaml`
- optional `references/`
- optional `scripts/`
- optional `assets/`

Important local conventions:
- `SKILL.md` frontmatter should clearly state what the skill does and when to use it.
- `agents/openai.yaml` carries human-facing metadata such as `display_name`, `short_description`, and `default_prompt`.
- Detailed material should live in supporting files, not in an oversized `SKILL.md`.

Good fits:
- converted Claude commands
- converted Claude skills
- focused expert workflows
- repeatable migration helpers

## Target 3: Responses API Or Agents SDK Design

Use this when the source behavior requires runtime orchestration.

Good fits:
- explicit specialist handoffs
- programmatic tool calling
- application-managed state
- agent teams or multiple specialists with separate roles

OpenAI primitives to use:
- Responses API for agentic tool-calling loops
- function tools with JSON schemas
- built-in tools where appropriate
- Agents SDK when handoffs or traced agent workflows are central

Output should include:
- agent definitions or roles
- tool schemas
- handoff rules
- execution flow
- implementation notes for the host application

## Mapping Heuristics

Use these defaults:
- Claude repo memory -> `AGENTS.md`
- Claude slash command -> Codex skill
- Claude skill -> Codex skill
- Claude subagent with mostly prompt logic -> Codex skill plus optional `AGENTS.md`
- Claude subagent with true delegation/runtime behavior -> Agents SDK or Responses API design

## Non-Equivalent Areas

Flag these explicitly during migration:
- tool allowlists that depend on Claude-specific tool names
- forked context and background execution
- worktree isolation
- lifecycle hooks
- persistent agent memory

## Source Notes

This summary uses:
- local Codex skill conventions in `/home/mark/.codex/skills/.system/skill-creator`
- OpenAI API docs for function calling and Agents SDK
- OpenAI public Codex guidance about `AGENTS.md`

Useful references:
- https://platform.openai.com/docs/guides/gpt/function-calling
- https://platform.openai.com/docs/guides/agents-sdk/
- https://platform.openai.com/docs/guides/migrate-to-responses
- https://openai.com/index/introducing-codex/
- https://openai.com/business/guides-and-resources/how-openai-uses-codex/
