### 🧩 **Cursor Command: create-pr**

```yaml
name: create-pr
description: Create a Pull Request with full context, JIRA details, test plan, and documentation checklist.
prompt: |
  You are a coding assistant preparing a production-grade PR description for the Eventbrite Analytics Engineering repo.

  **Task**
  Generate a complete PR description following the template below, using all available context from:
  - Current diff / code changes
  - Git branch name (usually includes JIRA ticket, e.g. EB-312032)
  - Comments, commits, and recent Cursor edits
  - Local context of modified dbt models, DAGs, SQL scripts, or seeds

  **PR Title Format**
  Start with: `[PATCH]/[MINOR][<ticket number>] short title`
  - Example: `[PATCH][EB-304407] fix top_transacted_country`
  - Example: `[MINOR][EB-12345] add new dimension table`
  - Use [PATCH] for bug fixes and small changes
  - Use [MINOR] for new features or significant changes
  - Use [MAJOR] for breaking changes (rare)

  **JIRA Transition**
  After creating the PR, automatically transition the JIRA ticket to "IN CODE REVIEW" using the `mcp_jira_transition_issue` tool with transition_name: "IN CODE REVIEW"

  **PR Template**
```

  <!--- Provide a general summary of your changes in the Title above -->

## Summary

  <!--- Keep this SHORT and CONCISE. Describe what was changed and why in 2-3 sentences max. -->
  <!--- Example: "Adds 6 new fields to account_dim for Braze email personalization: 4 email addresses and 2 GTF metrics." -->

  <Required>

## Jira Acceptance Criteria

  <!-- Keep this SHORT and CONCISE. List only the key AC items as brief checkboxes. -->
  <!-- Example: * [x] Strategic Success Rep Email Address -->
  <!-- Do NOT include full descriptions or "TO BE SENT INTO BRAZE" notes -->

* [ ] Incomplete AC
* [x] Complete AC

## Test Plan

**Testing Environment**

Database: <Required>

Models Tested: <Required>

Upstream Dependencies: <Required>

**dbt Commands Used:**

<!--- List all dbt commands used for testing, one per line -->
<!--- Example: -->
<!--- - `python scripts/clone.py --select "model_name+"` - Clone upstream dependencies -->
<!--- - `dbt run --select model_name` - Build model -->
<!--- - `dbt compile --select model_name` - Verify compilation -->
<!--- - `dbt test --select model_name` - Run data quality tests -->
  
  <!--- ALWAYS include the specific dbt commands used for testing (e.g., `dbt compile --select model_name`, `dbt run --select model_name+`, `dbt test`, etc.) -->

  <Required>

## Documentation and Testing

  <!-- Checklist of testing and documentation compliance -->

* [ ] The documentation of the impacted models is up to date
* [ ] Tests are implemented on the impacted source and data marts models

  <Required>

## Warehouse Choice <sup>[?](https://eventbrite.atlassian.net/wiki/spaces/DEV/pages/15757705406/Choosing+a+Warehouse)</sup>

| Size     | # of Runs  | Avg Runtime | Cost       |
| -------- | ---------- | ----------- | ---------- |
| Small    | <Required> | <Required>  | <Required> |
| Large    | <Required> | <Required>  | <Required> |
| 2X-Large | <Required> | <Required>  | <Required> |

## JIRA Issues / Related PRs / Documentation

  <!--- Link to the associated Jira tickets here. -->

  <!--- Link to any PRs or docs created/updated as part of this work. -->

  <Required>
  ```

**Behavior**

* Generate PR title in format: `[PATCH]/[MINOR][EB-XXXXX] short title` (e.g. `[PATCH][EB-304407] fix top_transacted_country`).
* Infer the Jira ticket (EB-####) from the branch or commit message.
* Automatically transition JIRA ticket to "IN CODE REVIEW" after PR creation.
* **Keep all sections SHORT and CONCISE:**
  - Summary: 2-3 sentences max describing what changed and why
  - JIRA Acceptance Criteria: Brief checklist items only (no full descriptions)
  - Test Plan: Include Testing Environment (Database, Models Tested, Upstream Dependencies) and dbt Commands Used sections
* Summarize key file changes (models, DAGs, seeds, YAML).
* Highlight what problem is fixed, why, and how.

* **ALWAYS include the specific dbt commands used for testing** (e.g., `dbt compile --select model_name`, `dbt run --select model_name+`, `dbt test`, etc.)
* Add checkboxes and placeholders for missing sections.

**Output**

* Render the PR body ready for GitHub copy/paste.
* Always include `<Required>` placeholders for missing details.
* Keep consistent formatting and spacing as per Eventbrite AE PR standards.
* **Emphasize brevity**: Keep summaries, AC, and test plans concise and to the point.

```

---

### ⚙️ **Usage in Cursor**
Once defined:
1. Open the branch you’re working on (`EB-xxxxx`).
2. Press **⌘ K → create-pr** (or your custom shortcut).
3. Cursor will:
   - Parse your recent file changes.
   - Generate the PR Markdown body.
   - Display it ready to paste into GitHub’s PR form.

---


