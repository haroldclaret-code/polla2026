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

# 1. FUNCIÓN PARA CREAR O CARGAR LA BASE DE DATOS REAL
def cargar_o_inicializar_datos():
    # Si el archivo ya existe en la nube, lo lee para no perder datos
    if os.path.exists(ARCHIVO_DATOS):
        return pd.read_csv(ARCHIVO_DATOS)
    
    # Si no existe (es la primera vez), genera la estructura de los 104 partidos automáticamente
    partidos = []
    for i in range(1, 73):
        partidos.append({"ID": f"P{i}", "Fase": "Fase de Grupos", "Partido": f"Partido de Grupo {i}", "Goles_Real_1": "", "Goles_Real_2": ""})
    for i in range(73, 89):
        partidos.append({"ID": f"P{i}", "Fase": "Dieciseisavos", "Partido": f"Llave Eliminatoria {i-72}", "Goles_Real_1": "", "Goles_Real_2": ""})
    for i in range(89, 97):
        partidos.append({"ID": f"P{i}", "Fase": "Octavos de Final", "Partido": f"Octavos {i-88}", "Goles_Real_1": "", "Goles_Real_2": ""})
    for i in range(97, 101):
        partidos.append({"ID": f"P{i}", "Fase": "Cuartos de Final", "Partido": f"Cuartos {i-96}", "Goles_Real_1": "", "Goles_Real_2": ""})
    partidos.append({"ID": "P101", "Fase": "Semifinal", "Partido": "Semifinal 1", "Goles_Real_1": "", "Goles_Real_2": ""})
    partidos.append({"ID": "P102", "Fase": "Semifinal", "Partido": "Semifinal 2", "Goles_Real_1": "", "Goles_Real_2": ""})
    partidos.append({"ID": "P103", "Fase": "Tercer Puesto", "Partido": "Definición Bronce", "Goles_Real_1": "", "Goles_Real_2": ""})
    partidos.append({"ID": "P104", "Fase": "Gran Final", "Partido": "Partido por la Copa", "Goles_Real_1": "", "Goles_Real_2": ""})
    
    df_partidos = pd.DataFrame(partidos)
    
    # Crea las columnas en blanco para los 11 apostadores
    for i in range(1, 12):
        df_partidos[f"Ap{i}_G1"] = ""
        df_partidos[f"Ap{i}_G2"] = ""
        
    df_partidos.to_csv(ARCHIVO_DATOS, index=False)
    return df_partidos

# Cargar la base de datos actual
if "db" not in st.session_state:
    st.session_state.db = cargar_o_inicializar_datos()

# 2. SISTEMA MATEMÁTICO DE REGLAS (Tus reglas oficiales)
def calcular_puntos(r1, r2, p1, p2):
    # Si falta el resultado real o el pronóstico, da 0 puntos
    if r1 == "" or r2 == "" or p1 == "" or p2 == "" or pd.isna(r1) or pd.isna(r2) or pd.isna(p1) or pd.isna(p2):
        return 0
    try:
        r1, r2, p1, p2 = int(r1), int(r2), int(p1), int(p2)
    except:
        return 0
        
    # Categoría 1: Marcador Exacto (10 puntos)
    if r1 == p1 and r2 == p2:
        return 10
        
    # Categoría 2: Acertar Ganador o Empate (5 puntos)
    ganador_real = 1 if r1 > r2 else (-1 if r1 < r2 else 0)
    ganador_pago = 1 if p1 > p2 else (-1 if p1 < p2 else 0)
    if ganador_real == ganador_pago:
        return 5
        
    # Categoría 3: Únicamente Diferencia de Goles (2 puntos)
    if (r1 - r2) == (p1 - p2):
        return 2
        
    return 0

# Pestañas de la interfaz de usuario
pestana = st.radio("Selecciona la Vista:", ["📋 Control de Partidos", "📊 Tabla de Posiciones Global", "🏆 Evolución y Premiación"], horizontal=True)

# --- HOJA 1: CONTROL DE PARTIDOS ---
if pestana == "📋 Control de Partidos":
    st.subheader("Registro de Marcadores Reales y Pronósticos")
    
    fase_sel = st.selectbox("Filtrar por Fase del Torneo", st.session_state.db["Fase"].unique())
    df_filtrado = st.session_state.db[st.session_state.db["Fase"] == fase_sel]
    
    # Control de seguridad por contraseña
    if password == "mundial2026": # CAMBIA ESTA CONTRASEÑA POR LA QUE TÚ QUIERAS
        st.success("🔓 Modo Administrador Activado. Tienes permiso de edición.")
        df_editado = st.data_editor(df_filtrado, hide_index=True)
        
        if st.button("💾 Guardar y Actualizar Polla Permanentemente"):
            st.session_state.db.update(df_editado)
            # Guarda los cambios físicamente en el archivo de la nube
            st.session_state.db.to_csv(ARCHIVO_DATOS, index=False)
            st.success("¡Datos guardados con éxito! Todos tus compañeros verán los cambios al actualizar.")
            st.rerun()
    else:
        st.info("🔒 Vista de Solo Lectura para Apostadores. Ingresa la contraseña en el panel izquierdo para editar.")
        st.dataframe(df_filtrado, hide_index=True)

# --- HOJA 2: TABLA DE POSICIONES GLOBAL ---
elif pestana == "📊 Tabla de Posiciones Global":
    st.subheader("Puntajes Acumulados")
    
    puntajes = {}
    for i in range(1, 12):
        total_puntos = 0
        for idx, fila in st.session_state.db.iterrows():
            total_puntos += calcular_puntos(fila["Goles_Real_1"], fila["Goles_Real_2"], fila[f"Ap{i}_G1"], fila[f"Ap{i}_G2"])
        puntajes[f"Apostador {i}"] = total_puntos
        
    df_posiciones = pd.DataFrame(list(puntajes.items()), columns=["Apostador", "Puntos Totales"])
    df_posiciones = df_posiciones.sort_values(by="Puntos Totales", ascending=False)
    
    st.dataframe(df_posiciones, hide_index=True, use_container_width=True)

# --- HOJA 3: EVOLUCIÓN Y PREMIACIÓN (RANKING DENSO) ---
elif pestana == "🏆 Evolución y Premiación":
    st.subheader("Asignación de Puestos para Premios (Primer, Segundo y Tercer lugar)")
    
    puntajes = {}
    for i in range(1, 12):
        total_puntos = 0
        for idx, fila in st.session_state.db.iterrows():
            total_puntos += calcular_puntos(fila["Goles_Real_1"], fila["Goles_Real_2"], fila[f"Ap{i}_G1"], fila[f"Ap{i}_G2"])
        puntajes[f"Apostador {i}"] = total_puntos
    
    df_premios = pd.DataFrame(list(puntajes.items()), columns=["Apostador", "Puntos"])
    
    # Implementación matemática del Ranking Denso para empates consecutivos
    df_premios["Puesto"] = df_premios["Puntos"].rank(method="dense", ascending=False).astype(int)
    df_premios = df_premios.sort_values(by="Puesto")
    
    def asignar_medalla(puesto):
        if puesto == 1: return "🥇 1º Puesto"
        if puesto == 2: return "🥈 2º Puesto"
        if puesto == 3: return "🥉 3º Puesto"
        return f"{puesto}º Lugar"
        
    df_premios["Puesto"] = df_premios["Puesto"].apply(asignar_medalla)
    st.table(df_premios)