with source as (
    select * from {{ ref('globepay_acceptance_report') }}
)

select
    external_ref,
    date_time::timestamptz                       as transaction_at,
    date_trunc('month', date_time::timestamptz)  as transaction_month,
    date_trunc('week',  date_time::timestamptz)  as transaction_week,
    date_trunc('day',   date_time::timestamptz)  as transaction_date,
    source,
    country,
    currency,
    (state = 'ACCEPTED')                         as is_accepted,
    cvv_provided::boolean                        as is_cvv_provided,
    status::boolean                              as is_active,
    rates::jsonb                                 as rates,
    {{ convert_to_usd('amount', 'rates::jsonb', 'currency') }} as amount_usd
from source
