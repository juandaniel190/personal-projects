with source as (
    select * from {{ ref('globepay_acceptance_report') }}
)

select
    external_ref,
    cast(date_time as timestamp)                       as transaction_at,
    date_trunc('month', cast(date_time as timestamp))  as transaction_month,
    date_trunc('week',  cast(date_time as timestamp))  as transaction_week,
    date_trunc('day',   cast(date_time as timestamp))  as transaction_date,
    source,
    country,
    currency,
    (state = 'ACCEPTED')                               as is_accepted,
    cast(cvv_provided as boolean)                      as is_cvv_provided,
    cast(status as boolean)                            as is_active,
    {% if target.type == 'duckdb' %}
    cast(rates as json)                                as rates,
    {% else %}
    rates::jsonb                                       as rates,
    {% endif %}
    {{ convert_to_usd('amount', 'rates', 'currency') }} as amount_usd
from source
