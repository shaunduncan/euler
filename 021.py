from itertools import ifilter


MAX = 10000
FOUND = set()


def divsum(n):
    """
    Find the sum of divisors from [1,n). Note that this will include 1, but not n.
    Repeatedly lower the top-end limit as a divisor is found
    """
    nums = [1]
    limit = n
    i = 2

    while i < limit:
        if n % i == 0:
            limit = n / i
            nums.extend([i, limit])
        i += 1

    return sum(nums)


def is_amicable(a):
    """
    Determines if a number `a` has an amicable pair, defined by

    d(a) = b, where b is sum of divisors of a, where a != b such that d(b) = a
    """
    global FOUND

    if a in FOUND:
        return True

    b = divsum(a)

    if b == a:
        return False

    if divsum(b) == a:
        FOUND.update([a, b])
        return True

    return False


print sum(ifilter(is_amicable, xrange(MAX)))
