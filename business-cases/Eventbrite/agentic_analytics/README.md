# Eventbrite Agentic Analytics

This is an analytics agent built with Cube, Langchain, Snowflake and Streamlit.

## Why Semantic Layer for LLM-powered apps?

When building text-to-SQL applications, it is crucial to provide LLM with rich context about underlying data model. In many cases it is not enough to feed LLM with database schema and expect it to generate the correct SQL. To operate correctly and execute trustworthy actions, it needs to have enough context and semantics about the data it consumes; it must understand the metrics, dimensions, entities, and relational aspects of the data by which it's powered. Basically—LLM needs a semantic layer.

![architecture](https://ucarecdn.com/32e98c8b-a920-4620-a8d2-05d57618db8e/)

[Read more on why to use a semantic layer with LLM-power apps.](https://cube.dev/blog/semantic-layer-the-backbone-of-ai-powered-data-experiences)


## Getting Started

- **Cube project**. If you don't have a Cube installed already, go to `cube/README.md`
- **OpenAI API**. This example uses OpenAI API, so you'll need an OpenAI API key.
- Make sure you have Python version >= 3.8
- Install dependencies: `pip install -r requirements.txt`
- Copy `.env_example` as `.env` and fill it in with your credentials. You need OpenAI API Key and credentials to access your Cube deployment.
- Run `streamlit run ./agentic_analytics.py`

## Unlock answers to new questions
To unlock answers to new questions, you can leverage the following assets
- Add new examples in `cube/agentic_analytics/example_queries/your_domain.yaml`
- Tweek the prompt template in `cube/agentic_analytics/utils.py`
- Change the field description in the corresponding cube files

## Ingest modified Cube context
When you add a new cube, a new view or modify anything in a Cube file that is useful for the app, you can delete `cube/agentic_analytics/vectorestore.pkl`. From there, when running the app, it will start by loading the new cube context.
