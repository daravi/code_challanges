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

#number_list = range(28124)
#
#def get_divisors(number):
#    divisors = set([1])
#    divisor = 2
#    while number > 1 and divisor <= number:
#        if number % divisor == 0:
#            number /= divisor
#            append_set = set([element * divisor for element in divisors])
#            divisors |= append_set
#        else:
#            divisor += 1
#    divisors.remove(max(divisors))
#    return divisors
#
#
##def is_abundant(first_number):
##    second_number = sum(get_divisors(first_number))
##    return second_number > first_number
#
#
#abundants_list = []
#for number in range(1, 28124):
#    if sum(get_divisors(number)) > number:
#        print number
#        abundants_list.append(number)
#
#
#
#can_be_abundanted = []
#for number in range(1, 28124):
#    idx = 0
#    while abundants_list[idx] <= number // 2:
#        second_number = number - abundants_list[idx]
#        if second_number in abundants_list:
#            #can_be_abundanted.append(number)
#            number_list[number] = 0
#            print number
#            break
#        idx += 1
#
##print can_be_abundanted
#
##sum_result =0
##for number in range(1, 28123 + 1):
##    if not number in can_be_abundanted:
##        sum_result += number
#
#print sum(number_list)
#
#def is_abundant(number):
#    is_abundant = False
#    return is_abundant
#
#
#def is_sum_of_abundants(number):
#    is_sum_of_abundants = False
#    return is_sum_of_abundants
#
#
#def get_sum_of_abundants(upper_limit):
#    sum_of_abundants = [False] * upper_limit
#    
#    for number in range(1, upper_limit + 1):
#        if not sum_of_abundants[number] and is_sum_of_abundants(number):
#            sum_of_abundants[number] = True
#            idx = 2 * number
#            while idx < goal:
#                nums[idx] = 0
#                idx += prime
#            
#    sum_of_abundants = []    
#    return sum_of_abundants
#    
#
#find first abundant number
#cross all its multiples below goal [set sum_abundants[multiple] to True]
#find next abundant or sum_abundant number not crossed num2
#for all previously crossed numbers i cross all num2 + i * j with j's limit such that num2 + i * j <= goal.'
#
#

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


def is_abundant(first_number):
    second_number = sum(get_divisors(first_number))
    return second_number > first_number


def get_sum_abundant(abundants_list, upper_limit):
    sum_abundant = [False] * (upper_limit + 1)
    sieve = []
    
    for number in range(1, upper_limit + 1):
        if number in abundants_list and not sum_abundant[number]: #or is_sum_abundant(number):
            #if is_sum_abundant(number):
            #   idx = number
            #else:
            sieve.append(number)
            for hole in sieve:
                idx = number + hole
                while idx < upper_limit:
                    sum_abundant[idx] = True
                    idx += hole

    #not_sum_abundant = []
    #for number in range(1, upper_limit + 1):
    #    if sum_abundant [number] == False: #and not is_sum_abundant(number):
    #        not_sum_abundant.append(number)
    return sum_abundant

    
def get_abundants_list(upper_limit):
    abundants_list = []
    for number in range(1, upper_limit + 1):
        if sum(get_divisors(number)) > number:
            abundants_list.append(number)
    return abundants_list

def get_non_sum_abundants(upper_limit):
    abundants_list = get_abundants_list(upper_limit)
    sum_abundant = get_sum_abundant(abundants_list, upper_limit) #All True ARE True but all False ARE NOT necessarily False
    print sum_abundant
    for number in range(1, upper_limit):
        if not sum_abundant[number]:
            idx = 0
            while abundants_list[idx] <= number // 2:
                second_number = number - abundants_list[idx]
                if second_number in abundants_list:
                    #can_be_abundanted.append(number)
                    sum_abundant[number] = True
                    print number
                    break
                idx += 1        
    
    not_sum_abundant = []
    for number in range(1, upper_limit + 1):
        if sum_abundant [number] == False: #and not is_sum_abundant(number):
            not_sum_abundant.append(number)
    return not_sum_abundant

print sum(get_non_sum_abundants(28123))
#4179871