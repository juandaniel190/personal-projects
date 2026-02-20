# Cursor configuration

Everything Cursor uses is under this folder: **commands**, **rules**, **plans**, and **skills**.

## Layout

```
.cursor/
├── README.md       ← this file
├── commands/       ← Command docs (create-pr, dbt-develop, jira, deploy, alert_pd, pr-review-ae, pre-commit, run_dap)
├── rules/          ← Rules (.mdc): create-pr, dbt-mcp-setup
├── plans/          ← Plans (reserved)
└── skills/         ← Agent skills (Cursor format)
    ├── tile.json   ← Skill registry
    ├── README-dbt-agent-skills.md
    ├── adding-dbt-unit-test/
    ├── using-dbt-for-analytics-engineering/
    ├── building-dbt-semantic-layer/
    ├── ... (all dbt + dbt-migration skills)
```

## Skills

The **skills/** folder contains the [dbt Agent Skills](https://github.com/dbt-labs/dbt-agent-skills) in the format Cursor expects: one folder per skill, each with `SKILL.md` and any references/scripts. Use **tile.json** for discovery; see **README-dbt-agent-skills.md** for the full list and usage.
