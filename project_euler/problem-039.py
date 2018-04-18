# -*- coding: utf-8 -*-
"""
Integer right triangles:
Problem 39
If p is the perimeter of a right angle triangle with integral length 
sides (integer numbers) {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
"""

# a = P(P﹣2b)/[2(P﹣b)]

import math

max_num_sols = float("-inf")
num_sols = [0] * 1000
p_solutions = [[i] for i in range(1000)]
#print p_solutions

for p in range (12, 1000):
    for a in range(1, p // 2):
        b = p * (p - 2.0 * a) / (2.0 * (p - a))
        if b.is_integer():
            c = math.sqrt(a ** 2 + b ** 2)
            if c.is_integer():
                p_solutions[p].append((a, b, c))
    num_sols[p] = len(p_solutions[p])
    if num_sols[p] > max_num_sols:
        max_num_sols = num_sols[p]
        result = p

print result

    