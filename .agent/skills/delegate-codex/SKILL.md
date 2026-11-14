---
name: delegate-codex
description: Delegate code review, bug investigation, second opinions, or isolated subtasks to OpenAI Codex CLI (`codex exec`) from Antigravity. Use when the user asks to consult, review with, or hand off a task to Codex.
---

# Delegate to Codex CLI (`codex exec`)

Use this skill when the user wants Antigravity to automatically invoke OpenAI Codex CLI as a sub-agent or reviewer.

## Pre-flight Check
1. Verify `codex` is installed and available on `PATH`:
   ```bash
   command -v codex
   ```
   If missing or not authenticated, inform the user to install/login (`codex login`) and stop.

## Execution Modes

### 1. Read-Only Review / Second Opinion / Bug Analysis (Default & Safest)
Use `--sandbox read-only` so Codex inspects the repo without modifying files while Antigravity retains write control:
```bash
codex exec --cd "<project_dir>" --sandbox read-only "Do not invoke agy or other AI CLIs. <specific_task_or_review_prompt>"
```

### 2. Implementation Handoff (Writes Allowed)
When delegating an implementation task to Codex:
- Do NOT edit the same files in parallel from Antigravity while Codex is running.
- Prefer isolating larger tasks in a separate git worktree if Antigravity will continue working concurrently.
- Run:
```bash
codex exec --cd "<project_dir>" --full-auto "Do not invoke agy or other AI CLIs. <specific_implementation_prompt>"
```

## Post-Execution Verification
1. Inspect Codex's stdout summary.
2. If Codex modified files, always review `git status` and `git diff`, and run the project's tests before accepting or committing the changes.
