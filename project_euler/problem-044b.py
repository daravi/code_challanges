# -*- coding: utf-8 -*-
"""
Pentagon numbers
Problem 44
Pentagonal numbers are generated by the formula, Pn=n(3n−1)/2. 
The first ten pentagonal numbers are:

1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8. 
However, their difference, 70 − 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk, for which their sum and 
difference are pentagonal and D = |Pk − Pj| is minimised; what is the value of D?
"""

import math

def get_pentagonals(goal):
    pentagonals, pentagonal, diff = [1], 1, 1
    for n in range(1, goal):
        diff += 3
        pentagonal += diff
        pentagonals.append(pentagonal)
    
    return pentagonals
    #return [n * (3 * n - 1) / 2 for n in range(1, goal)]


def is_pentagonal(number):
    return ((1 + math.sqrt(1 + 24 * number)) / 6.0).is_integer()


def get_pentagonal_diffsum_min(goal):
    pentagonals = get_pentagonals(goal)
    pentagonal_diffsum, pentagonal_diffsum_min = [], float("inf")
    
    for i in range(1, goal):
        for j in range (i - 1):
            pentagonal_diff = (pentagonals[i] - pentagonals[j])
            if is_pentagonal(pentagonal_diff):
                #print "hey1", pentagonals[i], pentagonals[j]
                if is_pentagonal(pentagonals[i] + pentagonals[j]):
                    #print "hey2", pentagonals[i], pentagonals[j]
                    pentagonal_diffsum.append((j, i))
                    if pentagonal_diff < pentagonal_diffsum_min:
                        pentagonal_diffsum_min = pentagonal_diff
                        
    return pentagonal_diffsum_min

print get_pentagonal_diffsum_min(10001)