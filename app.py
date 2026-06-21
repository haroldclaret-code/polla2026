import streamlit as st
import pandas as pd
import numpy as np
import os

# Configuración inicial de la aplicación
st.set_page_config(page_title="Polla Mundialista 2026", layout="wide", page_icon="⚽")

st.title("⚽ Polla Mundialista 2026 - Sistema Oficial")

# 📝 LISTA OFICIAL DE TU GRUPO DE APOSTADORES
NOMBRES_APOSTADORES = [
    "Lizeth", "Kevin", "Yudi", "Diana", "Yaritza", 
    "Álvaro", "Francisco", "Harold", "Alejandra", "Karina", "Milena"
]

ARCHIVO_DATOS = "datos_polla_2026.csv"

# 🛠️ CONSTRUCCIÓN COMPLETA DE TODOS LOS VERSUS REALES EXTRAÍDOS DE TUS IMÁGENES
def generar_fixture_oficial_total():
    partidos = []
    
    # Lista fiel a tus 12 imágenes organizada por las fechas exactas que allí aparecen
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

        # --- FECHA 2 ---
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

        # --- FECHA 3 ---
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
        {"Detalle": "26/06/2026", "Partido": "Cabo Verde vs Arabia Saudita"},
        {"Detalle": "26/06/2026", "Partido": "Noruega vs Francia"},
        {"Detalle": "26/06/2026", "Partido": "Senegal vs Irak"},
        
        {"Detalle": "27/06/2026", "Partido": "Jordania vs Argentina"},
        {"Detalle": "27/06/2026", "Partido": "Argelia vs Austria"},
        {"Detalle": "27/06/2026", "Partido": "Colombia vs Portugal"},
        {"Detalle": "27/06/2026", "Partido": "Rep. Democ. del Congo vs Uzbekistán"},
        {"Detalle": "27/06/2026", "Partido": "Panamá vs Inglaterra"},
        {"Detalle": "27/06/2026", "Partido": "Croacia vs Ghana"}
    ]
    
    contador = 1
    for p_info in partidos_grupos_origen:
        partidos.append({
            "ID": f"G_{contador}", "Fase": "Fase de Grupos", 
            "Detalle": p_info["Detalle"], "Partido": p_info["Partido"],
            "Goles_Real_1": "", "Goles_Real_2": ""
        })
        contador += 1
        
    # Añadimos los partidos vacíos correspondientes a los 2 grupos faltantes para completar el fixture general si lo requieres
    while contador <= 72:
        partidos.append({
            "ID": f"G_{contador}", "Fase": "Fase de Grupos", 
            "Detalle": "Fecha por Definir", "Partido": "Equipo Versus por Definir",
            "Goles_Real_1": "", "Goles_Real_2": ""
        })
        contador += 1

    # Fases Eliminatorias Siguientes
    for i in range(1, 17):
        partidos.append({"ID": f"16F_{i}", "Fase": "Dieciseisavos de Final", "Detalle": f"Llave {i}", "Partido": "Por Definir vs Por Definir", "Goles_Real_1": "", "Goles_Real_2": ""})
    for i in range(1, 9):
        partidos.append({"ID": f"8F_{i}", "Fase": "Octavos de Final", "Detalle": f"Llave {i}", "Partido": "Por Definir vs Por Definir", "Goles_Real_1": "", "Goles_Real_2": ""})
    for i in range(1, 5):
        partidos.append({"ID": f"4F_{i}", "Fase": "Cuartos de Final", "Detalle": f"Llave {i}", "Partido": "Por Definir vs Por Definir", "Goles_Real_1": "", "Goles_Real_2": ""})
    for i in range(1, 3):
        partidos.append({"ID": f"SF_{i}", "Fase": "Semifinal", "Detalle": f"Semifinal {i}", "Partido": "Por Definir vs Por Definir", "Goles_Real_1": "", "Goles_Real_2": ""})
        
    partidos.append({"ID": "F_3ER", "Fase": "Tercer Puesto", "Detalle": "Final de Consolación", "Partido": "Perdedor SF1 vs Perdedor SF2", "Goles_Real_1": "", "Goles_Real_2": ""})
    partidos.append({"ID": "F_GRAN", "Fase": "Gran Final", "Detalle": "Definición del Título", "Partido": "Ganador SF1 vs Ganador SF2", "Goles_Real_1": "", "Goles_Real_2": ""})

    for fila in partidos:
        for nom in NOMBRES_APOSTADORES:
            fila[f"{nom}_G1"] = ""
            fila[f"{nom}_G2"] = ""
            
    return pd.DataFrame(partidos)

# 🔄 SISTEMA DE MEMORIA PERSISTENTE (ANTI-RESET)
if "db" not in st.session_state:
    if os.path.exists(ARCHIVO_DATOS):
        try:
            df_file = pd.read_csv(ARCHIVO_DATOS).fillna("")
            if len(df_file) >= 104:
                for col in df_file.columns:
                    df_file[col] = df_file[col].astype(str).replace(r'^\s*$', '', regex=True)
                st.session_state.db = df_file
            else:
                raise ValueError()
        except:
            df_nuevo = generar_fixture_oficial_total()
            df_nuevo.to_csv(ARCHIVO_DATOS, index=False)
            st.session_state.db = df_nuevo
    else:
        df_nuevo = generar_fixture_oficial_total()
        df_nuevo.to_csv(ARCHIVO_DATOS, index=False)
        st.session_state.db = df_nuevo

# ⚙️ BARRA LATERAL ADMINISTRATIVA
st.sidebar.header("⚙️ Configuración")
password = st.sidebar.text_input("Contraseña de Administrador", type="password")

# 📥 BOTÓN DE COPIA DE SEGURIDAD ABSOLUTA
st.sidebar.subheader("📥 Respaldo General")
csv_bytes = st.session_state.db.to_csv(index=False).encode('utf-8')
st.sidebar.download_button(
    label="Descargar Toda la Polla (CSV)",
    data=csv_bytes,
    file_name="RESPALDO_POLLA_MUNDIAL_2026.csv",
    mime="text/csv",
    help="Descarga un respaldo absoluto con todos tus partidos y apuestas."
)

# 🧮 CÁLCULO ESTÁNDAR DE REGLAS DE PUNTOS
def calcular_puntos(r1, r2, p1, p2):
    if r1 == "" or r2 == "" or p1 == "" or p2 == "" or pd.isna(r1) or pd.isna(r2) or pd.isna(p1) or pd.isna(p2):
        return 0
    try:
        r1, r2, p1, p2 = int(float(r1)), int(float(r2)), int(float(p1)), int(float(p2))
    except:
        return 0
    if r1 == p1 and r2 == p2:
        return 10
    gr = 1 if r1 > r2 else (-1 if r1 < r2 else 0)
    gp = 1 if p1 > p2 else (-1 if p1 < p2 else 0)
    if gr == gp:
        return 5
    if (r1 - r2) == (p1 - p2):
        return 2
    return 0

# PESTAÑAS DE VISTA DE LA APLICACIÓN
pestana = st.radio("Secciones de la Polla:", ["📋 Gestión de Marcadores y Pronósticos", "📊 Tabla General de Posiciones", "🏆 Cuadro de Honor"], horizontal=True)

if pestana == "📋 Gestión de Marcadores y Pronósticos":
    st.subheader("Control del Calendario Oficial")
    fases = ["Fase de Grupos", "Dieciseisavos de Final", "Octavos de Final", "Cuartos de Final", "Semifinal", "Tercer Puesto", "Gran Final"]
    fase_sel = st.selectbox("Seleccionar Instancia Actual:", fases)
    
    df_filtrado = st.session_state.db[st.session_state.db["Fase"] == fase_sel]
    
    # Filtro cronológico interno exclusivo para la Fase de Grupos
    if fase_sel == "Fase de Grupos":
        fechas_internas = sorted(df_filtrado["Detalle"].unique())
        fecha_sel = st.selectbox("Filtrar por Día/Jornada:", fechas_internas)
        df_mostrar = df_filtrado[df_filtrado["Detalle"] == fecha_sel]
    else:
        df_mostrar = df_filtrado

    altura_dinamica = int((len(df_mostrar) + 1) * 35) + 45

    if password == "mundial2026":
        st.success("🔓 Administrador Activo: Puedes rellenar Versus, Fechas, Resultados Reales y Predicciones.")
        df_editado = st.data_editor(df_mostrar, hide_index=True, use_container_width=True, height=altura_dinamica)
        if st.button("💾 Guardar y Sincronizar Cambios"):
            st.session_state.db.update(df_editado)
            st.session_state.db.to_csv(ARCHIVO_DATOS, index=False)
            st.success("🔒 ¡Datos guardados permanentemente en el disco base!")
            st.rerun()
    else:
        st.info("🔒 Modo Lectura. Introduce la contraseña para registrar o modificar datos.")
        st.dataframe(df_mostrar, hide_index=True, use_container_width=True, height=altura_dinamica)

elif pestana == "📊 Tabla General de Posiciones":
    st.subheader("Clasificación de Miembros del Grupo")
    puntajes = {}
    for nom in NOMBRES_APOSTADORES:
        total = 0
        for idx, fila in st.session_state.db.iterrows():
            total += calcular_puntos(fila["Goles_Real_1"], fila["Goles_Real_2"], fila[f"{nom}_G1"], fila[f"{nom}_G2"])
        puntajes[nom] = total
        
    df_pos = pd.DataFrame(list(puntajes.items()), columns=["Apostador", "Puntos Totales"]).sort_values(by="Puntos Totales", ascending=False)
    st.dataframe(df_pos, hide_index=True, use_container_width=True)

elif pestana == "🏆 Cuadro de Honor":
    st.subheader("Asignación de Premios")
    puntajes = {}
    for nom in NOMBRES_APOSTADORES:
        total = 0
        for idx, fila in st.session_state.db.iterrows():
            total += calcular_puntos(fila["Goles_Real_1"], fila["Goles_Real_2"], fila[f"{nom}_G1"], fila[f"{nom}_G2"])
        puntajes[nom] = total
    df_premios = pd.DataFrame(list(puntajes.items()), columns=["Apostador", "Puntos"]).sort_values(by="Puntos", ascending=False)
    
    def medalla(p):
        if p == 1: return "🥇 Primer Puesto"
        if p == 2: return "🥈 Segundo Puesto"
        if p == 3: return "🥉 Tercer Puesto"
        return f"{p}º Lugar"
    df_premios["Puesto"] = [medalla(i+1) for i in range(len(df_premios))]
    st.table(df_premios[["Puesto", "Apostador", "Puntos"]])
