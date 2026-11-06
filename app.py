import streamlit as st
import numpy as np
import time
from game_logic import actualizar_grid, crear_grid_aleatorio, crear_grid_vacio

st.set_page_config(page_title="El Juego de la Vida", layout="centered")

st.title("El Juego de la Vida de Conway")
st.write("Proyecto colaborativo desarrollado por Aimeé y Lizbeth para la materia de programación.")

# Sidebar para controles
st.sidebar.header("Configuracion del Juego")

# Tamaño de la cuadrícula
filas = st.sidebar.slider("Numero de filas", min_value=10, max_value=50, value=20, step=1)
columnas = st.sidebar.slider("Numero de columnas", min_value=10, max_value=50, value=20, step=1)
velocidad = st.sidebar.slider("Velocidad de animacion (segundos)", min_value=0.05, max_value=1.0, value=0.2, step=0.05)

# Control de estado en Streamlit session_state
if 'grid' not in st.session_state:
    st.session_state.grid = crear_grid_aleatorio(filas, columnas)

if 'corriendo' not in st.session_state:
    st.session_state.corriendo = False

# Botones de control
col1, col2, col3 = st.sidebar.columns(3)
start_btn = col1.button("Iniciar")
stop_btn = col2.button("Pausar")
reset_btn = col3.button("Reiniciar")

if start_btn:
    st.session_state.corriendo = True
if stop_btn:
    st.session_state.corriendo = False
if reset_btn:
    st.session_state.corriendo = False
    st.session_state.grid = crear_grid_aleatorio(filas, columnas)

# Contenedor para mostrar la cuadrícula
container = st.empty()

# Bucle de ejecución si está activo
if st.session_state.corriendo:
    st.session_state.grid = actualizar_grid(st.session_state.grid)
    
    # Mostrar la matriz con texto limpio (O para vivo, . para muerto)
    representacion = "\n".join(["".join(["O " if celda == 1 else ". " for celda in fila]) for fila in st.session_state.grid])
    container.text(representacion)
    
    time.sleep(velocidad)
    st.rerun()
else:
    # Vista estática cuando está pausado
    representacion = "\n".join(["".join(["O " if celda == 1 else ". " for celda in fila]) for fila in st.session_state.grid])
    container.text(representacion)