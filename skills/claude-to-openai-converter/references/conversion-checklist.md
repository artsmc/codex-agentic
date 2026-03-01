# Conversion Checklist

Use this checklist for each migration.

## 1. Inventory

- Find all Claude-specific files.
- Note whether each file is project-level, user-level, or nested in a subtree.
- Record imported files or supporting assets that affect behavior.

## 2. Classify

- Is this guidance, a reusable workflow, or a runtime agent?
- Does it depend on Claude-only features?
- Is the best OpenAI target `AGENTS.md`, a Codex skill, or an API/SDK design?

## 3. Plan

- List source files and destination files.
- Note non-equivalent features.
- Identify missing information or user decisions.
- Decide validation steps before editing.

## 4. Convert

- Rewrite for the target format.
- Preserve intent and constraints.
- Keep trigger descriptions explicit.
- Move bulky detail into supporting files.

## 5. Validate

- Validate skill folders when creating Codex skills.
- Sanity-check that `AGENTS.md` guidance is concise and repo-specific.
- For API output, verify tool schemas and handoff logic are concrete.

## 6. Report

Report:
- what was converted
- what target each source mapped to
- what required approximation
- what still needs human decision or app-level implementation
