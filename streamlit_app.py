import streamlit as st
import pandas as pd
import numpy as np
from openpyxl import load_workbook

# Streamlit Page Config has to be first thing in script

st.set_page_config(
    page_title="old-ancient-axe",
    page_icon=None,
    layout="centered",
    initial_sidebar_state="auto",
)

# Local functions

def get_sheet_names(wb):
    return [sheetname for sheetname in wb.sheetnames]

def extract_named_tables(sheetname):
    named_tables = []
    sheet = wb[sheetname]
    if sheet.tables.keys() is not None:
        return sheet.tables.keys()
    else:
        return "No named tables in sheet"

# Define sidebar class (for ease of tracking/grouping controls)
class SideBar:
    uploaded_file = st.empty()
    workbook_name = ""
    sheet_select = st.empty()


# Start App layout

st.title("No Data in Excel - Prototype App")

sb = SideBar()

sb.uploaded_file = st.sidebar.file_uploader("Upload Files", type=["xlsx"])

if sb.uploaded_file is not None:
    st.write(sb.uploaded_file.name)
    wb = load_workbook(filename=sb.uploaded_file)
#    file_details = {
#        "FileName": uploaded_file.name,
#        "FileType": uploaded_file.type,
#        "FileSize": uploaded_file.size,
#    }
#    st.write(file_details)
    sheetnames = get_sheet_names(wb)
    sb.sheet_select = st.sidebar.radio('Worksheets:', sheetnames, 0)

st.header(sb.sheet_select)
st.write(extract_named_tables(sb.sheet_select))


# st.write(named_tables)

# See https://databooth.slite.com/api/s/note/KFoQMJupyw4ix32aSHqvdr/old-ancient-axe-No-Data-in-Excel-app-ideas