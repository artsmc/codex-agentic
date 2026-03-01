# Codex Agentic

Shareable Codex/OpenAI skills, plus full-source migrations of Claude-oriented agent bundles.

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
