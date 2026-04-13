-- Q1: What is the acceptance rate over time?
-- Grain: one row per ISO week (26 rows for Jan–Jun 2019).
-- Includes month for dual-axis monthly view in the notebook.

select
    transaction_month,
    transaction_week,
    count(*)                                                    as total_transactions,
    sum(is_accepted::int)                                       as accepted_transactions,
    round(sum(is_accepted::int)::numeric / count(*) * 100, 2)  as acceptance_rate_pct,
    sum(amount_usd)                                             as total_volume_usd
from {{ ref('stg_globepay__acceptance') }}
group by 1, 2
order by 2
