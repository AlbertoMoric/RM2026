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

st.title("Análisis de Plantillas de LaLiga")

# Leer query params para saber si hay un equipo seleccionado
query_params = st.experimental_get_query_params()
equipo_seleccionado = query_params.get("equipo", [None])[0]

if equipo_seleccionado and equipo_seleccionado in equipos:
    # Mostrar plantilla del equipo seleccionado
    st.subheader(f"Plantilla de {equipo_seleccionado}")

    try:
        df = pd.read_csv(equipos[equipo_seleccionado]["csv"])
        st.dataframe(df)
    except Exception as e:
        st.error(f"No se pudo cargar la plantilla: {e}")

    if st.button("Volver a la selección de equipos"):
        st.experimental_set_query_params()  # Limpia los params para volver a home

else:
    st.write("Selecciona un equipo:")
    cols = st.columns(len(equipos))
    for equipo, info in equipos.items():
        cols[list(equipos.keys()).index(equipo)].image(info["escudo"], width=80)
        if cols[list(equipos.keys()).index(equipo)].button(equipo):
            st.experimental_set_query_params(equipo=equipo)
