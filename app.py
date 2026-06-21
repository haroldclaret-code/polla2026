import streamlit as st
import pandas as pd
import numpy as np
import os

# Configuración inicial de la aplicación
st.set_page_config(page_title="Polla Mundialista 2026", layout="wide", page_icon="⚽")

st.title("⚽ Polla Mundialista 2026 - Sistema Profesional")

# 📝 LISTA OFICIAL DE TU GRUPO DE APOSTADORES
NOMBRES_APOSTADORES = [
    "Lizeth", "Kevin", "Yudi", "Diana", "Yaritza", 
    "Álvaro", "Francisco", "Harold", "Alejandra", "Karina", "Milena"
]

ARCHIVO_DATOS = "datos_polla_2026.csv"

# 🛠️ CONSTRUCCIÓN COMPLETA DEL FIXTURE OFICIAL EXTRAÍDO DE TUS IMÁGENES
def generar_fixture_oficial_total():
    partidos = []
    
    partidos_grupos_origen = [
        # --- FECHA 1 ---
        {"Detalle": "11/06/2026", "Partido": "México vs Sudáfrica"},
        {"Detalle": "11/06/2026", "Partido": "Corea del Sur vs República Checa"},
        {"Detalle": "12/06/2026", "Partido": "Canadá vs Bosnia y Herzegovina"},
        {"Detalle": "12/06/2026", "Partido": "EE.UU. vs Paraguay"},
        {"Detalle": "13/06/2026", "Partido": "Qatar vs Suiza"},
        {"Detalle": "13/06/2026", "Partido": "Brasil vs Marruecos"},
        {"Detalle": "13/06/2026", "Partido": "Haití vs Escocia"},
        {"Detalle": "13/06/2026", "Partido": "Australia vs Turquía"},
        {"Detalle": "14/06/2026", "Partido": "Alemania vs Curazao"},
        {"Detalle": "14/06/2026", "Partido": "Costa de Marfil vs Ecuador"},
