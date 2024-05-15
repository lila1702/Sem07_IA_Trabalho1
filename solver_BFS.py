import copy
from auxiliary_functions import turn_grid_to_tuple, turn_tuple_to_grid

class BFS_Solver():
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
            current_state = parents_dict.get(current_state)
        
        # Retorna os caminhos do estado inicial até o estado final
        return path[::-1]
    
    def bfs_solver(self, grid, objective):
        # Inicialita a fila de game_states, o set para os game_states visitados e o dicionário de parentesco dos game_states
        game_states_queue = [grid]
        visited_game_states = set()
        parent_game_state = {}
        
        # Enquanto houver game_state na fila
        while (game_states_queue != []):
            current_game_state = game_states_queue.pop(0)
            empty_tile_pos = self.find_zero_pos(current_game_state)
            current_state_tuple = turn_grid_to_tuple(current_game_state)
            
            # Adiciona o game_state atual ao set de visitados
            visited_game_states.add(current_state_tuple)
            
            # Se esse é o primeiro state, coloque que seu parentesco é None
            if (len(parent_game_state) == 0):
                parent_game_state[current_state_tuple] = None
            
            # Se o game_state atual é igual ao estado meta, começa a reconstrução do parentesco e retorna
            # todo os estados que fizeram chegar até o resultado
            if (current_game_state == objective):
                return self.reconstruct_path(objective, parent_game_state)
            
            # Gera os novos estados possíveis a partir do estado atual
            new_states = self.generate_states(current_game_state, empty_tile_pos)
            for new_state in new_states:
                new_state_tuple = turn_grid_to_tuple(new_state)
                # Se o novo estado ainda não foi visitado, adiciona-o na fila, e atualiza o dict de parentescos
                if (new_state_tuple not in visited_game_states):
                    game_states_queue.append(new_state)
                    parent_game_state[new_state_tuple] = current_state_tuple
        
        # Não achou solução
        return None

# PARA DEBUG
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
    
    resposta = solver.bfs_solver(grid_test, grid)
    
    if resposta:
        for state in resposta:
            for row in state:
                print(row)
            print()
    else:
        print("Não foi encontrada nenhuma solução.")