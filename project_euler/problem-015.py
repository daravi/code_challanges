# -*- coding: utf-8 -*-
"""
Lattice paths
Problem 15
Starting in the top left corner of a 2×2 grid, and only being able to move to 
the right and down, there are exactly 6 routes to the bottom right corner.
see: https://projecteuler.net/problem=15

How many such routes are there through a 20×20 grid?
"""

import os
import math
#os.system('clear')

def grid_ways(sides):
    x = math.factorial(sides)
    return math.factorial(2 * sides) / (x * x)


def grid_ways_rectangle(m, n):
    # Fm(n) = Fm-1(n) + Fm-1(n-1) + ... + Fm-1(1) + Fm-1(0)
    ways = 0
    if m > 1:
        for i in range(n + 1):
            ways += grid_ways_rectangle(m - 1, i)
    elif m == 1:
        ways = 1
    return ways
    

def grid_ways_recursive(sides):
    return grid_ways_rectangle(sides + 1, sides)

def grid_ways_rectangle_path(m, n):
    if m == 0 or n == 0:
        return 1
    return grid_ways_rectangle_path(m - 1, n) + grid_ways_rectangle_path(m, n - 1)

def grid_ways_recursive_path(sides):
    return grid_ways_rectangle_path(sides, sides)
    

def grid_ways_constructive(sides):
    ways_array = [[0] * (sides + 1)] * (sides + 1)
    
    for row in range(len(ways_array)):
        for col in range(len(ways_array[row])):
            if row == 0 or col == 0:
                ways_array[row][col] = 1
            else:
                ways_array[row][col] = ways_array[row - 1][col] + ways_array[row][col - 1]
            
    
    return ways_array[-1][-1]


#print grid_ways(3000)
#print grid_ways_recursive(10)
#print grid_ways_recursive_path(14)
#print grid_ways_constructive(3000)