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

# 1. CARGA DIRECTA DE LA BASE DE DATOS FIJA DESDE GITHUB
if "db" not in st.session_state:
    if os.path.exists(ARCHIVO_DATOS):
        st.session_state.db = pd.read_csv(ARCHIVO_DATOS).fillna("")
    else:
        st.error(f"⚠️ No se encontró el archivo '{ARCHIVO_DATOS}' en GitHub. Por favor súbelo.")
        st.stop()

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
    
    # Altura adaptable para evitar recortes visuales
    altura_dinamica = int((len(df_filtrado) + 1) * 35) + 45

    if password == "mundial2026":
        st.success("🔓 Modo Administrador Activado.")
        df_editado = st.data_editor(df_filtrado, hide_index=True, use_container_width=True, height=altura_dinamica)
        if st.button("💾 Guardar y Actualizar Polla Permanentemente"):
            st.session_state.db.update(df_editado)
            st.session_state.db.to_csv(ARCHIVO_DATOS, index=False)
            st.success("¡Datos guardados temporalmente en el servidor!")
            st.info("💡 Consejo: Si agregas datos clave y quieres congelarlos para siempre, descarga el CSV desde el editor y súbelo a GitHub.")
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
    st.table(df_premios)st.table(df_premios)
