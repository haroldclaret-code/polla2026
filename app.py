import streamlit as st
import pandas as pd
import io

# Configuración inicial de la aplicación
st.set_page_config(page_title="Polla Mundialista UNAD Chipaque", layout="wide", page_icon="⚽")
st.title("⚽ Polla Mundialista 2026 - UNAD Chipaque")

# Lista oficial de apostadores
NOMBRES_APOSTADORES = ["Lizeth", "Kevin", "Yudi", "Diana", "Yaritza", "Álvaro", "Francisco", "Harold", "Alejandra", "Karina", "Milena"]

# Control de persistencia en memoria interna de la sesión
if "db" not in st.session_state:
    st.session_state.db = None

# ⚙️ BARRA LATERAL ADMINISTRATIVA
st.sidebar.header("⚙️ Configuración")
password = st.sidebar.text_input("Contraseña de Administrador", type="password")

# Función auxiliar para limpiar y forzar enteros en visualización
def limpiar_enteros(val):
    if val == "" or pd.isna(val):
        return ""
    try:
        # Convierte a flotante primero por si viene como '1.0' y luego a entero string limpio
        return str(int(float(val)))
    except:
        return str(val)

# Botón para descargar el respaldo actual en CSV
if st.session_state.db is not None:
    # Formateamos una copia limpia para la descarga
    df_descarga = st.session_state.db.copy()
    for col in df_descarga.columns:
        df_descarga[col] = df_descarga[col].apply(limpiar_enteros)
        
    csv_bytes = df_descarga.to_csv(index=False).encode('utf-8')
    st.sidebar.download_button(
        label="⬇️ Descargar Copia (.CSV)",
        data=csv_bytes,
        file_name="RESPALDO_POLLA_MUNDIAL_2026.csv",
        mime="text/csv"
    )

# 🚨 SISTEMA DE RESTAURACIÓN (Doble opción: Archivo o Texto Copiado/Pegado)
with st.sidebar.expander("🚨 Cargar / Restaurar Datos", expanded=(st.session_state.db is None)):
    st.write("Usa cualquiera de las dos opciones para activar la Polla:")
    
    # Opción A: Subir Archivo
    archivo_cargado = st.file_uploader("Opción A: Subir archivo .csv o .txt", type=["csv", "txt"])
    
    # Opción B: Copiar y pegar texto limpio
    texto_pegado = st.text_area("Opción B: Pegar contenido del archivo de texto aquí:")
    
    raw_data = None
    if archivo_cargado is not None:
        raw_data = archivo_cargado
    elif texto_pegado.strip() != "":
        raw_data = io.StringIO(texto_pegado)
        
    if raw_data is not None:
        try:
            df_restaurado = pd.read_csv(raw_data).fillna("")
            # Asegurar que todo se trate como texto sin decimales ocultos .0
            for col in df_restaurado.columns:
                df_restaurado[col] = df_restaurado[col].astype(str).replace(r'^\s*$', '', regex=True)
                df_restaurado[col] = df_restaurado[col].apply(limpiar_enteros)
            st.session_state.db = df_restaurado
            st.success("¡Base de datos cargada correctamente!")
        except Exception as e:
            st.error(f"Error al procesar los datos: {e}")

# Reglas de cálculo de puntos (Forzando números enteros)
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

# Despliegue de la aplicación principal si los datos existen
if st.session_state.db is not None:
    pestana = st.radio("Secciones de la Polla:", ["📋 Gestión de Marcadores y Pronósticos", "📊 Tabla General de Posiciones", "🏆 Cuadro de Honor"], horizontal=True)

    if pestana == "📋 Gestión de Marcadores y Pronósticos":
        st.subheader("Control del Calendario Oficial")
        fases = sorted(st.session_state.db["Fase"].unique())
        fase_sel = st.selectbox("Seleccionar Instancia Actual:", fases)
        df_filtrado = st.session_state.db[st.session_state.db["Fase"] == fase_sel]
        
        if "Detalle" in df_filtrado.columns and fase_sel == "Fase de Grupos":
            fechas_internas = sorted(df_filtrado["Detalle"].unique())
            fecha_sel = st.selectbox("Filtrar por Día/Jornada:", fechas_internas)
            df_jornada = df_filtrado[df_filtrado["Detalle"] == fecha_sel]
        else:
            df_jornada = df_filtrado

        # --- RESULTADOS REALES (Formateados a entero string para evitar .0) ---
        st.markdown("### 🏆 Resultados Reales del Mundial")
        cols_reales = ["ID", "Detalle", "Partido", "Goles_Real_1", "Goles_Real_2"]
        df_reales_mostrar = df_jornada[cols_reales].copy()
        for c in ["Goles_Real_1", "Goles_Real_2"]:
            df_reales_mostrar[c] = df_reales_mostrar[c].apply(limpiar_enteros)
        
        if password == "mundial2026":
            st.caption("✏️ Edita los marcadores oficiales abajo y presiona guardar.")
            df_reales_editado = st.data_editor(df_reales_mostrar, hide_index=True, use_container_width=True, key="editor_reales")
        else:
            st.dataframe(df_reales_mostrar, hide_index=True, use_container_width=True)

        # --- PRONÓSTICOS DE APOSTADORES ---
        st.markdown("---")
        st.markdown("### 👤 Pronósticos de los Apostadores")
        apostador_sel = st.selectbox("Selecciona un Participante:", NOMBRES_APOSTADORES)
        col_g1, col_g2 = f"{apostador_sel}_G1", f"{apostador_sel}_G2"
        
        df_ap_mostrar = df_jornada[["ID", "Detalle", "Partido"]].copy()
        df_ap_mostrar["Goles Local"] = df_jornada[col_g1].apply(limpiar_enteros)
        df_ap_mostrar["Goles Visitante"] = df_jornada[col_g2].apply(limpiar_enteros)
        
        if password == "mundial2026":
            df_ap_editado = st.data_editor(df_ap_mostrar, hide_index=True, use_container_width=True, key=f"editor_{apostador_sel}")
            
            if st.button("💾 Sincronizar y Guardar Cambios"):
                for _, fila in df_reales_editado.iterrows():
                    idx = st.session_state.db[st.session_state.db["ID"] == fila["ID"]].index[0]
                    st.session_state.db.at[idx, "Goles_Real_1"] = limpiar_enteros(fila["Goles_Real_1"])
                    st.session_state.db.at[idx, "Goles_Real_2"] = limpiar_enteros(fila["Goles_Real_2"])
                for _, fila in df_ap_editado.iterrows():
                    idx = st.session_state.db[st.session_state.db["ID"] == fila["ID"]].index[0]
                    st.session_state.db.at[idx, col_g1] = limpiar_enteros(fila["Goles Local"])
                    st.session_state.db.at[idx, col_g2] = limpiar_enteros(fila["Goles Visitante"])
                st.success("¡Datos sincronizados como enteros! Descarga tu nuevo CSV en la barra lateral para guardar tus cambios permanentes.")
                st.rerun()
        else:
            st.dataframe(df_ap_mostrar, hide_index=True, use_container_width=True)

    elif pestana == "📊 Tabla General de Posiciones":
        st.subheader("Clasificación de Miembros del Grupo")
        puntajes = {nom: sum(calcular_puntos(f["Goles_Real_1"], f["Goles_Real_2"], f[f"{nom}_G1"], f[f"{nom}_G2"]) for _, f in st.session_state.db.iterrows()) for nom in NOMBRES_APOSTADORES}
        df_pos = pd.DataFrame(list(puntajes.items()), columns=["Apostador", "Puntos Totales"]).sort_values(by="Puntos Totales", ascending=False)
        st.dataframe(df_pos, hide_index=True, use_container_width=True)

    elif pestana == "🏆 Cuadro de Honor":
        st.subheader("Asignación de Premios")
        puntajes = {nom: sum(calcular_puntos(f["Goles_Real_1"], f["Goles_Real_2"], f[f"{nom}_G1"], f[f"{nom}_G2"]) for _, f in st.session_state.db.iterrows()) for nom in NOMBRES_APOSTADORES}
        df_premios = pd.DataFrame(list(puntajes.items()), columns=["Apostador", "Puntos"]).sort_values(by="Puntos", ascending=False)
        df_premios["Puesto"] = [f"🥇 1º Puesto" if i==0 else f"🥈 2º Puesto" if i==1 else f"🥉 3º Puesto" if i==2 else f"{i+1}º Lugar" for i in range(len(df_premios))]
        st.table(df_premios[["Puesto", "Apostador", "Puntos"]])
else:
    st.warning("⚠️ La aplicación está lista. Por favor, ve al menú izquierdo '🚨 Cargar / Restaurar Datos' y sube tu archivo (.csv/.txt) o pega el texto para iniciar.")
