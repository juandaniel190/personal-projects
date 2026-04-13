# Setup

## Prerequisites

- Python 3.10+
- A Supabase project (PostgreSQL) with the connection pooler enabled (port 6543)

## 1. Install dependencies

```bash
pip install -r requirements.txt
```

## 2. Configure credentials

```bash
cp .env.example .env
# Edit .env with your Supabase pooler host, user, password, and database name
```

The `.env.example` shows the expected format:

```
DBT_SUPABASE_HOST=aws-0-<region>.pooler.supabase.com
DBT_SUPABASE_PORT=6543
DBT_SUPABASE_USER=postgres.<project-ref>
DBT_SUPABASE_PASSWORD=<your-password>
DBT_SUPABASE_DBNAME=postgres
```

> **Note:** Use the connection pooler host and port (6543), not the direct connection (port 5432), to avoid firewall timeouts on restricted networks.

## 3. Run the pipeline

```bash
cd deel_dbt

dbt deps          # install dbt_utils package
dbt debug         # verify Supabase connection
dbt seed          # load raw CSVs (5,430 rows × 2 tables)
dbt run           # build staging views + mart tables
dbt test          # run all 24 data tests
```

Or all at once:

```bash
dbt build
```

## 4. Run the notebook

```bash
jupyter notebook notebooks/deel_analysis.ipynb
```

## 5. Generate docs

```bash
dbt docs generate && dbt docs serve
```
