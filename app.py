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

# 📝 LISTA OFICIAL DE TUS COMPAÑEROS
NOMBRES_APOSTADORES = [
    "Lizeth", "Kevin", "Yudi", "Diana", "Yaritza", 
    "Álvaro", "Francisco", "Harold", "Alejandra", "Karina", "Milena"
]

# 1. FUNCIÓN CON EL CALENDARIO REAL ESTIPULADO POR LA FIFA
def cargar_o_inicializar_datos():
    if os.path.exists(ARCHIVO_DATOS):
        return pd.read_csv(ARCHIVO_DATOS)
    
    # Lista con el orden cronológico oficial de los partidos estipulados
    partidos_reales = [
        # Grupo A (Inaugurales y fixture)
        {"ID": "P1", "Fase": "Fase de Grupos", "Partido": "México vs A2 (Inaugural - Estadio Azteca)", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P2", "Fase": "Fase de Grupos", "Partido": "A3 vs A4", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P25", "Fase": "Fase de Grupos", "Partido": "México vs A3 (Guadalajara)", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P26", "Fase": "Fase de Grupos", "Partido": "A4 vs A2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P53", "Fase": "Fase de Grupos", "Partido": "A4 vs México (Estadio Azteca)", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P54", "Fase": "Fase de Grupos", "Partido": "A2 vs A3", "Goles_Real_1": "", "Goles_Real_2": ""},
        
        # Grupo B (Canadá y fixture)
        {"ID": "P3", "Fase": "Fase de Grupos", "Partido": "Canadá vs B2 (Inaugural Canadá - Toronto)", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P4", "Fase": "Fase de Grupos", "Partido": "B3 vs B4", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P27", "Fase": "Fase de Grupos", "Partido": "B4 vs B2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P28", "Fase": "Fase de Grupos", "Partido": "Canadá vs B3 (Vancouver)", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P55", "Fase": "Fase de Grupos", "Partido": "B2 vs B3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P56", "Fase": "Fase de Grupos", "Partido": "B4 vs Canadá (Vancouver)", "Goles_Real_1": "", "Goles_Real_2": ""},
        
        # Grupo D (Estados Unidos y fixture)
        {"ID": "P5", "Fase": "Fase de Grupos", "Partido": "Estados Unidos vs D2 (Inaugural USA - Los Ángeles)", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P6", "Fase": "Fase de Grupos", "Partido": "D3 vs D4", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P29", "Fase": "Fase de Grupos", "Partido": "Estados Unidos vs D3 (Seattle)", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P30", "Fase": "Fase de Grupos", "Partido": "D4 vs D2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P57", "Fase": "Fase de Grupos", "Partido": "D4 vs Estados Unidos (Los Ángeles)", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P58", "Fase": "Fase de Grupos", "Partido": "D2 vs D3", "Goles_Real_1": "", "Goles_Real_2": ""},
    ]
    
    # Rellenar automáticamente el resto de grupos (C, E, F, G, H, I, J, K, L) hasta completar los 72 de fase de grupos
    letras_grupos = ["C", "E", "F", "G", "H", "I", "J", "K", "L"]
    id_partido = 7
    for g in letras_grupos:
        partidos_reales.append({"ID": f"P{id_partido}", "Fase": "Fase de Grupos", "Partido": f"Grupo {g}: {g}1 vs {g}2", "Goles_Real_1": "", "Goles_Real_2": ""})
        partidos_reales.append({"ID": f"P{id_partido+1}", "Fase": "Fase de Grupos", "Partido": f"Grupo {g}: {g}3 vs {g}4", "Goles_Real_1": "", "Goles_Real_2": ""})
        partidos_reales.append({"ID": f"P{id_partido+24}", "Fase": "Fase de Grupos", "Partido": f"Grupo {g}: {g}4 vs {g}2", "Goles_Real_1": "", "Goles_Real_2": ""})
        partidos_reales.append({"ID": f"P{id_partido+25}", "Fase": "Fase de Grupos", "Partido": f"Grupo {g}: {g}1 vs {g}3", "Goles_Real_1": "", "Goles_Real_2": ""})
        partidos_reales.append({"ID": f"P{id_partido+48}", "Fase": "Fase de Grupos", "Partido": f"Grupo {g}: {g}2 vs {g}3", "Goles_Real_1": "", "Goles_Real_2": ""})
        partidos_reales.append({"ID": f"P{id_partido+49}", "Fase": "Fase de Grupos", "Partido": f"Grupo {g}: {g}4 vs {g}1", "Goles_Real_1": "", "Goles_Real_2": ""})
        id_partido += 2
        if id_partido == 25: id_partido = 31 # Ajuste para saltar los bloques ya mapeados de USA/Mex/Can
        if id_partido == 53: id_partido = 59
        
    # Ordenar por ID numérico para mantener la consistencia del fixture
    df_partidos = pd.DataFrame(partidos_reales)
    df_partidos["Num"] = df_partidos["ID"].str.extract(r'(\d+)').astype(int)
    df_partidos = df_partidos.sort_values(by="Num").drop(columns=["Num"])
    
    # Agregar las llaves de eliminación directa estipuladas por FIFA
    llaves = []
    for i in range(73, 89):
        llaves.append({"ID": f"P{i}", "Fase": "Dieciseisavos", "Partido": f"Llave Eliminatoria {i-72} (32avos de Final)", "Goles_Real_1": "", "Goles_Real_2": ""})
    for i in range(89, 97):
        llaves.append({"ID": f"P{i}", "Fase": "Octavos de Final", "Partido": f"Octavos de Final {i-88}", "Goles_Real_1": "", "Goles_Real_2": ""})
    for i in range(97, 101):
        llaves.append({"ID": f"P{i}", "Fase": "Cuartos de Final", "Partido": f"Cuartos de Final {i-96}", "Goles_Real_1": "", "Goles_Real_2": ""})
    llaves.append({"ID": "P101", "Fase": "Semifinal", "Partido": "Semifinal 1 (Dallas/Atlanta)", "Goles_Real_1": "", "Goles_Real_2": ""})
    llaves.append({"ID": "P102", "Fase": "Semifinal", "Partido": "Semifinal 2 (Dallas/Atlanta)", "Goles_Real_1": "", "Goles_Real_2": ""})
    llaves.append({"ID": "P103", "Fase": "Tercer Puesto", "Partido": "Partido por el Tercer Puesto (Miami)", "Goles_Real_1": "", "Goles_Real_2": ""})
    llaves.append({"ID": "P104", "Fase": "Gran Final", "Partido": "Gran Final del Mundial 2026 (Nueva York / New Jersey)", "Goles_Real_1": "", "Goles_Real_2": ""})
    
    df_llaves = pd.DataFrame(llaves)
    df_partidos = pd.concat([df_partidos, df_llaves], ignore_index=True)
    
    # Crear las columnas de apuestas para tus 11 amigos
    for nom in NOMBRES_APOSTADORES:
        df_partidos[f"{nom}_G1"] = ""
        df_partidos[f"{nom}_G2"] = ""
        
    df_partidos.to_csv(ARCHIVO_DATOS, index=False)
    return df_partidos

if "db" not in st.session_state:
    st.session_state.db = cargar_o_inicializar_datos()

# 2. SISTEMA MATEMÁTICO DE REGLAS
def calcular_puntos(r1, r2, p1, p2):
    if r1 == "" or r2 == "" or p1 == "" or p2 == "" or pd.isna(r1) or pd.isna(r2) or pd.isna(p1) or pd.isna(p2):
        return 0
    try:
        r1, r2, p1, p2 = int(r1), int(r2), int(p1), int(p2)
    except:
        return 0
    if r1 == p1 and r2 == p2:
        return 10
    ganador_real = 1 if r1 > r2 else (-1 if r1 < r2 else 0)
    ganador_pago = 1 if p1 > p2 else (-1 if p1 < p2 else 0)
    if ganador_real == ganador_pago:
        return 5
    if (r1 - r2) == (p1 - p2):
        return 2
    return 0

pestana = st.radio("Selecciona la Vista:", ["📋 Control de Partidos", "📊 Tabla de Posiciones Global", "🏆 Evolución y Premiación"], horizontal=True)

if pestana == "📋 Control de Partidos":
    st.subheader("Registro de Marcadores Reales y Pronósticos")
    fase_sel = st.selectbox("Filtrar por Fase del Torneo", st.session_state.db["Fase"].unique())
    df_filtrado = st.session_state.db[st.session_state.db["Fase"] == fase_sel]
    
    if password == "mundial2026":
        st.success("🔓 Modo Administrador Activado.")
        df_editado = st.data_editor(df_filtrado, hide_index=True)
        if st.button("💾 Guardar y Actualizar Polla Permanentemente"):
            st.session_state.db.update(df_editado)
            st.session_state.db.to_csv(ARCHIVO_DATOS, index=False)
            st.success("¡Datos guardados con éxito!")
            st.rerun()
    else:
        st.info("🔒 Vista de Solo Lectura para Apostadores.")
        st.dataframe(df_filtrado, hide_index=True)

elif pestana == "📊 Tabla de Posiciones Global":
    st.subheader("Puntajes Acumulados")
    puntajes = {}
    for nom in NOMBRES_APOSTADORES:
        total_puntos = 0
        for idx, fila in st.session_state.db.iterrows():
            total_puntos += calcular_puntos(fila["Goles_Real_1"], fila["Goles_Real_2"], fila[f"{nom}_G1"], fila[f"{nom}_G2"])
        puntajes[nom] = total_puntos
        
    df_posiciones = pd.DataFrame(list(puntajes.items()), columns=["Apostador", "Puntos Totales"])
    df_posiciones = df_posiciones.sort_values(by="Puntos Totales", ascending=False)
    st.dataframe(df_posiciones, hide_index=True, use_container_width=True)

elif pestana == "🏆 Evolución y Premiación":
    st.subheader("Asignación de Puestos para Premios")
    puntajes = {}
    for nom in NOMBRES_APOSTADORES:
        total_puntos = 0
        for idx, fila in st.session_state.db.iterrows():
            total_puntos += calcular_puntos(fila["Goles_Real_1"], fila["Goles_Real_2"], fila[f"{nom}_G1"], fila[f"{nom}_G2"])
        puntajes[nom] = total_puntos
    df_premios = pd.DataFrame(list(puntajes.items()), columns=["Apostador", "Puntos"])
    df_premios["Puesto"] = df_premios["Puntos"].rank(method="dense", ascending=False).astype(int)
    df_premios = df_premios.sort_values(by="Puesto")
    
    def asignar_medalla(puesto):
        if puesto == 1: return "🥇 1º Puesto"
        if puesto == 2: return "🥈 2º Puesto"
        if puesto == 3: return "🥉 3º Puesto"
        return f"{puesto}º Lugar"
    df_premios["Puesto"] = df_premios["Puesto"].apply(asignar_medalla)
    st.table(df_premios)
