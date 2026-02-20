### 🚨 **Cursor Command: alert_pd**

```yaml
name: alert_pd
description: Use PagerDuty MCP to analyze high-urgency Analytics Engineering alerts for today and guide from detection to communication (summary, remediation, Slack draft).
prompt: |
  You are helping analyze PagerDuty alerts for Analytics Engineering Pipelines Prod and produce a clear summary, remediation plan, and a Slack message draft.

  **Data source**
  - Use the PagerDuty MCP (server: `user-pagerduty`).
  - Query criteria: exactly as in `docs/analytics_engineering_high_urgency_query.md` — service_ids `["PGOB0AD"]`, urgencies `["high"]`, sort_by `["created_at:desc"]`, limit 25.
  - **Scope to today:** Add `since` and `until` to the query_model so that only incidents created **today** (in the user's local timezone) are returned. Compute "start of today" and "end of today" in the user's local timezone, convert to ISO 8601 UTC (e.g. `2026-01-29T00:00:00Z` and `2026-01-29T23:59:59Z`), and pass them as `since` and `until`. If the user has not specified a timezone, use a reasonable default (e.g. America/Los_Angeles) and state it.

  **Execution steps (strict order)**

  **1) Fetch alerts**
  - Call `list_incidents` with the query above (including since/until for today).
  - If **zero** incidents are returned for today:
    - Say clearly: "No high-urgency PagerDuty alerts for Analytics Engineering Pipelines Prod today." Then stop; do not run steps 2–4.
  - If **more than one** incident is returned:
    - List each briefly: incident id (or number), title, created_at timestamp.
    - Ask: "Which alert should I investigate? (Reply with the incident number or id.)"
    - Do **not** continue to root cause analysis or later steps until the user picks one incident.
  - If **exactly one** incident: proceed to step 2 with that incident.

  **2) Root cause analysis**
  - For the **single** selected incident:
    - Call `get_incident` with that incident's id to fetch full details (summary, status, assignments, timestamps).
    - If the PagerDuty MCP or API exposes notes or additional metadata for the incident, fetch and use them.
    - From the incident title/summary, infer the failure context (e.g. DAG id and task id from "TASK FAILURE: dag_id/task_id").
    - Use the repo to enrich analysis: find the DAG file (e.g. under `airflow/dags/ae_dags/`), the task definition, and any readme (e.g. `docker/dbtae/dbtae/models/marts/<mart>/readme_*.md`) that describes how to respond to failures.
    - **Do not invent log content.** PagerDuty does not contain Airflow task logs. If the user has pasted Airflow logs in the chat, use them; otherwise state explicitly: "Actual task logs are in Airflow (see docs/pagerduty_to_airflow_logs.md). Without those logs or a pasted snippet, the exact dbt/model error cannot be confirmed here."
    - Summarize the most likely root cause based on what **is** available (incident title, DAG/task design, known failure patterns). If something is unknown or ambiguous, say so explicitly.

  **3) Summary + remediation plan**
  - **First:** Output a **High-level** paragraph: one short, concise paragraph (2–4 sentences) in plain language explaining what happened and the recommended action. The user should get this gist before any detailed sections. Then output the two sections below; do not mix them.

  **A) Short error summary**
  - Maximum 5 bullet points.
  - Plain language: what failed, where (DAG/task/service), and the best-understood reason.
  - No raw log dumps unless one line is essential.

  **B) Plan mode**
  - Numbered, step-by-step remediation plan.
  - Concrete actions the user should take to fix or mitigate (e.g. check Airflow log, clear task, rerun, verify downstream).
  - Include verification steps to confirm resolution (e.g. "Confirm the next DAG run succeeds" or "Check that table X was updated").

  **4) Slack communication**
  - Generate a **short, production-ready Slack message** for the `#alerts` channel.
  - Content must include:
    - What happened (one sentence).
    - Impact (if any); if unknown, say "Impact: TBD" or omit.
    - The fix or mitigation the user is deploying (one sentence).
  - Tone: calm, professional, concise.
  - **Do NOT send the message.** Output only the message text so the user can copy and post it.

  **Constraints**
  - Do not speculate. If something cannot be confirmed from data or the repo, state that explicitly.
  - Keep all outputs concise and actionable.
  - Do not repeat raw logs unless strictly necessary for understanding.
  - Reference `docs/pagerduty_to_airflow_logs.md` when directing the user to Airflow logs.
```

**How to use**

1. Run the command (e.g. via command palette or by name `alert_pd`).
2. The agent will fetch today's high-urgency AE alerts from PagerDuty and either report "no alerts," ask you to pick one, or analyze the single alert.
3. After analysis you get: a **High-level** paragraph (what happened + recommended action), **Short error summary**, **Plan mode**, and a **Slack message** draft for `#alerts` to copy.

**Reference**

- PagerDuty query: `docs/analytics_engineering_high_urgency_query.md`
- From PagerDuty to Airflow logs: `docs/pagerduty_to_airflow_logs.md`
