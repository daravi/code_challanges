"""
Self powers:
Problem 48
Published on 18 July 2003 at 06:00 pm [Server Time]
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

last_ten = [1] * 1000
for num in range(1, 1001):
    for _power in range(num):
        last_ten[num - 1] *= num
        last_ten[num - 1] %= 10 ** 10

print sum(last_ten) % (10 ** 10)

#9110846700
