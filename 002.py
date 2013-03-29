'''
Find the sum of even fibonacci sequence numbers < 4,000,000
'''

from itertools import count, ifilterfalse, imap, takewhile
from util import fib


even = lambda x: x % 2
until = lambda x: x < 4000000
print sum(takewhile(until, ifilterfalse(even, imap(fib, count()))))
