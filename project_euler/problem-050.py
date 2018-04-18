"""
Consecutive prime sum:
Problem 50
Published on 15 August 2003 at 06:00 pm [Server Time]
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
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

goal = 1000000

primes = primes_eratosthenes(goal)
max_len, max_summa = 0, 0
#print primes[2000:2500]
for idx in range(2500):#range(len(primes)):
    summa = 0
    for i in range(idx, len(primes)):
        summa += primes[i]
        if summa > goal: 
            #end = True
            break
        if summa % 2 != 0 and summa % 3 != 0 and summa % 5 != 0 and summa % 7 != 0 and summa in primes:
            if i - idx > max_len:
                max_len = i- idx
                max_summa = summa
                print summa
    #if end: break

#print max_summa, max_len