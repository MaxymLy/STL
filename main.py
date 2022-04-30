import streamlit as st

from coini_reports import coini

if __name__ == '__main__':
    pwd = st.sidebar.text_input("Password:", value="", type="password")
    #if pwd == 'ggg534534gfdgdf':
    coini()
