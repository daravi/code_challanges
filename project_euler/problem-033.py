"""
Digit cancelling fractions
Problem 33
The fraction 49/98 is a curious fraction, as an inexperienced mathematician 
in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, 
is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, 
and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
"""

for i in range(10,100):
    for j in range(10,100):
        if i != j and not (i % 10 == 0 and j % 10 == 0) and i / j < 1:
            if i % 10 == j % 10:
                if float(i) / j == float(i // 10) / (j // 10):
                    print i,j
            elif i % 10 == j // 10 and j % 10 != 0:
                if float(i) / j == float(i // 10) / (j % 10):
                    print i,j
            elif i // 10 == j // 10 and j % 10 != 0:
                if float(i) / j == float(i % 10) / (j % 10):
                    print i,j
            elif i // 10 == j % 10:
                if float(i) / j == float(i % 10) / (j // 10):
                    print i,j
