# -*- coding: utf-8 -*-
"""
Amicable numbers:
Problem 21
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""


def get_divisors(number):
    divisors = set([1])
    divisor = 2
    while number > 1 and divisor <= number:
        if number % divisor == 0:
            number /= divisor
            append_set = set([element * divisor for element in divisors])
            divisors |= append_set
        else:
            divisor += 1
    divisors.remove(max(divisors))
    return divisors


def is_amicable(first_number):
    second_number = sum(get_divisors(first_number))
    if second_number == first_number:
        return False
    third_number = sum(get_divisors(second_number))
    return first_number == third_number


def get_amicable_sum(number_range):
    amicable_sum = 0
    for number in range(1, number_range):
        if is_amicable(number):
            amicable_sum += number
    return amicable_sum


print get_amicable_sum(10000)
