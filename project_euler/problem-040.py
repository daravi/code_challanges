# -*- coding: utf-8 -*-
"""
Champernowne's constant:
Problem 40
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

#9        * 1       - 9            => 10                ||  r = 1           0     2digit passed     e:1     d1
#90       * 2       - 189          => 100               ||  r = 11          3     3digit passed     e:4     d2
#900      * 3       - 2889         => 1000              ||  r = 111         27    4digit passed     e:28    d3
#9000     * 4       - 38889        => 10000             ||  r = 1111        222   5digit passed     e:223   d1
#90000    * 5       - 488889       => 100000            ||  r = 11111       

running_product = 1

for i in range(1, 6):
    digits_passed = int(str(i - 1) + '8' * (i - 1) + '9')
    remaining_digits = 10 ** (i + 1) - digits_passed
    base = 10 ** i - 1
    while remaining_digits > 0:
        remaining_digits -= (i + 1)
        base += 1
    d = int(str(base)[remaining_digits - 1])
    running_product *= d

print running_product