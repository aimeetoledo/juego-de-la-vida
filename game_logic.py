import numpy as np

def crear_grid_vacio(filas, columnas):
    """Crea una cuadrícula llena de ceros (muertas)."""
    return np.zeros((filas, columnas), dtype=int)

def crear_grid_aleatorio(filas, columnas):
    """Crea una cuadrícula con celdas vivas (1) y muertas (0) al azar."""
    return np.random.choice([0, 1], size=(filas, columnas), p=[0.8, 0.2])

def actualizar_grid(grid):
    """Calcula la siguiente generación según las reglas del Juego de la Vida."""
    nueva_grid = grid.copy()
    filas, columnas = grid.shape
    
    for r in range(filas):
        for c in range(columnas):
            # Contar vecinos vivos rodeando la celda
            vecinos_vivos = 0
            for i in range(-1, 2):
                for j in range(-1, 2):
                    if i == 0 and j == 0:
                        continue
                    vr, vc = r + i, c + j
                    if 0 <= vr < filas and 0 <= vc < columnas:
                        vecinos_vivos += grid[vr, vc]
            
            # Aplicar reglas de Conway
            if grid[r, c] == 1:
                if vecinos_vivos < 2 or vecinos_vivos > 3:
                    nueva_grid[r, c] = 0
            else:
                if vecinos_vivos == 3:
                    nueva_grid[r, c] = 1
                    
    return nueva_grid