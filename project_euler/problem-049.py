"""
Prime permutations
Problem 49
Published on 01 August 2003 at 06:00 pm [Server Time]
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, 
is unusual in two ways: (i) each of the three terms are prime, and, (ii) each of the 4-digit 
numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
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


def are_permutes(num1, num2, num3):
    num_set1, num_set2, num_set3 = set(list(str(num1))), set(list(str(num2))), set(list(str(num3)))
    return num_set1 == num_set2 == num_set3


primes = primes_eratosthenes(10000)

for low_num in range(1000, 10000):
    if low_num in primes:
        for mid_num in range(low_num + 2, 10000):
            if mid_num % 2 != 0 and mid_num % 3 != 0 and mid_num % 5 != 0 and mid_num in primes:
                high_num = mid_num + (mid_num - low_num)
                if high_num in primes:
                    if are_permutes(low_num, mid_num, high_num):
                        print "*******************************************************"
                        print(low_num, mid_num, high_num)
                        print str(low_num) + str(mid_num) + str(high_num)


#296962999629
