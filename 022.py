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
