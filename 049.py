'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
increases by 3330, is unusual in two ways: (i) each of the three terms
are prime, and, (ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''

from itertools import ifilter, imap, permutations, combinations
from util import is_prime, odd

primes = list(ifilter(is_prime, ifilter(odd, xrange(1000, 10000))))
solutions = set()

in_primes = lambda x: x in primes

for prime in primes:
    # Find all permutations > 1000 that aren't the current prime and are
    # indeed prime themselves. Collect as a set to deal with uniques.
    # Yes. This is messy.
    others = set(ifilter(lambda x: x > 1000 and x != prime and x in primes,
                         imap(lambda x: int(''.join(x)), permutations(str(prime), 4))))

    # Need at least two
    if len(others) < 2:
        continue

    for a, b in combinations(others, 2):
        coll = sorted([prime, a, b])
        avg = sum(coll) / 3

        # Equidistant numbers will yield the middle value as the average
        if avg in coll:
            solutions.add(''.join(map(str, coll)))

print '\n'.join(solutions)
