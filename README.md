# Codex Agentic

Shareable Codex/OpenAI skills, plus full-source migrations of Claude-oriented agent bundles.

## Start Here

The easiest way to approach this repo is:

1. Start with a guided workflow like `feature-new`.
2. Set up project context with `documentation-start`, `document-hub-*`, and `memorybank-*`.
3. Move to focused planning and review skills like `spec-plan`, `spec-review`, and `pm-db`.
4. Graduate to the more advanced orchestration skills like `start-phase-plan`, `start-phase-execute`, and `remote-control-builder`.

If you are trying to understand the bundle quickly, treat `feature-new` as the on-ramp, `document-hub-*` and `memorybank-*` as the context layer, and the `start-phase-*` skills as the advanced layer.

## Structure

- `skills/` - installable Codex skills
- `scripts/convert_claude_dev_agents.py` - batch converter used to migrate `artsmc/claude-dev-agents`
- `reports/` - migration reports and mapping notes
- `imports/claude-dev-agents/` - vendored Claude runtime assets kept for reference
- `install.sh` - copy all repo skills into `~/.codex/skills`

## Included Skills

- `claude-to-openai-converter` - inventory Claude Code agents, commands, skills, and `CLAUDE.md` files, then convert them into the right OpenAI/Codex target
- original workflow names such as `feature-new`, `spec-plan`, `pm-db`, and `start-phase-plan`
- original specialist names such as `api-designer`, `spec-writer`, `security-auditor`, and `python-reviewer`

When source names collide, the conversion falls back to the source filename, for example `nextjs-code-reviewer` or `python-reviewer-2`.

## Recommended Path

### Getting Started

Use these first:

- `feature-new` - the most approachable end-to-end workflow
- `documentation-start` - initialize the documentation systems expected by the wider workflow
- `document-hub-read` - quickly understand the current documentation hub
- `memorybank-read` - quickly understand the current memory-bank state

### Context and Documentation

Use these to create and maintain project context:

- `document-hub-initialize`
- `document-hub-read`
- `document-hub-analyze`
- `document-hub-update`
- `memorybank-initialize`
- `memorybank-read`
- `memorybank-sync`
- `memorybank-update`

These skills are the context backbone for the planning and execution workflows.

### Planning and Tracking

Use these once the documentation layer is in place:

- `spec-plan` - generate specs and planning artifacts
- `spec-review` - review the quality of those specs
- `pm-db` - inspect or manage the project-management database layer explicitly

### Advanced Workflows

Use these once you want more control or more automation:

- `start-phase-plan` - break work into waves and execution phases
- `start-phase-execute` - run structured execution with quality gates and PM-DB tracking
- `start-phase-execute-team` - team-oriented execution variant
- `remote-control-builder` - higher-complexity orchestration workflow

### Specialist Skills

When you need focused expertise, reach for the migrated specialist skills such as:

- `api-designer`
- `spec-writer`
- `security-auditor`
- `python-reviewer`
- `technical-writer`

## Included Imports

The repo also vendors the non-portable parts of `artsmc/claude-dev-agents` under `imports/claude-dev-agents/`, including:

- `hooks/`
- `bin/`
- `lib/`
- `migrations/`
- `prisma/`
- `scripts/`
- `tests/`
- `docs/`
- `sounds/`
- `test-caching/`

These are kept as source material because Codex skills do not have direct equivalents for Claude hooks, slash-command UX, or the original runtime orchestration.

## Install With Codex

If Codex already has the system `skill-installer`, install directly from GitHub.

Example for one skill:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo artsmc/codex-agentic \
  --path skills/claude-to-openai-converter
```

Restart Codex after installation.

To install the whole bundle from a clone, use `install.sh`.

## Install From A Clone

```bash
git clone https://github.com/artsmc/codex-agentic.git ~/.codex/codex-agentic
bash ~/.codex/codex-agentic/install.sh
```

Restart Codex after installation.

## Create The GitHub Repo

From this directory:

```bash
cd ~/.codex/codex-agentic
git add .
git commit -m "Initial Codex skill repo"
gh repo create codex-agentic --public --source=. --remote=origin --push
```

## Notes

- This repo intentionally excludes private Codex runtime state such as auth, logs, sessions, and SQLite files.
- The `artsmc/claude-dev-agents` migration report lives at `reports/claude-dev-agents-migration.md`.
- Add more shareable skills under `skills/<skill-name>/`.
