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

# Función interna para construir el fixture oficial desde cero
def generar_base_datos_inicial():
    partidos_iniciales = []
    fechas_mundial = ["11/06/2026", "12/06/2026", "13/06/2026", "14/06/2026", "15/06/2026", "16/06/2026", "17/06/2026"]
    
    fixture_oficial = [
        {"Detalle": "11/06/2026", "Partido": "México vs Sudáfrica"},
        {"Detalle": "11/06/2026", "Partido": "Estados Unidos vs Asia/África Playoff"},
        {"Detalle": "11/06/2026", "Partido": "Guadalajara vs Partido 2"},
        {"Detalle": "11/06/2026", "Partido": "Corea vs Rep. Checa"},
        {"Detalle": "12/06/2026", "Partido": "Canadá vs Euro Playoff"},
        {"Detalle": "12/06/2026", "Partido": "Francia vs Jamaica"},
        {"Detalle": "12/06/2026", "Partido": "Argentina vs OFC Playoff"},
        {"Detalle": "12/06/2026", "Partido": "España vs Conmebol Playoff"},
        {"Detalle": "13/06/2026", "Partido": "Brasil vs OFC Playoff 2"},
        {"Detalle": "13/06/2026", "Partido": "Inglaterra vs Concacaf Playoff"},
        {"Detalle": "13/06/2026", "Partido": "Portugal vs Euro Playoff 2"},
        {"Detalle": "13/06/2026", "Partido": "Alemania vs CAF Playoff"},
    ]
    
    grupos = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L"]
    
    # Tus datos recuperados reales de los dos primeros partidos
    datos_p1 = {"Goles_Real_1": "2", "Goles_Real_2": "0", "Lizeth_G1": "2", "Lizeth_G2": "0", "Kevin_G1": "2", "Kevin_G2": "0", "Yudi_G1": "2", "Yudi_G2": "1", "Diana_G1": "2", "Diana_G2": "0", "Yaritza_G1": "1", "Yaritza_G2": "0", "Álvaro_G1": "2", "Álvaro_G2": "1", "Francisco_G1": "2", "Francisco_G2": "1", "Harold_G1": "2", "Harold_G2": "1", "Alejandra_G1": "2", "Alejandra_G2": "0", "Karina_G1": "2", "Karina_G2": "0", "Milena_G1": "3", "Milena_G2": "2"}
    datos_p2 = {"Goles_Real_1": "2", "Goles_Real_2": "1", "Lizeth_G1": "1", "Lizeth_G2": "0", "Kevin_G1": "1", "Kevin_G2": "0", "Yudi_G1": "1", "Yudi_G2": "0", "Diana_G1": "1", "Diana_G2": "1", "Yaritza_G1": "2", "Yaritza_G2": "1", "Álvaro_G1": "2", "Álvaro_G2": "0", "Francisco_G1": "2", "Francisco_G2": "0", "Harold_G1": "2", "Harold_G2": "0", "Alejandra_G1": "1", "Alejandra_G2": "1", "Karina_G1": "2", "Karina_G2": "1", "Milena_G1": "2", "Milena_G2": "2"}

    for i in range(72):
        num_p = i + 1
        f_act = fechas_mundial[i % len(fechas_mundial)]
        g_act = grupos[i % len(grupos)]
        
        if num_p == 1:
            fila = {"ID": "P1", "Fase": "Fase de Grupos", "Detalle": "11/06/2026", "Partido": "México vs Sudáfrica", **datos_p1}
        elif num_p == 2:
            fila = {"ID": "P2", "Fase": "Fase de Grupos", "Detalle": "11/06/2026", "Partido": "Corea vs Rep. Checa", **datos_p2}
        else:
            if i < len(fixture_oficial):
                partido_nombre = fixture_oficial[i]["Partido"]
                f_act = fixture_oficial[i]["Detalle"]
            else:
                partido_nombre = f"Rival 1 vs Rival 2 (Grupo {g_act})"
            
            fila = {
                "ID": f"P{num_p}", "Fase": "Fase de Grupos", "Detalle": f_act, "Partido": partido_nombre,
                "Goles_Real_1": "", "Goles_Real_2": ""
            }
            for nom in NOMBRES_APOSTADORES:
                fila[f"{nom}_G1"] = ""
                fila[f"{nom}_G2"] = ""
                
        partidos_iniciales.append(fila)
    return pd.DataFrame(partidos_iniciales)

# 1. CARGA DIRECTA Y SEGURA DE LA BASE DE DATOS
if "db" not in st.session_state:
    if os.path.exists(ARCHIVO_DATOS):
        try:
            df_cargado = pd.read_csv(ARCHIVO_DATOS).fillna("")
            if len(df_cargado) >= 72:
                for col in df_cargado.columns:
                    df_cargado[col] = df_cargado[col].astype(str).replace(r'^\s*$', '', regex=True)
                st.session_state.db = df_cargado
            else:
                raise ValueError("Incompleto")
        except:
            df_reconstruido = generar_base_datos_inicial()
            df_reconstruido.to_csv(ARCHIVO_DATOS, index=False)
            st.session_state.db = df_reconstruido
    else:
        df_reconstruido = generar_base_datos_inicial()
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
        # Forzar un ordenamiento cronológico para que salgan todas las fechas en la lista
        detalles_disponibles = sorted(df_fase["Detalle"].unique())
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
