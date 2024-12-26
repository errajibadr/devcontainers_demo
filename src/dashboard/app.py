import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(page_title="DataPilot Dashboard", layout="wide")

st.title("DataPilot - Tableau de bord financier")

# Sidebar pour les contrôles
st.sidebar.title("Contrôles")
selected_symbol = st.sidebar.text_input("Symbole boursier", value="AAPL")

# Zone principale
st.header(f"Analyse de {selected_symbol}")

# Placeholder pour les données (à implémenter)
st.info("Connectez-vous à l'API pour charger les données en temps réel")
