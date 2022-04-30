import streamlit as st
import pandas as pd

def coini():
    st.write('Everything')
    uploaded_file = st.file_uploader("Upload CSV", type=".xlsx")

    if uploaded_file:
        df = pd.read_excel(uploaded_file, index_col=3)
        st.dataframe(df)

