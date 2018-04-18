# -*- coding: utf-8 -*-
"""
Longest Collatz sequence:
Problem 14
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
"""

def get_chain(number):
    chain = [number]
    while not number == 1:
        if number % 2 == 0:
            number /= 2
        else:
            number = 3 * number + 1
        chain.append(number)
    return chain

def get_max_chain_length(goal):
    max_chain_length = 0
    max_number = 0
    for number in range(goal // 2, goal):
        chain = get_chain(number)
        if len(chain) > max_chain_length:
            max_chain_length = len(chain)
            max_number = number
    return (max_number, max_chain_length)

print get_max_chain_length(1000000)









