# Codex Agentic

**A shareable Codex/OpenAI skill bundle with guided workflows, advanced orchestration patterns, specialist skills, and a full migration of `artsmc/claude-dev-agents`.**

[![Skills: 48](https://img.shields.io/badge/Skills-48-blue)](./skills/)
[![Workflows: 23](https://img.shields.io/badge/Workflow%20Skills-23-green)](./skills/)
[![Specialists: 24](https://img.shields.io/badge/Specialist%20Skills-24-orange)](./skills/)
[![Migration: Included](https://img.shields.io/badge/Claude%20Migration-Included-purple)](./reports/claude-dev-agents-migration.md)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow)](./LICENSE)

> Start with `feature-new`, build context with `document-hub-*` and `memorybank-*`, then move into `start-phase-*`, `pm-db`, and specialist skills for more advanced workflows.

## Quick Start

```bash
# Guided on-ramp
$feature-new "Add user authentication"

# Build project context
$document-hub-read
$memorybank-read

# Move into structured planning
$spec-plan
$start-phase-plan ./job-queue/feature-auth/task-list.md
```

**Recommended progression**

1. `feature-new` for the easiest end-to-end workflow.
2. `documentation-start`, `document-hub-*`, and `memorybank-*` for the context layer.
3. `spec-plan`, `spec-review`, and `pm-db` for planning and tracking.
4. `start-phase-plan`, `start-phase-execute`, and `remote-control-builder` for advanced orchestration.

## Why This Repo

- **Beginner-friendly entry point:** `feature-new` gives you a clear starting workflow instead of a pile of disconnected skills.
- **Context-first workflows:** `document-hub-*` and `memorybank-*` help build the project understanding the rest of the bundle expects.
- **Advanced orchestration:** `start-phase-*`, `pm-db`, and `remote-control-builder` preserve the higher-order workflow patterns from the Claude ecosystem.
- **Specialist depth:** skills like `api-designer`, `spec-writer`, `security-auditor`, and `python-reviewer` let you pull in focused expertise when needed.
- **Lean migration bundle:** the useful workflows, specialists, scripts, and schema assets were kept without carrying the full Claude runtime snapshot.

## What’s Included

### Guided workflows

- `feature-new`
- `feature-continue`
- `spec-plan`
- `spec-review`
- `pm-db`
- `start-phase-plan`
- `start-phase-execute`
- `start-phase-execute-team`
- `remote-control-builder`

### Context layer

- `documentation-start`
- `document-hub-initialize`
- `document-hub-read`
- `document-hub-analyze`
- `document-hub-update`
- `memorybank-initialize`
- `memorybank-read`
- `memorybank-sync`
- `memorybank-update`

### Specialist skills

- `api-designer`
- `spec-writer`
- `security-auditor`
- `python-reviewer`
- `technical-writer`
- `debugger-specialist`
- `devops-infrastructure`
- `database-schema-specialist`
- and more under [`skills/`](./skills/)

### Conversion tooling

- `claude-to-openai-converter` for translating Claude artifacts into Codex/OpenAI targets
- [`scripts/convert_claude_dev_agents.py`](./scripts/convert_claude_dev_agents.py) for batch migration work
- [`reports/claude-dev-agents-migration.md`](./reports/claude-dev-agents-migration.md) for the source-to-target mapping

## Learning Path

### Start here

Use these first if you want the smoothest onboarding:

- `feature-new` for the most approachable end-to-end workflow
- `documentation-start` to initialize the expected documentation systems
- `document-hub-read` to understand the current documentation hub
- `memorybank-read` to understand the current memory-bank state

### Then move here

Once you have context, use:

- `spec-plan` to generate specs and planning artifacts
- `spec-review` to review spec quality
- `pm-db` to initialize, migrate, import, and inspect project tracking

### Advanced layer

When you want more control or more automation:

- `start-phase-plan`
- `start-phase-execute`
- `start-phase-execute-team`
- `remote-control-builder`

## Installation

### Option 1: Clone and install the full bundle

```bash
git clone https://github.com/artsmc/codex-agentic.git ~/.codex/codex-agentic
bash ~/.codex/codex-agentic/install.sh
```

Restart Codex after installation.

### Option 2: Install a single skill with the Codex skill installer

If Codex already has the system `skill-installer`, install directly from GitHub:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo artsmc/codex-agentic \
  --path skills/feature-new
```

You can swap `skills/feature-new` for any other skill path in this repository.

Restart Codex after installation.

## Repository Layout

- [`skills/`](./skills/) - installable Codex skills
- [`reports/`](./reports/) - migration reports and mapping notes
- [`scripts/`](./scripts/) - migration and maintenance tooling
- [`install.sh`](./install.sh) - copy all repo skills into `~/.codex/skills`

## About The Migration

This repository does not just copy prompts. It preserves:

- migrated workflow skills
- migrated specialist-agent skills
- helper scripts, tests, migrations, and schema snapshots where they add value

The main caveat is that Codex does not have direct equivalents for every Claude runtime feature. Hooks, slash-command UX, and some orchestration behavior were translated into documentation notes or kept only where directly useful inside migrated skills.

See [`reports/claude-dev-agents-migration.md`](./reports/claude-dev-agents-migration.md) for the detailed mapping.

## Notes

- This repo intentionally excludes private Codex runtime state such as auth, logs, sessions, and SQLite files.
- When source names collide, the migration falls back to the source filename, for example `nextjs-code-reviewer` or `python-reviewer-2`.
- Add more shareable skills under `skills/<skill-name>/`.
