import streamlit as st
import pandas as pd
import os
import re
import jwt
import numpy as np
from datetime import datetime
from sql_formatter.core import format_sql

from dotenv import load_dotenv
from langchain_openai import OpenAI
from langchain_openai.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import CubeSemanticLoader
from pathlib import Path

from utils import (
    check_input,
    call_sql_api,
    create_chart_from_data,
    sample_questions,
    load_example_queries,
    create_prompt_template,
    get_business_context,
    _NO_ANSWER_TEXT,
)

load_dotenv()

# Initialize session state for chat history and selected view
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'selected_view' not in st.session_state:
    st.session_state.selected_view = None

def add_to_chat_history(question, max_history=3):
    """Add question to chat history, keeping only last X"""
    st.session_state.chat_history.append(question)
    # Keep only the last X questions
    if len(st.session_state.chat_history) > max_history:
        st.session_state.chat_history = st.session_state.chat_history[-max_history:]

def get_available_views(vectorstore):
    """Get all available views from the vectorstore"""
    # Get all documents that are views
    docs = vectorstore.similarity_search("", k=1000, filter=dict(cube_data_obj_type="view"))

    # Extract unique table names
    views = set()
    for doc in docs:
        table_name = doc.metadata.get("table_name")
        if table_name:
            views.add(table_name)

    return sorted(list(views))

def ingest_cube_meta():
    security_context = {}
    token = jwt.encode(security_context, os.environ["CUBE_API_SECRET"], algorithm="HS256")

    loader = CubeSemanticLoader(os.environ["CUBE_API_URL"], token)
    documents = loader.load()

    embeddings = OpenAIEmbeddings()
    vectorstore = FAISS.from_documents(documents, embeddings)
    vectorstore.save_local("vectorstore.pkl")

if not Path("vectorstore.pkl").exists():
    with st.spinner('Loading context from Cube API...', show_time=True):
        ingest_cube_meta()

llm = OpenAI(
    temperature=0, openai_api_key=os.environ.get("OPENAI_API_KEY"), verbose=True
)

# Load vectorstore
if not Path("vectorstore.pkl").exists():
    st.error("vectorstore.pkl does not exist.")
    st.stop()

vectorstore = FAISS.load_local("vectorstore.pkl", OpenAIEmbeddings(), allow_dangerous_deserialization=True)

# View selection page
if st.session_state.selected_view is None:
    st.markdown("### What domain are you interested in?")

    # Get available views
    available_views = get_available_views(vectorstore)

    if not available_views:
        st.error("No views found in the vectorstore.")
        st.stop()

    # Create columns for better layout
    cols = st.columns(3)
    for i, view in enumerate(available_views):
        col = cols[i % 3]
        if col.button(view, key=f"view_{i}", use_container_width=True):
            st.session_state.selected_view = view
            st.rerun()

    st.stop()

# App titles
st.title("Eventbrite agentic analytics")
st.sidebar.markdown(f"## Selected domain: {st.session_state.selected_view}")

# Add option to change domain
if st.sidebar.button("Change domain", key="change_domain"):
    st.session_state.selected_view = None
    st.rerun()

# App side bar
with st.sidebar:
    sample_questions(st.session_state.selected_view)
    st.markdown("## Limitations")
    st.markdown("""
    - For now, context of previously asked questions is not considered.
    - Cube can't answer questions about forecasting nor causality yet
    """)

    # Chat History Section
    if st.session_state.chat_history and len(st.session_state.chat_history) > 0:
        st.markdown("---")
        st.markdown("## Previously Asked Questions")
        for i, question in enumerate(st.session_state.chat_history):
            with st.expander(f"{question[:30]}{'...' if len(question) > 30 else ''}"):
                st.markdown(question)

question = st.chat_input("Type your question and see if Cube gets the answer for you. ", key="input")

if question:

    # Check, record and display question
    check_input(question)
    add_to_chat_history(question)
    message = st.chat_message("user")
    message.write(question)

    # Get columns for the selected view
    table_name = st.session_state.selected_view
    docs = vectorstore.similarity_search(question, k=1000, filter=dict(cube_data_obj_type="view", table_name=table_name))

    lines = []
    for column_doc in docs:
        column_name = column_doc.metadata["column_name"]
        # Ignore columns ending with 'current_month', 'current_week' or 'iso'
        if not re.search(r"current_month|current_week|iso", column_name):
            lines.append(
                f"title: {column_doc.metadata['column_title']}\n"
                f"column name: {column_name}\n"
                f"description: {column_doc.metadata['column_description']}\n"
                f"datatype: {column_doc.metadata['column_data_type']}\n"
                f"member type: {column_doc.metadata['column_member_type']}"
            )
            print(column_name)
    columns = "\n\n".join(lines)

    # Create prompt template with the loaded examples
    prompt_template = create_prompt_template(table_name)

    # Construct the prompt
    prompt = prompt_template.format(
        input_question=question,
        table_info=table_name,
        columns_info=columns,
        top_k=1000,
        no_answer_text=_NO_ANSWER_TEXT,
        business_context=get_business_context(table_name),
    )

    # Call LLM API to get the SQL query
    with st.spinner('Translating your question into SQL', show_time=True):
        llm_answer = llm.invoke(prompt)

    if (_NO_ANSWER_TEXT in llm_answer.strip()):
        st.error(llm_answer)
        st.stop()

    sql_query = llm_answer.strip()
    with st.chat_message("ai"):
        with st.expander(label="Here is the query matching your question", expanded=True):
            st.code(format_sql(sql_query), language="sql")

        spinner = st.spinner('Getting the answer from Cube', show_time=True)
        spinner.__enter__()
        try:
            # Call Cube SQL API
            try:
                columns, rows = call_sql_api(sql_query)
                df = pd.DataFrame(rows, columns=columns)
            except Exception as e:
                st.error('Cube cannot execute the generated query. Please, try to rephrase your question.')
                with st.expander("Here is the error message from Cube", expanded=False):
                    st.code(str(e))
                st.stop()

            # Create chart from data if it makes sense
            df, match_chart = create_chart_from_data(df)

            with st.expander("And the query results", expanded=not match_chart):
                st.dataframe(df, hide_index=True, use_container_width=True)
        finally:
            spinner.__exit__(None, None, None)

# TODO:
# Keep context from a previous question
