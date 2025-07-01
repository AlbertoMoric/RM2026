import streamlit as st

st.title("Analista de Plantillas Inteligente")

# URLs de los escudos
escudos = {
    "Real Madrid": {
        "url": "https://upload.wikimedia.org/wikipedia/en/5/56/Real_Madrid_CF.svg",
        "csv": "Data/Real Madrid.csv"
    },
    "Barcelona": {
        "url": "https://upload.wikimedia.org/wikipedia/en/4/47/FC_Barcelona_%28crest%29.svg",
        #"csv": "Data/barcelona.csv"
    },
    "Atlético de Madrid": {
        "url": "https://upload.wikimedia.org/wikipedia/en/f/f4/Atletico_Madrid_2017_logo.svg",
        #"csv": "data/atletico.csv"
    },
}
cols = st.columns(len(escudos))

for i, (equipo, url) in enumerate(escudos.items()):
    cols[i].image(url, width=100)
    if cols[i].button(equipo):
        st.write(f"Has pulsado el botón de {equipo}")
