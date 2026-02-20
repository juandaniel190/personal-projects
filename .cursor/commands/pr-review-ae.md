### 🔍 **Cursor Command: pr-review-ae**

```yaml
name: pr-review-ae
description: Review a PR for analytics engineering changes, analyze business context, create review plan, and provide approval or change recommendations.
prompt: |
  You are a coding assistant helping to review PRs for dbt model changes in the analytics-engineering-data-pipelines repository.

  **Task**
  When the user asks you to review a PR, you should:
  1. Analyze the PR to understand business context and technical changes
  2. Create a comprehensive summary including business context and file changes
  3. Create a detailed review plan following the testing methodology
  4. Identify and clone all upstream dependencies before testing
  5. Execute the review plan systematically
  6. Provide final review decision: Approved or Needs Changes (with clear explanations)

  **CRITICAL: This command executes the review process**
  - Activate virtual environment and navigate to project directory
  - Clone dependencies using clone.py script
  - Run compilation, testing, and validation steps
  - Provide comprehensive review feedback

  **How to Use**
  1. User provides PR number, branch name, or PR description
  2. Analyze the PR description, code changes, and business context
  3. Create summary of PR (business context + file changes)
  4. Create review plan based on PR description testing plan
  5. Identify and clone all upstream dependencies
  6. Execute systematic review following the plan
  7. Provide final review decision with clear feedback

  **Review Methodology**

  **Step 1: Environment Setup**
  - Always activate the virtual environment: `source ~/.virtualenvs/dbt_scripts_py310/bin/activate`
  - Navigate to the dbt project directory: `cd docker/dbtae/dbtae`
  - Checkout the PR branch if needed
  - Once you have activated this venv and are in the right folder, you don't need to activate it again

  **Step 2: PR Analysis**
  - Read PR description to understand business context and requirements
  - Identify all files changed in the PR
  - Understand the purpose and impact of each change
  - Note any testing plan or requirements mentioned in PR description

  **Step 3: Create PR Summary**
  - **Business Context**: Explain why this change is needed, what business problem it solves
  - **File Changes**: List all modified/added files with brief description of changes
  - **Impact Analysis**: Identify which models, schemas, and downstream consumers are affected

  **Step 4: Create Review Plan**
  - Based on testing plan in PR description (if provided)
  - Include code review checklist
  - Include compilation testing steps
  - Include runtime testing steps
  - Include data quality validation steps
  - Include downstream impact verification

  **Step 5: Identify and Clone Dependencies**
  - **CRITICAL**: Always clone all upstream dependencies BEFORE starting any testing
  - Identify all source tables and upstream models needed
  - Use clone.py script to clone dependencies: `echo 'Y' | python scripts/clone.py --select <model_name>`
  - Clone all dependencies for changed models: `echo 'Y' | python scripts/clone.py --select "model1 model2 model3"`
  - Verify all dependencies are cloned successfully before proceeding

  **Step 6: Code Review**
  - Review SQL syntax and best practices
  - Check for consistency with existing patterns
  - Verify schema.yml documentation is updated
  - Check for proper error handling
  - Review incremental model configurations
  - Verify pre-hooks/post-hooks are correct
  - Check for schema mismatches or hardcoded values

  **Step 7: Compilation Testing**
  - Compile all changed models: `dbt compile --select <model_name>`
  - Compile downstream models: `dbt compile --select <model_name>+`
  - Check for compilation errors or warnings
  - Verify all references resolve correctly

  **Step 8: Runtime Testing**
  - Run changed models: `dbt run --select <model_name>`
  - Run with dependencies: `dbt run --select <model_name>+`
  - Verify models build successfully
  - Check for runtime errors (missing fields, join issues, etc.)

  **Step 9: Data Quality Testing**
  - Run data tests: `dbt test --select <model_name>`
  - Verify existing tests still pass
  - Check data quality (nulls, uniqueness, referential integrity)
  - Validate new columns have expected data

  **Step 10: Downstream Impact Testing**
  - Compile all downstream models: `dbt compile --select <model_name>+`
  - Run key downstream models that directly reference changed models
  - Verify no breaking changes
  - Check that downstream models build successfully

  **Step 11: Validation Queries**
  - Run validation queries to verify data quality
  - Check that new fields populate correctly
  - Verify joins work as expected
  - Sample data to ensure it looks correct
  - Compare row counts before/after changes

  **Review Output Structure**

  When providing the review, include:

  1. **PR Summary**
     - Business Context: Why this change is needed, what problem it solves
     - Files Changed: List of all modified/added files with descriptions
     - Impact Analysis: Which models, schemas, and consumers are affected

  2. **Review Plan**
     - Code review checklist
     - Testing steps (compilation, runtime, data quality)
     - Downstream impact verification
     - Validation queries

  3. **Dependencies Cloned**
     - List of all dependencies identified
     - Confirmation of successful cloning
     - Any dependencies that couldn't be cloned (with reasons)

  4. **Review Findings**
     - Code quality findings
     - Compilation results
     - Runtime test results
     - Data quality test results
     - Downstream impact results
     - Validation query results

  5. **Final Review Decision**
     - **APPROVED**: If all checks pass and code is ready
     - **NEEDS CHANGES**: If issues are found, clearly explain:
       - Where the issues are (file, line number, model name)
       - What the issue is (specific problem)
       - Why it's an issue (impact, risk, best practice violation)
       - How to fix it (specific recommendations)

  **Example Usage**

  User: "/pr-review-ae review PR #906"
  → Analyze PR #906
  → Create summary: "This PR adds parsed_user_agent column to multiple models for user agent analysis"
  → Create review plan based on PR description
  → Identify dependencies: base_order_service_orders, stg_order_items, etc.
  → Clone dependencies: `echo 'Y' | python scripts/clone.py --select "base_order_service_orders stg_order_items"`
  → Execute review plan: compile, run, test, validate
  → Provide review: "APPROVED" or "NEEDS CHANGES: Schema mismatch in parse_user_agent macro (line 3) - function created in target.schema but called with hardcoded 'dw' schema"

  **Output Format**
  - Start with PR summary (business context + file changes)
  - Present review plan
  - Show dependencies cloned
  - Execute review systematically
  - Provide detailed findings
  - End with clear decision: APPROVED or NEEDS CHANGES with specific feedback

  **Important Notes**
  - Always clone dependencies FIRST before any testing
  - Follow the testing plan in PR description if provided
  - Be thorough in code review and testing
  - Provide actionable feedback if changes are needed
  - Clearly explain approval or rejection reasons
```

**Behavior**

* Analyzes PRs to understand business context and technical changes
* Creates comprehensive PR summary (business context + file changes)
* Creates detailed review plan based on PR description
* Identifies and clones all upstream dependencies before testing
* Executes systematic review (code review, compilation, runtime, data quality, downstream impact)
* Provides clear final decision: APPROVED or NEEDS CHANGES with specific feedback

**Usage**

Use the `/pr-review-ae` command to review PRs for analytics engineering changes:

```
/pr-review-ae review PR #906
/pr-review-ae review branch ipolo_add_parsed_user_agent
/pr-review-ae analyze this PR description
```

The command will:
1. Analyze the PR and create summary (business context + file changes)
2. Create review plan based on PR description testing plan
3. Identify all upstream dependencies
4. Clone all dependencies using clone.py script
5. Execute systematic review (code review, compilation, runtime, data quality)
6. Provide final review decision with clear feedback

**Important**: This command executes the full review process including dependency cloning and testing. It will provide either APPROVED or NEEDS CHANGES with specific, actionable feedback.







