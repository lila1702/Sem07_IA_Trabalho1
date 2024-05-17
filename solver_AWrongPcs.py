import copy
from auxiliary_functions import turn_grid_to_tuple, turn_tuple_to_grid
from settings import *
#PRIMEIRO DE TUDO ESSA RUMA DE PRINT DE BICHO ERA PRA SABER ONDE TAVA ERRADO

#começa criando a classe do tipo de resolução
class AWrongPcs_solver():

    #gerar os movimentos possiveis para a casa vazia
    def generate_moves(self, empty_pos):
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
        
        # retorna os caminho do estado inicial até o final]
        print(path)
        return path[::-1]
        

    
    def count_wrong_pieces(self, state, objective_state):
    # contar o numero de peças fora do lugar
        wrong_pieces = 0
        for i, tile in enumerate(state):
            if tile != 0 and tile != objective_state[i]:
                wrong_pieces += 1
            return wrong_pieces
        print(wrong_pieces)
        
    def solve_A_WrongPcs(self, initial_state, objective_state):
        open_set = {turn_grid_to_tuple(initial_state): self.count_wrong_pieces(initial_state, objective_state)+0}
        #open_set = {turn_grid_to_tuple(initial_state): self.count_wrong_pieces(initial_state)}
        closet_set = set()
        parents_dict = {}

        print("girafa")
        while open_set:

            current_state, priority = min(open_set.items(), key=lambda x: x[1])
            current_state = turn_grid_to_tuple(current_state)

            if current_state== objective_state:
                return self.resconstruct_path(current_state, parents_dict)
            
            open_set.pop(turn_grid_to_tuple(current_state))
            closet_set.add(turn_grid_to_tuple(current_state))

            for next_state in self.generate_states(current_state, self.find_zero_pos(current_state)):
                next_state_tuple = turn_grid_to_tuple(next_state)
                g_score = float("inf")
                if next_state_tuple in open_set:
                    g_score = open_set[next_state_tuple] + 1
                else:
                    g_score = float("inf") + 1
                f_score = self.count_wrong_pieces(next_state, objective_state) + g_score

            if next_state_tuple not in closet_set or f_score < g_score:
                print("rinoceronte")
                continue
            parents_dict[next_state_tuple] = current_state
            open_set[next_state_tuple] = f_score
            print("hipotamo")
        

if (__name__ == "__main__"):
    solver = AWrongPcs_solver()
    
    objective_state = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    
    initial_state = [
        [1, 2, 3],
        [4, 6, 0],
        [7, 5, 8]
    ]
    
    solution_path = solver.solve_A_WrongPcs(initial_state, objective_state)
    print(solution_path)
    print('elefante')
