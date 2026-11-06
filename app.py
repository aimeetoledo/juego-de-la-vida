import streamlit as st
import numpy as np
import time
import matplotlib.pyplot as plt
from game_logic import actualizar_grid, crear_grid_aleatorio, crear_grid_vacio, crear_grid_glider

st.set_page_config(page_title="El Juego de la Vida", layout="centered")

st.title("El Juego de la Vida de Conway")
st.write("Proyecto colaborativo desarrollado por Aimeé y Lizbeth para la materia de programación.")

# Sidebar para controles
st.sidebar.header("Configuracion del Juego")

# Sliders de configuración
filas = st.sidebar.slider("Numero de filas", min_value=10, max_value=50, value=20, step=1)
columnas = st.sidebar.slider("Numero de columnas", min_value=10, max_value=50, value=20, step=1)
velocidad = st.sidebar.slider("Velocidad de animacion (segundos)", min_value=0.05, max_value=1.0, value=0.2, step=0.05)

# Selector de patrón inicial
patron = st.sidebar.selectbox("Selecciona un patrón inicial", ["Aleatorio", "Glider (Planeador)"])

# 1. Creamos los botones primero para que Python ya los conozca
col1, col2, col3 = st.sidebar.columns(3)
start_btn = col1.button("Iniciar")
stop_btn = col2.button("Pausar")
reset_btn = col3.button("Reiniciar")

# 2. Control de estado (aquí ya podemos usar reset_btn sin problema)
if 'grid' not in st.session_state or reset_btn:
    if patron == "Glider (Planeador)":
        st.session_state.grid = crear_grid_glider(filas, columnas)
    else:
        st.session_state.grid = crear_grid_aleatorio(filas, columnas)

if 'corriendo' not in st.session_state:
    st.session_state.corriendo = False


# Botones de control
col1, col2, col3 = st.sidebar.columns(3)
start_btn = col1.button("Iniciar", key="btn_iniciar")
stop_btn = col2.button("Pausar", key="btn_pausar")
reset_btn = col3.button("Reiniciar", key="btn_reiniciar")

if start_btn:
    st.session_state.corriendo = True
if stop_btn:
    st.session_state.corriendo = False
if reset_btn:
    st.session_state.corriendo = False
    st.session_state.grid = crear_grid_aleatorio(filas, columnas)

# Contenedor para mostrar la cuadrícula
container = st.empty()

# Crear la figura de Matplotlib para los bloques gráficos
fig, ax = plt.subplots(figsize=(6, 6))
ax.imshow(st.session_state.grid, cmap="binary")  # "binary" pinta las celdas en blanco y negro
ax.set_xticks([])
ax.set_yticks([])

# Mostrar la gráfica en Streamlit dentro del contenedor
container.pyplot(fig)
plt.close(fig)  # Libera memoria de la figura en cada paso

if st.session_state.corriendo:
    st.session_state.grid = actualizar_grid(st.session_state.grid)
    time.sleep(velocidad)
    st.rerun()
