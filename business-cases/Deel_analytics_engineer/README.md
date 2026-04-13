# Deel Analytics Engineer — Take-Home Challenge

Payment processing analytics over Globepay data using dbt + Supabase (PostgreSQL).

## Business Questions Answered

| # | Question | Model | Expected result |
|---|---|---|---|
| 1 | What is the acceptance rate over time? | `fct_acceptance_rate_over_time` | ~68–72% weekly, stable Jan–Jun 2019 |
| 2 | Which countries had declined transactions > $25M? | `fct_declined_by_country` | FR, UK, AE, US |
| 3 | Which transactions are missing chargeback data? | `fct_missing_chargeback` | 0 rows (100% coverage) |
| + | Does CVV provision affect acceptance rate? | `fct_cvv_acceptance_impact` | Yes — CVV provided → higher rate |

## Setup

### Prerequisites

- Python 3.10+
- A Supabase project (PostgreSQL, direct connection on port 5432)
- The Globepay source CSVs placed in `deelhome/`

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure credentials

```bash
cp .env.example .env
# Edit .env with your Supabase host, user, password, and database name
```

### 3. Run the pipeline

```bash
cd deel_dbt

dbt deps                        # install dbt_utils package
dbt debug                       # verify Supabase connection

# Copy source CSVs into seeds/
cp ../deelhome/Globepay_Acceptance_Report.csv seeds/globepay_acceptance_report.csv
cp ../deelhome/Globepay_Chargeback_Report.csv seeds/globepay_chargeback_report.csv

dbt seed                        # load raw data (5,428 rows × 2 tables)

dbt compile --select staging
dbt run    --select staging
dbt test   --select staging

dbt compile --select marts
dbt run    --select marts
dbt test   --select marts

dbt build                       # full smoke test
dbt docs generate && dbt docs serve
```

### 4. Run the notebook

```bash
jupyter notebook notebooks/deel_analysis.ipynb
```

## Data Model

```
seeds (raw schema)
  globepay_acceptance_report
  globepay_chargeback_report
        │
        ▼ staging (views)
  stg_globepay__acceptance
  stg_globepay__chargeback
        │
        ▼ marts (tables)
  fct_acceptance_rate_over_time
  fct_declined_by_country
  fct_missing_chargeback
  fct_cvv_acceptance_impact
```

## Key Technical Notes

**Minor-unit conversion:** The Globepay API returns `amount` in minor units (cents). All monetary figures divide by 100 before FX conversion. Without this, totals are 100× inflated. The `convert_to_usd` macro encapsulates this logic in one place.

**FX conversion:** `amount_usd = (amount / 100) / rates[currency]` where `rates` is a JSON map of ISO currency → units per 1 USD.

**Q3 = 0 rows is correct:** Acceptance and chargeback data arrive via separate async API responses. The LEFT JOIN pattern in `fct_missing_chargeback` is designed to catch gaps — 0 rows means 100% chargeback coverage, which is a data quality win.
