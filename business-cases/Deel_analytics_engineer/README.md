# Deel Analytics Engineer — Take-Home Challenge

Payment processing analytics over Globepay data (Jan–Jun 2019, 5,430 transactions) using dbt + Supabase (PostgreSQL).

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

## Business Questions

| # | Question | Model | Result |
|---|---|---|---|
| 1 | What is the acceptance rate over time? | `fct_acceptance_rate_over_time` | ~68–72% weekly, stable across Jan–Jun 2019 |
| 2 | Which countries had declined transactions > $25M? | `fct_declined_by_country` | FR, UK, AE, US |
| 3 | Which transactions are missing chargeback data? | `fct_missing_chargeback` | 0 rows — 100% chargeback coverage |
| + | Does CVV provision affect acceptance rate? | `fct_cvv_acceptance_impact` | Yes — CVV provided → meaningfully higher rate |

## Technical Notes

**FX conversion:** `amount_usd = amount / rates[currency]` where `rates` is a JSON map embedded per row (ISO currency → units per 1 USD).

**Note on minor units:** The Globepay API spec describes `amount` as minor units (cents), which would imply ÷100 before FX conversion. However, the actual data contains decimal values (e.g. `1020.46`, `2589.92`) that are inconsistent with cent amounts — confirming amounts are already in major units (dollars). No ÷100 is applied. The `convert_to_usd` macro is the single place to add it if the data ever changes.

**Q3 = 0 rows is correct:** Acceptance and chargeback data arrive via separate async API responses. The LEFT JOIN in `fct_missing_chargeback` is designed to surface gaps — 0 rows means 100% coverage, which is a data quality win.
