'''
Find sum of primes < 2,000,000
'''

from itertools import ifilter
from util import is_prime


# Need to add 2, since we ignore it
print sum(ifilter(is_prime, ifilter(lambda x: x % 2, xrange(2, 2000000)))) + 2
