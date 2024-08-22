def turn_grid_to_tuple(grid):
    return tuple(tuple(row) for row in grid)
    
def turn_tuple_to_grid(tup):
    return [list(row) for row in tup]

def print_states(solution_list):
    if (solution_list):
        for state in solution_list:
            for row in state:
                print(row)
            print()
    else:
        print("Não foi encontrada nenhuma solução.")