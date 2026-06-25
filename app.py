import streamlit as st
import pandas as pd
import numpy as np
import os
from io import StringIO

# Configuración inicial de la aplicación
st.set_page_config(page_title="Polla Mundialista UNAD Chipaque", layout="wide", page_icon="⚽")

st.title("⚽ Polla Mundialista 2026 - UNAD Chipaque")

# 📝 LISTA OFICIAL DE TU GRUPO DE APOSTADORES
NOMBRES_APOSTADORES = [
    "Lizeth", "Kevin", "Yudi", "Diana", "Yaritza", 
    "Álvaro", "Francisco", "Harold", "Alejandra", "Karina", "Milena"
]

ARCHIVO_DATOS = "datos_polla_2026.csv"

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
        {"Detalle": "19/06/2026", "Partido": "EE.UU. vs Australia"},
        {"Detalle": "20/06/2026", "Partido": "Alemania vs Costa de Marfil"},
        {"Detalle": "20/06/2026", "Partido": "Ecuador vs Curazao"},
        {"Detalle": "20/06/2026", "Partido": "Países Bajos vs Suecia"},
        {"Detalle": "20/06/2026", "Partido": "Túnez vs Japón"},
        {"Detalle": "21/06/2026", "Partido": "Bélgica vs Irán"},
        {"Detalle": "21/06/2026", "Partido": "Nueva Zelanda vs Egipto"},
        {"Detalle": "21/06/2026", "Partido": "España vs Arabia Saudita"},
        {"Detalle": "21/06/2026", "Partido": "Uruguay vs Cabo Verde"},
        {"Detalle": "22/06/2026", "Partido": "Francia vs Irak"},
        {"Detalle": "22/06/2026", "Partido": "Noruega vs Senegal"},
        {"Detalle": "22/06/2026", "Partido": "Argentina vs Austria"},
        {"Detalle": "22/06/2026", "Partido": "Jordania vs Argelia"},
        {"Detalle": "23/06/2026", "Partido": "Portugal vs Uzbekistán"},
        {"Detalle": "23/06/2026", "Partido": "Colombia vs Rep. Democ. del Congo"},
        {"Detalle": "23/06/2026", "Partido": "Inglaterra vs Ghana"},
        {"Detalle": "23/06/2026", "Partido": "Panamá vs Croacia"},
        {"Detalle": "24/06/2026", "Partido": "República Checa vs México"},
        {"Detalle": "24/06/2026", "Partido": "Sudáfrica vs Corea del Sur"},
        {"Detalle": "24/06/2026", "Partido": "Suiza vs Canadá"},
        {"Detalle": "24/06/2026", "Partido": "Bosnia y Herzegovina vs Qatar"},
        {"Detalle": "24/06/2026", "Partido": "Escocia vs Brasil"},
        {"Detalle": "24/06/2026", "Partido": "Marruecos vs Haití"},
        {"Detalle": "25/06/2026", "Partido": "Turquía vs EE.UU."},
        {"Detalle": "25/06/2026", "Partido": "Paraguay vs Australia"},
        {"Detalle": "25/06/2026", "Partido": "Ecuador vs Alemania"},
        {"Detalle": "25/06/2026", "Partido": "Curazao vs Costa de Marfil"},
        {"Detalle": "25/06/2026", "Partido": "Túnez vs Países Bajos"},
        {"Detalle": "25/06/2026", "Partido": "Japón vs Suecia"},
        {"Detalle": "26/06/2026", "Partido": "Nueva Zelanda vs Bélgica"},
        {"Detalle": "26/06/2026", "Partido": "Egipto vs Irán"},
        {"Detalle": "26/06/2026", "Partido": "Uruguay vs España"},
        {"Detalle": "26/
