import streamlit as st
st.title("Análisis de Plantillas de Fútbol IA")

# REAL MADRID
url_escudo_rm = "https://upload.wikimedia.org/wikipedia/en/5/56/Real_Madrid_CF.svg"
st.image(url_escudo_rm, width=150)
if st.button("Real Madrid"):
    st.write("Has hecho clic en Real Madrid")
