"""
Maximum path sum I:
Problem 18
By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

[refere to projecteuler.net/problem=18]

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

[refere to problem-018-data.txt]


"""

import os
#os.system('clear')

path = '/Users/daravi/Google Drive/1 Academic/3 Other/Project Euler/problem-018-data.txt'

def read_int_data(path):
    with open(path) as f:
        string_data = [i.split() for i in f.readlines()]
    int_data = string_data # Temporary initialization to give integer list the same size
    
    for row in range(len(string_data)):
        for col in range(len(string_data[row])):
            int_data[row][col] = int(string_data[row][col])
    
    return int_data
    
data = read_int_data(path)

def get_max_path(data):
    max_path = data
    for row in range(len(data) - 2, -1, -1):
        for col in range(len(data[row])):
            max_path[row][col] += max(max_path[row + 1][col], max_path[row + 1][col + 1])
    return max_path[0][0]

print get_max_path(data)