# -*- coding: utf-8 -*-
"""
Pandigital products
Problem 32
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand, multiplier, 
and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
"""

import itertools

#1      2      3      4
#4      3      2      1 

permutations = list(itertools.permutations(range(1,10), 5))

product_sum = set([])

for permutation in permutations:
    
    for i in range(1, 5):
        multiplicand = 0
        for j in range(i):
            multiplicand *= 10
            multiplicand += permutation[j]
        multiplier = 0
        for k in range(i, 5):
            multiplier *= 10
            multiplier += permutation[k]
    
        product = multiplicand * multiplier        
        product_digit_list = [int(char) for char in str(product)]        
        digits_list = list(permutation) + product_digit_list
        
        if set(digits_list) == set(range(1,10)) and len(digits_list) == 9:
            #product_sum.add((multiplicand, multiplier, product))
            product_sum.add(product)
    
print sum(list(product_sum))