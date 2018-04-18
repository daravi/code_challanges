# -*- coding: utf-8 -*-
"""
Largest product in a grid:
Problem 11
Refer to 20×20 grid from the data file: problem-011-data.txt

What is the greatest product of four adjacent numbers in the same direction 
(up, down, left, right, or diagonally) in the 20×20 grid?
"""

import os
os.system('clear')

path = '/Users/daravi/Google Drive/1 Academic/3 Other/Project Euler/problem-011-data.txt'

def read_int_grid_data(path):
    
    with open(path) as f:
        string_grid_data = [i.split() for i in f.readlines()]
    
    int_grid_data = string_grid_data # Temporary initialization to give integer list the same size
    
    for row in range(len(string_grid_data)):
        for col in range(len(string_grid_data[row])):
            int_grid_data[row][col] = int(string_grid_data[row][col])
    
    return int_grid_data
    

adj_len = 4

def find_max_mult(path, adj_len):
    
    data = read_int_grid_data(path)

    weights = [-1, 1, 0]
    direction_list = [[dir1, dir2] for dir1 in weights for dir2 in weights]
    direction_list.pop()

    max_mult = float("-inf")

    for row_start in range(len(data)):
        for col_start in range(len(data[row_start])):
            for direction in direction_list:
                mult = 1
                row = row_start
                col = col_start
                for _ in range(adj_len):
                    if 0 <= row < len(data) and 0 <= col < len(data[row]):
                        mult *= data[row][col]
                    else:
                        mult = None
                        break
                    row += direction[0]
                    col += direction[1]
        
                if mult > max_mult:
                    max_mult = mult

    return max_mult

print find_max_mult(path, adj_len)

# create read_int_grid_data module






