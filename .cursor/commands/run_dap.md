### 🚀 **Cursor Command: run_dap**

```yaml
name: run_dap
description: Execute the complete monthly DAP (Declaring AP) run including branch checkout, cloning dependencies, running seeds, and executing models.
prompt: |
  Execute the complete monthly DAP run script. This command will:
  1. Checkout the specified branch (defaults to damezquita_EB-313255-3-staging-layer-creation)
  2. Set up the virtual environment, warehouse, and DBTAE environment variable
  3. Clone source tables (invoice_charges, history_payouts)
  4. Clone f_order_itemization dependencies
  5. Clone f_dap dependencies (excluding DAP models themselves)
  6. Run DAP seeds
  7. Run all DAP models for the specified report month
  
  Configuration variables:
  - USERNAME: defaults to current user
  - REPORT_MONTH: defaults to 2025-11-01 (format: YYYY-MM-DD)
  - BRANCH: defaults to damezquita_EB-313255-3-staging-layer-creation
  
  Execute the following script:
  
  ```bash
  # Configuration
  USERNAME="${USERNAME:-$(whoami)}"
  REPORT_MONTH="${REPORT_MONTH:-2025-11-01}"
  BRANCH="${BRANCH:-damezquita_EB-313255-3-staging-layer-creation}"
  
  PROJECT_ROOT="/Users/${USERNAME}/Documents/GitHub/analytics-engineering-data-pipelines/docker/dbtae/dbtae"
  REPO_ROOT="/Users/${USERNAME}/Documents/GitHub/analytics-engineering-data-pipelines"
  
  # Checkout branch (assumes starting from main)
  cd "${REPO_ROOT}"
  git checkout "${BRANCH}"
  
  # Environment setup
  source ~/.virtualenvs/dbt_scripts/bin/activate
  cd "${PROJECT_ROOT}"
  export SNOWFLAKE_WAREHOUSE=DEV_2X-LARGE
  export DBTAE="${PROJECT_ROOT}"
  
  # Clone dependencies
  # Step 1: Clone source tables (required for stg_charges_credits and payout models)
  echo 'Y' | python scripts/clone.py \
    --select "source:eb.invoice_charges source:eb_history.history_payouts" \
    --resource-type source \
    --project-directory "${PROJECT_ROOT}"
  
  # Step 2: Clone f_order_itemization dependencies (required for stg_order_itemization_dap)
  echo 'Y' | python scripts/clone.py \
    --select "+f_order_itemization" \
    --project-directory "${PROJECT_ROOT}"
  
  # Step 3: Clone f_dap dependencies (excluding DAP models which are built locally)
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
  
  If the user wants to run with custom parameters, they can specify:
  - Custom report month: "run for 2025-10-01"
  - Custom branch: "run on branch-name"
  - Custom username: "run as username"
  
  Execute this script step by step, showing progress and any errors that occur.
```

**Behavior**

* Executes the complete monthly DAP run workflow
* Checks out the specified branch from main
* Clones all required source tables and model dependencies
* Runs DAP seeds and models
* Supports custom configuration via environment variables

**Usage**

Use the `/run_dap` command to execute the monthly DAP run:

```
/run_dap
/run_dap run for 2025-10-01
/run_dap run on my-branch-name
/run_dap run for 2025-10-01 on my-branch-name
```

The command will execute the complete workflow including:
1. Branch checkout
2. Environment setup (virtualenv, warehouse, DBTAE variable)
3. Clone source tables (invoice_charges, history_payouts)
4. Clone f_order_itemization dependencies
5. Clone f_dap dependencies (excluding DAP models)
6. Seed execution (all seed_dap* files)
7. Model execution (all DAP models for specified report month)


