import streamlit as st
import pandas as pd
import numpy as np
import os

# Configuración inicial de la aplicación
st.set_page_config(page_title="Polla Mundialista UNAD Chipaque", layout="wide", page_icon="⚽")

st.title("⚽ Polla Mundialista 2026 - UNAD Chipaque")

# 📝 LISTA OFICIAL DE TU GRUPO DE APOSTADORES
NOMBRES_APOSTADORES = [
    "Lizeth", "Kevin", "Yudi", "Diana", "Yaritza", 
    "Álvaro", "Francisco", "Harold", "Alejandra", "Karina", "Milena"
]

ARCHIVO_DATOS = "datos_polla_2026.csv"

# Función auxiliar para forzar la conversión visual a enteros limpios sin .0
def limpiar_enteros(val):
    if val == "" or pd.isna(val):
        return ""
    try:
        return str(int(float(val)))
    except:
        return str(val)

# 🛠️ CONSTRUCCIÓN DEL FIXTURE
def generar_fixture_oficial_total():
    partidos = []
    partidos_grupos_origen = [
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
        {"Detalle": "14/06/2026", "Partido": "Países Bajos vs Japón"},
        {"Detalle": "14/06/2026", "Partido": "Suecia vs Túnez"},
        {"Detalle": "15/06/2026", "Partido": "Bélgica vs Egipto"},
        {"Detalle": "15/06/2026", "Partido": "Irán vs Nueva Zelanda"},
        {"Detalle": "15/06/2026", "Partido": "España vs Cabo Verde"},
        {"Detalle": "15/06/2026", "Partido": "Arabia Saudita vs Uruguay"},
        {"Detalle": "16/06/2026", "Partido": "Francia vs Senegal"},
        {"Detalle": "16/06/2026", "Partido": "Irak vs Noruega"},
        {"Detalle": "16/06/2026", "Partido": "Argentina vs Argelia"},
        {"Detalle": "16/06/2026", "Partido": "Austria vs Jordania"},
        {"Detalle": "17/06/2026", "Partido": "Portugal vs Rep. Democ. del Congo"},
        {"Detalle": "17/06/2026", "Partido": "Uzbekistán vs Colombia"},
        {"Detalle": "17/06/2026", "Partido": "Inglaterra vs Croacia"},
        {"Detalle": "17/06/2026", "Partido": "Ghana vs Panamá"},
        {"Detalle": "18/06/2026", "Partido": "República Checa vs Sudáfrica"},
        {"Detalle": "18/06/2026", "Partido": "México vs Corea del Sur"},
        {"Detalle": "18/06/2026", "Partido": "Suiza vs Bosnia y Herzegovina"},
        {"Detalle": "18/06/2026", "Partido": "Canadá vs Qatar"},
        {"Detalle": "19/06/2026", "Partido": "Brasil vs Haití"},
        {"Detalle": "19/06/2026", "Partido": "Escocia vs Marruecos"},
        {"Detalle": "19/06/2026", "Partido": "Turquía vs Paraguay"},
        {"Detalle": "19/06/2026", "Partido": "EE.UU. vs
