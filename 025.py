'''
Find the first Fibonacci number with 1000 digits
Find the sum of even fibonacci sequence numbers < 4,000,000
'''

from itertools import count, imap
from util import fib


for i, fibnum in enumerate(imap(fib, count())):
    if len(str(fibnum)) >= 1000:
        print i
        break
