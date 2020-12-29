'''
Day 24
https://adventofcode.com/2020/day/24
'''
import util

def task1 (tiles):
    '''
    Finds the number of black tiles after initial flips

    Inputs:
        - tiles (lst of strs): list of directions to tiles to be fliped

    Outputs: 
        - num_black (int): number of black tiles
        - black_tiles (lst): list of black tile coordinates
        - d (dict): dictonary mapping tile coordinates to number of flips
    '''
    d = {}
    num_black = 0
    for tile in tiles:
        d = flip_tile(d, tile)
    black_tiles = []
    for key, value in d.items():
        if value%2 == 1:
            num_black += 1
            black_tiles.append(key)
    return num_black, black_tiles, d

def flip_tile(d, tile):
    '''
    Given a set of directions flips that tile and updates the tile dictionary

    Inputs:
        - d (dict): dictonary mapping tile coordinates to number of flips
        - tile (str): a string containing directions to a tile
    
    Outputs: an updated tile dictionary
    '''
    e, se, sw, w, nw, ne = 0, 0, 0, 0, 0, 0
    i = 0
    while i < len(tile):
        if tile[i] == "e":
            e += 1
        elif tile[i] == "w":
            w += 1
        elif tile[i] == "n":
            if tile[i+1] == "e":
                ne += 1
                i += 1
            elif tile[i+1] == "w":
                nw += 1
                i += 1
            else:
                print("ERROR")
        elif tile[i] == "s":
            if tile[i+1] == "e":
                se += 1
                i += 1
            elif tile[i+1] == "w":
                sw += 1
                i += 1
            else:
                print("ERROR")
        else:
            print("ERROR")
        i += 1
    tile_coord = [ne - sw, nw - se, e-w]
    x = tile_coord[0] + tile_coord[2]
    y = tile_coord[1] - tile_coord[2]
    z = -tile_coord[0] - tile_coord[1]
    assert(x + y + z == 0)
    
    tile_coord_xyz = (x, y, z)
    flip = d.get(tile_coord_xyz, 0)
    d[tile_coord_xyz] = flip +  1
    return d


def find_black_tiles(tile_dict):
    '''
    Helper function for task 2, finds all tiles currently black

    Inputs:
        - tile_dict (dict): dictonary mapping tile coordinates to number of 
            flips
    
    Outputs:
        - num_black (int): current number of black tiles
        - black_tiles (lst): list of cooridnates of black tile locations
    '''
    black_tiles = []
    num_black = 0
    for key, value in tile_dict.items():
        if value%2 == 1:
            num_black += 1
            black_tiles.append(key)
    return num_black, black_tiles


def one_day(tile_dict):
    '''
    Helper function for task 2, simulates one day

    Inputs:
        - tile_dict (dict): dictonary mapping tile coordinates to number of 
            flips
    
    Outputs: tile_dict (dict): dictonary mapping tile coordinates to number of 
        flips
    '''
    _, black_tiles = find_black_tiles(tile_dict)
    tiles_to_flip = []
    adj_dict = {}
    for tile in black_tiles:
        num_black_adj = 0
        adj = generate_adjacent_coords(tile)
        adj_dict[tile] = adj
        for adj_tile in adj:
            if adj_tile in black_tiles:
                num_black_adj += 1
        if (num_black_adj == 0 or num_black_adj > 2):
            tiles_to_flip.append(tile)
    inv_adj_dict = {}
    for value in adj_dict.values():
        for elt in value:
            times_seen = inv_adj_dict.get(elt, 0)
            inv_adj_dict[elt] = times_seen + 1
    for key, value in inv_adj_dict.items():
        if (value == 2 and key not in black_tiles):
            tiles_to_flip.append(key)
    for tile in tiles_to_flip:
        flip = tile_dict.get(tile, 0)
        tile_dict[tile] = flip + 1
    return tile_dict


def generate_adjacent_coords(coord):
    '''
    Helper function for task 2, finds all tiles adjacent tile coordiantes

    Inputs:
        - coords (tuple of ints): contains the x, y, z coordinates of the tile
            for which we want the adjacent coordinates
    
    Outputs: adj (lst of tuples): list of adjacent tile coordinates
    '''
    adj = []
    x, y, z = coord
    adj.append((x, y-1, z+1))
    adj.append((x, y+1, z-1))
    adj.append((x-1, y, z+1))
    adj.append((x+1, y, z-1))
    adj.append((x-1, y+1, z))
    adj.append((x+1, y-1, z))
    return adj


def task2(tiles):
    '''
    Runs the simulation for 100 days and finds the number of black tiles at 
        the end
    
    Inputs: 
        - tiles (lst of strs): list of directions to tiles to be fliped initally
    
    Outputs: an int, number of black tiles at the end of the simulation
    '''
    _, _, tile_dict = task1(tiles)
    for i in range(1, 101):
        tile_dict = one_day(tile_dict)
        num_black, _ = find_black_tiles(tile_dict)
    num_black, _ = find_black_tiles(tile_dict)
    return num_black


if __name__ == "__main__":
    tst = util.read_strs('inputs/day24_test.txt')
    inpt = util.read_strs('inputs/day24_input.txt')

    print('TASK 1')
    util.call_and_print(task1, tst)
    util.call_and_print(task1, inpt)

    print('\nTASK 2')
    util.call_and_print(task2, tst)
    util.call_and_print(task2, inpt)