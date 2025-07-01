import streamlit as st
st.title("Análisis de Plantillas de Fútbol IA")

# Diccionario con escudos y rutas a CSV
equipos = {
    "Real Madrid": {
        "escudo": "https://upload.wikimedia.org/wikipedia/en/5/56/Real_Madrid_CF.svg",
        #"csv": "real_madrid.csv"
    },
    "Barcelona": {
        "escudo": "https://upload.wikimedia.org/wikipedia/en/4/47/FC_Barcelona_%28crest%29.svg",
        #"csv": "barcelona.csv"
    },
    "Atlético de Madrid": {
        "escudo": "https://upload.wikimedia.org/wikipedia/en/f/f4/Atletico_Madrid_2017_logo.svg",
        #"csv": "atletico.csv"
    }
}
