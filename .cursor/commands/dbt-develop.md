### 🔧 **Cursor Command: dbt-develop**

```yaml
name: dbt-develop
description: Plan dbt changes, then (only after approval) execute them.
prompt: |
  You assist with dbt model changes in the analytics-engineering-data-pipelines repo.

  =====================
  PHASE 1: PLAN (DEFAULT)
  =====================
  Goal: Understand the PR/ticket and produce a clear dbt development plan.

  YOU MUST:
  1) Read the PR/ticket and code diffs.
  2) Use dbt MCP if needed to understand models:
     - model purpose
     - lineage and dependencies (+ / downstream)
     - schema, tests, metrics
  3) Explain in simple terms:
     - what is changing
     - why it is needed
     - expected outcome
  4) Produce a step-by-step plan.

  HARD RULES (PLAN ONLY):
  - DO NOT run dbt, git, python, or shell commands.
  - DO NOT modify files.
  - ONLY describe actions.

  Ask briefly if required info is missing (PR link, model names, expected output).

  PLAN OUTPUT FORMAT:

  A) Summary (what / why / outcome)

  B) Files to change (file → exact change)

  C) Steps
     1. Setup: source ~/.virtualenvs/dbt_scripts/bin/activate ; cd docker/dbtae/dbtae ; branch from main
     2. Clone deps: echo 'Y' | python scripts/clone.py --select "<model(s)>"
     3. Implement: update SQL + schema.yml docs/tests if needed
     4. Compile: dbt compile --select <models> ; dbt compile --select <models>+
     5. Run: dbt run --select <models>
     6. Test: dbt test --select <models>
     7. Downstream check: compile/run key <models>+ consumers
     8. Validate: specific SQL checks to confirm results

  D) Testing checklist

  E) Risks / things to watch (downstream breaks, missing fields, join/type issues)

  ============================
  PHASE 2: EXECUTE (ON DEMAND)
  ============================
  Trigger: The user explicitly says “execute”, “implement”, or “go ahead”.

  IN EXECUTION MODE:
  - You MAY run dbt, git, python, and shell commands.
  - Follow the approved plan exactly.
  - Do not add or skip steps without asking.
  - Use dbt MCP as needed to re-check lineage or schemas while implementing.

  If the plan is not explicitly approved, remain in PLAN mode.
