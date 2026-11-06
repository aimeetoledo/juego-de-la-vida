import random

class GameOfLife:
    def __init__(self, rows=20, cols=20):
        self.rows = rows
        self.cols = cols
        self.grid = [[random.choice([0, 1]) for _ in range(cols)] for _ in range(rows)]

    def step(self):
        """Calcula la siguiente generación según las reglas de Conway."""
        new_grid = [[0 for _ in range(self.cols)] for _ in range(self.rows)]
        
        for r in range(self.rows):
            for c in range(self.cols):
                neighbors = 0
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        if i == 0 and j == 0:
                            continue
                        nr, nc = r + i, c + j
                        if 0 <= nr < self.rows and 0 <= nc < self.cols:
                            neighbors += self.grid[nr][nc]
                
                if self.grid[r][c] == 1:
                    if neighbors in [2, 3]:
                        new_grid[r][c] = 1
                    else:
                        new_grid[r][c] = 0
                else:
                    if neighbors == 3:
                        new_grid[r][c] = 1
                        
        self.grid = new_grid
        