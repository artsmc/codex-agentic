---
name: documentation-start
description: "Initialize Memory Bank and Document Hub if not already set up. Use when Codex should run the converted documentation-start workflow. Inputs: force."
---

# Documentation Start

Converted Claude skill workflow for Codex/OpenAI use.

## Source

Converted from `skills/documentation-start/SKILL.md`.

## Converted Instructions

The content below was adapted from the Claude source. Rewrite tool and runtime assumptions as needed when they refer to Claude-only features.

# documentation-start Skill

Initialize project documentation systems (Memory Bank + Document Hub) if needed.

## Usage

```bash
$claude-dev-documentation-start           # Initialize if needed
$claude-dev-documentation-start --force   # Force re-initialization
```

## What It Does

1. **Check Memory Bank Status**
   - Check if `memory-bank/` directory exists
   - Check if all 6 core files present:
     - projectbrief.md
     - productContext.md
     - techContext.md
     - systemPatterns.md
     - activeContext.md
     - progress.md

2. **Check Document Hub Status**
   - Check if `cline-docs/` directory exists
   - Check if all 4 core files present:
     - systemArchitecture.md
     - keyPairResponsibility.md
     - glossary.md
     - techStack.md

3. **Initialize If Needed**
   - If Memory Bank missing → Call `$claude-dev-memory-bank-initialize`
   - If Document Hub missing → Call `$claude-dev-document-hub-initialize`
   - If both exist → Report "Already initialized ✅"

4. **Force Mode**
   - If `--force` flag provided:
     - Always call both initialize skills
     - Overwrites existing files

## Workflow Logic

```
START
  ↓
Check memory-bank/ exists?
  ├─ NO → Call $claude-dev-memory-bank-initialize
  └─ YES → Validate 6 files present
      ├─ Valid → Skip Memory Bank ✅
      └─ Invalid → Call $claude-dev-memory-bank-initialize
  ↓
Check cline-docs/ exists?
  ├─ NO → Call $claude-dev-document-hub-initialize
  └─ YES → Validate 4 files present
      ├─ Valid → Skip Document Hub ✅
      └─ Invalid → Call $claude-dev-document-hub-initialize
  ↓
Report initialization status
  ↓
END
```

## Output

```
🔍 Checking documentation systems...

Memory Bank:
  ✅ Already initialized (6/6 files present)

Document Hub:
  ⚠️ Not initialized
  🚀 Initializing Document Hub...
  ✅ Document Hub initialized (4/4 files created)

📊 Summary:
  Memory Bank: ✅ Ready
  Document Hub: ✅ Ready

Next steps:
  - Run $claude-dev-feature-new to start a new feature
  - Or use individual skills as needed
```

## When to Use

- **First time in a project**: Always run this first
- **New team members**: Ensures documentation is initialized
- **After cloning repository**: Sets up local documentation
- **Force re-init**: Use `--force` to rebuild documentation

## Implementation Details

This skill uses the Skill tool to invoke:
- `$claude-dev-memory-bank-initialize` (if needed)
- `$claude-dev-document-hub-initialize` (if needed)

No direct file manipulation - delegates to existing skills.
