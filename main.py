import pygame
import random
import time
from settings import *
from sprite import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.shuffle_time = 0
        self.start_shuffle = False
        self.previous_choice = ""
        self.start_game = False
        self.start_timer = False
        self.elapsed_time = 0
        
        self.moves_made = 0
        
    # Movimentos Possíveis:
    def move_right(self, row, col):
        self.tiles_grid[row][col], self.tiles_grid[row][col+1] = self.tiles_grid[row][col+1], self.tiles_grid[row][col]
    def move_left(self, row, col):
        self.tiles_grid[row][col], self.tiles_grid[row][col-1] = self.tiles_grid[row][col-1], self.tiles_grid[row][col]
    def move_up(self, row, col):
        self.tiles_grid[row][col], self.tiles_grid[row-1][col] = self.tiles_grid[row-1][col], self.tiles_grid[row][col]
    def move_down(self, row, col):
        self.tiles_grid[row][col], self.tiles_grid[row+1][col] = self.tiles_grid[row+1][col], self.tiles_grid[row][col]
    
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
    
    def shuffle(self):
        possible_moves = []
        
        for row, tiles in enumerate(self.tiles):
            for col, tile in enumerate(tiles):
                if (tile.text == "Empty"):
                    if (tile.right()):
                        possible_moves.append("Right")
                    if (tile.left()):
                        possible_moves.append("Left")
                    if (tile.up()):
                        possible_moves.append("Up")
                    if (tile.down()):
                        possible_moves.append("Down")
                    break
            
            if (len(possible_moves) > 0):
                break
        
        if (self.previous_choice == "Right"):
            possible_moves.remove("Left") if "Left" in possible_moves else possible_moves
        if (self.previous_choice == "Left"):
            possible_moves.remove("Right") if "Right" in possible_moves else possible_moves
        if (self.previous_choice == "Up"):
            possible_moves.remove("Down") if "Down" in possible_moves else possible_moves
        if (self.previous_choice == "Down"):
            possible_moves.remove("Up") if "Up" in possible_moves else possible_moves
        
        choice = random.choice(possible_moves)
        self.previous_choice = choice
        
        if (choice == "Right"):
            self.move_right(row, col)
        elif (choice == "Left"):
            self.move_left(row, col)
        elif (choice == "Up"):
            self.move_up(row, col)
        elif (choice == "Down"):
            self.move_down(row, col)
    
    def draw_tiles(self):
        self.tiles = []
        for row, x in enumerate(self.tiles_grid):
            self.tiles.append([])
            for col, tile in enumerate(x):
                if (tile != 0):
                    self.tiles[row].append(Tile(self, col, row, str(tile)))
                else:
                    self.tiles[row].append(Tile(self, col, row, "Empty"))
        
    
    def new(self):
        self.all_sprites = pygame.sprite.Group()
        
        # O que vai ser mudado
        self.tiles_grid = self.create_game()
        # Vai ter o resultado
        self.tiles_grid_completed = self.create_game()
        
        self.elapsed_time = 0
        self.start_timer = False
        self.start_game = False
        self.moves_made = 0
        
        self.draw_tiles()
        
        self.buttons_list = []
        self.buttons_list.append(Button(WIDTH-(WIDTH*0.25), 50, 220, 60, "Embaralhar", WHITE, BLACK))
        self.buttons_list.append(Button(WIDTH-(WIDTH*0.25), 130, 220, 60, "Resetar", WHITE, BLACK))
    
    def run(self):
        self.playing = True
        while (self.playing):
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    
    def update(self):
        if (self.start_game):
            if (self.tiles_grid == self.tiles_grid_completed):
                self.start_game = False
                print("Ganhou")
                
            if (self.start_timer):
                self.timer = time.time()
                self.start_timer = False
            self.elapsed_time = time.time() - self.timer
        
        if (self.start_shuffle):
            self.shuffle()
            self.draw_tiles()
            self.shuffle_time += 1
            if (self.shuffle_time > 120):
                self.start_shuffle = False
                self.start_game = True
                self.start_timer = True
                
        self.all_sprites.update()
    
    def draw_grid(self):
        for row in range(-1, GAMESIZE * TILESIZE, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGRAY, (row, 0), (row, GAMESIZE * TILESIZE))
        
        for col in range(-1, GAMESIZE * TILESIZE, TILESIZE):
            pygame.draw.line(self.screen, LIGHTGRAY, (0, col), (GAMESIZE * TILESIZE, col))
    
    def draw(self):
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)
        self.draw_grid()
        for button in self.buttons_list:
            button.draw(self.screen)
            
        UIElement(WIDTH-(WIDTH*0.25)+40, 250, str("%0.3f" % self.elapsed_time)).draw(self.screen)
        UIElement(WIDTH-(WIDTH*0.25)+40, 350, str(self.moves_made)).draw(self.screen)
        pygame.display.flip()
    
    def events(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                quit(0)
                
            if (event.type == pygame.MOUSEBUTTONDOWN):
                mouse_x, mouse_y = pygame.mouse.get_pos()
                for row, tiles in enumerate(self.tiles):
                    for col, tile in enumerate(tiles):
                        if (tile.click(mouse_x, mouse_y)):
                            if (tile.right() and self.tiles_grid[row][col+1] == 0):
                                self.move_right(row, col)
                                self.moves_made += 1
                            
                            if (tile.left() and self.tiles_grid[row][col-1] == 0):
                                self.move_left(row, col)
                                self.moves_made += 1
                                
                            if (tile.up() and self.tiles_grid[row-1][col] == 0):
                                self.move_up(row, col)
                                self.moves_made += 1
                                
                            if (tile.down() and self.tiles_grid[row+1][col] == 0):
                                self.move_down(row, col)
                                self.moves_made += 1
                                
                            self.draw_tiles()
                            
                for button in self.buttons_list:
                    if (button.click(mouse_x, mouse_y)):
                        if (button.text == "Embaralhar"):
                            self.shuffle_time = 0
                            self.start_shuffle = True
                        if (button.text == "Resetar"):
                            self.new()
    

game = Game()
while (True):
    game.new()
    game.run()