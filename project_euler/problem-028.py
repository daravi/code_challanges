"""
Number spiral diagonals
Problem 28
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

'21 22 23 24 '25
20  '7  8  '9 10
19  6  '1  2 11
18  '5  4  '3 12
'17 16 15 14 '13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
"""

#1,3,5,7,9,13,17,21,25,31,37,43,50,57,65,73,81?
#
#1[1x1]2,2,2,2,[3x3]4,4,4,4[5x5],6,6,6,6,[7x7]8,8,8,8,[9x9]...

diagonal_sum = 1
number = 1
for i in range(1,501):
    diagonal_sum += 4 * number + 20 * i
    number += 8 * i

print diagonal_sum