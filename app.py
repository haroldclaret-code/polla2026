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

# 1. FUNCIÓN CON EL FIXTURE REAL COMPLETO Y CATEGORIZADO
def cargar_o_inicializar_datos():
    if os.path.exists(ARCHIVO_DATOS):
        return pd.read_csv(ARCHIVO_DATOS)
    
    partidos_reales = [
        # --- JORNADA 1 ---
        {"ID": "P1", "Fase": "Fase de Grupos", "Detalle": "Jornada 1", "Partido": "Méx vs A2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P2", "Fase": "Fase de Grupos", "Detalle": "Jornada 1", "Partido": "A3 vs A4", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P3", "Fase": "Fase de Grupos", "Detalle": "Jornada 1", "Partido": "Can vs B2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P4", "Fase": "Fase de Grupos", "Detalle": "Jornada 1", "Partido": "B3 vs B4", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P5", "Fase": "Fase de Grupos", "Detalle": "Jornada 1", "Partido": "USA vs D2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P6", "Fase": "Fase de Grupos", "Detalle": "Jornada 1", "Partido": "D3 vs D4", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P7", "Fase": "Fase de Grupos", "Detalle": "Jornada 1", "Partido": "C1 vs C2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P8", "Fase": "Fase de Grupos", "Detalle": "Jornada 1", "Partido": "C3 vs C4", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P9", "Fase": "Fase de Grupos", "Detalle": "Jornada 1", "Partido": "E1 vs E2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P10", "Fase": "Fase de Grupos", "Detalle": "Jornada 1", "Partido": "E3 vs E4", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P11", "Fase": "Fase de Grupos", "Detalle": "Jornada 1", "Partido": "F1 vs F2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P12", "Fase": "Fase de Grupos", "Detalle": "Jornada 1", "Partido": "F3 vs F4", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P13", "Fase": "Fase de Grupos", "Detalle": "Jornada 1", "Partido": "G1 vs G2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P14", "Fase": "Fase de Grupos", "Detalle": "Jornada 1", "Partido": "G3 vs G4", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P15", "Fase": "Fase de Grupos", "Detalle": "Jornada 1", "Partido": "H1 vs H2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P16", "Fase": "Fase de Grupos", "Detalle": "Jornada 1", "Partido": "H3 vs H4", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P17", "Fase": "Fase de Grupos", "Detalle": "Jornada 1", "Partido": "I1 vs I2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P18", "Fase": "Fase de Grupos", "Detalle": "Jornada 1", "Partido": "I3 vs I4", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P19", "Fase": "Fase de Grupos", "Detalle": "Jornada 1", "Partido": "J1 vs J2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P20", "Fase": "Fase de Grupos", "Detalle": "Jornada 1", "Partido": "J3 vs J4", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P21", "Fase": "Fase de Grupos", "Detalle": "Jornada 1", "Partido": "K1 vs K2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P22", "Fase": "Fase de Grupos", "Detalle": "Jornada 1", "Partido": "K3 vs K4", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P23", "Fase": "Fase de Grupos", "Detalle": "Jornada 1", "Partido": "L1 vs L2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P24", "Fase": "Fase de Grupos", "Detalle": "Jornada 1", "Partido": "L3 vs L4", "Goles_Real_1": "", "Goles_Real_2": ""},

        # --- JORNADA 2 ---
        {"ID": "P25", "Fase": "Fase de Grupos", "Detalle": "Jornada 2", "Partido": "Méx vs A3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P26", "Fase": "Fase de Grupos", "Detalle": "Jornada 2", "Partido": "A4 vs A2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P27", "Fase": "Fase de Grupos", "Detalle": "Jornada 2", "Partido": "B4 vs B2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P28", "Fase": "Fase de Grupos", "Detalle": "Jornada 2", "Partido": "Can vs B3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P29", "Fase": "Fase de Grupos", "Detalle": "Jornada 2", "Partido": "USA vs D3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P30", "Fase": "Fase de Grupos", "Detalle": "Jornada 2", "Partido": "D4 vs D2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P31", "Fase": "Fase de Grupos", "Detalle": "Jornada 2", "Partido": "C4 vs C2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P32", "Fase": "Fase de Grupos", "Detalle": "Jornada 2", "Partido": "C1 vs C3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P33", "Fase": "Fase de Grupos", "Detalle": "Jornada 2", "Partido": "E4 vs E2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P34", "Fase": "Fase de Grupos", "Detalle": "Jornada 2", "Partido": "E1 vs E3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P35", "Fase": "Fase de Grupos", "Detalle": "Jornada 2", "Partido": "F4 vs F2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P36", "Fase": "Fase de Grupos", "Detalle": "Jornada 2", "Partido": "F1 vs F3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P37", "Fase": "Fase de Grupos", "Detalle": "Jornada 2", "Partido": "G4 vs G2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P38", "Fase": "Fase de Grupos", "Detalle": "Jornada 2", "Partido": "G1 vs G3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P39", "Fase": "Fase de Grupos", "Detalle": "Jornada 2", "Partido": "H4 vs H2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P40", "Fase": "Fase de Grupos", "Detalle": "Jornada 2", "Partido": "H1 vs H3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P41", "Fase": "Fase de Grupos", "Detalle": "Jornada 2", "Partido": "I4 vs I2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P42", "Fase": "Fase de Grupos", "Detalle": "Jornada 2", "Partido": "I1 vs I3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P43", "Fase": "Fase de Grupos", "Detalle": "Jornada 2", "Partido": "J4 vs J2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P44", "Fase": "Fase de Grupos", "Detalle": "Jornada 2", "Partido": "J1 vs J3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P45", "Fase": "Fase de Grupos", "Detalle": "Jornada 2", "Partido": "K4 vs K2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P46", "Fase": "Fase de Grupos", "Detalle": "Jornada 2", "Partido": "K1 vs K3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P47", "Fase": "Fase de Grupos", "Detalle": "Jornada 2", "Partido": "L4 vs L2", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P48", "Fase": "Fase de Grupos", "Detalle": "Jornada 2", "Partido": "L1 vs L3", "Goles_Real_1": "", "Goles_Real_2": ""},

        # --- JORNADA 3 ---
        {"ID": "P49", "Fase": "Fase de Grupos", "Detalle": "Jornada 3", "Partido": "A2 vs A3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P50", "Fase": "Fase de Grupos", "Detalle": "Jornada 3", "Partido": "A4 vs Méx", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P51", "Fase": "Fase de Grupos", "Detalle": "Jornada 3", "Partido": "B2 vs B3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P52", "Fase": "Fase de Grupos", "Detalle": "Jornada 3", "Partido": "B4 vs Can", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P53", "Fase": "Fase de Grupos", "Detalle": "Jornada 3", "Partido": "C2 vs C3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P54", "Fase": "Fase de Grupos", "Detalle": "Jornada 3", "Partido": "C4 vs C1", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P55", "Fase": "Fase de Grupos", "Detalle": "Jornada 3", "Partido": "D2 vs D3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P56", "Fase": "Fase de Grupos", "Detalle": "Jornada 3", "Partido": "D4 vs USA", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P57", "Fase": "Fase de Grupos", "Detalle": "Jornada 3", "Partido": "E2 vs E3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P58", "Fase": "Fase de Grupos", "Detalle": "Jornada 3", "Partido": "E4 vs E1", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P59", "Fase": "Fase de Grupos", "Detalle": "Jornada 3", "Partido": "F2 vs F3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P60", "Fase": "Fase de Grupos", "Detalle": "Jornada 3", "Partido": "F4 vs F1", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P61", "Fase": "Fase de Grupos", "Detalle": "Jornada 3", "Partido": "G2 vs G3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P62", "Fase": "Fase de Grupos", "Detalle": "Jornada 3", "Partido": "G4 vs G1", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P63", "Fase": "Fase de Grupos", "Detalle": "Jornada 3", "Partido": "H2 vs H3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P64", "Fase": "Fase de Grupos", "Detalle": "Jornada 3", "Partido": "H4 vs H1", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P65", "Fase": "Fase de Grupos", "Detalle": "Jornada 3", "Partido": "I2 vs I3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P66", "Fase": "Fase de Grupos", "Detalle": "Jornada 3", "Partido": "I4 vs I1", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P67", "Fase": "Fase de Grupos", "Detalle": "Jornada 3", "Partido": "J2 vs J3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P68", "Fase": "Fase de Grupos", "Detalle": "Jornada 3", "Partido": "J4 vs J1", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P69", "Fase": "Fase de Grupos", "Detalle": "Jornada 3", "Partido": "K2 vs K3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P70", "Fase": "Fase de Grupos", "Detalle": "Jornada 3", "Partido": "K4 vs K1", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P71", "Fase": "Fase de Grupos", "Detalle": "Jornada 3", "Partido": "L2 vs L3", "Goles_Real_1": "", "Goles_Real_2": ""},
        {"ID": "P72", "Fase": "Fase de Grupos", "Detalle": "Jornada 3", "Partido": "L4 vs L1", "Goles_Real_1": "", "Goles_Real_2": ""},
    ]
    
    df_partidos = pd.DataFrame(partidos_reales)
    
    # --- LLAVES ELIMINATORIAS (CORREGIDAS VINCULANDO EL DETALLE) ---
    llaves = []
    for i in range(73, 89):
        llaves.append({"ID": f"P{i}", "Fase": "Eliminatorias Directas", "Detalle": "Dieciseisavos de Final", "Partido": f"Llave {i-72}", "Goles_Real_1": "", "Goles_Real_2": ""})
    for i in range(89, 97):
        llaves.append({"ID": f"P{i}", "Fase": "Eliminatorias Directas", "Detalle": "Octavos de Final", "Partido": f"Octavos {i-88}", "Goles_Real_1": "", "Goles_Real_2": ""})
    for i in range(97, 101):
        llaves.append({"ID": f"P{i}", "Fase": "Eliminatorias Directas", "Detalle": "Cuartos de Final", "Partido": f"Cuartos {i-96}", "Goles_Real_1": "", "Goles_Real_2": ""})
    llaves.append({"ID": "P101", "Fase": "Eliminatorias Directas", "Detalle": "Semifinal", "Partido": "Semifinal 1", "Goles_Real_1": "", "Goles_Real_2": ""})
    llaves.append({"ID": "P102", "Fase": "Eliminatorias Directas", "Detalle": "Semifinal", "Partido": "Semifinal 2", "Goles_Real_1": "", "Goles_Real_2": ""})
    llaves.append({"ID": "P103", "Fase": "Eliminatorias Directas", "Detalle": "Tercer Puesto", "Partido": "Partido 3º Puesto", "Goles_Real_1": "", "Goles_Real_2": ""})
    llaves.append({"ID": "P104", "Fase": "Eliminatorias Directas", "Detalle": "Gran Final", "Partido": "Gran Final 🏆", "Goles_Real_1": "", "Goles_Real_2": ""})
    
    df_llaves = pd.DataFrame(llaves)
    df_partidos = pd.concat([df_partidos, df_llaves], ignore_index=True)
    
    # Crear las columnas para tus 11 amigos
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

pestana = st.radio("Selecciona la Vista Real:", ["📋 Control de Partidos", "📊 Tabla de Posiciones Global", "🏆 Evolución y Premiación"], horizontal=True)

if pestana == "📋 Control de Partidos":
    st.subheader("Registro de Marcadores Reales y Pronósticos")
    
    col_f1, col_f2 = st.columns(2)
    with col_f1:
        fase_sel = st.selectbox("1. Filtrar Gran Etapa:", st.session_state.db["Fase"].unique())
    
    df_fase = st.session_state.db[st.session_state.db["Fase"] == fase_sel]
    
    with col_f2:
        detalle_sel = st.selectbox("2. Seleccionar Ronda / Fecha:", df_fase["Detalle"].unique())
        
    df_filtrado = df_fase[df_fase["Detalle"] == detalle_sel]
    
    # 📐 Altura adaptable para que se desplieguen completas sin recortes molesto
    altura_dinamica = int((len(df_filtrado) + 1) * 35) + 45

    if password == "mundial2026":
        st.success("🔓 Modo Administrador Activado.")
        df_editado = st.data_editor(df_filtrado, hide_index=True, use_container_width=True, height=altura_dinamica)
        if st.button("💾 Guardar y Actualizar Polla Permanentemente"):
            st.session_state.db.update(df_editado)
            st.session_state.db.to_csv(ARCHIVO_DATOS, index=False)
            st.success("¡Datos guardados con éxito!")
            st.rerun()
    else:
        st.info("🔒 Vista de Solo Lectura para Apostadores.")
        st.dataframe(df_filtrado, hide_index=True, use_container_width=True, height=altura_dinamica)

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
    df_premios = df_premios.sort_values(by="Puntos", ascending=False)
    
    def asignar_medalla(puesto):
        if puesto == 1: return "🥇 1º Puesto"
        if puesto == 2: return "🥈 2º Puesto"
        if puesto == 3: return "🥉 3º Puesto"
        return f"{puesto}º Lugar"
    df_premios["Puesto"] = [asignar_medalla(i+1) for i in range(len(df_premios))]
    st.table(df_premios)
