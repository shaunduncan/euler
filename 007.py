'''
Find the 10001st prime

Not going to lie, my brain is much too far out of college
so I had to look up prime number checking
'''

from itertools import count, ifilter, dropwhile
from util import is_prime


found = 1  # We skip 2
for value in dropwhile(lambda y: y <= 1, ifilter(lambda x: x % 2, count())):
    if is_prime(value):
        found += 1

        if found == 10001:
            print value
            break
