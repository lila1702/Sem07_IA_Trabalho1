from settings import *
import copy

class BFS_Solver():
    def __init__(self):
        moves_made = []
    
    def generate_moves(self, empty_pos):
        possible_moves = []
        
        # Pode mover para cima
        if (empty_pos[0] > 0):
            possible_moves.append([empty_pos[0] - 1, empty_pos[1]])
        # Pode mover para baixo
        if (empty_pos[0] < 2):
            possible_moves.append([empty_pos[0] + 1, empty_pos[1]])
        # Pode mover para direita
        if (empty_pos[1] < 2):
            possible_moves.append([empty_pos[0], empty_pos[1] + 1])
        # Pode mover para esquerda
        if (empty_pos[1] > 0):
            possible_moves.append([empty_pos[0], empty_pos[1] - 1])
            
        #print(possible_moves)
        return possible_moves
    
    def move_tile(self, grid, pos, empty_tile):
        for row, tiles in enumerate(grid):
            for col, tile in enumerate(tiles):
                if (row == empty_tile[0] and col == empty_tile[1]):
                    # Troca as posições do lugar vazio com a posição verificada
                    grid[row][col], grid[pos[0]][pos[1]] = grid[pos[0]][pos[1]], grid[row][col]
                    return grid
    
    def generate_states(self, grid, empty_tile_pos):
        where_to_move = self.generate_moves(empty_tile_pos)
        states = []
        
        num_possible_moves = len(where_to_move)
        
        for i in range(num_possible_moves):
            states.append(copy.deepcopy(grid))
            states[i] = self.move_tile(states[i], where_to_move[i], empty_tile_pos)
            
        return states
    
    def find_zero_pos(self, grid):
        empty_tile_pos = []

        for row, tiles in enumerate(grid):
            for col, tile in enumerate(tiles):
                if (tile == 0):
                    empty_tile_pos.append(row)
                    empty_tile_pos.append(col)
                    print(f"Empty_tile_pos: {empty_tile_pos}")
                    return empty_tile_pos
            
    def bfs_solver(self, grid, objective):
        #print(grid)
        empty_tile_pos = self.find_zero_pos(grid)
        initial_state = grid
        # Guardará os game states que devem ser visitados
        game_states_queue = []
        # Guardará os game states visitados
        visited_game_states = []
        
        game_states_queue.append(grid)
        #visited_game_states.append(initial_state)
        
        while (len(game_states_queue) != 0):
            current_game_state = game_states_queue.pop(0)
            #print(current_game_state)
            if (current_game_state == objective):
                return self.moves_made
        
            new_states = self.generate_states(grid, empty_tile_pos)
            size = len(new_states)
            for n in range(size):
                game_states_queue.append(new_states[n])
                
            visited_game_states.append(current_game_state)            
            
            print(visited_game_states)
            print(game_states_queue)
            break
        
if __name__ == "__main__":
    solver = BFS_Solver()
    
    grid = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    
    grid_test = [
        [1, 2, 3],
        [4, 6, 0],
        [7, 5, 8]
    ]
    
    #solver.move_tile(grid_test, [2, 2])
    solver.bfs_solver(grid_test, grid)
    
    # TERMINAR MOVE_TILE E COLOCAR PRA ELE MODIFICAR A POSIÇÃO DO STATE