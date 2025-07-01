import streamlit as st
st.title("Análisis de Plantillas de Fútbol IA")
import streamlit as st
import pandas as pd

# Diccionario con equipos, escudos y URLs de CSV
equipos = {
    "Real Madrid": {
        "escudo": "https://upload.wikimedia.org/wikipedia/en/5/56/Real_Madrid_CF.svg",
        "csv": "https://raw.githubusercontent.com/tu_usuario/tu_repositorio/main/data/real_madrid.csv"
    },
    "Barcelona": {
        "escudo": "https://upload.wikimedia.org/wikipedia/en/4/47/FC_Barcelona_%28crest%29.svg",
        "csv": "https://raw.githubusercontent.com/tu_usuario/tu_repositorio/main/data/barcelona.csv"
    },
    "Atlético de Madrid": {
        "escudo": "https://upload.wikimedia.org/wikipedia/en/f/f4/Atletico_Madrid_2017_logo.svg",
        "csv": "https://raw.githubusercontent.com/tu_usuario/tu_repositorio/main/data/atletico.csv"
    },
}
