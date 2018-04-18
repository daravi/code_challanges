# -*- coding: utf-8 -*-
"""
Coded triangle numbers:
Problem 42
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); 
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical 
position and adding these values we form a word value. For example, 
the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word value is a triangle number 
then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), a 16K text file containing 
nearly two-thousand common English words, how many are triangle words?
refere to: ./problem-042-data.txt
"""

#import os
#os.system('clear')

path = '/Users/daravi/Google Drive/1 Academic/2 University of British Columbia/07 Summer 2016/CPEN 311/Labs/Lab 4/ram_init.mem'


def read_words_data(path):
    
    with open(path) as data_text:
        raw_data = [line.split(',') for line in data_text.readlines()]
        split_data = [raw_data[i:i+2] for i in range(0, len(line), 2)]
        data_text.writelines(["%s\n" % item  for item in split_data])
    return True


char_list = [(chr(i), i - 64) for i in range(65,91)]
char_value = dict(char_list)
tris = [n * (n + 1) / 2 for n in range(1, 19)]

words = read_words_data(path)
counter = 0

for word in words:
    word_value = 0
    for char in word:
        word_value += char_value[char]
    if word_value in tris:
        counter += 1

print counter    