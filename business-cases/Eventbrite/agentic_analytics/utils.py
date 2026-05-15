import os
import datetime
import psycopg2
import altair as alt
import streamlit as st
import yaml
from pathlib import Path

from dotenv import load_dotenv
from langchain.prompts import PromptTemplate, FewShotPromptTemplate
from langchain.docstore.document import Document


def check_input(question: str):
    if question == "":
        raise Exception("Please enter a question.")
    else:
        pass

def load_example_queries(selected_view: str):
    """Load example queries from YAML file based on selected view"""
    yaml_file = Path(__file__).parent / "example_queries" / f"{selected_view}.yaml"

    if not yaml_file.exists():
        # Return empty list if no YAML file exists for this view
        return []

    with open(yaml_file, 'r') as file:
        data = yaml.safe_load(file)
        return data.get('example_queries', [])

def create_prompt_template(selected_view):
    """Create the prompt template with the given example queries and business context"""

    return FewShotPromptTemplate(
    examples=load_example_queries(selected_view),
    example_prompt=PromptTemplate(
        input_variables=["question", "query"],
        template="Question: {question}\n {query}\n"
    ),
    prefix="""
    You are a PostgreSQL expert. Given an input question, create a syntactically correct PostgreSQL query to run and return it as the answer to the input question.
    Unless the user specifies in the question a specific number of examples to obtain, query for at most {top_k} results using the LIMIT clause as per PostgreSQL.
    Never query for all columns from a table. You must query only the columns that are needed to answer the question.
    Note that the columns with (member_type: measure) are numeric columns and the ones with (member_type: dimension) are string columns.
    You should include at least one column with (member_type: measure) in your query.
    If there is only 1 select item in the query, do not use GROUP BY.
    Only when you need to compare 2 dimensions, use a CTE first. Then compare the columns without using a measure() function in the last step.
    Only use a CTE and a with clause when you need to compare 2 dimensions. Otherwise write a simple query.
    Consider the column descriptions when choosing dimension for the query, they can contain useful synonyms and context.

    {business_context}

    When the question contains 'daily', 'weekly', 'monthly', 'yearly' or 'quarterly', don't look for it in the column names. Just use date_trunc to group by the date.
    So weekly free tickets means translate to date_trunc('week', trx_date) as date and free_item_qty as the measure."""
    ,
    suffix="""
    Do not mention columns that do not exist.
    Only look among the following columns and pick the relevant ones:
    {columns_info}

    Question: {input_question}

    Only if you couldn't construct the query, answer exactly: `{no_answer_text}`. And explain why you can't build the query.

    Otherwise, answer a single valid PostgreSQL query without anything comment, explanation or anything else after the query.""",
    input_variables=[
        "input_question",
        "table_info",
        "columns_info",
        "top_k",
        "no_answer_text",
        "business_context",
    ],
    example_separator="\n\n",
)

_NO_ANSWER_TEXT = "I can't answer this question."


def call_sql_api(sql_query: str):
    load_dotenv()
    CONN_STR = os.environ["DATABASE_URL"]

    # Initializing Cube SQL API connection)
    connection = psycopg2.connect(CONN_STR)

    cursor = connection.cursor()
    cursor.execute(sql_query)

    columns = [desc[0] for desc in cursor.description]
    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return columns, rows


def create_docs_from_values(columns_values, table_name, column_name):
    value_docs = []

    for column_value in columns_values:
        print(column_value)
        metadata = dict(
            table_name=table_name,
            column_name=column_name,
        )

        page_content = column_value
        value_docs.append(Document(page_content=page_content, metadata=metadata))

    return value_docs

def create_chart_from_data(df):
    # Check for datetime, numeric, and categorical columns
    has_datetime = not df.select_dtypes(include=["datetime"]).empty
    has_numeric = not df.select_dtypes(include=["number"]).empty
    has_categorical = not df.select_dtypes(include=["object"]).empty

    # Get datetime column and convert to date
    if has_datetime:
        date_col = df.select_dtypes(include=["datetime"]).columns[0]
        df[date_col] = df[date_col].dt.date
        df = df.sort_values(date_col)

    # Get numeric columns
    if has_numeric:
        numeric_cols = []
        for i, col in enumerate(df.select_dtypes(include=["number"])):
            if not col.endswith("_id"):
                numeric_cols.append(col)

    # Get categorical columns
    if has_categorical:
        categorical_cols = []
        for i, col in enumerate(df.select_dtypes(include=["object"])):
            if (has_datetime and col != date_col) or (not has_datetime):
                categorical_cols.append(col)

    # If we have datetime, numeric several records
    with st.expander("Generated visualisation", expanded=True):
        match_chart = False
        if has_datetime and has_numeric and len(df.index) > 1:

            # If we have categorical, create a stacked area chart
            if has_categorical:
                match_chart = True
                if len(df[categorical_cols[0]].unique()) < 6:
                    title = f"{numeric_cols[0].replace('_', ' ')} by {categorical_cols[0].replace('_', ' ')} over time"
                    st.markdown(f"#### {title.capitalize()}")
                    st.area_chart(df, use_container_width=True, x=date_col, y=numeric_cols[0], color=categorical_cols[0])
                else:
                    # Get the top 5 categories with the most values
                    title = f"{numeric_cols[0].replace('_', ' ')} for top 5 {categorical_cols[0].replace('_', ' ')}"
                    st.markdown(f"#### {title.capitalize()}")
                    top_5 = df.groupby(categorical_cols[0], as_index=False).sum(numeric_cols[0]).sort_values(by=numeric_cols[0], ascending=False).head(5)[categorical_cols[0]].tolist()
                    st.area_chart(df[df[categorical_cols[0]].isin(top_5)], use_container_width=True, x=date_col, y=numeric_cols[0], color=categorical_cols[0])

            # If we have multiple numeric columns, create a line chart
            elif 1 < len(numeric_cols) < 5:
                match_chart = True
                title = f"{', '.join(numeric_cols).replace('_', ' ')} over time"
                st.markdown(f"#### {title.capitalize()}")
                st.line_chart(df, use_container_width=True, x=date_col)

            # If we have only one numeric column, create an area chart
            elif len(numeric_cols) == 1:
                match_chart = True
                title = f"{numeric_cols[0].replace('_', ' ')} over time"
                st.markdown(f"#### {title.capitalize()}")
                st.area_chart(df, use_container_width=True, x=date_col, y=numeric_cols[0])

        # If we have categorical and numeric, create a bar chart
        elif has_categorical and has_numeric and len(df.index) > 1:
            match_chart = True
            df = df.sort_values(by=numeric_cols[0], ascending=False)
            title = f"{numeric_cols[0].replace('_', ' ')} by {categorical_cols[0].replace('_', ' ')}"
            st.markdown(f"#### {title.capitalize()}")
            c = alt.Chart(df).mark_bar().encode(x=alt.X(categorical_cols[0], sort=None), y=numeric_cols[0])
            st.altair_chart(c, use_container_width=True)

    return df, match_chart

def sample_questions(selected_view):
    if selected_view in ["transactions", "events", "tax"]:
        st.markdown("## Few questions to try")
        if selected_view == "transactions":
            st.markdown("""
            - Monthly paid orders vs last year
            - Weekly free vs paid tickets in Q2 2025
            - Average ticket price by month for 2025
            """ )
        elif selected_view == "events":
            st.markdown("""
            - How many events were created last month?
            - Show me monthly hosting creators vs last year
            - Paid publishing creators by week Year to date
            """ )
        else:
            st.markdown("""
            - EB tax in USD in Q3 2025 where event payout country is 'US'
            - Creators with taxable GTV > 0 with event published in 2024
            """ )

def get_business_context(selected_view):
    if selected_view in ["transactions", "events", "tax"]:
        business_context = "There are some key concepts to keep in mind about the business: \n"
        if selected_view == "transactions":
            business_context += """
            - 'Transacted' is referring to both paid and free transactions.
            - If the question asks for paid or free measures like 'paid orders', 'paid tickets' or 'free publishing creators', you must use a measure with 'paid' or 'free' in the name.
            - 'Tickets' and 'items' are the same thing.
            - 'paid tickets' in a question translates to the measure 'paid_item_qty' in the query.
            - 'free tickets' in a question translates to the measure 'free_item_qty' in the query.
            - 'paid vs free tickets' in a question translates to the both 'paid_item_qty' and 'free_item_qty' measures in the query.
            """
        elif selected_view == "events":
            business_context += """
            - If the question asks for paid or free measures like 'paid publishing creators' or 'free published capacity', you must use a measure with 'paid' or 'free' in the name.
            """
        else:
            business_context += """
            - When the user asks for a measure in USD, look for the measure with '_usd' in the suffix.
            - If the user asks for local or native currency, look for the measure without '_usd' in the suffix.
            - When asked for an order level report or results per order, just use the order_id as a dimension. Same for event level report, use the event_id as a dimension.
            - If the question mentions a date range, use it against the trx_date column by default unless specified otherwise.
            - If the question does not specify the location type, use the event venue location by default.
            - 'event country' in the question translates to 'event_venue_country' in the query.
            - When 'currency' is asked as a dimension, use 'transaction_currency'.
            """
    else:
        business_context = ""

    return business_context
