import streamlit as st
import pandas as pd
import numpy as np
import spacy
import spacy_transformers

st.title('Analizador de curriculos')

uploaded_files = st.file_uploader("Ingresa los currículos a analizar", type=["pdf"],accept_multiple_files=True)
for uploaded_file in uploaded_files:
     bytes_data = uploaded_file.read()
     st.write("filename:", uploaded_file.name)
    # st.write(bytes_data)

df = pd.read_json('jsonformatter.txt')

options = st.multiselect(
     'Ingresa las habilidades que está buscando',
     df['name'].values,
     None)

st.write('Opciones seleccionadas:', options)

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')