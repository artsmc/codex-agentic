# Codex Agentic

Shareable skills for Codex/OpenAI workflows.

## Structure

- `skills/` - installable Codex skills
- `install.sh` - copy all repo skills into `~/.codex/skills`

## Included Skills

- `claude-to-openai-converter` - inventory Claude Code agents, commands, skills, and `CLAUDE.md` files, then convert them into the right OpenAI/Codex target

## Install With Codex

If Codex already has the system `skill-installer`, install directly from GitHub:

```bash
python3 ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo artsmc/codex-agentic \
  --path skills/claude-to-openai-converter
```

Restart Codex after installation.

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
- Add more shareable skills under `skills/<skill-name>/`.
