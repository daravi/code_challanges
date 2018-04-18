"""
Double-base palindromes:
Problem 36
The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

def get_palin_sum():
    palin_sum = 1 + 3 + 5 + 7 + 9
    
    for i in range(1, 100):
        for mid in [''] + range(10):
            num_dec = int(str(i) + str(mid) + str(i)[::-1])
            num_bin = bin(num_dec)[2:]
            if str(num_bin)[:len(num_bin) / 2] == str(num_bin)[-1:-(len(num_bin) / 2 + 1):-1]: # if palindrome
                palin_sum += num_dec
                    
    for j in range(100, 1000):
        num_dec = int(str(j) + str(j)[::-1])
        num_bin = bin(num_dec)[2:]
        if str(num_bin)[:len(num_bin) / 2] == str(num_bin)[-1:-(len(num_bin) / 2 + 1):-1]: # if palindrome
            palin_sum += num_dec
    
    return palin_sum
                
print get_palin_sum()

#shorter way to check if palindrome: str(num) == str(num)[::-1]