from auxiliary_functions import *
from settings import *
import copy

class A_WrongPcs_Solver():
    def generate_moves(self, empty_pos):
        possible_moves = []
        
        GAMESIZE = len(self.grid)
        
        # Pode mover para cima
        if (empty_pos[0] > 0):
            possible_moves.append([empty_pos[0] - 1, empty_pos[1]])
        # Pode mover para baixo
        if (empty_pos[0] < GAMESIZE-1):
            possible_moves.append([empty_pos[0] + 1, empty_pos[1]])
        # Pode mover para direita
        if (empty_pos[1] < GAMESIZE-1):
            possible_moves.append([empty_pos[0], empty_pos[1] + 1])
        # Pode mover para esquerda
        if (empty_pos[1] > 0):
            possible_moves.append([empty_pos[0], empty_pos[1] - 1])
        
        return possible_moves
    
    def move_tile(self, grid, pos, empty_tile):
        new_grid = copy.deepcopy(grid)
        new_grid[empty_tile[0]][empty_tile[1]], new_grid[pos[0]][pos[1]] = new_grid[pos[0]][pos[1]], new_grid[empty_tile[0]][empty_tile[1]]
        
        return new_grid
    
    def generate_states(self, grid, empty_tile_pos):
        where_to_move = self.generate_moves(empty_tile_pos)
        states = []
        
        for move in where_to_move:
            states.append(self.move_tile(grid, move, empty_tile_pos))
        
        return states
    
    def find_zero_pos(self, grid):
        for row, tiles in enumerate(grid):
            for col, tile in enumerate(tiles):
                if (tile == 0):
                    return [row, col]
    
    def reconstruct_path(self, final_state, parents_dict):
        path = []
        current_state = turn_grid_to_tuple(final_state)
        
        while (current_state != None):
            path.append(turn_tuple_to_grid(current_state))
            current_state = parents_dict.get(turn_grid_to_tuple(current_state))
        
        # Retorna os caminhos do estado inicial até o estado final
        return path[::-1]

    def find_goal_pos(self, grid, wanted_num):
        for row, tiles in enumerate(grid):
            for col, tile in enumerate(tiles):
                if (tile == wanted_num):
                    return row, col

    def count_misplaced_tiles(self, grid, objective):
        misplaced_tiles = 0
        
        for row, tiles in enumerate(grid):
            for col, tile in enumerate(tiles):
                if (tile != objective[row][col] and tile != 0):
                    misplaced_tiles += 1
        return misplaced_tiles

    def a_star_wrongpcs_solver(self, grid, objective):
        self.grid = grid
        
        game_states_queue = [grid]
        visited_game_states = set()
        parent_game_states = {}
        # Custo de ir de um estado inicial até outro estado
        g_score = {turn_grid_to_tuple(grid) : 0}
        
        while (game_states_queue):
            # Organiza a fila de prioridade de acordo com o g_score e o f_score, que é a contagem de peças nos lugares errados
            game_states_queue.sort(key=lambda x: g_score[turn_grid_to_tuple(x)] + self.count_misplaced_tiles(x, objective))
            
            current_game_state = game_states_queue.pop(0)
            current_game_state_tuple = turn_grid_to_tuple(current_game_state)
            
            visited_game_states.add(current_game_state_tuple)
            
            if (len(parent_game_states) == 0):
                parent_game_states[current_game_state_tuple] = None
            
            if (current_game_state == objective):
                return self.reconstruct_path(objective, parent_game_states)
            
            for next_state in self.generate_states(current_game_state, self.find_zero_pos(current_game_state)):
                next_state_tuple = turn_grid_to_tuple(next_state)
                
                if (next_state_tuple in visited_game_states):
                    continue
                
                new_g_score = g_score[current_game_state_tuple] + 1
                
                if (next_state_tuple not in g_score or new_g_score < g_score[next_state_tuple]):
                    parent_game_states[next_state_tuple] = current_game_state
                    g_score[next_state_tuple] = new_g_score
                    game_states_queue.append(next_state)

# PARA DEBUG

if (__name__ == "__main__"):
    solver = A_WrongPcs_Solver()
    
    objective = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    
    grid_test = [
        [1, 2, 3],
        [4, 6, 0],
        [7, 5, 8]
    ]
    
    grid_test2 = [
        [3, 7, 5],
        [1, 0, 8],
        [6, 4, 2]
    ]
    
    result = solver.a_star_wrongpcs_solver(grid_test2, objective)
    
    print_states(result)