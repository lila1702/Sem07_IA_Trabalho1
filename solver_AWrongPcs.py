import copy
from auxiliary_functions import turn_grid_to_tuple, turn_tuple_to_grid
from settings import *

class AWrongPcs_Solver():
    # Gera movimentos possíveis para a casa vazia
    def generate_moves(self, empty_pos):
        possible_moves = []

        # Verifica movimentos válidos em todas as direções
        if empty_pos[0] > 0:
            possible_moves.append([empty_pos[0] - 1, empty_pos[1]])
        if empty_pos[0] < GAMESIZE -1:
            possible_moves.append([empty_pos[0] + 1, empty_pos[1]])
        if empty_pos[1] < GAMESIZE -1:
            possible_moves.append([empty_pos[0], empty_pos[1] + 1])
        if empty_pos[1] > 0:
            possible_moves.append([empty_pos[0], empty_pos[1] - 1])

        return possible_moves
  
  # cria uma copia da grade para evitar modificações no original
    def move_tile(self, grid, pos, empty_tile):
        new_grid = copy.deepcopy(grid)
        #troca as posições das peças na posição espercificada com o espaço vazio
        new_grid[empty_tile[0]][empty_tile[1]], new_grid[pos[0]][pos[1]] = new_grid[pos[0]][pos[1]], new_grid[empty_tile[0]][empty_tile[1]]
        # retorna a nova grade 
        return new_grid
    
    # Gera todos os estados possíveis a partir do atual
    def generate_states(self, grid, empty_tile_pos):
        where_to_move = self.generate_moves(empty_tile_pos)
        states = []

        for move in where_to_move:
            states.append(self.move_tile(grid, move, empty_tile_pos))

        return states

    def find_zero_pos(self, grid):
        # Encontra a posição da casa vazia
        for row, tiles in enumerate(grid):
            for col, tile in enumerate(tiles):
                if tile == 0:
                    return [row, col]

    def count_wrong_pieces(self, state, objective_state):
        # Conta o número de peças fora do lugar
        wrong_pieces = 0
        for i, tile in enumerate(state):
            if tile != 0 and tile != objective_state[i]:
                wrong_pieces += 1
        return wrong_pieces
    
    def reconstruct_path(self, current_state, parents, objective_state):
        path = []
        while current_state != objective_state:
            path.append(current_state)
            current_state = parents[turn_grid_to_tuple(current_state)]
        path.append(objective_state)  # Adiciona o estado final ao caminho
        path.reverse()  # Inverte a ordem para ter o caminho do início ao fim
        return path

    def priority_fucntion(item):
        return item[1]
    current_state, priority = min(open_set.items(), key=priority_function)

    def calculate_f_score(next_state):
        return self.count_wrong_pieces(next_state) + g_score

    f_score = calculate_f_score(next_state)

    def solve_puzzle_a_star(self, initial_state, objective_state):
        open_set = {turn_grid_to_tuple(initial_state): self.count_wrong_pieces(initial_state) + 0}
        closed_set = set()
        parents = {}

        while open_set:
            for item in open_set.items():
                if not current_state or priority > item[1]:
                    current_state, priority = item
            current_state = turn_tuple_to_grid(current_state)

            if current_state == objective_state:
                return self.reconstruct_path(current_state, parents)  # Supondo que reconstruct_path está em auxiliary_functions.py

            open_set.pop(turn_grid_to_tuple(current_state))
            closed_set.add(turn_grid_to_tuple(current_state))

            for next_state in self.generate_states(current_state, self.find_zero_pos(current_state)):
                next_state_tuple = turn_grid_to_tuple(next_state)
                g_score = open_set.get(next_state_tuple, float('inf')) + 1
                f_score = self.count_wrong_pieces(next_state) + g_score

                if next_state_tuple not in closed_set or f_score < g_score:
                    parents[next_state_tuple] = current_state  # Atualiza pai
                    open_set[next_state_tuple] = f_score  # Atualiza prioridade no open set

        # Nenhuma solução encontrada (opcional):
        # raise Exception("Nenhuma solução encontrada para o estado inicial fornecido.")

        return None  # Ou qualquer indicador de que não há solução
# PARA DEBUG
if __name__ == "__main__":
    solver = AWrongPcs_Solver()
    
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
    
    resposta = solver.solve_puzzle_a_star(grid_test)
    
    if resposta:
        for state in resposta:
            for row in state:
                print(row)
            print()
    else:
        print("Não foi encontrada nenhuma solução.")