'''
Day 17
I did this keeping track of the entire grid. A more efficient method
would probably have been to just keep track fo the location of the active sites
'''

import util
import copy

def task_1_2(grid, days_to_simulate, dim4):
    '''
    Runs the simulation for the number of days specified and then counts the 
    number of active sites in the grid.

    Inputs:
        grid (list of list of lists or list of lists of lists of lists):
            gives the initial location of active sites
        days_to_simulate (int): number of days to run the simulation
        dim4 (boolean): Whether we're working in 4 dimensions (task 2)

    Outputs: num_activiated (int): the number of active sites after running the 
        full simulation
    '''
    for i in range(days_to_simulate):
        updated_grid = simulate_one_step(grid, dim4)
        grid = updated_grid
    num_activated = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            for k in range(len(grid[0][0])):
                if dim4:
                    for m in range(len(grid[0][0][0])):
                        num_activated += grid[i][j][k][m]
                else:
                    num_activated += grid[i][j][k]
    return num_activated

def copy_list(grid, dim4):
    '''
    Helper function that copies the grid for the simulate function
    
    Inputs:
        grid (list of list of lists or list of lists of lists of lists):
            location of active sites
        dim4 (boolean): Whether we're working in 4 dimensions (task 2)

    Outputs: rv_grid (list of list of lists or list of lists of lists of lists):
        the updated grid

    Outputs: new_grid (list of list of lists or list of lists of lists of lists):
        copy of the original list
    '''
    new_grid=[]
    for layer in grid:
        new_layer = []
        for row in layer:
            new_row = []
            for elt in row:
                if dim4:
                    new_elt = []
                    for hyperelt in elt:
                        new_elt.append(hyperelt)
                    new_row.append(new_elt)
                else:
                    new_row.append(elt)
            new_layer.append(new_row)
        new_grid.append(new_layer)
    return new_grid


def simulate_one_step(grid, dim4):
    '''
    Runs one cycle of the simulation.

    Inputs:
        grid (list of list of lists or list of lists of lists of lists):
            location of active sites
        dim4 (boolean): Whether we're working in 4 dimensions (task 2)

    Outputs: rv_grid (list of list of lists or list of lists of lists of lists):
        the updated grid
    '''
    if dim4:
        new_grid = expand_grid_4dim(grid)
    else:
        new_grid = expand_grid(grid)
    rv_grid = copy_list(new_grid, dim4)
    for i in range(len(new_grid)):
        for j in range(len(new_grid[0])):
            for k in range(len(new_grid[0][0])):
                if dim4:
                    for m in range(len(new_grid[0][0][0])):
                        num_activated = num_neighbors_activated(
                            new_grid, (i, j, k, m), dim4)
                        if new_grid[i][j][k][m] == 1 and not (
                            num_activated == 2 or num_activated == 3):
                            rv_grid[i][j][k][m] = 0
                        elif new_grid[i][j][k][m] == 0 and num_activated == 3:
                            rv_grid[i][j][k][m] = 1
                else:
                    num_activated = num_neighbors_activated(
                        new_grid, (i, j, k), dim4)
                    if new_grid[i][j][k] == 1 and not (
                        num_activated == 2 or num_activated == 3):
                        rv_grid[i][j][k] = 0
                    elif new_grid[i][j][k] == 0 and num_activated == 3:
                        rv_grid[i][j][k] = 1
    return rv_grid

    

def num_neighbors_activated(grid, position, dim4):
    '''
    Helper function for simulate_one_step. Finds the number of active neighbors
    
    Inputs:
        grid (list of list of lists or list of lists of lists of lists):
            location of active sites
        position (tuple): a location in the grid
        dim4 (boolean): Whether we're working in 4 dimensions (task 2)

    Outputs: num_activated (int): the number of neighbors currently active
    '''
    num_activated = 0
    if dim4:
        layer, row, col, hyp = position
    else:
        layer, row, col = position
    for i in range(max(0, layer-1), min(len(grid)-1, layer + 1)+1):
        for j in range(max(0, row-1), min(len(grid[0])-1, row + 1)+1):
            for k in range(max(0, col-1), min(len(grid[0][0])-1, col + 1)+1):
                if dim4:
                    for m in range(max(0, hyp-1), min(
                            len(grid[0][0][0])-1, hyp + 1)+1):
                        if (i, j, k, m) != position:
                            num_activated += grid[i][j][k][m]
                else:
                    if (i, j, k) != (layer, row, col):
                        num_activated += grid[i][j][k]
    return num_activated
                    
      

def expand_grid_4dim(grid):
    '''
    Helper function for simulate_one_step. Expands the grid so that we can run 
        the next cycle of the simualtion. Task 2 version
    
    Inputs: 
        grid (list of lists of lists of lists): location of active sites

    Outputs: new_grid (list of lists of lists of lists): expanded grid showing 
                location of active sites
    '''
    hyp_num = len(grid[0][0][0])
    col_num = len(grid[0][0])
    row_num = len(grid[0])
    new_grid = []
    new_grid.append([[[0] * (hyp_num + 2)] * (col_num + 2)] * (row_num + 2))
    for layer in grid:
        new_layer = [[[0] * (hyp_num + 2)] * (col_num + 2)]
        for row in layer:
            new_row = [[0] * (hyp_num + 2)]
            for hyp in row:
                new_hyp = [0]
                new_hyp += hyp
                new_hyp.append(0)
                new_row.append(new_hyp)
            new_row.append([0] * (hyp_num + 2))
            new_layer.append(new_row)
        new_layer.append([[0] * (hyp_num + 2)] * (col_num + 2))
        new_grid.append(new_layer)
    new_grid.append([[[0] * (hyp_num + 2)] * (col_num + 2)] * (row_num + 2))
    return new_grid


def expand_grid (grid):
    '''
    Helper function for simulate_one_step. Expands the grid so that we can run 
        the next cycle of the simualtion. Task 1 version
    
    Inputs: 
        grid (list of lists of lists) location of active sites

    Outputs: new_grid (list of lists of lists): expanded grid showing 
                location of active sites
    '''
    col_num = len(grid[0][0])
    row_num = len(grid[0])
    new_grid = []
    new_grid.append([[0] * (col_num + 2)] * (row_num + 2))
    for layer in grid:
        new_layer = [[0] * (col_num + 2)]
        for row in layer:
            new_row = [0]
            new_row += row
            new_row.append(0)
            new_layer.append(new_row)
        new_layer.append([0] * (col_num + 2))
        new_grid.append(new_layer)
    new_grid.append([[0] * (col_num + 2)] * (row_num + 2))
    return new_grid




if __name__ == "__main__":
    lines = util.read_strs("inputs/day17_inputs.txt")

    # creates the list of lists
    init_inpt = []
    for line in lines:
        init_line = []
        for val in line:
            if val == '.':
                init_line.append(0)
            else:
                init_line.append(1)
        init_inpt.append(init_line)

    # given test data
    tst = [[[0, 1, 0], [0, 0, 1], [1, 1, 1]]]

    print("TASK 1")
    util.call_and_print(task_1_2, tst, 6, False)
    util.call_and_print(task_1_2, [init_inpt], 6, False)

    print("\nTASK2")
    util.call_and_print(task_1_2, [tst], 6, True)
    util.call_and_print(task_1_2, [[init_inpt]], 6, True)
