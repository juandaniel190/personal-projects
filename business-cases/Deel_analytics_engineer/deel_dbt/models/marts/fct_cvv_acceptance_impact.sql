-- Bonus: Does CVV provision correlate with higher acceptance rates?
-- The Globepay API marks CVV as optional-but-recommended.
-- Grain: one row per CVV provision flag (2 rows: TRUE / FALSE).

select
    is_cvv_provided,
    count(*)                                                    as total_transactions,
    sum(is_accepted::int)                                       as accepted_transactions,
    round(sum(is_accepted::int)::numeric / count(*) * 100, 2)  as acceptance_rate_pct,
    sum(amount_usd)                                             as total_volume_usd
from {{ ref('stg_globepay__acceptance') }}
group by 1
order by 1 desc
