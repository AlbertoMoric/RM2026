import streamlit as st
import pandas as pd

# URL plantilla Real Madrid
url_csv_rm = "https://raw.githubusercontent.com/tu_usuario/tu_repositorio/main/data/real_madrid.csv"
url_escudo_rm = "https://upload.wikimedia.org/wikipedia/en/5/56/Real_Madrid_CF.svg"

# Inicializamos el estado para controlar la "página"
if "pagina" not in st.session_state:
    st.session_state.pagina = "home"

def mostrar_home():
    st.title("Plantillas de LaLiga")
    st.image(url_escudo_rm, width=150)
    if st.button("Real Madrid"):
        st.session_state.pagina = "real_madrid"
        #st.experimental_rerun()  # Recarga la app para mostrar la página nueva

def mostrar_real_madrid():
    st.title("Plantilla Real Madrid")
    try:
        df = pd.read_csv(url_csv_rm)
        st.dataframe(df)
    except Exception as e:
        st.error(f"No se pudo cargar la plantilla: {e}")
    if st.button("Volver"):
        st.session_state.pagina = "home"
        st.experimental_rerun()

# Lógica para mostrar la página correcta
if st.session_state.pagina == "home":
    mostrar_home()
elif st.session_state.pagina == "real_madrid":
    mostrar_real_madrid()

