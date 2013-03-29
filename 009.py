'''
Pythagorean triplets are three natural numbers of the form:

    a^2 + b^2 = c^2

where a < b < c (i.e. 3, 4, 5)

Find the one Pythagorean triplet where a + b + c = 1000. Return
the product of a, b, and c
'''

import math
import sys

target = 1000

# This is a brute force
for c in xrange(target):
    csq = c ** 2
    for b in xrange(4, c):
        bsq = b ** 2
        for a in xrange(3, b):
            asq = a ** 2
            if asq + bsq == csq and a + b + c == target:
                print a * b * c
                sys.exit(0)
