def turn_grid_to_tuple(grid):
    return tuple(tuple(row) for row in grid)
    
def turn_tuple_to_grid(tup):
    return [list(row) for row in tup]