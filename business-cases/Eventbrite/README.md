### Eventbrite Cube Semantic Layer & Agentic Analytics

End-to-end example of a Cube semantic layer backed by Snowflake with an optional Streamlit app that uses LangChain + OpenAI to translate natural language into SQL executed via Cube's SQL API.

For the Streamlit app details, see `agentic_analytics/README.md`.

## Prerequisites
- Access to a Snowflake account and role with SELECT permissions on referenced schemas/tables
- Optional (for the Streamlit app): Python 3.8+, OpenAI API key

## 1) Run Cube locally
1. Follow the steps in that [document](https://docs.google.com/document/d/1XJnDvMKMlUmJhfplVQ_oH0HgRthb-2KCypmRXNk9viE/edit?tab=t.0) for local setup

To make sure your setup works properly, check the Playground at `http://localhost:4000`

## 2) Semantic model
The semantic schema is in `model/` and organized as:
- `model/cubes/`: Cube definitions over Snowflake tables/views
  - `dim_event.yml`: event creation, publication, and hosting metrics/dimensions
  - `f_order_purchase.yml`: transactions-focused metrics (tickets, orders, creators, buyers, finance)
  - `f_order_purchase_agg.yml`: aggregated weekly/monthly activity exposed as `agg_trx_events`
  - `f_transaction.yml`: tax datamart measures and tax-related fields
- `model/views/`: User-friendly views that group fields into folders
  - `events.yml`, `transactions.yml`, `tax.yml`

Tip: Enrich field `description` in cube YAML to improve LLM grounding and the developer experience.

## 3) Optional: Run the Agentic Analytics app
The app lets users pick a domain (`events`, `transactions`, `tax`), ask questions, generate SQL with LangChain+OpenAI, and execute via Cube's SQL API. It ingests Cube metadata with a signed JWT to build a FAISS vectorstore.

See `agentic_analytics/README.md` for more context, examples, and how to tune prompts and examples.
