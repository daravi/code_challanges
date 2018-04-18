"""
Problem 1
Multiples of 3 and 5
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.
"""

num_sum = 0

fib = [0, 1]
i = 1
sumnum = 0

while fib[i] <= 4000000:
    #print fib[i]
    fib.append(fib[i] + fib[i-1])
    if fib[i+1] % 2 == 0:
        sumnum += fib[i+1]
        #print "hey" + str(fib[i+1])
    i += 1
    print fib[i]

print sumnum
    