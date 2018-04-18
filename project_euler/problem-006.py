# -*- coding: utf-8 -*-
"""
Problem 6
Sum square difference
The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers
and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural 
numbers and the square of the sum.
"""

def sum_of_squares(upper):
    sum_of_squares = 0
    for num in range(1, upper + 1):
        sum_of_squares += num * num
    return sum_of_squares

def square_of_sum(upper):
    num_sum = 0
    for num in range(1, upper + 1):
        num_sum += num
    return num_sum * num_sum

print square_of_sum(100) - sum_of_squares(100)