"""
We shall say that an n-digit number is pandigital if it makes use of all the digits
1 to n exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand,
multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be
written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include
it once in your sum.
"""
import string

from itertools import imap, permutations


digits = string.digits.replace('0', '')


# This isn't pretty, but whatever
def go():
    products = set()

    for d in imap(lambda x: ''.join(x), permutations(digits, 9)):
        dlen = len(d)

        for i in xrange(1, 6):
            start = int(d[:i])

            for j in xrange(1, 6):
                if i + j + 1 >= dlen:
                    break

                end = int(d[i:i+j+1])
                prod = int(d[i+j+1:])

                if start * end == prod:
                    products.add(prod)

    return products

print sum(go())
