import random
import time
from settings import *
from solver_BFS import BFS_Solver
from solver_DFSi import IDDFS_Solver
# from solver_AWrongPcs import AWrongPcs_Solver
from solver_AManhathan import A_Manhattan_Solver

class Game:
    def __init__(self):
        self.shuffle_time = 0
        self.start_shuffle = False
        self.previous_choice = ""
        self.start_game = False
        self.start_timer = False
        self.shuffled = False
        
        self.aux_gamestate = []
        
        self.solver_types = {
                            1 : "Humano",
                            2 : "BFS",
                            3 : "DFSi",
                            4 : "A* WrngPcs",
                            5 : "A* Manhattan"
                            }
        self.solver_used = self.solver_types[1]
        self.solution_steps = []
        self.solution_index = 0
        
        self.moves_made = 0
        
    def create_game(self):
        grid = []
        number = 1
        for x in range(GAMESIZE):
            grid.append([])
            for y in range (GAMESIZE):
                grid[x].append(number)
                number += 1
        
        grid[-1][-1] = 0
        return grid
    
    def new(self):
        # O que vai ser mudado
        self.tiles_grid = self.create_game()
        # Vai ter o resultado
        self.tiles_grid_completed = self.create_game()
        
        self.start_timer = False
        self.start_game = False
        self.moves_made = 0
        self.shuffled = False
        self.solver_used = self.solver_types[1]
        
        self.solution_steps = []
        self.solution_index = 0
    
    def generate_moves(self, empty_pos):
        possible_moves = []
        
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
    
    def find_zero_pos(self, grid):
        for row, tiles in enumerate(grid):
            for col, tile in enumerate(tiles):
                if (tile == 0):
                    return [row, col]
    
    def move_tile(self, zero_pos, new_pos):
        zero_pos[0], zero_pos[1], new_pos[0], new_pos[1] = new_pos[0], new_pos[1], zero_pos[0], zero_pos[1]
    
    def right(self, col):
        if (col < GAMESIZE-1):
            return True
    def left(self, col):
        if (col > 0):
            return True
    def up(self, row):
        if (row > 0):
            return True
    def down(self, row):
        if (row < GAMESIZE-1):
            return True
    
    def shuffle_grid(self):
        zero_pos = self.find_zero_pos(self.tiles_grid)
        possible_moves = []
        
        if (self.right(zero_pos[1])):
            possible_moves.append("Right")
        if (self.left(zero_pos[1])):
            possible_moves.append("Left")
        if (self.up(zero_pos[0])):
            possible_moves.append("Up")
        if (self.down(zero_pos[0])):
            possible_moves.append("Down")
        
        if (self.previous_choice == "Right"):
            possible_moves.remove("Left") if "Left" in possible_moves else possible_moves
        if (self.previous_choice == "Left"):
            possible_moves.remove("Right") if "Right" in possible_moves else possible_moves
        if (self.previous_choice == "Up"):
            possible_moves.remove("Down") if "Down" in possible_moves else possible_moves
        if (self.previous_choice == "Down"):
            possible_moves.remove("Up") if "Up" in possible_moves else possible_moves
        
        choice = random.choice(possible_moves)
        if (choice == "Right"):
            self.previous_choice = "Right"
            new_pos = [zero_pos[0+1], zero_pos[1]]
        if (choice == "Left"):
            self.previous_choice = "Left"
            new_pos = [zero_pos[0-1], zero_pos[1]]
        if (choice == "Up"):
            self.previous_choice = "Up"
            new_pos = [zero_pos[0], zero_pos[1+1]]
        if (choice == "Down"):
            self.previous_choice = "Down"
            new_pos = [zero_pos[0+1], zero_pos[1-1]]
            
        self.move_tile(zero_pos, new_pos)
        
    def print_grid(self, grid):
        for row in grid:
            print(row)
    
    def play(self):
        self.shuffle_grid()
    
    def run(self):
        self.print_grid(self.tiles_grid)
        print("\nDigite 'q' para sair, '1' para jogar, '2' para usar o BFS, '3' para usar o DFS, '4' para usar o A* com heurística de peças erradas e '5' para usar o A* com heurística de manhattan")

# O JOGO:
game = Game()
while (True):
    game.new()
    game.run()
    player_input = input().strip().lower()
    if (player_input == 'q'):
        break
    if (player_input == '1'):
        game.play()
    if (player_input == '2'):
        pass
    if (player_input == '3'):
        pass
    if (player_input == '4'):
        pass
    if (player_input == '5'):
        pass