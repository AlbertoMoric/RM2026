import streamlit as st

st.title("Análisis de Plantillas de Fútbol IA")

# URLs de los escudos (ejemplo con algunos equipos)
escudos = {
    "Real Madrid": "https://upload.wikimedia.org/wikipedia/en/5/56/Real_Madrid_CF.svg",
    "Barcelona": "https://upload.wikimedia.org/wikipedia/en/4/47/FC_Barcelona_%28crest%29.svg",
    "Atlético de Madrid": "https://upload.wikimedia.org/wikipedia/en/f/f4/Atletico_Madrid_2017_logo.svg",
    # añade más aquí si quieres
}

# Mostrar escudos en columnas
cols = st.columns(len(escudos))
for i, (equipo, url) in enumerate(escudos.items()):
    cols[i].image(url, width=80)
    cols[i].caption(equipo)
