-- Q2: Which countries had declined transactions exceeding $25M?
-- Expected answer: FR, UK, AE, US (after minor-unit → USD conversion).
-- CTE used to aggregate first; the WHERE on total_declined_usd
-- avoids an illegal alias reference in the same SELECT.

with declined as (
    select
        country,
        sum(amount_usd) as total_declined_usd
    from {{ ref('stg_globepay__acceptance') }}
    where not is_accepted
    group by 1
)

select
    country,
    total_declined_usd,
    total_declined_usd > 25000000 as exceeds_25m_threshold
from declined
where total_declined_usd > 25000000
order by total_declined_usd desc
