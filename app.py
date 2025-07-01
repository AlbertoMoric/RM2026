import streamlit as st
import pandas as pd
st.title("Analista de Plantillas Inteligente")
#SELECCIONAR EQUIPOS
escudos = {
    "Alavés": {
        "url": "https://upload.wikimedia.org/wikipedia/en/7/76/Deportivo_Alav%C3%A9s_logo.svg",
        "csv": "data/alaves.csv"
    },
    "Athletic Club": {
        "url": "https://upload.wikimedia.org/wikipedia/en/1/19/Athletic_Bilbao_logo.svg",
        "csv": "data/athletic_club.csv"
    },
    "Atlético de Madrid": {
        "url": "https://upload.wikimedia.org/wikipedia/en/f/f4/Atletico_Madrid_2017_logo.svg",
        "csv": "data/atletico.csv"
    },
    "Barcelona": {
        "url": "https://upload.wikimedia.org/wikipedia/en/4/47/FC_Barcelona_%28crest%29.svg",
        "csv": "data/barcelona.csv"
    },
    "Cádiz": {
        "url": "https://upload.wikimedia.org/wikipedia/en/9/97/Cadiz_CF_logo.svg",
        "csv": "data/cadiz.csv"
    },
    "Celta de Vigo": {
        "url": "https://upload.wikimedia.org/wikipedia/en/c/c6/Celta_de_Vigo_logo.svg",
        "csv": "data/celta_de_vigo.csv"
    },
    "Elche": {
        "url": "https://upload.wikimedia.org/wikipedia/en/6/6d/Elche_CF_logo.svg",
        "csv": "data/elche.csv"
    },
    "Espanyol": {
        "url": "https://upload.wikimedia.org/wikipedia/en/4/44/RCD_Espanyol_logo.svg",
        "csv": "data/espanyol.csv"
    },
    "Getafe": {
        "url": "https://upload.wikimedia.org/wikipedia/en/e/e2/Getafe_CF_logo.svg",
        "csv": "data/getafe.csv"
    },
    "Girona": {
        "url": "https://upload.wikimedia.org/wikipedia/en/f/f0/Girona_FC_logo.svg",
        "csv": "data/girona.csv"
    },
    "Granada": {
        "url": "https://upload.wikimedia.org/wikipedia/en/8/82/Granada_CF_logo.svg",
        "csv": "data/granada.csv"
    },
    "Las Palmas": {
        "url": "https://upload.wikimedia.org/wikipedia/en/c/c6/UD_Las_Palmas_logo.svg",
        "csv": "data/las_palmas.csv"
    },
    "Mallorca": {
        "url": "https://upload.wikimedia.org/wikipedia/en/f/f2/RCD_Mallorca_logo.svg",
        "csv": "data/mallorca.csv"
    },
    "Osasuna": {
        "url": "https://upload.wikimedia.org/wikipedia/en/d/d7/CA_Osasuna_logo.svg",
        "csv": "data/osasuna.csv"
    },
    "Rayo Vallecano": {
        "url": "https://upload.wikimedia.org/wikipedia/en/f/fd/Rayo_Vallecano_logo.svg",
        "csv": "data/rayo_vallecano.csv"
    },
    "Real Betis": {
        "url": "https://upload.wikimedia.org/wikipedia/en/f/f1/Real_Betis_logo.svg",
        "csv": "data/real_betis.csv"
    },
    "Real Madrid": {
        "url": "https://upload.wikimedia.org/wikipedia/en/5/56/Real_Madrid_CF.svg",
        "csv": "data/real_madrid.csv"
    },
    "Real Sociedad": {
        "url": "https://upload.wikimedia.org/wikipedia/en/0/0e/Real_Sociedad_logo.svg",
        "csv": "data/real_sociedad.csv"
    },
    "Sevilla": {
        "url": "https://upload.wikimedia.org/wikipedia/en/7/7a/Sevilla_FC_logo.svg",
        "csv": "data/sevilla.csv"
    },
    "Valencia": {
        "url": "https://upload.wikimedia.org/wikipedia/en/7/7f/Valenciacf.svg",
        "csv": "data/valencia.csv"
    },
    "Villarreal": {
        "url": "https://upload.wikimedia.org/wikipedia/en/f/f5/Villarreal_CF_logo.svg",
        "csv": "data/villarreal.csv"
    }
}
cols = st.columns(len(escudos))
for i, (equipo, info) in enumerate(escudos.items()):
    cols[i].image(info["url"], width=100)
    if cols[i].button(equipo):
        try:
            df = pd.read_csv(info["csv"])
            st.write(f"### Plantilla de {equipo}")
            st.dataframe(df)
        except Exception as e:
            st.error(f"No se pudo cargar la plantilla de {equipo}: {e}")
