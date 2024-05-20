from auxiliary_functions import *
from settings import *
import copy

class DFSi_Solver:
    def __init__(self):
        self.goal = None

    def find_zero_pos(self, grid):
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    return (row, col)

    def generate_moves(self, pos):
        moves = []
        GAMESIZE = len(self.grid)
        
        x, y = pos
        if (x > 0): moves.append((x - 1, y))  # Pode mover para cima
        if (x < GAMESIZE - 1): moves.append((x + 1, y))  # Pode mover para baixo
        if (y > 0): moves.append((x, y - 1))  # Pode mover para esquerda
        if (y < GAMESIZE - 1): moves.append((x, y + 1))  # Pode mover para direita
        return moves

    def move_tile(self, grid, pos, empty_pos):
        new_grid = copy.deepcopy(grid)
        x1, y1 = pos
        x2, y2 = empty_pos
        new_grid[x2][y2], new_grid[x1][y1] = new_grid[x1][y1], new_grid[x2][y2]
        return new_grid

    def dfs_limited(self, grid, empty_pos, depth, path, visited):
        if (grid == self.goal):
            return path
        # Delimita a profundidade
        if (depth == 0):
            return None
        
        visited.add(turn_grid_to_tuple(grid))
        
        for move in self.generate_moves(empty_pos):
            new_grid = self.move_tile(grid, move, empty_pos)
            new_tuple = turn_grid_to_tuple(new_grid)
            
            if (new_tuple not in visited):
                result = self.dfs_limited(new_grid, move, depth - 1, path + [new_grid], visited)
                if (result is not None):
                    return result
        
        visited.remove(turn_grid_to_tuple(grid))
        return None

    def dfsi_solver(self, grid, objective):
        self.grid = grid
        self.goal = objective
        depth = 0
        while (True):
            visited = set()
            result = self.dfs_limited(grid, self.find_zero_pos(grid), depth, [grid], visited)
            if (result is not None):
                return result
            # Incrementa a profundidade para a próxima iteração
            depth += 1

if __name__ == "__main__":
    solver = DFSi_Solver()
    
    objetivo = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    
    teste = [
        [1, 2, 3],
        [4, 6, 0],
        [7, 5, 8]
    ]
    
    solution = solver.dfsi_solver(teste, objetivo)
    
    print_states(solution)
