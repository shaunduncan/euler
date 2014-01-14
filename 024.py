"""
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation
of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
from itertools import imap, islice, permutations
from math import factorial


def fast():
    """
    The fast way. We do this by factorial trickery. Going in order we construct a list
    until we reach the 1,000,000th one. When is that? If we choose a number for the first
    spot, there are 9! choices remaining. So we choose the next item based on whether n!
    breaks over 1,000,000 or not, where n is the number of remaining items to choose from.
    """
    numitems = 10
    choices = range(10)
    end = 1000000
    total = 0
    result = []

    for i in xrange(numitems):
        for j, k in enumerate(sorted(choices)):
            fact = factorial(numitems - len(result) - 1)
            if total + fact < end:
                total += fact
                continue
            else:
                result.append(k)
                del choices[j]
                break

    return ''.join(map(str, result))


def slow():
    """
    The slow way. Iterate sorted integer permutations and islice the 1,000,000th one
    """
    end = 1000000
    makeint = lambda tup: int(''.join(map(str, tup)))
    return list(islice(sorted(imap(makeint, permutations(xrange(10), 10))), end+1, end+2))[0]


print fast()
