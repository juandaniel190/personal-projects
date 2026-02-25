---
name: pr-review-ae
description: Review a PR for Analytics Engineering dbt changes. Analyzes business context, clones dependencies, runs compilation/runtime/data quality tests, and returns APPROVED or NEEDS CHANGES with specific feedback.
disable-model-invocation: true
argument-hint: "[PR number or branch name]"
---

You are a coding assistant reviewing PRs for dbt model changes in the analytics-engineering-data-pipelines repository.

**Input:** `$ARGUMENTS` — PR number, branch name, or PR description.

**Step 1: Environment setup**
- Activate venv: `source ~/.virtualenvs/dbt_scripts_py310/bin/activate`
- Navigate to dbt project: `cd docker/dbtae/dbtae`
- Checkout the PR branch if needed.
- Once activated and in the right folder, do not activate again.

**Step 2: PR analysis**
- Read PR description for business context and requirements.
- Identify all files changed and the purpose/impact of each.

**Step 3: PR summary**
- **Business Context:** Why this change is needed, what business problem it solves.
- **File Changes:** List of all modified/added files with brief descriptions.
- **Impact Analysis:** Which models, schemas, and downstream consumers are affected.

**Step 4: Review plan**
- Based on the testing plan in the PR description (if provided).
- Include: code review checklist, compilation steps, runtime steps, data quality validation, downstream impact verification.

**Step 5: Clone dependencies (CRITICAL — do this FIRST before any testing)**
- Identify all source tables and upstream models needed.
- `echo 'Y' | python scripts/clone.py --select <model_name>`
- Clone all changed model dependencies together: `echo 'Y' | python scripts/clone.py --select "model1 model2 model3"`
- Verify all dependencies cloned successfully before proceeding.

**Step 6: Code review**
- SQL syntax and best practices.
- Consistency with existing patterns.
- schema.yml documentation updated.
- Proper error handling, incremental model configs, pre/post-hooks.
- No schema mismatches or hardcoded values.

**Step 7: Compilation testing**
- `dbt compile --select <model_name>`
- `dbt compile --select <model_name>+`
- Check for errors, warnings, unresolved references.

**Step 8: Runtime testing**
- `dbt run --select <model_name>`
- `dbt run --select <model_name>+`
- Check for missing fields, join issues, runtime errors.

**Step 9: Data quality testing**
- `dbt test --select <model_name>`
- Verify nulls, uniqueness, referential integrity, new column data.

**Step 10: Downstream impact testing**
- `dbt compile --select <model_name>+`
- Run key downstream models that directly reference changed models.
- Verify no breaking changes.

**Step 11: Validation queries**
- Verify new fields populate correctly, joins work, data looks correct.
- Compare row counts before/after changes.

**Review output structure:**
1. PR Summary (business context + file changes + impact)
2. Review Plan
3. Dependencies cloned (list + confirmation)
4. Review Findings (code quality, compilation, runtime, data quality, downstream, validation)
5. **Final decision:**
   - **APPROVED** — if all checks pass
   - **NEEDS CHANGES** — with: where the issue is (file/line/model), what it is, why it matters, how to fix it

**Example:**
`/pr-review-ae review PR #906`
`/pr-review-ae review branch ipolo_add_parsed_user_agent`
