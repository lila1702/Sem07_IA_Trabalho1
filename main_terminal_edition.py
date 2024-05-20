from copy import deepcopy
from random import choice, randint
from settings import *
from auxiliary_functions import *
from solver_BFS import BFS_Solver
from solver_DFSi import DFSi_Solver
from solver_AWrongPcs import A_WrongPcs_Solver
from solver_AManhathan import A_Manhattan_Solver

class Game():
    def __init__(self):
        self.board = []
        self.goal_board = []
    
    def generate_board(self):
        num = 1
        for i in range(GAMESIZE):
            self.board.append([])
            for j in range(GAMESIZE):
                self.board[i].append(num)
                num += 1
        
        self.board[-1][-1] = 0
        
        self.goal_board = deepcopy(self.board)
        return self.board

    def find_empty_pos(self, grid):
        for row, tiles in enumerate(grid):
            for col, tile in enumerate(tiles):
                if (tile == 0):
                    return [row, col]
                
    def find_possible_moves(self, grid, empty_pos):
        moves = []
        x, y = empty_pos
        
        # Pode mover para cima
        if (x > 0):
            moves.append((x - 1, y))
        # Pode mover para baixo
        if (x < GAMESIZE - 1):
            moves.append((x + 1, y))
        # Pode mover para esquerda
        if (y > 0):
            moves.append((x, y - 1))
        # Pode mover para direita
        if (y < GAMESIZE - 1):
            moves.append((x, y + 1))
        return moves

    def move_tiles(self, grid, pos, empty_pos):
        new_grid = deepcopy(grid)
        x1, y1 = pos
        x2, y2 = empty_pos
        new_grid[x2][y2], new_grid[x1][y1] = new_grid[x1][y1], new_grid[x2][y2]
        return new_grid

    def print_board(self):
        print()
        
        for row in self.board:
            print(row)

    def shuffle_board(self, board):
        last_move = ()
        empty_pos = self.find_empty_pos(board)
        
        for _ in range(randint(120, 240)):
            possible_moves = self.find_possible_moves(board, empty_pos)
            possible_moves = [move for move in possible_moves if move != last_move[::-1]]
            this_choice = choice(possible_moves)
            board = self.move_tiles(board, this_choice, empty_pos)
            empty_pos = this_choice
            last_move = (empty_pos, this_choice)
        self.board = board
        self.print_board()

    def menu(self):
        shuffled = False
        solution = None
        self.generate_board()
        self.print_board()
        while (True):
            print("\nEscolha o que deseja fazer: ")
            print("1) Embaralhar tabuleiro\n2) Resetar tabuleiro\n3) BFS_Solver\n4) DFSi_Solver\n5) A_Star_WrongPieces_Solver\n6) A_Star_Manhattan_Solver\n0) Sair")
            escolha = int(input("Digite o número correspondente: ").strip())
            if (escolha == 0):
                break
            elif (shuffled == False and escolha == 1):
                self.start_game()
                shuffled = True
            elif (shuffled == True and escolha == 2 or solution != None):
                self.board = []
                self.goal_board = []
                self.generate_board()
                self.print_board()
                shuffled = False
                solution = None
            elif (shuffled == True and escolha == 3 and solution == None):
                solver = BFS_Solver()
                solution = solver.bfs_solver(self.board, self.goal_board)
                shuffled = False
            elif (shuffled == True and escolha == 4 and solution == None):
                solver = DFSi_Solver()
                solution = solver.dfsi_solver(self.board, self.goal_board)
                shuffled = False
            elif (shuffled == True and escolha == 5 and solution == None):
                solver = A_WrongPcs_Solver()
                solution = solver.a_star_wrongpcs_solver(self.board, self.goal_board)
                shuffled = False
            elif (shuffled == True and escolha == 6 and solution == None):
                solver = A_Manhattan_Solver()
                solution = solver.a_star_manhattan_solver(self.board, self.goal_board)
                shuffled = False
            else:
                print("Escolha inválida")
                
            if (solution != None):
                print_states(solution)

    def start_game(self):
        self.shuffle_board(self.board)

# MAIN
game = Game()
game.menu()