# Claude Dev Agents Migration Report

## Inventory

- Claude skills converted: 23
- Claude agents converted: 24
- Claude runtime and hook directories were reviewed during migration, but the raw imported snapshot is no longer included

## Target Mapping

- `skills/*/SKILL.md` -> Codex skills using the original skill name where possible
- `agents/*.md` -> specialist Codex skills using the original agent name or filename on collision
- Claude hooks and orchestration runtime -> documented as non-equivalent/manual follow-up

## Converted Skills

- `architecture-quality-assess` -> `architecture-quality-assess`
- `code-duplication` -> `code-duplication`
- `document-hub-analyze` -> `document-hub-analyze`
- `document-hub-initialize` -> `document-hub-initialize`
- `document-hub-read` -> `document-hub-read`
- `document-hub-update` -> `document-hub-update`
- `documentation-start` -> `documentation-start`
- `feature-continue` -> `feature-continue`
- `feature-new` -> `feature-new`
- `mastra-dev` -> `mastra-dev`
- `memorybank-initialize` -> `memorybank-initialize`
- `memorybank-read` -> `memorybank-read`
- `memorybank-sync` -> `memorybank-sync`
- `memorybank-update` -> `memorybank-update`
- `new-product` -> `new-product`
- `pm-db` -> `pm-db`
- `remote-control-builder` -> `remote-control-builder`
- `security-quality-assess` -> `security-quality-assess`
- `spec-plan` -> `spec-plan`
- `spec-review` -> `spec-review`
- `start-phase-execute` -> `start-phase-execute`
- `start-phase-execute-team` -> `start-phase-execute-team`
- `start-phase-plan` -> `start-phase-plan`

## Converted Agents

- `accessibility-specialist` -> `accessibility-specialist`
- `api-designer` -> `api-designer`
- `code-reviewer` -> `code-reviewer`
- `database-schema-specialist` -> `database-schema-specialist`
- `debugger-specialist` -> `debugger-specialist`
- `devops-infrastructure` -> `devops-infrastructure`
- `front-end-developer` -> `front-end-developer`
- `frontend-developer` -> `frontend-developer`
- `mastra-core-developer` -> `mastra-core-developer`
- `nextjs-backend-developer` -> `nextjs-backend-developer`
- `code-reviewer` -> `nextjs-code-reviewer`
- `qa-engineer` -> `qa-engineer`
- `qa-engineer` -> `nextjs-qa-engineer`
- `python-fastapi-expert` -> `python-fastapi-expert`
- `python-fastapi-expert` -> `python-fastapi-expert-2`
- `python-reviewer` -> `python-reviewer`
- `python-reviewer` -> `python-reviewer-2`
- `python-tester` -> `python-tester`
- `python-tester` -> `python-tester-2`
- `refactoring-specialist` -> `refactoring-specialist`
- `security-auditor` -> `security-auditor`
- `spec-writer` -> `spec-writer`
- `technical-writer` -> `technical-writer`
- `ui-developer` -> `ui-developer`

## Non-Equivalent Features

- Claude slash-command UX was approximated with explicit Codex skill invocation via `$skill-name`.
- Claude hooks do not have a direct Codex lifecycle equivalent.
- Multi-agent runtime orchestration, prompt caching, and PM-DB automation remain application-level concerns rather than static skill features.
