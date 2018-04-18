"""
Reciprocal cycles:
Problem 26
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""
import os
import math

os.system('clear')

def get_longest_cycle(upper_limit, numerator = 1):
    longest_cycle_divisor, cycle_lenth_max = 1, 0
    quotients_max_cycle = []
    for divisor in range(1, upper_limit):
        dividend = numerator
        remainders, quotients = [], []
        while dividend % divisor not in remainders: # can you avoid using remainders and only use quotients?
            if dividend >= divisor:
                dividend, quotient = dividend % divisor, dividend // divisor
                remainders.append(dividend)
                quotients.append(quotient)
            dividend *= 10 ** (int(math.log10(divisor)) + 1)
        if dividend == 0:
            cycle_lenth = 0
        else:
            cycle_lenth = len(remainders[(remainders.index(dividend % divisor)):])
        if cycle_lenth > cycle_lenth_max:
            cycle_lenth_max = cycle_lenth
            longest_cycle_divisor = divisor
            quotients_max_cycle = quotients
    
    return (longest_cycle_divisor, cycle_lenth_max, quotients_max_cycle)

print get_longest_cycle(1000)[0]
# error: quotient does not include zeroes

