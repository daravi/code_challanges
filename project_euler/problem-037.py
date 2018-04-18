"""
Truncatable primes:
Problem 37
The number 3797 has an interesting property. Being prime itself, 
it is possible to continuously remove digits from left to right, 
and remain prime at each stage: 3797, 797, 97, and 7. 
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable 
from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

def primes_erat(goal):
    nums = range(0, goal)
    for num in nums[2:]:
        if not num == None:
            prime = num
            idx = 2 * prime
            while idx < goal:
                nums[idx] = None
                idx += prime
    primes = [prime for prime in nums[2:] if not prime == None]
    return primes

goal = 1000000
primes = primes_erat(goal)

def is_truncable(number):
    str_number = str(number)
    for ch in range(len(str_number)):
        if not (int(str_number[ch:]) in primes):
            return False
        if not (int(str_number[0:ch + 1]) in primes):
            return False
    return True

truncables = []
for num in primes_erat(goal):
    if is_truncable(num):
        truncables.append(num)
        
print sum(truncables[4:])

# 748317
