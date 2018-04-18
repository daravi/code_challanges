# -*- coding: utf-8 -*-
"""
Names scores:
Problem 22
Using names.txt (right click and 'Save Link/Target As...') refere to problem-022-data.txt, 
a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, multiply this value by its 
alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 
3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
"""

import os
os.system('clear')

path = '/Users/daravi/Google Drive/1 Academic/3 Other/Project Euler/problem-022-data.txt'

def read_name_data(path):
    
    with open(path) as data_text:
        name_data = [line.split(',') for line in data_text.readlines()]
    #int_grid_data = name_data # Temporary initialization to give integer list the same size
    #
    #for row in range(len(name_data)):
    #    for col in range(len(name_data[row])):
    #        int_grid_data[row][col] = int(name_data[row][col])
    name_data = [name[1:-1] for name in name_data[0]]
    return name_data
    
names = (sorted(read_name_data(path)))
name_score_sum = 0

for name_position in range(len(names)):
    name_value = 0
    for char in names[name_position]:
        name_value += ord(char) - 64
        #print char
    name_score = (name_position + 1) * name_value
    name_score_sum += name_score

print name_score_sum
        

