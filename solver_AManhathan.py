from auxiliary_functions import *
from settings import *
import copy

class A_Manhattan_Solver():
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

    def calculate_manhattan_distance(self, grid, objective):
        manhattan_cost = 0
        
        for row, tiles in enumerate(grid):
            for col, tile in enumerate(tiles):
                if (tile != 0):
                    goal_row, goal_col = self.find_goal_pos(objective, tile)
                    # Manhattan Cost: |x1 - x2| + |y1 - y2|
                    manhattan_cost += abs(row - goal_row) + abs(col - goal_col)
        return manhattan_cost

    def a_star_manhattan_solver(self, grid, objective):
        self.grid = grid
        game_states_queue = [grid]
        visited_game_states = set()
        parent_game_states = {}
        # Custo de ir de um estado inicial até outro estado
        g_score = {turn_grid_to_tuple(grid) : 0}
        
        while (game_states_queue):
            # Organiza a fila de prioridade de acordo com o g_score e o f_score, que é a soma das manhattan distances
            game_states_queue.sort(key=lambda x: g_score[turn_grid_to_tuple(x)] + self.calculate_manhattan_distance(x, objective))
            
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
                
                if (next_state_tuple not in game_states_queue):
                    game_states_queue.append(next_state)
                elif (new_g_score >= g_score[next_state]):
                    continue
                
                parent_game_states[next_state_tuple] = current_game_state
                g_score[next_state_tuple] = new_g_score

if (__name__ == "__main__"):
    debug_mode = True
    
    solver = A_Manhattan_Solver()
    
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
    
    objective2 = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 0]
    ]
    
    grid_test3 = [
        [5, 1, 2, 3],
        [6, 10, 7, 4],
        [9, 11, 0, 8],
        [13, 14, 15, 12]
    ]
    
    resposta = solver.a_star_manhattan_solver(grid_test3, objective2)
    
    print_states(resposta)