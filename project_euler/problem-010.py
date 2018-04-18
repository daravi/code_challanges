"""
Summation of primes:
Problem 10
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

def is_prime(number, primes_before):
    for prime in primes_before:
        if number % prime == 0:
            return False
    return True

def sum_primes(goal):
    primes = [2,3,5]
    for number in range(6, goal, 6):
        if is_prime(number + 1, primes):
            primes.append(number + 1)
        if is_prime(number + 5, primes):
            primes.append(number + 5)
    if range(6, goal, 6)[-1] + 5 > goal:
        primes.pop()
    return sum(primes)

def sum_primes2(goal):
    primes = [2]
    for number in range(3, goal):
        if is_prime(number, primes):
            primes.append(number)
    return sum(primes)


def sum_primes3(goal):
    nums = []
    for num in range(2, goal):
        nums.append(num)
    for idx in range(0,len(nums), 2):
        nums.pop(idx/2)
    for idx in range(0,len(nums), 3):
        print idx/3 * 2
        nums.pop(idx/3 * 2)
    return 'done'

def primes_eratosthenes(goal): # append vs list comprehension? is there a difference in speed?
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

#print sum_primes(100000)
#print sum_primes3(2000000)
print sum(primes_eratosthenes(2000000))
