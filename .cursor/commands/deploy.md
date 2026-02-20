### 🚀 **Cursor Command: deploy**

```yaml
name: deploy
description: Deploy commit to production using deploy_commit_to_prod.sh script
prompt: |
  Help the user deploy their code to production.
  
  **Task**
  Execute the deployment process:
  1. Switch to main branch (if needed)
  2. Pull latest changes from origin/main
  3. Find the commit SHA (use provided one, or latest on main if not provided)
  4. Run ./deploy_commit_to_prod.sh with the commit SHA
  5. Show deployment summary and wait for user confirmation
  6. Provide next steps after deployment
  
  **Steps to execute:**
  
  ```bash
  # 1. Ensure we're on main and up to date
  git checkout main
  git pull origin main
  
  # 2. Get commit SHA (use provided one, or latest on main)
  # If user provided commit SHA, use it
  # Otherwise, get latest: git log -1 --format="%H" main
  git log --oneline -5
  
  # 3. Run deploy script (will show detailed summary first)
  ./deploy_commit_to_prod.sh <COMMIT_SHA>
  ```
  
  **Script Behavior:**
  - If no commit SHA provided: Uses latest commit on main automatically
  - Shows detailed deployment summary including:
    - Commit information (SHA, author, date)
    - List of all commits to be deployed
    - Files changed (with status: Added/Modified/Deleted)
    - Commit description/body
  - Prompts for confirmation before proceeding
  - Creates production tag and pushes to origin
  
  **If user provides a commit SHA:**
  - Use that specific commit
  - Verify it exists and is on main branch
  
  **If no commit SHA provided:**
  - Use the latest commit on main
  - Show which commit will be deployed
  
  **Important:**
  - Script automatically switches to main branch if needed
  - Script verifies commit is on main branch before deploying
  - Script shows comprehensive summary BEFORE asking for confirmation
  - User must review the summary and confirm before deployment proceeds
  - After deployment, remind user to check CircleCI for deployment status
  - Remind user about post-deployment steps (manual UPDATEs, dbt seed, etc.)
  
  **Optional Flags:**
  - Use `--yes` or `-y` flag to skip confirmation (only if user explicitly requests)
  - Example: `./deploy_commit_to_prod.sh --yes <COMMIT_SHA>`

```

---
### ⚙️ **Usage in Cursor**
Once defined:
1. Make sure your PR is merged to main
2. Press **⌘ K → deploy** (or your custom shortcut)
3. Optionally provide a commit SHA, or let it use the latest commit
4. Cursor will:
   - Switch to main branch (if needed)
   - Pull latest changes
   - Show detailed deployment summary:
     - Commit info (SHA, author, date)
     - List of commits to be deployed
     - Files changed with status
     - Commit description
   - Wait for your confirmation
   - Execute the deployment script
   - Create production tag and push to origin
   - Provide deployment status and next steps

**Example:**
- `deploy` - Deploy latest commit on main
- `deploy c50547c3` - Deploy specific commit

---

