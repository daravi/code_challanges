"""
Sub-string divisibility:
Problem 43
The number, 1406357289, is a 0 to 9 pandigital number because it is made up of 
each of the digits 0 to 9 in some order, but it also has a rather interesting 
sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property.
"""

import itertools

primes = [2, 3, 5, 7, 11, 13, 17]
pandigitals_list = list(itertools.permutations(range(10)))
special_pandigital_sum = 0

for pandigital_list in pandigitals_list:
    pandigital = ''.join([str(digit) for digit in pandigital_list])
    is_special = True
    
    for digit in range(2,9):
        if int(pandigital[digit - 1 : digit + 2]) % primes[digit - 2] != 0:
            is_special = False
            break
    
    if is_special:
        if len(pandigital) == 10:
            special_pandigital_sum += int(pandigital)

print special_pandigital_sum