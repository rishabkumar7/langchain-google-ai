import streamlit as st
import app as ai
import textwrap

st.title("Stoic AI Bot")

st.write("Welcome to Stoic AI Bot! I am here to help you.")

query = st.text_input(label="Ask your question", value="", max_chars=None)

if query:
    response = ai.help(query)
    st.write(response)