"""
Large sum:
Problem 13
Work out the first ten digits of the sum of the one-hundred 50-digit numbers.
Refer to file: problem-013-data.txt
"""

import os
#os.system('clear')

path = '/Users/daravi/Google Drive/1 Academic/3 Other/Project Euler/problem-013-data.txt'

def read_int_grid_data(path):
    with open(path) as f:
        string_data = [i.split() for i in f.readlines()]
    #print string_data[0]
    int_data = []
    
    for row in string_data:
        digit_row = [int(digit) for digit in row[0]]
        #print digit_row
        #digit_row = map(int, list(row))
        int_data.append(digit_row)
    
    return int_data
    
data = read_int_grid_data(path)

def sum_large(length):
    sum_list = [0] * length
    dig_sum = 0
    for digit in range(1, length + 1):
        for row in data:
            dig_sum += row[-(digit)]
        sum_list[length - digit] = dig_sum % 10
        dig_sum //= 10
    
    sum_num = ''
    for number in sum_list:
        sum_num += str(number)
    
    return str(dig_sum) + sum_num

print sum_large(50)
#9831892672
#5537376230
