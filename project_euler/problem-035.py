"""
Circular primes
Problem 35
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, 
are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

import math
import bisect

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


primes_total = primes_eratosthenes(1000000)
counter = 0

def bin_search(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect.bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return True
    return False

primes1 = primes_total[0:4]
primes2 = primes_total[4:25]
primes3 = primes_total[25:168]
primes4 = primes_total[168:1229]
primes5 = primes_total[1229:9592]
primes6 = primes_total[9592:78498]

primess1 = primes_total[0:4]
primess2 = primes_total[0:25]
primess3 = primes_total[0:168]
primess4 = primes_total[0:1229]
primess5 = primes_total[0:9592]
primess6 = primes_total[0:78498]

primes = [primes1, primes2, primes3, primes4, primes5, primes6]
primess = [primess1, primess2, primess3, primess4, primess5, primess6]

for i in range(6):
    for prime in primes[i]:
        order = int(math.log10(prime) + 1)
        circular_prime = True 
        for place in range(order):
            new_num = int(str(prime)[place:] + str(prime)[:place])
            if not bin_search(primess[i], new_num):
                circular_prime = False
                break
        if circular_prime:
            counter += 1
            print counter, prime
            #''.join([str(digit) for digit in permutation])
