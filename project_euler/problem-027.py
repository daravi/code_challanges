# -*- coding: utf-8 -*-
"""
Quadratic primes:
Problem 27
Euler discovered the remarkable quadratic formula:

n² + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. 
However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when 
n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes for the consecutive 
values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n² + an + b, where |a| < 1000 and |b| < 1000

where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4
Find the product of the coefficients, a and b, for the quadratic expression that produces the maximum 
number of primes for consecutive values of n, starting with n = 0.
"""

# what would happen if you started from anywhere?

import os
#import math

#os.system('clear')

def euler_quad((a, b), n):
    return (n * n + a * n + b)

def primes_eratosthenes(goal):
    nums = range(0, goal)
    for num in nums[2:]:
        if not num == 0:
            prime = num
            idx = 2 * prime
            while idx < goal:
                nums[idx] = 0
                idx += prime
    primes = [prime for prime in nums[2:] if not prime == 0]
    return primes


primes = primes_eratosthenes(1000)
print len(primes)

def bin_search(number, primes):
    idx, left, right = number / 10, 0, len(primes)
    for _ in range(log(len(primes))):
        if number > prime[idx]:
            idx = (idx + right) / 2
        elif number < prime[idx]: idx = (idx + right) / 2
        #else return True
    return False

def is_prime(number):
    global primes
    if number in primes:
        return True
    else:
        if primes[-1] < number < primes[-1] ** 2:
            for prime in primes:
                if number % prime == 0:
                    return False
            return True
        elif number > primes[-1] ** 2:
            errr = 0
            print 5 / errr
            return 'out of range'
    
    return False


def max_consecutive_primes(a_upper_limit, b_upper_limit):
    n_max,a_max, b_max = 0, 0, 0
    for a in range(-a_upper_limit + 1, a_upper_limit):
        for b in range(-b_upper_limit + 1, b_upper_limit):
            n = 0
            while is_prime(euler_quad((a, b), n)):
                n += 1
            if n > n_max: n_max, a_max, b_max = n, a, b
            print a,b
    return (n_max,a_max, b_max)

print max_consecutive_primes(1000, 1000)
# (71, -61, 971)
