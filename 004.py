'''
Find the largest palindrome made from the product of
two 3-digit integers
'''

from itertools import product, starmap, imap, ifilter
from operator import mul

start = 100
end = 1000

# The products of every three digit number
products = starmap(mul, product(xrange(start, end), repeat=2))

print max(imap(int, ifilter(lambda x: x == x[::-1], imap(str, products))))
