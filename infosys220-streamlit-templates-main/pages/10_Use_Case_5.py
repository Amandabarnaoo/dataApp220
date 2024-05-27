import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("UC5 | Manage Search | F1: Apply Filters")

# edit this to a suitable url
url = "https://docs.google.com/spreadsheets/d/1cvBrKIwSECxpIGHMD9J-HuWWnhUnR1oBPlOn7y_q52A/edit#gid=285238946"

conn = st.connection(
    "gsheets",
    type=GSheetsConnection,
)

# edit this to store the result in a dataframe
spreadsheetData = conn.read(spreadsheet=url)

st.dataframe(
    spreadsheetData,  # edit this to show the dataframe from above
    hide_index=True,
)
