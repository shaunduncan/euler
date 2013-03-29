'''
Find the sum of even fibonacci sequence numbers < 4,000,000
'''

from itertools import count, ifilter, imap, takewhile
from util import fib, even


until = lambda x: x < 4000000
print sum(takewhile(until, ifilter(even, imap(fib, count()))))
