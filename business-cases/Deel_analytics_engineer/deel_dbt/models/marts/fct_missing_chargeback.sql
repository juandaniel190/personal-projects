-- Q3: Which transactions are missing chargeback data?
-- Pattern: LEFT JOIN acceptance → chargeback; NULL on right side = missing record.
-- Expected answer: 0 rows — full chargeback coverage in this dataset.
-- Model is production-ready to surface gaps as new data arrives.

select
    a.external_ref,
    a.transaction_at,
    a.country,
    a.currency,
    a.amount_usd,
    a.is_accepted
from {{ ref('stg_globepay__acceptance') }} a
left join {{ ref('stg_globepay__chargeback') }} c
    on a.external_ref = c.external_ref
where c.external_ref is null
