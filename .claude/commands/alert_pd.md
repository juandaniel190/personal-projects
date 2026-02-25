---
name: alert_pd
description: Analyze high-urgency PagerDuty alerts for Analytics Engineering Pipelines Prod today. Fetches alerts, runs root cause analysis, and drafts a Slack message for #alerts.
disable-model-invocation: true
---

You are helping analyze PagerDuty alerts for Analytics Engineering Pipelines Prod and produce a clear summary, remediation plan, and a Slack message draft.

**Data source**
- Use the PagerDuty MCP (server: `user-pagerduty`).
- Query criteria: service_ids `["PGOB0AD"]`, urgencies `["high"]`, sort_by `["created_at:desc"]`, limit 25.
- **Scope to today:** Add `since` and `until` so only incidents created **today** are returned. Compute start/end of today in the user's local timezone, convert to ISO 8601 UTC, and pass as `since`/`until`. Default timezone: America/Los_Angeles (state it if assumed).

**Execution steps (strict order)**

**1) Fetch alerts**
- Call `list_incidents` with the query above (including since/until for today).
- If **zero** incidents: Say "No high-urgency PagerDuty alerts for Analytics Engineering Pipelines Prod today." Then stop.
- If **more than one**: List each briefly (incident id, title, created_at). Ask: "Which alert should I investigate?" Wait for user to pick one before continuing.
- If **exactly one**: proceed to step 2.

**2) Root cause analysis**
- Call `get_incident` for the selected incident (summary, status, assignments, timestamps).
- Infer failure context from the incident title (e.g. DAG id/task id from "TASK FAILURE: dag_id/task_id").
- Use the repo to enrich analysis: find the DAG file (e.g. `airflow/dags/ae_dags/`), the task definition, and any readme (e.g. `docker/dbtae/dbtae/models/marts/<mart>/readme_*.md`).
- **Do not invent log content.** PagerDuty does not contain Airflow task logs. If the user has pasted logs, use them; otherwise state: "Actual task logs are in Airflow (see docs/pagerduty_to_airflow_logs.md)."
- Summarize the most likely root cause from available data. If something is unknown, say so explicitly.

**3) Summary + remediation plan**

First output a **High-level paragraph** (2–4 sentences): what happened and recommended action.

**A) Short error summary** — max 5 bullets: what failed, where (DAG/task/service), best-understood reason. No raw log dumps.

**B) Plan mode** — numbered step-by-step remediation. Concrete actions + verification steps (e.g. "Confirm next DAG run succeeds", "Check table X was updated").

**4) Slack communication**
- Draft a short, production-ready Slack message for `#alerts`.
- Include: what happened (1 sentence), impact (or "Impact: TBD"), fix/mitigation being deployed (1 sentence).
- Tone: calm, professional, concise.
- **Do NOT send the message.** Output text only for the user to copy.

**Constraints**
- Do not speculate. If something cannot be confirmed, state that explicitly.
- Keep all outputs concise and actionable.
- Reference `docs/pagerduty_to_airflow_logs.md` when directing user to Airflow logs.
