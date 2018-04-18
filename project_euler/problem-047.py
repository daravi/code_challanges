# -*- coding: utf-8 -*-
"""
Distinct primes factors:
Problem 47
Published on 04 July 2003 at 06:00 pm [Server Time]
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors. What is the first of these numbers?
"""

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
    return primes


primes_list = primes_eratosthenes(1000)

def factorize(number):
    global primes_list
    factorized_number = []
    for prime in primes_list:
        if not number % prime:
            power = 0
            while number % prime == 0: 
                number /= prime
                power += 1
            factorized_number.append((prime, power))
        if number == 1: break
                  
    return factorized_number


def are_distinct(factorized1, factorized2):
    if len(factorized1) > len(factorized2):
        factorized_bigger = factorized1
        factorized_smaller = factorized2
    else:
        factorized_bigger = factorized2
        factorized_smaller = factorized1
    
    for idx in range(len(factorized_bigger)):
        if factorized_bigger[idx] in factorized_smaller:
            return False
    return True


num = [factorize(2), factorize(3), factorize(4), 0]
pointer = 0

while True:
    num[(pointer + 3) % 4] = factorize(pointer + 5)
    idx = [pointer % 4, (pointer + 1) % 4, (pointer + 2) % 4, (pointer + 3) % 4]
    if 4 == len(num[idx[0]]) == len(num[idx[1]]) == len(num[idx[2]]) == len(num[idx[3]]):
        if (are_distinct(num[idx[0]], num[idx[1]]) and 
            are_distinct(num[idx[1]], num[idx[2]]) and 
            are_distinct(num[idx[2]], num[idx[3]])):
            break
    pointer += 1

first = 1
for factor in num[idx[0]]: first *= factor[0] ** factor[1]
print first


