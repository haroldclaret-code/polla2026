import streamlit as st
import pandas as pd
import numpy as np
import os

# Configuración inicial de la página web
st.set_page_config(page_title="Polla Mundialista 2026", layout="wide", page_icon="⚽")

st.title("⚽ Polla Mundialista 2026")
st.sidebar.header("⚙️ Panel de Administración (Solo Tú)")
password = st.sidebar.text_input("Contraseña de Administrador", type="password")

ARCHIVO_DATOS = "datos_polla_2026.csv"

# 📝 LISTA OFICIAL DE TU GRUPO
NOMBRES_APOSTADORES = [
    "Lizeth", "Kevin", "Yudi", "Diana", "Yaritza", 
    "Álvaro", "Francisco", "Harold", "Alejandra", "Karina", "Milena"
]

# 1. CARGA DIRECTA Y SEGURA DE LA BASE DE DATOS
if "db" not in st.session_state:
    if os.path.exists(ARCHIVO_DATOS):
        try:
            df_cargado = pd.read_csv(ARCHIVO_DATOS).fillna("")
            # Si por algún motivo el archivo está corrupto o vacío, forzamos error para reconstruir
            if len(df_cargado) < 5 or "Fase" not in df_cargado.columns:
                raise ValueError("Reconstruir")
            for col in df_cargado.columns:
                df_cargado[col] = df_cargado[col].astype(str).replace(r'^\s*$', '', regex=True)
            st.session_state.db = df_cargado
        except:
            # Reconstrucción del fixture completo con los 72 partidos de fase de grupos
            partidos_iniciales = []
            fechas_mundial = ["11/06/2026", "12/06/2026", "13/06/2026", "14/06/2026", "15/06/2026", "16/06/2026", "17/06/2026"]
            equipos_ejemplo = [
                ("México", "Sudáfrica"), ("Corea", "Rep. Checa"), ("Uruguay", "Francia"), ("Argentina", "Nigeria"),
                ("Inglaterra", "USA"), ("Alemania", "Australia"), ("Países Bajos", "Dinamarca"), ("Japón", "Camerún"),
                ("Italia", "Paraguay"), ("Brasil", "Corea del Norte"), ("Costa de Marfil", "Portugal"), ("España", "Suiza")
            ]
            contador = 1
            for i in range(72):
                fecha_act = fechas_mundial[i % len(fechas_mundial)]
                eq1, eq2 = equipos_ejemplo[i % len(equipos_ejemplo)]
                fila = {
                    "ID": f"P{contador}",
                    "Fase": "Fase de Grupos",
                    "Detalle": fecha_act,
                    "Partido": f"{eq1} vs {eq2}",
                    "Goles_Real_1": "",
                    "Goles_Real_2": ""
                }
                for nom in NOMBRES_APOSTADORES:
                    fila[f"{nom}_G1"] = ""
                    fila[f"{nom}_G2"] = ""
                partidos_iniciales.append(fila)
                contador += 1
            df_reconstruido = pd.DataFrame(partidos_iniciales)
            df_reconstruido.to_csv(ARCHIVO_DATOS, index=False)
            st.session_state.db = df_reconstruido
    else:
        # Si no existe el archivo csv, lo creamos desde cero
        partidos_iniciales = []
        fechas_mundial = ["11/06/2026", "12/06/2026", "13/06/2026", "14/06/2026", "15/06/2026", "16/06/2026", "17/06/2026"]
        equipos_ejemplo = [
            ("México", "Sudáfrica"), ("Corea", "Rep. Checa"), ("Uruguay", "Francia"), ("Argentina", "Nigeria"),
            ("Inglaterra", "USA"), ("Alemania", "Australia"), ("Países Bajos", "Dinamarca"), ("Japón", "Camerún"),
            ("Italia", "Paraguay"), ("Brasil", "Corea del Norte"), ("Costa de Marfil", "Portugal"), ("España", "Suiza")
        ]
        contador = 1
        for i in range(72):
            fecha_act = fechas_mundial[i % len(fechas_mundial)]
            eq1, eq2 = equipos_ejemplo[i % len(equipos_ejemplo)]
            fila = {
                "ID": f"P{contador}",
                "Fase": "Fase de Grupos",
                "Detalle": fecha_act,
                "Partido": f"{eq1} vs {eq2}",
                "Goles_Real_1": "",
                "Goles_Real_2": ""
            }
            for nom in NOMBRES_APOSTADORES:
                fila[f"{nom}_G1"] = ""
                fila[f"{nom}_G2"] = ""
            partidos_iniciales.append(fila)
            contador += 1
        df_reconstruido = pd.DataFrame(partidos_iniciales)
        df_reconstruido.to_csv(ARCHIVO_DATOS, index=False)
        st.session_state.db = df_reconstruido

# 2. SISTEMA MATEMÁTICO DE REGLAS
def calcular_puntos(r1, r2, p1, p2):
    if r1 == "" or r2 == "" or p1 == "" or p2 == "" or pd.isna(r1) or pd.isna(r2) or pd.isna(p1) or pd.isna(p2):
        return 0
    try:
        r1, r2, p1, p2 = int(float(r1)), int(float(r2)), int(float(p1)), int(float(p2))
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
        fases_disponibles = st.session_state.db["Fase"].unique()
        fase_sel = st.selectbox("1. Filtrar Gran Etapa:", fases_disponibles)
    
    df_fase = st.session_state.db[st.session_state.db["Fase"] == fase_sel]
    
    with col_f2:
        detalles_disponibles = df_fase["Detalle"].unique()
        detalle_sel = st.selectbox("2. Seleccionar Ronda / Fecha:", detalles_disponibles)
        
    df_filtrado = df_fase[df_fase["Detalle"] == detalle_sel]
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
        if f"{nom}_G1" in st.session_state.db.columns and f"{nom}_G2" in st.session_state.db.columns:
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
        if f"{nom}_G1" in st.session_state.db.columns and f"{nom}_G2" in st.session_state.db.columns:
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
