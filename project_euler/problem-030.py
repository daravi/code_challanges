"""
Digit fifth powers:
Problem 30
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4
As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

i = 2
summ = 0

dic = { '0': 0, '1': 1, '2': 32, '3': 243, '4': 1024, '5': 3125, '6': 7776, '7': 16807, '8': 32768, '9':59049}
print dict

while 1:
    su = 0
    st = str(i)
    for di in st:
        su += dic[di]
    if su == i:
        
        print i
    i += 1
