{% macro convert_to_usd(amount_col, rates_col, currency_col) %}
    {% if target.type == 'duckdb' %}
    round(
        cast(
            {{ amount_col }}
            / nullif(cast(cast({{ rates_col }} as json) ->> {{ currency_col }} as double), 0)
        as numeric),
        2
    )
    {% else %}
    round(
        ({{ amount_col }}
        / nullif(({{ rates_col }}::jsonb ->> {{ currency_col }})::numeric, 0))::numeric,
        2
    )
    {% endif %}
{% endmacro %}
