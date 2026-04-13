{% macro convert_to_usd(amount_col, rates_col, currency_col) %}
    round(
        ({{ amount_col }} / 100.0)
        / nullif(({{ rates_col }}::jsonb ->> {{ currency_col }})::numeric, 0),
        2
    )
{% endmacro %}
