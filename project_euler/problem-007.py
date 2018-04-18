"""
10001st prime:
    
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, 
we can see that the 6th prime is 13.

What is the 10,001st prime number?
"""

def is_prime(number, primes_before):
    for prime in primes_before:
        if number % prime == 0:
            return False
    return True

def nth_prime_finder(goal):
    primes = []
    counter = len(primes)
    number = 2
    while not counter == goal:
        if is_prime(number, primes):
            primes.append(number)
            counter += 1
        number += 1
    return primes[goal - 1]
    
print nth_prime_finder(10001)