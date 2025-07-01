import streamlit as st

# URL de la imagen de fondo (puedes usar una URL pública o un archivo local con base64)
imagen_fondo_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/7/7f/La_Liga_logo.svg/1200px-La_Liga_logo.svg.png"

page_bg_img = f"""
<style>
.stApp {{
  background-image: url("{imagen_fondo_url}");
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  background-attachment: fixed;
}}
</style>
"""

st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("Análisis de Plantillas de Fútbol - LaLiga")
