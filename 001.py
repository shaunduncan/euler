'''
Find the sum of all multiples of 3 and 5 below 1000
'''

from itertools import ifilter

print sum(ifilter(lambda x: x % 3 == 0 or x % 5 == 0, xrange(1000)))
