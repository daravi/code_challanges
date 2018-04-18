"""
Problem 3
Largest prime factor
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
num_unbroken = 600851475143
factors = []

num_broken = num_unbroken
factor = 2

while num_broken > 1:
    if num_broken % factor == 0:
        factors.append(factor)
        while num_broken % factor == 0:
            num_broken /= factor
    factor += 1
    
print factors[-1]