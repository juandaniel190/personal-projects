with source as (
    select * from {{ ref('globepay_chargeback_report') }}
)

select
    external_ref,
    status::boolean as is_active,
    (chargeback = 'TRUE') as has_chargeback
from source
