from auxiliary_functions import turn_grid_to_tuple, turn_tuple_to_grid
from settings import *
import copy

class IDDFS_Solver:
    def __init__(self):
        self.max_depth = 20  # Pode ser ajustado conforme necessário

    def iddfs(self, root, goal):
        for depth in range(self.max_depth):
            found, path = self.dls(root, goal, depth)
            if found:
                return path
        return []

    def dls(self, node, goal, depth):
        if depth == 0 and node == goal:
            return True, [node]
        elif depth > 0:
            for move in self.possible_moves(node):
                new_node = self.move(node, move)
                found, path = self.dls(new_node, goal, depth - 1)
                print(new_node)
                if found:
                    print(found)
                    return True, [node] + path
        return False, []

    def possible_moves(self, state):
        moves = []
        size = len(state)
        for i in range(size):
            if 0 in state[i]:
                blank_x, blank_y = i, state[i].index(0)
                break
        if blank_x > 0:
            moves.append('up')
        if blank_x < size - 1:
            moves.append('down')
        if blank_y > 0:
            moves.append('left')
        if blank_y < size - 1:
            moves.append('right')
        return moves

    def move(self, state, direction):
        size = len(state)
        for i in range(size):
            if 0 in state[i]:
                blank_x, blank_y = i, state[i].index(0)
                break
        new_state = [list(row) for row in state]
        if direction == 'up':
            new_state[blank_x][blank_y], new_state[blank_x - 1][blank_y] = new_state[blank_x - 1][blank_y], new_state[blank_x][blank_y]
        elif direction == 'down':
            new_state[blank_x][blank_y], new_state[blank_x + 1][blank_y] = new_state[blank_x + 1][blank_y], new_state[blank_x][blank_y]
        elif direction == 'left':
            new_state[blank_x][blank_y], new_state[blank_x][blank_y - 1] = new_state[blank_x][blank_y - 1], new_state[blank_x][blank_y]
        elif direction == 'right':
            new_state[blank_x][blank_y], new_state[blank_x][blank_y + 1] = new_state[blank_x][blank_y + 1], new_state[blank_x][blank_y]
        return tuple(tuple(row) for row in new_state)

    def solve(self, initial_state, goal_state):
        initial_state_tuple = turn_grid_to_tuple(initial_state)
        goal_state_tuple = turn_grid_to_tuple(goal_state)
        path = self.iddfs(initial_state_tuple, goal_state_tuple)
        return [turn_tuple_to_grid(state) for state in path]
    
if (__name__ == "__main__"):
    solver = IDDFS_Solver()
    
    objetivo = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 0]
    ]
    
    teste = [
        [1, 2, 3],
        [4, 6, 0],
        [7, 5, 8]
    ]
    
    solution = solver.solve(teste, objetivo)
    
    print(solution)