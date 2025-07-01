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


# Estado para equipo seleccionado
if "equipo_seleccionado" not in st.session_state:
    st.session_state.equipo_seleccionado = None

# Mostrar escudos como botones
cols = st.columns(len(equipos))
for i, (equipo, info) in enumerate(equipos.items()):
    if cols[i].button(equipo):
        st.session_state.equipo_seleccionado = equipo
    cols[i].image(info["escudo"], width=80)
    cols[i].caption(equipo)

# Mostrar plantilla si hay equipo seleccionado
if st.session_state.equipo_seleccionado:
    equipo = st.session_state.equipo_seleccionado
    st.subheader(f"Plantilla de {equipo}")
    try:
        df = pd.read_csv(equipos[equipo]["csv"])
        st.dataframe(df)
    except FileNotFoundError:
        st.error(f"No se encontró el archivo para {equipo}")
else:
    st.info("Selecciona un equipo haciendo click en su escudo para ver su plantilla.")
