{% macro convert_to_usd(amount_col, rates_col, currency_col) %}
    round(
        ({{ amount_col }}
        / nullif(({{ rates_col }}::jsonb ->> {{ currency_col }})::numeric, 0))::numeric,
        2
    )
{% endmacro %}
