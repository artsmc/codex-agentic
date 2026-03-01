#!/usr/bin/env bash

set -euo pipefail

CODEX_HOME="${CODEX_HOME:-$HOME/.codex}"
SOURCE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
SKILLS_DIR="$SOURCE_DIR/skills"
DEST_DIR="$CODEX_HOME/skills"
FORCE="${1:-}"

mkdir -p "$DEST_DIR"

for skill_path in "$SKILLS_DIR"/*; do
  [ -d "$skill_path" ] || continue

  skill_name="$(basename "$skill_path")"
  target_path="$DEST_DIR/$skill_name"

  if [ -e "$target_path" ] && [ "$FORCE" != "--force" ]; then
    echo "Skipping $skill_name: $target_path already exists"
    continue
  fi

  rm -rf "$target_path"
  cp -R "$skill_path" "$target_path"
  echo "Installed $skill_name -> $target_path"
done

echo "Restart Codex to pick up new skills."
