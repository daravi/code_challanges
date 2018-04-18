# -*- coding: utf-8 -*-
"""
Problem 4
Largest palindrome product
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

import math

def is_palindromic(num):
    num_list = list(str(num))
    while len(num_list) > 1:
        if num_list[0] == num_list[-1]:
            #print "before pop:  "
            #print num_list
            num_list.pop()
            num_list.pop(0)
            #print "\n after pop:"
            #print num_list
            #print "\n\n"
        else:
            return False
    return True

lower = 100*100
upper = 999*999

max_pal = 0
factors = (0, 0)

for num in range (lower, upper):
    if is_palindromic(num):
        up = int(math.sqrt(num)) + 1
        for factor in range(100, up):
            if num % factor == 0:
                if num / factor <= 999:
                    max_pal = num
                    factors = (factor, num / factor)
                #else:
                 #   break
                
print max_pal
print factors