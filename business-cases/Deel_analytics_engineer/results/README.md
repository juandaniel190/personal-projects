# Query Results

Output of the four dbt mart tables, exported directly from the Supabase database.
These are here so you can inspect the answers without running anything.

| File | Rows | Answers |
|---|---|---|
| `fct_acceptance_rate_over_time.csv` | 26 | Weekly acceptance rate, Jan–Jun 2019 |
| `fct_declined_by_country.csv` | 4 | Countries with declined volume > $25M: FR, UK, AE, US |
| `fct_missing_chargeback.csv` | 0 | 0 transactions missing chargeback data (100% coverage) |
| `fct_cvv_acceptance_impact.csv` | 2 | CVV provided → 62.5% rate; not provided → 69.6% rate |
