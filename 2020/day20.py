'''
Day 20
'''
import util
import numpy as np

SEA_CREATURE_COORDS = [(0,18), 
                       (1,0), (1,5), (1,6), (1,11), (1,12), (1,17), (1,18), (1,19),
                       (2,1), (2,4), (2,7), (2,10), (2,13), (2,16)]


class Tile:
    '''
    Class representing a tile
    '''
    def __init__(self, arr, id_num):
        self.grid = arr
        self.id = id_num
        self.top = self.grid[0, :]
        self.bottom = self.grid[-1, :]
        self.right = self.grid[:, -1]
        self.left = self.grid[:, 0]
        self.top_match = False
        self.bottom_match = False
        self.left_match = False
        self.right_match = False
    
    def rotate_tile(self):
        self.grid = np.rot90(self.grid)
        self.recalculate_sides()
    
    def mirror_tile(self):
        self.grid = np.fliplr(self.grid)
        self.recalculate_sides()
    
    def recalculate_sides(self):
        self.top = self.grid[0, :]
        self.bottom = self.grid[-1, :]
        self.right = self.grid[:, -1]
        self.left = self.grid[:, 0]

    def calc_num_match(self):
        self.num_match = 0
        if self.top_match:
            self.num_match += 1
        if self.bottom_match:
            self.num_match += 1
        if self.left_match:
            self.num_match += 1
        if self.right_match:
            self.num_match += 1

    def __repr__(self):
        return "Tile " + str(self.id) 


def task1(tiles):
    '''
    Finds the corner tiles (those with 2 unique boundries)

    Input: 
        tiles (lst of tiles): an array of tile objects:

    Output: an integer that is the multiple of the corner ids and the 
        list of corner rectangle objects
    '''
    candidates = []
    for i, tile in enumerate(tiles):
        for j, tile_2 in enumerate(tiles):
            if tile.id != tile_2.id:
                cmp_lst = [tile_2.left, tile_2.right, tile_2.top, tile_2.bottom]
                for cmp_side in cmp_lst:
                    if np.array_equal(tile.right, cmp_side) or np.array_equal(np.flip(tile.right), cmp_side):
                        tile.right_match = True
                    if np.array_equal(tile.left, cmp_side) or np.array_equal(np.flip(tile.left), cmp_side) :              
                        tile.left_match = True
                    if np.array_equal(tile.top, cmp_side) or np.array_equal(np.flip(tile.top), cmp_side):
                        tile.top_match = True
                    if np.array_equal(tile.bottom, cmp_side) or np.array_equal(np.flip(tile.bottom), cmp_side):
                        tile.bottom_match = True
        tile.calc_num_match()
        rv_task2 = []
        if tile.num_match == 2:
            candidates.append(tile.id)
            rv_task2.append(tile)
    return int(candidates[0]) * int(candidates[1]) * int(candidates[2]) * int(candidates[3]), rv_task2


def add_boarder(grid, remaining_tiles, position):
    '''
    Adds a border piece (only one neighbor to compare) to the rectangle grid

    Input: 
        grid (lst of rectangles): an array that contains the current grid of 
            regtangle objects
        remaining tiles (lst): A list tile objects that haven't been placed yet
        Position (tuple): an x, y coordinate for the position to be added


    Output: The updated grid
    '''
    x, y = position
    above = False
    tile_added = None
    if x!= 0:
        side_to_match = grid[y][x-1].right
    else:
        side_to_match = grid[y-1][x].bottom
        above = True
    if not above:
        for tile in remaining_tiles:
            for i in range(2):
                for j in range(4):
                    if np.array_equal(side_to_match, tile.left):
                        grid[y][x] = tile
                        remaining_tiles.remove(tile)
                        return grid, remaining_tiles
                    else:
                        tile.rotate_tile()
                tile.mirror_tile()
    else:
        for tile in remaining_tiles:
            for i in range(2):
                for i in range(4):
                    if np.array_equal(side_to_match, tile.top):
                        grid[y][x] = tile
                        remaining_tiles.remove(tile)
                        return grid, remaining_tiles
                    else:
                        tile.rotate_tile()
                tile.mirror_tile()
    print("ERROR")
    return -1

def add_interior(grid, remaining_tiles, position):
    '''
    Adds a "interior" piece (two neighbors to compare) to the rectangle grid

    Input: 
        grid (lst of lst of rectangles): an array that contains the current 
            grid of regtangle objects
        remaining tiles (lst): A list tile objects that haven't been placed yet
        Position (tuple): an x, y coordinate for the position to be added


    Output: The updated grid
    '''
    x, y = position
    to_match_left = grid[y][x-1].right
    to_match_top = grid[y-1][x].bottom
    for tile in remaining_tiles:
            for i in range(2):
                for j in range(4):
                    if np.array_equal(to_match_left, tile.left) and np.array_equal(to_match_top, tile.top):
                        grid[y][x] = tile
                        remaining_tiles.remove(tile)
                        return grid, remaining_tiles
                    else:
                        tile.rotate_tile()
                tile.mirror_tile()
    print("ERROR")
    return -1

def create_grid(grid, remaining_tiles):
    '''
    Creates the grid of rectangles

    Input: 
        grid (lst of lsts): an array thats a subset of the full grid:
        remaining tiles (lst): A list tile objects that haven't been placed yet

    Output: A boolean giving whether the subgrid contains a sea creature.
    '''
    n = len(grid)
    for y in range(n):
        for x in range(n):
            if (x, y) == (0, 0):
                continue
            elif (x == 0 or y == 0):
                grid, remaining_tiles = add_boarder(grid, remaining_tiles, (x, y))
            else:
                grid, remaining_tiles = add_interior(grid, remaining_tiles, (x, y))
    return grid


def stitch_grid(gen_grid):
    '''
    Stitches a grid together from a list of lists of tile objects

    Input: 
        gen_grid (lst of lst of tiles): a full list of list of tile 
            objects that the stitched grid will correspond to

    Output: an np.array of the stitched grid
    '''
    n = len(gen_grid)
    for y in range(n):
        for x in range(n):
            if x == 0:
                row = gen_grid[y][x].grid[1:-1 ,1:-1]
            elif x == n-1:
                row = np.concatenate((row, gen_grid[y][x].grid[1:-1, 1:-1]), 1)
            else:
                row = np.concatenate((row, gen_grid[y][x].grid[1:-1, 1:-1]), 1)
        if y == 0:
            rv = row
        else:
            rv = np.concatenate((rv, row), 0)
    return rv


def create_tiles(inpt):
    '''
    Creates a list of tile objects from the input

    Input: 
        inpt (lst of strs): the input in strings

    Output: the list of tile objects
    '''
    tile_lst = []
    for tile in inpt:
        lst = tile.split("\n")
        id_num = lst[0][-5:-1]
        new_arr = []
        for line in lst[1:]:
            new_row = []
            for elt in line:
                if elt == "#":
                    new_row.append(1)
                elif elt == ".":
                    new_row.append(0)
            new_arr.append(new_row)
        arr = np.array(new_arr)
        tile_lst.append(Tile(arr, id_num))
    return tile_lst


def is_sea_creature(subgrid):
    '''
    Sees if an selection of the grid contains a sea creature. Credit to Borja 
        Sotomayor for the idea of using the local coordinates.

    Input: 
        Subgrid (np.array): an array thats a subset of the full grid:

    Output: A boolean giving whether the subgrid contains a sea creature.
    '''
    for y, x in SEA_CREATURE_COORDS:
        if subgrid[y, x] == 0:
            return False
    return True


def task2 (grid, remaining_tiles):
    '''
    Finds the total number of "#" in the grid once removing sea creatures

    Inputs:
        grid (lst of lsts): An list of tile objects
        remaining tiles (lst): A list tile objects that haven't been placed yet

    Outputs: An integer, denoting the number of "#" in the grid once sea 
        creatures are removed 
    '''
    grid = create_grid(grid, remaining_tiles)
    stitched_grid = stitch_grid(grid)
    total_octathorps = np.sum(stitched_grid)
    n = len(stitched_grid)-1
    for i in range(2):
        for j in range(4):
            num_sea_creature = 0
            for y in range(n - 3):
                for x in range(n-20):
                    if is_sea_creature(stitched_grid[y:y+3, x:x+20]):
                        num_sea_creature += 1
            if num_sea_creature > 0:
                return total_octathorps - (num_sea_creature * 15)
            stitched_grid = np.rot90(stitched_grid)
        stitched_grid = np.fliplr(stitched_grid)
    return total_octathorps




if __name__ == "__main__":
    tst = util.read_strs("inputs/day20_test.txt", sep = "\n\n")
    inpt = util.read_strs("inputs/day20_input.txt", sep = "\n\n")
    tst_tiles = create_tiles(tst)
    tst_sqr = len(tst_tiles)**.5
    inpt_tiles = create_tiles(inpt)
    len_sqr = len(inpt_tiles)**.5

    print("TASK 1")
    util.call_and_print(task1, tst_tiles)
    util.call_and_print(task1, inpt_tiles)

    full_grid = []
    for i in range(int(len_sqr)):
        full_grid.append([None] * int(len_sqr))
    tst_grid = []
    for i in range(int(tst_sqr)):
        tst_grid.append([None] * int(tst_sqr))
    tst_tiles[1].mirror_tile()
    tst_tiles[1].rotate_tile()
    tst_tiles[1].rotate_tile()
    tst_grid[0][0] = tst_tiles[1]
    tst_tiles.pop(1)


    starting_tile = None
    for i, tile in enumerate(inpt_tiles):
        if tile.id == "2711":
            starting_tile = tile
            break
    starting_tile.mirror_tile()
    full_grid[0][0] = starting_tile
    inpt_tiles.pop(i)
    
    print("\nTASK 2")
    util.call_and_print(task2, tst_grid, tst_tiles)
    util.call_and_print(task2, full_grid, inpt_tiles)

    

    

