# Setup

## Prerequisites

- Python 3.10+

## 1. Install dependencies

```bash
pip install -r requirements.txt
```

## 2. Run the pipeline

### Option A — DuckDB (default, zero setup)

No credentials needed. Everything runs locally.

```bash
# source /Users/damezquita/Documents/GitHub/personal-projects/business-cases/Deel_analytics_engineer/.venv/bin/activate   
cd deel_dbt
dbt deps
dbt build
```

That's it. A `deel.duckdb` file is created in the project root with all tables ready to query.

### Option B — Supabase (hosted PostgreSQL)

To run against a real cloud database, configure your credentials first:

```bash
cp .env.example .env
# Fill in your Supabase pooler host, user, password, and database
```

`.env.example` shows the expected format:

```
DBT_SUPABASE_HOST=aws-0-<region>.pooler.supabase.com
DBT_SUPABASE_PORT=6543
DBT_SUPABASE_USER=postgres.<project-ref>
DBT_SUPABASE_PASSWORD=<your-password>
DBT_SUPABASE_DBNAME=postgres
```

> Use the **connection pooler** host and port 6543 (not the direct connection on 5432) to avoid firewall timeouts on restricted networks.

Then run:

```bash
cd deel_dbt
dbt deps
dbt build --target supabase
```

## 3. Run the notebook

The notebook auto-detects which backend to use based on whether `.env` is present.

```bash
jupyter notebook notebooks/deel_analysis.ipynb
```

## 4. Generate docs

```bash
cd deel_dbt
dbt docs generate && dbt docs serve
```
