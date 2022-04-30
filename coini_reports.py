import streamlit as st
import pickle

def coini():
    st.write('Everything')
    uploaded_file = st.file_uploader("Upload")

    filename = 'dogs.pickle'
    outfile = open(filename, 'wb')

    pickle.dump(uploaded_file, outfile)
    outfile.close()

