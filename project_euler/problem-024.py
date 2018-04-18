"""
Lexicographic permutations:
Problem 24
A permutation is an ordered arrangement of objects. For example, 3124 is one possible 
permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically 
or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
import os
os.system('clear')

counter = 0

def get_permutations(objects, start = 0):
    global counter
    
    permutations = []
    objects_copy = list(objects)
    
    if start == len(objects_copy) - 1: 
        permutations.append(tuple(objects_copy))
        counter += 1
    else:
        for swapper_position in range(start, len(objects_copy)):
            objects_copy[start], objects_copy[swapper_position] = objects_copy[swapper_position], objects_copy[start]
            permutations += get_permutations(objects_copy, start + 1)
            if counter == 1000000:
                break
        
    return permutations

permutation = get_permutations(range(10))[-1]
print ''.join([str(digit) for digit in permutation])