import streamlit as st
import pickle

def coini():
    st.write('Everything')
    uploaded_file = st.file_uploader("Upload")

    df = pd.read_excel(uploaded_file, index_col=3)

    st.dataframe(df)

