---
name: deploy
description: Deploy a commit to production using deploy_commit_to_prod.sh. Switches to main, pulls latest, runs the deploy script, and waits for confirmation before proceeding.
disable-model-invocation: true
argument-hint: "[commit_sha]"
---

Help deploy code to production using `deploy_commit_to_prod.sh`.

**Arguments:** Optionally pass a commit SHA — e.g. `/deploy c50547c3`. If none provided, uses the latest commit on main.

**Steps to execute:**

```bash
# 1. Ensure on main and up to date
git checkout main
git pull origin main

# 2. Show recent commits
git log --oneline -5

# 3. Run deploy script
# If $ARGUMENTS provided: ./deploy_commit_to_prod.sh $ARGUMENTS
# Otherwise: ./deploy_commit_to_prod.sh $(git log -1 --format="%H" main)
```

**Script behavior:**
- Shows detailed deployment summary before any action: commit info (SHA, author, date), list of commits to deploy, files changed (Added/Modified/Deleted), commit description.
- Prompts for confirmation before proceeding.
- Creates production tag and pushes to origin.

**If commit SHA provided (`/deploy <sha>`):**
- Use that specific commit.
- Verify it exists and is on main branch.

**If no commit SHA provided:**
- Use the latest commit on main.
- Show which commit will be deployed.

**After deployment:**
- Remind user to check CircleCI for deployment status.
- Remind user about post-deployment steps (manual UPDATEs, dbt seed, etc.).

**Optional flag:** Use `--yes` / `-y` only if user explicitly requests skipping confirmation.
Example: `./deploy_commit_to_prod.sh --yes <COMMIT_SHA>`

**Important:** Always show the deployment summary and wait for user confirmation before executing.
