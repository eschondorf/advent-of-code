'''
Day 12
https://adventofcode.com/2020/day/12
'''
import util
import math

class Waypoint:
    '''
    A class for the waypoint
    '''
    def __init__(self):
        self.x = 10
        self.y = 1
        self.ship = None
    
    def move_waypoint(self, direction, steps):
        if direction == "N":
            self.y += steps
        elif direction == "S":
            self.y += -steps
        elif direction == "E":
            self.x += steps
        elif direction == "W":
            self.x += -steps

    def rotate_waypoint(self, angle):
        angle = math.radians(angle)
        a, b = self.ship.x, self.ship.y
        x, y = self.x, self.y
        x_prime, y_prime = x - a, y - b
        x_prime_rot = x_prime * math.cos(angle) - y_prime * math.sin(angle)
        y_prime_rot = x_prime * math.sin(angle) + y_prime * math.cos(angle)
        self.x = x_prime_rot + a
        self.y = y_prime_rot + b


class Ship:  
    '''
    A class for the ship
    '''
    def __init__(self):  
        self.x = 0
        self.y = 0
        self.rot = 0
        self.waypoint = None

    def move_forward(self, steps):
        x_change = steps * math.cos(self.rot)
        y_change = steps * math.sin(self.rot)
        self.x += x_change
        self.y += y_change
    
    def rotate(self, angle):
        self.rot += math.radians(angle)
    
    def get_manhat_dist(self):
        return abs(self.x) + abs(self.y)

    def move_to_waypoint(self):
        x, y = self.waypoint.x, self.waypoint.y
        a, b = self.x, self.y
        self.waypoint.x = 2*x - a
        self.waypoint.y = 2*y - b
        self.x = x
        self.y = y



def task1(inpt):
    '''
    Moves the ship and finds the Manhattan distance according to task 1 rules

    Input:
        - inpt (lst of strs): the list of directions for the ship
    
    Output: a float representing the final Manhattan distance of the ship from 
        the starting point
    '''
    ship = Ship()
    i = 0
    for line in inpt:
        direction = line[0]
        step = int(line[1:])
        if direction == "N":
            ship.y += step
        elif direction == "S":
            ship.y += -step
        elif direction == "E":
            ship.x += step
        elif direction == "W":
            ship.x += -step
        elif direction == "F":
            ship.move_forward(step)
        elif direction == "L":
            ship.rotate(step)
        elif direction == "R":
            ship.rotate(-step)
        else:
            print('ERROR')        
    return ship.get_manhat_dist()


def task2(inpt):
    '''
    Moves the ship and waypoint to finds the Manhattan distance according to 
        task 2 rules

    Input:
        - inpt (lst of strs): the list of directions for the ship and waypoint
    
    Output: a float representing the final Manhattan distance of the ship from 
        the starting point
    '''
    ship = Ship()
    wp = Waypoint()
    ship.waypoint = wp
    wp.ship = ship
    j = 0
    for line in inpt:
        j += 1
        direction = line[0]
        steps = int(line[1:])
        if direction == 'F':
            for i in range(steps):
                ship.move_to_waypoint()
        elif direction == 'L' or direction == 'R':
            if direction == 'R':
                steps = -steps
            wp.rotate_waypoint(steps)
        elif direction in ['N', 'S', 'E', 'W']:
            wp.move_waypoint(direction, steps)
        else:
            print("ERROR")
    return ship.get_manhat_dist()




if __name__ == "__main__":
    tst = util.read_strs('inputs/day12_test.txt')
    inpt = util.read_strs('inputs/day12_input.txt')
    
    print('TASK 1')
    util.call_and_print(task1, tst)
    util.call_and_print(task1, inpt)

    print('\nTASK2')
    util.call_and_print(task2, tst)
    util.call_and_print(task2, inpt)