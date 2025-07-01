import streamlit as st
import pandas as pd

st.title("Analizador de Plantilas")

# Ruta relativa al CSV
#ruta_csv = "data.csv"

# Lista de equipos y sus archivos CSV correspondientes
equipos = {
    "Real Madrid": "real_madrid.csv",
    "Barcelona": "barcelona.csv",
    "Atlético de Madrid": "atletico.csv",
    # añade más equipos aquí
}

# Selector para el equipo
equipo_seleccionado = st.selectbox("Selecciona un equipo", list(equipos.keys()))

# Cargar CSV según equipo seleccionado
ruta_csv = equipos[equipo_seleccionado]

try:
    df = pd.read_csv(ruta_csv)
    st.write(f"Plantilla de {equipo_seleccionado}")
    st.dataframe(df)
except FileNotFoundError:
    st.error(f"No se encontró el archivo para {equipo_seleccionado}")
