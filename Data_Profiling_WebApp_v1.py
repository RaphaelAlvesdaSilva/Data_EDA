import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

# Web App Title
st.markdown('''
# **EDA WebApp**
Add an excel or csv file to run an **Exploratory Data Analysis** on the data
---
'''
)

# read file
def read_file(file):
    file_type = file.name.split(".")[-1]
    if file_type == "csv":
        df = pd.read_csv(file)
    elif file_type == "xlsx":
        sheets = pd.read_excel(file, sheet_name=None)
        sheet_names = list(sheets.keys())
        selected_sheet = st.sidebar.selectbox("Select a sheet", sheet_names)
        df = sheets[selected_sheet]
    else:
        st.error("Invalid file format. Only CSV and XLSX are supported.")
        df = None
    return df

# Upload data
with st.header("Upload file"):
    file = st.file_uploader("Upload a file", type=["csv", "xlsx"])

# Pandas Profiling Report
if file is not None:
    df = read_file(file)
    pr = ProfileReport(df, explorative=True)
    st.header('**Input DataFrame**')
    st.write(df)
    st.write('---')
    st.header('**Pandas Profiling Report**')
    st_profile_report(pr)
else:
    st.info('Awaiting for file to be uploaded.')