# -*- coding: utf-8 -*-
"""
Pandigital multiples
Problem 38
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. 
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, 
giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as the 
concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

def is_pandigital(number):
    return set(map(int, list(str(number)))) == set(range(1, 10))

def concatenated_product(multiplicand, multipliers):
    pass

def largest_cp_pandigital():
    cp_pandigital = []
    for number in range(10000):
        concat_prod, i = '', 1
        while len(concat_prod) < 9:
            concat_prod += str(number * i)
            i += 1
        if len(concat_prod) == 9 and is_pandigital(concat_prod):
            cp_pandigital.append(concat_prod)
        
    return max(cp_pandigital)
    
print largest_cp_pandigital()