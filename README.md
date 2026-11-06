# El Juego de la Vida (Conway's Game of Life)

Proyecto parcial desarrollado en Python utilizando Streamlit para la visualización de autómatas celulares.

## Autoras
* **Aimeé Toledo**
* **Lizbeth Graciela Cervera Romero**

## Resumen
Los autómatas celulares son modelos matemáticos y computacionales utilizados para representar sistemas computacionales utilizados para representar sistemas complejos mediante elementos individuales que interactúan siguiendo determinadas reglas. Uno de los principales retos para comprender su funcionamiento es visualizar cómo evolucionan estos sistemas con el paso del tiempo y cómo las interacciones entre sus elementos pueden generar comportamientos inesperados. Por esta razón, surge la necesidad de desarrollar una herramienta que permita representar gráficamente el comportamiento de un autómata celular y facilitar la experimentación con sus diferentes estados.

## Introducción
Los autómatas celulares son modelos matemáticos y computacionales utilizados para representar sistemas computacionales utilizados para representar sistemas complejos mediante elementos individuales que interactúan siguiendo determinadas reglas.
Uno de los principales retos para comprender su funcionamiento es visualizar cómo evolucionan estos sistemas con el paso del tiempo y cómo las interacciones entre sus elementos pueden generar comportamientos inesperados.
Por esta razón, surge la necesidad de desarrollar una herramienta que permita representar gráficamente el comportamiento de un autómata celular y facilitar la experimentación con sus diferentes estados.

## Objetivos
El objetivo general de este trabajo consiste en desarrollar una aplicación interactiva y funcional del Juego de la Vida de Conway utilizando Python y Streamlit, asegurando la reproducibilidad del código mediante control de versiones GitHub. Como objetivos principales, buscamos implementar reglas lógicas de nacimiento, supervivencia y muerte de las celdas en un archivo modular, así como incorporar una interfaz de renderizado gráfico avanzado mediante Matplotlib y la selección de patrones iniciales predefinidos, como el Glider.

## Solución 
Aquí integramos los cambios de los archivos app.py y game_logic.py:
Para resolver el problema, desarrollamos una arquitectura modular dividida en dos componentes. Por un lado, la lógica del juego contenida en un archivo específico (game_logic.py) que incluye las funciones encargadas de inicializar las cuadrículas de forma aleatoria, vacía o mediante patrones clásicos predefinidos como el Glider, además de calcular la matriz de la siguiente generación evaluando los vecinos según las reglas de Conway. Por otro lado, la interfaz de usuario desarrollada en la aplicación principal (app.py), la cual utiliza Streamlit en conjunto con Matplotlib (imshow con escala binaria) para ofrecer una representación visual limpia y profesional en lugar de texto plano. Esta interfaz incluye controles interactivos como barras deslizantes para el tamaño de la cuadrícula y la velocidad de animación, un selector de patrones iniciales y botones de control con gestión de estado para iniciar, pausar y reiniciar la simulación sin interrupciones.

## Conclusion
El desarrollo de este proyecto permitió comprender e implementar los fundamentos de los autómatas celulares. A través de la programación de sus reglas y la representación gráfica dinámica mediante mapas de calor, fue posible observar cómo un conjunto de condiciones sencillas puede producir patrones y comportamientos complejos, tal como se comprobó con el desplazamiento diagonal del patrón Glider. Asimismo, la modularización del código en Python permitió separar con éxito la lógica matemática de la interfaz gráfica, facilitando la colaboración en equipo, el control de errores y la escalabilidad del sistema.

## Estructura del Proyecto
* **`game_logic.py`**: Contiene la lógica central del autómata celular y las reglas de transición de Conway.
* **`app.py`**: Interfaz de usuario interactiva desarrollada con Streamlit.
* **`requirements.txt`**: Archivo con las dependencias necesarias para ejecutar la aplicación.

## Instrucciones de Instalación y Ejecución
Para probar e instalar este proyecto en cualquier computadora, es necesario clonar el repositorio desde GitHub, intalar las dependencias necesarias indicadas en el archivo de requisitos mediante el comando de instalación de paquetes de Python y finalmente ejecutar la aplicación de Streamlit para desplegar la interfaz en el navegador web local.
Ejemplo:
1. Clona este repositorio en tu computadora.
2. Instala las dependencias ejecutando:
   ```bash
   pip install -r requirements.txt
   streamlit run app.py
   