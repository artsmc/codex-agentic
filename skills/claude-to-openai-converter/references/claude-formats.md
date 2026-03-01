# Claude Source Formats

Use this file to understand what the Claude artifacts mean before converting them.

## Files To Inspect

### `CLAUDE.md`

Treat this as persistent project guidance.

Key behaviors from Anthropic docs:
- Claude Code loads memory files automatically.
- `CLAUDE.md` can import other files with `@path`.
- Claude discovers `CLAUDE.md` files up the directory tree and also from relevant subtrees.

Conversion guidance:
- Move durable repo guidance into `AGENTS.md`.
- Inline imported content only when it is essential and concise.
- Replace Claude-specific commands and memory features with plain instructions that Codex can follow directly.

### `.claude/commands/*.md`

These are reusable prompt commands. The filename becomes the slash command name. The body is the prompt template. `$ARGUMENTS` and indexed argument placeholders may appear.

Conversion guidance:
- Usually convert these into Codex/OpenAI skills.
- Preserve the trigger phrase and expected arguments.
- Convert argument placeholders into explicit instructions in `SKILL.md`.

### `.claude/skills/*/SKILL.md`

Claude skills are prompt-based playbooks with optional frontmatter. They may run inline or in forked subagent context, and they can include supporting files.

Common Claude frontmatter you may encounter:
- `name`
- `description`
- `argument-hint`
- `disable-model-invocation`
- `user-invocable`
- `allowed-tools`
- `model`
- `context`
- `agent`
- `hooks`

Conversion guidance:
- Rebuild the skill in the Codex skill layout instead of copying fields mechanically.
- Keep trigger information in the `description`.
- Convert supporting files into `references/`, `scripts/`, or `assets/` as appropriate.

### `.claude/agents/*.md`

Claude subagents are markdown files with YAML frontmatter plus a markdown body that becomes the system prompt.

Common subagent fields:
- `name`
- `description`
- `tools`
- `disallowedTools`
- `model`
- `permissionMode`
- `maxTurns`
- `skills`
- `mcpServers`
- `hooks`
- `memory`
- `background`
- `isolation`

Conversion guidance:
- Do not force a one-to-one mapping into a Codex skill.
- Decide whether the artifact is really:
  - reusable instructions
  - repo guidance
  - or a runtime delegation design
- Features like memory, worktree isolation, and background execution usually need approximation or explicit application logic.

## Claude Features With No Clean Static Equivalent

Treat these as migration risks:
- automatic subagent delegation from descriptions
- separate context windows for subagents
- background subagent execution
- persistent subagent memory
- worktree isolation
- hooks tied to agent or skill lifecycle

When any of these are central to the source behavior, propose an Agents SDK or application-level orchestration target instead of only creating a static skill.

## Source Notes

This summary is based on Anthropic Claude Code documentation for memory, slash commands, skills, and subagents:
- https://code.claude.com/docs/en/skills
- https://code.claude.com/docs/en/sub-agents
- https://docs.anthropic.com/en/docs/claude-code/slash-commands
- https://docs.anthropic.com/en/docs/claude-code/memory
