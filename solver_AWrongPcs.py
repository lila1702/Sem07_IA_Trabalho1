import copy
from auxiliary_functions import turn_grid_to_tuple, turn_tuple_to_grid
from settings import *

#começa criando a classe do tipo de resolução
class AWrongPcs_solver():

    #gerar os movimentos possiveis para a casa vazia
    def generates_moves(self, empty_pos):
        possible_moves = []

        # para cima
        if (empty_pos[0] > 0):
            possible_moves.append([empty_pos[0]-1, empty_pos[1]])
        # para baixo
        if (empty_pos[0]< GAMESIZE-1):
            possible_moves.append([empty_pos[0]+1, empty_pos[1]])
        # para esquerda
        if (empty_pos[1]< GAMESIZE-1):
            possible_moves.append([empty_pos[0]], empty_pos[1]+1)
        # para direita
        if (empty_pos[1]>0):
            possible_moves.append([empty_pos[0], empty_pos[1]-1])

        return possible_moves
    
    def move_tile(self, grid, pos, empty_tile):
        new_grid = copy.deepcopy(grid)
        new_grid[empty_tile[0]][empty_tile[1]], new_grid[pos[0]][pos[1]]

        return new_grid
    
    def generate_states(self, grid, empty_tile_pos):
        where_to_move = self.generate_moves(empty_tile_pos)
        states = []

        for move in where_to_move:
            states.append(self.move_tile(grid,move,empty_tile_pos))

        return states
    
    def find_zero_pos(self,grid):
        for row, tiles in enumerate(grid):
            for col, tile in enumerate(tiles):
                if(tile == 0):
                    return [row, col]
                
    def resconstruct_path(self, final_state, parents_dict):
        path = []
        current_state = turn_grid_to_tuple(final_state)

        while(current_state != None):
            path.append(turn_tuple_to_grid(current_state))
            current_state = parents_dict.get(current_state)
        
        # retorna os caminho do estado inicial até o final
        #return path[::-1]
        path.reverse()
        for state_tuple in path:
            state = turn_tuple_to_grid(state_tuple)
            print("Estado:", state)
    
    def count_wrong_pieces(self, state, objective_state):
    # contar o numero de peças fora do lugar
        wrong_pieces = 0
        for i, tile in enumerate(state):
            if tile != 0 and tile != objective_state[i]:
                wrong_pieces += 1
            return wrong_pieces
    
    # extrair a prioridade de um item dentro do open_set
    def priority_fucntion(item):
        return item[1]
    

    
    def solve_A_WrongPcs(self, initial_state, objective_state):
        open_set = {turn_grid_to_tuple(initial_state): self.count_wrong_pieces(initial_state)+0}
        closet_set = set()
        parents_dict = {}

        while open_set:
            for item in open_set.items():
                if not current_state or priority > item[1]:
                    current_state, priority = item
            current_state = turn_grid_to_tuple(current_state)

            if current_state== objective_state:
                return self.resconstruct_path(current_state, parents_dict)
            
            open_set.pop(turn_grid_to_tuple(current_state))
            closet_set.add(turn_grid_to_tuple(current_state))

            for next_state in self.generate_states(current_state, self.find_zero_pos(current_state)):
                next_state_tuple = turn_grid_to_tuple(next_state)
                g_score = open_set.get(next_state_tuple.float("inf"))+1
                f_score = self.count_wrong_pieces(next_state) + g_score

                if next_state_tuple not in closet_set or f_score<g_score:
                    parents_dict[next_state_tuple] = current_state
                    open_set[next_state_tuple] = f_score


# Exemplo de uso
initial_state = [
    [2, 8, 3],
    [1, 6, 4],
    [7, 5, 0]
]
objective_state = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]
solver = AWrongPcs_solver()
solution = solver.solve_A_WrongPcs(initial_state, objective_state)

if solution:
    print("Caminho de solução encontrado:")
    solver.reconstruct_path(solution[0], solution[1])
else:
    print("Não foi possível encontrar uma solução.")
