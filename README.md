# 🦠 El Juego de la Vida (Conway's Game of Life)

Proyecto parcial desarrollado en Python utilizando Streamlit para la visualización de autómatas celulares.

## 👥 Autoras
* **Aimeé Toledo**
* **Lizbeth Graciela Cervera Romero**

## Resumen
EL presente proyecto consiste en el desarrollo de una aplicacion interactiva basada en el Juego de la Vida de Conway.
El sistema simula el comportamiento de una problación celular dentro de una cuadrícula bidimensional, donde cada célula puede encontrarse en dos estados: viva o muerta.Su evolución está determinada por un conjunto de reglas que consideran el estadi de sus células vecinas.
## 📂 Estructura del Proyecto
* **`game_logic.py`**: Contiene la lógica central del autómata celular y las reglas de transición de Conway.
* **`app.py`**: Interfaz de usuario interactiva desarrollada con Streamlit.
* **`requirements.txt`**: Archivo con las dependencias necesarias para ejecutar la aplicación.

## ⚙️ Instrucciones de Instalación y Ejecución
1. Clona este repositorio en tu computadora.
2. Instala las dependencias ejecutando:
   ```bash
   pip install -r requirements.txt
   streamlit run app.py
   