import streamlit as st
import pandas as pd
import numpy as np
from openpyxl import load_workbook

# from pathlib import Path

st.set_page_config(
    page_title="old-ancient-axe",
    page_icon=None,
    layout="centered",
    initial_sidebar_state="collapsed",
)

st.title("No Data in Excel - Prototype App")

uploaded_file = st.file_uploader("Upload Files", type=["xlsx"])

if uploaded_file is not None:
    file_details = {
        "FileName": uploaded_file.name,
        "FileType": uploaded_file.type,
        "FileSize": uploaded_file.size,
    }
    st.write(file_details)

wb = load_workbook(filename=uploaded_file)

named_tables = []
for name in wb.sheetnames:
    sheet = wb[name]
    if sheet.tables.keys() is not None:
        named_tables.append([name, sheet.tables.keys()])
    else:
        named_tables.append([name, 'No named tables in sheet'])

st.write(named_tables)

# See https://databooth.slite.com/api/s/note/KFoQMJupyw4ix32aSHqvdr/old-ancient-axe-No-Data-in-Excel-app-ideas