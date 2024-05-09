from settings import *

class BFS_Solver():
    def __init__(self):
        self.possible_moves = []
        self.empty_tile_pos = []
    
    def generate_moves(self, grid, empty_pos):
        # Pode mover para cima
        if (empty_pos[0] > 0):
            self.possible_moves.append([empty_pos[0] - 1, empty_pos[1]])
        # Pode mover para baixo
        if (empty_pos[0] < 2):
            self.possible_moves.append([empty_pos[0] + 1, empty_pos[1]])
        # Pode mover para direita
        if (empty_pos[1] > 0):
            self.possible_moves.append([empty_pos[0], empty_pos[1] + 1])
        # Pode mover para esquerda
        if (empty_pos[1] < 0):
            self.possible_moves.append([empty_pos[0], empty_pos[1] - 1])
            
        print(self.possible_moves)
    
    def bfs_solver(self, grid, objective):
        print(grid)
        
        for row, tiles in enumerate(grid):
            for col, tile in enumerate(tiles):
                if (tile == 0):
                    self.empty_tile_pos.append(row)
                    self.empty_tile_pos.append(col)
                    print(self.empty_tile_pos)
        
        self.generate_moves(grid, self.empty_tile_pos)