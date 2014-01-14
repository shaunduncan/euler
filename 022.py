"""
Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand
first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for
each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth
3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of
938 × 53 = 49714.

What is the total of all the name scores in the file?
"""
import csv
import string

from collections import defaultdict

total_score = 0
letter_values = defaultdict(int)

# Get letter scores ONCE
for letter in string.letters:
    normalizer = 64 if letter in string.uppercase else 96
    letter_values[letter] = ord(letter) - normalizer

for names in csv.reader(open('./data/022/names.txt', 'r')):
    for pos, name in enumerate(sorted(names)):
        total_score += (pos + 1) * sum(letter_values[letter] for letter in name)

print total_score
