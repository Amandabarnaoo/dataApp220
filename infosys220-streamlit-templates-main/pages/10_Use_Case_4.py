import streamlit as st
from streamlit_gsheets import GSheetsConnection

st.title("UC4 | Manage Advertising | F2: Create Custom Ads")

# edit this to a suitable url
url = "https://docs.google.com/spreadsheets/d/1cvBrKIwSECxpIGHMD9J-HuWWnhUnR1oBPlOn7y_q52A/edit#gid=569583629"

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
