'''
Find the number < 1000000 that produces the longest chain of Collatz
numbers where collatz(n) is:

    if even(n): n / 2
    if odd(n): 3n + 1
'''

from util import collatz


longest = 0
cnum = 0

for n in xrange(2, 1000000):
    path = 1
    c = collatz(n)

    while c != 1:
        path += 1
        c = collatz(c)

    if path + 1 > longest:
        cnum = n
        longest = path + 1

print cnum
