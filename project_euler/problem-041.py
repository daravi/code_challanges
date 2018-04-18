"""
Pandigital prime
Problem 41
We shall say that an n-digit number is pandigital if it makes use of all the 
digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

import itertools


def primes_eratosthenes(goal):
    nums = range(goal)
    for num in nums[2:]:
        if not num == 0:
            prime = num
            idx = 2 * prime
            while idx < goal:
                nums[idx] = 0
                idx += prime
    primes = [prime for prime in nums[2:] if not prime == 0]
    return primes


primes = primes_eratosthenes(10000)


def is_prime(permutation):
    global primes
    for prime in primes[4:]:
        if permutation % prime == 0:
            return False
    return True


max_prime_pandigital = 0

for digits in range(1,9):
    
    permutations = list(itertools.permutations(range(1,digits + 1)))
    
    for permutation in permutations:
        pandigital = int(''.join([str(digit) for digit in permutation]))
        if pandigital % 2 != 0 and pandigital % 3 != 0 and pandigital % 5 != 0 and pandigital % 7 != 0:
            if is_prime(pandigital):
                if pandigital > max_prime_pandigital:                    
                    max_prime_pandigital = pandigital
                
print max_prime_pandigital

#7652413

