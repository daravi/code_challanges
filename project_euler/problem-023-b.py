"""
Non-abundant sums:
Problem 23
A perfect number is a number for which the sum of its proper divisors is exactly 
equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant 
if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as 
the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater 
than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced 
any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of 
two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

import os
#os.system('clear')

number_list = range(28124)

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


#def is_abundant(first_number):
#    second_number = sum(get_divisors(first_number))
#    return second_number > first_number


abundants_list = []
for number in range(1, 28124):
    if sum(get_divisors(number)) > number:
        print number
        abundants_list.append(number)
        idx = number * 2
        while idx < 28124:
            number_list[number] = 0
            idx += number


can_be_abundanted = []
for number in range(1, 28124):
    idx = 0
    while abundants_list[idx] <= number // 2:
        second_number = number - abundants_list[idx]
        if second_number in abundants_list:
            #can_be_abundanted.append(number)
            number_list[number] = 0
            print number
            break
        idx += 1

#print can_be_abundanted

#sum_result =0
#for number in range(1, 28123 + 1):
#    if not number in can_be_abundanted:
#        sum_result += number

print sum(number_list)
        
