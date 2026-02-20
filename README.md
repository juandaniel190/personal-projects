# Personal Projects

Portfolio of case studies, analytics, and data work.

## Repository layout

```
personal-projects/
├── README.md              ← this file
├── business-cases/        ← all case study folders
│   ├── Bark/              ← Trading diagnostic (UK & US)
│   ├── Perk/              ← Revenue Operations case study
│   ├── Cabify/
│   ├── Deel/
│   ├── Glovo/
│   ├── Hotel_Cancellations_ML/
│   └── People_Analytics_TSLA/
└── .cursor/               ← Cursor config: commands, rules, plans, skills (all in one place)
    ├── commands/         ← create-pr, dbt-develop, jira, deploy, etc.
    ├── rules/             ← create-pr, dbt-mcp-setup
    ├── plans/
    └── skills/            ← dbt Agent Skills (tile.json + one folder per skill)
```

## Business cases

All case studies live under **`business-cases/`**:

- **Bark** — [live demo](https://juandaniel190.github.io/personal-projects/business-cases/Bark/deck/Bark_Trading_Diagnostic.html)
- **Perk** — [live demo](https://juandaniel190.github.io/personal-projects/business-cases/Perk/deck/Revenue_Operations_Case_Study.html)
- **Cabify**, **Deel**, **Glovo**, **Hotel_Cancellations_ML**, **People_Analytics_TSLA**

## Cursor (commands, rules, skills)

Everything Cursor uses is under **`.cursor/`**:

- **commands/** — PR, dbt-develop, Jira, deploy, PagerDuty, pre-commit, etc.
- **rules/** — Cursor rules (`.mdc`)
- **plans/** — reserved
- **skills/** — dbt Agent Skills in Cursor’s format: each skill is a folder with `SKILL.md`; **tile.json** is the registry. See `.cursor/README.md` and `.cursor/skills/README-dbt-agent-skills.md` for details.

No separate “courses-and-skills” folder; it’s all under `.cursor` so Cursor and any course/agent use the same layout.
