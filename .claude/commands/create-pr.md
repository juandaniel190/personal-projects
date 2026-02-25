---
name: create-pr
description: Create a production-grade PR description for the Eventbrite Analytics Engineering repo. Infers JIRA ticket from branch, fills the PR template, and transitions the ticket to IN CODE REVIEW.
disable-model-invocation: true
---

You are a coding assistant preparing a production-grade PR description for the Eventbrite Analytics Engineering repo.

**Task**
Generate a complete PR description using all available context:
- Current diff / code changes
- Git branch name (usually includes JIRA ticket, e.g. EB-312032)
- Comments, commits, and recent edits
- Local context of modified dbt models, DAGs, SQL scripts, or seeds

**PR Title Format**
`[PATCH]/[MINOR]/[MAJOR][<ticket number>] short title`
- `[PATCH]` for bug fixes and small changes
- `[MINOR]` for new features or significant changes
- `[MAJOR]` for breaking changes (rare)
- Example: `[PATCH][EB-304407] fix top_transacted_country`

**JIRA Transition**
After creating the PR, automatically transition the JIRA ticket to "IN CODE REVIEW" using `mcp_jira_transition_issue` with `transition_name: "IN CODE REVIEW"`.

**PR Template to fill**

```
## Summary
<!--- SHORT and CONCISE. What was changed and why, 2-3 sentences max. -->

<Required>

## Jira Acceptance Criteria
<!-- Brief checkboxes only. No full descriptions. -->
* [ ] Incomplete AC
* [x] Complete AC

## Test Plan

**Testing Environment**

Database: <Required>
Models Tested: <Required>
Upstream Dependencies: <Required>

**dbt Commands Used:**
<!-- ALWAYS include the specific dbt commands used, one per line -->
<!-- e.g. `python scripts/clone.py --select "model_name+"` -->
<!-- e.g. `dbt run --select model_name` -->
<!-- e.g. `dbt test --select model_name` -->

<Required>

## Documentation and Testing
* [ ] The documentation of the impacted models is up to date
* [ ] Tests are implemented on the impacted source and data marts models

<Required>

## Warehouse Choice

| Size     | # of Runs  | Avg Runtime | Cost       |
| -------- | ---------- | ----------- | ---------- |
| Small    | <Required> | <Required>  | <Required> |
| Large    | <Required> | <Required>  | <Required> |
| 2X-Large | <Required> | <Required>  | <Required> |

## JIRA Issues / Related PRs / Documentation
<!-- Link to associated Jira tickets, related PRs, or updated docs -->

<Required>
```

**Behavior**
- Infer the JIRA ticket (EB-####) from the branch or commit message.
- Keep all sections SHORT and CONCISE (Summary: 2–3 sentences; AC: brief checkboxes only).
- Always include the specific dbt commands used for testing.
- Add `<Required>` placeholders for missing details.
- After generating the PR body, transition the JIRA ticket to "IN CODE REVIEW".

**Output**
Render the PR body ready for GitHub copy/paste with consistent Eventbrite AE formatting.
