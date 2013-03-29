'''
Find the largest prime factor of 600851475143

The prime factors of 13195 are 5, 7, 13 and 29
'''

import math
from itertools import ifilter
from util import is_prime, odd

value = 600851475143
stop = int(math.sqrt(value))
primes = set()


for n in ifilter(odd, xrange(3, stop)):
    if value % n == 0 and is_prime(n):
        primes.add(n)


print max(primes)
