---
name: run_dap
description: Execute the complete monthly DAP (Declaring AP) run — branch checkout, environment setup, dependency cloning, seeds, and model execution.
disable-model-invocation: true
argument-hint: "[run for YYYY-MM-DD] [on branch-name]"
---

Execute the complete monthly DAP run. Accepts optional arguments via `$ARGUMENTS`:
- Custom report month: "run for 2025-10-01"
- Custom branch: "run on branch-name"
- Both: "run for 2025-10-01 on my-branch"

**Configuration (defaults):**
- `REPORT_MONTH`: 2025-11-01
- `BRANCH`: damezquita_EB-313255-3-staging-layer-creation
- `USERNAME`: current user (`whoami`)

**Script to execute:**

```bash
# Configuration
USERNAME="${USERNAME:-$(whoami)}"
REPORT_MONTH="${REPORT_MONTH:-2025-11-01}"
BRANCH="${BRANCH:-damezquita_EB-313255-3-staging-layer-creation}"

PROJECT_ROOT="/Users/${USERNAME}/Documents/GitHub/analytics-engineering-data-pipelines/docker/dbtae/dbtae"
REPO_ROOT="/Users/${USERNAME}/Documents/GitHub/analytics-engineering-data-pipelines"

# Checkout branch (from main)
cd "${REPO_ROOT}"
git checkout "${BRANCH}"

# Environment setup
source ~/.virtualenvs/dbt_scripts/bin/activate
cd "${PROJECT_ROOT}"
export SNOWFLAKE_WAREHOUSE=DEV_2X-LARGE
export DBTAE="${PROJECT_ROOT}"

# Step 1: Clone source tables (required for stg_charges_credits and payout models)
echo 'Y' | python scripts/clone.py \
  --select "source:eb.invoice_charges source:eb_history.history_payouts" \
  --resource-type source \
  --project-directory "${PROJECT_ROOT}"

# Step 2: Clone f_order_itemization dependencies
echo 'Y' | python scripts/clone.py \
  --select "+f_order_itemization" \
  --project-directory "${PROJECT_ROOT}"

# Step 3: Clone f_dap dependencies (excluding DAP models built locally)
echo 'Y' | python scripts/clone.py \
  --select "+f_dap" \
  --exclude "path:models/marts/accounting/declaring_ap_datamart seed*" \
  --resource-type "model source" \
  --project-directory "${PROJECT_ROOT}"

# Run seeds
dbt seed \
  --select "seed_dap*" \
  --project-dir "${PROJECT_ROOT}" \
  --profiles-dir "${PROJECT_ROOT}"

# Run models
dbt run \
  --select "path:models/marts/accounting/declaring_ap_datamart" \
  --exclude "oct_dap oct_dap_hardcoded" \
  --vars "{\"report_month\": \"${REPORT_MONTH}\"}" \
  --project-dir "${PROJECT_ROOT}" \
  --profiles-dir "${PROJECT_ROOT}"
```

Execute step by step, showing progress and any errors that occur.
