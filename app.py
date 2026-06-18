import streamlit as st
import pandas as pd
import numpy as np
import os

# Configuración inicial de la página web
st.set_page_config(page_title="Polla Mundialista 2026", layout="wide", page_icon="⚽")

st.title("⚽ Sistema Oficial - Polla Mundialista 2026")
st.sidebar.header("⚙️ Panel de Administración (Solo Tú)")
password = st.sidebar.text_input("Contraseña de Administrador", type="password")

ARCHIVO_DATOS = "datos_polla_2026.csv"

# 📝 LISTA OFICIAL DE TU GRUPO
NOMBRES_APOSTADORES = [
    "Lizeth", "Kevin", "Yudi", "Diana", "Yaritza", 
    "Álvaro", "Francisco", "Harold", "Alejandra", "Karina", "Milena"
]

# 1. FUNCIÓN CON EL FIXTURE REAL COMPLETO Y ABREVIADO
def cargar_o_inicializar_datos():
    if os.path.exists(ARCHIVO_DATOS):
        return pd.read_csv(ARCHIVO_DATOS)
    
    partidos_reales = [
        # --- JORNADA 1 ---
        {"ID": "P1", "Fase": "Fase de Grupos", "Partido": "Méx vs A2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P2", "Fase": "Fase de Grupos", "Partido": "A3 vs A4", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P3", "Fase": "Fase de Grupos", "Partido": "Can vs B2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P4", "Fase": "Fase de Grupos", "Partido": "B3 vs B4", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P5", "Fase": "Fase de Grupos", "Partido": "USA vs D2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P6", "Fase": "Fase de Grupos", "Partido": "D3 vs D4", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P7", "Fase": "Fase de Grupos", "Partido": "C1 vs C2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P8", "Fase": "Fase de Grupos", "Partido": "C3 vs C4", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P9", "Fase": "Fase de Grupos", "Partido": "E1 vs E2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P10", "Fase": "Fase de Grupos", "Partido": "E3 vs E4", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P11", "Fase": "Fase de Grupos", "Partido": "F1 vs F2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P12", "Fase": "Fase de Grupos", "Partido": "F3 vs F4", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P13", "Fase": "Fase de Grupos", "Partido": "G1 vs G2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P14", "Fase": "Fase de Grupos", "Partido": "G3 vs G4", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P15", "Fase": "Fase de Grupos", "Partido": "H1 vs H2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P16", "Fase": "Fase de Grupos", "Partido": "H3 vs H4", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P17", "Fase": "Fase de Grupos", "Partido": "I1 vs I2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P18", "Fase": "Fase de Grupos", "Partido": "I3 vs I4", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P19", "Fase": "Fase de Grupos", "Partido": "J1 vs J2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P20", "Fase": "Fase de Grupos", "Partido": "J3 vs J4", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P21", "Fase": "Fase de Grupos", "Partido": "K1 vs K2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P22", "Fase": "Fase de Grupos", "Partido": "K3 vs K4", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P23", "Fase": "Fase de Grupos", "Partido": "L1 vs L2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P24", "Fase": "Fase de Grupos", "Partido": "L3 vs L4", "Goles_Real_1": "", "Goles_Real_2": ""},

        # --- JORNADA 2 ---
        {"ID": "P25", "Fase": "Fase de Grupos", "Partido": "Méx vs A3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P26", "Fase": "Fase de Grupos", "Partido": "A4 vs A2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P27", "Fase": "Fase de Grupos", "Partido": "B4 vs B2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P28", "Fase": "Fase de Grupos", "Partido": "Can vs B3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P29", "Fase": "Fase de Grupos", "Partido": "USA vs D3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P30", "Fase": "Fase de Grupos", "Partido": "D4 vs D2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P31", "Fase": "Fase de Grupos", "Partido": "C4 vs C2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P32", "Fase": "Fase de Grupos", "Partido": "C1 vs C3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P33", "Fase": "Fase de Grupos", "Partido": "E4 vs E2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P34", "Fase": "Fase de Grupos", "Partido": "E1 vs E3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P35", "Fase": "Fase de Grupos", "Partido": "F4 vs F2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P36", "Fase": "Fase de Grupos", "Partido": "F1 vs F3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P37", "Fase": "Fase de Grupos", "Partido": "G4 vs G2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P38", "Fase": "Fase de Grupos", "Partido": "G1 vs G3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P39", "Fase": "Fase de Grupos", "Partido": "H4 vs H2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P40", "Fase": "Fase de Grupos", "Partido": "H1 vs H3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P41", "Fase": "Fase de Grupos", "Partido": "I4 vs I2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P42", "Fase": "Fase de Grupos", "Partido": "I1 vs I3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P43", "Fase": "Fase de Grupos", "Partido": "J4 vs J2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P44", "Fase": "Fase de Grupos", "Partido": "J1 vs J3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P45", "Fase": "Fase de Grupos", "Partido": "K4 vs K2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P46", "Fase": "Fase de Grupos", "Partido": "K1 vs K3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P47", "Fase": "Fase de Grupos", "Partido": "L4 vs L2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P48", "Fase": "Fase de Grupos", "Partido": "L1 vs L3", "Goles_Real_1": "", "Goles_Real_2": ""},

        # --- JORNADA 3 ---
        {"ID": "P49", "Fase": "Fase de Grupos", "Partido": "A2 vs A3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P50", "Fase": "Fase de Grupos", "Partido": "A4 vs Méx", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P51", "Fase": "Fase de Grupos", "Partido": "B2 vs B3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P52", "Fase": "Fase de Grupos", "Partido": "B4 vs Can", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P53", "Fase": "Fase de Grupos", "Partido": "C2 vs C3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P54", "Fase": "Fase de Grupos", "Partido": "C4 vs C1", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P55", "Fase": "Fase de Grupos", "Partido": "D2 vs D3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P56", "Fase": "Fase de Grupos", "Partido": "D4 vs USA", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P57", "Fase": "Fase de Grupos", "Partido": "E2 vs E3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P58", "Fase": "Fase de Grupos", "Partido": "E4 vs E1", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P59", "Fase": "Fase de Grupos", "Partido": "F2 vs F3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P60", "Fase": "Fase de Grupos", "Partido": "F4 vs F1", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P61", "Fase": "Fase de Grupos", "Partido": "G2 vs G3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P62", "Fase": "Fase de Grupos", "Partido": "G4 vs G1", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P63", "Fase": "Fase de Grupos", "Partido": "H2 vs H3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P64", "Fase": "Fase de Grupos", "Partido": "H4 vs H1", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P65", "Fase": "Fase de Grupos", "Partido": "I2 vs I3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P66", "Fase": "Fase de Grupos", "Partido": "I4 vs I1", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P67", "Fase": "Fase de Grupos", "Partido": "J2 vs J3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P68", "Fase": "Fase de Grupos", "Partido": "J4 vs J1", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P69", "Fase": "Fase de Grupos", "Partido": "K2 vs K3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P70", "Fase": "Fase de Grupos", "Partido": "K4 vs K1", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P71", "Fase": "Fase de Grupos", "Partido": "L2 vs L3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P72", "Fase": "Fase de Grupos", "Partido": "L4 vs L1", "Goles_Real_1": "", "Goles_Real_2": ""},
    ]
    
    df_partidos = pd.DataFrame(partidos_reales)
    
    # Agregar las llaves de eliminación directa simplificadas
    llaves = []
    for i in range(73, 89):
        llaves.append({"ID": f"P{i}", "Fase": "Dieciseisavos", "Partido": f"Llave {i-72}", "Goles_Real_1": "", "Goles_Real_2": ""})
    for i in range(89, 97):
        llaves.append({"ID": f"P{i}", "Fase": "Octavos de Final", "Partido": f"Octavos {i-88}", "Goles_Real_1": "", "Goles_Real_2": ""})
    for i in range(97, 101):
        llaves.append({"ID": f"P{i}", "Fase": "Cuartos de Final", "Partido": f"Cuartos {i-96}", "Goles_Real_1": "", "Goles_Real_2": ""})
    llaves.append({"ID": "P101", "Fase": "Semifinal", "Partido": "Semifinal 1", "Goles_Real_1": "", "Goles_Real_2": ""})
    llaves.append({"ID": "P102", "Fase": "Semifinal", "Partido": "Semifinal 2", "Goles_Real_1": "", "Goles_Real_2": ""},)
    llaves.append({"ID": "P103", "Fase": "Tercer Puesto", "Partido": "Tercer Puesto", "Goles_Real_1": "", "Goles_Real_2": ""})
    llaves.append({"ID": "P104", "Fase": "Gran Final", "Partido": "Gran Final 🏆", "Goles_Real_1": "", "Goles_Real_2": ""})
