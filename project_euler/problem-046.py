# -*- coding: utf-8 -*-
"""
Goldbach's other conjecture:
Problem 46
Published on 20 June 2003 at 06:00 pm [Server Time]
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
"""

import math


def primes_eratosthenes(goal):
    primes = []
    nums = range(goal)
    for num in nums[2:]:
        if nums[num] != 0:
            prime = num
            primes.append(prime)
            idx = 2 * prime
            while idx < goal:
                nums[idx] = 0
                idx += prime
    return primes, nums


def is_twice_squared(number):
    return (math.sqrt(number / 2.0)).is_integer()

def get_first_non_goldback(goal):
    primes, nums = primes_eratosthenes(goal)
    for number in range(2, goal):
        print number
        if number % 2 != 0 and nums[number] == 0:
            not_goldbach = True
            #if number % 2 == 0:
            #    if is_twice_squared(number - 2):
            #        not_goldbach = False
            #        print 'hey'
            #else:
            idx = 1
            while primes[idx] < number:
                if is_twice_squared(number - primes[idx]):
                    not_goldbach = False
                    break
                idx += 1
            if not_goldbach: break
    return number
            
print get_first_non_goldback(10000)
