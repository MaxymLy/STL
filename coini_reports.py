import streamlit as st
import pandas as pd
import openpyxl


def coini():
    st.write('Everything')
    uploaded_file = st.file_uploader("Upload CSV", type=".xlsx")

    if uploaded_file:
        df = pd.read_excel(uploaded_file)
        st.dataframe(df)

        df.loc[df['Remarks'].isna(), ['Remarks']]

        st.dataframe(df.loc[df['Remarks'].isna(), ['KYC Status']])
