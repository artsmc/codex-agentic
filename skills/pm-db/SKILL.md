---
name: pm-db
description: "Project management database for tracking specs, jobs, tasks, and execution. Use when Codex should run the converted pm-db workflow. Inputs: command."
---

# Pm Db

Converted Claude skill workflow for Codex/OpenAI use.

## Source

Converted from `skills/pm-db/SKILL.md`.

## Bundled Resources

Supporting files copied from the Claude source:

- `references/ACCEPTANCE_CRITERIA_VERIFICATION.md`
- `references/API_REFERENCE.md`
- `references/DEVELOPMENT.md`
- `references/DOCUMENTATION_REVIEW.md`
- `references/README.md`
- `references/SECURITY_AUDIT.md`
- `references/USER_GUIDE.md`
- `scripts`
- `assets/tests`
- `assets/migrations`
- `assets/prisma/schema.prisma`

## Converted Instructions

The content below was adapted from the Claude source. Rewrite tool and runtime assumptions as needed when they refer to Claude-only features.

## Codex Adaptation Notes

- The helper scripts in `scripts/` and SQL migrations in `assets/migrations/` are the primary portable parts of this skill.
- The original Claude setup used hooks for automatic tracking, but Codex does not run those automatically.
- Use this skill for explicit database setup, import, migration, and reporting tasks. Treat hook references as optional application integration work.

# pm-db Skill

Manage the project management database for tracking specifications, jobs, tasks, code reviews, and execution logs.

## Available Commands

### `init` - Initialize Database

Creates the projects.db database and runs all migrations.

```bash
$pm-db init
$pm-db init --reset  # Backup existing and create fresh database
```

### `import` - Import Specifications

Imports specifications from job-queue folders.

```bash
$pm-db import
$pm-db import --project auth  # Filter by project name
```

### `dashboard` - Show Dashboard

Displays project management dashboard with metrics.

```bash
$pm-db dashboard
$pm-db dashboard --format json
$pm-db dashboard --format markdown
```

### `migrate` - Run Migrations

Applies pending database migrations.

```bash
$pm-db migrate
$pm-db migrate --dry-run
$pm-db migrate --target-version 2
```

### `backup` - Backup Database

Creates a timestamped backup of the database (not yet implemented).

```bash
$pm-db backup
```

## Examples

```bash
# First-time setup
$pm-db init

# Import all specs
$pm-db import

# View dashboard
$pm-db dashboard

# Export to JSON
$pm-db dashboard --format json
```

## Database Location

Default: `~/.codex/projects.db`

## Hook Sources

The original Claude setup used hook scripts for automatic tracking, but they are not native Codex behavior.

## Schema

See `assets/migrations/` for the vendored SQL schema and `assets/prisma/schema.prisma` for the Prisma schema snapshot.

Tables:
- `projects` - Top-level projects
- `specs` - Specifications (FRD, FRS, GS, TR, task-list)
- `jobs` - Execution jobs
- `tasks` - Individual tasks within jobs
- `code_reviews` - Code review results
- `execution_logs` - Command execution logs
- `agent_assignments` - Agent work assignments
