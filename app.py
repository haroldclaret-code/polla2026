import streamlit as st
import pandas as pd
import io

# Configuración inicial de la aplicación
st.set_page_config(page_title="Polla Mundialista UNAD Chipaque", layout="wide", page_icon="⚽")
st.title("⚽ Polla Mundialista 2026 - UNAD Chipaque")

# 📝 LISTA OFICIAL DE TU GRUPO DE APOSTADORES
NOMBRES_APOSTADORES = [
    "Lizeth", "Kevin", "Yudi", "Diana", "Yaritza", 
    "Álvaro", "Francisco", "Harold", "Alejandra", "Karina", "Milena"
]

# 🛠️ FUNCIÓN PARA GENERAR EL FIXTURE DESDE CERO
def generar_fixture_inicial():
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
        
    while contador <= 72:
        partidos.append({
            "ID": f"G_{contador}", "Fase": "Fase de Grupos", 
            "Detalle": "Fecha por Definir", "Partido": "Equipo Versus por Definir",
            "Goles_Real_1": "", "Goles_Real_2": ""
        })
        contador += 1

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

# 🔄 CONTROL DE PERSISTENCIA EN CACHÉ DE SESIÓN
if "db" not in st.session_state:
    st.session_state.db = generar_fixture_inicial()

# ⚙️ BARRA LATERAL ADMINISTRATIVA
st.sidebar.header("⚙️ Configuración")
password = st.sidebar.text_input("Contraseña de Administrador", type="password")

# Descargar Respaldo Directo
csv_bytes = st.session_state.db.to_csv(index=False).encode('utf-8')
st.sidebar.download_button(
    label="⬇️ Descargar Copia (.CSV)",
    data=csv_bytes,
    file_name="RESPALDO_POLLA_MUNDIAL_2026.csv",
    mime="text/csv"
)

# 🚨 SISTEMA DE SUBIDA DIRECTA DE ARCHIVO (Recovery mejorado)
if password == "mundial2026":
    with st.sidebar.expander("🚨 Cargar / Restaurar Archivo de Datos"):
        st.caption("Selecciona el archivo '.csv' guardado en tu PC para restaurar los marcadores:")
        archivo_cargado = st.file_uploader("Subir archivo de respaldo", type=["csv"])
        if archivo_cargado is not None:
            try:
                df_restaurado = pd.read_csv(archivo_cargado).fillna("")
                for col in df_restaurado.columns:
                    df_restaurado[col] = df_restaurado[col].astype(str).replace(r'^\s*$', '', regex=True)
                st.session_state.db = df_restaurado
                st.success("¡Base de datos restaurada con éxito desde el archivo!")
            except Exception as e:
                st.error(f"Error al leer el archivo: {e}")

# 🧮 REGLAS DE PUNTOS
def calcular_puntos(r1, r2, p1, p2):
    if r1 == "" or r2 == "" or p1 == "" or p2 == "" or pd.isna(r1) or pd.isna(r2) or pd.isna(p1) or pd.isna(p2):
        return 0
    try:
        r1, r2, p1, p2 = int(float(r
