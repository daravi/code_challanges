"""
Counting Sundays:
Problem 19
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
"""

import os
#import math
os.system('clear')

days = dict.fromkeys(zip(range(1,13), [False]*12), 31)
days.update(dict.fromkeys(zip([4,6,9,11], [False]*4), 30))
days.update({(2, False): 28, (2, True): 29})

def get_first_day_sundays(date_start, date_end):
    year = date_start[0]
    month = date_start[1]
    day = date_start[2]
    first_day_sundays = 0
    while year < date_end[0] or (year == date_end[0] and month < date_end[1]) or (year == date_end[0] and month == date_end[1] and day < date_end[2]):
        # update_date # day += 7
        leap = False
        leap_fev = False
        if (year % 4 == 0 and not year % 100 == 0) or year % 400 == 0:
            leap = True
        if month == 2 and leap == True:
            leap_fev = True
        day += 7
        days_in_month = days[(month, leap_fev)]
        month += day // (days_in_month + 1)
        day = (day % (days_in_month + 1)) + (day // (days_in_month + 1))
        year += month // 13
        month = (month % 13) + (month // 13)
        
        if day == 1:
            first_day_sundays += 1        
        
    return first_day_sundays


print get_first_day_sundays((1901,1,6), (2000,12,31))












