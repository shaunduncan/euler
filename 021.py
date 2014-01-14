"""
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which
divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a and b are an
amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and
110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so
d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""
from itertools import ifilter
from util import sum_of_divisors


FOUND = set()


def is_amicable(a):
    """
    Determines if a number `a` has an amicable pair, defined by

    d(a) = b, where b is sum of divisors of a, where a != b such that d(b) = a
    """
    global FOUND

    if a in FOUND:
        return True

    b = sum_of_divisors(a)

    if b == a:
        return False

    if sum_of_divisors(b) == a:
        FOUND.update([a, b])
        return True

    return False


print sum(ifilter(is_amicable, xrange(10000)))
