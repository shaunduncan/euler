'''
Count the number of letters in spelled out numbers 1 to 1000

one
two
...
one hundred and forty-five

Exclude spaces/hyphens and use 'and' after hundreds
'''

words = {
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety'
}

total = 0


def make_word(num):
    if num in words:
        return words[num]
    elif num > 20 and num < 100:
        base = (num // 10) * 10
        return ''.join((words[base], words[num - base]))


for x in xrange(1, 1000):
    if x < 100:
        total += len(make_word(x))
    else:
        base = (x // 100)
        rem = x - (base * 100)
        parts = [words[base], 'hundred']
        if rem > 0:
            parts.extend(['and', make_word(rem)])
        total += len(''.join(parts))

print total + len('onethousand')
